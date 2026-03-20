"""
review_remaps.py - Check for false positives in the geo remapping
Flag any us_state -> us_new_england or us_state -> us_northeast
where the idea is clearly a 50-state comparison
"""
import re

with open('data.js', encoding='utf-8') as f:
    content = f.read()

suspicious = []
for line in content.split('\n'):
    if not (line.startswith('{id:') or line.startswith(',{id:')):
        continue
    geo_m = re.search(r'geo:"([^"]+)"', line)
    if not geo_m: continue
    geo = geo_m.group(1)
    if geo not in ('us_new_england', 'us_northeast'): continue

    title_m = re.search(r'title:"([^"]*)"', line)
    title = title_m.group(1) if title_m else '?'
    fmt_m = re.search(r'fmt:"([^"]*)"', line)
    fmt = fmt_m.group(1) if fmt_m else '?'

    # Flag if fmt is State choropleth or title says "by state"
    if fmt == 'State choropleth' or 'by state' in title.lower() or 'each state' in title.lower():
        suspicious.append((geo, fmt, title))

print(f"Suspicious remaps (state-level maps tagged as regional): {len(suspicious)}")
for geo, fmt, title in suspicious[:30]:
    print(f"  {geo:20s} [{fmt}] {title[:70]}")
