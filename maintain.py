"""
maintain.py - Mapzimus board maintenance
Run after adding any new ideas: python maintain.py

Steps (in order):
  1. compact      - rebuild data.js from scratch, deduplicate, strip all blank lines
  2. fix_chars    - replace non-ASCII chars that cause browser rendering issues
  3. add_ext      - patch ext[] sources onto ideas missing them
  4. normalize_fmt- collapse fmt variants to 15 canonical categories
  5. validate     - count ideas, check holes/dupes, report fmt distribution
"""
import re, sys
from collections import Counter, OrderedDict

# ── 1. COMPACT ────────────────────────────────────────────────────────────────
def compact():
    """Rebuild data.js: deduplicate, strip blank lines, fix leading comma."""
    with open('data.js', 'r', encoding='utf-8') as f:
        content = f.read()
    if content.startswith('\ufeff'):
        content = content[1:]

    # Extract all unique ideas in order
    ideas = OrderedDict()
    for m in re.finditer(r',?\{id:"([^"]+)",[^\n]+\}', content):
        id_val = m.group(1)
        if id_val not in ideas:
            ideas[id_val] = m.group(0).lstrip(',')

    # Rebuild cleanly
    vals = list(ideas.values())
    body = '\n'.join([vals[0]] + [',' + v for v in vals[1:]])
    clean = '// data.js - Mapzimus master idea database\nconst D =[\n' + body + '\n]; // end D\n'

    with open('data.js', 'w', encoding='utf-8') as f:
        f.write(clean)
    print(f'  [compact] {len(ideas)} ideas | {round(len(clean)/1024,1)} KB')

# ── 2. FIX CHARS ─────────────────────────────────────────────────────────────
def fix_chars():
    """Replace non-ASCII chars that cause browser rendering issues."""
    changed = 0
    for filename in ['data.js', 'app.js']:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        new = content.replace('\u00b7', ' - ').replace('\u00b2', '2')
        new = new.replace('\u2014', '-').replace('\u2013', '-')
        if new != content:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(new)
            changed += 1
    if changed:
        print(f'  [fix_chars] Fixed in {changed} file(s)')

# ── 3. ADD EXT ────────────────────────────────────────────────────────────────
ACS        = 'ACS 5-year estimates: MHI, poverty rate, population by geography (Census API - free, tidycensus)'
BEA_STATE  = 'BEA Regional: GDP + personal income per capita by state (apps.bea.gov - free)'
BEA_METRO  = 'BEA Regional: GDP + personal income per capita by metro (apps.bea.gov - free)'
CENSUS_POP = 'Census Population Estimates: annual population by state/county (census.gov - free)'
BLS_STATE  = 'BLS LAUS: unemployment + labor force by state (bls.gov - free)'
BLS_COUNTY = 'BLS LAUS: unemployment + labor force by county (bls.gov - free)'
BLS_METRO  = 'BLS LAUS: unemployment + labor force by metro (bls.gov - free)'
BLS_NAT    = 'BLS national data: employment, wages, CPI (bls.gov - free API)'
FRED       = 'FRED: any national economic time series (fred.stlouisfed.org - free API)'
WORLD_BANK = 'World Bank Open Data: GDP, population, income by country (data.worldbank.org - free API)'
CDC_WONDER = 'CDC WONDER: mortality + disease rates by county/state (wonder.cdc.gov - free)'
FBI_UCR    = 'FBI Crime Data Explorer: UCR/NIBRS by state/agency (cde.ucr.cjis.gov - free)'
EIA_SEDS   = 'EIA State Energy Data System: production + consumption by state (eia.gov - free API)'
USDA_ERS   = 'USDA ERS: food environment, rural classification, farm income (ers.usda.gov - free)'
MIT_ELAB   = 'MIT Election Lab: presidential/congressional results (electionlab.mit.edu - free)'
HUD_FAIR   = 'HUD Fair Market Rents + housing data by state/county (huduser.gov - free)'

GEO_RULES = {
    'us_state':    [ACS, BEA_STATE, CENSUS_POP, BLS_STATE],
    'us_county':   [ACS, CENSUS_POP, BLS_COUNTY],
    'us_metro':    [ACS, BEA_METRO, BLS_METRO],
    'us_city':     [ACS],
    'us_national': [FRED, BLS_NAT],
    'worldwide':   [WORLD_BANK],
    'top_n_list':  [],
}
SECTION_BONUS = [
    (['Health', 'health'],               CDC_WONDER),
    (['Crime', 'Law Enforcement'],        FBI_UCR),
    (['Energy', 'energy', 'coal'],        EIA_SEDS),
    (['Agriculture', 'farm'],             USDA_ERS),
    (['Elections', 'vote', 'election'],   MIT_ELAB),
    (['Housing', 'housing', 'mortgage'],  HUD_FAIR),
]

def build_ext(geo, section):
    sources = list(GEO_RULES.get(geo, []))
    for keywords, source in SECTION_BONUS:
        if any(kw.lower() in section.lower() for kw in keywords):
            if source not in sources:
                sources.append(source)
    return sources

def add_ext():
    with open('data.js', 'r', encoding='utf-8') as f:
        lines = f.readlines()
    out, modified, skipped = [], 0, 0
    for line in lines:
        if not re.search(r',?\{id:"', line):
            out.append(line); continue
        if 'ext:[' in line:
            skipped += 1; out.append(line); continue
        geo_m     = re.search(r'geo:"([^"]*)"', line)
        section_m = re.search(r'section:"([^"]*)"', line)
        geo     = geo_m.group(1) if geo_m else ''
        section = section_m.group(1) if section_m else ''
        sources = build_ext(geo, section)
        ext_str = 'ext:[' + ','.join(f'"{s}"' for s in sources) + ']' if sources else 'ext:[]'
        if 'vars:[' in line:
            out.append(line.replace('vars:[', ext_str + ',vars:[', 1))
            modified += 1
        else:
            out.append(line)
    with open('data.js', 'w', encoding='utf-8') as f:
        f.writelines(out)
    print(f'  [add_ext] Modified: {modified} | Skipped: {skipped}')

# ── 4. NORMALIZE FMT ─────────────────────────────────────────────────────────
FMT_RULES = [
    (r'^Scatter',              'Scatter plot'),
    (r'^State choropleth',     'State choropleth'),
    (r'^Side.by.side state',   'State choropleth'),
    (r'^City map',             'City map'),
    (r'^County choropleth',    'County choropleth'),
    (r'^H3 hexbin',            'H3 hexbin map'),
    (r'^Bivariate choropleth', 'Bivariate choropleth'),
    (r'^Bivariate$',           'Bivariate choropleth'),
    (r'^World choropleth',     'World choropleth'),
    (r'^World bubble',         'World choropleth'),
    (r'^Dot map',              'Dot map'),
    (r'^Flow map',             'Dot map'),
    (r'^Continuous raster',    'Special map'),
    (r'^Special map',          'Special map'),
    (r'^Quadrant',             'Quadrant chart'),
    (r'^Dual.line|^Multi.line|^Line chart|^Dual.axis', 'Line chart'),
    (r'^Dual area|^Area chart|^Stacked area', 'Area chart'),
    (r'^Grouped|^Stacked bar|^Horizontal bar|^Diverging|^Side.by.side bar|^Bar chart|^Pareto|^Pie chart|^Demographic', 'Bar chart'),
    (r'^Treemap',              'Treemap'),
    (r'^Horizontal ranked|^Ranked|^Top/bottom|^River flow|^RANKED', 'Ranked list'),
]

def get_canonical(fmt_str):
    prefix = re.split(r'\s*[-—–]\s*', fmt_str)[0].strip()
    for pattern, canonical in FMT_RULES:
        if re.match(pattern, prefix, re.IGNORECASE):
            return canonical
    return prefix

def normalize_fmt():
    with open('data.js', 'r', encoding='utf-8') as f:
        content = f.read()
    changes = [0]
    def replace(m):
        orig = m.group(1)
        canon = get_canonical(orig)
        if canon != orig:
            changes[0] += 1
            return f'fmt:"{canon}"'
        return m.group(0)
    result = re.sub(r'fmt:"([^"]+)"', replace, content)
    with open('data.js', 'w', encoding='utf-8') as f:
        f.write(result)
    fmts = Counter(re.findall(r'fmt:"([^"]+)"', result))
    print(f'  [normalize_fmt] Changed: {changes[0]} | Categories: {len(fmts)}')
    for k, n in sorted(fmts.items(), key=lambda x: -x[1]):
        print(f'    {n:4d}  {k}')

# ── 5. VALIDATE ───────────────────────────────────────────────────────────────
def validate():
    with open('data.js', 'r', encoding='utf-8') as f:
        content = f.read()
    ids = re.findall(r'\{id:"([^"]+)"', content)
    dupes = [k for k, n in Counter(ids).items() if n > 1]
    doubles = len(re.findall(r',\s*,', content))
    ends = len(re.findall(r'\];\s*//\s*end D', content))
    size_kb = round(len(content)/1024, 1)
    print(f'  [validate] Ideas: {len(ids)} | Dupes: {dupes or "none"} | Double commas: {doubles} | End markers: {ends} | Size: {size_kb} KB')
    bad = [t for t in re.findall(r'type:"([^"]+)"', content) if t not in {'MAP','RANK','XREF','CHART'}]
    if bad:
        print(f'  [validate] BAD TYPES: {Counter(bad)}')

# ── MAIN ──────────────────────────────────────────────────────────────────────
if __name__ == '__main__':
    print('Running maintain.py...')
    compact()
    fix_chars()
    add_ext()
    normalize_fmt()
    validate()
    print('Done. Run: git add . && git commit -m "..." && git push')
