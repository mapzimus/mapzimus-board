import re

with open(r'D:\projects\mapzimus-board\data.js','r',encoding='utf-8') as f: content=f.read()
lines = content.split('\n')

# Map: old_id -> (new_id, title_fragment to identify WHICH occurrence to rename)
# We rename the SECOND occurrence (wrong one) by matching on title fragment
fixes = [
    # nuclear_warheads_2025_map second occurrence is actually the immigrant health paradox map
    ('nuclear_warheads_2025_map', 'metro_foreign_born_health_advantage', 'native-born mortality rate'),
    # global_port_throughput_by_location second occurrence is happiness vs gini
    ('global_port_throughput_by_location', 'xref_global_happiness_vs_gini', 'Happiness Report score vs. Gini'),
    # union_density_by_state_trend_1980_2024 second occurrence is employer monopsony
    ('union_density_by_state_trend_1980_2024', 'xref_labor_monopsony_vs_wages', 'employer monopsony'),
    # Also fix first occurrence of global_port_throughput (which has title about eviction)
    ('global_port_throughput_by_location', 'xref_eviction_rate_vs_homelessness', 'Eviction rate vs. homelessness'),
    # Also fix first occurrence of union_density (which has title about highways)
    ('union_density_by_state_trend_1980_2024', 'xref_highway_routing_black_neighborhoods', 'highway routing through Black'),
]

changed = 0
seen_ids = {}  # track which we've already processed

new_lines = []
for line in lines:
    if not (line.startswith(',{id:') or line.startswith('{id:')):
        new_lines.append(line)
        continue

    id_m = re.search(r'id:"([^"]+)"', line)
    if not id_m:
        new_lines.append(line)
        continue

    current_id = id_m.group(1)
    matched = False

    for old_id, new_id, title_frag in fixes:
        if current_id == old_id and title_frag.lower() in line.lower():
            # Check if we already used this new_id
            if new_id not in seen_ids:
                line = line.replace('id:"%s"' % old_id, 'id:"%s"' % new_id, 1)
                seen_ids[new_id] = True
                changed += 1
                print('Renamed %s -> %s' % (old_id, new_id))
                matched = True
                break

    new_lines.append(line)

with open(r'D:\projects\mapzimus-board\data.js','w',encoding='utf-8') as f:
    f.write('\n'.join(new_lines))

print('Done. Changed:', changed)
