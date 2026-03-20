# BATCH_AS.py — Global demographics: population decline, aging, youth burden
# 20 ideas | IDs start at as_ prefix | Draws from: UN WPP, OWID population datasets

ideas = [

{
"id":"pop_collapse_2100",
"title":"Countries projected to lose more than half their population by 2100",
"sub":"South Korea -58%. Ukraine -60%. China -55%. The civilizational contraction no one is ready for.",
"type":"MAP","geo":"worldwide","fmt":"World choropleth",
"tbl":"UN, World Population Prospects (2024) via Our World in Data: Population medium projection by country to 2100 (ourworldindata.org/population-growth)",
"section":"International Statistics",
"ext":["World Bank Open Data: GDP, population, income by country (data.worldbank.org  free API)"],
"vars":["population_pct_change_2023_2100"],
"join":["old_age_dependency_ratio","birth_rate","net_migration_rate","gdp_per_capita"],
"sc":{"emotional":9,"relatability":7,"clarity":9,"surprise":10,"tension":8,"visual":10,"data_ready":9,"originality":9},
"vs":0,"tags":"population collapse decline demographic crisis South Korea Ukraine China aging fertility birth rate future 2100 projection",
"notes":"","topics":[],"status":"idea"
},

{
"id":"pop_explosion_2100",
"title":"Countries projected to more than triple in population by 2100",
"sub":"DRC +307%. Angola +308%. Somalia +267%. Tanzania +295%. The other half of the demographic map.",
"type":"MAP","geo":"worldwide","fmt":"World choropleth",
"tbl":"UN, World Population Prospects (2024) via Our World in Data: Population medium projection by country to 2100 (ourworldindata.org/population-growth)",
"section":"International Statistics",
"ext":["World Bank Open Data: GDP, population, income by country (data.worldbank.org  free API)"],
"vars":["population_pct_change_2023_2100"],
"join":["youth_dependency_ratio","birth_rate","water_access_pct","gdp_per_capita"],
"sc":{"emotional":9,"relatability":6,"clarity":9,"surprise":9,"tension":8,"visual":10,"data_ready":9,"originality":8},
"vs":0,"tags":"population explosion growth Africa DRC Angola Somalia Tanzania demographics fertility future projection 2100",
"notes":"","topics":[],"status":"idea"
},

{
"id":"pop_divergence_2100_bivariate",
"title":"Population direction by 2100: the shrinking world vs. the exploding world",
"sub":"Europe and East Asia collapse. Sub-Saharan Africa triples. The same planet, opposite futures.",
"type":"XREF","geo":"worldwide","fmt":"Bivariate choropleth",
"tbl":"UN, World Population Prospects (2024) via Our World in Data: Population medium projection by country to 2100 (ourworldindata.org/population-growth)",
"section":"International Statistics",
"ext":["World Bank Open Data: GDP, population, income by country (data.worldbank.org  free API)"],
"vars":["population_pct_change_2023_2100","current_pop_2023"],
"join":["birth_rate","old_age_dependency_ratio","gdp_per_capita"],
"sc":{"emotional":10,"relatability":7,"clarity":7,"surprise":10,"tension":9,"visual":10,"data_ready":9,"originality":10},
"vs":0,"tags":"population divergence collapse growth bivariate demographics Africa East Asia Europe South Korea DRC future 2100",
"notes":"","topics":[],"status":"idea"
},

{
"id":"old_age_dependency_world",
"title":"Old-age dependency ratio by country 2023",
"sub":"Japan: 1 worker for every 2 elderly. Niger: 1 elderly for every 30 workers. Same planet.",
"type":"MAP","geo":"worldwide","fmt":"World choropleth",
"tbl":"UN, World Population Prospects (2024) via Our World in Data: Population by age group by country 1950-2023 (ourworldindata.org/age-structure)",
"section":"International Statistics",
"ext":["World Bank Open Data: GDP, population, income by country (data.worldbank.org  free API)"],
"vars":["old_age_dependency_ratio"],
"join":["gdp_per_capita","pension_spending_pct_gdp","water_access_pct","political_regime"],
"sc":{"emotional":8,"relatability":7,"clarity":8,"surprise":8,"tension":7,"visual":10,"data_ready":10,"originality":7},
"vs":0,"tags":"aging elderly dependency ratio Japan Niger pension workers demographics retirement fiscal crisis population",
"notes":"","topics":[],"status":"idea"
},

{
"id":"youth_dependency_world",
"title":"Youth dependency ratio by country 2023",
"sub":"Central African Republic: more children than working-age adults. Iceland: 1 child per 3 workers.",
"type":"MAP","geo":"worldwide","fmt":"World choropleth",
"tbl":"UN, World Population Prospects (2024) via Our World in Data: Population by age group by country 1950-2023 (ourworldindata.org/age-structure)",
"section":"International Statistics",
"ext":["World Bank Open Data: GDP, population, income by country (data.worldbank.org  free API)"],
"vars":["youth_dependency_ratio"],
"join":["gdp_per_capita","water_access_pct","school_enrollment_pct","political_regime"],
"sc":{"emotional":8,"relatability":6,"clarity":8,"surprise":8,"tension":7,"visual":10,"data_ready":10,"originality":7},
"vs":0,"tags":"youth children dependency ratio Central African Republic Africa demographics poverty fertility population education",
"notes":"","topics":[],"status":"idea"
},

{
"id":"dependency_double_burden",
"title":"Total dependency ratio: countries carrying both the oldest and youngest populations",
"sub":"The fiscal squeeze is worst where youth AND elderly dependency are both elevated.",
"type":"MAP","geo":"worldwide","fmt":"World choropleth",
"tbl":"UN, World Population Prospects (2024) via Our World in Data: Population by age group by country 1950-2023 (ourworldindata.org/age-structure)",
"section":"International Statistics",
"ext":["World Bank Open Data: GDP, population, income by country (data.worldbank.org  free API)"],
"vars":["total_dependency_ratio","old_age_dependency_ratio","youth_dependency_ratio"],
"join":["gdp_per_capita","government_spending_pct_gdp"],
"sc":{"emotional":7,"relatability":6,"clarity":7,"surprise":8,"tension":7,"visual":9,"data_ready":9,"originality":9},
"vs":0,"tags":"dependency ratio fiscal burden elderly youth demographics total population aging poverty development",
"notes":"","topics":[],"status":"idea"
},

{
"id":"xref_old_dep_vs_gdp",
"title":"Old-age dependency ratio vs. GDP per capita by country",
"sub":"The richer the country, the more elderly per worker. Wealth buys survival but not babies.",
"type":"XREF","geo":"worldwide","fmt":"Scatter plot",
"tbl":"UN, World Population Prospects (2024) via Our World in Data: Population by age group (ourworldindata.org) + World Bank: GDP per capita (data.worldbank.org)",
"section":"International Statistics",
"ext":["World Bank Open Data: GDP, population, income by country (data.worldbank.org  free API)"],
"vars":["old_age_dependency_ratio","gdp_per_capita"],
"join":["birth_rate","life_expectancy","political_regime"],
"sc":{"emotional":7,"relatability":6,"clarity":6,"surprise":7,"tension":7,"visual":8,"data_ready":9,"originality":8},
"vs":0,"tags":"aging wealth GDP dependency ratio development economics demographics retirement pension fiscal",
"notes":"","topics":[],"status":"idea"
},

{
"id":"xref_water_regime",
"title":"Water access vs. political regime type by country 2023",
"sub":"Liberal democracies: 99.5% water access. Closed autocracies: 84.7%. The governance-infrastructure gap.",
"type":"XREF","geo":"worldwide","fmt":"Bivariate choropleth",
"tbl":"WHO/UNICEF JMP (2025) via Our World in Data: Basic drinking water access by country (ourworldindata.org/water-access) + V-Dem: Political regime classification (ourworldindata.org/democracy)",
"section":"International Statistics",
"ext":["World Bank Open Data: GDP, population, income by country (data.worldbank.org  free API)"],
"vars":["water_access_pct","political_regime"],
"join":["gdp_per_capita","sanitation_access_pct","child_mortality_rate"],
"sc":{"emotional":9,"relatability":7,"clarity":8,"surprise":9,"tension":9,"visual":10,"data_ready":9,"originality":10},
"vs":0,"tags":"water access democracy autocracy regime governance infrastructure inequality development OWID",
"notes":"","topics":[],"status":"idea"
},

{
"id":"xref_water_youth_burden",
"title":"Youth dependency ratio vs. water access by country 2023",
"sub":"Countries with the most children have the worst water. The places adding people fastest have the least infrastructure.",
"type":"XREF","geo":"worldwide","fmt":"Scatter plot",
"tbl":"UN WPP (2024) via Our World in Data: Population by age group (ourworldindata.org) + WHO/UNICEF JMP (2025): Basic drinking water access (ourworldindata.org/water-access)",
"section":"International Statistics",
"ext":["World Bank Open Data: GDP, population, income by country (data.worldbank.org  free API)"],
"vars":["youth_dependency_ratio","water_access_pct"],
"join":["gdp_per_capita","population_growth_rate","political_regime"],
"sc":{"emotional":9,"relatability":6,"clarity":7,"surprise":9,"tension":9,"visual":9,"data_ready":9,"originality":10},
"vs":0,"tags":"water access youth dependency poverty children infrastructure growth Africa demographics collision course",
"notes":"","topics":[],"status":"idea"
},

{
"id":"water_access_world",
"title":"Share of population with basic drinking water access by country 2023",
"sub":"DRC 35%. Central African Republic 36%. South Sudan 40%. In 2023.",
"type":"MAP","geo":"worldwide","fmt":"World choropleth",
"tbl":"WHO/UNICEF Joint Monitoring Programme (2025) via Our World in Data: Basic drinking water access by country 2000-2024 (ourworldindata.org/water-access)",
"section":"International Statistics",
"ext":["World Bank Open Data: GDP, population, income by country (data.worldbank.org  free API)"],
"vars":["water_access_pct"],
"join":["gdp_per_capita","political_regime","child_mortality_rate","sanitation_access_pct"],
"sc":{"emotional":10,"relatability":8,"clarity":9,"surprise":8,"tension":9,"visual":10,"data_ready":10,"originality":6},
"vs":0,"tags":"water access drinking water poverty DRC Central African Republic South Sudan infrastructure development Africa",
"notes":"","topics":[],"status":"idea"
},

{
"id":"water_access_progress_2000_2024",
"title":"Improvement in drinking water access by country 2000-2024",
"sub":"Sub-Saharan Africa: +22 points in 24 years. But DRC still under 36%. Progress and the gap that remains.",
"type":"MAP","geo":"worldwide","fmt":"World choropleth",
"tbl":"WHO/UNICEF Joint Monitoring Programme (2025) via Our World in Data: Basic drinking water access by country 2000-2024 (ourworldindata.org/water-access)",
"section":"International Statistics",
"ext":["World Bank Open Data: GDP, population, income by country (data.worldbank.org  free API)"],
"vars":["water_access_pct_change_2000_2024","water_access_pct_2024"],
"join":["gdp_per_capita_change","political_regime","population_growth_rate"],
"sc":{"emotional":8,"relatability":6,"clarity":8,"surprise":7,"tension":7,"visual":9,"data_ready":9,"originality":8},
"vs":0,"tags":"water access progress improvement 2000 2024 Africa development infrastructure Sub-Saharan WHO UNICEF",
"notes":"","topics":[],"status":"idea"
},

{
"id":"xref_water_pop_growth",
"title":"Population growth rate vs. drinking water access by country 2023",
"sub":"The fastest-growing countries have the worst water infrastructure. Chad +5.7% growth, 52% water. The compounding crisis.",
"type":"XREF","geo":"worldwide","fmt":"Scatter plot",
"tbl":"UN WPP (2024) + WHO/UNICEF JMP (2025) via Our World in Data: Population growth and water access by country",
"section":"International Statistics",
"ext":["World Bank Open Data: GDP, population, income by country (data.worldbank.org  free API)"],
"vars":["population_growth_rate","water_access_pct"],
"join":["gdp_per_capita","political_regime","youth_dependency_ratio"],
"sc":{"emotional":9,"relatability":6,"clarity":7,"surprise":9,"tension":9,"visual":9,"data_ready":9,"originality":9},
"vs":0,"tags":"population growth water access infrastructure development compounding crisis Chad Africa demographics collision",
"notes":"","topics":[],"status":"idea"
},

{
"id":"africa_children_inversion",
"title":"Where the world's children will live by 2100",
"sub":"Africa will have more children than Asia by 2100. 789M vs 655M. Asia's under-15 population collapses 40%.",
"type":"CHART","geo":"worldwide","fmt":"Stacked area chart",
"tbl":"UN, World Population Prospects (2024) via Our World in Data: Children under 15 by world region with projections to 2100 (ourworldindata.org/age-structure)",
"section":"International Statistics",
"ext":["World Bank Open Data: GDP, population, income by country (data.worldbank.org  free API)"],
"vars":["population_under15_by_region","population_under15_projection"],
"join":["fertility_rate_by_region","gdp_per_capita"],
"sc":{"emotional":9,"relatability":7,"clarity":8,"surprise":10,"tension":8,"visual":10,"data_ready":9,"originality":10},
"vs":0,"tags":"Africa Asia children under 15 demographics 2100 projection inversion population future fertility youth",
"notes":"","topics":[],"status":"idea"
},

{
"id":"india_china_crossover",
"title":"India overtakes China as the world's most populous country",
"sub":"India: 1.438B. China: 1.423B in 2023. The crossover that redraws the geopolitical map.",
"type":"CHART","geo":"worldwide","fmt":"Line chart",
"tbl":"UN, World Population Prospects (2024) via Our World in Data: Total population by country 1950-2023 (ourworldindata.org/population-growth)",
"section":"International Statistics",
"ext":["World Bank Open Data: GDP, population, income by country (data.worldbank.org  free API)"],
"vars":["population_total_india","population_total_china"],
"join":["gdp_per_capita","birth_rate","old_age_dependency_ratio"],
"sc":{"emotional":8,"relatability":8,"clarity":9,"surprise":7,"tension":7,"visual":9,"data_ready":10,"originality":6},
"vs":0,"tags":"India China population overtake most populous country crossover demographics 2023 geopolitics",
"notes":"","topics":[],"status":"idea"
},

{
"id":"ukraine_population_collapse",
"title":"Ukraine's population collapse: from 52M to 37.7M and projected to 15M by 2100",
"sub":"War, emigration, and the lowest birth rates in Europe. Ukraine may lose 60% of its people this century.",
"type":"CHART","geo":"worldwide","fmt":"Line chart",
"tbl":"UN, World Population Prospects (2024) via Our World in Data: Total population Ukraine 1950-2100 projection (ourworldindata.org/population-growth)",
"section":"International Statistics",
"ext":["World Bank Open Data: GDP, population, income by country (data.worldbank.org  free API)"],
"vars":["population_total_ukraine","population_medium_projection_ukraine"],
"join":["net_migration_rate","birth_rate","population_growth_rate"],
"sc":{"emotional":10,"relatability":7,"clarity":8,"surprise":9,"tension":10,"visual":9,"data_ready":9,"originality":8},
"vs":0,"tags":"Ukraine population collapse war emigration birth rate decline 2100 projection demographic crisis Russia",
"notes":"","topics":[],"status":"idea"
},

{
"id":"eastern_europe_depopulation",
"title":"Eastern Europe's depopulation crisis: countries losing people fastest",
"sub":"Moldova -51% by 2100. Latvia -51%. Bosnia -57%. Lithuania -58%. The slow disappearance of Eastern Europe.",
"type":"MAP","geo":"worldwide","fmt":"Regional choropleth",
"tbl":"UN, World Population Prospects (2024) via Our World in Data: Population medium projection by country to 2100 (ourworldindata.org/population-growth)",
"section":"International Statistics",
"ext":["World Bank Open Data: GDP, population, income by country (data.worldbank.org  free API)"],
"vars":["population_pct_change_2023_2100"],
"join":["net_migration_rate","birth_rate","old_age_dependency_ratio","gdp_per_capita"],
"sc":{"emotional":9,"relatability":7,"clarity":8,"surprise":9,"tension":8,"visual":10,"data_ready":9,"originality":8},
"vs":0,"tags":"Eastern Europe depopulation Moldova Latvia Lithuania Bosnia Ukraine demographic crisis emigration aging",
"notes":"","topics":[],"status":"idea"
},

{
"id":"migration_as_demographic_lifeline",
"title":"Countries where immigration is the only thing preventing population decline 2023",
"sub":"US natural growth: +0.20%. Migration adds another +0.39%. Without it, America barely replaces itself.",
"type":"MAP","geo":"worldwide","fmt":"World choropleth",
"tbl":"UN, World Population Prospects (2024) via Our World in Data: Population growth with and without migration by country (ourworldindata.org/migration)",
"section":"International Statistics",
"ext":["World Bank Open Data: GDP, population, income by country (data.worldbank.org  free API)"],
"vars":["natural_growth_rate","total_growth_rate","migration_contribution_pct"],
"join":["net_migration_rate","birth_rate","old_age_dependency_ratio"],
"sc":{"emotional":9,"relatability":8,"clarity":8,"surprise":9,"tension":9,"visual":10,"data_ready":8,"originality":9},
"vs":0,"tags":"immigration migration population growth lifeline US Europe demographic dependency anti-immigration birth rate",
"notes":"","topics":[],"status":"idea"
},

{
"id":"xref_pct_elderly_vs_water",
"title":"Share of population over 65 vs. drinking water access by country 2023",
"sub":"Counterintuitive: the oldest countries have the best water. The youngest countries have the worst. Age predicts infrastructure.",
"type":"XREF","geo":"worldwide","fmt":"Scatter plot",
"tbl":"UN WPP (2024) + WHO/UNICEF JMP (2025) via Our World in Data: Population over 65 and water access by country",
"section":"International Statistics",
"ext":["World Bank Open Data: GDP, population, income by country (data.worldbank.org  free API)"],
"vars":["pct_population_over65","water_access_pct"],
"join":["gdp_per_capita","political_regime","population_growth_rate"],
"sc":{"emotional":7,"relatability":6,"clarity":7,"surprise":9,"tension":7,"visual":9,"data_ready":9,"originality":9},
"vs":0,"tags":"elderly aging water access counterintuitive XREF development wealth infrastructure demographics correlation",
"notes":"","topics":[],"status":"idea"
},

{
"id":"south_korea_demographic_cliff",
"title":"South Korea's demographic cliff: the fastest-aging society in history",
"sub":"Fertility rate 0.72. Projected to lose 58% of its population by 2100. The sharpest demographic decline ever recorded.",
"type":"CHART","geo":"worldwide","fmt":"Line chart",
"tbl":"UN, World Population Prospects (2024) via Our World in Data: Population projection South Korea 1950-2100 (ourworldindata.org/population-growth)",
"section":"International Statistics",
"ext":["World Bank Open Data: GDP, population, income by country (data.worldbank.org  free API)"],
"vars":["population_total_south_korea","population_medium_projection_south_korea","fertility_rate_south_korea"],
"join":["old_age_dependency_ratio","gdp_per_capita","net_migration_rate"],
"sc":{"emotional":9,"relatability":7,"clarity":8,"surprise":10,"tension":9,"visual":9,"data_ready":9,"originality":8},
"vs":0,"tags":"South Korea fertility demographic cliff aging population collapse 2100 projection fastest history crisis",
"notes":"","topics":[],"status":"idea"
},

{
"id":"world_population_peak",
"title":"When does world population peak and where does it go after?",
"sub":"Peak around 10.3B near 2080. Then slow decline. The century humanity stopped growing.",
"type":"CHART","geo":"worldwide","fmt":"Line chart",
"tbl":"UN, World Population Prospects (2024) via Our World in Data: World population with UN projections 1950-2100 (ourworldindata.org/population-growth)",
"section":"International Statistics",
"ext":["World Bank Open Data: GDP, population, income by country (data.worldbank.org  free API)"],
"vars":["world_population_total","world_population_medium_projection"],
"join":["world_fertility_rate","world_life_expectancy"],
"sc":{"emotional":8,"relatability":8,"clarity":9,"surprise":8,"tension":7,"visual":9,"data_ready":9,"originality":7},
"vs":0,"tags":"world population peak 2080 decline projection UN demographics future 10 billion plateau",
"notes":"","topics":[],"status":"idea"
},

]

def vscore(sc):
    return int(sc['emotional']*2 + sc['relatability']*2 + sc['clarity']*2 +
            sc['surprise']*1.5 + sc['tension']*1 + sc['visual']*1 +
            sc['data_ready']*0.5 + sc['originality']*0.5)

for idea in ideas:
    idea['vs'] = vscore(idea['sc'])
