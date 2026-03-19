# MAPZIMUS BOARD — HANDOVER BLUEPRINT
# For: Idea-adding chat
# Purpose: Everything needed to continue adding ideas to the board
# Last updated: March 2026 | Current idea count: 1,466

---

## IDENTITY & CONTEXT

- **Brand:** @mapzimus (Instagram + Reddit r/MapPorn)
- **Creator:** Max, GIS analyst, Boston area
- **Concept:** Nightly viral infographic ideas database — a personal research tool and publishing pipeline
- **Constraint:** FOSS-only for all spatial work (R, QGIS, Python, PostgreSQL/PostGIS). No Esri.

---

## THE BOARD

- **Live site:** https://mapzimus.github.io/mapzimus-board/
- **GitHub repo:** https://github.com/mapzimus/mapzimus-board
- **Local path:** D:\projects\mapzimus-board\
- **Core files:**
  - `data.js` — master idea database (~1.6MB, 1,466 ideas)
  - `app.js` — board logic v6 (virtual scroll, inline editing, topic filters)
  - `index.html` — UI (all filter rows, card CSS)
  - `maintain.py` — master maintenance script (run after every batch)
  - `backfill_topics.py` — topic tag assignment (imported by maintain.py)

---

## IDEA SCHEMA (every field required)

Each idea is a single-line JS object. All ideas live in data.js as const D=[...].

```
{id:"snake_case_unique_id",
 title:"Full descriptive title with hook",
 sub:"2-3 sentence data-rich description with specific numbers",
 type:"MAP|XREF|CHART|RANK",
 geo:"us_state|us_county|us_national|us_metro|us_city|worldwide|top_n_list",
 fmt:"[see canonical formats below]",
 tbl:"Primary data source with URL",
 section:"[see section list below]",
 ext:["ext source 1","ext source 2"],
 vars:["primary_variable_1","primary_variable_2"],
 join:["joinable_variable_1","joinable_variable_2"],
 sc:{emotional:N,relatability:N,clarity:N,surprise:N,tension:N,visual:N,data_ready:N,originality:N},
 vs:N,
 topics:["topic1","topic2"],
 status:"idea",
 notes:"",
 tags:"space separated keywords for search"}
```

### TYPES
- `MAP` — geographic map (choropleth, dot map, city map, etc.)
- `XREF` — cross-reference / correlation (scatter plot, bivariate)
- `CHART` — non-map visualization (bar, line, area, treemap, ranked list)
- `RANK` — ranked list / top-N

### 15 CANONICAL FORMATS (normalize_fmt enforces these)
```
Scatter plot | State choropleth | Line chart | Bar chart | Area chart
Ranked list | County choropleth | World choropleth | Bivariate choropleth
City map | Dot map | Treemap | Special map | Quadrant chart | H3 hexbin map
```

### GEO VALUES
```
us_state | us_county | us_national | us_metro | us_city | worldwide | top_n_list
```

### STATUS VALUES
```
idea | in-progress | built | published
```

### SECTION VALUES (18 canonical sections)
```
Health | Elections | Income | Housing | Labor Force | Law Enforcement
Education | Energy | Agriculture | Transportation | Population
National Security | International Statistics | Geography | Banking
Information | State Government | Federal Government
```

---

## V-SCORE FORMULA (max 100, auto-computed)

```
vs = emotional×2.0 + relatability×2.0 + clarity×2.0 + surprise×1.5
     + tension×1.0 + visual×1.0 + data_ready×0.5 + originality×0.5
```

All sc fields are 1-10. Target vs range: 60-94. Current mean: 75.4.

**Clarity guide:**
- 9-10 = Ranked list, anyone reads it in 10 sec
- 7-8 = Choropleth, bar chart (general audience)
- 5-6 = Scatter plot, time series (needs some statistical literacy)
- 4 = Bivariate, H3 hexbin (specialists)

**Type modifiers:**
- XREF: subtract 1 from clarity estimate
- RANK: add 1 to clarity estimate

---

## 34 TOPIC TAGS (multi-value array, auto-assigned by backfill_topics.py)

```
war | military | crime | drugs | guns | health | poverty | food | energy
climate | economy | labor | housing | education | politics | immigration
race | gender | technology | media | religion | population | transportation
infrastructure | environment | finance | trade | inequality | democracy
agriculture | international | history | space | data
```

Topics are auto-assigned by maintain.py using keyword matching on title+sub+tags+section.
Do NOT manually set — let the script handle it.

---

## STANDARD BATCH WORKFLOW

### Step 1: Write the batch script

Create `BATCH_XX.py` in D:\projects\mapzimus-board\ using this exact template:

```python
"""BATCH_XX.py - [description of what this batch covers]"""
with open('data.js','r',encoding='utf-8') as f: c=f.read()
c=c[:c.rfind('\n]; // end D')]
with open('data.js','w',encoding='utf-8') as f: f.write(c)

ideas = [
',{id:"idea_id_here",...}',
',{id:"idea_id_2",...}',
# ... up to 20 ideas per batch
]

with open('data.js','a',encoding='utf-8') as f:
    f.write('\n'.join(ideas))
    f.write('\n]; // end D\n')
print('Batch XX done.')
```

### Step 2: Run in PowerShell (separate lines — no && in PowerShell)

```powershell
cd D:\projects\mapzimus-board
python BATCH_XX.py
python maintain.py
git add .
git commit -m "Batch XX: description"
git push
```

### What maintain.py does (in order):
1. **compact** — deduplicates ideas, rebuilds data.js cleanly
2. **fix_chars** — strips non-ASCII that breaks the browser
3. **add_ext** — auto-adds standard ext[] sources based on geo+section
4. **normalize_fmt** — collapses fmt variants to 15 canonical categories
5. **validate** — checks for dupes, double commas, counts ideas
6. **validate_js** — Node.js parse check (must pass before pushing)

**Validate output to watch for:**
- `Dupes:` must say `none` — if not, fix before pushing
- `Valid JS - N ideas parseable in browser` — must appear

---

## NAMING CONVENTIONS

### ID rules
- `snake_case_only`, no spaces, no special chars
- Descriptive but concise: `xref_union_density_vs_wage_inequality`
- Prefix `xref_` for XREF type ideas
- Max ~60 characters
- Must be globally unique across all 1,466+ ideas

### tbl field (primary data source)
- Use real source name + URL, NOT T-codes
- Format: `"Agency/Dataset: description (url)"`
- Example: `"BLS LAUS: unemployment rate and labor force by state (bls.gov/lau)"`
- For combinations: `"Source A + Source B"`

### ext[] field
- Added automatically by maintain.py based on geo+section — leave as `ext:[]` in batch scripts
- maintain.py will fill it in

### tags field
- Space-separated keywords
- Include: key numbers from sub, data source names, methodology terms
- Used for full-text search on the board

---

## WRITING HIGH-QUALITY IDEAS

### The four ingredients of a viral map idea:
1. **Specific numbers** in sub — "14 states have zero providers" not "many states"
2. **The hook** — one sentence that would make someone share it
3. **The tension** — why does this matter / what's the conflict
4. **The data exists** — it must be a real, accessible dataset

### Score targets by type:
- **MAP** ideas: emotional 6-9, visual 7-9, clarity 7-8
- **XREF** ideas: surprise 7-9, tension 6-8, clarity 5-6 (scatter plots are harder to read)
- **CHART** ideas: relatability 7-9, clarity 7-9
- **RANK** ideas: relatability 8-10, clarity 9-10

### The sub field formula:
Sentence 1: The specific data finding with numbers.
Sentence 2: The geographic/demographic breakdown.
Sentence 3: The why-it-matters or the counterintuitive angle.

---

## NEXT BATCH LETTER: AS

Batches A through AR are complete. Next batch is **BATCH_AS.py**.

### Already-covered topics (do not heavily repeat):
- Labor economics, unions (AR)
- Transportation, infrastructure, mobility (AQ)
- Immigration, labor markets, enforcement (AP)
- Education outcomes, funding equity (AO)
- Banking, finance, Wall Street, monetary policy (AN)
- Energy transition, climate policy, environmental justice (AM)
- Criminal justice, incarceration, racial disparities (AL)
- Demographic trends, generational economics, fertility (AK)
- Global healthcare, insurance, maternal mortality (AJ)
- Tech geography, innovation, R&D, AI, EV (AI)
- Agriculture, food systems, rural economy, farmland (AH)

### Suggested topic areas for future batches:
- **AS**: Global poverty, development economics, foreign aid geography
- **AT**: Housing affordability, eviction, zoning, homelessness geography
- **AU**: Gun violence geography, weapons policy, mass shootings
- **AV**: Drug geography, opioid crisis, treatment access, cartels
- **AW**: Media deserts, press freedom, misinformation geography
- **AX**: Religion and secularization geography, church closures
- **AY**: Water rights, aquifers, drought geography, water wars
- **AZ**: Space economy, satellite geography, launch sites
- **BA**: Historical maps — redlining, sundown towns, New Deal geography
- **BB**: Electoral geography, gerrymandering, voter suppression
- **BC**: Military geography, bases, contractor spending by district
- **BD**: Food desert geography, SNAP access, grocery store deserts

---

## TOP IDEAS (V-Score ≥ 90) — built queue priority

```
V:94  abortion_drive_time — Drive time to nearest abortion provider post-Dobbs
V:94  which_red_counties_get_most_federal_aid — Federal aid per capita in most Republican counties
V:94  xref_ceo_pay_worker_pay — CEO-to-worker pay ratio vs. worker share of income
V:93  gofundme_medical_campaigns_by_county — GoFundMe medical campaigns per capita
V:92  xref_social_mobility_parents_income — Social mobility vs. parents' income by county
V:92  xref_missing_men_incarceration_and_mortality — Missing men map
V:92  abortion_rates_by_state_2022 — Abortion rates by state post-Dobbs
V:91  metro_housing_affordability_ranked — Metro housing affordability ranked
```

---

## IMPORTANT TECHNICAL NOTES

### PowerShell gotchas
- Use separate lines, NOT `&&` between commands
- `&&` causes parse errors in Windows PowerShell
- Always `cd D:\projects\mapzimus-board` first

### Encoding
- Always write data.js with `encoding='utf-8'`
- No em dashes (—), smart quotes (" "), or any non-ASCII in idea text
- maintain.py fix_chars() will strip them, but avoid them in batches

### One idea per line
- Each idea MUST be a single line in data.js
- No line breaks inside an idea object
- The compact() function in maintain.py enforces this

### Duplicate IDs
- validate() catches dupes — fix before pushing
- If dupes appear: check if truly duplicate content (delete one) or wrong ID (rename)

### Non-breaking rule: never use T-codes in tbl field
- Wrong: `tbl:"T573 - T454"`
- Right: `tbl:"BEA/Census: Government transfer payments per capita by state (bea.gov)"`

---

## FILE INVENTORY (key scripts only)

```
maintain.py         — Run after every batch (compact+fix+validate)
backfill_topics.py  — Topic auto-assignment (called by maintain.py)
fix_tbl_codes.py    — 300-entry lookup: T-code → real source name
fix_dupes_v2.py     — Duplicate ID fixer
backfill_clarity.py — Clarity score + status/notes backfill (already run, don't re-run)
BATCH_A.py ... BATCH_AR.py — Historical batches (reference for style)
```

---

## BOARD FEATURES (UI reference)

**Filters (all stackable):**
- Type: MAP / XREF / CHART / RANK
- Geo: US state / county / national / metro / city / worldwide / Top-N
- Format: Scatter / State map / County map / World map / Bivariate / Line / Bar / Area / Ranked list / Treemap
- Status: Ideas / In Progress / Built / Published
- Notes: Has notes / No notes
- **Topic: 34 tags (multi-select, OR logic)** ← newest addition

**Sort:** V-Score / Newest / Oldest / Emotional / Relatability / Clarity / Surprise / Tension / Visual / Data ready / Originality

**Card features:**
- Click colored dot → change status (idea/in-progress/built/published)
- Click "＋ Add note" → inline note editing
- All edits saved to localStorage instantly
- "⬇ Export edits" button → downloads patch_overrides.py to apply edits to data.js

**Performance:** Virtual scroll — renders 100 cards at a time, loads more on scroll.

---

## GIT STATE

- **Remote:** https://github.com/mapzimus/mapzimus-board.git
- **Branch:** main
- **Last commit:** e6b7b19 — "Add 34 topic tags to all 1466 ideas + multi-select topic filter row in UI"
- **Cache version:** v=12 (data.js?v=12, app.js?v=12 in index.html)
- **When pushing a batch:** increment cache version in index.html script tags

---

## QUICK REFERENCE: FULL BATCH EXAMPLE

```python
"""BATCH_AS.py - Global poverty, development economics, foreign aid geography"""
with open('data.js','r',encoding='utf-8') as f: c=f.read()
c=c[:c.rfind('\n]; // end D')]
with open('data.js','w',encoding='utf-8') as f: f.write(c)

ideas = [
',{id:"extreme_poverty_rate_by_country_2024",title:"Extreme poverty rate by country 2024 - the $2.15/day line and where people live below it",sub:"691 million people live on less than $2.15/day (2017 PPP). Sub-Saharan Africa holds 60% of the global extreme poor despite having 14% of world population. The poverty headcount in South Asia fell from 400M to 180M 2000-2023. Progress has been extraordinarily uneven.",type:"MAP",geo:"worldwide",fmt:"World choropleth",tbl:"World Bank PovcalNet/PIP: poverty headcount ratio at $2.15/day by country (data.worldbank.org - free API)",section:"International Statistics",ext:[],vars:["birth_rate","population_per_sq_km"],join:["net_migration_rate","rd_pct_gdp","population_pct_change_2020_2025"],sc:{emotional:9,relatability:7,clarity:8,surprise:6,tension:7,visual:8,data_ready:9,originality:4},vs:79,topics:[],status:"idea",notes:"",tags:"extreme poverty $2.15 day 691 million Sub-Saharan Africa 60% 14% population South Asia 400M 180M 2000 2023 uneven World Bank PovcalNet PIP headcount ratio"}',
]

with open('data.js','a',encoding='utf-8') as f:
    f.write('\n'.join(ideas))
    f.write('\n]; // end D\n')
print('Batch AS done.')
```

Then run:
```powershell
cd D:\projects\mapzimus-board
python BATCH_AS.py
python maintain.py
git add .
git commit -m "Batch AS: global poverty, development economics"
git push
```

---

## THIS CHAT VS THE OTHER CHAT

- **This new chat (idea-adding):** Write batches, run maintain.py, push. Stay focused on data quality and coverage breadth.
- **UI/brainstorming chat (original):** New board features, filter ideas, V-score formula tweaks, visual redesign concepts.

Changes to app.js / index.html belong in the original chat.
Changes to data.js (new ideas) belong here.
