import re, collections

with open('data.js','r',encoding='utf-8') as f: raw=f.read()

lines = [l for l in raw.split('\n') if l.startswith(',{id:') or l.startswith('{id:')]
print('Total idea lines:', len(lines))

WEIGHTS = {'emotional':2.5,'relatability':2.0,'surprise':1.5,'tension':1.5,'visual':1.0,'data_ready':1.0,'originality':0.5}

bad_vs = []
vs_vals = []
type_counts = collections.Counter()
geo_counts = collections.Counter()
fmt_counts = collections.Counter()
section_counts = collections.Counter()
id_list = []
no_ext = []
no_vars = []
no_join = []
no_tags = []
ext_zero = []

for line in lines:
    id_m = re.search('id:"([^"]+)"', line)
    id_ = id_m.group(1) if id_m else 'UNKNOWN'
    id_list.append(id_)

    vs_m = re.search(',vs:(\d+),', line)
    sc_m = re.search('sc:\{([^}]+)\}', line)
    if vs_m and sc_m:
        vs = int(vs_m.group(1))
        vs_vals.append(vs)
        sc = {}
        for pair in re.finditer('(\w+):(\d+)', sc_m.group(1)):
            sc[pair.group(1)] = int(pair.group(2))
        computed = round(sum(sc.get(k,0)*w for k,w in WEIGHTS.items()))
        if abs(computed - vs) > 3:
            bad_vs.append((id_, vs, computed, vs-computed))

    t_m = re.search(',type:"([^"]+)"', line)
    g_m = re.search(',geo:"([^"]+)"', line)
    f_m = re.search(',fmt:"([^"]+)"', line)
    s_m = re.search(',section:"([^"]+)"', line)
    if t_m: type_counts[t_m.group(1)] += 1
    if g_m: geo_counts[g_m.group(1)] += 1
    if f_m: fmt_counts[f_m.group(1)] += 1
    if s_m: section_counts[s_m.group(1)] += 1

    if 'ext:[' not in line: no_ext.append(id_)
    if 'vars:[' not in line: no_vars.append(id_)
    if 'join:[' not in line: no_join.append(id_)
    if ',tags:' not in line: no_tags.append(id_)

    # ext with empty array
    ext_m = re.search('ext:\[([^\]]*)\]', line)
    if ext_m and ext_m.group(1).strip() == '':
        ext_zero.append(id_)

# Dupes
seen = set()
dupe_ids = []
for id_ in id_list:
    if id_ in seen: dupe_ids.append(id_)
    seen.add(id_)

print('Duplicate IDs: %d' % len(dupe_ids), dupe_ids[:5] if dupe_ids else '- none')
print()
print('Field completeness:')
print('  Missing ext:[]: %d' % len(no_ext))
print('  Missing vars:[]: %d' % len(no_vars))
print('  Missing join:[]: %d' % len(no_join))
print('  Missing tags: %d' % len(no_tags))
print('  Empty ext[]: %d' % len(ext_zero), ext_zero[:3] if ext_zero else '')
print()
print('V-score drift >3 pts (top 20):')
bad_vs.sort(key=lambda x: abs(x[3]), reverse=True)
for id_,stored,comp,diff in bad_vs[:20]:
    print('  stored:%d computed:%d diff:%+d  %s' % (stored,comp,diff,id_))
print()
print('Type distribution:', dict(type_counts))
print('Geo distribution:', dict(geo_counts))
print()
print('Format counts (top 15):')
for f,c in fmt_counts.most_common(15):
    print('  %-30s %d' % (f,c))
print()
print('Section counts (top 15):')
for s,c in section_counts.most_common(15):
    print('  %-35s %d' % (s,c))
print()
print('V-score distribution:')
if vs_vals:
    print('  min:%d max:%d mean:%.1f' % (min(vs_vals),max(vs_vals),sum(vs_vals)/len(vs_vals)))
    buckets = collections.Counter(v//10*10 for v in vs_vals)
    for b in sorted(buckets):
        bar = '#' * (buckets[b]//5)
        print('  %d-%d: %4d  %s' % (b,b+9,buckets[b],bar))
