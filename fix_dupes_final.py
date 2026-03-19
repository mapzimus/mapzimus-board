"""
Fix duplicate IDs by renaming the SECOND occurrence of each dupe.
Strategy: find all lines, track which IDs we've seen, rename 2nd occurrence
using a slug derived from the title.
"""
import re

def title_to_id(title):
    t = title.lower()
    t = re.sub(r'[^a-z0-9]+', '_', t)
    t = t.strip('_')[:60]
    return 'xref_' + t if not t.startswith('xref_') else t

with open(r'D:\projects\mapzimus-board\data.js','r',encoding='utf-8') as f:
    content = f.read()

lines = content.split('\n')
seen_ids = set()
new_lines = []
changed = 0

for line in lines:
    if not (line.startswith(',{id:') or line.startswith('{id:')):
        new_lines.append(line)
        continue

    id_m = re.search(r'(?<!\w)id:"([^"]+)"', line)
    if not id_m:
        new_lines.append(line)
        continue

    current_id = id_m.group(1)

    if current_id in seen_ids:
        # This is the duplicate - rename it
        title_m = re.search(r'title:"([^"]+)"', line)
        title = title_m.group(1) if title_m else ''
        new_id = title_to_id(title)
        # Make sure new_id is also unique
        base = new_id
        n = 2
        while new_id in seen_ids:
            new_id = base + '_%d' % n
            n += 1
        # Replace ONLY the first id: field (not tags)
        line = re.sub(r'((?:^|,)\{?)id:"' + re.escape(current_id) + '"', 
                      lambda m: m.group(1) + 'id:"%s"' % new_id, line, count=1)
        seen_ids.add(new_id)
        changed += 1
        print('RENAMED: %s -> %s' % (current_id, new_id))
        print('   title: %s' % title[:80])
    else:
        seen_ids.add(current_id)

    new_lines.append(line)

with open(r'D:\projects\mapzimus-board\data.js','w',encoding='utf-8') as f:
    f.write('\n'.join(new_lines))

print('\nDone. Renamed: %d' % changed)

# Verify
from collections import Counter
ids2 = re.findall(r'\{id:"([^"]+)"', '\n'.join(new_lines))
dupes2 = [(k,n) for k,n in Counter(ids2).items() if n > 1]
print('Remaining dupes:', dupes2 if dupes2 else 'NONE')
