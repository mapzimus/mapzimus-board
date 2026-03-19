"""Fix remaining 2 duplicate IDs in data.js"""
import re
from collections import Counter

with open(r'D:\projects\mapzimus-board\data.js','r',encoding='utf-8') as f:
    content = f.read()

fixes_made = 0

# Fix 1: nuclear_warheads_2025_map - second occurrence has different title
# Find both occurrences
target = '{id:"nuclear_warheads_2025_map"'
first = content.find(target)
second = content.find(target, first + 1)
if second >= 0:
    # Replace id in second occurrence only
    content = (content[:second] +
               content[second:second+50].replace('nuclear_warheads_2025_map',
                                                  'nuclear_warheads_country_2025', 1) +
               content[second+50:])
    fixes_made += 1
    print('Fixed nuclear_warheads dupe')
else:
    print('nuclear_warheads: only 1 occurrence found (already fixed?)')

# Fix 2: global_port_throughput_by_location - exact duplicate, remove second
target2 = '{id:"global_port_throughput_by_location"'
first2 = content.find(target2)
second2 = content.find(target2, first2 + 1)
if second2 >= 0:
    # Find end of the duplicate idea (next idea starts with ,{ or end of array)
    # Ideas are separated by \n,{ so find the next one after second2
    next_idea = content.find('\n,{id:', second2)
    if next_idea > second2:
        # Remove from the comma before second2 back to end of previous idea
        # second2 starts with {id: so the comma is just before it
        remove_start = second2 - 1  # the comma before this idea
        content = content[:remove_start] + content[next_idea:]
        fixes_made += 1
        print('Removed duplicate global_port_throughput idea')
    else:
        print('Could not find end of duplicate port idea')
else:
    print('global_port_throughput: only 1 occurrence (already fixed?)')

with open(r'D:\projects\mapzimus-board\data.js','w',encoding='utf-8') as f:
    f.write(content)

print('Total fixes:', fixes_made)

# Verify
ids = re.findall(r'\{id:"([^"]+)"', content)
dupes = [(k,n) for k,n in Counter(ids).items() if n > 1]
print('Remaining dupes:', dupes if dupes else 'NONE - CLEAN!')
print('Total ideas:', len(ids))
