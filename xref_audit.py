import re, collections

with open(r'D:\projects\mapzimus-board\data.js', 'r', encoding='utf-8') as f:
    raw = f.read()

# data.js uses JS object syntax with unquoted keys like {id:"foo", title:"bar",...}
# Strategy: split on top-level commas between objects, then parse each block

# Split into per-idea chunks by finding ,{ boundaries at top level
# Each idea starts with {id:"
chunks = re.split(r'\n,\{', raw)
print(f"Chunks: {len(chunks)}")

def extract(block, field):
    # handles both quoted and unquoted keys
    m = re.search(rf'\b{field}\s*:\s*"((?:[^"\\]|\\.)*)\"', block)
    return m.group(1) if m else ''

def extract_arr(block, field):
    m = re.search(rf'\b{field}\s*:\s*\[([^\]]*)\]', block)
    if m:
        return re.findall(r'"([^"]+)"', m.group(1))
    return []

ideas = []
for chunk in chunks:
    if 'id:' not in chunk and '"id"' not in chunk:
        continue
    chunk = '{' + chunk.lstrip('{')
    idea = {
        'id':      extract(chunk, 'id'),
        'title':   extract(chunk, 'title'),
        'type':    extract(chunk, 'type'),
        'geo':     extract(chunk, 'geo'),
        'section': extract(chunk, 'section'),
        'tags':    extract(chunk, 'tags'),
        'vars':    extract_arr(chunk, 'vars'),
        'join':    extract_arr(chunk, 'join'),
        'status':  extract(chunk, 'status'),
    }
    if idea['id']:
        ideas.append(idea)

print(f"Valid ideas: {len(ideas)}")
print(f"\nTypes: {dict(collections.Counter(i['type'] for i in ideas).most_common())}")
print(f"\nGeo: {dict(collections.Counter(i['geo'] for i in ideas).most_common())}")

xref_ideas = [i for i in ideas if i['type'] == 'XREF']
print(f"\nExisting XREF ideas: {len(xref_ideas)}")

# Variable frequency across ALL ideas
all_vars = collections.Counter()
for i in ideas:
    for v in i['vars'] + i['join']:
        if v: all_vars[v] += 1

print(f"\nTop 40 most-used variables:")
for v, c in all_vars.most_common(40):
    print(f"  {v}: {c}")

print(f"\nSections covered:")
for sec, c in collections.Counter(i['section'] for i in ideas).most_common():
    print(f"  {sec}: {c}")

# Tag gap check for new dataset themes
new_themes = {
    'regime/democracy/autocracy': ['regime','autocracy','liberal democracy','electoral'],
    'water/drinking': ['water','drinking','sanitation'],
    'dependency ratio': ['dependency','elderly ratio','old-age'],
    'median age': ['median age'],
    'population projections 2100': ['projection','2100','future population'],
    'youth burden': ['youth burden','youth dependency','children per worker'],
    'natural growth rate': ['natural growth','natural increase'],
    'migration vs natural growth': ['natural growth rate','migration contribution'],
    'Africa demographic': ['africa demographic','african population boom'],
    'children by region': ['children by region','under 15 region'],
}
print(f"\n=== TAG/TITLE GAP ANALYSIS for new dataset themes ===")
for theme_group, keywords in new_themes.items():
    hits = []
    for kw in keywords:
        for i in ideas:
            combined = (i['tags'] + ' ' + i['title'] + ' ' + i['section']).lower()
            if kw.lower() in combined and i not in hits:
                hits.append(i)
    print(f"\n  Theme '{theme_group}': {len(hits)} existing ideas")
    for i in hits[:4]:
        print(f"    - {i['id']}: {i['title'][:70]}")

# Worldwide XREF ideas
world_xref = [i for i in ideas if i['geo'] in ('worldwide','world') and i['type'] == 'XREF']
print(f"\n=== Worldwide XREF ideas: {len(world_xref)} ===")
for i in world_xref:
    print(f"  {i['id']}: {i['title'][:65]}")
    print(f"    vars={i['vars']} join={i['join'][:3]}")

# All existing vars in worldwide ideas (to find gaps)
world_all = [i for i in ideas if i['geo'] in ('worldwide','world')]
world_vars = collections.Counter()
for i in world_all:
    for v in i['vars'] + i['join']:
        if v: world_vars[v] += 1
print(f"\nVariables used in worldwide ideas:")
for v, c in world_vars.most_common(30):
    print(f"  {v}: {c}")
