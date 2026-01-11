#!/usr/bin/env python3
"""
Convert markdown documents 6 and 7 to complete HTML sections
"""

import re

def convert_markdown_to_html(md_content, doc_id):
    """Convert markdown content to HTML"""
    html_lines = []

    # Start section
    html_lines.append(f'<section id="{doc_id}" class="document-section">')

    in_code_block = False
    in_list = False
    in_table = False
    table_rows = []

    lines = md_content.split('\n')
    i = 0

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # Skip empty lines outside of special blocks
        if not stripped and not in_code_block:
            if in_list:
                html_lines.append('</ul>')
                in_list = False
            elif in_table:
                # Process table
                html_lines.append('<table class="scoring-table">')
                for row_idx, row in enumerate(table_rows):
                    if row_idx == 0:
                        html_lines.append('<thead><tr>')
                        for cell in row:
                            html_lines.append(f'<th>{escape_html(cell)}</th>')
                        html_lines.append('</tr></thead>')
                    elif row_idx == 1 and all(set(cell.strip()) <= {'-', '|', ':'} for cell in row):
                        # Skip separator row
                        if row_idx == 1:
                            html_lines.append('<tbody>')
                    else:
                        html_lines.append('<tr>')
                        for cell in row:
                            html_lines.append(f'<td>{escape_html(cell)}</td>')
                        html_lines.append('</tr>')
                if len(table_rows) > 1:
                    html_lines.append('</tbody>')
                html_lines.append('</table>')
                in_table = False
                table_rows = []
            html_lines.append('<br>')
            i += 1
            continue

        # Code blocks
        if stripped.startswith('```'):
            if not in_code_block:
                html_lines.append('<div class="example-box"><pre><code>')
                in_code_block = True
            else:
                html_lines.append('</code></pre></div>')
                in_code_block = False
            i += 1
            continue

        if in_code_block:
            html_lines.append(escape_html(line))
            i += 1
            continue

        # Headers
        if stripped.startswith('#'):
            if in_list:
                html_lines.append('</ul>')
                in_list = False

            level = len(stripped) - len(stripped.lstrip('#'))
            text = stripped.lstrip('#').strip()

            if level == 1:
                html_lines.append(f'<div class="tier-header"><h2>{escape_html(text)}</h2></div>')
            elif level == 2:
                html_lines.append(f'<h3>{escape_html(text)}</h3>')
            elif level == 3:
                html_lines.append(f'<h4>{escape_html(text)}</h4>')
            else:
                html_lines.append(f'<h5>{escape_html(text)}</h5>')
            i += 1
            continue

        # Tables
        if '|' in stripped and not in_table:
            in_table = True
            table_rows = []

        if in_table:
            if '|' in stripped:
                cells = [cell.strip() for cell in stripped.split('|')[1:-1]]
                table_rows.append(cells)
                i += 1
                continue
            else:
                # End of table
                html_lines.append('<table class="scoring-table">')
                for row_idx, row in enumerate(table_rows):
                    if row_idx == 0:
                        html_lines.append('<thead><tr>')
                        for cell in row:
                            html_lines.append(f'<th>{escape_html(cell)}</th>')
                        html_lines.append('</tr></thead><tbody>')
                    elif row_idx == 1 and all(set(cell.strip()) <= {'-', '|', ':', ' '} for cell in row):
                        # Skip separator row
                        pass
                    else:
                        html_lines.append('<tr>')
                        for cell in row:
                            html_lines.append(f'<td>{escape_html(cell)}</td>')
                        html_lines.append('</tr>')
                html_lines.append('</tbody></table>')
                in_table = False
                table_rows = []
                continue

        # Horizontal rules
        if stripped.startswith('---') or stripped.startswith('***'):
            if in_list:
                html_lines.append('</ul>')
                in_list = False
            html_lines.append('<hr>')
            i += 1
            continue

        # Lists
        if stripped.startswith('- ') or stripped.startswith('* ') or stripped.startswith('+ '):
            if not in_list:
                html_lines.append('<ul>')
                in_list = True
            text = stripped[2:].strip()
            html_lines.append(f'<li>{format_inline(text)}</li>')
            i += 1
            continue

        # Numbered lists
        if re.match(r'^\d+\.', stripped):
            text = re.sub(r'^\d+\.\s*', '', stripped)
            html_lines.append(f'<li>{format_inline(text)}</li>')
            i += 1
            continue

        # Special formatting blocks
        if stripped.startswith('**') and stripped.endswith('**') and len(stripped) > 4:
            if in_list:
                html_lines.append('</ul>')
                in_list = False
            text = stripped.strip('*').strip()
            if ':' in text:
                # Likely a scoring rubric or criterion
                html_lines.append(f'<div class="rubric-level"><strong>{escape_html(text)}</strong>')
                i += 1
                # Collect following lines until next header or empty line
                while i < len(lines) and lines[i].strip() and not lines[i].strip().startswith('#') and not lines[i].strip().startswith('**'):
                    i += 1
                    content_line = lines[i-1].strip()
                    if content_line.startswith('- '):
                        if '</div>' not in html_lines[-1]:
                            html_lines.append('<ul>')
                        html_lines.append(f'<li>{format_inline(content_line[2:])}</li>')
                    else:
                        html_lines.append(f'<p>{format_inline(content_line)}</p>')
                if '<ul>' in ''.join(html_lines[-5:]):
                    html_lines.append('</ul>')
                html_lines.append('</div>')
                continue
            else:
                html_lines.append(f'<p><strong>{escape_html(text)}</strong></p>')

        # Regular paragraphs
        else:
            if in_list and not stripped.startswith('  '):
                html_lines.append('</ul>')
                in_list = False

            if stripped:
                # Check if it's a question or special box
                if stripped.startswith('**Questions'):
                    html_lines.append(f'<div class="assessment-questions">')
                    html_lines.append(f'<p><strong>{format_inline(stripped)}</strong></p>')
                    i += 1
                    while i < len(lines) and lines[i].strip() and not lines[i].strip().startswith('#'):
                        html_lines.append(f'<p>{format_inline(lines[i].strip())}</p>')
                        i += 1
                    html_lines.append('</div>')
                    continue
                elif stripped.startswith('**Example'):
                    html_lines.append(f'<div class="example-box">')
                    html_lines.append(f'<p><strong>{format_inline(stripped)}</strong></p>')
                    i += 1
                    while i < len(lines) and lines[i].strip() and not lines[i].strip().startswith('#') and not lines[i].strip().startswith('**'):
                        html_lines.append(f'<p>{format_inline(lines[i].strip())}</p>')
                        i += 1
                    html_lines.append('</div>')
                    continue
                else:
                    html_lines.append(f'<p>{format_inline(stripped)}</p>')

        i += 1

    # Close any open tags
    if in_list:
        html_lines.append('</ul>')
    if in_table:
        html_lines.append('</tbody></table>')

    html_lines.append('</section>')

    return '\n'.join(html_lines)

def format_inline(text):
    """Format inline markdown elements"""
    # Bold
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    # Italic
    text = re.sub(r'\*(.+?)\*', r'<em>\1</em>', text)
    # Code
    text = re.sub(r'`(.+?)`', r'<code>\1</code>', text)
    # Links
    text = re.sub(r'\[(.+?)\]\((.+?)\)', r'<a href="\2">\1</a>', text)

    return escape_html_selective(text)

def escape_html(text):
    """Escape HTML special characters"""
    return (text
            .replace('&', '&amp;')
            .replace('<', '&lt;')
            .replace('>', '&gt;')
            .replace('"', '&quot;')
            .replace("'", '&#39;'))

def escape_html_selective(text):
    """Escape HTML but preserve already formatted tags"""
    # Don't escape if we already have HTML tags
    if '<strong>' in text or '<em>' in text or '<code>' in text or '<a href=' in text:
        return text
    return escape_html(text)

def main():
    # Read document 6
    print("Reading document 6...")
    with open('06_JUDGING_CRITERIA_EVALUATION_SYSTEM.md', 'r', encoding='utf-8') as f:
        doc6_content = f.read()

    # Read document 7
    print("Reading document 7...")
    with open('07_WINNING_PROJECT_BLUEPRINT.md', 'r', encoding='utf-8') as f:
        doc7_content = f.read()

    print("Converting document 6 to HTML...")
    doc6_html = convert_markdown_to_html(doc6_content, 'doc6')

    print("Converting document 7 to HTML...")
    doc7_html = convert_markdown_to_html(doc7_content, 'doc7')

    # Add CSS
    css = '''<style>
/* Document 6 & 7 Styling */
.scoring-table {
    width: 100%;
    border-collapse: collapse;
    margin: 20px 0;
    background: white;
}

.scoring-table th {
    background: #1a1a1a;
    color: #c9a961;
    padding: 12px;
    text-align: left;
    font-weight: 600;
}

.scoring-table td {
    padding: 12px;
    border: 1px solid #e0e0e0;
}

.scoring-table tr:hover {
    background: #f9f9f9;
}

.rubric-level {
    background: #f5f5f5;
    padding: 15px;
    margin: 15px 0;
    border-left: 4px solid #c9a961;
}

.assessment-questions {
    background: #fff9e6;
    padding: 15px;
    margin: 15px 0;
    border-radius: 5px;
}

.example-box {
    background: #f0f8ff;
    padding: 15px;
    margin: 15px 0;
    border-left: 4px solid #4a90e2;
}

.tier-header {
    background: linear-gradient(135deg, #1a1a1a 0%, #3a3a3a 100%);
    color: #c9a961;
    padding: 20px;
    margin: 30px 0 20px 0;
    border-radius: 8px;
}

.scorecard {
    background: #f9f9f9;
    padding: 20px;
    margin: 25px 0;
    border: 2px solid #c9a961;
    border-radius: 8px;
}

.checklist-item {
    padding: 8px 0;
    border-bottom: 1px solid #e0e0e0;
}

.phase-header {
    background: #c9a961;
    color: white;
    padding: 15px 20px;
    margin: 30px 0 15px 0;
    border-radius: 5px;
    font-size: 1.3em;
    font-weight: 600;
}

.playbook-box {
    background: #fff;
    border: 2px solid #c9a961;
    padding: 20px;
    margin: 20px 0;
    border-radius: 8px;
}

.strategy-table {
    width: 100%;
    margin: 20px 0;
    border-collapse: collapse;
}

.strategy-table th {
    background: #c9a961;
    color: white;
    padding: 10px;
    text-align: left;
}

.strategy-table td {
    padding: 10px;
    border: 1px solid #ddd;
    vertical-align: top;
}

.warning-box {
    background: #fff3cd;
    border-left: 4px solid #ffc107;
    padding: 15px;
    margin: 15px 0;
}

.success-box {
    background: #d4edda;
    border-left: 4px solid #28a745;
    padding: 15px;
    margin: 15px 0;
}
</style>

'''

    # Combine everything
    print("Creating combined HTML file...")
    output = css + '\n\n' + doc6_html + '\n\n' + doc7_html

    with open('docs_6_and_7_COMPLETE.html', 'w', encoding='utf-8') as f:
        f.write(output)

    print(f"[OK] Created docs_6_and_7_COMPLETE.html ({len(output)} characters)")
    print(f"[OK] Document 6 HTML: {len(doc6_html)} characters")
    print(f"[OK] Document 7 HTML: {len(doc7_html)} characters")
    print("\nDone! File ready for integration into index.html")

if __name__ == '__main__':
    main()
