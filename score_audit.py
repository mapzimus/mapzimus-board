import re, pathlib, statistics

data = pathlib.Path('data.js').read_text(encoding='utf-8')

# Parse all ideas with flexible sc field order
pat = re.compile(r'id:"([^"]+)".*?sc:\{([^}]+)\},vs:(\d+)')

ideas = []
for m in pat.finditer(data):
    id_ = m.group(1)
    sc_raw = m.group(2)
    vs = int(m.group(3))
    sc = {}
    for kv in sc_raw.split(','):
        k, v = kv.split(':')
        sc[k.strip()] = int(v.strip())
    ideas.append({'id': id_, 'vs': vs, **sc})

print(f'Total ideas parsed: {len(ideas)}')

all_vs = [x['vs'] for x in ideas]
print(f'Mean vs: {statistics.mean(all_vs):.1f}  Median: {statistics.median(all_vs)}  Min: {min(all_vs)}  Max: {max(all_vs)}')

buckets = {}
for v in all_vs:
    b = (v // 10) * 10
    buckets[b] = buckets.get(b, 0) + 1
print('\nScore distribution:')
for b in sorted(buckets):
    bar = '#' * (buckets[b] // 10)
    print(f'  {b:3d}-{b+9}: {buckets[b]:4d}  {bar}')

# Show average of each sc field
print('\nAverage sc field values across ALL ideas:')
for field in ['emotional','relatability','clarity','surprise','tension','visual','originality','data_ready']:
    vals = [x.get(field,0) for x in ideas]
    print(f'  {field:15s}: {statistics.mean(vals):.1f}')

# Now recompute vs for every idea using the formula and compare
# formula: raw = e*2+r*2+c*2+s*1.5+t*1+v*1.25+o*1
# vs = int((raw/10.75)*(1-0.3*(1-dr/100)))
print('\nChecking formula correctness...')
mismatches = 0
for x in ideas:
    e = x.get('emotional',0)
    r = x.get('relatability',0)
    c = x.get('clarity',0)
    s = x.get('surprise',0)
    t = x.get('tension',0)
    v = x.get('visual',0)
    o = x.get('originality',0)
    dr = x.get('data_ready',0)
    raw = e*2 + r*2 + c*2 + s*1.5 + t*1 + v*1.25 + o*1
    vs_correct = int((raw/10.75)*(1-0.3*(1-dr/100)))
    if vs_correct != x['vs']:
        mismatches += 1
        if mismatches <= 5:
            print(f"  MISMATCH: {x['id'][:50]} stored:{x['vs']} correct:{vs_correct}")
print(f'Total mismatches: {mismatches}')

# Bottom 20 ideas
print('\nBottom 20 ideas by vs:')
for x in sorted(ideas, key=lambda x: x['vs'])[:20]:
    print(f"  vs:{x['vs']:3d}  {x['id'][:60]}")

# Top 20 ideas  
print('\nTop 20 ideas by vs:')
for x in sorted(ideas, key=lambda x: -x['vs'])[:20]:
    print(f"  vs:{x['vs']:3d}  {x['id'][:60]}")
