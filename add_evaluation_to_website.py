import re

# Read the evaluation markdown
with open('MEMOIR_CONCEPT_EVALUATION.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Read the current index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

# Convert markdown to HTML
def markdown_to_html(md_text):
    """Convert markdown to HTML with proper styling"""

    # Convert headers
    md_text = re.sub(r'^# (.+)$', r'<h1>\1</h1>', md_text, flags=re.MULTILINE)
    md_text = re.sub(r'^## (.+)$', r'<h2>\1</h2>', md_text, flags=re.MULTILINE)
    md_text = re.sub(r'^### (.+)$', r'<h3>\1</h3>', md_text, flags=re.MULTILINE)
    md_text = re.sub(r'^#### (.+)$', r'<h4>\1</h4>', md_text, flags=re.MULTILINE)

    # Convert bold text
    md_text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', md_text)

    # Convert lists
    md_text = re.sub(r'^- (.+)$', r'<li>\1</li>', md_text, flags=re.MULTILINE)
    md_text = re.sub(r'^✅ (.+)$', r'<li class="check">✅ \1</li>', md_text, flags=re.MULTILINE)
    md_text = re.sub(r'^⚠️ (.+)$', r'<li class="warning">⚠️ \1</li>', md_text, flags=re.MULTILINE)

    # Convert blockquotes
    md_text = re.sub(r'^> (.+)$', r'<blockquote>\1</blockquote>', md_text, flags=re.MULTILINE)

    # Convert horizontal rules
    md_text = re.sub(r'^---$', r'<hr>', md_text, flags=re.MULTILINE)

    # Convert tables (simple approach)
    def convert_table(match):
        table_text = match.group(0)
        lines = table_text.strip().split('\n')

        if len(lines) < 3:
            return table_text

        # Parse header
        headers = [cell.strip() for cell in lines[0].split('|')[1:-1]]

        # Parse rows (skip separator line)
        rows = []
        for line in lines[2:]:
            cells = [cell.strip() for cell in line.split('|')[1:-1]]
            if cells:
                rows.append(cells)

        # Build HTML table
        html = '<table class="evaluation-table">\n<thead>\n<tr>\n'
        for header in headers:
            html += f'<th>{header}</th>\n'
        html += '</tr>\n</thead>\n<tbody>\n'

        for row in rows:
            html += '<tr>\n'
            for cell in row:
                html += f'<td>{cell}</td>\n'
            html += '</tr>\n'

        html += '</tbody>\n</table>'
        return html

    # Match tables
    md_text = re.sub(r'\|.+\|[\r\n]+\|[-:\s|]+\|[\r\n]+(?:\|.+\|[\r\n]+)+', convert_table, md_text)

    # Wrap bare text in paragraphs
    lines = md_text.split('\n')
    result = []
    in_list = False
    in_table = False

    for line in lines:
        stripped = line.strip()

        # Check if we're in a table
        if '<table' in stripped:
            in_table = True
        elif '</table>' in stripped:
            in_table = False
            result.append(line)
            continue

        # Check if we're in a list
        if stripped.startswith('<li>'):
            if not in_list:
                result.append('<ul>')
                in_list = True
        elif in_list and not stripped.startswith('<li>'):
            result.append('</ul>')
            in_list = False

        # Add the line
        if stripped and not stripped.startswith('<') and not in_table:
            result.append(f'<p>{line}</p>')
        else:
            result.append(line)

    if in_list:
        result.append('</ul>')

    return '\n'.join(result)

# Convert evaluation content
html_evaluation = markdown_to_html(content)

# Create the evaluation section HTML
evaluation_section = f'''
        <!-- Document 24: MEMOIR Concept Evaluation -->
        <section id="doc24" class="document-section">
            {html_evaluation}
        </section>
'''

# Find where to insert (before the closing </main> tag)
insert_position = html_content.rfind('</main>')

if insert_position == -1:
    print("Error: Could not find </main> tag in index.html")
else:
    # Insert the evaluation section
    new_html = html_content[:insert_position] + evaluation_section + html_content[insert_position:]

    # Update navigation - find the MEMOIR CONCEPT section and add the evaluation link
    nav_insert = new_html.find('<a href="#doc23" class="nav-item">23. Video Script & Q&A Defense</a>')

    if nav_insert != -1:
        nav_link = '\n                <a href="#doc24" class="nav-item">24. Concept Evaluation (94.75%)</a>'
        # Find the end of this line
        line_end = new_html.find('\n', nav_insert)
        new_html = new_html[:line_end] + nav_link + new_html[line_end:]

    # Add custom CSS for evaluation styling
    css_insert = new_html.find('</style>')
    if css_insert != -1:
        evaluation_css = '''
        /* Evaluation-specific styles */
        .evaluation-table {
            width: 100%;
            border-collapse: collapse;
            margin: 25px 0;
            font-size: 14px;
            background-color: white;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
        }

        .evaluation-table thead tr {
            background-color: var(--primary-color);
            color: white;
            text-align: left;
            font-weight: 600;
        }

        .evaluation-table th,
        .evaluation-table td {
            padding: 14px 18px;
            border: 1px solid var(--border-color);
        }

        .evaluation-table tbody tr {
            border-bottom: 1px solid var(--border-color);
        }

        .evaluation-table tbody tr:nth-of-type(even) {
            background-color: var(--light-gray);
        }

        .evaluation-table tbody tr:hover {
            background-color: rgba(201, 169, 97, 0.1);
        }

        ul li.check {
            color: #28a745;
        }

        ul li.warning {
            color: #ffc107;
        }

        .document-section h1 {
            color: var(--primary-color);
            border-bottom: 3px solid var(--secondary-color);
            padding-bottom: 15px;
            margin-bottom: 30px;
        }

        .document-section h2 {
            color: var(--accent-color);
            margin-top: 40px;
            margin-bottom: 20px;
            padding-left: 10px;
            border-left: 4px solid var(--secondary-color);
        }

        .document-section h3 {
            color: var(--text-color);
            margin-top: 30px;
            margin-bottom: 15px;
        }

        '''
        new_html = new_html[:css_insert] + evaluation_css + new_html[css_insert:]

    # Write the updated HTML
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_html)

    print("SUCCESS: Evaluation section successfully added to index.html")
    print("SUCCESS: Navigation updated with link to Document 24")
    print("SUCCESS: Custom styling added for evaluation tables and content")
