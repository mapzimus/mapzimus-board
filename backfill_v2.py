"""
backfill_v2.py
Adds clarity, notes, status to every idea.
Recomputes vs with new 8-component formula.

New formula (max ~105, practical ceiling ~97):
  emotional   x2.0
  relatability x2.0
  clarity     x2.0  <-- NEW
  surprise    x1.5
  tension     x1.0
  visual      x1.0
  data_ready  x0.5
  originality x0.5
"""
import re, collections

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

# Clarity base by format
FMT_CLARITY = {
    'county choropleth':   8,
    'state choropleth':    8,
    'world choropleth':    8,
    'dot map':             7,
    'city map':            7,
    'line chart':          7,
    'bar chart':           7,
    'area chart':          7,
    'treemap':             6,
    'ranked list':         9,
    'scatter plot':        5,
    'special map':         5,
    'h3 hexbin map':       5,
    'quadrant chart':      5,
    'bivariate choropleth':4,
}

def estimate_clarity(fmt_str, type_str):
    base = FMT_CLARITY.get(fmt_str.strip().lower(), 6)
    if type_str.upper() == 'XREF':
        base = max(1, base - 1)
    if type_str.upper() == 'RANK':
        base = min(10, base + 1)
    return base

def compute_vs(sc):
    return round(sum(sc.get(k, 0) * w for k, w in WEIGHTS.items()))

with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()

lines = content.split('\n')
new_lines = []

added_clarity = 0
added_notes   = 0
added_status  = 0
vs_changed    = 0

for line in lines:
    if not (line.startswith(',{id:') or line.startswith('{id:')):
        new_lines.append(line)
        continue

    # --- Extract existing fields ---
    sc_m    = re.search(r'sc:\{([^}]+)\}', line)
    vs_m    = re.search(r',vs:(\d+),', line)
    fmt_m   = re.search(r',fmt:"([^"]+)"', line)
    type_m  = re.search(r',type:"([^"]+)"', line)
    tags_m  = re.search(r',tags:"', line)

    if not sc_m:
        new_lines.append(line)
        continue

    sc_str = sc_m.group(1)
    sc = {}
    for pair in re.finditer(r'(\w+):(\d+)', sc_str):
        sc[pair.group(1)] = int(pair.group(2))

    fmt_val  = fmt_m.group(1)  if fmt_m  else ''
    type_val = type_m.group(1) if type_m else ''

    # --- Add clarity if missing ---
    if 'clarity' not in sc:
        sc['clarity'] = estimate_clarity(fmt_val, type_val)
        new_sc_str = ','.join('%s:%d' % (k, sc[k]) for k in
                    ['emotional','relatability','surprise','tension','visual','data_ready','originality','clarity'])
        line = line.replace(sc_str, new_sc_str)
        added_clarity += 1

    # --- Recompute vs ---
    new_vs = compute_vs(sc)
    old_vs = int(vs_m.group(1)) if vs_m else 0
    if new_vs != old_vs:
        line = re.sub(r',vs:\d+,', ',vs:%d,' % new_vs, line)
        vs_changed += 1

    # --- Add notes field if missing ---
    if ',notes:' not in line:
        line = line.rstrip('}') + ',notes:""}'
        added_notes += 1

    # --- Add status field if missing ---
    if ',status:' not in line:
        line = line.rstrip('}') + ',status:"idea"}'
        added_status += 1

    new_lines.append(line)

with open('data.js', 'w', encoding='utf-8') as f:
    f.write('\n'.join(new_lines))

print("Backfill complete.")
print("  Added clarity:  %d ideas" % added_clarity)
print("  Added notes:    %d ideas" % added_notes)
print("  Added status:   %d ideas" % added_status)
print("  vs recomputed:  %d ideas changed" % vs_changed)

# Quick score distribution check
lines2 = [l for l in '\n'.join(new_lines).split('\n') if l.startswith(',{id:') or l.startswith('{id:')]
vs_vals = []
for line in lines2:
    m = re.search(r',vs:(\d+),', line)
    if m: vs_vals.append(int(m.group(1)))

if vs_vals:
    buckets = collections.Counter(v//10*10 for v in vs_vals)
    print("\nNew V-score distribution:")
    print("  min:%d  max:%d  mean:%.1f" % (min(vs_vals), max(vs_vals), sum(vs_vals)/len(vs_vals)))
    for b in sorted(buckets):
        print("  %d-%d: %d" % (b, b+9, buckets[b]))
