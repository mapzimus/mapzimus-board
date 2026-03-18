import re

print("Reading data.js...")
with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()

print(f"File size: {len(content)/1024/1024:.1f} MB")

# Find all unique idea objects by id
# Each idea is: ,{id:"...",title:...} on a single line
idea_lines = {}
count = 0
for m in re.finditer(r',?\{id:"([^"]+)",[^\n]+\}', content):
    id_val = m.group(1)
    if id_val not in idea_lines:
        idea_lines[id_val] = m.group(0)
        count += 1

print(f"Unique ideas found: {count}")

# Get the header (const D = [)
header = "// data.js - Mapzimus master idea database\nconst D =[\n"

# Rebuild clean file - one idea per line, no extra whitespace
lines = []
for id_val, obj in idea_lines.items():
    # Ensure starts with comma
    obj = obj.strip()
    if not obj.startswith(','):
        obj = ',' + obj
    lines.append(obj)

clean = header + '\n'.join(lines) + '\n]; // end D\n'
print(f"Clean file size: {len(clean)/1024/1024:.1f} MB")
print(f"Ideas in clean file: {len(re.findall(chr(123)+'id:', clean))}")

with open('data.js', 'w', encoding='utf-8') as f:
    f.write(clean)
print("Written.")
