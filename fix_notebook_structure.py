"""
Transforms generate_lab_notebooks.py:
1. Splits code cells that mix calculation + plotting at '# Plot' lines
2. Inserts brief md() narrators between consecutive code() blocks
"""

import re

with open('generate_lab_notebooks.py') as f:
    lines = f.readlines()

output = []
i = 0

def extract_section_label(lines_slice):
    """Get the first # comment from a block for narration."""
    for ln in lines_slice:
        m = re.match(r'\s*#\s*([A-Z0-9]\.\d+)\s*[—\-–]+\s*(.+)', ln)
        if m:
            return m.group(2).strip().rstrip('.')
        m2 = re.match(r'\s*#\s*(.{10,60})', ln)
        if m2 and not m2.group(1).startswith('!'):
            return m2.group(1).strip().rstrip('.')
    return None

def make_narrator(desc):
    if not desc:
        return "Run the next cell."
    d = desc.strip()
    d = re.sub(r'^[A-Z0-9]\.\d+\s*[—\-–]+\s*', '', d).strip()
    if not d:
        return "Run the next cell."
    return d[0].upper() + d[1:] + ('.' if not d.endswith('.') else '')

# ── Pass 1: split code blocks at '# Plot' lines ────────────────────────────
# State machine: track whether we're inside a code("""\...""") block
in_code_block = False
code_block_start = None  # line index where code("""\  appears
plot_split_idx  = None   # line inside block that starts with # Plot/# Visualis

new_lines = []
i = 0
while i < len(lines):
    line = lines[i]

    if not in_code_block:
        # Detect opening of a code block: '        code("""\'
        if re.match(r'\s+code\("""\\\s*$', line):
            in_code_block = True
            code_block_start = len(new_lines)
            plot_split_idx = None
        new_lines.append(line)
    else:
        # We're inside a code block
        # Check for the closing '""")'  or '"""]'
        stripped = line.rstrip()
        if stripped.endswith('"""),') or stripped.endswith('"""])') or stripped.endswith('""")'):
            # End of code block
            if plot_split_idx is not None:
                # Split: everything from block start to split goes in first cell,
                # then md(), then plot portion in second cell
                # Find the indentation of the code() call
                open_line = new_lines[code_block_start]
                indent = len(open_line) - len(open_line.lstrip())
                ind = ' ' * indent

                # Collect block lines so far (after the opening line)
                # new_lines[code_block_start] is the 'code("""\' line
                # new_lines[code_block_start+1 .. plot_split_idx-1] = calc portion
                # new_lines[plot_split_idx .. ] = plot portion (not yet in new_lines, still in lines[])
                # Actually plot_split_idx refers to an index into new_lines

                calc_lines = new_lines[code_block_start+1 : plot_split_idx]
                plot_lines_so_far = new_lines[plot_split_idx:]
                # pop back to just before the calc portion
                del new_lines[code_block_start+1:]

                # End the first (calc) code block
                # Remove trailing blank lines from calc
                while calc_lines and calc_lines[-1].strip() == '':
                    calc_lines.pop()
                for cl in calc_lines:
                    new_lines.append(cl)
                new_lines.append(f'{ind}"""),\n')

                # Get narration from plot header
                plot_header = plot_lines_so_far[0] if plot_lines_so_far else ''
                desc = plot_header.strip().lstrip('# ').rstrip(':').strip()
                if desc.lower().startswith('plot'):
                    narration = 'The chart below ' + desc[4:].strip().lower() + '.'
                elif desc:
                    narration = 'The chart below ' + desc[0].lower() + desc[1:].rstrip('.') + '.'
                else:
                    narration = 'The chart below visualises the results.'

                new_lines.append('\n')
                new_lines.append(f'{ind}md("""\\\n')
                new_lines.append(f'{narration}"""),\n')
                new_lines.append('\n')

                # Start the second (plot) code block
                new_lines.append(f'{ind}code("""\\\n')
                for pl in plot_lines_so_far:
                    new_lines.append(pl)

            # Append the closing line (with plt.show() or just """),)
            new_lines.append(line)
            in_code_block = False
            plot_split_idx = None

        elif re.match(r'# (?:Plot|Visualis|plot|visualis|Compare plot|Overlay)', line.lstrip()):
            # This is a plot-section comment — mark split point
            if plot_split_idx is None:
                plot_split_idx = len(new_lines)
            new_lines.append(line)
        else:
            new_lines.append(line)

    i += 1

lines = new_lines
print(f"Pass 1 (calc+plot splits): {len([l for l in lines if 'md(\"\"\"' in l and 'chart below' in l])} splits inserted")

# ── Pass 2: insert md() between consecutive code() blocks ──────────────────
# Find pairs:  '"""),\n' (end of code block) followed by blank lines then '        code("""\
output2 = []
i = 0
while i < len(lines):
    output2.append(lines[i])
    line = lines[i].rstrip()

    # Detect end of a code block
    if (line.endswith('"""),') or line.endswith('"""])')) and i > 0:
        # Look ahead past blank lines for the next non-blank line
        j = i + 1
        while j < len(lines) and lines[j].strip() == '':
            j += 1
        if j < len(lines) and re.match(r'\s+code\("""\\\s*$', lines[j]):
            # Next non-blank line is another code() block — insert md() narrator
            # But first check there's no md() already in between
            between = ''.join(lines[i+1:j])
            if 'md(' not in between:
                # Peek into the next code block to get a description
                next_block_lines = []
                k = j + 1
                while k < len(lines):
                    nl = lines[k].rstrip()
                    if nl.endswith('"""),') or nl.endswith('"""])'):
                        next_block_lines.append(lines[k])
                        break
                    next_block_lines.append(lines[k])
                    k += 1

                desc = extract_section_label(next_block_lines)
                narration = make_narrator(desc)

                indent = len(lines[j]) - len(lines[j].lstrip())
                ind = ' ' * indent

                # Add blank line + md() + blank line before the next code block
                output2.append('\n')
                output2.append(f'{ind}md("""\\\n')
                output2.append(f'{narration}"""),\n')
    i += 1

n_md_inserted = sum(1 for l in output2 if 'md("""' in l) - sum(1 for l in lines if 'md("""' in l)
print(f"Pass 2 (consecutive code narrators): {n_md_inserted} md() cells inserted")

with open('generate_lab_notebooks.py', 'w') as f:
    f.writelines(output2)

print("Done.")
