"""
consolidate.py - Fix fmt/geo taxonomy in data.js
"""
import re

with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()

original_size = len(content)

# FMT CONSOLIDATIONS
fmt_map = {
    'Regional choropleth':        'State choropleth',
    'Bar or line chart':          'Bar chart',
    'County scatter or bivariate':'Scatter plot',
    'Multi':                      'Bar chart',
    'Quadrant chart':             'Scatter plot',
    'H3 hexbin map':              'Special map',
}
for old, new in fmt_map.items():
    count = content.count(f'fmt:"{old}"')
    content = content.replace(f'fmt:"{old}"', f'fmt:"{new}"')
    print(f'  fmt: {old} -> {new} ({count} changed)')

# GEO top_n_list -> us_national + fmt -> Ranked list
# These are simple one-line records, use line-by-line replacement
lines = content.split('\n')
fixed = 0
new_lines = []
for line in lines:
    if 'geo:"top_n_list"' in line:
        line = line.replace('geo:"top_n_list"', 'geo:"us_national"')
        line = re.sub(r'fmt:"[^"]*"', 'fmt:"Ranked list"', line)
        fixed += 1
    new_lines.append(line)
content = '\n'.join(new_lines)
print(f'  geo: top_n_list -> us_national + Ranked list ({fixed} ideas)')

with open('data.js', 'w', encoding='utf-8') as f:
    f.write(content)

print(f'Done. {original_size} -> {len(content)} bytes')

fmts = re.findall(r'fmt:"([^"]+)"', content)
from collections import Counter
print('Final fmt counts:')
for k,n in Counter(fmts).most_common():
    print(f'  {n:4d}  {k}')
