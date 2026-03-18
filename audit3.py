import re

with open('data.js','r',encoding='utf-8') as f: raw=f.read()
lines = [l for l in raw.split('\n') if l.startswith(',{id:') or l.startswith('{id:')]

# Find Dual format
for line in lines:
    if 'fmt:"Dual"' in line:
        id_m = re.search('id:"([^"]+)"', line)
        title_m = re.search('title:"([^"]+)"', line)
        fmt_m = re.search('fmt:"([^"]+)"', line)
        geo_m = re.search('geo:"([^"]+)"', line)
        type_m = re.search('type:"([^"]+)"', line)
        print("Dual format idea:")
        print("  id:", id_m.group(1) if id_m else '?')
        print("  title:", title_m.group(1) if title_m else '?')
        print("  type:", type_m.group(1) if type_m else '?')
        print("  geo:", geo_m.group(1) if geo_m else '?')

print()

# Show geo filter values in app.js
with open('app.js','r',encoding='utf-8') as f: app=f.read()

# Find the geo filter button definitions in index.html
with open('index.html','r',encoding='utf-8') as f: html=f.read()
print("=== Geo filter pills in index.html ===")
for line in html.split('\n'):
    if 'data-geo' in line or ('geo' in line.lower() and 'pill' in line.lower()):
        print(" ", line.strip()[:120])

print()
print("=== top_n_list references in app.js ===")
for line in app.split('\n'):
    if 'top_n' in line or 'top-n' in line.lower():
        print(" ", line.strip()[:120])
