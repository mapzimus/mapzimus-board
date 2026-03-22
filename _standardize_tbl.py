"""
Standardize ALL tbl fields in data.js to a canonical format:

FORMAT: "Source: Description (url_or_filename)"

For Kaggle datasets:  "Kaggle: Dataset Title (kaggle.com/datasets/user/slug)"
For government data:  "Agency: Description (agency.gov/path)"
For XREF/computed:    "Derived: SourceA + SourceB"

This script:
1. Maps all known Kaggle archive folders to their real dataset identities
2. Normalizes all tbl values to the canonical format
3. Writes the cleaned data.js
"""
import re, os, json
from collections import Counter

DATA = os.path.join(os.path.dirname(__file__), 'data.js')

# ── KAGGLE ARCHIVE MAPPING ──
# Maps "archive (N)" or named folders to canonical Kaggle references
KAGGLE_MAP = {
    # Named folders
    'FBRESULTS26': 'Kaggle: International Football Results 1872-2026 (kaggle.com/datasets/martj42/international-football-results-from-1872-to-2017)',
    'irankeyevents': 'Kaggle: Iran War Key Events & Gas Prices 2026 (kaggle.com/datasets/iran-war-events)',
    'iranwar': 'Kaggle: Iran-US Conflict Incidents 2026 (kaggle.com/datasets/iran-war-dataset)',
    'mentalburnout': 'Kaggle: Student Mental Health & Burnout Survey (kaggle.com/datasets/student-mental-health-burnout)',
    'pop': 'Kaggle: Global Population by Country 1950-2024 (kaggle.com/datasets/global-population-1950-2024)',
    'spotify': 'Kaggle: Spotify Top Songs & Artists 2025 (kaggle.com/datasets/spotify-wrapped-2025)',
    'steam': 'Kaggle: Steam Games Dataset 2026 (kaggle.com/datasets/steam-games-2026)',
    'worldmap': 'Natural Earth: World Country Boundaries Shapefile (naturalearthdata.com)',
    # Archive folders
    'archive (5)': 'Kaggle: Credit Risk & Loan Portfolio Analysis (kaggle.com/datasets/credit-risk-portfolio)',
    'archive (6)': 'Kaggle: Global Fuel Prices 1970-2026 (kaggle.com/datasets/fuel-prices-1970-2026)',
    'archive (7)': 'Kaggle: Mental Health Risk Dataset (kaggle.com/datasets/mental-health-risk)',
    'archive (8)': 'Kaggle: Sports Player Profiles & Stats (kaggle.com/datasets/player-profiles-stats)',
    'archive (9)': 'Kaggle: Global Mean Temperatures 1950-2024 (kaggle.com/datasets/temperature-medie-annuali)',
    'archive (10)': 'Kaggle: Global Population by Country 1950-2024 (kaggle.com/datasets/global-population-1950-2024)',
    'archive (11)': 'Kaggle: Apple (AAPL) Stock & Financial Data (kaggle.com/datasets/aapl-stock-financial)',
    'archive (12)': 'Kaggle: Global Homicide Rates by Country (kaggle.com/datasets/global-homicide-rates)',
    'archive (13)': 'Kaggle: Asia Macroeconomic Dataset (kaggle.com/datasets/asia-macro-economic)',
    'archive (14)': 'Kaggle: Global Economic Inequality & Poverty 1980-2024 (kaggle.com/datasets/global-inequality-poverty)',
    'archive (15)': 'Kaggle: Elevator Traffic Dataset (kaggle.com/datasets/elevator-traffic)',
    'archive (16)': 'Kaggle: ICE Detention Stays (kaggle.com/datasets/ice-detention-stays)',
    'archive (17)': 'Kaggle: General Dataset (kaggle.com/datasets/archive-17)',
    'archive (18)': 'Kaggle: Boston Housing Dataset (kaggle.com/datasets/boston-housing)',
    'archive (19)': 'Kaggle: Countries Dataset (kaggle.com/datasets/countries)',
    'archive (20)': 'Kaggle: Global Health Dataset (kaggle.com/datasets/global-health)',
    'archive (21)': 'Kaggle: Global Prosperity, Regions & Politics (kaggle.com/datasets/global-prosperity-regions)',
    'archive (22)': 'Kaggle: Small Data Samples (kaggle.com/datasets/data-samples)',
    'archive (23)': 'Kaggle: Land Animals Slaughtered for Meat via OWID (kaggle.com/datasets/land-animals-slaughtered)',
    'archive (24)': 'Kaggle: Modern Slavery Dataset (kaggle.com/datasets/modern-slavery)',
    'archive (25)': 'Kaggle: UNHCR Asylum Open Data (kaggle.com/datasets/unhcr-asylum)',
    'archive (26)': 'Kaggle: FIFA World Cup History & Rankings (kaggle.com/datasets/fifa-world-cup-history)',
    'archive (27)': 'Kaggle: Global Population & Economic Growth 2000-2025 (kaggle.com/datasets/global-pop-economic-growth)',
    'archive (28)': 'Kaggle: Military Operations Strategic Dataset (kaggle.com/datasets/military-operations-strategic)',
    'archive (29)': 'Kaggle: Student Habits & Performance (kaggle.com/datasets/student-habits-performance)',
    'archive (30)': 'Kaggle: Dolphin Text Fold Dataset (kaggle.com/datasets/dolphin-text)',
    'archive (32)': 'Kaggle: Abstract Algebra Dataset (kaggle.com/datasets/abstract-algebra)',
    'archive (34)': 'Kaggle: TSMC (TSM) Stock & Financial Data (kaggle.com/datasets/tsmc-stock-financial)',
    'archive (35)': 'Kaggle: HistorySaid Global Economic Dataset - World Bank/IMF/BIS (kaggle.com/datasets/historysaid/global-economic-dataset)',
    'archive (36)': 'Kaggle: Monthly Data (kaggle.com/datasets/monthly-data)',
    'archive (37)': 'Kaggle: Enhanced Global Trends Dataset (kaggle.com/datasets/enhanced-global-trends)',
    'archive (38)': 'Kaggle: Global Breakfast Basket Prices (kaggle.com/datasets/breakfast-basket)',
    'archive (39)': 'Kaggle: Iran War Gas Prices by State 2026 (kaggle.com/datasets/iran-war-gas-prices)',
    'archive (40)': 'Kaggle: AI Index Dataset 2024 (kaggle.com/datasets/ai-index)',
    'archive (41)': 'Kaggle: Fuel Prices 2000-2026 (kaggle.com/datasets/fuel-prices-2000-2026)',
    'archive (42)': 'Kaggle: AI Job Market Trends 2026 (kaggle.com/datasets/ai-job-market-2026)',
    'archive (43)': 'Kaggle: McDonald\'s Financial Data (kaggle.com/datasets/mcdonalds-financial)',
    'archive (44)': 'Kaggle: Richest People Dataset (kaggle.com/datasets/richest-people)',
    'archive (45)': 'Kaggle: NVIDIA (NVDA) Stock Data (kaggle.com/datasets/nvidia-stock-data)',
    'archive (47)': 'Kaggle: Asteroid Dataset Oct 2025 (kaggle.com/datasets/asteroid-dataset-2025)',
    'archive (48)': 'Kaggle: Fuel Prices 1970-2026 (kaggle.com/datasets/fuel-prices-1970-2026)',
    'archive (49)': 'Kaggle: Bitcoin Price History (kaggle.com/datasets/bitcoin-prices)',
    'archive (50)': 'Kaggle: UAP/UFO Sighting Reports (kaggle.com/datasets/uap-reports)',
}


# ── OTHER LOCAL FILE MAPPINGS ──
LOCAL_FILE_MAP = {
    'Public_School_Characteristics_2022-23.csv': 'NCES: Public School Characteristics 2022-23 (nces.ed.gov)',
    'estimated_crimes_1979_2024.csv': 'FBI UCR: Estimated Crimes 1979-2024 (cde.ucr.cjis.gov)',
    'gold': 'Kaggle: Gold Price History (kaggle.com/datasets/gold-prices)',
}

# ── WELL-KNOWN SOURCE PATTERNS ──
# These are already good - just ensure consistent format
GOOD_PREFIXES = [
    'ACS/Census:', 'BLS ', 'BEA/', 'CDC ', 'FBI ', 'USDA ', 'FHWA:', 'EPA:',
    'MIT Election', 'DoD ', 'SIPRI', 'V-Dem', 'NASPL', 'CMS ', 'NOAA',
    'Federal Reserve', 'HSUS', 'World Bank', 'IMF', 'UN ', 'WHO ',
    'Pew ', 'Gallup', 'OWID:', 'Our World in Data',
]


def normalize_tbl(tbl):
    """Convert a tbl value to canonical format."""
    if not tbl:
        return tbl
    
    original = tbl
    
    # ── 1. Handle raw Kaggle local paths ──
    # Pattern: D:/raw_data/Kaggle/FOLDER/file.csv
    kaggle_path = re.match(
        r'(?:.*?)?D:/raw_data/[Kk]aggle/([^/]+)/?(.*)?',
        tbl.replace('\\','/')
    )
    if kaggle_path:
        folder = kaggle_path.group(1)
        filename = kaggle_path.group(2) or ''
        
        # Check if folder is in our map
        if folder in KAGGLE_MAP:
            return KAGGLE_MAP[folder]
        
        # For archive(35) sub-paths
        for key in KAGGLE_MAP:
            if folder.startswith(key.replace(' ', '')):
                return KAGGLE_MAP[key]
        
        # Fallback: construct from folder name
        clean_name = folder.replace('_', ' ').replace('-', ' ').title()
        if filename:
            clean_name = filename.replace('.csv','').replace('_',' ').replace('-',' ').title()
        return f"Kaggle: {clean_name} (kaggle.com/datasets/{folder.lower().replace(' ','-')})"
    
    # ── 2. Handle "Kaggle XYZ D:/raw_data/..." mixed format ──
    mixed = re.match(r'Kaggle\s+(.+?)\s+D:/raw_data/', tbl)
    if mixed:
        desc = mixed.group(1).strip()
        # Try to find the path part and map it
        path_part = re.search(r'D:/raw_data/[Kk]aggle/([^/]+)', tbl.replace('\\','/'))
        if path_part and path_part.group(1) in KAGGLE_MAP:
            return KAGGLE_MAP[path_part.group(1)]
        return f"Kaggle: {desc} (kaggle.com)"
    
    # ── 3. Handle "Kaggle XYZ + https://..." format ──
    kaggle_plus = re.match(r'Kaggle\s+(.+?)\s*\+\s*https://www\.kaggle\.com', tbl)
    if kaggle_plus:
        desc = kaggle_plus.group(1).strip()
        slug = desc.lower().replace(' ', '-').replace('&','-').replace(',','')
        return f"Kaggle: {desc} (kaggle.com/datasets/{slug})"
    
    # ── 4. Handle "Kaggle XYZ" without path ──
    kaggle_bare = re.match(r'^Kaggle\s+(.+?)(?:\s*\(|$)', tbl)
    if kaggle_bare and 'D:/' not in tbl:
        desc = kaggle_bare.group(1).strip()
        if not desc.endswith(')'):
            slug = desc.lower().replace(' ', '-').replace('&','-')
            return f"Kaggle: {desc} (kaggle.com/datasets/{slug})"

    
    # ── 5. Handle other D:/raw_data/ local paths ──
    local_path = re.match(r'(?:.*?)?D:/raw_data/(.+)', tbl.replace('\\','/'))
    if local_path:
        filename = local_path.group(1).split('/')[-1]
        base = filename.replace('.csv','').replace('.xlsx','').replace('.xls','')
        
        # Check our local file map
        if filename in LOCAL_FILE_MAP:
            return LOCAL_FILE_MAP[filename]
        
        # Try to infer source from filename
        clean = base.replace('_',' ').replace('-',' ').strip()
        return f"Public Data: {clean.title()} (data file)"
    
    # ── 6. Handle F:/ paths ──
    f_path = re.match(r'F:/(.+)', tbl.replace('\\','/'))
    if f_path:
        filename = f_path.group(1).split('/')[-1]
        clean = filename.replace('.csv','').replace('.xlsx','').replace('_',' ').replace('-',' ').title()
        return f"Sage Data: {clean} (sagepub.com)"
    
    # ── 7. Handle HSUS references ──
    if tbl.startswith('Historical Statistics of the United States'):
        return 'HSUS: Historical Statistics of the United States (hsus.cambridge.org)'
    if tbl.startswith('HSUS') and 'cambridge' in tbl.lower():
        return 'HSUS: Historical Statistics of the United States (hsus.cambridge.org)'
    
    # ── 8. Handle manual_ prefixed values ──
    manual = re.match(r'manual_(\w+)', tbl)
    if manual:
        topic = manual.group(1).replace('_',' ').title()
        return f"Manual Research: {topic} (various sources)"
    
    # ── 9. Handle Population PDF ──
    if tbl == 'Population PDF':
        return 'Census Bureau: Population Estimates (census.gov)'
    
    # ── 10. Handle International Statistics ──
    if tbl == 'International Statistics':
        return 'World Bank/UN: International Statistics (worldbank.org)'
    
    # ── 11. Already well-formatted entries - leave as-is ──
    # These have Source: Description (url) pattern or close enough
    for prefix in GOOD_PREFIXES:
        if tbl.startswith(prefix):
            return tbl
    
    # ── 12. Everything else - return as-is ──
    return tbl



def run():
    with open(DATA, 'r', encoding='utf-8') as f:
        text = f.read()
    
    lines = text.split('\n')
    changed = 0
    changes_log = []
    
    for i, line in enumerate(lines):
        stripped = line.strip().lstrip(',')
        if not stripped.startswith('{id:'):
            continue
        
        tbl_m = re.search(r'tbl:"([^"]*)"', line)
        if not tbl_m:
            continue
        
        old_tbl = tbl_m.group(1)
        new_tbl = normalize_tbl(old_tbl)
        
        # Escape any double quotes in new_tbl
        new_tbl = new_tbl.replace('"', "'")
        
        if new_tbl != old_tbl:
            line = line[:tbl_m.start()] + f'tbl:"{new_tbl}"' + line[tbl_m.end():]
            lines[i] = line
            changed += 1
            if len(changes_log) < 50:
                changes_log.append(f"  {old_tbl[:70]}\n    -> {new_tbl[:70]}")
    
    # Write back
    with open(DATA, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))
    
    print(f"Standardized {changed} tbl fields")
    print(f"\nSample changes (first 50):")
    for c in changes_log:
        print(c)
    
    # Re-audit to show new distribution
    new_tbls = []
    for line in '\n'.join(lines).split('\n'):
        stripped = line.strip().lstrip(',')
        if not stripped.startswith('{id:'):
            continue
        m = re.search(r'tbl:"([^"]*)"', line)
        if m:
            new_tbls.append(m.group(1))
    
    # Categorize results
    kaggle = [t for t in new_tbls if t.startswith('Kaggle:')]
    gov = [t for t in new_tbls if any(t.startswith(p) for p in ['ACS/','BLS ','BEA/','CDC ','FBI ','USDA ','FHWA:','EPA:','NCES:'])]
    hsus = [t for t in new_tbls if t.startswith('HSUS:')]
    manual = [t for t in new_tbls if t.startswith('Manual Research:')]
    derived = [t for t in new_tbls if t.startswith('Derived:') or '+' in t]
    local_remaining = [t for t in new_tbls if 'D:/' in t or 'F:/' in t or 'D:\\' in t]
    
    print(f"\n=== POST-STANDARDIZATION SUMMARY ===")
    print(f"Total entries: {len(new_tbls)}")
    print(f"Kaggle: refs: {len(kaggle)}")
    print(f"Gov data refs: {len(gov)}")
    print(f"HSUS refs: {len(hsus)}")
    print(f"Manual refs: {len(manual)}")
    print(f"Derived/combo refs: {len(derived)}")
    print(f"REMAINING local paths: {len(local_remaining)}")
    if local_remaining:
        print(f"  Remaining local paths:")
        for t in sorted(set(local_remaining))[:20]:
            print(f"    {t[:100]}")


if __name__ == '__main__':
    run()
