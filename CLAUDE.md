# CLAUDE.md — Mapzimus Board Project Reference

> Last updated: 2026-04-02
> This file documents the full technical picture of the mapzimus-board project for use across AI-assisted sessions.

---

## 1. Project Overview

**Mapzimus Board** is a static, single-page web app hosted on GitHub Pages.
It displays a searchable, filterable dashboard of ~19,000+ data-visualization *ideas*
(maps, charts, cross-references, rankings) scored by a virality algorithm.

- **Live URL:** GitHub Pages (auto-deploys from `main` branch)
- **Stack:** Vanilla JS + HTML + CSS — no build step, no frameworks
- **Data file:** `data.js` (~10.2 MB) — a single `const D = [...]` array
- **Entry point:** `index.html` (loads `app.js`, `data.js`)

---

## 2. File Map

| File | Role |
|------|------|
| `data.js` | All ~19,410 ideas as a JS array (`const D`) |
| `app.js` | Card rendering, filtering, sorting, search UI |
| `index.html` | Dashboard shell, CSS, embedded dashboard script |
| `maintain.py` | Pipeline: compact → fix_chars → add_ext → normalize_fmt → recalc_vs → validate → js_check |
| `backfill_topics.py` | Assigns topic tags to ideas with empty `topics:[]` |
| `backfill_humor.py` | Assigns humor scores to ideas missing `bonus.humor` |
| `apply_bonuses.py` | Computes/updates `bonus` fields (hook, humor, timeliness) |
| `_archive/` | All batch files (`BATCH_*.py`), one-off fix scripts, pipeline helpers |
| `_archive/do_git.py` | Runs `git add . && git commit && git push` via Python subprocess |
| `_archive/_commit_msg.txt` | Active commit message — edit before running `do_git.py` |

---

## 3. Data Format (`data.js`)

```js
const D = [
{id:"gop_transfers", title:"GOP vote share vs...", type:"XREF", geo:"us_state",
 fmt:"Scatter plot", tbl:"MIT Election Lab; Census BEA", sub:"...",
 topics:["politics","economy"], section:"Elections and Voting",
 sc:{emotional:82,relatability:78,clarity:88,surprise:80,tension:75,visual:75,originality:82,data_ready:90},
 vs:71, dd:"2022", status:"idea",
 ext:{type:"bivariate",layer1:"political",layer2:"economic"}},
,{id:"abortion_state_map", ...},
...
]; // end D
```

**Key rules:**
- Every idea is on a **single line** (required by `compact()` and the regex parser)
- The first entry has no leading comma; all subsequent entries start with `,{`
- `const D` at script top level does **not** attach to `window.D` — use `typeof D !== "undefined"` checks in app.js
- File must end with `]; // end D` — the validate function checks for exactly one such marker

### Required Fields (all 15,978 ideas have these)

| Field | Type | Notes |
|-------|------|-------|
| `id` | string | Unique slug, no spaces |
| `title` | string | JSON-encoded (handles quotes/apostrophes) |
| `fmt` | string | Must be one of 22 canonical values (see §5) |
| `geo` | string | Geographic scope — `us_state`, `us_county`, `us_national`, `world`, etc. |
| `tbl` | string | Data source description |
| `sc` | object | Seven subscores 0–100 + `data_ready` |
| `type` | string | `MAP`, `CHART`, `XREF`, or `RANK` |
| `topics` | array | Zero or more topic tags |
| `section` | string | Thematic section name |
| `status` | string | `idea` (default), `wip`, `done` |
| `sub` | string | One-line subtitle / hook (may be empty string) |
| `vs` | integer | V-Score (computed by `recalc_vs`) |

### Optional Fields

| Field | Notes |
|-------|-------|
| `dd` | One-line data description string — what the data actually shows (e.g. "Union membership share by state over 40 years"). Some legacy entries use a short date string ("2022") but new batches use full descriptions. |
| `ext` | Structured metadata object |
| `bonus` | Object with `hook`, `humor`, `timeliness` sub-scores |

---

## 4. V-Score Formula (v5)

V-Score measures predicted virality. Range is roughly 40–95.

```python
raw = v*3.0 + e*2.5 + s*2.0 + o*1.75 + t*1.75 + r*2.0 + c*1.5
# v=visual, e=emotional, s=surprise, o=originality,
# t=tension, r=relatability, c=clarity

base_vs = raw / 14.5
floor   = 0.85 if min(e, r, c, s, t, v, o) < 35 else 1.0
penalty = 1 - 0.35 * (1 - data_ready / 100)
vs      = int(base_vs * floor * penalty)
```

**Weight rationale (v5 vs v4):**
- `visual` 2.0 → 3.0 — thumbnail IS the content
- `emotional` 2.0 → 2.5 — sharing reflex driver
- `surprise` 1.5 → 2.0 — "wait WHAT" drives saves
- `originality` 1.5 → 1.75 — fresh ideas pop
- `tension` 1.5 → 1.75 — outrage/urgency amplifier
- `relatability` 2.0 → 2.0 — unchanged, drives comments
- `clarity` 2.0 → 1.5 — clear is table stakes, not differentiating

**IMPORTANT:** `recalc_vs()` in maintain.py only replaces existing `vs:NNN` fields.
New ideas injected into data.js must have a `vs:0` placeholder — otherwise recalc_vs
skips them silently and they stay at 0 forever.

---

## 5. Canonical Formats (22 total)

The `fmt` field must exactly match one of these values (case-sensitive):

```
Animated map       Area chart         Article
Bar chart          Bivariate choropleth  Bubble map
Cartogram          County choropleth  Dot map
Flow chart         Hex bin map        Infographic
Interactive        Line chart         Narrative
Ranked list        Scatter plot       Special map
State choropleth   Timeline           Treemap
World choropleth
```

`normalize_fmt()` in maintain.py uses `FMT_RULES` regexes to auto-correct common
variants (e.g. `"Stacked bar"` → `"Bar chart"`, `"Flow map"` → `"Dot map"`).
As of 2026-03-25, FMT_RULES also handles `Interactive`, `Article`, `Narrative`
(case-insensitive) — added to prevent lowercase variants from slipping through.

---

## 6. Type Field

Derived from `fmt`:

| Type | Fmt values |
|------|-----------|
| `MAP` | State choropleth, County choropleth, City map, Dot map, World choropleth, Bivariate choropleth, Special map |
| `CHART` | Bar chart, Line chart, Scatter plot, Area chart, Treemap, Article, Interactive, Narrative |
| `XREF` | (cross-reference ideas — typically `Scatter plot` or `Bivariate choropleth` comparing two datasets) |
| `RANK` | Ranked list |

Legacy type values (`topic`, `explainer`, `data`, etc.) were batch-fixed in 2025
using `fix_all_attrs.py` — all 6,706 legacy values replaced.

---

## 7. Canonical Topics

Topic tags are free-form arrays but a standard set of ~35 canonical topics is enforced.
Micro-topics are merged into their canonical parents:

| Removed | Merged into |
|---------|------------|
| `policy` | `politics` |
| `culture` | `entertainment` |
| `debt` | `economy` |
| `oil` | `energy` |
| `conflict` | `crime` |
| `urban` | `housing` |
| `banking` | `economy` |
| `censorship` | `media` |
| `wealth_inequality` | `economy` |

**Common canonical topics:**
`politics`, `economy`, `health`, `crime`, `housing`, `education`, `environment`,
`energy`, `immigration`, `race`, `gender`, `religion`, `guns`, `drugs`, `labor`,
`sports`, `entertainment`, `media`, `history`, `technology`, `finance`, `military`,
`middle_east`, `science`, `food`, `transportation`

~539 ideas still have empty `topics:[]` — these are too niche for keyword-based backfill.

---

## 8. Pipeline

Run in this order after adding/modifying ideas:

```
python backfill_topics.py    # fill empty topics[] using section seeds + keyword rules
python backfill_humor.py     # fill missing bonus.humor scores
python apply_bonuses.py      # compute/update full bonus field
python maintain.py           # compact → fix_chars → add_ext → normalize_fmt → recalc_vs → validate → js_check
```

Then commit and push:
```
# Edit _archive\_commit_msg.txt first, then:
python _archive\do_git.py
```

### What each maintain.py step does

| Step | Function | What it does |
|------|----------|-------------|
| 1 | `compact()` | Strips extra whitespace, ensures one idea per line |
| 2 | `fix_chars()` | Fixes bad Unicode characters and encoding artifacts |
| 3 | `add_ext()` | Injects `ext:{}` metadata (geo type, layer info) where missing |
| 4 | `normalize_fmt()` | Maps non-canonical fmt values to canonical ones via FMT_RULES |
| 5 | `recalc_vs()` | Recomputes all `vs:` scores using v5 formula |
| 6 | `validate()` | Checks for dupes, double commas, bad types, end marker |
| 7 | `validate_js()` | Runs Node.js eval to confirm data.js parses as valid JS |

---

## 9. Writing New Idea Batches

Each batch file lives in `_archive/BATCH_HPX.py` and uses the `mk()` helper:

```python
def mk(id, title, fmt, geo, tbl, sc, dd=None, section=None, topics=None, ext=None, status='idea'):
    parts = [f'id:"{id}"', f'title:{json.dumps(title)}', f'fmt:"{fmt}"', ...]
    # Always includes vs:0 placeholder so recalc_vs can compute it
    return '{' + ','.join(parts) + '}'
```

**Batch naming convention:**
- Batches are named `BATCH_HPA`, `BATCH_HPB`, ... `BATCH_HPJ`, etc.
- IDs within each batch: `HPA01`–`HPA26`, `HPB01`–`HPB26`, etc.
- ~26 ideas per batch, 3 batches per pipeline run

**Tag rotation (to balance topic coverage):**
1. finance / middle_east / humor
2. guns / religion / history
3. labor / race / economy
4. immigration / media / entertainment
5. sports / gender / drugs
→ repeat

**Batches are injected into data.js** by appending before the closing `]; // end D` marker.

---

## 10. Batch Injection Pattern

When injecting a new batch, the script appends ideas before `]; // end D`:

```python
marker = ']; // end D'
new_block = '\n' + '\n'.join(f',{idea}' for idea in ideas) + '\n'
content = content.replace(marker, new_block + marker, 1)
```

After injection, run the full pipeline (§8) so:
- `recalc_vs` fills in the `vs:0` placeholders
- `validate_js` confirms the file parses correctly
- No double commas or encoding errors slip through

---

## 11. Git Workflow

Git is NOT in PATH on this machine. All git operations go through Python subprocess.

```python
# _archive/do_git.py — reads _archive/_commit_msg.txt for the message
import subprocess
msg = open(r'D:\projects\mapzimus-board\_archive\_commit_msg.txt').read().strip()
subprocess.run(['git', 'add', '.'], ...)
subprocess.run(['git', 'commit', '-m', msg], ...)
subprocess.run(['git', 'push'], ...)
```

**To restore data.js from last commit** (e.g. after a bad write):
```
python _archive\do_git_restore.py
# Runs: git checkout HEAD -- data.js
```

---

## 12. app.js Key Behavior

- **Card rendering:** Each idea in `D` renders as a card via `renderCard(d)`
- **Type guard:** `d.type||'unk'` — never assume type is present even though all current ideas have it
- **Sub guard:** `d.sub ? \`<div class="cs">${d.sub}</div>\` : ''` — sub may be empty string
- **Geo guard:** `(d.geo||'').startsWith(prefix)` — geo filter uses prefix matching
- **Search:** `(d.title+' '+(d.sub||'')+' '+(d.tags||'')+' '+(d.section||'')).toLowerCase()`
- **dd pill:** Displayed in the pills row (not V-Score label area) with green styling `.dd`
- **Topic colors:** Defined in `TOPIC_COLORS` object — ~40 topics mapped to colors

### `const D` vs `window.D`

`const` at script top-level does NOT attach to `window` in strict-mode environments.
Always check `typeof D !== "undefined"` — never `window.D`.

---

## 13. Dashboard (index.html embedded script)

The dashboard script (`new_dash2.js`) is embedded directly in index.html.
Key behaviors:

- **`normGeo(raw)`** — normalizes raw geo strings to canonical display labels:
  `"world"/"worldwide"/"global"` → `"Global / World"`,
  `"usa"/"us"/"national"` → `"National (US)"`, etc.
- **Spatial Formats panel** — shows only spatial map types (not all 22 fmt values)
- **Topic distribution** — filtered to topics with `count >= 5`
- **Topic gaps** — shows underrepresented topics (count 2–25)
- **Format type breakdown** — Spatial Map / Cross-reference / Chart / Ranking

Cache-buster query string on `app.js` and `data.js` includes `?v=N` — bump `N`
in index.html whenever app.js or the dashboard script changes.

---

## 14. Windows / Shell Gotchas

- **Python path:** `C:\Users\mhowe\AppData\Local\Python\pythoncore-3.14-64\python.exe`
- **Shell for scripts:** always use `shell: "cmd"` in Desktop Commander
- **Multi-line code in REPL:** The Desktop Commander Python REPL rejects multi-line blocks.
  Always write scripts via `write_file` then execute with `start_process`.
- **Unicode console errors:** Writing Unicode chars to Windows console raises
  `UnicodeEncodeError: 'charmap' codec`. Fix: redirect output to a UTF-8 file,
  then read with `type` or `read_file`.
- **Binary-safe HTML patching:** Open index.html as bytes (`'rb'`), find/replace byte
  literals, write back (`'wb'`) — avoids UTF-8 decode errors from special chars in data.js.

---

## 15. Known Issues & Gotchas

### recalc_vs skips new ideas with no `vs:` field
`recalc_vs()` uses `re.sub(r',vs:\d+', ...)` — only replaces existing fields.
New batch ideas **must** include `vs:0` as a placeholder before `sc:{`.
The `mk()` helper in modern batch files handles this automatically.

### Topic MERGE dict — use `in` not `.get()`
When remapping topics, always use `if t in MERGE_DICT` before accessing `MERGE_DICT[t]`.
Using `MERGE_DICT.get(t)` returns `None` for any missing key — the `None` check
`if val is not None` passes for keys with value `None`, but `dict.get(key)` returns
`None` for both "key not in dict" and "key explicitly mapped to None".
The prior version of `fix_all_attrs.py` had this bug and stripped all canonical topics.

### compact() regex requires one idea per line
`compact()` uses `r',?\{id:"([^"]+)",[^\n]+\}'` — stops at the last `}` on the line.
If an idea spans multiple lines (e.g. from a bad injection), compact will corrupt it.
Always inject ideas as single-line strings.

### Title text with escaped quotes
Do NOT use `title:"[^"]*"` regex to find insertion points inside idea lines.
Title text can contain `\"` (escaped quotes), causing the regex to stop mid-title.
Use `,fmt:"` as an anchor instead — that pattern never appears inside title strings.

### data.js zeroed to 0 bytes
If a script crashes mid-write with `open(path, 'w')` already called but the content
variable is undefined, data.js will be zeroed. Recovery:
```
python _archive\do_git_restore.py
```
This runs `git checkout HEAD -- data.js` to restore the last committed version.

---

## 16. _archive Script Inventory (key files)

| Script | Purpose |
|--------|---------|
| `do_git.py` | git add/commit/push (reads `_commit_msg.txt`) |
| `do_git_restore.py` | `git checkout HEAD -- data.js` recovery |
| `backfill_topics.py` | Assign topics to empty-topic ideas |
| `backfill_humor.py` | Assign humor sub-scores |
| `apply_bonuses.py` | Compute/update bonus field |
| `fix_all_attrs.py` | Bulk fix: topic merge, type retype, sub/status backfill |
| `fix_fmt_case.py` | Fixed lowercase interactive/article → proper case |
| `fix_fmt_rules.py` | Added Interactive/Article/Narrative to FMT_RULES |
| `fix_culture.py` | Merged culture → entertainment (154 ideas) |
| `fix_hp_ideas.py` | Fixed HPI/HPJ batch: vs placeholder, sub field, sc key format, dd format |
| `patch_appjs.py` | Applied 8 targeted patches to app.js |
| `patch_index.py` | Binary-safe HTML patcher + cache-buster bump |
| `patch_css.py` | Added .dd and .unk CSS rules |
| `audit_code.py` | Full codebase audit → `audit_report.txt` |
| `new_dash2.js` | Dashboard script (geo normalization, Spatial Formats panel) |

---

## 17. Data Stats (as of 2026-04-02)

| Metric | Value |
|--------|-------|
| Total ideas | 19,410 |
| Types | MAP: ~9,500 · CHART: ~7,700 · XREF: ~1,900 · RANK: ~310 |
| Unique fmt values | 22 (fully canonical) |
| Ideas with topics | ~99%+ |
| Ideas with dd | ~85%+ |
| Ideas with bonus | ~70.4% |
| Top fmts | Bar chart (3,453) · State choropleth (2,684) · World choropleth (2,067) · Scatter plot (1,716) · Dot map (1,691) |
