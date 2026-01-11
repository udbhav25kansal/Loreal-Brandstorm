#!/usr/bin/env python3
"""
Integrate complete content for documents 6, 7, and 8-13 into index.html
"""

def main():
    print("Reading index.html...")
    with open('index.html', 'r', encoding='utf-8') as f:
        html_lines = f.readlines()

    print("Reading complete content file...")
    with open('ALL_SECTIONS_6_to_13_COMPLETE.html', 'r', encoding='utf-8') as f:
        new_content = f.read()

    print("Reading new navigation...")
    with open('updated_navigation_structure.html', 'r', encoding='utf-8') as f:
        nav_content = f.read()

    # Extract just the nav-menu section from the navigation file
    nav_start = nav_content.find('<nav class="nav-menu">')
    nav_end = nav_content.find('</nav>', nav_start) + 6
    new_nav = nav_content[nav_start:nav_end]

    # Find and replace navigation (lines 383-391)
    nav_start_line = None
    nav_end_line = None
    for i, line in enumerate(html_lines):
        if '<div class="nav-menu">' in line:
            nav_start_line = i
        if nav_start_line and '</div>' in line and i > nav_start_line:
            nav_end_line = i + 1
            break

    if nav_start_line and nav_end_line:
        print(f"Replacing navigation (lines {nav_start_line+1}-{nav_end_line})...")
        # Replace old nav with new nav (adjust indentation)
        new_nav_indented = '\n'.join(['        ' + line if line.strip() else line
                                       for line in new_nav.split('\n')])
        html_lines[nav_start_line:nav_end_line] = [new_nav_indented + '\n']

    # Find doc6 section start
    doc6_start = None
    for i, line in enumerate(html_lines):
        if 'id="doc6"' in line and 'section' in line:
            doc6_start = i
            break

    # Find doc7 section end
    doc7_end = None
    if doc6_start:
        for i in range(doc6_start, len(html_lines)):
            if 'id="doc7"' in html_lines[i]:
                # Find the closing </section> for doc7
                for j in range(i, len(html_lines)):
                    if '</section>' in html_lines[j]:
                        doc7_end = j + 1
                        break
                break

    if doc6_start and doc7_end:
        print(f"Replacing documents 6 & 7 (lines {doc6_start+1}-{doc7_end}) with complete content...")
        # Add proper indentation to new content (8 spaces for sections inside main-content)
        new_content_indented = '\n'.join(['        ' + line if line.strip() and not line.startswith('<') else line
                                          for line in new_content.split('\n')])

        # Replace old sections with new complete content
        html_lines[doc6_start:doc7_end] = [new_content_indented + '\n']

    # Also need to add the CSS for navigation sections
    # Find the style section
    style_end = None
    for i, line in enumerate(html_lines):
        if '</style>' in line:
            style_end = i
            break

    if style_end:
        # Add navigation section CSS before </style>
        nav_css = '''
        .nav-section {
            margin-bottom: 30px;
        }

        .nav-section-header {
            padding: 12px 25px;
            font-size: 11px;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 1.5px;
            color: var(--secondary-color);
            border-bottom: 1px solid rgba(201, 169, 97, 0.2);
            margin-bottom: 10px;
        }

        /* Highlight winner analyses */
        .nav-item[href="#doc10"],
        .nav-item[href="#doc11"],
        .nav-item[href="#doc12"] {
            background: rgba(201, 169, 97, 0.05);
        }

        .nav-item[href="#doc10"]:before,
        .nav-item[href="#doc11"]:before,
        .nav-item[href="#doc12"]:before {
            content: "🏆 ";
            margin-right: 6px;
        }
'''
        html_lines.insert(style_end, nav_css)

    # Write updated HTML
    print("Writing updated index.html...")
    with open('index.html', 'w', encoding='utf-8') as f:
        f.writelines(html_lines)

    print("\n" + "="*60)
    print("SUCCESS! Integration complete.")
    print("="*60)
    print("\nWhat was updated:")
    print("1. Navigation now shows all 13 documents in 3 sections")
    print("2. Document 6: Full Judging Criteria (250-point framework)")
    print("3. Document 7: Full Winning Blueprint (5-phase roadmap)")
    print("4. Documents 8-13: Complete presentation analysis")
    print("\nOpen index.html in your browser to view the complete site!")
    print("="*60)

if __name__ == '__main__':
    main()
