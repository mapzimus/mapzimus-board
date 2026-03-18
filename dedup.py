import re

with open('data.js', 'r', encoding='utf-8') as f:
    c = f.read()

key = 'farm_consolidation_trend'
positions = [m.start() for m in re.finditer(re.escape(key), c)]
print('Occurrences:', len(positions), 'at', positions)

if len(positions) == 2:
    # Remove the second occurrence - find its ,{ start and next ,{ end
    second_pos = positions[1]
    chunk_start = c.rfind(',', 0, second_pos)
    next_obj = re.search(r'\n,\{id:', c[second_pos:])
    chunk_end = second_pos + next_obj.start() if next_obj else len(c)
    print('Removing chunk_start:', chunk_start, 'chunk_end:', chunk_end)
    c = c[:chunk_start] + c[chunk_end:]
    with open('data.js', 'w', encoding='utf-8') as f:
        f.write(c)
    print('Done - removed duplicate')
