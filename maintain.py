"""
maintain.py - Mapzimus board maintenance
Run after adding any new ideas: python maintain.py

Steps (in order):
  1. compact      - rebuild data.js from scratch, deduplicate, strip all blank lines
  2. fix_chars    - replace non-ASCII chars that cause browser rendering issues
  3. add_ext      - patch ext[] sources onto ideas missing them
  4. normalize_fmt- collapse fmt variants to 15 canonical categories
  5. recalc_vs    - recalculate all virality scores (v5 algorithm)
  6. validate     - count ideas, check holes/dupes, report fmt distribution
  7. js_check     - run Node.js to confirm valid browser JS
"""
import re, sys
from collections import Counter, OrderedDict

# -- 1. COMPACT ----------------------------------------------------------------
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

# -- 2. FIX CHARS --------------------------------------------------------------
def fix_chars():
    """Strip all non-ASCII and fix JS syntax issues that break the browser."""
    import re as _re
    for filename in ['data.js', 'app.js']:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        new = content
        # Named replacements first (preserve meaning)
        for bad, good in [
            ('\u2014', '-'),   # em dash
            ('\u2013', '-'),   # en dash
            ('\u2019', "'"),   # right single quote
            ('\u2018', "'"),   # left single quote
            ('\u201c', ''),    # left double quote -> remove (breaks JS strings)
            ('\u201d', ''),    # right double quote -> remove
            ('\u2026', '...'), # ellipsis
            ('\u2192', '->'),  # right arrow
            ('\u00b7', ' - '), # middot
            ('\u00b2', '2'),   # superscript 2
            ('\u00b0', ' degrees'), # degree symbol
            ('\u00a0', ' '),   # non-breaking space
            ('\u00d7', 'x'),   # multiplication sign
        ]:
            new = new.replace(bad, good)
        # Nuclear option: strip any remaining non-ASCII
        new = _re.sub(r'[^\x00-\x7F]', '', new)
        # Fix = signs inside sc:{} blocks (should always be :)
        new = _re.sub(
            r'(emotional|relatability|surprise|tension|visual|data_ready|originality)=(\d+)',
            r'\1:\2', new
        )
        if new != content:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(new)
    # Count remaining non-ASCII (should be 0)
    with open('data.js', 'r', encoding='utf-8') as f:
        final = f.read()
    bad_count = len([c for c in final if ord(c) > 127])
    if bad_count:
        print(f'  [fix_chars] WARNING: {bad_count} non-ASCII chars remain!')
    else:
        print(f'  [fix_chars] Clean (0 non-ASCII chars)')

# -- 3. ADD EXT ----------------------------------------------------------------
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

# -- 4. NORMALIZE FMT ----------------------------------------------------------
FMT_RULES = [
    (r'^Scatter|^Quadrant',    'Scatter plot'),
    (r'^State choropleth',     'State choropleth'),
    (r'^Regional choropleth',  'State choropleth'),
    (r'^Side.by.side state',   'State choropleth'),
    (r'^City map',             'City map'),
    (r'^County choropleth',    'County choropleth'),
    (r'^H3 hexbin',            'Special map'),
    (r'^Bivariate choropleth', 'Bivariate choropleth'),
    (r'^Bivariate$',           'Bivariate choropleth'),
    (r'^World choropleth',     'World choropleth'),
    (r'^World bubble',         'World choropleth'),
    (r'^Dot map',              'Dot map'),
    (r'^Flow map',             'Dot map'),
    (r'^Continuous raster',    'Special map'),
    (r'^Special map',          'Special map'),
    (r'^Ranked',               'Ranked list'),
    (r'^Dual.line|^Multi.line|^Line chart|^Dual.axis', 'Line chart'),
    (r'^Dual area|^Area chart|^Stacked area', 'Area chart'),
    (r'^Grouped|^Stacked bar|^Horizontal bar|^Diverging|^Side.by.side bar|^Bar chart|^Pareto|^Pie chart|^Demographic|^Multi$|^Bar or line', 'Bar chart'),
    (r'^Treemap',              'Treemap'),
    (r'^Horizontal ranked|^Ranked|^Top/bottom|^River flow|^RANKED', 'Ranked list'),
]

def get_canonical(fmt_str):
    prefix = re.split(r'\s*[-\u2014\u2013]\s*', fmt_str)[0].strip()
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

# -- 4b. RECALC VS SCORES (v5 algorithm) --------------------------------------

def recalc_vs():
    """Recalculate vs scores using virality formula v5.

    Changes from v4 (informed by multi-perspective audit):
      - visual weight:       2.0  -> 3.0   (thumbnail IS the content)
      - emotional weight:    2.0  -> 2.5   (sharing reflex driver)
      - surprise weight:     1.5  -> 2.0   ("wait WHAT" drives saves)
      - originality weight:  1.5  -> 1.75  (fresh ideas, but familiar topics can still pop)
      - tension weight:      1.5  -> 1.75  (outrage/urgency amplifier)
      - relatability weight: 2.0  -> 2.0   (unchanged — drives shares and comments)
      - clarity weight:      1.25 -> 1.5   (confusion kills virality)
      - data_ready penalty:  0.5  -> 0.35  (idea quality > data feasibility)
      - NEW: floor penalty if any score < 35 (one rotten dimension tanks everything)

    Formula:
      raw     = v*3.0 + e*2.5 + s*2.0 + o*1.75 + t*1.75 + r*2.0 + c*1.5
      base_vs = raw / 14.5
      floor   = 0.85 if min(e,r,c,s,t,v,o) < 35 else 1.0
      penalty = 1 - 0.35 * (1 - data_ready/100)
      vs      = int(base_vs * floor * penalty)
    """
    with open('data.js', 'r', encoding='utf-8') as f:
        content = f.read()

    def parse_sc(sc_str):
        vals = {}
        for m in re.finditer(r'(\w+):(\d+)', sc_str):
            vals[m.group(1)] = int(m.group(2))
        return vals

    def calc_vs(vals, fmt):
        e = vals.get('emotional', 0)
        r = vals.get('relatability', 0)
        c = vals.get('clarity', 0)
        s = vals.get('surprise', 0)
        t = vals.get('tension', 0)
        v = vals.get('visual', 0)
        o = vals.get('originality', 0)
        dr = vals.get('data_ready', 0)
        raw = (v * 3.0 + e * 2.5 + s * 2.0 + o * 1.75 +
               t * 1.75 + r * 2.0 + c * 1.5)
        base_vs = raw / 14.5
        floor = 0.85 if min(e, r, c, s, t, v, o) < 35 else 1.0
        penalty = 1.0 - 0.35 * (1.0 - dr / 100.0)
        return int(base_vs * floor * penalty)

    def replace_vs(line):
        sc_m = re.search(r'sc:\{([^}]+)\}', line)
        fmt_m = re.search(r'fmt:"([^"]*)"', line)
        if not sc_m:
            return line
        fmt = fmt_m.group(1) if fmt_m else ''
        new_vs = calc_vs(parse_sc(sc_m.group(0)), fmt)
        return re.sub(r',vs:\d+', f',vs:{new_vs}', line)

    new_lines = []
    changed = 0
    for line in content.split('\n'):
        if line.startswith('{id:') or line.startswith(',{id:'):
            new_line = replace_vs(line)
            if new_line != line:
                changed += 1
            new_lines.append(new_line)
        else:
            new_lines.append(line)

    result = '\n'.join(new_lines)
    with open('data.js', 'w', encoding='utf-8') as f:
        f.write(result)

    # Report stats
    all_vs = [int(x) for x in re.findall(r',vs:(\d+)', result)]
    samples = all_vs[:5]
    if all_vs:
        import statistics
        print(f'  [recalc_vs] v5 algorithm | Recalculated {changed} scores')
        print(f'    Range: {min(all_vs)}-{max(all_vs)} | Mean: {statistics.mean(all_vs):.1f} | Median: {statistics.median(all_vs):.0f}')
        print(f'    Samples: {samples}')
        print(f'    Floor penalty (<35 on any dimension) | DR penalty coeff: 0.35')
    else:
        print(f'  [recalc_vs] Recalculated {changed} scores | samples: {samples}')

# -- 5. VALIDATE ---------------------------------------------------------------
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


def validate_js():
    """Run Node.js to confirm data.js is syntactically valid JavaScript."""
    import subprocess
    script = (
        "try{"
        "eval(require('fs').readFileSync('data.js','utf8').replace('const D','var D'));"
        "console.log('ok:'+D.length);"
        "}catch(e){console.log('err:'+e.message.substring(0,120));}"
    )
    try:
        r = subprocess.run(['node', '-e', script],
                           capture_output=True, text=True, timeout=30)
        out = r.stdout.strip()
        if out.startswith('ok:'):
            print(f'  [js_check] Valid JS - {out[3:]} ideas parseable in browser')
        else:
            print(f'  [js_check] JS PARSE ERROR: {out}')
            print('  Fix the error above before pushing!')
            sys.exit(1)
    except FileNotFoundError:
        print('  [js_check] Node.js not found - skipping JS validation')
    except subprocess.TimeoutExpired:
        print('  [js_check] Node.js timed out - skipping')

# -- MAIN ----------------------------------------------------------------------
if __name__ == '__main__':
    print('Running maintain.py...')
    compact()
    fix_chars()
    add_ext()
    normalize_fmt()
    recalc_vs()
    validate()
    validate_js()
    print('Done. Run: git add . && git commit -m "..." && git push')
