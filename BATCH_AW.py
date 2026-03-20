# BATCH_AW.py — Service economy, gig work, demographic-infrastructure XREFs
# 16 ideas | Draws from: StatAb Section 27 Services + cross-dataset XREF combos

ideas = [

{
"id":"nail_salon_workforce_demographics",
"title":"40% of US nail salon workers are Asian — the geography of ethnic labor concentration",
"sub":"In California, Vietnamese immigrants built an entire industry. The ethnic specialization map of American services.",
"type":"MAP","geo":"us_state","fmt":"State choropleth",
"tbl":"BLS OES + Census ACS: Manicurist occupation demographics by state (bls.gov/oes + census.gov)",
"section":"Accommodation Food Services Other Services",
"ext":["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API  free, tidycensus)"],
"vars":["pct_asian_manicurists","manicurist_employment_state"],
"join":["pct_foreign_born","median_household_income","pct_bachelors"],
"sc":{"emotional":7,"relatability":8,"clarity":7,"surprise":9,"tension":6,"visual":9,"data_ready":7,"originality":9},
"vs":0,"tags":"nail salon Asian Vietnamese labor immigration ethnic workforce California demographics service industry",
"notes":"","topics":[],"status":"idea"
},

{
"id":"landscaping_hispanic_workforce",
"title":"47% of US landscaping workers are Hispanic — the labor geography of outdoor service work",
"sub":"The industry that keeps American suburbs green runs almost entirely on Hispanic labor.",
"type":"MAP","geo":"us_state","fmt":"State choropleth",
"tbl":"BLS OES + Census ACS: Grounds maintenance worker demographics by state (bls.gov/oes + census.gov)",
"section":"Accommodation Food Services Other Services",
"ext":["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API  free, tidycensus)"],
"vars":["pct_hispanic_grounds_workers","grounds_maintenance_employment_state"],
"join":["pct_foreign_born","median_household_income","rep_pct"],
"sc":{"emotional":7,"relatability":8,"clarity":7,"surprise":8,"tension":7,"visual":9,"data_ready":7,"originality":8},
"vs":0,"tags":"landscaping Hispanic Latino immigration labor workforce outdoor service suburbs grounds maintenance",
"notes":"","topics":[],"status":"idea"
},

{
"id":"restaurant_industry_covid_crash",
"title":"Restaurant industry revenue: $757B crash to $640B in 2020, then recovery to $957B by 2022",
"sub":"The fastest sectoral collapse and recovery in US economic history. COVID rewrote the service economy.",
"type":"CHART","geo":"us_national","fmt":"Area chart",
"tbl":"US Census Bureau + NRA: Food service and drinking place sales (census.gov/retail / restaurant.org)",
"section":"Accommodation Food Services Other Services",
"ext":["FRED: any national economic time series (fred.stlouisfed.org  free API)","BLS national data: employment, wages, CPI (bls.gov  free API)"],
"vars":["restaurant_sales_total","restaurant_employment"],
"join":["food_away_from_home_cpi","food_away_from_home_expenditure"],
"sc":{"emotional":8,"relatability":9,"clarity":9,"surprise":7,"tension":7,"visual":8,"data_ready":9,"originality":6},
"vs":0,"tags":"restaurant industry COVID crash collapse recovery $957B food service 2020 2022 pandemic economy jobs",
"notes":"","topics":[],"status":"idea"
},

{
"id":"gig_economy_nonemployers_growth",
"title":"Gig economy nonemployer firms grew 60% in a decade: the invisible workforce explosion",
"sub":"From 15M to 27M single-person businesses since 2010. America is becoming a nation of self-employed contractors.",
"type":"CHART","geo":"us_national","fmt":"Area chart",
"tbl":"Census Bureau Nonemployer Statistics: Total nonemployer firms by sector (census.gov/programs-surveys/nonemployer-statistics)",
"section":"Accommodation Food Services Other Services",
"ext":["FRED: any national economic time series (fred.stlouisfed.org  free API)"],
"vars":["total_nonemployer_firms","nonemployer_receipts_total"],
"join":["rideshare_nonemployer_count","gig_sector_breakdown"],
"sc":{"emotional":7,"relatability":8,"clarity":8,"surprise":7,"tension":7,"visual":8,"data_ready":8,"originality":7},
"vs":0,"tags":"gig economy nonemployers self-employed contractors growth 2010 2020 freelance workforce 27 million",
"notes":"","topics":[],"status":"idea"
},

{
"id":"xref_service_wages_race",
"title":"Service industry wages vs. racial composition by state",
"sub":"States where service workers are majority non-white pay the lowest wages. The race-wage geography of service work.",
"type":"XREF","geo":"us_state","fmt":"Scatter plot",
"tbl":"BLS OES: Median wages for service occupations by state + ACS: Race demographics in service industries",
"section":"Accommodation Food Services Other Services  -  Income",
"ext":["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API  free, tidycensus)","BLS national data: employment, wages, CPI (bls.gov  free API)"],
"vars":["median_service_wage","pct_nonwhite_service_workers"],
"join":["minimum_wage_state","rep_pct","median_household_income"],
"sc":{"emotional":9,"relatability":7,"clarity":6,"surprise":8,"tension":9,"visual":8,"data_ready":7,"originality":8},
"vs":0,"tags":"service wages race racial composition state XREF inequality labor discrimination minimum wage South",
"notes":"","topics":[],"status":"idea"
},

{
"id":"xref_water_access_child_mortality",
"title":"Drinking water access vs. child mortality rate by country 2023",
"sub":"The tightest correlation in global development data. Every percentage point of water access saves children.",
"type":"XREF","geo":"worldwide","fmt":"Scatter plot",
"tbl":"WHO/UNICEF JMP (2025): Water access by country + World Bank / UNICEF: Under-5 mortality rate by country",
"section":"International Statistics",
"ext":["World Bank Open Data: GDP, population, income by country (data.worldbank.org  free API)"],
"vars":["water_access_pct","under5_mortality_rate"],
"join":["gdp_per_capita","sanitation_access_pct","political_regime"],
"sc":{"emotional":10,"relatability":7,"clarity":8,"surprise":7,"tension":9,"visual":9,"data_ready":9,"originality":8},
"vs":0,"tags":"water access child mortality XREF correlation development health Africa DRC South Sudan infrastructure",
"notes":"","topics":[],"status":"idea"
},

{
"id":"xref_youth_burden_gdp",
"title":"Youth dependency ratio vs. GDP per capita by country 2023",
"sub":"The more children per worker, the poorer the country. The single most powerful demographic-economic correlation.",
"type":"XREF","geo":"worldwide","fmt":"Scatter plot",
"tbl":"UN WPP (2024) via Our World in Data: Age structure by country + World Bank: GDP per capita",
"section":"International Statistics",
"ext":["World Bank Open Data: GDP, population, income by country (data.worldbank.org  free API)"],
"vars":["youth_dependency_ratio","gdp_per_capita"],
"join":["water_access_pct","political_regime","female_education_years"],
"sc":{"emotional":8,"relatability":6,"clarity":7,"surprise":7,"tension":8,"visual":9,"data_ready":9,"originality":7},
"vs":0,"tags":"youth dependency GDP per capita XREF correlation poverty development demographics children workers",
"notes":"","topics":[],"status":"idea"
},

{
"id":"xref_migration_dependency",
"title":"Countries most dependent on immigration to maintain their population 2023",
"sub":"UAE: 76% of population growth is migrants. Canada: 84%. Without immigration, both are shrinking.",
"type":"MAP","geo":"worldwide","fmt":"World choropleth",
"tbl":"UN WPP (2024) via Our World in Data: Population growth rate with and without migration by country",
"section":"International Statistics",
"ext":["World Bank Open Data: GDP, population, income by country (data.worldbank.org  free API)"],
"vars":["migration_contribution_to_growth_pct","natural_growth_rate","total_growth_rate"],
"join":["old_age_dependency_ratio","gdp_per_capita","political_regime"],
"sc":{"emotional":9,"relatability":8,"clarity":8,"surprise":9,"tension":9,"visual":10,"data_ready":8,"originality":9},
"vs":0,"tags":"immigration migration dependency population growth UAE Canada wealthy nations anti-immigration demographics",
"notes":"","topics":[],"status":"idea"
},

{
"id":"xref_pop_collapse_water",
"title":"Countries projecting the most population loss by 2100 — do they also have the worst infrastructure today?",
"sub":"South Korea and Eastern Europe are collapsing in people but have excellent water access. DRC is collapsing in infrastructure but exploding in people. Two totally different crises.",
"type":"XREF","geo":"worldwide","fmt":"Scatter plot",
"tbl":"UN WPP (2024) projections + WHO/UNICEF JMP (2025) via Our World in Data",
"section":"International Statistics",
"ext":["World Bank Open Data: GDP, population, income by country (data.worldbank.org  free API)"],
"vars":["population_pct_change_2023_2100","water_access_pct"],
"join":["gdp_per_capita","political_regime","old_age_dependency_ratio"],
"sc":{"emotional":8,"relatability":6,"clarity":6,"surprise":9,"tension":8,"visual":9,"data_ready":8,"originality":10},
"vs":0,"tags":"population collapse water access XREF infrastructure South Korea DRC Eastern Europe two different crises 2100",
"notes":"","topics":[],"status":"idea"
},

{
"id":"xref_farmconsolidation_rural_depop",
"title":"Farm consolidation vs. rural county population loss since 1950",
"sub":"The counties that consolidated agriculture the most are also the ones that hollowed out the most.",
"type":"XREF","geo":"us_county","fmt":"County scatter or bivariate",
"tbl":"USDA NASS Census of Agriculture: Farm size by county + Census Bureau: County population change 1950-2020",
"section":"Agriculture  -  Population",
"ext":["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API  free, tidycensus)","Census Population Estimates: annual population by state/county (census.gov  free)"],
"vars":["pct_acres_large_farms","population_pct_change_1950_2020"],
"join":["median_household_income","pct_on_snap","rep_pct"],
"sc":{"emotional":8,"relatability":7,"clarity":6,"surprise":8,"tension":8,"visual":8,"data_ready":7,"originality":9},
"vs":0,"tags":"farm consolidation rural depopulation county XREF agriculture hollow out 1950 2020 population loss",
"notes":"","topics":[],"status":"idea"
},

{
"id":"xref_dept_store_collapse_county_income",
"title":"Department store closures vs. county median income change since 2000",
"sub":"The counties that lost their anchor stores lost their middle class too. A chicken-or-egg question for rural America.",
"type":"XREF","geo":"us_county","fmt":"County choropleth",
"tbl":"Census ARTS: Retail store closures by county + ACS: Median income change by county 2000-2023",
"section":"Wholesale and Retail Trade  -  Income",
"ext":["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API  free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov  free)"],
"vars":["dept_store_closures_per_capita","median_income_change_2000_2023"],
"join":["population_pct_change_2000_2023","pct_on_snap","rep_pct"],
"sc":{"emotional":8,"relatability":8,"clarity":6,"surprise":8,"tension":8,"visual":8,"data_ready":6,"originality":9},
"vs":0,"tags":"department store closures county income retail anchor store rural America middle class 2000 2023",
"notes":"","topics":[],"status":"idea"
},

{
"id":"xref_gmo_adoption_farm_size",
"title":"GMO adoption rate vs. average farm size by state",
"sub":"Bigger farms adopted GMOs faster. The technology and the consolidation march together.",
"type":"XREF","geo":"us_state","fmt":"Scatter plot",
"tbl":"USDA ERS: GMO adoption by state + USDA NASS: Average farm size by state",
"section":"Agriculture",
"ext":["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API  free, tidycensus)"],
"vars":["gmo_adoption_rate_state","avg_farm_size_acres"],
"join":["net_farm_income_per_farm","farmland_value_per_acre"],
"sc":{"emotional":7,"relatability":6,"clarity":6,"surprise":7,"tension":6,"visual":7,"data_ready":7,"originality":7},
"vs":0,"tags":"GMO adoption farm size consolidation XREF technology agriculture state correlation USDA",
"notes":"","topics":[],"status":"idea"
},

{
"id":"xref_warehousing_jobs_red_counties",
"title":"Where Amazon warehousing jobs landed — mostly in red counties that voted against unions",
"sub":"The fulfillment center map overlaps almost perfectly with low-union red counties. Amazon chose its geography.",
"type":"XREF","geo":"us_county","fmt":"County choropleth",
"tbl":"BLS QCEW: Warehousing and storage employment by county + MIT Election Lab: 2024 results by county",
"section":"Transportation  -  Elections",
"ext":["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API  free, tidycensus)","MIT Election Lab: presidential/congressional results (electionlab.mit.edu  free)"],
"vars":["warehousing_employment_county","rep_pct_county","union_density_county"],
"join":["median_household_income","pct_on_snap"],
"sc":{"emotional":8,"relatability":8,"clarity":6,"surprise":9,"tension":8,"visual":9,"data_ready":7,"originality":9},
"vs":0,"tags":"Amazon warehouse jobs red counties anti-union geography fulfillment center distribution employment XREF",
"notes":"","topics":[],"status":"idea"
},

{
"id":"xref_pedestrian_deaths_suv_share",
"title":"Pedestrian death rate vs. SUV/truck market share by state",
"sub":"States where trucks dominate the roads have the most pedestrian deaths. The vehicle-to-body size mismatch.",
"type":"XREF","geo":"us_state","fmt":"Scatter plot",
"tbl":"NHTSA FARS: Pedestrian fatality rate by state + BTS: Vehicle registrations by type by state",
"section":"Transportation",
"ext":["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API  free, tidycensus)"],
"vars":["pedestrian_fatality_rate","suv_truck_registration_pct"],
"join":["urban_rural_pct","rep_pct","speed_limit"],
"sc":{"emotional":9,"relatability":8,"clarity":7,"surprise":8,"tension":8,"visual":8,"data_ready":7,"originality":8},
"vs":0,"tags":"pedestrian deaths SUV truck market share state XREF safety street design vehicle size mismatch",
"notes":"","topics":[],"status":"idea"
},

{
"id":"xref_ag_trade_deficit_county_farm",
"title":"US agricultural trade deficit vs. net farm income by state — who is losing and who is still winning?",
"sub":"Iowa farms are still profitable. But national ag trade went negative. The disconnect between farm income and trade balance.",
"type":"XREF","geo":"us_state","fmt":"Bivariate choropleth",
"tbl":"USDA ERS: State-level ag trade and farm income (ers.usda.gov)",
"section":"Agriculture  -  Foreign Commerce",
"ext":["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API  free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov  free)"],
"vars":["state_ag_exports","state_ag_imports","net_farm_income_state"],
"join":["farmland_value_per_acre","rep_pct"],
"sc":{"emotional":7,"relatability":6,"clarity":6,"surprise":8,"tension":7,"visual":8,"data_ready":7,"originality":8},
"vs":0,"tags":"agricultural trade deficit farm income state XREF Iowa profitable national negative disconnect exports",
"notes":"","topics":[],"status":"idea"
},

{
"id":"xref_ecommerce_county_retail_jobs",
"title":"Growth in ecommerce vs. loss of retail jobs by county 2010-2023",
"sub":"For every dollar that moved online, retail floor jobs disappeared. The geography of the trade-off.",
"type":"XREF","geo":"us_county","fmt":"County choropleth",
"tbl":"Census ARTS + BLS QCEW: Ecommerce growth by region + retail employment by county",
"section":"Wholesale and Retail Trade  -  Labor Force",
"ext":["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API  free, tidycensus)","BLS LAUS: unemployment + labor force by county (bls.gov  free)"],
"vars":["ecommerce_share_growth","retail_employment_change_pct"],
"join":["median_household_income","warehousing_employment_county","rep_pct"],
"sc":{"emotional":8,"relatability":8,"clarity":6,"surprise":7,"tension":7,"visual":8,"data_ready":6,"originality":8},
"vs":0,"tags":"ecommerce retail jobs county XREF trade-off Amazon online shopping offline employment loss geography",
"notes":"","topics":[],"status":"idea"
},

]

def vscore(sc):
    return int(sc['emotional']*2 + sc['relatability']*2 + sc['clarity']*2 +
            sc['surprise']*1.5 + sc['tension']*1 + sc['visual']*1 +
            sc['data_ready']*0.5 + sc['originality']*0.5)

for idea in ideas:
    idea['vs'] = vscore(idea['sc'])
