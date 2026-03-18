import re, collections

with open('data.js','r',encoding='utf-8') as f: raw=f.read()
lines = [l for l in raw.split('\n') if l.startswith(',{id:') or l.startswith('{id:')]

# 1. The lone RANKED_LIST type (should be RANK)
print("=== 1. RANKED_LIST type (should be RANK) ===")
for line in lines:
    if ',type:"RANKED_LIST"' in line:
        id_m = re.search('id:"([^"]+)"', line)
        print("  id:", id_m.group(1) if id_m else '?')

# 2. top_n_list geo (non-standard)
print("\n=== 2. top_n_list geo entries ===")
top_n_ids = []
for line in lines:
    if ',geo:"top_n_list"' in line:
        id_m = re.search('id:"([^"]+)"', line)
        fmt_m = re.search(',fmt:"([^"]+)"', line)
        top_n_ids.append(id_m.group(1) if id_m else '?')
print("  count:", len(top_n_ids))
print("  sample:", top_n_ids[:8])

# 3. Empty ext[] - what are these ideas?
print("\n=== 3. Empty ext[] ideas (sample 10) ===")
ext_empty = []
for line in lines:
    ext_m = re.search('ext:\[([^\]]*)\]', line)
    if ext_m and ext_m.group(1).strip() == '':
        id_m = re.search('id:"([^"]+)"', line)
        geo_m = re.search(',geo:"([^"]+)"', line)
        ext_empty.append((id_m.group(1) if id_m else '?', geo_m.group(1) if geo_m else '?'))
for id_,geo in ext_empty[:10]:
    print("  %s [geo:%s]" % (id_, geo))

# 4. Format name inconsistencies (case/spacing issues)
print("\n=== 4. Non-canonical format names ===")
CANONICAL_FMTS = {
    'Scatter plot','State choropleth','World choropleth','County choropleth',
    'Line chart','Bar chart','Area chart','Ranked list','City map','Dot map',
    'Special map','Bivariate choropleth','Treemap','Quadrant chart','H3 hexbin map'
}
bad_fmts = collections.Counter()
for line in lines:
    f_m = re.search(',fmt:"([^"]+)"', line)
    if f_m:
        fmt = f_m.group(1)
        if fmt not in CANONICAL_FMTS:
            bad_fmts[fmt] += 1
print("  Non-canonical formats found:")
for f,c in bad_fmts.most_common(20):
    print("  %-35s %d" % (f, c))

# 5. Sub-score sanity: any sc values > 10 or < 0?
print("\n=== 5. Out-of-range sc values ===")
bad_sc = []
for line in lines:
    sc_m = re.search('sc:\{([^}]+)\}', line)
    id_m = re.search('id:"([^"]+)"', line)
    if sc_m:
        sc_str = sc_m.group(1)
        for pair in re.finditer('(\w+):(\d+)', sc_str):
            val = int(pair.group(2))
            if val > 10 or val < 0:
                bad_sc.append((id_m.group(1) if id_m else '?', pair.group(1), val))
for id_,k,v in bad_sc[:10]:
    print("  %s: %s=%d" % (id_,k,v))
if not bad_sc:
    print("  None - all sc values 0-10")

# 6. Missing sc sub-fields
print("\n=== 6. Ideas with missing sc sub-fields ===")
SC_FIELDS = ['emotional','relatability','surprise','tension','visual','data_ready','originality']
missing_sc = []
for line in lines:
    sc_m = re.search('sc:\{([^}]+)\}', line)
    id_m = re.search('id:"([^"]+)"', line)
    if sc_m:
        sc_str = sc_m.group(1)
        sc_keys = [pair.group(1) for pair in re.finditer('(\w+):(\d+)', sc_str)]
        missing = [f for f in SC_FIELDS if f not in sc_keys]
        if missing:
            missing_sc.append((id_m.group(1) if id_m else '?', missing))
for id_,missing in missing_sc[:10]:
    print("  %s missing: %s" % (id_, missing))
if not missing_sc:
    print("  None - all ideas have all 7 sc fields")

# 7. IDs with special characters or spaces
print("\n=== 7. Suspicious IDs ===")
bad_ids = []
for line in lines:
    id_m = re.search('id:"([^"]+)"', line)
    if id_m:
        id_ = id_m.group(1)
        if ' ' in id_ or not re.match(r'^[a-z0-9_]+$', id_):
            bad_ids.append(id_)
print("  Bad-format IDs:", len(bad_ids), bad_ids[:5] if bad_ids else 'none')

# 8. tbl field completeness (short/empty tbl strings)
print("\n=== 8. Very short tbl fields (<15 chars) ===")
short_tbl = []
for line in lines:
    id_m = re.search('id:"([^"]+)"', line)
    tbl_m = re.search(',tbl:"([^"]+)"', line)
    if tbl_m:
        tbl = tbl_m.group(1)
        if len(tbl) < 15:
            short_tbl.append((id_m.group(1) if id_m else '?', tbl))
for id_,tbl in short_tbl[:10]:
    print("  %s: tbl=%r" % (id_,tbl))
if not short_tbl:
    print("  None")
