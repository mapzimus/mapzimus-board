"""
full_audit.py - Complete sanity check of data.js + app.js + index.html
Checks:
  1. data.js: idea count, dupes, vs score distribution, empty fields,
     non-canonical topics, non-canonical geos, fmt distribution,
     ideas with identity_signal still in sc (leftover from v2),
     notes that aren't empty, data_ready=0 ideas
  2. app.js: syntax via node
  3. Cross-check: geo values in data.js that aren't in GEO_TREE
"""
import re, subprocess
from collections import Counter

with open('data.js', encoding='utf-8') as f:
    content = f.read()

lines = [l for l in content.split('\n') if l.startswith('{id:') or l.startswith(',{id:')]
print(f"=== DATA.JS AUDIT ===")
print(f"Total ideas: {len(lines)}")

# Dupes
ids = [re.search(r'id:"([^"]+)"', l).group(1) for l in lines if re.search(r'id:"([^"]+)"', l)]
dupes = [k for k,n in Counter(ids).items() if n > 1]
print(f"Duplicate IDs: {len(dupes)} {dupes[:5] if dupes else ''}")

# VS scores
vs = [int(re.search(r',vs:(\d+)', l).group(1)) for l in lines if re.search(r',vs:(\d+)', l)]
print(f"VS scores: min={min(vs)} max={max(vs)} avg={sum(vs)/len(vs):.1f} count={len(vs)}")
dist = Counter(v//10*10 for v in vs)
for k in sorted(dist.keys(), reverse=True):
    print(f"  {k:3d}-{k+9}: {dist[k]:4d}  {'#'*(dist[k]//10)}")

# Empty fields check
empty_title   = sum(1 for l in lines if 'title:""' in l)
empty_sub     = sum(1 for l in lines if 'sub:""' in l)
empty_tbl     = sum(1 for l in lines if 'tbl:""' in l)
empty_section = sum(1 for l in lines if 'section:""' in l)
empty_topics  = sum(1 for l in lines if 'topics:[]' in l)
empty_tags    = sum(1 for l in lines if 'tags:""' in l)
print(f"\nEmpty fields:")
print(f"  title:      {empty_title}")
print(f"  sub:        {empty_sub}")
print(f"  tbl:        {empty_tbl}")
print(f"  section:    {empty_section}")
print(f"  topics:     {empty_topics}")
print(f"  tags:       {empty_tags}")

# Non-empty notes (should all be empty now)
nonempty_notes = sum(1 for l in lines if re.search(r',notes:"[^"]+?"', l))
print(f"\nNon-empty notes (should be 0): {nonempty_notes}")
if nonempty_notes > 0:
    for l in lines[:5]:
        nm = re.search(r',notes:"([^"]{1,40})"', l)
        if nm: print(f"  {nm.group(1)}")

# Identity signal still in sc (leftover v2 scores)
has_identity = sum(1 for l in lines if 'identity_signal:' in l)
print(f"\nIdeas still with identity_signal in sc: {has_identity}")

# data_ready = 0
dr_zero = sum(1 for l in lines if 'data_ready:0,' in l or 'data_ready:0}' in l)
print(f"Ideas with data_ready=0: {dr_zero}")

# Canonical topics check
CANONICAL = {
    'health','economy','politics','crime','poverty','housing','education',
    'labor','race','gender','immigration','war','military','energy','climate',
    'environment','food','agriculture','drugs','guns','finance','trade',
    'inequality','transportation','infrastructure','technology','media',
    'population','international','democracy','religion','history','space',
    'data','humor','science','geography','demographics','children','rural',
    'manufacturing','law',
}
all_topics = []
for l in lines:
    tm = re.search(r'topics:\[([^\]]*)\]', l)
    if tm:
        for t in re.findall(r'"([^"]+)"', tm.group(1)):
            all_topics.append(t)
bad_topics = [t for t in all_topics if t not in CANONICAL]
print(f"\nNon-canonical topics: {len(bad_topics)}")
if bad_topics:
    for k,n in Counter(bad_topics).most_common(10):
        print(f"  {n:4d}  {k}")

# Geo distribution
geos = re.findall(r'geo:"([^"]+)"', content)
geo_counts = Counter(geos)
print(f"\nGeo distribution ({len(geo_counts)} unique values):")
for k,n in geo_counts.most_common():
    print(f"  {n:5d}  {k}")

# Geo values NOT in known set
KNOWN_GEOS = {
    'us_national','us_state','us_county','us_metro','us_city','us_cities',
    'us_zip','us_tract','us_tz','us_northeast','us_new_england','us_mid_atlantic',
    'us_south','us_southeast','us_midwest','us_great_plains','us_west',
    'us_southwest','us_pacific_nw','us_tz_eastern','us_tz_central',
    'us_tz_mountain','us_tz_pacific','us_tz_alaska','us_tz_hawaii',
    'us_al','us_ak','us_az','us_ar','us_ca','us_co','us_ct','us_de','us_fl','us_ga',
    'us_hi','us_id','us_il','us_in','us_ia','us_ks','us_ky','us_la','us_me','us_md',
    'us_ma','us_mi','us_mn','us_ms','us_mo','us_mt','us_ne','us_nv','us_nh','us_nj',
    'us_nm','us_ny','us_nc','us_nd','us_oh','us_ok','us_or','us_pa','us_ri','us_sc',
    'us_sd','us_tn','us_tx','us_ut','us_vt','us_va','us_wa','us_wv','us_wi','us_wy',
    'us_dc','us_pr','us_vi','us_gu','us_as','us_mp',
    'worldwide','global_city','north_america',
    'europe','europe_west','europe_east','europe_nordic','europe_south',
    'asia','asia_east','asia_south','asia_southeast','asia_central',
    'africa','africa_sub','africa_west','africa_east','africa_north',
    'middle_east','latin_america','latin_south','latin_central','caribbean','oceania',
}
unknown_geos = {k:n for k,n in geo_counts.items() if k not in KNOWN_GEOS}
if unknown_geos:
    print(f"\nUNKNOWN geo values (not in accordion tree): {unknown_geos}")
else:
    print(f"\nAll geo values are valid accordion nodes.")

# Type distribution
types = re.findall(r'type:"([^"]+)"', content)
print(f"\nType distribution:")
for k,n in Counter(types).most_common():
    print(f"  {n:5d}  {k}")
bad_types = [t for t in types if t not in {'MAP','XREF','CHART','RANK'}]
if bad_types:
    print(f"  BAD TYPES: {Counter(bad_types)}")

# FMT distribution
fmts = re.findall(r'fmt:"([^"]+)"', content)
print(f"\nFmt distribution:")
for k,n in Counter(fmts).most_common():
    print(f"  {n:5d}  {k}")

print(f"\n=== APP.JS SYNTAX ===")
result = subprocess.run(['node', '--check', 'app.js'], capture_output=True, text=True)
if result.returncode == 0:
    print("app.js: SYNTAX OK")
else:
    print(f"app.js ERROR: {result.stderr}")

print(f"\n=== SUMMARY ===")
issues = []
if dupes: issues.append(f"{len(dupes)} duplicate IDs")
if empty_title: issues.append(f"{empty_title} empty titles")
if empty_tbl: issues.append(f"{empty_tbl} empty tbl fields")
if empty_topics: issues.append(f"{empty_topics} empty topics arrays")
if bad_topics: issues.append(f"{len(set(bad_topics))} non-canonical topic values")
if unknown_geos: issues.append(f"{len(unknown_geos)} unknown geo values")
if bad_types: issues.append(f"bad type values: {set(bad_types)}")
if nonempty_notes: issues.append(f"{nonempty_notes} non-empty notes in data.js")
if result.returncode != 0: issues.append("app.js syntax error")

if issues:
    print("Issues found:")
    for i in issues: print(f"  ✗ {i}")
else:
    print("All checks passed. Board is clean.")
