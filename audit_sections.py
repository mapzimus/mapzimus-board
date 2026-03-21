import re, pathlib

data = pathlib.Path('data.js').read_text(encoding='utf-8')
app  = pathlib.Path('app.js').read_text(encoding='utf-8')

# All section values actually used in data.js
used = sorted(set(re.findall(r'section:"([^"]+)"', data)))
print('=== SECTIONS USED IN DATA.JS ===')
for s in used:
    c = len(re.findall(f'section:"{re.escape(s)}"', data))
    print(f'  {c:4d}  {s}')

# All section strings that appear in app.js
app_sections = sorted(set(re.findall(r'"([^"]{3,40})"', app)))
# Filter to ones that look like category names (title-case-ish, no special chars)
cat_like = [s for s in app_sections if s in used]

print('\n=== SECTIONS FROM DATA.JS THAT APPEAR IN APP.JS ===')
for s in cat_like:
    print(f'  {s}')

print('\n=== IN DATA.JS BUT NOT IN APP.JS ===')
for s in used:
    if s not in app_sections:
        print(f'  MISSING: {s}')

print('\n=== IN APP.JS BUT NOT IN DATA.JS ===')
for s in cat_like:
    if s not in used:
        print(f'  ORPHAN: {s}')

# Also dump BADGE_SECTIONS block raw
m = re.search(r'BADGE_SECTIONS[^;]+;', app)
if m:
    print('\n=== BADGE_SECTIONS RAW ===')
    print(m.group(0)[:3000])
