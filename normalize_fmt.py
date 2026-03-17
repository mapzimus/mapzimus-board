"""
normalize_fmt.py — consolidate fmt field to ~12 canonical categories
Preserves the descriptive suffix after — but standardizes the prefix key
"""
import re

# ── CANONICAL MAP: raw prefix → canonical category ───────────────────────────
# Order matters — more specific rules first

RULES = [
    # Scatter (keep as one bucket regardless of suffix complexity)
    (r'^Scatter', 'Scatter plot'),

    # Choropleth maps
    (r'^State choropleth', 'State choropleth'),
    (r'^Side-by-side state map', 'State choropleth'),
    (r'^Side-by-side city map', 'City map'),
    (r'^County choropleth', 'County choropleth'),
    (r'^Trivariate county map', 'County choropleth'),
    (r'^H3 hexbin', 'H3 hexbin map'),
    (r'^Bivariate choropleth', 'Bivariate choropleth'),
    (r'^Bivariate$', 'Bivariate choropleth'),
    (r'^World choropleth', 'World choropleth'),
    (r'^World bubble map', 'World choropleth'),
    (r'^Dot map', 'Dot map'),
    (r'^US dot map', 'Dot map'),
    (r'^Flow map', 'Dot map'),
    (r'^Continuous raster surface', 'Special map'),
    (r'^Three-panel triptych', 'Special map'),

    # Quadrant
    (r'^Quadrant', 'Quadrant chart'),
    (r'^Ranked scatter', 'Quadrant chart'),

    # Line charts (all dual/multi/axis variants → Line chart)
    (r'^Dual-line', 'Line chart'),
    (r'^Multi-line', 'Line chart'),
    (r'^Line chart', 'Line chart'),
    (r'^Dual-axis', 'Line chart'),
    (r'^Dual area', 'Area chart'),

    # Area charts
    (r'^Area chart', 'Area chart'),
    (r'^Stacked area', 'Area chart'),

    # Bar charts (grouped, stacked, horizontal non-ranked, side-by-side)
    (r'^Grouped bar', 'Bar chart'),
    (r'^Grouped ranked bar', 'Bar chart'),
    (r'^Stacked bar', 'Bar chart'),
    (r'^Horizontal bar', 'Bar chart'),
    (r'^Diverging horizontal bar', 'Bar chart'),
    (r'^Side-by-side bar', 'Bar chart'),
    (r'^Demographic breakdown', 'Bar chart'),
    (r'^Pie chart', 'Bar chart'),
    (r'^Bar chart', 'Bar chart'),
    (r'^Pareto chart', 'Bar chart'),
    (r'^Treemap or stacked bar', 'Treemap'),
    (r'^Treemap', 'Treemap'),

    # Ranked lists (all ranked bar / top-bottom list variants)
    (r'^Horizontal ranked bar', 'Ranked list'),
    (r'^Ranked horizontal bar', 'Ranked list'),
    (r'^Ranked bar', 'Ranked list'),
    (r'^Ranked list', 'Ranked list'),
    (r'^Top/bottom', 'Ranked list'),
    (r'^River flow diagram', 'Ranked list'),
]

def normalize_prefix(fmt_str):
    """Return (canonical_category, original_suffix)"""
    # Split on em dash or regular dash used as separator
    parts = re.split(r'\s*[—–]\s*', fmt_str, maxsplit=1)
    prefix = parts[0].strip()
    suffix = parts[1].strip() if len(parts) > 1 else ''

    for pattern, canonical in RULES:
        if re.match(pattern, prefix, re.IGNORECASE):
            return canonical, suffix

    # No match — return original prefix as-is
    return prefix, suffix

def rebuild_fmt(canonical, suffix):
    if suffix:
        return f'{canonical} — {suffix}'
    return canonical

# ── APPLY TO data.js ──────────────────────────────────────────────────────────
with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()

changes = 0
skipped = 0

def replace_fmt(match):
    global changes, skipped
    original = match.group(1)
    canonical, suffix = normalize_prefix(original)
    new_fmt = rebuild_fmt(canonical, suffix)
    if new_fmt != original:
        changes += 1
        return f'fmt:"{new_fmt}"'
    skipped += 1
    return match.group(0)

result = re.sub(r'fmt:"([^"]+)"', replace_fmt, content)

with open('data.js', 'w', encoding='utf-8') as f:
    f.write(result)

print(f'Done. Changed: {changes} | Unchanged: {skipped}')

# ── REPORT FINAL DISTRIBUTION ─────────────────────────────────────────────────
with open('data.js', 'r', encoding='utf-8') as f:
    content2 = f.read()

import re as re2
fmts = {}
for m in re2.finditer(r'fmt:"([^"]+)"', content2):
    key = m.group(1).split('—')[0].split('(')[0].strip()
    fmts[key] = fmts.get(key, 0) + 1

print('\nFinal distribution:')
for k, n in sorted(fmts.items(), key=lambda x: -x[1]):
    print(f'  {n:3d}  {k}')
