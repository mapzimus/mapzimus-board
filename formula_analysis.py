"""formula_analysis.py - Analyze the current V-score formula and its properties"""
import re, collections

with open('data.js','r',encoding='utf-8') as f: raw=f.read()
lines = [l for l in raw.split('\n') if l.startswith(',{id:') or l.startswith('{id:')]

WEIGHTS = {'emotional':2.5,'relatability':2.0,'surprise':1.5,'tension':1.5,
           'visual':1.0,'data_ready':1.0,'originality':0.5}

# --- 1. Formula properties ---
print("=== CURRENT FORMULA ===")
print("  emotional   * 2.5")
print("  relatability* 2.0")
print("  surprise    * 1.5")
print("  tension     * 1.5")
print("  visual      * 1.0")
print("  data_ready  * 1.0")
print("  originality * 0.5")
total_w = sum(WEIGHTS.values())
print("  Total weight: %.1f" % total_w)
print("  Max possible score (all 10s): %d" % round(sum(v*10 for v in WEIGHTS.values())))
print("  Min possible score (all 0s): 0")
print()

# --- 2. Per-dimension stats across all ideas ---
print("=== PER-DIMENSION STATS (mean, stdev, distribution) ===")
dim_vals = {k:[] for k in WEIGHTS}
vs_all = []

for line in lines:
    sc_m = re.search('sc:\\{([^}]+)\\}', line)
    vs_m = re.search(',vs:(\\d+),', line)
    if sc_m:
        for pair in re.finditer('(\\w+):(\\d+)', sc_m.group(1)):
            k,v = pair.group(1), int(pair.group(2))
            if k in dim_vals:
                dim_vals[k].append(v)
    if vs_m:
        vs_all.append(int(vs_m.group(1)))

for dim in ['emotional','relatability','surprise','tension','visual','data_ready','originality']:
    vals = dim_vals[dim]
    mean = sum(vals)/len(vals)
    var = sum((v-mean)**2 for v in vals)/len(vals)
    stdev = var**0.5
    dist = collections.Counter(vals)
    print("  %-14s  mean:%.2f  stdev:%.2f  [%s]" % (
        dim, mean, stdev,
        '  '.join('%d:%d' % (k,dist[k]) for k in sorted(dist))
    ))

print()

# --- 3. Clarity concern: which dimensions actually differentiate? ---
print("=== DIMENSION DIFFERENTIATION (range of scores used) ===")
print("  (Low range = dimension is not differentiating ideas much)")
for dim in ['emotional','relatability','surprise','tension','visual','data_ready','originality']:
    vals = dim_vals[dim]
    unique = sorted(set(vals))
    mean = sum(vals)/len(vals)
    print("  %-14s  range:%d-%d  unique_values:%d  mean:%.1f  weight:%.1f  effective_range:%.1f" % (
        dim, min(vals), max(vals), len(unique), mean,
        WEIGHTS[dim], (max(vals)-min(vals))*WEIGHTS[dim]
    ))

print()

# --- 4. Correlation between dimensions (are some redundant?) ---
print("=== DIMENSION CORRELATION MATRIX ===")
dims = ['emotional','relatability','surprise','tension','visual','data_ready','originality']
n = len(dim_vals['emotional'])

def corr(a,b):
    ma,mb = sum(a)/n, sum(b)/n
    num = sum((a[i]-ma)*(b[i]-mb) for i in range(n))
    da = (sum((a[i]-ma)**2 for i in range(n)))**0.5
    db = (sum((b[i]-mb)**2 for i in range(n)))**0.5
    return num/(da*db) if da*db > 0 else 0

print("  " + "  ".join("%-5s" % d[:5] for d in dims))
for d1 in dims:
    row = []
    for d2 in dims:
        c = corr(dim_vals[d1], dim_vals[d2])
        row.append("%-5.2f" % c)
    print("  %-14s %s" % (d1, "  ".join(row)))

print()

# --- 5. What does changing one dimension by 1 point do to the final score? ---
print("=== SCORE SENSITIVITY (1-point change per dimension) ===")
for dim, w in sorted(WEIGHTS.items(), key=lambda x:-x[1]):
    print("  +1 %s = +%.1f to V-score (%.1f%% of max range)" % (dim, w, w/sum(WEIGHTS.values())*100))

print()

# --- 6. Score distribution sanity ---
print("=== V-SCORE DISTRIBUTION ===")
print("  mean:%.1f  min:%d  max:%d" % (sum(vs_all)/len(vs_all), min(vs_all), max(vs_all)))
above80 = sum(1 for v in vs_all if v >= 80)
above85 = sum(1 for v in vs_all if v >= 85)
above90 = sum(1 for v in vs_all if v >= 90)
print("  Ideas >=80: %d (%.1f%%)" % (above80, above80/len(vs_all)*100))
print("  Ideas >=85: %d (%.1f%%)" % (above85, above85/len(vs_all)*100))
print("  Ideas >=90: %d (%.1f%%)" % (above90, above90/len(vs_all)*100))
