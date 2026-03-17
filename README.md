# Mapzimus Idea Board

Interactive idea database for the [@mapzimus](https://instagram.com/mapzimus) viral map project.

## What is this?

A searchable, filterable board of ~75 map/chart/infographic ideas, all sourced exclusively from the **ProQuest Statistical Abstract of the United States 2026** (all 36 PDFs scanned).

Each idea has:
- A **V-Score** (0–100) computed from 7 weighted factors: emotional charge, relatability, surprise, tension, visual clarity, data readiness, originality
- A **format recommendation** (bivariate choropleth, ranked bar, dual-line chart, etc.)
- The **exact ProQuest table** it comes from
- **Joinable variables** — other datasets it can be cross-referenced with

## Three modes

**Browse** — search by keyword, filter by type (XREF / MAP / RANK / CHART) and geography, sort by any of the 7 V-Score factors

**Correlate** — pick any variable from the ProQuest table index and instantly see every idea that uses it or can be joined with it — the cross-PDF correlation discovery engine

**By format** — click a format type to see all ideas that share that visual presentation, for content calendar planning

## Data source

ProQuest Statistical Abstract of the United States: 2026 Online Edition  
All spatial analysis: R (sf, ggplot2, tigris, tidycensus) · QGIS · PostgreSQL/PostGIS  
No external data sources used.

## Tech

Pure HTML/CSS/JS. No frameworks, no build step, no API calls. Deploys to GitHub Pages as a single static site.
