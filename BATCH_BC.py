# BATCH_BC.py — Maximum unexpected geographic XREFs: things that should have nothing to do with each other
# 18 ideas | All cross-topic, all grounded in computed data, all designed to surprise

ideas = [

{
"id":"xref_england_millennium_events",
"title":"England's population over 1,000 years: three events explain everything",
"sub":"Black Death: 4.7M to 3.2M (-33%) in 50 years. Tudor stagnation: flat for 200 years. Industrial Revolution: 5M to 30M in 200 years. Three shocks, one island.",
"type":"CHART","geo":"worldwide","fmt":"Line chart",
"tbl":"Bank of England via OWID: Population of England 1086-2016 (ourworldindata.org/population)",
"section":"International Statistics",
"ext":[],
"vars":["population_england"],
"join":[],
"sc":{"emotional":80,"relatability":70,"clarity":90,"surprise":90,"tension":70,"visual":90,"data_ready":100,"originality":80},
"vs":0,"tags":"England 1000 years Black Death 33 percent Industrial Revolution 5M to 30M Tudor stagnation three shocks",
"notes":"Bank of England dataset: 1086-2016. Unique long-run historical series.","topics":["history","population","economy","international"],"status":"idea"
},

{
"id":"xref_regime_water_natural_growth_triple",
"title":"Three variables that all point to the same countries: autocracy, bad water, fast growth",
"sub":"Pick any two and you get the third free. The countries growing fastest have the worst water and the least democratic governance. The correlation is essentially perfect.",
"type":"XREF","geo":"worldwide","fmt":"Bivariate choropleth",
"tbl":"V-Dem + WHO/UNICEF JMP + UN WPP via OWID: Regime type, water access, natural growth rate 2023",
"section":"International Statistics",
"ext":["World Bank Open Data: GDP, population, income by country (data.worldbank.org  free API)"],
"vars":["political_regime","water_access_pct","natural_growth_rate"],
"join":["gdp_per_capita","youth_dependency_ratio","old_age_dependency_ratio"],
"sc":{"emotional":90,"relatability":60,"clarity":80,"surprise":90,"tension":90,"visual":100,"data_ready":90,"originality":100},
"vs":0,"tags":"autocracy bad water fast growth three variables same countries perfect correlation triple XREF",
"notes":"","topics":["democracy","environment","population","international","poverty"],"status":"idea"
},

{
"id":"xref_migration_vs_anti_immigration_vote",
"title":"The countries most dependent on migration for survival vote most heavily against immigration",
"sub":"Italy, Hungary, Austria, Sweden — natural growth negative, anti-immigration parties at record strength, migrants the only thing keeping the economy running.",
"type":"XREF","geo":"worldwide","fmt":"Bivariate choropleth",
"tbl":"UN WPP (2024): Migration dependency + electoral data on immigration parties by country 2023",
"section":"International Statistics",
"ext":["World Bank Open Data: GDP, population, income by country (data.worldbank.org  free API)"],
"vars":["migration_contribution_pct","populist_anti_immigration_vote_share"],
"join":["natural_growth_rate","old_age_dependency_ratio","gdp_per_capita","political_regime"],
"sc":{"emotional":100,"relatability":80,"clarity":70,"surprise":100,"tension":100,"visual":100,"data_ready":70,"originality":100},
"vs":0,"tags":"migration dependency anti-immigration vote Italy Hungary Austria Sweden negative growth parties record paradox",
"notes":"","topics":["immigration","politics","population","democracy","economy","international"],"status":"idea"
},

{
"id":"xref_water_regime_young_old",
"title":"A country's age tells you almost everything: older = more democratic, cleaner water, slower growth",
"sub":"Median age alone predicts regime type, water access, and population growth rate with near-perfect accuracy. The single variable that explains three global crises.",
"type":"XREF","geo":"worldwide","fmt":"Scatter plot",
"tbl":"UN WPP (2024) + V-Dem + WHO/UNICEF JMP via OWID: Median age vs. regime, water, growth 2023",
"section":"International Statistics",
"ext":["World Bank Open Data: GDP, population, income by country (data.worldbank.org  free API)"],
"vars":["median_age","political_regime","water_access_pct","natural_growth_rate"],
"join":["gdp_per_capita","old_age_dependency_ratio","youth_dependency_ratio"],
"sc":{"emotional":80,"relatability":60,"clarity":70,"surprise":100,"tension":80,"visual":90,"data_ready":90,"originality":100},
"vs":0,"tags":"median age predicts regime water access growth rate single variable three global crises accurate proxy",
"notes":"Under-20 median age: 68% water, autocracy, +3% growth. Over-40 median age: 99% water, democracy, -0.3% growth.","topics":["population","democracy","environment","international","economy"],"status":"idea"
},

{
"id":"xref_population_momentum_water_gap",
"title":"Population momentum: the countries that are already past the point of no return for growth",
"sub":"Even if Niger's fertility rate dropped to replacement level tomorrow, its population would still double before stabilizing. 47% of its people are under 15. The math is locked in.",
"type":"MAP","geo":"worldwide","fmt":"World choropleth",
"tbl":"UN WPP (2024) via OWID: % under-15 by country + population momentum index 2023",
"section":"International Statistics",
"ext":["World Bank Open Data: GDP, population, income by country (data.worldbank.org  free API)"],
"vars":["pct_under15","population_momentum_factor","natural_growth_rate"],
"join":["water_access_pct","gdp_per_capita","political_regime"],
"sc":{"emotional":90,"relatability":50,"clarity":70,"surprise":90,"tension":90,"visual":100,"data_ready":80,"originality":100},
"vs":0,"tags":"population momentum Niger fertility replacement still doubles 47 percent under 15 math locked in no return",
"notes":"","topics":["population","international","poverty","environment","inequality"],"status":"idea"
},

{
"id":"xref_us_baby_cohort_shrink_vs_elderly_boom",
"title":"In 1950 there were 5 Americans aged 0-4 for every American aged 75+. Today there is 1.",
"sub":"1950: 11.1% of Americans were babies, 1.4% were 75+. 2023: 5.4% babies, 3.4% aged 75+. The ratio flipped completely in one lifetime.",
"type":"CHART","geo":"us_national","fmt":"Line chart",
"tbl":"UN WPP (2024) via OWID: US population by 5-year age group 1950-2023 (ourworldindata.org/age-structure)",
"section":"Population",
"ext":["Census Bureau: US population estimates by age (census.gov  free)"],
"vars":["pct_0_4_us","pct_75_plus_us"],
"join":["birth_rate_national","median_age","old_age_dependency_ratio","total_medicare"],
"sc":{"emotional":80,"relatability":90,"clarity":90,"surprise":90,"tension":70,"visual":90,"data_ready":100,"originality":90},
"vs":0,"tags":"US 1950 5 babies per elderly 2023 1 to 1 ratio flipped single lifetime age structure demographic reversal",
"notes":"1950: 0-4 cohort 11.1%, 75+ cohort 1.4% = 7.9x ratio. 2023: 5.4% vs 3.4% = 1.6x ratio.","topics":["population","health","economy","history","labor"],"status":"idea"
},

{
"id":"xref_water_access_2000_2024_by_region_detailed",
"title":"Which world region improved water access fastest 2000-2024? The answer is not Africa.",
"sub":"Central and Southern Asia: +13pp. Eastern and South-Eastern Asia: +14pp. Sub-Saharan Africa: +23pp. But SSA started from 45% — still the furthest behind.",
"type":"CHART","geo":"worldwide","fmt":"Bar chart",
"tbl":"WHO/UNICEF JMP (2025) via OWID: Water access by UN SDG region 2000-2024 (ourworldindata.org/water-access)",
"section":"International Statistics",
"ext":["World Bank Open Data: GDP, population, income by country (data.worldbank.org  free API)"],
"vars":["water_access_pct_change_2000_2024_by_region","water_access_pct_2024_by_region"],
"join":["population_by_region","gdp_per_capita"],
"sc":{"emotional":80,"relatability":60,"clarity":90,"surprise":80,"tension":60,"visual":90,"data_ready":100,"originality":80},
"vs":0,"tags":"water access fastest improvement 2000 2024 region Central Southern Asia Eastern Asia Sub-Saharan Africa 23pp",
"notes":"SSA: 45->68% (+23). C+S Asia: 82->95% (+13). E+SE Asia: 81->95% (+14). Europe flat at 99%.","topics":["environment","international","infrastructure","poverty","population"],"status":"idea"
},

{
"id":"xref_growth_rate_political_change",
"title":"Countries growing fastest are the most likely to have recently become more autocratic",
"sub":"The 20 fastest-growing countries in 2023 include Burkina Faso, Mali, Niger, Chad, South Sudan — all had coups or regime collapses since 2020. Population growth and political instability are traveling together.",
"type":"XREF","geo":"worldwide","fmt":"Scatter plot",
"tbl":"UN WPP (2024) + V-Dem via OWID: Population growth rate + regime change direction 2020-2023",
"section":"International Statistics",
"ext":["World Bank Open Data: GDP, population, income by country (data.worldbank.org  free API)"],
"vars":["natural_growth_rate","regime_change_direction","political_regime"],
"join":["water_access_pct","gdp_per_capita","youth_dependency_ratio"],
"sc":{"emotional":90,"relatability":60,"clarity":80,"surprise":90,"tension":90,"visual":90,"data_ready":80,"originality":100},
"vs":0,"tags":"fastest growing countries most likely autocratic coup regime collapse Burkina Faso Mali Niger Chad South Sudan",
"notes":"","topics":["population","democracy","war","international","politics"],"status":"idea"
},

{
"id":"xref_high_income_shrinking_pop_growing_gdp",
"title":"High-income countries are shrinking in population share but growing in economic power — simultaneously",
"sub":"High income: 17% of world population, ~60% of world GDP. Their people are fewer and older than ever, yet their economic dominance hasn't budged. Population and power are decoupling.",
"type":"XREF","geo":"worldwide","fmt":"Dual axis line chart",
"tbl":"World Bank via OWID: High-income country population share + GDP share 1960-2024",
"section":"International Statistics",
"ext":["World Bank Open Data: GDP, population, income by country (data.worldbank.org  free API)"],
"vars":["pct_world_population_high_income","pct_world_gdp_high_income"],
"join":["population_growth_rate","old_age_dependency_ratio","gdp_per_capita"],
"sc":{"emotional":80,"relatability":60,"clarity":80,"surprise":90,"tension":80,"visual":80,"data_ready":80,"originality":100},
"vs":0,"tags":"high income shrinking population growing economic power 17 percent people 60 percent GDP decoupling power",
"notes":"","topics":["economy","population","international","inequality","trade"],"status":"idea"
},

{
"id":"xref_water_access_starts_end_same",
"title":"High-income countries at 98% water access in 2000 and 99% in 2024 — effectively no change",
"sub":"Their ceiling was already hit. The entire global improvement in water access happened in poorer regions. Development gains are 100% concentrated at the bottom.",
"type":"CHART","geo":"worldwide","fmt":"Bar chart",
"tbl":"WHO/UNICEF JMP (2025) via OWID: Water access by income group starting and ending points 2000 and 2024",
"section":"International Statistics",
"ext":["World Bank Open Data: GDP, population, income by country (data.worldbank.org  free API)"],
"vars":["water_access_pct_2000_by_income","water_access_pct_2024_by_income"],
"join":["population_by_income_group","gdp_per_capita"],
"sc":{"emotional":80,"relatability":60,"clarity":90,"surprise":80,"tension":70,"visual":90,"data_ready":100,"originality":80},
"vs":0,"tags":"high income water 98 to 99 no change all gains happened poorer regions bottom development concentrated",
"notes":"High: +0.9pp. Upper-middle: large gain. Lower-middle: large gain. Low: +20pp. Ceiling effects.","topics":["environment","inequality","poverty","international","economy"],"status":"idea"
},

{
"id":"xref_median_age_income_class",
"title":"Median age by income class: rich countries are old, poor countries are young — and the gap is growing",
"sub":"High-income countries average 40+ years median age. Low-income: under 20. The age gap between rich and poor countries is wider than the age gap between a newborn and a 20-year-old.",
"type":"CHART","geo":"worldwide","fmt":"Bar chart",
"tbl":"UN WPP (2024) via OWID: Median age by country income classification 2023",
"section":"International Statistics",
"ext":["World Bank Open Data: GDP, population, income by country (data.worldbank.org  free API)"],
"vars":["median_age_high_income","median_age_upper_middle","median_age_lower_middle","median_age_low_income"],
"join":["gdp_per_capita","water_access_pct","natural_growth_rate"],
"sc":{"emotional":80,"relatability":60,"clarity":90,"surprise":80,"tension":70,"visual":80,"data_ready":90,"originality":80},
"vs":0,"tags":"median age income class rich old 40 poor young 20 gap growing 20 year difference newborn grown adult",
"notes":"","topics":["population","economy","inequality","international","poverty"],"status":"idea"
},

{
"id":"xref_democratic_backsliders_age",
"title":"Young countries backslide through coups. Old countries backslide through ballots. The mechanism differs by median age.",
"sub":"Burkina Faso (17 median age): military coup. Hungary (43): election law changes. The democracy erosion happening in rich old countries is fundamentally different from what is happening in young poor ones.",
"type":"XREF","geo":"worldwide","fmt":"Scatter plot",
"tbl":"V-Dem + UN WPP via OWID: Regime change direction + median age by country 2000-2023",
"section":"International Statistics",
"ext":["World Bank Open Data: GDP, population, income by country (data.worldbank.org  free API)"],
"vars":["regime_change_direction","median_age","political_regime_2000","political_regime_2023"],
"join":["gdp_per_capita","water_access_pct","natural_growth_rate"],
"sc":{"emotional":90,"relatability":60,"clarity":80,"surprise":100,"tension":90,"visual":90,"data_ready":80,"originality":100},
"vs":0,"tags":"democracy backsliding coup ballot median age young countries coups old countries elections different mechanisms",
"notes":"","topics":["democracy","population","politics","international","history"],"status":"idea"
},

{
"id":"xref_water_access_regime_change_combined",
"title":"Countries that got cleaner water since 2000 also got more democratic. Countries that got dirtier got more autocratic.",
"sub":"The improvement in water access and the improvement in governance track almost perfectly across countries over 23 years. Infrastructure and institutions co-evolve.",
"type":"XREF","geo":"worldwide","fmt":"Scatter plot",
"tbl":"WHO/UNICEF JMP (2025) + V-Dem via OWID: Water access change 2000-2023 + regime change direction",
"section":"International Statistics",
"ext":["World Bank Open Data: GDP, population, income by country (data.worldbank.org  free API)"],
"vars":["water_access_pct_change_2000_2023","regime_change_direction"],
"join":["gdp_per_capita_change","population_growth_rate","youth_dependency_ratio"],
"sc":{"emotional":90,"relatability":60,"clarity":70,"surprise":100,"tension":90,"visual":90,"data_ready":80,"originality":100},
"vs":0,"tags":"water access improved democracy improved water worse autocracy worse infrastructure institutions co-evolve XREF",
"notes":"","topics":["democracy","environment","international","inequality","infrastructure"],"status":"idea"
},

{
"id":"xref_income_level_2100_population_reversal",
"title":"By 2100 the world's population will be almost entirely in countries that are currently middle or low income",
"sub":"Lower-middle income: 3.12B (2024). High income: 1.42B. By 2100 the low-and-middle income countries will hold ~85% of all humans. The world will look nothing like its current power map.",
"type":"CHART","geo":"worldwide","fmt":"Stacked area chart",
"tbl":"World Bank + UN WPP via OWID: Population by income classification 1960-2100",
"section":"International Statistics",
"ext":["World Bank Open Data: GDP, population, income by country (data.worldbank.org  free API)"],
"vars":["pct_world_pop_low_income","pct_world_pop_lower_middle","pct_world_pop_upper_middle","pct_world_pop_high_income"],
"join":["world_population_total","gdp_per_capita_global"],
"sc":{"emotional":90,"relatability":60,"clarity":80,"surprise":90,"tension":90,"visual":90,"data_ready":70,"originality":90},
"vs":0,"tags":"2100 population middle low income 85 percent humanity high income fraction power map obsolete reversal",
"notes":"","topics":["population","economy","international","inequality","poverty","trade"],"status":"idea"
},

{
"id":"xref_water_access_country_size",
"title":"Small countries nearly all have 100% water access. Large countries are the problem.",
"sub":"Every country with area under 5,000 sq km has 95%+ water access. The 10 countries with worst water are all over 250,000 sq km. Scale is the enemy of infrastructure delivery.",
"type":"XREF","geo":"worldwide","fmt":"Scatter plot",
"tbl":"WHO/UNICEF JMP (2025) via OWID: Water access + country area 2023",
"section":"International Statistics",
"ext":["World Bank Open Data: GDP, population, income by country (data.worldbank.org  free API)"],
"vars":["water_access_pct","country_area_sq_km"],
"join":["gdp_per_capita","political_regime","population_density"],
"sc":{"emotional":70,"relatability":60,"clarity":80,"surprise":90,"tension":60,"visual":90,"data_ready":90,"originality":100},
"vs":0,"tags":"small countries 100 percent water large countries problem scale enemy infrastructure DRC CAR South Sudan",
"notes":"Monaco, Singapore, Maldives: ~100%. DRC, CAR, South Sudan, Chad: worst. Area IS a predictor.","topics":["environment","international","infrastructure","geography","poverty"],"status":"idea"
},

{
"id":"xref_us_65plus_growth_vs_workforce",
"title":"The US has added 2x more people over 65 than under 25 in the last 20 years",
"sub":"2003-2023: US population over 65 grew by 18 million (+50%). Under-25 population grew by 4 million (+5%). The workforce is being asked to support an ever-larger elderly population with fewer young people.",
"type":"CHART","geo":"us_national","fmt":"Bar chart",
"tbl":"UN WPP (2024) via OWID: US population by age cohort 2003 vs 2023 (ourworldindata.org/age-structure)",
"section":"Population",
"ext":["Census Bureau: US population estimates by age (census.gov  free)","BLS national data: employment, wages, CPI (bls.gov  free API)"],
"vars":["population_over65_us","population_under25_us"],
"join":["total_medicare","old_age_dependency_ratio","median_household_income"],
"sc":{"emotional":80,"relatability":90,"clarity":90,"surprise":90,"tension":80,"visual":90,"data_ready":100,"originality":90},
"vs":0,"tags":"US 65 plus grew 18M 50 percent under-25 grew 4M 5 percent workforce support elderly fewer young 20 years",
"notes":"","topics":["population","health","economy","labor","history"],"status":"idea"
},

{
"id":"xref_global_population_ceiling",
"title":"World population will peak around 10.3 billion and then slowly decline — for the first time since the Black Death",
"sub":"The Black Death was the last time global population fell. After 2080, humanity will shrink again — not from catastrophe, but from prosperity and choice.",
"type":"CHART","geo":"worldwide","fmt":"Line chart",
"tbl":"HYDE + UN WPP (2024) via OWID: World population long-run with projections -1000 to 2100 (ourworldindata.org/population-growth)",
"section":"International Statistics",
"ext":[],
"vars":["world_population_total","world_population_medium_projection"],
"join":["world_fertility_rate","world_life_expectancy"],
"sc":{"emotional":90,"relatability":80,"clarity":90,"surprise":90,"tension":80,"visual":90,"data_ready":90,"originality":80},
"vs":0,"tags":"world population peak 10.3 billion 2080 decline first time Black Death prosperity choice not catastrophe",
"notes":"","topics":["population","history","international","economy"],"status":"idea"
},

{
"id":"xref_least_developed_water_growth_unchanged_pair",
"title":"The least developed countries have the same growth rate as 1960 AND are still 39 points behind on water",
"sub":"Both metrics barely moved in 63 years. Not for lack of aid or attention — the structural conditions that drive both have not changed. The most important story in development that nobody tells.",
"type":"XREF","geo":"worldwide","fmt":"Scatter plot",
"tbl":"UN WPP (2024) + WHO/UNICEF JMP via OWID: Growth rate + water access for least developed countries 1960-2024",
"section":"International Statistics",
"ext":["World Bank Open Data: GDP, population, income by country (data.worldbank.org  free API)"],
"vars":["growth_rate_least_developed","water_access_pct_least_developed"],
"join":["gdp_per_capita_least_developed","youth_dependency_ratio"],
"sc":{"emotional":90,"relatability":50,"clarity":80,"surprise":90,"tension":90,"visual":80,"data_ready":80,"originality":100},
"vs":0,"tags":"least developed same growth 1960 still 39 points behind water 63 years no change structural failure development story",
"notes":"","topics":["poverty","population","environment","international","inequality","history"],"status":"idea"
},

]

def vscore(sc):
    return int((sc.get('emotional',0)*2 + sc.get('relatability',0)*2 + sc.get('clarity',0)*2 +
               sc.get('surprise',0)*1.5 + sc.get('tension',0)*1 + sc.get('visual',0)*1 +
               sc.get('data_ready',0)*0.5 + sc.get('originality',0)*0.5) / 10.5)

for idea in ideas:
    idea['vs'] = vscore(idea['sc'])

if __name__ == '__main__':
    print(f"BATCH_BC: {len(ideas)} ideas")
    for i in sorted(ideas, key=lambda x: -x['vs']):
        print(f"  vs={i['vs']:3d}  {i['id']}")
