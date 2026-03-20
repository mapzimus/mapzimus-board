# BATCH_BE.py — Bivariate maps: branching existing single-variable maps into 2-variable stories

ideas = [

{
"id":"bivariate_gop_transfers",
"title":"Red states, federal money: vote margin vs. federal transfers per capita — the bivariate edition",
"sub":"The darker the red, the more federal money received. The correlation is not a coincidence — it is the map.",
"type":"XREF","geo":"us_state","fmt":"Bivariate choropleth",
"tbl":"BEA: Government transfer payments per capita + MIT Election Lab: 2024 presidential results",
"section":"Social Insurance  -  Elections",
"ext":["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API  free, tidycensus)","MIT Election Lab: presidential/congressional results (electionlab.mit.edu  free)"],
"vars":["total_transfers_per_capita","rep_pct"],
"join":["median_household_income","pct_on_snap","violent_crime_rate"],
"sc":{"emotional":90,"relatability":80,"clarity":80,"surprise":90,"tension":100,"visual":100,"data_ready":100,"originality":80},
"vs":0,"tags":"bivariate red states federal money transfers GOP vote margin per capita darker red more money",
"notes":"Extends gop_transfers idea into proper bivariate format. Most iconic map on the board.","topics":["politics","economy","inequality","elections","social insurance"],"status":"idea"
},

{
"id":"bivariate_crime_poverty_county",
"title":"Violent crime rate vs. poverty rate — bivariate county choropleth",
"sub":"The tightest correlation in American social data, rendered at county level in two-variable color space.",
"type":"XREF","geo":"us_county","fmt":"Bivariate choropleth",
"tbl":"FBI UCR/NIBRS: Violent crime by county + ACS: Poverty rate by county",
"section":"Law Enforcement  -  Income",
"ext":["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API  free, tidycensus)","FBI Crime Data Explorer: UCR/NIBRS by state/agency (cde.ucr.cjis.gov  free)"],
"vars":["violent_crime_rate","poverty_rate_county"],
"join":["median_household_income","rep_pct_county","pct_on_snap","incarceration_rate"],
"sc":{"emotional":90,"relatability":80,"clarity":70,"surprise":70,"tension":90,"visual":100,"data_ready":80,"originality":70},
"vs":0,"tags":"violent crime poverty county bivariate tightest correlation American social data two-variable color space",
"notes":"Extends crime_poverty to county level bivariate. Much more granular story.","topics":["crime","poverty","inequality","race","politics"],"status":"idea"
},

{
"id":"bivariate_renewable_politics",
"title":"Renewable energy share vs. 2024 presidential vote — the green-red paradox bivariate",
"sub":"Iowa is deep red and near 30% wind. Wyoming is deepest red and 97% fossil. The relationship between politics and clean energy is messier than it looks.",
"type":"XREF","geo":"us_state","fmt":"Bivariate choropleth",
"tbl":"EIA SEDS: Renewable energy share by state + MIT Election Lab: 2024 results",
"section":"Energy  -  Elections",
"ext":["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API  free, tidycensus)","MIT Election Lab: presidential/congressional results (electionlab.mit.edu  free)","EIA State Energy Data System: production + consumption by state (eia.gov  free API)"],
"vars":["renewable_energy_share","rep_pct"],
"join":["energy_consumption_per_capita","coal_production_index","median_household_income"],
"sc":{"emotional":70,"relatability":70,"clarity":70,"surprise":90,"tension":70,"visual":100,"data_ready":90,"originality":80},
"vs":0,"tags":"renewable energy politics bivariate Iowa red 30 percent wind Wyoming fossil green-red paradox",
"notes":"Iowa anomaly breaks the simple narrative. Wind is rural economic development, not ideology.","topics":["energy","politics","climate","elections","geography"],"status":"idea"
},

{
"id":"bivariate_teacher_salary_outcomes",
"title":"Teacher salary vs. student outcomes — bivariate state map",
"sub":"California pays teachers $101K and ranks 36th in outcomes. Mississippi pays $54K and ranks 50th. The relationship between teacher pay and performance is real but not linear.",
"type":"XREF","geo":"us_state","fmt":"Bivariate choropleth",
"tbl":"NCES: Average teacher salary by state + NAEP: 4th and 8th grade reading/math scores by state",
"section":"Education",
"ext":["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API  free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov  free)"],
"vars":["avg_teacher_salary","naep_composite_score"],
"join":["expenditure_per_pupil","median_household_income","pct_bachelors","rep_pct"],
"sc":{"emotional":80,"relatability":80,"clarity":70,"surprise":80,"tension":70,"visual":100,"data_ready":90,"originality":80},
"vs":0,"tags":"teacher salary outcomes bivariate California 101K 36th Mississippi 54K 50th not linear relationship",
"notes":"","topics":["education","labor","inequality","politics","economy"],"status":"idea"
},

{
"id":"bivariate_teen_birth_poverty",
"title":"Teen birth rate vs. poverty rate — bivariate state choropleth, the tightest two-variable story in public health",
"sub":"The two variables are so correlated that one almost predicts the other exactly. Except Utah, which defies both.",
"type":"XREF","geo":"us_state","fmt":"Bivariate choropleth",
"tbl":"CDC NCHS: Teen birth rates by state + ACS: Poverty rate by state",
"section":"Births Deaths  -  Income",
"ext":["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API  free, tidycensus)"],
"vars":["teen_birth_rate","poverty_rate_state"],
"join":["rep_pct","pct_bachelors","pct_births_unmarried","median_household_income"],
"sc":{"emotional":80,"relatability":70,"clarity":70,"surprise":70,"tension":80,"visual":100,"data_ready":100,"originality":70},
"vs":0,"tags":"teen birth rate poverty bivariate tightest two-variable public health except Utah defies both",
"notes":"","topics":["health","poverty","gender","education","inequality","race"],"status":"idea"
},

{
"id":"bivariate_water_regime_world",
"title":"Water access vs. regime type — the flagship bivariate world map",
"sub":"Map each country in a 2x2 color grid: clean/dirty water crossed with democratic/autocratic. Four quadrants reveal the geography of governance and infrastructure.",
"type":"XREF","geo":"worldwide","fmt":"Bivariate choropleth",
"tbl":"WHO/UNICEF JMP (2025) + V-Dem via OWID: Water access + regime type by country 2023",
"section":"International Statistics",
"ext":["World Bank Open Data: GDP, population, income by country (data.worldbank.org  free API)"],
"vars":["water_access_pct","political_regime"],
"join":["gdp_per_capita","child_mortality_rate","natural_growth_rate"],
"sc":{"emotional":90,"relatability":70,"clarity":80,"surprise":90,"tension":90,"visual":100,"data_ready":90,"originality":100},
"vs":0,"tags":"water access regime type bivariate world map 2x2 color quadrants governance infrastructure flagship",
"notes":"Best bivariate world map in the dataset. Clean democracy vs dirty autocracy in one look.","topics":["democracy","environment","international","inequality","infrastructure"],"status":"idea"
},

{
"id":"bivariate_farm_size_income",
"title":"Farm consolidation vs. median income — bivariate county map of rural America",
"sub":"Where large farms dominate, incomes stay low. Where small farms survive, communities survive. The two-color map of rural economic health.",
"type":"XREF","geo":"us_county","fmt":"Bivariate choropleth",
"tbl":"USDA NASS Census of Agriculture: % acres in large farms by county + ACS: Median income by county",
"section":"Agriculture  -  Income",
"ext":["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API  free, tidycensus)","Census Population Estimates: annual population by state/county (census.gov  free)"],
"vars":["pct_acres_large_farms","median_household_income"],
"join":["pct_on_snap","rural_population_pct","rep_pct_county"],
"sc":{"emotional":80,"relatability":70,"clarity":70,"surprise":80,"tension":80,"visual":100,"data_ready":70,"originality":80},
"vs":0,"tags":"farm consolidation median income bivariate county rural economic health large farms dominate income stays low",
"notes":"","topics":["agriculture","inequality","poverty","labor","economy"],"status":"idea"
},

{
"id":"bivariate_bridge_condition_transfers",
"title":"Bridge condition vs. federal transfers received — bivariate state map of the infrastructure paradox",
"sub":"The worst bridges get the most federal money. The two-color map makes the irony visceral.",
"type":"XREF","geo":"us_state","fmt":"Bivariate choropleth",
"tbl":"FHWA: % bridges poor condition by state + BEA: Government transfers per capita by state",
"section":"Transportation  -  Social Insurance",
"ext":["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API  free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov  free)"],
"vars":["pct_bridges_poor","total_transfers_per_capita"],
"join":["rep_pct","median_household_income","state_gdp_per_capita"],
"sc":{"emotional":80,"relatability":70,"clarity":70,"surprise":80,"tension":80,"visual":100,"data_ready":90,"originality":80},
"vs":0,"tags":"bridges poor condition federal transfers bivariate paradox worst bridges most money irony visceral",
"notes":"","topics":["infrastructure","politics","transportation","inequality","social insurance"],"status":"idea"
},

{
"id":"bivariate_education_vote_county",
"title":"College attainment vs. 2024 vote margin — bivariate at county level",
"sub":"The education-politics sort is perfect at state level. At county level, the edges get messier and the story gets more honest.",
"type":"XREF","geo":"us_county","fmt":"Bivariate choropleth",
"tbl":"ACS: % with bachelor's degree by county + MIT Election Lab: 2024 presidential results by county",
"section":"Education  -  Elections",
"ext":["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API  free, tidycensus)","MIT Election Lab: presidential/congressional results (electionlab.mit.edu  free)"],
"vars":["pct_bachelors_county","rep_pct_county"],
"join":["median_household_income","violent_crime_rate","population_density_county"],
"sc":{"emotional":80,"relatability":80,"clarity":70,"surprise":70,"tension":90,"visual":100,"data_ready":90,"originality":70},
"vs":0,"tags":"college education vote bivariate county education-politics sort messy at county level honest story",
"notes":"","topics":["education","politics","elections","inequality","race"],"status":"idea"
},

{
"id":"bivariate_opioid_manufacturing_loss",
"title":"Opioid death rate vs. manufacturing job loss — bivariate county map of the American crisis",
"sub":"The counties that lost factories in the 1990s and 2000s are the same counties drowning in overdoses in the 2010s and 2020s. The two-color map writes its own story.",
"type":"XREF","geo":"us_county","fmt":"Bivariate choropleth",
"tbl":"CDC WONDER: Drug overdose mortality by county + BLS QCEW: Manufacturing employment change by county",
"section":"Health  -  Labor Force",
"ext":["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API  free, tidycensus)"],
"vars":["opioid_death_rate_county","manufacturing_job_loss_pct"],
"join":["median_household_income","rep_pct_county","poverty_rate_county","pct_on_snap"],
"sc":{"emotional":100,"relatability":80,"clarity":70,"surprise":80,"tension":100,"visual":100,"data_ready":80,"originality":90},
"vs":0,"tags":"opioid death rate manufacturing job loss bivariate county 1990s 2000s factories 2010s 2020s overdoses",
"notes":"Appalachia/Rust Belt overlap is near-perfect. One of the most powerful bivariate maps possible.","topics":["health","labor","drugs","poverty","history","economy","race"],"status":"idea"
},

{
"id":"bivariate_median_age_growth_rate_world",
"title":"Median age vs. natural growth rate — the global demographic clock in bivariate",
"sub":"Young and growing vs. old and dying. Every country falls into one of four quadrants. The map of the century.",
"type":"XREF","geo":"worldwide","fmt":"Bivariate choropleth",
"tbl":"UN WPP (2024) via OWID: Median age + natural growth rate by country 2023",
"section":"International Statistics",
"ext":["World Bank Open Data: GDP, population, income by country (data.worldbank.org  free API)"],
"vars":["median_age","natural_growth_rate"],
"join":["gdp_per_capita","political_regime","water_access_pct"],
"sc":{"emotional":80,"relatability":60,"clarity":80,"surprise":80,"tension":80,"visual":100,"data_ready":100,"originality":90},
"vs":0,"tags":"median age natural growth rate bivariate world four quadrants young growing old dying demographic clock",
"notes":"","topics":["population","international","history","economy","democracy"],"status":"idea"
},

{
"id":"bivariate_snap_crop_insurance",
"title":"SNAP enrollment vs. crop insurance payouts — bivariate state map of the dual subsidy",
"sub":"The same states subsidize both the farmers and the food-insecure. The two-color map asks: who is the welfare state actually for?",
"type":"XREF","geo":"us_state","fmt":"Bivariate choropleth",
"tbl":"USDA FNS: SNAP enrollment by state + USDA RMA: Crop insurance indemnities by state",
"section":"Agriculture  -  Social Insurance",
"ext":["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API  free, tidycensus)"],
"vars":["pct_on_snap","crop_insurance_indemnities_per_capita"],
"join":["rep_pct","median_household_income","rural_population_pct"],
"sc":{"emotional":90,"relatability":70,"clarity":70,"surprise":90,"tension":90,"visual":100,"data_ready":80,"originality":90},
"vs":0,"tags":"SNAP crop insurance bivariate dual subsidy welfare state for whom farmers food-insecure same states",
"notes":"","topics":["agriculture","poverty","politics","social insurance","food","inequality"],"status":"idea"
},

{
"id":"bivariate_water_youth_dep_world",
"title":"Youth dependency vs. water access — bivariate map of where children are most and least served",
"sub":"Where the most children live, the worst water is. The two-color map of the world's most solvable injustice.",
"type":"XREF","geo":"worldwide","fmt":"Bivariate choropleth",
"tbl":"UN WPP (2024) + WHO/UNICEF JMP (2025) via OWID: Youth dependency + water access 2023",
"section":"International Statistics",
"ext":["World Bank Open Data: GDP, population, income by country (data.worldbank.org  free API)"],
"vars":["youth_dependency_ratio","water_access_pct"],
"join":["gdp_per_capita","political_regime","natural_growth_rate"],
"sc":{"emotional":90,"relatability":60,"clarity":70,"surprise":80,"tension":90,"visual":100,"data_ready":90,"originality":90},
"vs":0,"tags":"youth dependency water access bivariate most children worst water solvable injustice two-color world map",
"notes":"","topics":["population","environment","poverty","international","inequality"],"status":"idea"
},

{
"id":"bivariate_home_price_commute",
"title":"Home price vs. commute time — bivariate metro map of the affordability-convenience tradeoff",
"sub":"High price + short commute (San Francisco). Low price + long commute (Riverside). The two-color map of where Americans actually want to live vs. where they can afford to.",
"type":"XREF","geo":"us_metro","fmt":"Bivariate choropleth",
"tbl":"FHFA: Home price index by metro + ACS: Mean commute time by metro",
"section":"Housing  -  Transportation",
"ext":["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API  free, tidycensus)","BEA Regional: GDP + personal income per capita by metro (apps.bea.gov  free)"],
"vars":["home_price_index_metro","avg_commute_time_metro"],
"join":["median_household_income","population_growth_metro","transit_ridership"],
"sc":{"emotional":80,"relatability":90,"clarity":80,"surprise":70,"tension":70,"visual":100,"data_ready":80,"originality":80},
"vs":0,"tags":"home price commute time bivariate metro affordability convenience tradeoff San Francisco Riverside want vs afford",
"notes":"","topics":["housing","transportation","economy","labor","inequality"],"status":"idea"
},

{
"id":"bivariate_uninsured_rural",
"title":"Uninsured rate vs. rural population share — bivariate state map of healthcare access",
"sub":"The most rural states have the fewest insured. The states that refused Medicaid expansion are exactly those. Two colors, one policy failure.",
"type":"XREF","geo":"us_state","fmt":"Bivariate choropleth",
"tbl":"Census SAHIE: Uninsured rate by state + Census: Rural population share by state",
"section":"Health  -  Population",
"ext":["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API  free, tidycensus)"],
"vars":["uninsured_rate","rural_population_pct"],
"join":["rep_pct","medicaid_expansion_status","median_household_income"],
"sc":{"emotional":90,"relatability":80,"clarity":80,"surprise":70,"tension":90,"visual":100,"data_ready":90,"originality":70},
"vs":0,"tags":"uninsured rate rural bivariate Medicaid expansion refusal two colors one policy failure state map",
"notes":"","topics":["health","rural","poverty","politics","inequality"],"status":"idea"
},

{
"id":"bivariate_energy_gdp_state",
"title":"Energy consumption per capita vs. GDP per capita — bivariate state map of the efficiency gap",
"sub":"Louisiana: highest energy use, below-average GDP. California: below-average energy, above-average GDP. The decoupling of prosperity from consumption.",
"type":"XREF","geo":"us_state","fmt":"Bivariate choropleth",
"tbl":"EIA SEDS: Energy per capita by state + BEA: GDP per capita by state",
"section":"Energy  -  Income",
"ext":["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API  free, tidycensus)","EIA State Energy Data System: production + consumption by state (eia.gov  free API)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov  free)"],
"vars":["energy_consumption_per_capita","state_gdp_per_capita"],
"join":["renewable_energy_share","rep_pct","industrial_employment_pct"],
"sc":{"emotional":70,"relatability":70,"clarity":80,"surprise":80,"tension":60,"visual":100,"data_ready":100,"originality":80},
"vs":0,"tags":"energy consumption GDP per capita bivariate efficiency gap Louisiana California prosperity decoupling consumption",
"notes":"","topics":["energy","economy","climate","environment","inequality"],"status":"idea"
},

]

def vscore(sc):
    return int((sc.get('emotional',0)*2 + sc.get('relatability',0)*2 + sc.get('clarity',0)*2 +
               sc.get('surprise',0)*1.5 + sc.get('tension',0)*1 + sc.get('visual',0)*1 +
               sc.get('data_ready',0)*0.5 + sc.get('originality',0)*0.5) / 10.5)

for idea in ideas:
    idea['vs'] = vscore(idea['sc'])

if __name__ == '__main__':
    print(f"BATCH_BE: {len(ideas)} ideas")
    for i in sorted(ideas, key=lambda x: -x['vs']):
        print(f"  vs={i['vs']:3d}  {i['id']}")
