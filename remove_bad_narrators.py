"""
Remove md() narrator cells incorrectly inserted after section-header md() cells.
Pattern: section-header md() ending -> blank lines -> short narrator md() -> blank lines -> code()
Remove the short narrator md() and the blank lines before it.
"""

import re

with open('generate_lab_notebooks.py') as f:
    lines = f.readlines()

# State machine: track section-header md() endings
# A section-header md() is one whose body contains ---/## Part/## Question/~N min
# A bad narrator md() is: single-line body (plain sentence, no markdown syntax)

# Pass through lines, tracking state
# When we see a section-header md() close, check if next non-blank is a short narrator md()
# If so, skip it and the blanks before it

def is_section_header_body(body_lines):
    text = ' '.join(body_lines)
    return bool(re.search(r'(^---$|## Part|## Question|## Does|## Phase|~\d+ min)', text, re.MULTILINE))

def is_short_narrator(body_lines):
    if len(body_lines) != 1:
        return False
    body = body_lines[0].strip()
    # Must be plain text (not markdown)
    if re.match(r'^(#|>|\*|-{3}|✏️|\||\*\*)', body):
        return False
    # Must end with sentence-ending punctuation
    if not re.search(r'[.?]$', body):
        return False
    # Must be short (< 120 chars)
    return len(body) < 120

# First, parse out md() blocks with their line ranges and bodies
md_blocks = []  # (start_line_idx, end_line_idx, body_lines)
i = 0
while i < len(lines):
    if re.match(r'\s+md\("""\\\s*$', lines[i]) or re.match(r'\s+md\("""\s*$', lines[i]):
        start = i
        body = []
        i += 1
        while i < len(lines):
            stripped = lines[i].rstrip()
            if stripped.endswith('"""),') or stripped.endswith('"""])') or stripped.endswith('""")'):
                # Closing line - extract any text before the closing """
                text_before = re.sub(r'"""\)[,\]]?\s*$', '', stripped).strip()
                if text_before:
                    body.append(text_before)
                md_blocks.append((start, i, body))
                i += 1
                break
            else:
                body.append(stripped)
                i += 1
    else:
        i += 1

# Find bad narrator blocks: those that follow a section-header md()
lines_to_skip = set()

for idx in range(len(md_blocks) - 1):
    curr_start, curr_end, curr_body = md_blocks[idx]
    next_start, next_end, next_body = md_blocks[idx + 1]

    # Check if they're close (only blank lines between curr_end and next_start)
    between = lines[curr_end + 1 : next_start]
    if not all(l.strip() == '' for l in between):
        continue  # Non-blank content between them — not a direct consecutive pair

    if is_section_header_body(curr_body) and is_short_narrator(next_body):
        # Mark the narrator md() and the blank lines before it for removal
        for k in range(curr_end + 1, next_end + 1):
            lines_to_skip.add(k)
        # Also remove blank line(s) after the narrator (before the next code block)
        k = next_end + 1
        while k < len(lines) and lines[k].strip() == '':
            lines_to_skip.add(k)
            k += 1
        # Keep one blank line (put it back effectively by NOT skipping curr_end+1)
        # Actually we want: after the section header, just one blank line then code/next
        # Let's keep the blank line right after the section header
        if curr_end + 1 in lines_to_skip:
            lines_to_skip.discard(curr_end + 1)

removed = len([l for l in lines_to_skip if re.match(r'\s+md\("""\\\s*$', lines[l]) or re.match(r'\s+md\("""\s*$', lines[l])])
print(f"Removing {removed} bad narrator md() cells (plus surrounding blank lines)")

output = [line for i, line in enumerate(lines) if i not in lines_to_skip]

with open('generate_lab_notebooks.py', 'w') as f:
    f.writelines(output)

print("Done.")
