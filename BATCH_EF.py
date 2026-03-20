# BATCH_EF.py — Kaggle iranwar dataset
# Sources: incidents.csv, waves.csv, international_reactions.csv
# This dataset is extraordinarily detailed — every Iran-Israel attack wave 2024-2025
# with weapon types, intercept rates, coalition response, coordinates, casualties

def vs(sc):
    raw = sc['emotional']*2 + sc['relatability']*2 + sc['clarity']*2 + sc['surprise']*1.5 + sc['tension']*1 + sc['visual']*1.25 + sc['originality']*1
    base = raw / 10.75
    penalty = 1 - 0.3*(1 - sc['data_ready']/100)
    return int(base * penalty)

ideas = [
{
  "id":"iranwar_weapon_types_by_wave",
  "title":"Iran's evolving missile arsenal 2024–2025: how each strike wave introduced a new weapon",
  "sub":"True Promise 1 used Shahed-136 drones (slow, saturating). True Promise 2 dropped drones entirely and used Fattah-1 hypersonic missiles for the first time in combat. Each successive operation showed Iran learning from the interception rates of the previous one. The dataset logs every weapon type, wave number, and whether it was a first combat use — a real-time record of a country updating its doctrine under fire.",
  "type":"CHART","geo":"middle_east","fmt":"Bar chart",
  "tbl":"Kaggle iranwar: waves.csv — weapon types used by operation and wave, new_weapon_first_use flag",
  "section":"National Security","ext":["ACLED: armed conflict data (acleddata.com - free for research)"],
  "vars":["weapons_used_by_wave","drones_vs_ballistic_vs_cruise_by_operation","first_combat_use_flag"],
  "join":["intercept_rate","damage_assessment","coalition_response"],
  "sc":{"emotional":80,"relatability":60,"clarity":80,"surprise":90,"tension":90,"visual":80,"originality":90,"data_ready":100},
  "vs":0,"tags":"Iran missile arsenal 2024 2025 Shahed-136 Fattah-1 hypersonic True Promise 1 2 learning doctrine updating first combat use",
  "notes":"The tactical evolution from TP1 to TP2 (drones dropped, hypersonics introduced) is the key finding — shows real-time military learning.",
  "topics":["war","military","history","technology","middle_east","data"],"status":"idea"
},
{
  "id":"iranwar_interception_rates_by_system",
  "title":"Iron Dome, Arrow, David's Sling, and US Aegis — which system intercepted what in 2024",
  "sub":"The Iran-Israel conflict produced the first large-scale real-world test of layered missile defense. Arrow-3 handled exoatmospheric intercepts of ballistic missiles. Iron Dome handled drones. David's Sling handled cruise missiles. The overall system achieved 99% interception in TP1, dropping to ~85% in TP2 when Iran switched to faster ballistic-only attacks. Coalition support (US Aegis, UK RAF, Jordan, France) provided the margin.",
  "type":"CHART","geo":"middle_east","fmt":"Bar chart",
  "tbl":"Kaggle iranwar: incidents.csv + waves.csv — interception_systems, estimated_intercept_rate, intercepted_by_israel/us/uk/jordan by wave",
  "section":"National Security","ext":["CSIS: Missile Defense Project (missilethreat.csis.org - free)"],
  "vars":["intercept_rate_by_system","coalition_contribution_to_interceptions"],
  "join":["weapon_type_incoming","ballistic_vs_drone","exo_vs_endo_atmospheric"],
  "sc":{"emotional":70,"relatability":60,"clarity":80,"surprise":90,"tension":80,"visual":80,"originality":90,"data_ready":100},
  "vs":0,"tags":"Iron Dome Arrow David's Sling Aegis interception rate 99 percent TP1 85 percent TP2 ballistic only layered defense coalition US UK Jordan France",
  "notes":"","topics":["war","military","technology","middle_east","data","science"],"status":"idea"
},
{
  "id":"iranwar_munitions_count_cumulative",
  "title":"Cumulative munitions fired by Iran at Israel 2024–2025: the largest aerial assault ever mapped",
  "sub":"The Kaggle dataset tracks cumulative_total across all operations: TP1 (320 munitions), TP2 (~200), TP3, TP4. The total exceeds 1,200 projectiles across 2024-2025 — the largest sustained aerial bombardment of one nation by another in the post-WWII era outside of the Russia-Ukraine conflict. Each wave dot can be plotted on a timeline with weapon type and intercept outcome.",
  "type":"CHART","geo":"middle_east","fmt":"Area chart",
  "tbl":"Kaggle iranwar: waves.csv — cumulative_total, estimated_munitions_count, payload description by wave chronology",
  "section":"National Security","ext":["IISS: The Military Balance (iiss.org - subscription, some free summaries)"],
  "vars":["cumulative_munitions_by_operation","munitions_by_weapon_type"],
  "join":["interception_rate","fatalities","damage_assessment"],
  "sc":{"emotional":80,"relatability":60,"clarity":80,"surprise":90,"tension":90,"visual":90,"originality":80,"data_ready":100},
  "vs":0,"tags":"cumulative munitions Iran Israel TP1 320 TP2 200 1200 total post-WWII largest aerial bombardment timeline weapon type intercept",
  "notes":"","topics":["war","military","history","middle_east","data","technology"],"status":"idea"
},
{
  "id":"iranwar_international_reactions_map",
  "title":"How 190 countries responded to the Iran-Israel strikes: the full global alignment map",
  "sub":"The international_reactions.csv contains the official government stance of every UN member on each Iranian strike operation. The world splits into three blocs: Western allies condemning Iran (~60 countries), Global South staying neutral or silent (~90 countries), and a small group expressing understanding of Iran's position (~40 countries). The split tracks almost perfectly with BRICS vs. NATO/EU membership.",
  "type":"MAP","geo":"worldwide","fmt":"World choropleth",
  "tbl":"Kaggle iranwar: international_reactions.csv — overall_stance (condemns_iran/condemns_israel/neutral/silent) by country and operation",
  "section":"National Security","ext":["UN General Assembly: voting records (digitallibrary.un.org - free)"],
  "vars":["country_stance_on_iran_strikes"],"join":["nato_member","brics_member","un_vote_alignment_us","gdp_per_capita"],
  "sc":{"emotional":80,"relatability":70,"clarity":90,"surprise":80,"tension":80,"visual":100,"originality":80,"data_ready":100},
  "vs":0,"tags":"190 countries Iran Israel strikes global alignment Western condemn 60 Global South neutral 90 BRICS NATO EU split",
  "notes":"","topics":["war","international","politics","middle_east","geography","data","democracy"],"status":"idea"
},
{
  "id":"iranwar_targets_by_category",
  "title":"What Iran actually targeted in Israel: airbases, intelligence HQ, civilian infrastructure — the target map",
  "sub":"The incidents.csv contains target_iaf_base, target_us_base, target_government_c2, target_intelligence, target_civilian_infrastructure flags for each wave. TP1 targeted airbases only. TP2 added the Mossad/Unit 8200 headquarters for the first time. TP4 (the largest) included civilian infrastructure targeting. The escalation ladder from military to civilian targets is fully documented.",
  "type":"CHART","geo":"middle_east","fmt":"Bar chart",
  "tbl":"Kaggle iranwar: incidents.csv — target category flags by operation (iaf_base, government_c2, intelligence, civilian_infra)",
  "section":"National Security","ext":["ACLED: armed conflict data (acleddata.com - free for research)"],
  "vars":["target_category_by_operation"],"join":["operation_number","fatalities","damage_reported"],
  "sc":{"emotional":80,"relatability":60,"clarity":80,"surprise":80,"tension":90,"visual":80,"originality":80,"data_ready":100},
  "vs":0,"tags":"Iran targets Israel airbase Mossad Unit 8200 civilian infrastructure escalation ladder TP1 TP2 TP4 military to civilian",
  "notes":"","topics":["war","military","middle_east","history","data","technology"],"status":"idea"
},
{
  "id":"iranwar_proxy_involvement_geography",
  "title":"Iran's proxy network geography 2024–2025: where missiles came from besides Iran",
  "sub":"Multiple TP waves involved proxy forces: Hezbollah in Lebanon, Islamic Resistance in Iraq, Ansar Allah (Houthis) in Yemen all launched simultaneous attacks during TP1. The iranwar dataset flags proxy_involvement and proxy_description for each wave. The full picture is a multi-front coordinated campaign spanning 2,000+ km — not just an Iran-Israel bilateral conflict.",
  "type":"MAP","geo":"middle_east","fmt":"Special map",
  "tbl":"Kaggle iranwar: waves.csv — proxy_involvement flag, proxy_description, launch_site_lat/lon by wave",
  "section":"National Security","ext":["ACLED: armed conflict data (acleddata.com - free for research)"],
  "vars":["proxy_involvement_by_wave","launch_sites_by_country"],
  "join":["hezbollah_territory","houthi_territory","iraqi_militia_locations"],
  "sc":{"emotional":80,"relatability":60,"clarity":80,"surprise":80,"tension":90,"visual":90,"originality":80,"data_ready":100},
  "vs":0,"tags":"Iran proxy Hezbollah Lebanon Iraq Houthi Yemen simultaneous multi-front 2000km coordinated not bilateral launch site geography",
  "notes":"","topics":["war","military","middle_east","geography","history","data"],"status":"idea"
},
{
  "id":"iranwar_fattah1_hypersonic_debut",
  "title":"The Fattah-1 hypersonic missile's combat debut: what the data shows about its actual performance",
  "sub":"True Promise 2 wave 2 marked the first combat use of the Fattah-1 hypersonic missile. Iran claimed successful penetration of Israeli air defenses near Tel Aviv. Israel claimed successful interception. The incidents.csv documents the disputed outcome with damage reports (homes hit ~500m from Mossad HQ), interception system responses, and source URLs from both sides. The truth is in the geometry of the craters.",
  "type":"CHART","geo":"middle_east","fmt":"Special map",
  "tbl":"Kaggle iranwar: incidents.csv — Fattah-1 wave row: target_lat/lon, damage, interception_report, fatalities, injuries, source_urls",
  "section":"National Security","ext":["Bellingcat: open source verification (bellingcat.com - free)"],
  "vars":["fattah1_impact_locations","fattah1_intercept_disputed"],
  "join":["target_distance_from_mossad_hq","damage_radius","satellite_imagery"],
  "sc":{"emotional":70,"relatability":50,"clarity":70,"surprise":90,"tension":80,"visual":80,"originality":90,"data_ready":100},
  "vs":0,"tags":"Fattah-1 hypersonic first combat use True Promise 2 disputed Iran claims penetration Israel claims intercept 500m Mossad HQ craters",
  "notes":"","topics":["war","military","technology","middle_east","data","science"],"status":"idea"
},
{
  "id":"iranwar_fatalities_by_operation",
  "title":"Fatalities and injuries from Iranian strikes on Israel 2024–2025 by operation and target type",
  "sub":"Despite 1,200+ projectiles fired, the total confirmed fatalities in Israel from direct Iranian strikes are in single digits across all operations. The TP1 99% interception rate held. TP2 produced 2 fatalities — the first ever from a direct Iranian strike. The near-zero casualty outcome from the largest aerial bombardment in modern Middle Eastern history is itself the story.",
  "type":"CHART","geo":"middle_east","fmt":"Bar chart",
  "tbl":"Kaggle iranwar: incidents.csv — fatalities, injuries, civilian_casualties, military_casualties by wave and operation",
  "section":"National Security","ext":["ACLED: armed conflict data (acleddata.com - free for research)"],
  "vars":["fatalities_by_operation","injuries_by_operation","civilian_vs_military_casualties"],
  "join":["munitions_fired","intercept_rate","damage_level"],
  "sc":{"emotional":80,"relatability":60,"clarity":80,"surprise":100,"tension":80,"visual":70,"originality":80,"data_ready":100},
  "vs":0,"tags":"fatalities Iranian strikes 1200 projectiles single digits 2 fatalities TP2 first ever 99 percent interception near-zero casualty story",
  "notes":"","topics":["war","military","middle_east","data","science","history"],"status":"idea"
},
]

for idea in ideas:
    idea['vs'] = vs(idea['sc'])
