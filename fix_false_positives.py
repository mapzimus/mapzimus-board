"""
fix_false_positives.py
Revert State choropleth / by state ideas that were wrongly tagged regional
"""
import re

with open('data.js', encoding='utf-8') as f:
    content = f.read()

lines = content.split('\n')
new_lines = []
reverted = 0

for line in lines:
    if not (line.startswith('{id:') or line.startswith(',{id:')):
        new_lines.append(line)
        continue

    geo_m   = re.search(r'geo:"([^"]+)"', line)
    fmt_m   = re.search(r'fmt:"([^"]*)"', line)
    title_m = re.search(r'title:"([^"]*)"', line)

    if not geo_m:
        new_lines.append(line)
        continue

    geo   = geo_m.group(1)
    fmt   = fmt_m.group(1) if fmt_m else ''
    title = title_m.group(1).lower() if title_m else ''

    # Revert if: tagged as regional but is clearly a 50-state idea
    should_revert = (
        geo in ('us_new_england', 'us_northeast') and
        (fmt == 'State choropleth' or
         fmt == 'Bivariate choropleth' or
         'by state' in title or
         'each state' in title or
         'per state' in title or
         'state by state' in title or
         'all states' in title or
         'every state' in title or
         'across states' in title)
    )

    if should_revert:
        line = line.replace(f'geo:"{geo}"', 'geo:"us_state"')
        reverted += 1

    new_lines.append(line)

print(f"Reverted {reverted} false positives back to us_state")

new_content = '\n'.join(new_lines)
with open('data.js', 'w', encoding='utf-8') as f:
    f.write(new_content)

# Final counts
geos = re.findall(r'geo:"([^"]+)"', new_content)
from collections import Counter
print("Final geo distribution:")
for k,n in Counter(geos).most_common():
    print(f"  {n:5d}  {k}")
