# BATCH_AU.py — US Agriculture: farm consolidation, GMO adoption, trade, farmland as asset
# 17 ideas | Draws from: StatAb Section 17 Agriculture data

ideas = [

{
"id":"farm_consolidation_land",
"title":"Top 4.4% of US farms control 61% of all farmland",
"sub":"The American family farm is mostly a myth now. Six in ten acres are owned by a tiny fraction of operations.",
"type":"CHART","geo":"us_national","fmt":"Treemap or bar chart",
"tbl":"USDA NASS Census of Agriculture: Farm size distribution and acreage by sales class (nass.usda.gov)",
"section":"Agriculture",
"ext":["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API  free, tidycensus)"],
"vars":["farm_count_by_size","farmland_acres_by_size","pct_farms_large","pct_acres_large"],
"join":["farm_income_by_size","net_farm_income"],
"sc":{"emotional":9,"relatability":8,"clarity":8,"surprise":9,"tension":9,"visual":9,"data_ready":9,"originality":8},
"vs":0,"tags":"farm consolidation agriculture inequality land ownership corporate farming family farm USDA concentration",
"notes":"","topics":[],"status":"idea"
},

{
"id":"farmland_value_asset",
"title":"US farmland value: from $946B to $3.49T since 2000",
"sub":"Farmland tripled in value in 25 years. It is no longer just food production — it is a financial asset class.",
"type":"CHART","geo":"us_national","fmt":"Area chart",
"tbl":"USDA ERS + NASS: Farm real estate and farmland value by state (ers.usda.gov / nass.usda.gov)",
"section":"Agriculture",
"ext":["FRED: any national economic time series (fred.stlouisfed.org  free API)"],
"vars":["total_farmland_value","farmland_value_per_acre"],
"join":["farm_count","total_cropland_acres","net_farm_income"],
"sc":{"emotional":8,"relatability":7,"clarity":8,"surprise":9,"tension":8,"visual":8,"data_ready":9,"originality":8},
"vs":0,"tags":"farmland value asset class investment hedge fund agriculture real estate 2000 2024 financialization rural",
"notes":"","topics":[],"status":"idea"
},

{
"id":"farmland_value_per_acre_state",
"title":"Average farmland value per acre by state 2023",
"sub":"New Jersey $14,900/acre. Iowa $8,700/acre. Wyoming $800/acre. The farmland price map of America.",
"type":"MAP","geo":"us_state","fmt":"State choropleth",
"tbl":"USDA NASS: Farm real estate value per acre by state (nass.usda.gov)",
"section":"Agriculture",
"ext":["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API  free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov  free)"],
"vars":["farmland_value_per_acre"],
"join":["pct_land_in_farms","net_farm_income_per_farm","median_household_income"],
"sc":{"emotional":7,"relatability":7,"clarity":8,"surprise":8,"tension":6,"visual":9,"data_ready":9,"originality":7},
"vs":0,"tags":"farmland value per acre state map USDA agriculture real estate rural investment New Jersey Iowa Wyoming",
"notes":"","topics":[],"status":"idea"
},

{
"id":"gmo_adoption_arc",
"title":"GMO adoption in US corn, soybeans, and cotton: from 25% to 94% in 25 years",
"sub":"GMO corn: 25% in 1999, 94% in 2023. The silent transformation of American agriculture.",
"type":"CHART","geo":"us_national","fmt":"Line chart",
"tbl":"USDA ERS: Adoption of genetically engineered crops in the US by type (ers.usda.gov/data-products/adoption-of-genetically-engineered-crops-in-the-us)",
"section":"Agriculture",
"ext":[],
"vars":["gmo_corn_pct","gmo_soybean_pct","gmo_cotton_pct"],
"join":["herbicide_resistant_pct","insect_resistant_pct"],
"sc":{"emotional":8,"relatability":7,"clarity":8,"surprise":8,"tension":7,"visual":8,"data_ready":9,"originality":7},
"vs":0,"tags":"GMO genetically modified corn soybeans cotton adoption percentage USDA agriculture 1999 2023 transformation",
"notes":"","topics":[],"status":"idea"
},

{
"id":"nonfamily_corporate_farms",
"title":"Non-family corporate farms tripled from 7,000 to 19,000 between 2002 and 2022",
"sub":"The corporate takeover of the American farm is in the data. Three times as many in 20 years.",
"type":"CHART","geo":"us_national","fmt":"Bar or line chart",
"tbl":"USDA NASS Census of Agriculture: Farm operator type and tenure (nass.usda.gov)",
"section":"Agriculture",
"ext":["FRED: any national economic time series (fred.stlouisfed.org  free API)"],
"vars":["nonfamily_corporate_farm_count","family_farm_count","total_farm_count"],
"join":["farmland_acres_by_operator_type","farm_income_by_type"],
"sc":{"emotional":9,"relatability":7,"clarity":8,"surprise":9,"tension":9,"visual":8,"data_ready":9,"originality":8},
"vs":0,"tags":"corporate farms family farm consolidation USDA agriculture nonfamily operators 2002 2022 rural inequality",
"notes":"","topics":[],"status":"idea"
},

{
"id":"us_ag_trade_deficit",
"title":"The US went from a $33B agricultural trade surplus to a $37B deficit",
"sub":"America was the world's farm. Now it imports more food than it exports. The flip happened around 2019.",
"type":"CHART","geo":"us_national","fmt":"Area chart",
"tbl":"USDA ERS: US agricultural trade balance by year (ers.usda.gov/topics/international-markets-us-trade/us-agricultural-trade)",
"section":"Agriculture",
"ext":["FRED: any national economic time series (fred.stlouisfed.org  free API)"],
"vars":["ag_exports_total","ag_imports_total","ag_trade_balance"],
"join":["trade_balance_goods","current_account_balance"],
"sc":{"emotional":9,"relatability":7,"clarity":8,"surprise":10,"tension":9,"visual":8,"data_ready":9,"originality":9},
"vs":0,"tags":"agriculture trade deficit surplus food imports exports USDA flip reversal 2019 2024 America farm",
"notes":"","topics":[],"status":"idea"
},

{
"id":"farmer_aging_crisis",
"title":"The average US farmer is now 58.1 years old — up from 50.5 in 1982",
"sub":"Nobody is taking over the farm. In 40 years, the average farmer aged faster than the population.",
"type":"CHART","geo":"us_national","fmt":"Line chart",
"tbl":"USDA NASS Census of Agriculture: Average age of principal farm operator by census year (nass.usda.gov)",
"section":"Agriculture",
"ext":[],
"vars":["avg_age_principal_operator"],
"join":["farm_count","young_farmer_count","farm_income_by_age"],
"sc":{"emotional":8,"relatability":7,"clarity":8,"surprise":8,"tension":8,"visual":8,"data_ready":9,"originality":8},
"vs":0,"tags":"farmer aging average age succession crisis rural agriculture USDA 1982 2022 young farmers",
"notes":"","topics":[],"status":"idea"
},

{
"id":"organic_farm_growth",
"title":"Certified organic farms and sales in the US 2000-2022",
"sub":"Organic sales surged from under $5B to over $60B. But still only 1.3% of all US farms are certified organic.",
"type":"CHART","geo":"us_national","fmt":"Dual axis line chart",
"tbl":"USDA ERS + NASS: Certified organic farm operations and sales (ers.usda.gov/topics/natural-resources-environment/organic-agriculture)",
"section":"Agriculture",
"ext":[],
"vars":["certified_organic_farms","organic_sales_total"],
"join":["total_farm_count","total_farm_sales"],
"sc":{"emotional":7,"relatability":8,"clarity":7,"surprise":7,"tension":5,"visual":8,"data_ready":9,"originality":6},
"vs":0,"tags":"organic farming growth sales certified USDA agriculture food consumer demand premium market",
"notes":"","topics":[],"status":"idea"
},

{
"id":"egg_cash_receipts_avian_flu",
"title":"Egg cash receipts tripled due to avian flu: from $8B to $24B in two years",
"sub":"The most dramatic single-commodity price shock in recent US agricultural history — mapped to the outbreak.",
"type":"CHART","geo":"us_national","fmt":"Line chart",
"tbl":"USDA ERS + NASS: Livestock and poultry cash receipts by commodity (ers.usda.gov/topics/farm-economy/farm-sector-income-finances)",
"section":"Agriculture",
"ext":["BLS CPI: Consumer Price Index by expenditure category (bls.gov/cpi)"],
"vars":["egg_cash_receipts","poultry_cash_receipts","avian_flu_flocks_affected"],
"join":["eggs_cpi","food_at_home_cpi"],
"sc":{"emotional":8,"relatability":9,"clarity":8,"surprise":9,"tension":7,"visual":8,"data_ready":8,"originality":8},
"vs":0,"tags":"eggs avian flu price cash receipts USDA 2023 2024 poultry inflation grocery cost food supply shock",
"notes":"","topics":[],"status":"idea"
},

{
"id":"xref_farmland_value_politics",
"title":"Farmland value per acre vs. 2024 presidential vote margin by state",
"sub":"The most valuable farmland is in blue-leaning states. The deepest red states have the cheapest land.",
"type":"XREF","geo":"us_state","fmt":"Scatter plot",
"tbl":"USDA NASS: Farm real estate value by state + MIT Election Lab: 2024 presidential results by state",
"section":"Agriculture  -  Elections",
"ext":["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API  free, tidycensus)","MIT Election Lab: presidential/congressional results (electionlab.mit.edu  free)"],
"vars":["farmland_value_per_acre","rep_pct","margin"],
"join":["median_household_income","pct_bachelors","net_farm_income_per_farm"],
"sc":{"emotional":8,"relatability":7,"clarity":6,"surprise":8,"tension":8,"visual":8,"data_ready":8,"originality":8},
"vs":0,"tags":"farmland value politics vote 2024 Trump rural agriculture red state blue state XREF",
"notes":"","topics":[],"status":"idea"
},

{
"id":"xref_farm_consolidation_income",
"title":"Farm consolidation vs. median household income by state",
"sub":"States where large farms dominate have lower median incomes. Consolidation hollows out local economies.",
"type":"XREF","geo":"us_state","fmt":"Scatter plot",
"tbl":"USDA NASS Census of Agriculture: Farm size and land concentration by state + ACS: Household income by state",
"section":"Agriculture  -  Income",
"ext":["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API  free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov  free)"],
"vars":["pct_acres_large_farms","median_household_income"],
"join":["pct_on_snap","rep_pct","rural_population_pct"],
"sc":{"emotional":8,"relatability":7,"clarity":6,"surprise":8,"tension":8,"visual":8,"data_ready":8,"originality":8},
"vs":0,"tags":"farm consolidation income inequality rural economy state XREF agriculture corporate hollow out poverty",
"notes":"","topics":[],"status":"idea"
},

{
"id":"net_farm_income_volatility",
"title":"US net farm income 2000-2024: the boom, bust, and COVID whiplash",
"sub":"$90B in 2013, $56B in 2018, $170B in 2022. Farm income swings more than almost any US sector.",
"type":"CHART","geo":"us_national","fmt":"Area chart",
"tbl":"USDA ERS: Net farm income by year (ers.usda.gov/topics/farm-economy/farm-sector-income-finances)",
"section":"Agriculture",
"ext":["FRED: any national economic time series (fred.stlouisfed.org  free API)"],
"vars":["net_farm_income","gross_farm_income","production_expenses"],
"join":["commodity_prices_index","ag_exports_total"],
"sc":{"emotional":7,"relatability":6,"clarity":7,"surprise":7,"tension":7,"visual":8,"data_ready":9,"originality":6},
"vs":0,"tags":"farm income volatile USDA boom bust COVID 2022 2013 agriculture finance net income rural economy",
"notes":"","topics":[],"status":"idea"
},

{
"id":"crop_insurance_by_state",
"title":"Federal crop insurance payouts by state: who gets bailed out most?",
"sub":"Texas, Iowa, Kansas, Nebraska dominate. The federal farm safety net is deeply geographically concentrated.",
"type":"MAP","geo":"us_state","fmt":"State choropleth",
"tbl":"USDA RMA: Crop insurance participation and indemnity payments by state (rma.usda.gov/data)",
"section":"Agriculture",
"ext":["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API  free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov  free)"],
"vars":["crop_insurance_indemnities","crop_insurance_premiums","net_insurance_benefit"],
"join":["rep_pct","total_transfers_per_capita","net_farm_income"],
"sc":{"emotional":8,"relatability":6,"clarity":7,"surprise":8,"tension":8,"visual":9,"data_ready":8,"originality":7},
"vs":0,"tags":"crop insurance federal subsidy USDA state map Texas Iowa Kansas bailout agriculture political geography",
"notes":"","topics":[],"status":"idea"
},

{
"id":"pesticide_use_by_crop",
"title":"Pesticide and herbicide use on major US crops 2000-2020",
"sub":"Herbicide use on corn tripled since GMO introduction. The chemical consequence of the GMO revolution.",
"type":"CHART","geo":"us_national","fmt":"Line chart",
"tbl":"USDA NASS: Agricultural chemical use by crop and state (nass.usda.gov/Surveys/Guide_to_NASS_Surveys/Chemical_Use)",
"section":"Agriculture",
"ext":[],
"vars":["herbicide_lbs_per_acre_corn","insecticide_lbs_per_acre","fungicide_lbs_per_acre"],
"join":["gmo_corn_pct","gmo_soybean_pct"],
"sc":{"emotional":8,"relatability":7,"clarity":7,"surprise":8,"tension":7,"visual":8,"data_ready":7,"originality":7},
"vs":0,"tags":"pesticide herbicide GMO corn agriculture chemical use USDA environment health Roundup glyphosate",
"notes":"","topics":[],"status":"idea"
},

{
"id":"food_away_from_home_convergence",
"title":"Americans now spend nearly as much eating out as eating at home",
"sub":"Food away from home: $508B. Food at home: $415B. The crossover that defines modern American eating.",
"type":"CHART","geo":"us_national","fmt":"Line chart",
"tbl":"USDA ERS: Food expenditures by type — at home vs. away from home (ers.usda.gov/topics/food-choices-health/food-prices-expenditures)",
"section":"Agriculture",
"ext":["FRED: any national economic time series (fred.stlouisfed.org  free API)","BLS CPI: Consumer Price Index by expenditure category (bls.gov/cpi)"],
"vars":["food_away_from_home_expenditure","food_at_home_expenditure"],
"join":["food_at_home_cpi","food_away_from_home_cpi","restaurant_count"],
"sc":{"emotional":7,"relatability":9,"clarity":9,"surprise":7,"tension":5,"visual":8,"data_ready":9,"originality":6},
"vs":0,"tags":"food away from home eating out restaurants groceries spending convergence USDA Americans dining habits",
"notes":"","topics":[],"status":"idea"
},

{
"id":"xref_farm_consolidation_snap",
"title":"Farm consolidation vs. SNAP enrollment by state",
"sub":"States with the most consolidated farmland have the highest food stamp rates. The irony of industrial agriculture.",
"type":"XREF","geo":"us_state","fmt":"Scatter plot",
"tbl":"USDA NASS Census of Agriculture: Farm size by state + USDA FNS: SNAP enrollment by state",
"section":"Agriculture  -  Social Insurance",
"ext":["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API  free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov  free)"],
"vars":["pct_acres_large_farms","pct_on_snap"],
"join":["median_household_income","rep_pct","rural_population_pct"],
"sc":{"emotional":9,"relatability":7,"clarity":6,"surprise":9,"tension":9,"visual":8,"data_ready":8,"originality":9},
"vs":0,"tags":"farm consolidation SNAP food stamps irony agriculture inequality rural XREF corporate farming poverty",
"notes":"","topics":[],"status":"idea"
},

{
"id":"us_livestock_cash_receipts",
"title":"US livestock cash receipts by commodity 2000-2023",
"sub":"Cattle: $88B. Poultry: $48B. Hogs: $26B. Dairy: $52B. The animal agriculture economy, mapped over time.",
"type":"CHART","geo":"us_national","fmt":"Stacked bar chart",
"tbl":"USDA ERS + NASS: Livestock and poultry cash receipts by commodity (ers.usda.gov)",
"section":"Agriculture",
"ext":[],
"vars":["cattle_cash_receipts","poultry_cash_receipts","dairy_cash_receipts","hog_cash_receipts","egg_cash_receipts"],
"join":["net_farm_income","total_farm_cash_receipts"],
"sc":{"emotional":6,"relatability":7,"clarity":8,"surprise":6,"tension":4,"visual":9,"data_ready":9,"originality":5},
"vs":0,"tags":"livestock cattle poultry dairy hogs eggs cash receipts USDA agriculture industry revenue 2023",
"notes":"","topics":[],"status":"idea"
},

]

def vscore(sc):
    return int(sc['emotional']*2 + sc['relatability']*2 + sc['clarity']*2 +
            sc['surprise']*1.5 + sc['tension']*1 + sc['visual']*1 +
            sc['data_ready']*0.5 + sc['originality']*0.5)

for idea in ideas:
    idea['vs'] = vscore(idea['sc'])
