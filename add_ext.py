"""
add_ext.py — batch-inject ext[] proxy data sources into all mapzimus ideas
that don't already have one, based on geo + section rules.
"""
import re

# ── SOURCE LIBRARY ────────────────────────────────────────────────────────────

ACS        = "ACS 5-year estimates: MHI, poverty rate, population by geography (Census API — free, tidycensus)"
BEA_STATE  = "BEA Regional: GDP + personal income per capita by state (apps.bea.gov — free)"
BEA_METRO  = "BEA Regional: GDP + personal income per capita by metro (apps.bea.gov — free)"
CENSUS_POP = "Census Population Estimates: annual population by state/county (census.gov — free)"
BLS_STATE  = "BLS LAUS: unemployment + labor force by state (bls.gov — free)"
BLS_COUNTY = "BLS LAUS: unemployment + labor force by county (bls.gov — free)"
BLS_METRO  = "BLS LAUS: unemployment + labor force by metro (bls.gov — free)"
BLS_NAT    = "BLS national data: employment, wages, CPI (bls.gov — free API)"
FRED       = "FRED: any national economic time series (fred.stlouisfed.org — free API)"
WORLD_BANK = "World Bank Open Data: GDP, population, income by country (data.worldbank.org — free API)"
CDC_WONDER = "CDC WONDER: mortality + disease rates by county/state (wonder.cdc.gov — free)"
FBI_UCR    = "FBI Crime Data Explorer: UCR/NIBRS by state/agency (cde.ucr.cjis.gov — free)"
EIA_SEDS   = "EIA State Energy Data System: production + consumption by state (eia.gov — free API)"
USDA_ERS   = "USDA ERS: food environment, rural classification, farm income (ers.usda.gov — free)"
MIT_ELAB   = "MIT Election Lab: presidential/congressional results (electionlab.mit.edu — free)"
HUD_FAIR   = "HUD Fair Market Rents + housing data by state/county (huduser.gov — free)"

# ── GEO BASE RULES ────────────────────────────────────────────────────────────

GEO_RULES = {
    "us_state":   [ACS, BEA_STATE, CENSUS_POP, BLS_STATE],
    "us_county":  [ACS, CENSUS_POP, BLS_COUNTY],
    "us_metro":   [ACS, BEA_METRO, BLS_METRO],
    "us_city":    [ACS],
    "us_national":[FRED, BLS_NAT],
    "worldwide":  [WORLD_BANK],
    "top_n_list": [],
}

# ── SECTION BONUS RULES (keyword → additional source) ────────────────────────

SECTION_BONUS = [
    (["Health", "healthcare", "health"],        CDC_WONDER),
    (["Crime", "Law Enforcement", "murder"],     FBI_UCR),
    (["Energy", "energy", "coal", "renewable"],  EIA_SEDS),
    (["Agriculture", "farming", "farm"],         USDA_ERS),
    (["Elections", "vote", "election"],          MIT_ELAB),
    (["Housing", "housing", "mortgage"],         HUD_FAIR),
]

# ── HELPERS ───────────────────────────────────────────────────────────────────

def get_field(line, field):
    """Extract a simple string field value like geo:"us_state" """
    m = re.search(rf'{field}:"([^"]*)"', line)
    return m.group(1) if m else ""

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

# ── MAIN ──────────────────────────────────────────────────────────────────────

with open("data.js", "r", encoding="utf-8") as f:
    raw = f.read()

lines = raw.split("\n")
out = []
modified = 0
skipped_has_ext = 0

for line in lines:
    # Only process lines that are idea objects
    if not re.search(r',?\{id:"', line):
        out.append(line)
        continue

    # Already has ext: — leave it alone
    if "ext:[" in line:
        skipped_has_ext += 1
        out.append(line)
        continue

    # Extract geo + section
    geo     = get_field(line, "geo")
    section = get_field(line, "section")

    sources = build_ext(geo, section)
    ext_str = ext_js(sources)

    # Insert ext:[...], right before vars:[
    if "vars:[" in line:
        new_line = line.replace("vars:[", ext_str + ",vars:[", 1)
        out.append(new_line)
        modified += 1
    else:
        out.append(line)

result = "\n".join(out)

with open("data.js", "w", encoding="utf-8") as f:
    f.write(result)

print(f"Done.")
print(f"  Modified (ext added): {modified}")
print(f"  Skipped (had ext):    {skipped_has_ext}")
print(f"  Total lines:          {len(out)}")
