# BATCH_AV.py — US Retail & Transportation: retail collapse, driving costs, infrastructure
# 17 ideas | Draws from: StatAb Section 22 Retail/Wholesale + Section 23 Transportation

ideas = [

{
"id":"department_store_collapse",
"title":"Department store retail sales collapsed from $232B to $43.7B between 2000 and 2022",
"sub":"An 81% decline in 22 years. Sears, JCPenney, Macy's, Kohl's. The physical retail obituary.",
"type":"CHART","geo":"us_national","fmt":"Area chart",
"tbl":"US Census Bureau: Annual Retail Trade Survey — department store and nonstore retailer sales (census.gov/retail)",
"section":"Wholesale and Retail Trade",
"ext":["FRED: any national economic time series (fred.stlouisfed.org  free API)"],
"vars":["dept_store_sales","nonstore_retailer_sales","total_retail_sales"],
"join":["ecommerce_sales_pct","food_away_from_home_expenditure"],
"sc":{"emotional":8,"relatability":9,"clarity":9,"surprise":8,"tension":8,"visual":9,"data_ready":9,"originality":7},
"vs":0,"tags":"department stores retail collapse Sears JCPenney Macy's Amazon ecommerce death decline mall shopping",
"notes":"","topics":[],"status":"idea"
},

{
"id":"ecommerce_explosion",
"title":"Nonstore retail sales: from $165B to $1.19 trillion between 2000 and 2022",
"sub":"Amazon and friends created a $1T+ industry from almost nothing. The most dramatic sectoral shift in retail history.",
"type":"CHART","geo":"us_national","fmt":"Area chart",
"tbl":"US Census Bureau: Annual Retail Trade Survey — nonstore and ecommerce sales (census.gov/retail)",
"section":"Wholesale and Retail Trade",
"ext":["FRED: any national economic time series (fred.stlouisfed.org  free API)"],
"vars":["nonstore_retailer_sales","ecommerce_sales","total_retail_sales"],
"join":["dept_store_sales","warehouse_club_sales"],
"sc":{"emotional":8,"relatability":9,"clarity":9,"surprise":7,"tension":7,"visual":9,"data_ready":9,"originality":6},
"vs":0,"tags":"ecommerce Amazon nonstore retail online shopping growth trillion 2000 2022 digital economy",
"notes":"","topics":[],"status":"idea"
},

{
"id":"retail_vs_ecommerce_crossover",
"title":"The great retail crossover: when ecommerce surpassed department stores, bookstores, and electronics",
"sub":"In 2010, department stores still outsold all of ecommerce. By 2015, it was over.",
"type":"CHART","geo":"us_national","fmt":"Line chart",
"tbl":"US Census Bureau: Annual Retail Trade Survey — sales by retail sector (census.gov/retail)",
"section":"Wholesale and Retail Trade",
"ext":[],
"vars":["nonstore_retailer_sales","dept_store_sales","book_store_sales","electronics_store_sales"],
"join":["ecommerce_sales_pct"],
"sc":{"emotional":8,"relatability":9,"clarity":9,"surprise":8,"tension":7,"visual":9,"data_ready":9,"originality":7},
"vs":0,"tags":"retail crossover ecommerce department stores books electronics Amazon death of retail mall 2015 shopping",
"notes":"","topics":[],"status":"idea"
},

{
"id":"new_car_price_arc",
"title":"Average new car price in America: from $30K to $47.6K since 2000",
"sub":"New cars are 59% more expensive than they were 24 years ago, after inflation. The automotive squeeze.",
"type":"CHART","geo":"us_national","fmt":"Line chart",
"tbl":"Bureau of Economic Analysis + NADA: Average transaction price of new vehicles (bea.gov / nada.org)",
"section":"Wholesale and Retail Trade",
"ext":["FRED: any national economic time series (fred.stlouisfed.org  free API)","BLS CPI: Consumer Price Index by expenditure category (bls.gov/cpi)"],
"vars":["avg_new_car_price","new_car_cpi","all_items_cpi"],
"join":["auto_loan_rate","total_auto_sales","ev_sales_pct"],
"sc":{"emotional":8,"relatability":9,"clarity":8,"surprise":7,"tension":7,"visual":8,"data_ready":8,"originality":6},
"vs":0,"tags":"car price inflation new vehicle average cost transportation affordability 2000 2024 auto market squeeze",
"notes":"","topics":[],"status":"idea"
},

{
"id":"ev_sales_arc",
"title":"Electric vehicle sales in America: from near zero to 8% of all new cars",
"sub":"EV sales crossed 8% market share in 2023. The S-curve of automotive transformation.",
"type":"CHART","geo":"us_national","fmt":"Line chart",
"tbl":"BEA + Ward's AutoInfoBank + DOE: New vehicle sales by powertrain type (afdc.energy.gov)",
"section":"Wholesale and Retail Trade",
"ext":["FRED: any national economic time series (fred.stlouisfed.org  free API)"],
"vars":["ev_sales_total","ev_market_share_pct","hybrid_sales_total"],
"join":["gasoline_price_regular","ev_charging_stations","renewable_energy_share"],
"sc":{"emotional":7,"relatability":8,"clarity":8,"surprise":7,"tension":6,"visual":8,"data_ready":8,"originality":5},
"vs":0,"tags":"electric vehicle EV sales growth market share Tesla 2023 transportation climate green energy cars",
"notes":"","topics":[],"status":"idea"
},

{
"id":"warehousing_jobs_explosion",
"title":"Warehousing and storage jobs: from 638K to 1.85M since 2000",
"sub":"Amazon built a jobs category. Warehouse work is now one of the fastest-growing occupations in America.",
"type":"CHART","geo":"us_national","fmt":"Area chart",
"tbl":"BLS OES + CES: Employment in warehousing and storage by year (bls.gov)",
"section":"Transportation",
"ext":["FRED: any national economic time series (fred.stlouisfed.org  free API)","BLS national data: employment, wages, CPI (bls.gov  free API)"],
"vars":["warehousing_employment","total_transportation_employment"],
"join":["nonstore_retailer_sales","ecommerce_sales","median_warehouse_wage"],
"sc":{"emotional":7,"relatability":8,"clarity":8,"surprise":8,"tension":6,"visual":8,"data_ready":9,"originality":7},
"vs":0,"tags":"warehousing jobs Amazon fulfillment employment growth 638K 1.85M logistics supply chain labor economy",
"notes":"","topics":[],"status":"idea"
},

{
"id":"rideshare_gig_growth",
"title":"Rideshare and gig transport nonemployers: from 176K to 1.376M operators",
"sub":"Uber and Lyft did not create employees — they created 1.2 million new micro-businesses. The gig economy, quantified.",
"type":"CHART","geo":"us_national","fmt":"Area chart",
"tbl":"Census Bureau Nonemployer Statistics: Transportation nonemployer firms by sector (census.gov/programs-surveys/nonemployer-statistics)",
"section":"Transportation",
"ext":["FRED: any national economic time series (fred.stlouisfed.org  free API)"],
"vars":["rideshare_nonemployer_count","total_transport_nonemployers"],
"join":["gig_worker_income","median_rideshare_revenue"],
"sc":{"emotional":7,"relatability":9,"clarity":8,"surprise":8,"tension":7,"visual":8,"data_ready":8,"originality":7},
"vs":0,"tags":"rideshare gig Uber Lyft nonemployers growth 176K 1.376M workers economy transportation self-employed",
"notes":"","topics":[],"status":"idea"
},

{
"id":"pedestrian_deaths_surge",
"title":"Pedestrian traffic deaths up 53% since 2010 — while overall traffic deaths fell",
"sub":"Overall road deaths declined. Pedestrian deaths surged. Bigger vehicles, faster speeds, distracted driving.",
"type":"CHART","geo":"us_national","fmt":"Dual axis line chart",
"tbl":"NHTSA FARS: Traffic fatalities by victim type (nhtsa.dot.gov/data)",
"section":"Transportation",
"ext":["FRED: any national economic time series (fred.stlouisfed.org  free API)"],
"vars":["pedestrian_fatalities","total_traffic_fatalities","bicyclist_fatalities"],
"join":["suv_truck_market_share","speed_limit_changes","distracted_driving_citations"],
"sc":{"emotional":9,"relatability":9,"clarity":8,"surprise":9,"tension":8,"visual":8,"data_ready":9,"originality":8},
"vs":0,"tags":"pedestrian deaths traffic fatalities surge 53 percent 2010 SUV trucks speed walkers safety streets",
"notes":"","topics":[],"status":"idea"
},

{
"id":"gas_tax_by_state",
"title":"State gas tax by state 2024: Pennsylvania 61c, California 56c, Alaska 9c",
"sub":"Pennsylvania charges the highest gas tax in the country. Alaska the lowest. The invisible price at the pump.",
"type":"MAP","geo":"us_state","fmt":"State choropleth",
"tbl":"American Petroleum Institute + FHWA: State motor fuel tax rates (api.org / fhwa.dot.gov)",
"section":"Transportation",
"ext":["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API  free, tidycensus)"],
"vars":["state_gas_tax_cents","combined_gas_tax_cents"],
"join":["gasoline_price_regular","rep_pct","median_household_income","pct_bridges_poor"],
"sc":{"emotional":7,"relatability":9,"clarity":8,"surprise":7,"tension":6,"visual":9,"data_ready":9,"originality":6},
"vs":0,"tags":"gas tax state Pennsylvania California Alaska pump price infrastructure transportation funding per gallon",
"notes":"","topics":[],"status":"idea"
},

{
"id":"drone_pilot_certs_explosion",
"title":"FAA drone pilot certifications: from zero to 368,000 in 10 years",
"sub":"A new profession was created from scratch. 368K certified drone pilots in the US by 2023.",
"type":"CHART","geo":"us_national","fmt":"Area chart",
"tbl":"FAA: Registered unmanned aircraft and remote pilot certificates (faa.gov/data-research/aviation-data-statistics)",
"section":"Transportation",
"ext":[],
"vars":["remote_pilot_certs_total","drone_registrations_commercial","drone_registrations_recreational"],
"join":[],
"sc":{"emotional":6,"relatability":7,"clarity":8,"surprise":9,"tension":4,"visual":8,"data_ready":8,"originality":8},
"vs":0,"tags":"drones FAA pilot certification 368K zero to one new profession technology growth commercial recreational",
"notes":"","topics":[],"status":"idea"
},

{
"id":"xref_bridges_politics",
"title":"Worst bridge condition states vs. 2024 vote margin",
"sub":"Iowa 19.2% bridges poor. West Virginia 18.6%. Pennsylvania 15%. All voted Republican. Infrastructure and ideology.",
"type":"XREF","geo":"us_state","fmt":"Scatter plot",
"tbl":"FHWA: Structurally deficient bridge rate by state + MIT Election Lab: 2024 results",
"section":"Transportation  -  Elections",
"ext":["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API  free, tidycensus)","MIT Election Lab: presidential/congressional results (electionlab.mit.edu  free)"],
"vars":["pct_bridges_poor","rep_pct"],
"join":["total_transfers_per_capita","state_gdp_per_capita","median_household_income"],
"sc":{"emotional":8,"relatability":7,"clarity":6,"surprise":8,"tension":8,"visual":8,"data_ready":9,"originality":7},
"vs":0,"tags":"bridges infrastructure poor condition Republican Trump states Iowa West Virginia Pennsylvania politics XREF",
"notes":"","topics":[],"status":"idea"
},

{
"id":"xref_bridges_transfers",
"title":"Worst bridge infrastructure states vs. federal transfers per capita",
"sub":"States with the worst bridges receive the most federal money per person. The infrastructure-transfers paradox.",
"type":"XREF","geo":"us_state","fmt":"Scatter plot",
"tbl":"FHWA: Bridge condition by state + BEA: Government transfer payments per capita by state",
"section":"Transportation  -  Social Insurance",
"ext":["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API  free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov  free)"],
"vars":["pct_bridges_poor","total_transfers_per_capita"],
"join":["rep_pct","median_household_income","state_gdp_per_capita"],
"sc":{"emotional":8,"relatability":6,"clarity":6,"surprise":8,"tension":8,"visual":8,"data_ready":9,"originality":8},
"vs":0,"tags":"bridges infrastructure federal transfers XREF paradox poor states funding West Virginia Iowa Pennsylvania",
"notes":"","topics":[],"status":"idea"
},

{
"id":"airport_on_time_map",
"title":"Worst on-time performance at major US airports 2024",
"sub":"SFO: 61.7% on time — worst major hub. Salt Lake City best. The geography of the delayed flight.",
"type":"MAP","geo":"us_city","fmt":"Dot map",
"tbl":"BTS T-100 + FAA OPSNET: On-time performance by airport (bts.gov)",
"section":"Transportation",
"ext":[],
"vars":["pct_ontime_arrivals","pct_ontime_departures"],
"join":["passengers_enplaned","avg_delay_minutes"],
"sc":{"emotional":6,"relatability":10,"clarity":8,"surprise":7,"tension":4,"visual":10,"data_ready":9,"originality":5},
"vs":0,"tags":"airports on-time performance SFO worst Salt Lake City delays travel flying consumer frustration hub",
"notes":"","topics":[],"status":"idea"
},

{
"id":"transportation_gdp_share",
"title":"Transportation and warehousing share of US GDP 1990-2023",
"sub":"From 3.1% to 5.8% of GDP. The Amazon-ification of the economy created a new economic sector.",
"type":"CHART","geo":"us_national","fmt":"Area chart",
"tbl":"BEA GDP by Industry: Transportation and warehousing value added (bea.gov/data/gdp/gdp-industry)",
"section":"Transportation",
"ext":["FRED: any national economic time series (fred.stlouisfed.org  free API)"],
"vars":["transportation_gdp_share","warehousing_gdp_share"],
"join":["warehousing_employment","ecommerce_sales"],
"sc":{"emotional":6,"relatability":6,"clarity":7,"surprise":7,"tension":4,"visual":7,"data_ready":8,"originality":7},
"vs":0,"tags":"transportation warehousing GDP share Amazon logistics economy growth sector share percentage",
"notes":"","topics":[],"status":"idea"
},

{
"id":"worst_traffic_metros",
"title":"US metro areas with the worst traffic congestion 2024",
"sub":"Boston, LA, and NYC trade the top spot every year. But Houston is closing fast.",
"type":"RANK","geo":"us_metro","fmt":"Ranked list",
"tbl":"INRIX / TomTom Traffic Index: Annual hours lost to congestion by metro area",
"section":"Transportation",
"ext":[],
"vars":["hours_lost_congestion","congestion_cost_per_driver"],
"join":["transit_ridership","metro_unemployment_rate"],
"sc":{"emotional":6,"relatability":9,"clarity":10,"surprise":6,"tension":4,"visual":9,"data_ready":8,"originality":4},
"vs":0,"tags":"traffic congestion worst metros Boston LA NYC Houston commute hours lost cost driving urban",
"notes":"","topics":[],"status":"idea"
},

{
"id":"xref_gas_tax_bridge_condition",
"title":"State gas tax rate vs. bridge condition — do states that tax more maintain better?",
"sub":"Pennsylvania charges the most but still has terrible bridges. The disconnect between tax revenue and infrastructure quality.",
"type":"XREF","geo":"us_state","fmt":"Scatter plot",
"tbl":"API + FHWA: State gas tax rate + FHWA: Bridge structural condition by state",
"section":"Transportation",
"ext":["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API  free, tidycensus)"],
"vars":["state_gas_tax_cents","pct_bridges_poor"],
"join":["rep_pct","median_household_income","state_gdp_per_capita"],
"sc":{"emotional":7,"relatability":7,"clarity":6,"surprise":8,"tension":7,"visual":8,"data_ready":8,"originality":8},
"vs":0,"tags":"gas tax bridge condition XREF infrastructure Pennsylvania disconnect revenue spending quality",
"notes":"","topics":[],"status":"idea"
},

{
"id":"xref_car_price_income",
"title":"Average new car price vs. median household income by state 2023",
"sub":"In Mississippi, a new car costs 87% of median household income. In Maryland, 47%. The affordability collapse.",
"type":"XREF","geo":"us_state","fmt":"Scatter plot",
"tbl":"NADA + BEA: Average vehicle transaction price by state + ACS: Median household income by state",
"section":"Wholesale and Retail Trade  -  Income",
"ext":["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API  free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov  free)"],
"vars":["avg_new_car_price_state","median_household_income","car_to_income_ratio"],
"join":["auto_loan_rate","rep_pct","public_transit_usage"],
"sc":{"emotional":8,"relatability":9,"clarity":7,"surprise":8,"tension":7,"visual":8,"data_ready":7,"originality":8},
"vs":0,"tags":"car price income affordability Mississippi Maryland XREF ratio transportation household budget auto loan",
"notes":"","topics":[],"status":"idea"
},

]

def vscore(sc):
    return int(sc['emotional']*2 + sc['relatability']*2 + sc['clarity']*2 +
            sc['surprise']*1.5 + sc['tension']*1 + sc['visual']*1 +
            sc['data_ready']*0.5 + sc['originality']*0.5)

for idea in ideas:
    idea['vs'] = vscore(idea['sc'])
