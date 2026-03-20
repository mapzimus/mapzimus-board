# BATCH_AT.py — Global demographics: democracy backsliding, regime geography, political infrastructure
# 18 ideas | Draws from: V-Dem political-regime.csv + water + population datasets

ideas = [

{
"id":"democracy_backsliding_map",
"title":"Countries that backslid from democracy to autocracy 2000-2025",
"sub":"Hungary, Turkey, India, Mexico, Philippines. 17 countries downgraded in 25 years. The tide is turning.",
"type":"MAP","geo":"worldwide","fmt":"World choropleth",
"tbl":"V-Dem Institute via Our World in Data: Political regime classification by country 1789-2025 (ourworldindata.org/democracy)",
"section":"International Statistics",
"ext":["World Bank Open Data: GDP, population, income by country (data.worldbank.org  free API)"],
"vars":["political_regime_2025","political_regime_2000","regime_change_direction"],
"join":["gdp_per_capita","population_total","water_access_pct"],
"sc":{"emotional":10,"relatability":7,"clarity":9,"surprise":9,"tension":10,"visual":10,"data_ready":9,"originality":8},
"vs":0,"tags":"democracy backsliding autocracy Hungary Turkey India Mexico Philippines V-Dem regime change 2000 2025 politics",
"notes":"","topics":[],"status":"idea"
},

{
"id":"regime_type_world_2025",
"title":"Political regime type by country 2025",
"sub":"Only 12.7% of humanity lives in a liberal democracy. 43.6% live under electoral autocracy.",
"type":"MAP","geo":"worldwide","fmt":"World choropleth",
"tbl":"V-Dem Institute via Our World in Data: Political regime classification by country 1789-2025 (ourworldindata.org/democracy)",
"section":"International Statistics",
"ext":["World Bank Open Data: GDP, population, income by country (data.worldbank.org  free API)"],
"vars":["political_regime"],
"join":["population_total","gdp_per_capita","water_access_pct"],
"sc":{"emotional":9,"relatability":7,"clarity":9,"surprise":9,"tension":9,"visual":10,"data_ready":10,"originality":7},
"vs":0,"tags":"democracy autocracy liberal electoral regime type world map 2025 V-Dem freedom political systems",
"notes":"","topics":[],"status":"idea"
},

{
"id":"pct_humanity_under_democracy",
"title":"Share of humanity living under democracy vs. autocracy over time",
"sub":"Liberal democracies held 17.4% of world population in 2000. Down to 12.7% by 2025. The quiet reversal.",
"type":"CHART","geo":"worldwide","fmt":"Stacked area chart",
"tbl":"V-Dem Institute via Our World in Data: Political regime classification and population by country 1789-2025 (ourworldindata.org/democracy)",
"section":"International Statistics",
"ext":["World Bank Open Data: GDP, population, income by country (data.worldbank.org  free API)"],
"vars":["pct_population_liberal_democracy","pct_population_electoral_democracy","pct_population_electoral_autocracy","pct_population_closed_autocracy"],
"join":["world_population_total"],
"sc":{"emotional":9,"relatability":7,"clarity":9,"surprise":9,"tension":9,"visual":10,"data_ready":9,"originality":9},
"vs":0,"tags":"democracy population share humanity autocracy time series decline V-Dem liberal freedom politics 2025",
"notes":"","topics":[],"status":"idea"
},

{
"id":"us_downgrade_electoral_democracy",
"title":"The US was downgraded from a liberal to an electoral democracy in 2025",
"sub":"V-Dem now classifies the United States alongside Hungary and Romania, not Canada and Germany.",
"type":"MAP","geo":"worldwide","fmt":"World choropleth",
"tbl":"V-Dem Institute via Our World in Data: Political regime classification by country 2024-2025 (ourworldindata.org/democracy)",
"section":"International Statistics",
"ext":["World Bank Open Data: GDP, population, income by country (data.worldbank.org  free API)"],
"vars":["political_regime_2025","political_regime_2024"],
"join":["gdp_per_capita","water_access_pct","population_total"],
"sc":{"emotional":10,"relatability":8,"clarity":9,"surprise":10,"tension":10,"visual":10,"data_ready":9,"originality":9},
"vs":0,"tags":"US democracy downgrade V-Dem electoral liberal classification 2025 Hungary Romania Canada Germany political regime",
"notes":"","topics":[],"status":"idea"
},

{
"id":"liberal_democracies_peak_decline",
"title":"Number of liberal democracies in the world peaked in 2012 and has fallen 32% since",
"sub":"44 liberal democracies in 2012. 30 in 2024. A 32% collapse in 12 years.",
"type":"CHART","geo":"worldwide","fmt":"Line chart",
"tbl":"V-Dem Institute via Our World in Data: Count of countries by regime type 1789-2025 (ourworldindata.org/democracy)",
"section":"International Statistics",
"ext":["World Bank Open Data: GDP, population, income by country (data.worldbank.org  free API)"],
"vars":["count_liberal_democracies","count_electoral_democracies","count_electoral_autocracies","count_closed_autocracies"],
"join":[],
"sc":{"emotional":9,"relatability":7,"clarity":9,"surprise":9,"tension":10,"visual":9,"data_ready":9,"originality":8},
"vs":0,"tags":"liberal democracy peak decline 2012 count V-Dem world autocracy trend 32 percent reversal",
"notes":"","topics":[],"status":"idea"
},

{
"id":"xref_regime_gdp",
"title":"Political regime type vs. GDP per capita by country 2023",
"sub":"Liberal democracies average $47K GDP per capita. Closed autocracies average $9K. Governance predicts prosperity.",
"type":"XREF","geo":"worldwide","fmt":"Scatter plot",
"tbl":"V-Dem Institute via Our World in Data: Regime type (ourworldindata.org/democracy) + World Bank: GDP per capita (data.worldbank.org)",
"section":"International Statistics",
"ext":["World Bank Open Data: GDP, population, income by country (data.worldbank.org  free API)"],
"vars":["political_regime","gdp_per_capita"],
"join":["water_access_pct","life_expectancy","old_age_dependency_ratio"],
"sc":{"emotional":8,"relatability":6,"clarity":7,"surprise":7,"tension":8,"visual":9,"data_ready":9,"originality":7},
"vs":0,"tags":"regime type GDP democracy autocracy wealth prosperity correlation governance development XREF",
"notes":"","topics":[],"status":"idea"
},

{
"id":"xref_regime_life_expectancy",
"title":"Political regime type vs. life expectancy by country 2023",
"sub":"Liberal democracies average life expectancy: 81 years. Closed autocracies: 68 years. Freedom adds 13 years.",
"type":"XREF","geo":"worldwide","fmt":"Scatter plot",
"tbl":"V-Dem Institute via Our World in Data: Regime type (ourworldindata.org/democracy) + World Bank: Life expectancy (data.worldbank.org)",
"section":"International Statistics",
"ext":["World Bank Open Data: GDP, population, income by country (data.worldbank.org  free API)"],
"vars":["political_regime","life_expectancy"],
"join":["gdp_per_capita","water_access_pct","child_mortality_rate"],
"sc":{"emotional":9,"relatability":7,"clarity":7,"surprise":8,"tension":8,"visual":9,"data_ready":9,"originality":8},
"vs":0,"tags":"regime democracy life expectancy autocracy freedom health outcomes governance correlation XREF",
"notes":"","topics":[],"status":"idea"
},

{
"id":"longest_continuous_democracies",
"title":"Countries with the longest unbroken streaks of liberal democracy",
"sub":"Switzerland liberal democracy since 1849. Norway since 1900. The stability map of the democratic world.",
"type":"RANK","geo":"worldwide","fmt":"Ranked list",
"tbl":"V-Dem Institute via Our World in Data: Political regime classification by country 1789-2025 (ourworldindata.org/democracy)",
"section":"International Statistics",
"ext":[],
"vars":["liberal_democracy_streak_years","year_became_liberal_democracy"],
"join":[],
"sc":{"emotional":7,"relatability":7,"clarity":10,"surprise":8,"tension":5,"visual":9,"data_ready":9,"originality":8},
"vs":0,"tags":"democracy streak longest Switzerland Norway history liberal stable countries ranking political regime",
"notes":"","topics":[],"status":"idea"
},

{
"id":"democracy_before_1900",
"title":"Which countries were democratic before 1900?",
"sub":"Switzerland 1849. France 1871. New Zealand 1893. The tiny club of early democracies.",
"type":"MAP","geo":"worldwide","fmt":"World choropleth",
"tbl":"V-Dem Institute via Our World in Data: Political regime classification by country 1789-2025 (ourworldindata.org/democracy)",
"section":"International Statistics",
"ext":[],
"vars":["year_first_became_democracy","political_regime_1900"],
"join":[],
"sc":{"emotional":7,"relatability":6,"clarity":8,"surprise":8,"tension":5,"visual":10,"data_ready":8,"originality":8},
"vs":0,"tags":"democracy history 1800s 1900 Switzerland France New Zealand early liberal early adopters political history",
"notes":"","topics":[],"status":"idea"
},

{
"id":"xref_regime_water_bivariate",
"title":"Regime type vs. water access: bivariate map of governance and basic infrastructure",
"sub":"The strongest predictor of whether you have clean water is whether your government was elected.",
"type":"XREF","geo":"worldwide","fmt":"Bivariate choropleth",
"tbl":"V-Dem via Our World in Data: Regime type (ourworldindata.org/democracy) + WHO/UNICEF JMP (2025): Water access (ourworldindata.org/water-access)",
"section":"International Statistics",
"ext":["World Bank Open Data: GDP, population, income by country (data.worldbank.org  free API)"],
"vars":["political_regime","water_access_pct"],
"join":["gdp_per_capita","sanitation_access_pct","child_mortality_rate"],
"sc":{"emotional":10,"relatability":7,"clarity":8,"surprise":9,"tension":9,"visual":10,"data_ready":9,"originality":10},
"vs":0,"tags":"regime democracy water access bivariate governance infrastructure clean water autocracy predictor XREF",
"notes":"","topics":[],"status":"idea"
},

{
"id":"closed_autocracies_population_2025",
"title":"Who lives under closed autocracy in 2025?",
"sub":"2.18 billion people — 27% of humanity — live under governments with no meaningful elections.",
"type":"MAP","geo":"worldwide","fmt":"World choropleth",
"tbl":"V-Dem Institute via Our World in Data: Political regime and population by country 2025 (ourworldindata.org/democracy)",
"section":"International Statistics",
"ext":["World Bank Open Data: GDP, population, income by country (data.worldbank.org  free API)"],
"vars":["political_regime","population_total"],
"join":["gdp_per_capita","water_access_pct"],
"sc":{"emotional":9,"relatability":7,"clarity":9,"surprise":8,"tension":9,"visual":10,"data_ready":9,"originality":7},
"vs":0,"tags":"closed autocracy population 2025 no elections humanity China Russia democracy freedom 2.18 billion",
"notes":"","topics":[],"status":"idea"
},

{
"id":"india_regime_downgrade",
"title":"India downgraded to electoral autocracy: the world's largest democracy in name only?",
"sub":"V-Dem reclassified India as an electoral autocracy in 2021. 1.4 billion people, reclassified.",
"type":"MAP","geo":"worldwide","fmt":"World choropleth",
"tbl":"V-Dem Institute via Our World in Data: Political regime classification by country 1789-2025 (ourworldindata.org/democracy)",
"section":"International Statistics",
"ext":["World Bank Open Data: GDP, population, income by country (data.worldbank.org  free API)"],
"vars":["political_regime_2025","political_regime_2015"],
"join":["population_total","gdp_per_capita","water_access_pct"],
"sc":{"emotional":9,"relatability":7,"clarity":8,"surprise":9,"tension":9,"visual":9,"data_ready":9,"originality":8},
"vs":0,"tags":"India democracy downgrade autocracy V-Dem 2021 Modi BJP electoral largest democracy reclassified 1.4 billion",
"notes":"","topics":[],"status":"idea"
},

{
"id":"xref_regime_pop_growth",
"title":"Political regime type vs. population growth rate 2023",
"sub":"Closed autocracies average +1.8% growth. Liberal democracies average +0.3%. The demographic-governance gap.",
"type":"XREF","geo":"worldwide","fmt":"Scatter plot",
"tbl":"V-Dem via Our World in Data: Regime type (ourworldindata.org/democracy) + UN WPP (2024): Population growth by country",
"section":"International Statistics",
"ext":["World Bank Open Data: GDP, population, income by country (data.worldbank.org  free API)"],
"vars":["political_regime","population_growth_rate"],
"join":["gdp_per_capita","fertility_rate","old_age_dependency_ratio"],
"sc":{"emotional":8,"relatability":6,"clarity":7,"surprise":8,"tension":7,"visual":9,"data_ready":9,"originality":8},
"vs":0,"tags":"regime democracy population growth rate autocracy fertility demographic governance XREF correlation",
"notes":"","topics":[],"status":"idea"
},

{
"id":"new_autocracies_since_2000",
"title":"Every country that became more autocratic since 2000",
"sub":"A world map of democratic backsliding: Hungary, Turkey, India, Mexico, Philippines, Bangladesh and 11 more.",
"type":"MAP","geo":"worldwide","fmt":"World choropleth",
"tbl":"V-Dem Institute via Our World in Data: Political regime change direction by country 2000-2025 (ourworldindata.org/democracy)",
"section":"International Statistics",
"ext":["World Bank Open Data: GDP, population, income by country (data.worldbank.org  free API)"],
"vars":["regime_change_2000_2025","political_regime_2000","political_regime_2025"],
"join":["gdp_per_capita_change","population_total","water_access_pct"],
"sc":{"emotional":10,"relatability":7,"clarity":9,"surprise":9,"tension":10,"visual":10,"data_ready":9,"originality":8},
"vs":0,"tags":"autocracy backsliding map Hungary Turkey India Philippines Mexico Bangladesh democratic erosion 2000 2025",
"notes":"","topics":[],"status":"idea"
},

{
"id":"xref_regime_old_dep",
"title":"Political regime type vs. old-age dependency ratio: do democracies age faster?",
"sub":"Liberal democracies average 0.28 elderly per worker. Closed autocracies: 0.12. Democracy and aging track together.",
"type":"XREF","geo":"worldwide","fmt":"Scatter plot",
"tbl":"V-Dem via Our World in Data: Regime type (ourworldindata.org/democracy) + UN WPP (2024): Age structure by country",
"section":"International Statistics",
"ext":["World Bank Open Data: GDP, population, income by country (data.worldbank.org  free API)"],
"vars":["political_regime","old_age_dependency_ratio"],
"join":["gdp_per_capita","water_access_pct","population_growth_rate"],
"sc":{"emotional":7,"relatability":6,"clarity":7,"surprise":8,"tension":6,"visual":8,"data_ready":9,"originality":9},
"vs":0,"tags":"democracy aging old age dependency regime type XREF correlation wealthy democracies pension fiscal",
"notes":"","topics":[],"status":"idea"
},

{
"id":"global_freedom_score_trend",
"title":"Global democratic freedom score has declined every year since 2006",
"sub":"Freedom House has recorded 18 consecutive years of global democratic decline. The longest streak on record.",
"type":"CHART","geo":"worldwide","fmt":"Line chart",
"tbl":"V-Dem Institute via Our World in Data: Democracy index scores over time (ourworldindata.org/democracy)",
"section":"International Statistics",
"ext":[],
"vars":["global_democracy_index","count_liberal_democracies"],
"join":[],
"sc":{"emotional":9,"relatability":7,"clarity":9,"surprise":8,"tension":10,"visual":8,"data_ready":8,"originality":7},
"vs":0,"tags":"freedom democracy index decline 18 years consecutive Freedom House V-Dem global trend autocracy rise",
"notes":"","topics":[],"status":"idea"
},

{
"id":"xref_triple_water_regime_youth",
"title":"Three-way: water access, regime type, and youth dependency — the development trap map",
"sub":"The countries with the most children, least democracy, and worst water are the same countries. Every time.",
"type":"XREF","geo":"worldwide","fmt":"Bivariate choropleth",
"tbl":"WHO/UNICEF JMP (2025) + V-Dem + UN WPP (2024) via Our World in Data: Water, regime, and age structure by country",
"section":"International Statistics",
"ext":["World Bank Open Data: GDP, population, income by country (data.worldbank.org  free API)"],
"vars":["water_access_pct","political_regime","youth_dependency_ratio"],
"join":["gdp_per_capita","population_growth_rate"],
"sc":{"emotional":10,"relatability":6,"clarity":7,"surprise":10,"tension":9,"visual":10,"data_ready":8,"originality":10},
"vs":0,"tags":"triple XREF water regime youth dependency development trap Africa governance poverty infrastructure correlation",
"notes":"","topics":[],"status":"idea"
},

{
"id":"xref_regime_fertility",
"title":"Political regime type vs. total fertility rate by country 2023",
"sub":"The most authoritarian countries have the highest birth rates. The most democratic have the lowest. Why?",
"type":"XREF","geo":"worldwide","fmt":"Scatter plot",
"tbl":"V-Dem via Our World in Data: Regime type (ourworldindata.org/democracy) + World Bank: Fertility rate by country (data.worldbank.org)",
"section":"International Statistics",
"ext":["World Bank Open Data: GDP, population, income by country (data.worldbank.org  free API)"],
"vars":["political_regime","fertility_rate"],
"join":["gdp_per_capita","water_access_pct","female_education_years"],
"sc":{"emotional":8,"relatability":6,"clarity":7,"surprise":9,"tension":7,"visual":9,"data_ready":9,"originality":9},
"vs":0,"tags":"regime democracy fertility rate autocracy birth rate XREF correlation governance reproductive rights women education",
"notes":"","topics":[],"status":"idea"
},

]

def vscore(sc):
    return int(sc['emotional']*2 + sc['relatability']*2 + sc['clarity']*2 +
            sc['surprise']*1.5 + sc['tension']*1 + sc['visual']*1 +
            sc['data_ready']*0.5 + sc['originality']*0.5)

for idea in ideas:
    idea['vs'] = vscore(idea['sc'])
