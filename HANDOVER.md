# @mapzimus Board — Handover Blueprint
**Last updated:** March 2026 | **Status:** Live at mapzimus.github.io/mapzimus-board

---

## 1. What This Project Is

A password-protected, self-hosted viral infographic idea board for the Instagram/Reddit account **@mapzimus** (Max Howe, Boston area). It is a single-page web app that stores and filters a curated list of map/chart/infographic ideas, each scored by a virality algorithm. The board is used to decide what to build next, track status, and maintain a backlog.

**Live site:** https://mapzimus.github.io/mapzimus-board  
**Password:** `gridline` (SHA-256 hashed in index.html)  
**Repo:** https://github.com/mapzimus/mapzimus-board  
**Local path:** `D:\projects\mapzimus-board\`

---

## 2. Tech Stack

| Layer | Tool |
|---|---|
| Frontend | Vanilla JS + HTML + CSS (no framework) |
| Data | `data.js` — one giant `const D = [...]` array |
| Pipeline | `maintain.py` — Python 3.14 script |
| Hosting | GitHub Pages (auto-deploy on push to `main`) |
| Version control | Git / GitHub |
| GIS build stack | PostgreSQL 18 + PostGIS 3.6.1 + QGIS 3.44.7 + R + Python |

**Python path on this machine:**  
`C:\Users\mhowe\AppData\Local\Python\pythoncore-3.14-64\python.exe`

**PowerShell rules (critical):**
- Never use `&&` — use `;` or separate lines
- Never use `Set-Content` or `Out-File` (defaults to UTF-16, breaks everything)
- Always use `$py = "..."` then `& $py script.py` pattern

---

## 3. Repository File Map

```
mapzimus-board/
├── index.html          # Password gate + UI shell
├── app.js              # All board logic (~970 lines)
├── data.js             # The idea database (const D = [...])
├── maintain.py         # Pipeline: compact→fix_chars→add_ext→normalize→recalc→validate→js_check
├── full_audit.py       # Board health check — run anytime
├── score_audit.py      # Score distribution analysis
├── audit_sections.py   # Section/category alignment audit
├── inject_all_remaining.py  # EM-FZ batch injection script (complete, already run)
└── HANDOVER.md         # This file
```

---

## 4. The Data: `data.js`

Every idea is a single-line JS object in the `const D = [...]` array.

### 4a. Full Schema

```js
{
  id: "snake_case_unique_id",          // Required. Unique. No spaces. No non-ASCII.
  title: "Human-readable title",       // Required. The headline.
  sub: "One-sentence hook",            // Required. The Instagram caption hook.
  type: "MAP",                         // Required. One of: MAP | CHART | XREF | RANK
  geo: "us_state",                     // Required. See canonical geo values below.
  fmt: "State choropleth",             // Required. One of 13 canonical formats (see below).
  section: "Health",                   // Required. See canonical sections below.
  tbl: "Source Name + URL",            // Required. Real source name + full URL. Never fake.
  sc: {                                // Required. All fields 0-100.
    emotional: 80,
    relatability: 75,
    clarity: 85,
    surprise: 70,
    tension: 65,
    visual: 80,
    originality: 70,
    data_ready: 90                     // How ready the data is. Soft penalty on vs score.
  },
  vs: 74,                              // Computed by maintain.py. Do not hand-edit.
  topics: [],                          // Auto-filled by maintain.py. Leave empty.
  ext: [],                             // Auto-filled by maintain.py. Leave empty.
  status: "idea",                      // One of: idea | building | done | skip
  notes: ""                            // Always empty in data.js. Private via localStorage.
}
```

### 4b. Canonical `fmt` Values (13 total)
```
State choropleth | County choropleth | City map | World choropleth |
Bivariate choropleth | Dot map | Special map |
Line chart | Bar chart | Area chart | Scatter plot |
Ranked list | Treemap
```

### 4c. Canonical `geo` Values
```
us_national | us_state | us_county | us_city | us_metro |
us_northeast | us_new_england | us_tz | us_zip |
us_ma | us_nh |
worldwide | europe | asia | africa | latin_america |
middle_east | oceania | global_city
```

### 4d. Canonical `section` Values (what shows as clickable badges on cards)

**Legacy ProQuest/HSUS sections (from early batches):**
Health, Elections, Income, Housing, Labor Force, Law Enforcement, Education, Energy,
Agriculture, Transportation, Population, National Security, Banking, Finance, Prices,
Births Deaths, Business Enterprise, Foreign Commerce, Social Insurance, Geography,
Arts Recreation, Information

**Hand-crafted canonical sections (EM-FZ batches onward):**
Crime and Law Enforcement, Demographics, Economy, Environment, Entertainment,
Food & Nutrition, History, Labor, Science & Technology, Sports & Recreation, Climate

**Rule:** New ideas should use the hand-crafted canonical sections. Do not use compound
"Section - Subsection" strings for new ideas.

---

## 5. The Virality Score (vs) Algorithm — v3

```python
raw    = emotional*2 + relatability*2 + clarity*2 + surprise*1.5 + tension*1 + visual*1.25 + originality*1
base   = raw / 10.75
penalty = 1 - 0.3 * (1 - data_ready/100)
vs     = int(base * penalty)
```

**Key facts:**
- All sc fields are 0-100 scale
- `data_ready` is a soft multiplier penalty, not additive
- Max theoretical score: 90 | Board average: ~69 | Bell curve: 60-79
- `identity_signal` field was removed in v3 (not present in schema)
- `maintain.py` recalculates all vs scores on every run — never hand-edit `vs`

**Why new ideas score lower:** Ideas added in EM-FZ batches have `data_ready` of 70-85 because the source data isn't downloaded yet. As data is acquired and `data_ready` is bumped to 90-100, scores naturally rise. This is correct behavior.

---

## 6. `maintain.py` Pipeline

Run this after any edit to data.js:

```powershell
$py = "C:\Users\mhowe\AppData\Local\Python\pythoncore-3.14-64\python.exe"
cd D:\projects\mapzimus-board
& $py maintain.py
```

**Pipeline steps in order:**
1. `[compact]` — strips whitespace, enforces single-line objects
2. `[fix_chars]` — removes non-ASCII characters (critical for JS parse)
3. `[add_ext]` — auto-fills `ext:[]` and `topics:[]` from related fields
4. `[normalize_fmt]` — corrects fmt values to canonical list
5. `[recalc_vs]` — recalculates every vs score from sc fields
6. `[validate]` — checks idea count, dupes, double commas, end markers
7. `[js_check]` — runs Node.js parse to confirm valid browser JS

**Only push to GitHub after `[js_check] Valid JS` appears.**

---

## 7. How to Add New Ideas

### Option A: Add directly to data.js
Append single-line objects before the closing `]; // end D`. Run `maintain.py` after.

### Option B: Write a batch inject script (preferred for large batches)
Use the `mk()` helper function pattern from `inject_all_remaining.py`:

```python
def mk(id,title,sub,typ,geo,fmt,sect,tbl,e,r,c,s,t,v,o,dr):
    raw=e*2+r*2+c*2+s*1.5+t*1+v*1.25+o*1
    vs=int((raw/10.75)*(1-0.3*(1-dr/100)))
    return ('{id:"'+id+'",title:"'+title+'",sub:"'+sub+'",type:"'+typ+'",'
            'geo:"'+geo+'",fmt:"'+fmt+'",section:"'+sect+'",tbl:"'+tbl+'",'
            'sc:{emotional:'+str(e)+',relatability:'+str(r)+',clarity:'+str(c)
            +',surprise:'+str(s)+',tension:'+str(t)+',visual:'+str(v)
            +',originality:'+str(o)+',data_ready:'+str(dr)+'}'
            ',vs:'+str(vs)+',topics:[],ext:[],status:"idea",notes:""}')
```

The inject script must also:
- Check for existing IDs before injecting (dedupe guard)
- Strip the `]; // end D` tail, append new ideas, re-add tail
- Run `maintain.py` at the end

---

## 8. Current Board State (March 2026)

| Metric | Value |
|---|---|
| Total ideas | 2,686 |
| Valid JS | ✅ Yes |
| Duplicate IDs | 0 |
| Last commit | `a0f6bc4` |
| Score range | 46 – 90 |
| Score mean | 69.4 |


---

## 9. UI Architecture (app.js)

### Key constants (top of app.js)
- `P` — pastel color palette object (rose, blue, green, orange, etc.)
- `SECTION_COLORS` — maps section names to palette colors (substring match)
- `SECTION_COLOR_MAP` — precomputed O(1) lookup built from SECTION_COLORS at load
- `BADGE_SECTIONS` — Set of section names that render as clickable pill badges on cards
- `GEO_TREE` — hierarchical geo accordion filter structure (USA/WORLD drill-down)

### Card rendering
Each card shows:
- Left border color = type color (MAP=green, CHART=purple, XREF=blue, RANK=amber)
- Topic pills (colored, clickable, tint on deselect)
- Section badge (clickable, colored, only if section is in BADGE_SECTIONS)
- vs score, format, geo, status

### Filters
- **Type** — MAP / CHART / XREF / RANK
- **Format** — all 13 fmt values
- **Status** — idea / building / done / skip
- **Section badge** — click any section pill on a card to filter
- **Topics** — multi-select pills at top
- **Geo accordion** — hierarchical USA/WORLD drill-down (full 50 states + territories)
- **Score sliders** — 8 dual-handle range sliders for each sc field
- **Search** — full-text search across title + sub + id
- **Sort** — any field, asc/desc
- **Reset Filters** — appears when any filter is active
- **Saved Filters** — localStorage bookmark strip above search bar (`mz_saved_filters`)
- **Notes** — private per-idea notes via localStorage only (never in data.js)

### Password gate
- SHA-256 hash of "gridline" checked in index.html on load
- Session stored in `sessionStorage` (clears on browser close)

---

## 10. GIS Stack (for Building Ideas)

**Database:** PostgreSQL 18 + PostGIS 3.6.1  
**DB name:** `gis_projects`  
**Schemas:** `public`, `schools`, `municipal`, `equity`, `transportation`  

**Extensions installed:**
postgis, raster, topology, sfcgal, pgrouting, pgagent, fuzzystrmatch,
address_standardizer, tiger_geocoder, h3, h3_postgis, ogr_fdw, mobilitydb

**Desktop tools:** QGIS 3.44.7 + DBeaver + VS Code (all connected to DB)  
**GEE project:** `gis-test-489902` (mhowe.gis@gmail.com)  
**Preferred basemap:** CartoDB Light All  
**Reliable shapefile import:** `shp2pgsql` (QGIS DB Manager had connection issues)  

**First loaded dataset:**  
`municipal.municipalities` — MassGIS municipalities (SRID 26986, 1,239 rows)

**R packages in use:** sf, ggplot2, tigris, tidycensus  
**Reusable nightly R template:** built — dark background, color scale presets, caption templates

---

## 11. Raw Data Sources (D:\raw_data\)

| Folder | Contents |
|---|---|
| `fivethirtyeight/` | 29 CSVs: drug use, bad drivers, hate crimes, college majors, births, alcohol, divorce, airline safety, ICU beds, Bechdel test, classic rock |
| `fbi/` | Estimated crimes by state 1979–2024, officers killed 1960–2024, hate crimes, trafficking |
| `cpi/` | Historical CPI-U through Feb 2026, PPI series (food, energy, industrial) |
| `ProQuest Statistical Abstract 2026/` | 37 chapter PDFs, all US stat categories |
| `Sage_Data/` | Religion Census 2020, NAEP scores, arrests by race, inmates, vehicle registration, marijuana use, personal income by NAICS |
| `Kaggle/FBRESULTS26/` | International soccer results 1872–present, goalscorers, shootouts |
| `Kaggle/iranwar/` | Iran-Israel conflict 2024–2025, weapon-level detail, interception rates |
| `Our World In Data/` | 239 files: population projections, political regime 1789–2025, prison rates, CO2, fertility, HDI, military spending, internet access, child mortality |
| `MBTA Data 2025/` | 127 rapid transit stops, 348 commuter rail stations, 6,866 bus stops (lat/lon, accessibility) |
| `airbnb/boston/` | 1,741 listings with revenue, occupancy, ratings, coordinates |
| `worldcup/` | All WC matches 1930–2022 with xG, FIFA rankings Oct 2022 |
| `WalkabilityIndex/` | EPA National Walkability Index, census block group level nationwide |
| `HSUS/` | 202 XLS files, Historical Statistics of US 1790–2000 |
| `Public_School_Characteristics_2022-23.csv` | Every US public school with lat/lon, enrollment, Title I |
| `Pew/` | Abortion report PDF March 2026 |
| `MassGIS/` | Municipalities loaded. More layers incoming. |

---

## 12. Priority Build Queue (Top Ideas by vs + GIS Readiness)

These are the highest-value ideas that are also GIS-buildable with current data:

| ID | vs | Technique | Data Status |
|---|---|---|---|
| `geo_abortion_drive_time_post_dobbs` | 79 | pgRouting | Guttmacher provider list needed |
| `geo_golden_hour_ambulance_coverage` | 75 | pgRouting | NHTSA EMS data needed |
| `geo_nicu_drive_time` | 72 | pgRouting | AAP NICU list needed |
| `geo_redlining_tree_canopy_bivariate` | 72 | PostGIS bivariate | Mapping Inequality + USFS canopy |
| `geo_solar_noon_vs_clock_noon` | 67 | PostGIS calculation | USNO solar calculator |
| `geo_h3_commute_flow_us` | 60 | H3 hexbin | Census LODES data |
| `geo_irs_migration_mobilitdb` | 72 | MobilityDB animation | IRS SOI migration data |
| `geo_superfund_buffer_demographics` | 72 | PostGIS buffer + join | EPA NPL + Census TIGER |

**Standard pgRouting workflow:**
1. Load OSM road network via `osm2pgrouting` into PostGIS
2. Load destination points (hospitals, providers, etc.)
3. Run `pgr_drivingDistance()` from each origin centroid
4. Join results to county/census tract layer
5. Export to R for ggplot2 choropleth rendering

---

## 13. Content Strategy

**Platform split:**
- **Instagram (@mapzimus):** Visual hook first — dark background, strong color, punchy caption
- **Reddit (r/MapPorn):** Methodology credibility — source citations, methodology note in comments

**Aesthetic:** Dark background (#0a0a0a), pastel data colors, reusable R template already built

**FOSS-only constraint:** R, QGIS, Python, PostgreSQL/PostGIS only. No Esri tools. Adobe Illustrator used privately for final polish but not publicized.

**Content pipeline — batch ideas by theme:**

*Tier 1 / Priority:* Abortion drive time, golden hour ambulance, redlining+tree canopy, IRS migration animated, GoFundMe medical campaigns

*High-virality ready-to-build:* Dollar General vs grocery routing, farm subsidy + vote xref, rural hospital closure + mortality, lead pipe demographics, wage theft vs street crime

*Engagement formats that work:* "The map nobody talks about" framing, before/after comparisons, "your state" hooks, scandal + data combinations

---

## 14. Ongoing / Pending Work

- [ ] Acquire Guttmacher abortion provider list → build `geo_abortion_drive_time_post_dobbs`
- [ ] Load OSM road network for Massachusetts into PostGIS (first pgRouting test)
- [ ] Load MassGIS additional layers (roads, parcels, land use)
- [ ] Load NHGRANIT (New Hampshire GIS) datasets
- [ ] Bump `data_ready` scores as source data is downloaded (will raise vs scores)
- [ ] Build first complete MassGIS end-to-end workflow
- [ ] Continue adding ideas in batches beyond FZ as new data sources arrive

---

## 15. How to Continue in Cowork

1. Open `D:\projects\mapzimus-board\` in Cowork
2. Read this file first
3. Run `full_audit.py` for a health check: `& $py full_audit.py`
4. Run `maintain.py` to verify the current state is clean before any edits
5. Always commit after `[js_check] Valid JS` passes
6. Use `inject_all_remaining.py` as the template pattern for new batch injections

**The one thing that breaks everything:** Non-ASCII characters (curly quotes, em-dashes, etc.) in `sub` or `title` fields. `maintain.py [fix_chars]` catches most, but watch for `"smart quotes"` copied from external sources.

**Git workflow:**
```powershell
cd D:\projects\mapzimus-board
git add .
git commit -m "description of what changed"
git push
```
GitHub Pages auto-deploys within ~60 seconds of push.

---

*Blueprint written March 2026. Board at commit `a0f6bc4`. 2,686 ideas. Valid JS.*
