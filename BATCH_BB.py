# BATCH_BB.py — Growth rate divergence: who slowed, who didn't, and what it means geographically
# 18 ideas | Draws from: growth rate datasets, migration, projections
# Heavy emphasis on unexpected geographic correlations across topics

ideas = [

{
"id":"xref_asia_children_collapse_vs_africa",
"title":"Asia's children are disappearing while Africa's multiply — on the same timeline",
"sub":"Asia under-15: 1.098 billion (2023) falling to 655 million by 2100. Africa under-15: 584 million rising to 789 million. The crossover happens around 2070.",
"type":"CHART","geo":"worldwide","fmt":"Line chart",
"tbl":"UN WPP (2024) via OWID: Population under 15 by world region with projections 1950-2100 (ourworldindata.org/age-structure)",
"section":"International Statistics",
"ext":["World Bank Open Data: GDP, population, income by country (data.worldbank.org  free API)"],
"vars":["population_under15_asia","population_under15_africa","population_under15_africa_projection","population_under15_asia_projection"],
"join":["fertility_rate_by_region","gdp_per_capita","water_access_pct"],
"sc":{"emotional":90,"relatability":60,"clarity":90,"surprise":100,"tension":90,"visual":100,"data_ready":90,"originality":100},
"vs":0,"tags":"Asia children disappearing Africa multiplying same timeline crossover 2070 under-15 1B to 655M 584M to 789M",
"notes":"","topics":["population","international","history","economy","inequality"],"status":"idea"
},

{
"id":"europe_negative_natural_growth",
"title":"Europe's natural population growth went negative in 2020 — and is projected to stay there forever",
"sub":"Europe was still adding people naturally as recently as 2000. By 2020 it crossed zero. By 2100 it will be at -0.29%/year. Only immigration keeps European nations alive.",
"type":"CHART","geo":"worldwide","fmt":"Area chart",
"tbl":"UN WPP (2024) via OWID: Europe population growth rate historical and projected 1950-2100 (ourworldindata.org/population-growth)",
"section":"International Statistics",
"ext":["World Bank Open Data: GDP, population, income by country (data.worldbank.org  free API)"],
"vars":["growth_rate_europe","growth_rate_europe_projection"],
"join":["net_migration_rate","old_age_dependency_ratio","political_regime"],
"sc":{"emotional":90,"relatability":70,"clarity":90,"surprise":90,"tension":90,"visual":90,"data_ready":90,"originality":90},
"vs":0,"tags":"Europe natural growth negative 2020 forever projected -0.29 percent 2100 immigration only thing keeping alive",
"notes":"","topics":["population","international","immigration","history","democracy"],"status":"idea"
},

{
"id":"latin_america_growth_collapse",
"title":"Latin America's population growth rate fell from 2.8% in 1965 to 0.7% today — faster than Europe ever did",
"sub":"The demographic transition that took Europe 150 years took Latin America 50. The fastest fertility decline in history happened in Brazil and Mexico.",
"type":"CHART","geo":"worldwide","fmt":"Line chart",
"tbl":"UN WPP (2024) via OWID: Latin America population growth rate 1950-2100 (ourworldindata.org/population-growth)",
"section":"International Statistics",
"ext":["World Bank Open Data: GDP, population, income by country (data.worldbank.org  free API)"],
"vars":["growth_rate_latin_america","growth_rate_europe","growth_rate_world"],
"join":["fertility_rate_latin_america","gdp_per_capita","water_access_pct"],
"sc":{"emotional":80,"relatability":60,"clarity":90,"surprise":90,"tension":70,"visual":80,"data_ready":90,"originality":90},
"vs":0,"tags":"Latin America growth rate 2.8 to 0.7 percent 50 years faster than Europe demographic transition Brazil Mexico",
"notes":"","topics":["population","international","economy","history"],"status":"idea"
},

{
"id":"xref_growth_rate_vs_water_access_trend",
"title":"Regions growing fastest have the least water — and the gap keeps widening",
"sub":"Africa +2.3%/year growth, 68% water access. Europe -0.06%/year, 99% water. The places adding people have the least capacity. The places losing people have the most.",
"type":"XREF","geo":"worldwide","fmt":"Scatter plot",
"tbl":"UN WPP (2024) + WHO/UNICEF JMP via OWID: Regional growth rate + water access 2023",
"section":"International Statistics",
"ext":["World Bank Open Data: GDP, population, income by country (data.worldbank.org  free API)"],
"vars":["population_growth_rate_region","water_access_pct_region"],
"join":["gdp_per_capita","old_age_dependency_ratio"],
"sc":{"emotional":90,"relatability":60,"clarity":80,"surprise":90,"tension":90,"visual":90,"data_ready":90,"originality":90},
"vs":0,"tags":"regional growth rate water access gap widening Africa 2.3 percent 68 Europe negative 99 capacity mismatch",
"notes":"","topics":["population","environment","international","inequality","poverty"],"status":"idea"
},

{
"id":"migration_dependency_wealthy_nations",
"title":"The world's richest nations are now completely dependent on migration for population growth",
"sub":"Canada 84% of growth from migration. Germany 108% (migration exceeds natural growth). Australia 68%. The anti-immigration party's home countries need immigrants more than anyone.",
"type":"MAP","geo":"worldwide","fmt":"World choropleth",
"tbl":"UN WPP (2024) via OWID: Natural vs. total population growth rate by country 2023 (ourworldindata.org/migration)",
"section":"International Statistics",
"ext":["World Bank Open Data: GDP, population, income by country (data.worldbank.org  free API)"],
"vars":["migration_contribution_pct","natural_growth_rate","total_growth_rate"],
"join":["gdp_per_capita","old_age_dependency_ratio","political_regime","pct_population_over65"],
"sc":{"emotional":100,"relatability":80,"clarity":80,"surprise":100,"tension":100,"visual":100,"data_ready":80,"originality":100},
"vs":0,"tags":"wealthy nations dependent migration Canada 84 Germany 108 Australia 68 anti-immigration parties home countries",
"notes":"","topics":["immigration","population","international","politics","democracy","economy"],"status":"idea"
},

{
"id":"xref_population_shrinkage_gdp",
"title":"Countries shrinking in population are overwhelmingly wealthy — and vice versa",
"sub":"Every country with negative natural growth has GDP per capita above $15,000. Every country below $2,000 GDP is still growing at 2%+. Wealth buys demographic decline.",
"type":"XREF","geo":"worldwide","fmt":"Scatter plot",
"tbl":"UN WPP (2024) + World Bank via OWID: Natural growth rate + GDP per capita 2023",
"section":"International Statistics",
"ext":["World Bank Open Data: GDP, population, income by country (data.worldbank.org  free API)"],
"vars":["natural_growth_rate","gdp_per_capita"],
"join":["old_age_dependency_ratio","water_access_pct","political_regime","median_age"],
"sc":{"emotional":80,"relatability":60,"clarity":80,"surprise":90,"tension":80,"visual":90,"data_ready":90,"originality":90},
"vs":0,"tags":"population shrinkage GDP wealthy negative growth above 15000 GDP below 2000 GDP still growing 2 percent",
"notes":"","topics":["population","economy","international","inequality"],"status":"idea"
},

{
"id":"xref_asia_2100_demographic_reversal",
"title":"Asia will have fewer people in 2100 than in 2023 — and fewer children than Africa",
"sub":"Asia peaks around 2050 at 5.28 billion, then declines to 4.61 billion by 2100. Meanwhile Africa surges to 3.81 billion. The center of gravity of humanity shifts south.",
"type":"CHART","geo":"worldwide","fmt":"Stacked area chart",
"tbl":"UN WPP (2024) via OWID: Population by world region with projections 1950-2100 (ourworldindata.org/population-growth)",
"section":"International Statistics",
"ext":["World Bank Open Data: GDP, population, income by country (data.worldbank.org  free API)"],
"vars":["population_asia","population_africa","population_asia_projection","population_africa_projection"],
"join":["fertility_rate_by_region","old_age_dependency_ratio"],
"sc":{"emotional":90,"relatability":60,"clarity":90,"surprise":100,"tension":80,"visual":100,"data_ready":90,"originality":90},
"vs":0,"tags":"Asia fewer people 2100 than 2023 Africa 3.81 billion center of gravity humanity shifts south demographic reversal",
"notes":"","topics":["population","international","economy","history","trade"],"status":"idea"
},

{
"id":"xref_least_dev_growth_rate_water",
"title":"The least developed countries grow 16x faster than the most developed — and have 40% less water access",
"sub":"Least developed: 2.31% annual growth, 61% water access. More developed: 0.14%, 99% water. Two civilizations running on different planets.",
"type":"XREF","geo":"worldwide","fmt":"Bivariate choropleth",
"tbl":"UN WPP (2024) + WHO/UNICEF JMP via OWID: Growth rate + water access by development level",
"section":"International Statistics",
"ext":["World Bank Open Data: GDP, population, income by country (data.worldbank.org  free API)"],
"vars":["growth_rate_total","water_access_pct","development_level"],
"join":["gdp_per_capita","old_age_dependency_ratio","political_regime"],
"sc":{"emotional":90,"relatability":60,"clarity":80,"surprise":90,"tension":90,"visual":100,"data_ready":90,"originality":90},
"vs":0,"tags":"least developed 16x faster growth 40 percent less water most developed two civilizations different planets",
"notes":"","topics":["population","poverty","environment","international","inequality"],"status":"idea"
},

{
"id":"xref_migration_gap_elderly_burden",
"title":"Countries with the most elderly per worker are also the ones importing the most migrants",
"sub":"Japan, Italy, Germany, Finland — the highest old-age dependency ratios, the most migration-dependent. Migrants are the pension system now.",
"type":"XREF","geo":"worldwide","fmt":"Scatter plot",
"tbl":"UN WPP (2024) via OWID: Old-age dependency ratio + migration contribution by country 2023",
"section":"International Statistics",
"ext":["World Bank Open Data: GDP, population, income by country (data.worldbank.org  free API)"],
"vars":["old_age_dependency_ratio","migration_contribution_pct"],
"join":["gdp_per_capita","political_regime","natural_growth_rate","pension_spending_pct_gdp"],
"sc":{"emotional":90,"relatability":70,"clarity":80,"surprise":90,"tension":90,"visual":90,"data_ready":90,"originality":100},
"vs":0,"tags":"elderly per worker migration dependency Japan Italy Germany Finland pension system migrants now XREF",
"notes":"","topics":["immigration","population","economy","international","labor","democracy"],"status":"idea"
},

{
"id":"xref_water_access_development_income",
"title":"Water access by income group 2000-2024: the gap closed but didn't close",
"sub":"High income: 98.2% to 99.1% (near-ceiling). Low income: 41.6% to 61.6% (+20pts). The gap narrowed from 56.6 to 37.5 points — but 37.5 points is still catastrophic.",
"type":"CHART","geo":"worldwide","fmt":"Line chart",
"tbl":"WHO/UNICEF JMP (2025) + World Bank via OWID: Water access by income group 2000-2024",
"section":"International Statistics",
"ext":["World Bank Open Data: GDP, population, income by country (data.worldbank.org  free API)"],
"vars":["water_access_pct_high_income","water_access_pct_low_income","water_access_pct_lower_middle","water_access_pct_upper_middle"],
"join":["population_by_income_group","gdp_per_capita_growth"],
"sc":{"emotional":90,"relatability":60,"clarity":90,"surprise":80,"tension":80,"visual":80,"data_ready":100,"originality":80},
"vs":0,"tags":"water access income group gap closed but not 56.6 to 37.5 points high income ceiling low income 20 point gain",
"notes":"","topics":["environment","poverty","inequality","international","economy"],"status":"idea"
},

{
"id":"xref_africa_eu_size_comparison",
"title":"Africa and the EU in 2050: Africa will have more people than Europe + North America + Latin America combined",
"sub":"2050: Africa 2.5B. Europe + North America + Latin America = ~1.7B. The continent that built nothing of the current global order will soon be its demographic engine.",
"type":"CHART","geo":"worldwide","fmt":"Bar chart",
"tbl":"UN WPP (2024) via OWID: Population by world region 2050 projection (ourworldindata.org/population-growth)",
"section":"International Statistics",
"ext":["World Bank Open Data: GDP, population, income by country (data.worldbank.org  free API)"],
"vars":["population_africa_projection_2050","population_europe_projection_2050","population_north_america_projection_2050","population_latin_america_projection_2050"],
"join":["gdp_per_capita","water_access_pct","political_regime"],
"sc":{"emotional":90,"relatability":60,"clarity":90,"surprise":100,"tension":90,"visual":100,"data_ready":90,"originality":90},
"vs":0,"tags":"Africa 2050 more people than Europe North America Latin America combined 2.5B vs 1.7B demographic engine",
"notes":"","topics":["population","international","economy","trade","history","inequality"],"status":"idea"
},

{
"id":"xref_growth_rate_2100_income_class",
"title":"By 2100: high-income countries at -0.03% growth, low-income countries still at +0.37% — the gap never closes",
"sub":"The demographic transition that every development economist predicted would happen in low-income countries has not happened. The gap closes on paper, but not in the data.",
"type":"CHART","geo":"worldwide","fmt":"Line chart",
"tbl":"UN WPP (2024) via OWID: Projected population growth rate by development level 2023-2100 (ourworldindata.org/population-growth)",
"section":"International Statistics",
"ext":["World Bank Open Data: GDP, population, income by country (data.worldbank.org  free API)"],
"vars":["growth_rate_high_income_projection","growth_rate_low_income_projection","growth_rate_least_developed_projection"],
"join":["gdp_per_capita","water_access_pct","fertility_rate"],
"sc":{"emotional":80,"relatability":50,"clarity":80,"surprise":90,"tension":80,"visual":80,"data_ready":80,"originality":90},
"vs":0,"tags":"growth rate 2100 high income -0.03 low income 0.37 demographic transition never happened gap never closes",
"notes":"","topics":["population","economy","international","inequality","poverty","history"],"status":"idea"
},

{
"id":"xref_water_country_size_comparison",
"title":"DRC, Central African Republic, South Sudan: three of the world's largest countries by area — three of its worst for water access",
"sub":"DRC: 2.3M sq km, 35.7% water access. CAR: 623K sq km, 36.5%. South Sudan: 619K sq km, 39.7%. Land does not equal infrastructure.",
"type":"MAP","geo":"worldwide","fmt":"World choropleth",
"tbl":"WHO/UNICEF JMP (2025) via OWID: Water access by country 2023 (ourworldindata.org/water-access)",
"section":"International Statistics",
"ext":["World Bank Open Data: GDP, population, income by country (data.worldbank.org  free API)"],
"vars":["water_access_pct","country_area_sq_km"],
"join":["gdp_per_capita","political_regime","population_density"],
"sc":{"emotional":90,"relatability":60,"clarity":90,"surprise":90,"tension":90,"visual":100,"data_ready":100,"originality":90},
"vs":0,"tags":"DRC CAR South Sudan largest countries area worst water access land not infrastructure 35 36 39 percent",
"notes":"","topics":["environment","poverty","international","geography","inequality"],"status":"idea"
},

{
"id":"xref_uk_vs_nigeria_crossover",
"title":"Nigeria surpassed the UK in population in 1996 and will be 4x larger by 2100",
"sub":"1950: UK 51M, Nigeria 39M. 2023: UK 67M, Nigeria 228M. 2100: UK 75M (projected), Nigeria 546M. The former colony now dwarfs the colonizer.",
"type":"CHART","geo":"worldwide","fmt":"Line chart",
"tbl":"UN WPP (2024) via OWID: UK and Nigeria population 1950-2100 with projections (ourworldindata.org/population-growth)",
"section":"International Statistics",
"ext":["World Bank Open Data: GDP, population, income by country (data.worldbank.org  free API)"],
"vars":["population_nigeria","population_uk","population_nigeria_projection","population_uk_projection"],
"join":["gdp_per_capita","water_access_pct","median_age"],
"sc":{"emotional":90,"relatability":80,"clarity":90,"surprise":100,"tension":90,"visual":90,"data_ready":90,"originality":100},
"vs":0,"tags":"Nigeria UK crossover 1996 4x larger 2100 former colony dwarfs colonizer 1950 UK 51M Nigeria 39M",
"notes":"","topics":["population","international","history","economy","inequality"],"status":"idea"
},

{
"id":"xref_growth_unchanged_water_stuck",
"title":"The least developed countries' growth rate has not changed since 1960. Neither has their water gap.",
"sub":"Least developed growth rate: 2.36% (1960), 2.31% (2023). Low income water access: 41.6% (2000), 61.6% (2024) — still 37 points below high income. Both needles barely moved.",
"type":"CHART","geo":"worldwide","fmt":"Dual axis line chart",
"tbl":"UN WPP (2024) + WHO/UNICEF JMP via OWID: Least developed growth rate + low income water access 1960-2024",
"section":"International Statistics",
"ext":["World Bank Open Data: GDP, population, income by country (data.worldbank.org  free API)"],
"vars":["growth_rate_least_developed","water_access_pct_low_income"],
"join":["gdp_per_capita_low_income","youth_dependency_ratio"],
"sc":{"emotional":90,"relatability":50,"clarity":80,"surprise":90,"tension":90,"visual":80,"data_ready":90,"originality":100},
"vs":0,"tags":"least developed growth rate unchanged 1960 water gap stuck both needles barely moved structural failure",
"notes":"","topics":["poverty","population","environment","international","inequality","history"],"status":"idea"
},

{
"id":"xref_africa_population_vs_gdp_2100",
"title":"Africa will have 38% of all humans by 2100 but currently generates about 3% of world GDP",
"sub":"The largest demographic block of the 22nd century is also currently the smallest economic one. The mismatch between people and power has never been this stark.",
"type":"XREF","geo":"worldwide","fmt":"Bivariate choropleth",
"tbl":"UN WPP (2024) projections + World Bank: GDP share by region",
"section":"International Statistics",
"ext":["World Bank Open Data: GDP, population, income by country (data.worldbank.org  free API)"],
"vars":["population_africa_projection_2100","gdp_share_africa"],
"join":["water_access_pct","political_regime","youth_dependency_ratio"],
"sc":{"emotional":90,"relatability":60,"clarity":80,"surprise":100,"tension":100,"visual":100,"data_ready":80,"originality":100},
"vs":0,"tags":"Africa 38 percent humanity 2100 3 percent world GDP people power mismatch demographic economic divergence",
"notes":"","topics":["population","economy","international","inequality","trade","history"],"status":"idea"
},

{
"id":"xref_southern_asia_water_rise",
"title":"Central and Southern Asia improved water access from 82% to 95% in 24 years — the fastest gain of any major region",
"sub":"South Asia added 13 percentage points of water access while adding 400 million people. The largest improvement in infrastructure delivery in recent history, almost unreported.",
"type":"CHART","geo":"worldwide","fmt":"Line chart",
"tbl":"WHO/UNICEF JMP (2025) via OWID: Water access by UN SDG region 2000-2024 (ourworldindata.org/water-access)",
"section":"International Statistics",
"ext":["World Bank Open Data: GDP, population, income by country (data.worldbank.org  free API)"],
"vars":["water_access_pct_central_southern_asia","water_access_pct_sub_saharan_africa","water_access_pct_world"],
"join":["population_south_asia","gdp_per_capita_south_asia"],
"sc":{"emotional":80,"relatability":60,"clarity":90,"surprise":90,"tension":70,"visual":80,"data_ready":100,"originality":90},
"vs":0,"tags":"South Asia water access 82 to 95 percent fastest major region gain 13 points 400 million people unreported",
"notes":"","topics":["environment","international","infrastructure","poverty","population"],"status":"idea"
},

{
"id":"xref_population_growth_rate_to_2100_divergence",
"title":"By 2100: Africa still growing, Asia shrinking, Europe deep in decline — the three-way demographic split",
"sub":"Africa 2100: +0.36%/yr. Asia: -0.48%/yr. Europe: -0.29%/yr. The same world, three completely different demographic futures converging in the same century.",
"type":"CHART","geo":"worldwide","fmt":"Line chart",
"tbl":"UN WPP (2024) via OWID: Population growth rate by region projected 2023-2100 (ourworldindata.org/population-growth)",
"section":"International Statistics",
"ext":["World Bank Open Data: GDP, population, income by country (data.worldbank.org  free API)"],
"vars":["growth_rate_africa_projection","growth_rate_asia_projection","growth_rate_europe_projection","growth_rate_latin_america_projection"],
"join":["fertility_rate_by_region","old_age_dependency_ratio"],
"sc":{"emotional":90,"relatability":60,"clarity":90,"surprise":90,"tension":80,"visual":90,"data_ready":80,"originality":90},
"vs":0,"tags":"2100 Africa growing Asia shrinking Europe decline three-way demographic split divergence projections",
"notes":"","topics":["population","international","economy","history","trade"],"status":"idea"
},

]

def vscore(sc):
    return int((sc.get('emotional',0)*2 + sc.get('relatability',0)*2 + sc.get('clarity',0)*2 +
               sc.get('surprise',0)*1.5 + sc.get('tension',0)*1 + sc.get('visual',0)*1 +
               sc.get('data_ready',0)*0.5 + sc.get('originality',0)*0.5) / 10.5)

for idea in ideas:
    idea['vs'] = vscore(idea['sc'])

if __name__ == '__main__':
    print(f"BATCH_BB: {len(ideas)} ideas")
    for i in sorted(ideas, key=lambda x: -x['vs']):
        print(f"  vs={i['vs']:3d}  {i['id']}")
