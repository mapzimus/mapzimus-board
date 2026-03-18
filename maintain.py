"""
maintain.py - Mapzimus board maintenance
Run after adding any new ideas: python maintain.py

Does three things in order:
  1. fix_encoding  - strips BOM, fixes double-encoded chars, ensures closing bracket
  2. add_ext       - patches ext[] sources onto ideas missing them (geo + section rules)
  3. normalize_fmt - collapses fmt variants to 15 canonical categories
  4. validate      - counts ideas, checks for holes/dupes, reports fmt distribution
"""
import re, sys
from collections import Counter

# ── 1. FIX ENCODING ──────────────────────────────────────────────────────────

def fix_encoding():
    with open('data.js', 'rb') as f:
        raw = f.read()
    if raw[:3] == b'\xef\xbb\xbf':
        raw = raw[3:]
        print('  [fix_encoding] Stripped BOM')
    text = raw.decode('utf-8')
    text = text.replace('\u00e2\u0080\u0094', '\u2014')
    text = text.replace('\u00e2\u0080\u0093', '\u2013')
    text = text.replace('â€"', '\u2014')
    text = text.replace('â€™', "'")
    # Fix sparse array holes: ,<whitespace>, -> single comma
    before = len(re.findall(r',\s*,', text))
    if before:
        text = re.sub(r',(\s*),', r',\1', text)
        print(f'  [fix_encoding] Fixed {before} double-comma(s)')
    # Ensure closing bracket
    if not text.rstrip().endswith(']; // end D'):
        text = text.rstrip() + '\n]; // end D\n'
        print('  [fix_encoding] Added closing bracket')
    with open('data.js', 'w', encoding='utf-8') as f:
        f.write(text)

# ── 2. ADD EXT ────────────────────────────────────────────────────────────────

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

def ext_js(sources):
    if not sources:
        return 'ext:[]'
    parts = ','.join(f'"{s}"' for s in sources)
    return f'ext:[{parts}]'

def add_ext():
    with open('data.js', 'r', encoding='utf-8') as f:
        lines = f.readlines()
    out, modified, skipped = [], 0, 0
    for line in lines:
        if not re.search(r',?\{id:"', line):
            out.append(line)
            continue
        if 'ext:[' in line:
            skipped += 1
            out.append(line)
            continue
        geo     = (re.search(r'geo:"([^"]*)"', line) or ['',''])[1] if re.search(r'geo:"([^"]*)"', line) else ''
        section = (re.search(r'section:"([^"]*)"', line) or ['',''])[1] if re.search(r'section:"([^"]*)"', line) else ''
        sources = build_ext(geo, section)
        ext_str = ext_js(sources)
        if 'vars:[' in line:
            out.append(line.replace('vars:[', ext_str + ',vars:[', 1))
            modified += 1
        else:
            out.append(line)
    with open('data.js', 'w', encoding='utf-8') as f:
        f.writelines(out)
    print(f'  [add_ext] Modified: {modified} | Skipped (had ext): {skipped}')

# ── 3. NORMALIZE FMT ─────────────────────────────────────────────────────────

FMT_RULES = [
    (r'^Scatter',              'Scatter plot'),
    (r'^State choropleth',     'State choropleth'),
    (r'^Side.by.side state',   'State choropleth'),
    (r'^City map',             'City map'),
    (r'^Side.by.side city',    'City map'),
    (r'^County choropleth',    'County choropleth'),
    (r'^Trivariate county',    'County choropleth'),
    (r'^H3 hexbin',            'H3 hexbin map'),
    (r'^Bivariate choropleth', 'Bivariate choropleth'),
    (r'^Bivariate$',           'Bivariate choropleth'),
    (r'^World choropleth',     'World choropleth'),
    (r'^World bubble',         'World choropleth'),
    (r'^Dot map',              'Dot map'),
    (r'^US dot map',           'Dot map'),
    (r'^Flow map',             'Dot map'),
    (r'^Continuous raster',    'Special map'),
    (r'^Three.panel',          'Special map'),
    (r'^Special map',          'Special map'),
    (r'^Quadrant',             'Quadrant chart'),
    (r'^Ranked scatter',       'Quadrant chart'),
    (r'^Dual.line',            'Line chart'),
    (r'^Multi.line',           'Line chart'),
    (r'^Line chart',           'Line chart'),
    (r'^Dual.axis',            'Line chart'),
    (r'^Dual area',            'Area chart'),
    (r'^Area chart',           'Area chart'),
    (r'^Stacked area',         'Area chart'),
    (r'^Grouped bar',          'Bar chart'),
    (r'^Grouped ranked bar',   'Bar chart'),
    (r'^Stacked bar',          'Bar chart'),
    (r'^Horizontal bar',       'Bar chart'),
    (r'^Diverging horizontal', 'Bar chart'),
    (r'^Side.by.side bar',     'Bar chart'),
    (r'^Demographic',          'Bar chart'),
    (r'^Pie chart',            'Bar chart'),
    (r'^Bar chart',            'Bar chart'),
    (r'^Pareto',               'Bar chart'),
    (r'^Treemap or stacked',   'Treemap'),
    (r'^Treemap',              'Treemap'),
    (r'^Horizontal ranked',    'Ranked list'),
    (r'^Ranked horizontal',    'Ranked list'),
    (r'^Ranked bar',           'Ranked list'),
    (r'^Ranked list',          'Ranked list'),
    (r'^Top/bottom',           'Ranked list'),
    (r'^River flow',           'Ranked list'),
    (r'^RANKED',               'Ranked list'),
]

def get_canonical(fmt_str):
    prefix = re.split(r'\s*[—–]\s*', fmt_str)[0].strip()
    if prefix == fmt_str.strip():
        prefix = re.split(r'\s+-\s+', fmt_str)[0].strip()
    for pattern, canonical in FMT_RULES:
        if re.match(pattern, prefix, re.IGNORECASE):
            return canonical
    return prefix

def normalize_fmt():
    with open('data.js', 'r', encoding='utf-8') as f:
        content = f.read()
    changes = 0
    def replace(m):
        global changes
        orig = m.group(1)
        canon = get_canonical(orig)
        if canon != orig:
            changes += 1  # noqa
            return f'fmt:"{canon}"'
        return m.group(0)
    result = re.sub(r'fmt:"([^"]+)"', replace, content)
    # Also strip City map suffixes
    result = re.sub(r'fmt:"City map[^"]+"', 'fmt:"City map"', result)
    with open('data.js', 'w', encoding='utf-8') as f:
        f.write(result)
    fmts = Counter(re.findall(r'fmt:"([^"]+)"', result))
    print(f'  [normalize_fmt] Changed: {changes} | Unique categories: {len(fmts)}')
    for k, n in sorted(fmts.items(), key=lambda x: -x[1]):
        print(f'    {n:4d}  {k}')

# ── 4. VALIDATE ───────────────────────────────────────────────────────────────

def validate():
    with open('data.js', 'r', encoding='utf-8') as f:
        content = f.read()
    # Count {id: patterns
    ids = re.findall(r'\{id:"([^"]+)"', content)
    dupes = [k for k, n in Counter(ids).items() if n > 1]
    double_commas = len(re.findall(r',\s*,', content))
    print(f'  [validate] Ideas: {len(ids)} | Dupes: {dupes or "none"} | Double commas: {double_commas}')
    # Check valid types/geos
    valid_types = {'MAP','RANK','XREF','CHART'}
    valid_geos  = {'us_state','us_county','us_metro','us_city','us_national','worldwide','top_n_list'}
    bad_types = re.findall(r'type:"([^"]+)"', content)
    bad = [t for t in bad_types if t not in valid_types]
    if bad:
        print(f'  [validate] BAD TYPES: {Counter(bad)}')

# ── MAIN ──────────────────────────────────────────────────────────────────────

if __name__ == '__main__':
    print('Running maintain.py...')
    fix_encoding()
    add_ext()
    normalize_fmt()
    validate()
    print('Done. Commit with: git add . && git commit -m "..." && git push')
