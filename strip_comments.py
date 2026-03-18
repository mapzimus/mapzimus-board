import re

with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()

original_len = len(content)

# Remove all // comment lines that appear between array elements
# These are lines that start with optional whitespace then //
# We must NOT remove comments inside strings (they're fine)
# Safe approach: remove lines that are ONLY a comment (nothing else on the line)

lines = content.split('\n')
cleaned = []
removed = 0

for line in lines:
    stripped = line.strip()
    # Remove lines that are purely a comment (start with //)
    # but keep them if they're part of object fields (would be inside quotes)
    if stripped.startswith('//') and not stripped.startswith('//ext') and not stripped.startswith('//vars'):
        removed += 1
        # Replace with empty line to avoid joining problems
        cleaned.append('')
    else:
        cleaned.append(line)

content = '\n'.join(cleaned)

# Collapse runs of 3+ blank lines to just 1
content = re.sub(r'\n{4,}', '\n\n', content)

with open('data.js', 'w', encoding='utf-8') as f:
    f.write(content)

print(f'Removed {removed} comment lines')
print(f'Original size: {original_len:,} chars')
print(f'New size: {len(content):,} chars')
