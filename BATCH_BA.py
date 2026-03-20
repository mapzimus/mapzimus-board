# BATCH_BA.py — Age structure shocks: youth bulges, graying nations, pyramids inverted
# 20 ideas | Draws from: population-by-five-year-age-group, population-by-age-group-with-projections
# Cross-referenced with regime type, water access, income level

ideas = [

{
"id":"us_age_pyramid_flip_1950_2023",
"title":"The American age pyramid flipped: babies 11% of US population in 1950, 5.4% today",
"sub":"The 0-4 cohort halved as a share of America. The 85+ cohort quadrupled. The same country, reversed.",
"type":"CHART","geo":"us_national","fmt":"Bar chart",
"tbl":"UN WPP (2024) via OWID: US population by 5-year age group 1950 vs 2023 (ourworldindata.org/age-structure)",
"section":"Population",
"ext":["Census Bureau: US population estimates by age (census.gov  free)"],
"vars":["population_by_age_group_us_1950","population_by_age_group_us_2023"],
"join":["birth_rate_state","median_age","old_age_dependency_ratio"],
"sc":{"emotional":80,"relatability":80,"clarity":80,"surprise":80,"tension":70,"visual":100,"data_ready":90,"originality":80},
"vs":0,"tags":"US age pyramid flip 1950 2023 babies elderly population structure reversed baby boom bust aging",
"notes":"Classic population pyramid: wide base 1950, inverted top-heavy 2023. Baby boom echo still visible in 55-64 bulge.","topics":["population","history","economy","health"],"status":"idea"
},

{
"id":"japan_vs_niger_age_pyramid",
"title":"Japan vs. Niger: two age pyramids that could not look more different",
"sub":"Japan: 12% under-15, 30% over-65. Niger: 47% under-15, 3% over-65. Two planets in one world.",
"type":"CHART","geo":"worldwide","fmt":"Bar chart",
"tbl":"UN WPP (2024) via OWID: Population by 5-year age group Japan and Niger 2023 (ourworldindata.org/age-structure)",
"section":"International Statistics",
"ext":["World Bank Open Data: GDP, population, income by country (data.worldbank.org  free API)"],
"vars":["population_by_age_group_japan","population_by_age_group_niger"],
"join":["gdp_per_capita","water_access_pct","political_regime","median_age"],
"sc":{"emotional":90,"relatability":70,"clarity":90,"surprise":100,"tension":80,"visual":100,"data_ready":100,"originality":90},
"vs":0,"tags":"Japan Niger age pyramid comparison under-15 over-65 opposite demographic worlds visualized",
"notes":"35 year median age gap. Japan elderly > Niger entire. Best dual-pyramid chart in the dataset.","topics":["population","international","economy","inequality","history"],"status":"idea"
},

{
"id":"age_structure_regime_type",
"title":"Liberal democracies average 18% elderly, 17% youth. Closed autocracies: 5% elderly, 31% youth.",
"sub":"The age gap between regime types is wider than the gap between any two continents.",
"type":"XREF","geo":"worldwide","fmt":"Scatter plot",
"tbl":"UN WPP (2024) + V-Dem via OWID: Population by age group + regime type by country 2023",
"section":"International Statistics",
"ext":["World Bank Open Data: GDP, population, income by country (data.worldbank.org  free API)"],
"vars":["pct_over65","pct_under15","political_regime"],
"join":["gdp_per_capita","water_access_pct","median_age","natural_growth_rate"],
"sc":{"emotional":80,"relatability":60,"clarity":80,"surprise":90,"tension":80,"visual":90,"data_ready":100,"originality":90},
"vs":0,"tags":"age structure regime type liberal democracy autocracy elderly youth percentage gap wider than continents",
"notes":"Liberal democracies: 18% over-65 avg. Closed autocracies: 5% over-65. 13pp gap.","topics":["democracy","population","international","politics"],"status":"idea"
},

{
"id":"youth_bulge_map_2023",
"title":"The youth bulge map: countries where babies outnumber young adults 2-to-1",
"sub":"In DRC, Chad, and Somalia, the 0-4 age cohort is more than twice the size of the 20-24 cohort. The population engine is running at full speed with no off switch.",
"type":"MAP","geo":"worldwide","fmt":"World choropleth",
"tbl":"UN WPP (2024) via OWID: Population by 5-year age group by country 2023 (ourworldindata.org/age-structure)",
"section":"International Statistics",
"ext":["World Bank Open Data: GDP, population, income by country (data.worldbank.org  free API)"],
"vars":["ratio_under5_to_20_24","pct_under15"],
"join":["water_access_pct","political_regime","gdp_per_capita","natural_growth_rate"],
"sc":{"emotional":90,"relatability":60,"clarity":80,"surprise":90,"tension":90,"visual":100,"data_ready":90,"originality":100},
"vs":0,"tags":"youth bulge babies outnumber young adults DRC Chad Somalia 2to1 population momentum explosive",
"notes":"DRC 2.10x, Chad 2.04x, Somalia 2.02x. 45 countries with ratio above 1.3. Explosive demographic map.","topics":["population","international","inequality","poverty"],"status":"idea"
},

{
"id":"least_developed_growth_unchanged",
"title":"The least developed countries grew at 2.36% in 1960 and 2.31% in 2023 — 63 years, zero progress",
"sub":"While the developed world slowed from 1.16% to 0.14%, the least developed world barely moved. The gap was already wide. It is now a chasm.",
"type":"CHART","geo":"worldwide","fmt":"Dual axis line chart",
"tbl":"UN WPP (2024) via OWID: Population growth rate by development level 1950-2023 (ourworldindata.org/population-growth)",
"section":"International Statistics",
"ext":["World Bank Open Data: GDP, population, income by country (data.worldbank.org  free API)"],
"vars":["growth_rate_least_developed","growth_rate_more_developed","growth_rate_world"],
"join":["water_access_pct","gdp_per_capita","old_age_dependency_ratio"],
"sc":{"emotional":90,"relatability":60,"clarity":90,"surprise":100,"tension":90,"visual":90,"data_ready":90,"originality":100},
"vs":0,"tags":"least developed countries growth rate unchanged 1960 2023 63 years no change developed world slowed chasm",
"notes":"Least dev: 2.36% (1960) vs 2.31% (2023). More dev: 1.16% (1960) vs 0.14% (2023). Stunning divergence.","topics":["poverty","population","international","inequality","history"],"status":"idea"
},

{
"id":"high_income_population_share_collapse",
"title":"High-income countries held 30% of world population in 1960. Today: 17%. And falling.",
"sub":"In 1960, nearly 1 in 3 people alive lived in a high-income country. Now it is less than 1 in 6. The world got bigger around the rich world.",
"type":"CHART","geo":"worldwide","fmt":"Area chart",
"tbl":"World Bank + OWID: Population by income classification 1960-2024 (ourworldindata.org/population)",
"section":"International Statistics",
"ext":["World Bank Open Data: GDP, population, income by country (data.worldbank.org  free API)"],
"vars":["pct_high_income_world_pop","pct_low_income_world_pop","pct_lower_middle_world_pop","pct_upper_middle_world_pop"],
"join":["world_population_total","gdp_per_capita_global"],
"sc":{"emotional":80,"relatability":70,"clarity":90,"surprise":90,"tension":70,"visual":90,"data_ready":90,"originality":80},
"vs":0,"tags":"high income population share 30 to 17 percent 1960 2024 rich world shrinking low income grew 5x",
"notes":"High income: 0.91B of 3B (1960) -> 1.42B of 8.1B (2024). Low income: 0.11B -> 0.62B (5.4x).","topics":["economy","population","international","inequality","poverty"],"status":"idea"
},

{
"id":"low_income_water_gap",
"title":"Low-income countries improved water access from 42% to 62% since 2000 — but grew by 300 million people",
"sub":"They got better infrastructure while getting bigger faster. The raw number of people without clean water barely moved.",
"type":"CHART","geo":"worldwide","fmt":"Dual axis line chart",
"tbl":"World Bank + WHO/UNICEF JMP via OWID: Water access % + total population for low-income countries 2000-2024",
"section":"International Statistics",
"ext":["World Bank Open Data: GDP, population, income by country (data.worldbank.org  free API)"],
"vars":["water_access_pct_low_income","population_low_income_countries"],
"join":["gdp_per_capita_low_income","youth_dependency_ratio"],
"sc":{"emotional":100,"relatability":60,"clarity":80,"surprise":90,"tension":100,"visual":90,"data_ready":90,"originality":100},
"vs":0,"tags":"low income countries water access improved 42 to 62 percent but grew 300 million people raw numbers stuck",
"notes":"42% of 0.32B (2000) = 186M without water. 62% of 0.62B (2024) = 236M without water. Progress ate itself.","topics":["poverty","environment","population","inequality","international"],"status":"idea"
},

{
"id":"sub_saharan_water_linear_progress",
"title":"Sub-Saharan Africa improved water access by 23 points in 24 years — one of the greatest infrastructure achievements in history",
"sub":"45% in 2000. 68% in 2024. A 23-point gain for a region that added 500 million people in the same period.",
"type":"CHART","geo":"worldwide","fmt":"Area chart",
"tbl":"WHO/UNICEF JMP (2025) via OWID: Water access Sub-Saharan Africa 2000-2024 (ourworldindata.org/water-access)",
"section":"International Statistics",
"ext":["World Bank Open Data: GDP, population, income by country (data.worldbank.org  free API)"],
"vars":["water_access_pct_sub_saharan_africa","population_sub_saharan_africa"],
"join":["gdp_per_capita","political_regime"],
"sc":{"emotional":80,"relatability":60,"clarity":90,"surprise":90,"tension":70,"visual":90,"data_ready":100,"originality":80},
"vs":0,"tags":"Sub-Saharan Africa water access 45 to 68 percent 23 points 24 years 500 million people infrastructure achievement",
"notes":"","topics":["environment","international","poverty","population","infrastructure"],"status":"idea"
},

{
"id":"xref_pct_elderly_gdp_by_country",
"title":"% population over 65 vs. GDP per capita: the prosperity-aging lock-in",
"sub":"Japan 29.5% elderly, $34K GDP per capita. Niger 3% elderly, $600 GDP. The two variables are almost perfectly correlated across 180 countries.",
"type":"XREF","geo":"worldwide","fmt":"Scatter plot",
"tbl":"UN WPP (2024) via OWID: % over 65 by country + World Bank: GDP per capita",
"section":"International Statistics",
"ext":["World Bank Open Data: GDP, population, income by country (data.worldbank.org  free API)"],
"vars":["pct_population_over65","gdp_per_capita"],
"join":["water_access_pct","political_regime","natural_growth_rate","median_age"],
"sc":{"emotional":70,"relatability":60,"clarity":80,"surprise":80,"tension":60,"visual":90,"data_ready":100,"originality":80},
"vs":0,"tags":"percent elderly GDP per capita correlation prosperity aging 180 countries Japan Niger perfectly correlated",
"notes":"","topics":["economy","population","international","history"],"status":"idea"
},

{
"id":"xref_youth_bulge_water_income",
"title":"Countries where babies outnumber young adults also have the worst water and lowest incomes — every single time",
"sub":"Every country where the 0-4 cohort is 2x the 20-24 cohort has water access below 70% and GDP per capita below $2,000. Not one exception.",
"type":"XREF","geo":"worldwide","fmt":"Scatter plot",
"tbl":"UN WPP (2024) + WHO/UNICEF JMP + World Bank via OWID: Youth bulge, water access, GDP by country 2023",
"section":"International Statistics",
"ext":["World Bank Open Data: GDP, population, income by country (data.worldbank.org  free API)"],
"vars":["ratio_under5_to_20_24","water_access_pct","gdp_per_capita"],
"join":["political_regime","natural_growth_rate","old_age_dependency_ratio"],
"sc":{"emotional":90,"relatability":60,"clarity":70,"surprise":100,"tension":90,"visual":90,"data_ready":90,"originality":100},
"vs":0,"tags":"youth bulge water access income GDP zero exceptions DRC Chad Somalia all cluster same corner triple XREF",
"notes":"Zero exceptions: all 2x+ ratio countries below 70% water AND below $2K GDP. Perfect clustering.","topics":["population","poverty","environment","international","inequality"],"status":"idea"
},

{
"id":"xref_over65_water_access",
"title":"Countries with the most elderly also have the cleanest water — and vice versa",
"sub":"Nations where 20%+ of people are over 65 average 99% water access. Nations where under 5% are elderly average 74%. The same variable predicts both.",
"type":"XREF","geo":"worldwide","fmt":"Scatter plot",
"tbl":"UN WPP (2024) + WHO/UNICEF JMP via OWID: % over 65 + water access by country 2023",
"section":"International Statistics",
"ext":["World Bank Open Data: GDP, population, income by country (data.worldbank.org  free API)"],
"vars":["pct_population_over65","water_access_pct"],
"join":["gdp_per_capita","political_regime","median_age","natural_growth_rate"],
"sc":{"emotional":80,"relatability":60,"clarity":80,"surprise":90,"tension":80,"visual":90,"data_ready":100,"originality":90},
"vs":0,"tags":"elderly percentage water access correlation 20 percent 65 plus 99 water 5 percent 65 plus 74 water XREF",
"notes":"","topics":["population","environment","international","health","inequality"],"status":"idea"
},

{
"id":"south_korea_age_collapse_timeline",
"title":"South Korea's age pyramid 1950-2100: from classic triangle to upside-down diamond",
"sub":"1950: wide base, few elderly. 2023: balanced middle bulge. 2100: narrow base, crushing elderly top. The fastest inversion in recorded history.",
"type":"CHART","geo":"worldwide","fmt":"Bar chart",
"tbl":"UN WPP (2024) via OWID: South Korea population by age group 1950-2100 projection (ourworldindata.org/age-structure)",
"section":"International Statistics",
"ext":["World Bank Open Data: GDP, population, income by country (data.worldbank.org  free API)"],
"vars":["population_by_age_group_south_korea_1950","population_by_age_group_south_korea_2023","population_by_age_group_south_korea_2075"],
"join":["fertility_rate_south_korea","gdp_per_capita","net_migration_rate"],
"sc":{"emotional":90,"relatability":70,"clarity":90,"surprise":100,"tension":90,"visual":100,"data_ready":90,"originality":90},
"vs":0,"tags":"South Korea age pyramid 1950 2100 triangle to diamond fastest inversion history fertility 0.72",
"notes":"Under-15 was 41% in 1950. Will be around 8% by 2100. Over-65 going from 3% to 40%+.","topics":["population","international","economy","history"],"status":"idea"
},

{
"id":"baby_boom_echo_visible",
"title":"You can see the baby boom in the US age pyramid — and its echo, and its echo's echo",
"sub":"The 55-64 cohort is the largest in America. 30-34 is next. The boom of 1946-1964 still ripples through every generation that followed.",
"type":"CHART","geo":"us_national","fmt":"Bar chart",
"tbl":"UN WPP (2024) via OWID: US population by 5-year age group 2023 (ourworldindata.org/age-structure)",
"section":"Population",
"ext":["Census Bureau: US population estimates by age (census.gov  free)"],
"vars":["population_by_age_group_us_2023"],
"join":["birth_rate_national","median_age","old_age_dependency_ratio"],
"sc":{"emotional":70,"relatability":90,"clarity":90,"surprise":70,"tension":50,"visual":100,"data_ready":100,"originality":80},
"vs":0,"tags":"baby boom echo visible US age pyramid 55-64 largest cohort 30-34 echo 1946 1964 generational ripple",
"notes":"","topics":["population","history","economy","housing"],"status":"idea"
},

{
"id":"xref_high_income_water_stagnation",
"title":"High-income countries already at 98% water access in 2000 — barely moved in 24 years",
"sub":"High income: 98.2% (2000) to 99.1% (2024). Low income: 41.6% to 61.6%. The gains all happened at the bottom. The top was already saturated.",
"type":"CHART","geo":"worldwide","fmt":"Line chart",
"tbl":"WHO/UNICEF JMP (2025) + World Bank via OWID: Water access by income group 2000-2024",
"section":"International Statistics",
"ext":["World Bank Open Data: GDP, population, income by country (data.worldbank.org  free API)"],
"vars":["water_access_pct_high_income","water_access_pct_low_income","water_access_pct_lower_middle_income"],
"join":["population_by_income_group","gdp_per_capita"],
"sc":{"emotional":80,"relatability":60,"clarity":90,"surprise":80,"tension":70,"visual":80,"data_ready":100,"originality":80},
"vs":0,"tags":"high income water access stagnation 98 to 99 low income 42 to 62 gains happened at bottom saturated top",
"notes":"","topics":["environment","inequality","poverty","international","economy"],"status":"idea"
},

{
"id":"nigeria_age_bomb",
"title":"Nigeria's 0-4 cohort: 33.5 million children — larger than the entire population of Canada",
"sub":"Nigeria has more children under 5 than Canada has people. And its fertility rate is still above 5. The most important demographic story nobody is mapping.",
"type":"MAP","geo":"worldwide","fmt":"World choropleth",
"tbl":"UN WPP (2024) via OWID: Population under 5 by country 2023 (ourworldindata.org/age-structure)",
"section":"International Statistics",
"ext":["World Bank Open Data: GDP, population, income by country (data.worldbank.org  free API)"],
"vars":["population_under5","fertility_rate","population_growth_rate"],
"join":["water_access_pct","gdp_per_capita","political_regime"],
"sc":{"emotional":90,"relatability":70,"clarity":90,"surprise":100,"tension":90,"visual":100,"data_ready":100,"originality":90},
"vs":0,"tags":"Nigeria 33.5 million under-5 larger than Canada entire population fertility 5 demographic bomb unmapped",
"notes":"Nigeria 0-4: 33.5M. Canada total: 38M. Ethiopia 0-4: 19.1M, Pakistan: 31.8M. Stunning scale comparison.","topics":["population","international","poverty","economy","inequality"],"status":"idea"
},

{
"id":"world_over65_growth_arc",
"title":"The world's elderly population: 128M in 1950, 808M today, 2.4 billion by 2100",
"sub":"It took all of human history to produce 128 million elderly people. We will add that many every 15 years by 2100.",
"type":"CHART","geo":"worldwide","fmt":"Area chart",
"tbl":"UN WPP (2024) via OWID: World population ages 65+ with projections 1950-2100 (ourworldindata.org/age-structure)",
"section":"International Statistics",
"ext":["World Bank Open Data: GDP, population, income by country (data.worldbank.org  free API)"],
"vars":["world_population_over65","world_population_over65_projection"],
"join":["world_old_age_dependency_ratio","world_pension_spending"],
"sc":{"emotional":90,"relatability":70,"clarity":90,"surprise":90,"tension":80,"visual":90,"data_ready":90,"originality":80},
"vs":0,"tags":"world elderly 128M 1950 808M 2023 2.4 billion 2100 all human history 15 years add same every century",
"notes":"","topics":["population","international","economy","health","history"],"status":"idea"
},

{
"id":"xref_growth_rate_divergence_income",
"title":"Development level and population growth: the gap that has widened every decade since 1960",
"sub":"1960: developed world grew at 1.16%, least developed at 2.36% — a 1.2pp gap. 2023: developed 0.14%, least developed 2.31% — a 2.17pp gap. The divergence doubled.",
"type":"CHART","geo":"worldwide","fmt":"Line chart",
"tbl":"UN WPP (2024) via OWID: Population growth rate by development level 1950-2023 (ourworldindata.org/population-growth)",
"section":"International Statistics",
"ext":["World Bank Open Data: GDP, population, income by country (data.worldbank.org  free API)"],
"vars":["growth_rate_more_developed","growth_rate_least_developed","growth_rate_low_income"],
"join":["water_access_pct","gdp_per_capita","old_age_dependency_ratio"],
"sc":{"emotional":90,"relatability":60,"clarity":90,"surprise":90,"tension":90,"visual":90,"data_ready":90,"originality":90},
"vs":0,"tags":"development level population growth rate divergence 1960 2023 gap doubled developed zero least developed unchanged",
"notes":"","topics":["population","international","inequality","poverty","economy","history"],"status":"idea"
},

{
"id":"drc_age_pyramid_explosion",
"title":"DRC's age pyramid: 19.3 million children under 5, projected to be the world's 3rd most populous country by 2100",
"sub":"The Democratic Republic of Congo had 105 million people in 2023. By 2100: 430 million — a 307% increase. Its 0-4 cohort is already 2.1x its 20-24 cohort.",
"type":"CHART","geo":"worldwide","fmt":"Bar chart",
"tbl":"UN WPP (2024) via OWID: DRC population by age group + projection 2023-2100 (ourworldindata.org/age-structure)",
"section":"International Statistics",
"ext":["World Bank Open Data: GDP, population, income by country (data.worldbank.org  free API)"],
"vars":["population_by_age_group_drc","population_medium_projection_drc"],
"join":["water_access_pct","gdp_per_capita","political_regime"],
"sc":{"emotional":90,"relatability":60,"clarity":90,"surprise":100,"tension":90,"visual":100,"data_ready":90,"originality":90},
"vs":0,"tags":"DRC 19.3 million under-5 430 million 2100 3rd most populous 307 percent growth age pyramid explosion",
"notes":"","topics":["population","international","poverty","environment","inequality"],"status":"idea"
},

{
"id":"xref_under25_share_vs_conflict",
"title":"Countries where over 60% of the population is under 25 are overwhelmingly conflict-prone",
"sub":"The youth bulge and political instability have been documented for decades. The map still holds: where half the country is under 25, coups and civil wars cluster.",
"type":"XREF","geo":"worldwide","fmt":"Bivariate choropleth",
"tbl":"UN WPP (2024) via OWID: Population under-25 share + V-Dem: Political regime type + conflict data (UCDP)",
"section":"International Statistics",
"ext":["World Bank Open Data: GDP, population, income by country (data.worldbank.org  free API)"],
"vars":["pct_under25","political_regime","regime_change_direction"],
"join":["water_access_pct","gdp_per_capita","natural_growth_rate"],
"sc":{"emotional":90,"relatability":60,"clarity":70,"surprise":80,"tension":90,"visual":100,"data_ready":80,"originality":90},
"vs":0,"tags":"under-25 population share 60 percent conflict coups civil war youth bulge political instability map clusters",
"notes":"","topics":["population","democracy","war","international","politics"],"status":"idea"
},

{
"id":"world_children_peak",
"title":"The number of children under 15 in the world already peaked and is declining",
"sub":"World under-15 population: 2.025 billion in 2023, falling to 1.681 billion by 2100. Humanity is not just aging — it is having its last great generation of children.",
"type":"CHART","geo":"worldwide","fmt":"Line chart",
"tbl":"UN WPP (2024) via OWID: World population under 15 with projections 1950-2100 (ourworldindata.org/age-structure)",
"section":"International Statistics",
"ext":["World Bank Open Data: GDP, population, income by country (data.worldbank.org  free API)"],
"vars":["world_population_under15","world_population_under15_projection"],
"join":["world_fertility_rate","world_population_total"],
"sc":{"emotional":90,"relatability":70,"clarity":90,"surprise":90,"tension":80,"visual":90,"data_ready":90,"originality":80},
"vs":0,"tags":"world children under 15 peaked declining 2.025 billion 1.681 billion 2100 last great generation aging",
"notes":"Peaked around 2017 at ~2.05B. Now declining. Except Africa: 584M->789M. Asia: 1098M->655M.","topics":["population","international","history","economy"],"status":"idea"
},

]

def vscore(sc):
    return int((sc.get('emotional',0)*2 + sc.get('relatability',0)*2 + sc.get('clarity',0)*2 +
               sc.get('surprise',0)*1.5 + sc.get('tension',0)*1 + sc.get('visual',0)*1 +
               sc.get('data_ready',0)*0.5 + sc.get('originality',0)*0.5) / 10.5)

for idea in ideas:
    idea['vs'] = vscore(idea['sc'])

if __name__ == '__main__':
    print(f"BATCH_BA: {len(ideas)} ideas")
    for i in sorted(ideas, key=lambda x: -x['vs']):
        print(f"  vs={i['vs']:3d}  {i['id']}")
