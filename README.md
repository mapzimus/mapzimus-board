# mapzimus-board

A personal research tool for organizing and scoring data visualization concepts by their correlative potential with real public datasets.

## What it does

Each entry in the board represents a potential data visualization — a pairing of a question with the public datasets needed to answer it. The board helps surface which ideas are most actionable based on:

- **Data readiness** — are the required datasets publicly available and joinable?
- **Variable correlation** — which ideas share underlying variables, enabling cross-referencing?
- **Format distribution** — how ideas break down by map type, chart format, and geographic scope

## Scoring

Each entry is scored across 8 dimensions (0–100 scale):

| Field | What it measures |
|---|---|
| `emotional` | Does the data hit on something people care about personally? |
| `relatability` | Will most people have direct experience with this topic? |
| `clarity` | Can the core finding be communicated in one visual? |
| `surprise` | Does the data contradict conventional wisdom? |
| `tension` | Is there conflict or inequality embedded in the numbers? |
| `visual` | Does the data have strong spatial or temporal structure? |
| `data_ready` | Are the required datasets publicly accessible? |
| `originality` | Has this specific angle been done before? |

These are weighted into a single **V-Score** using: `(emotional×2 + relatability×2 + clarity×2 + surprise×1.5 + tension×1 + visual×1 + data_ready×0.5 + originality×0.5) / 10.5`

## Data sources referenced

All datasets referenced in entries are free and publicly accessible:

- US Census Bureau / ACS (via `tidycensus`)
- BLS, BEA, FRED (economic time series)
- CDC WONDER (health outcomes)
- FBI Crime Data Explorer
- EIA (energy)
- MIT Election Lab
- World Bank Open Data
- UN / WHO / FAO (international)

## Tech stack

- Vanilla JS frontend — no framework, no build step
- `data.js` — flat array of all entries, loaded at runtime
- `app.js` — filtering, sorting, virtual scroll, status tracking
- `maintain.py` — data pipeline: deduplication, normalization, JS validation
- PostgreSQL + PostGIS on the backend for spatial joins and routing analysis

## Modes

**Browse** — filter by type (MAP / XREF / CHART), geography, format, status, and topic. Sort by any score dimension. Virtual scroll handles the full dataset.

**Correlate** — pick any variable and see every entry that references it, either as a primary variable or a join key. Useful for identifying which datasets unlock the most ideas at once.

**By format** — browse entries grouped by visualization format to plan production batches.

## Status tracking

Each entry moves through: `idea → in-progress → built → published`. Status edits are stored in `localStorage` and exportable as a Python patch script to persist changes back to `data.js`.

---

Built for [@mapzimus](https://instagram.com/mapzimus)
