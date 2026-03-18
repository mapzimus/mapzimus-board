"""
normalize_fmt.py — collapse fmt field to 15 canonical categories.
Strips all suffixes. Stores ONLY the canonical name.
Handles both em dash (—) and hyphen (-) separators.
"""
import re

RULES = [
    (r'^Scatter',              'Scatter plot'),
    (r'^State choropleth',     'State choropleth'),
    (r'^Side.by.side state',   'State choropleth'),
    (r'^Side.by.side city',    'City map'),
    (r'^County choropleth',    'County choropleth'),
    (r'^Trivariate county',    'County choropleth'),
    (r'^H3 hexbin',            'H3 hexbin map'),
    (r'^Bivariate choropleth', 'Bivariate choropleth'),
    (r'^Bivariate$',           'Bivariate choropleth'),
    (r'^World choropleth',     'World choropleth'),
    (r'^World bubble',         'World choropleth'),
    (r'^Dot map',              'Dot map'),
    (r'^US dot map',           'Dot map'),
    (r'^Flow map',             'Dot map'),
    (r'^Continuous raster',    'Special map'),
    (r'^Three.panel',          'Special map'),
    (r'^Special map',          'Special map'),
    (r'^Quadrant',             'Quadrant chart'),
    (r'^Ranked scatter',       'Quadrant chart'),
    (r'^Dual.line',            'Line chart'),
    (r'^Multi.line',           'Line chart'),
    (r'^Line chart',           'Line chart'),
    (r'^Dual.axis',            'Line chart'),
    (r'^Dual area',            'Area chart'),
    (r'^Area chart',           'Area chart'),
    (r'^Stacked area',         'Area chart'),
    (r'^Grouped bar',          'Bar chart'),
    (r'^Grouped ranked bar',   'Bar chart'),
    (r'^Stacked bar',          'Bar chart'),
    (r'^Horizontal bar',       'Bar chart'),
    (r'^Diverging horizontal', 'Bar chart'),
    (r'^Side.by.side bar',     'Bar chart'),
    (r'^Demographic',          'Bar chart'),
    (r'^Pie chart',            'Bar chart'),
    (r'^Bar chart',            'Bar chart'),
    (r'^Pareto',               'Bar chart'),
    (r'^Treemap or stacked',   'Treemap'),
    (r'^Treemap',              'Treemap'),
    (r'^Horizontal ranked',    'Ranked list'),
    (r'^Ranked horizontal',    'Ranked list'),
    (r'^Ranked bar',           'Ranked list'),
    (r'^Ranked list',          'Ranked list'),
    (r'^Top/bottom',           'Ranked list'),
    (r'^River flow',           'Ranked list'),
    (r'^RANKED',               'Ranked list'),
]

def get_canonical(fmt_str):
    # Strip everything after first em dash, en dash, OR ' - ' (space-hyphen-space)
    # First try splitting on em/en dash
    prefix = re.split(r'\s*[—–]\s*', fmt_str)[0].strip()
    # Then try splitting on ' - ' (space-hyphen-space) if no em dash found
    if prefix == fmt_str.strip():
        prefix = re.split(r'\s+-\s+', fmt_str)[0].strip()

    for pattern, canonical in RULES:
        if re.match(pattern, prefix, re.IGNORECASE):
            return canonical

    # No match — return the prefix as-is (trimmed)
    return prefix

with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()

changes = 0
skipped = 0

def replace_fmt(match):
    global changes, skipped
    original = match.group(1)
    canonical = get_canonical(original)
    if canonical != original:
        changes += 1
        return f'fmt:"{canonical}"'
    skipped += 1
    return match.group(0)

result = re.sub(r'fmt:"([^"]+)"', replace_fmt, content)

with open('data.js', 'w', encoding='utf-8') as f:
    f.write(result)

print(f'Done. Changed: {changes} | Already canonical: {skipped}')

# Report final distribution
fmts = {}
for m in re.finditer(r'fmt:"([^"]+)"', result):
    key = m.group(1)
    fmts[key] = fmts.get(key, 0) + 1

print('\nFinal fmt distribution:')
for k, n in sorted(fmts.items(), key=lambda x: -x[1]):
    print(f'  {n:4d}  {k}')
print(f'\nTotal unique categories: {len(fmts)}')
