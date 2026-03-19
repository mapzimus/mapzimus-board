"""Direct targeted replacement of each second dupe occurrence."""
import re

with open(r'D:\projects\mapzimus-board\data.js','r',encoding='utf-8') as f: content=f.read()

# Each: (old_fragment_unique_to_2nd_occurrence, new_id)
replacements = [
    # nuclear_warheads_2025_map second: "Nuclear warheads by country 2025 - where the world's 12,500 bombs"
    (
        '{id:"nuclear_warheads_2025_map",title:"Nuclear warheads by country 2025',
        '{id:"nuclear_warheads_country_2025_map",title:"Nuclear warheads by country 2025'
    ),
    # global_port_throughput_by_location - need to check which is second
    # From earlier: second is "World Happiness Report score vs. Gini"
    # Let's find the second occurrence
    (
        '{id:"global_port_throughput_by_location",title:"Global port throughput',
        '{id:"global_container_port_throughput_map",title:"Global port throughput'
    ),
    # union_density_by_state_trend_1980_2024 - second is "Labor market concentration"
    (
        '{id:"union_density_by_state_trend_1980_2024",title:"Union membership density',
        '{id:"union_density_by_state_map_1980_2024",title:"Union membership density'
    ),
]

changed = 0
for old, new in replacements:
    if old in content:
        # Replace only the SECOND occurrence
        first = content.find(old)
        second = content.find(old, first + 1)
        if second >= 0:
            content = content[:second] + new + content[second+len(old):]
            print('Fixed (2nd occ): %r -> %r' % (old[:50], new[:50]))
            changed += 1
        else:
            # Only one occurrence - replace it directly if needed
            print('Only 1 occurrence of: %r' % old[:50])
    else:
        print('NOT FOUND: %r' % old[:50])

with open(r'D:\projects\mapzimus-board\data.js','w',encoding='utf-8') as f:
    f.write(content)

print('\nChanged:', changed)

# Verify
from collections import Counter
ids = re.findall(r'\{id:"([^"]+)"', content)
dupes = [(k,n) for k,n in Counter(ids).items() if n > 1]
print('Remaining dupes:', dupes if dupes else 'NONE - CLEAN!')
print('Total ideas:', len(ids))
