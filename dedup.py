import re

with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Find duplicate IDs using raw text scan
ids_positions = {}
for m in re.finditer(r'\{id:"([^"]+)"', content):
    id_val = m.group(1)
    pos = m.start()
    if id_val in ids_positions:
        ids_positions[id_val].append(pos)
    else:
        ids_positions[id_val] = [pos]

dupes = {k: v for k, v in ids_positions.items() if len(v) > 1}
print(f'Duplicates found: {list(dupes.keys())}')

for id_val, positions in dupes.items():
    # Keep first occurrence, remove second
    # Find the object starting at second position - go back to find ,{
    second_pos = positions[1]
    # Find the comma-brace that starts this object
    chunk_start = content.rfind(',{id:', 0, second_pos + 5)
    # Find the closing brace of this object
    # Walk forward from second_pos tracking depth
    i = second_pos
    depth = 0
    started = False
    while i < len(content):
        ch = content[i]
        if ch == '{': depth += 1; started = True
        elif ch == '}':
            depth -= 1
            if started and depth == 0:
                chunk_end = i + 1
                break
        i += 1
    
    removed = content[chunk_start:chunk_end]
    print(f'  Removing [{id_val}]: chars {chunk_start}-{chunk_end} ({chunk_end-chunk_start} chars)')
    print(f'  Preview: {repr(removed[:80])}')
    content = content[:chunk_start] + content[chunk_end:]

# Verify
remaining = len(re.findall(r'\{id:"([^"]+)"', content))
print(f'Ideas after dedup: {remaining}')

with open('data.js', 'w', encoding='utf-8') as f:
    f.write(content)
print('Written.')
