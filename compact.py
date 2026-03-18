import re

print("Reading data.js...")
with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()

print(f"File size: {len(content)/1024/1024:.1f} MB")

# Find all unique idea objects by id - one per line format
idea_lines = {}
for m in re.finditer(r',?\{id:"([^"]+)",[^\n]+\}', content):
    id_val = m.group(1)
    if id_val not in idea_lines:
        obj = m.group(0).lstrip(',')  # strip leading comma
        idea_lines[id_val] = obj

print(f"Unique ideas found: {len(idea_lines)}")

# Rebuild: first idea has no leading comma, rest have commas
header = "// data.js - Mapzimus master idea database\nconst D =[\n"
lines = list(idea_lines.values())
# First idea: no comma. All others: comma prefix
parts = [lines[0]] + [',' + l for l in lines[1:]]
clean = header + '\n'.join(parts) + '\n]; // end D\n'

print(f"Clean file size: {len(clean)/1024/1024:.1f} MB")
print(f"Ideas in clean file: {len(re.findall(chr(123)+'id:', clean))}")
print(f"First chars after [: {repr(clean[clean.find('['):clean.find('[')+15])}")

with open('data.js', 'w', encoding='utf-8') as f:
    f.write(clean)
print("Written.")
