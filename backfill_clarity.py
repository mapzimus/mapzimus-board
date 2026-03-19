"""
backfill_clarity.py
Adds clarity to sc{}, adds status:"idea", adds notes:"", recomputes all vs.

New formula:
  emotional*2.0 + relatability*2.0 + clarity*2.0 + surprise*1.5
  + tension*1.0 + visual*1.0 + data_ready*0.5 + originality*0.5
Max = 100
"""
import re

WEIGHTS = {
    'emotional':    2.0,
    'relatability': 2.0,
    'clarity':      2.0,
    'surprise':     1.5,
    'tension':      1.0,
    'visual':       1.0,
    'data_ready':   0.5,
    'originality':  0.5,
}

def estimate_clarity(fmt, type_, geo):
    """Auto-estimate clarity from format/type."""
    base = {
        'State choropleth':    8,
        'County choropleth':   8,
        'World choropleth':    8,
        'Bar chart':           7,
        'Line chart':          7,
        'Area chart':          7,
        'Ranked list':         9,
        'Dot map':             7,
        'City map':            7,
        'Scatter plot':        5,
        'Bivariate choropleth':4,
        'H3 hexbin map':       5,
        'Special map':         5,
        'Treemap':             6,
        'Quadrant chart':      5,
    }.get(fmt, 6)
    if type_ == 'XREF':  base = max(1, base - 1)
    if type_ == 'RANK':  base = min(10, base + 1)
    return base

def compute_vs(sc):
    return round(sum(sc.get(k, 0) * w for k, w in WEIGHTS.items()))

with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()

lines = content.split('\n')
new_lines = []
changed = 0
skipped = 0

for line in lines:
    if not (line.startswith(',{id:') or line.startswith('{id:')):
        new_lines.append(line)
        continue

    sc_m   = re.search(r'sc:\{([^}]+)\}', line)
    vs_m   = re.search(r',vs:(\d+),', line)
    fmt_m  = re.search(r',fmt:"([^"]+)"', line)
    type_m = re.search(r',type:"([^"]+)"', line)
    geo_m  = re.search(r',geo:"([^"]+)"', line)

    if not (sc_m and vs_m):
        skipped += 1
        new_lines.append(line)
        continue

    sc_str = sc_m.group(1)
    sc = {}
    for pair in re.finditer(r'(\w+):(\d+)', sc_str):
        sc[pair.group(1)] = int(pair.group(2))

    fmt   = fmt_m.group(1)  if fmt_m  else ''
    type_ = type_m.group(1) if type_m else ''
    geo   = geo_m.group(1)  if geo_m  else ''

    # Add clarity if missing
    if 'clarity' not in sc:
        sc['clarity'] = estimate_clarity(fmt, type_, geo)

    # Rebuild sc block in canonical order
    order = ['emotional','relatability','clarity','surprise','tension','visual','data_ready','originality']
    sc_new = ','.join('%s:%d' % (k, sc[k]) for k in order if k in sc)
    line = re.sub(r'sc:\{[^}]+\}', 'sc:{%s}' % sc_new, line)

    # Recompute vs
    new_vs = compute_vs(sc)
    line = re.sub(r',vs:\d+,', ',vs:%d,' % new_vs, line)

    # Add status:"idea" if missing
    if ',status:' not in line:
        line = re.sub(r',tags:"', ',status:"idea",tags:"', line)

    # Add notes:"" if missing
    if ',notes:' not in line:
        line = re.sub(r',tags:"', ',notes:"",tags:"', line)

    changed += 1
    new_lines.append(line)

with open('data.js', 'w', encoding='utf-8') as f:
    f.write('\n'.join(new_lines))

print('Done.')
print('  Ideas updated: %d' % changed)
print('  Skipped:       %d' % skipped)

# Show new top 10
results = []
for line in new_lines:
    if not (line.startswith(',{id:') or line.startswith('{id:')):
        continue
    id_m  = re.search(r'id:"([^"]+)"', line)
    vs_m  = re.search(r',vs:(\d+),', line)
    if id_m and vs_m:
        results.append((int(vs_m.group(1)), id_m.group(1)))
results.sort(reverse=True)
print()
print('New top 10 V-scores:')
for vs, id_ in results[:10]:
    print('  vs:%d  %s' % (vs, id_))
print()
print('V-score distribution:')
import collections
vs_vals = [v for v,_ in results]
if vs_vals:
    print('  min:%d max:%d mean:%.1f' % (min(vs_vals), max(vs_vals), sum(vs_vals)/len(vs_vals)))
    buckets = collections.Counter(v//10*10 for v in vs_vals)
    for b in sorted(buckets):
        print('  %d-%d: %d' % (b, b+9, buckets[b]))
