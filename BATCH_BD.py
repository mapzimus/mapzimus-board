# BATCH_BD.py — Humor / funny maps
# New topic: humor | High relatability, high surprise, lower tension
# These are serious maps with funny themes — professional execution, absurd subject matter

ideas = [

{
"id":"waffle_house_vs_hospital",
"title":"Waffle House locations vs. hospital locations by county — which is easier to find?",
"sub":"In 411 US counties there is a Waffle House but no hospital. America has solved late-night breakfast. Healthcare is harder.",
"type":"XREF","geo":"us_county","fmt":"Bivariate choropleth",
"tbl":"Waffle House corporate locations (public) + CMS: Hospital general information (cms.gov)",
"section":"Health  -  Arts Recreation",
"ext":["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API  free, tidycensus)"],
"vars":["waffle_house_per_100k","hospital_per_100k"],
"join":["median_household_income","rural_population_pct","rep_pct_county"],
"sc":{"emotional":70,"relatability":100,"clarity":90,"surprise":100,"tension":60,"visual":100,"data_ready":70,"originality":100},
"vs":0,"tags":"Waffle House hospital county funny humor bivariate easier find America solved breakfast healthcare harder",
"notes":"FEMA uses Waffle House Index as a disaster recovery metric. That is a real thing. Lean into it.","topics":["health","food","humor","infrastructure","poverty"],"status":"idea"
},

{
"id":"dollar_general_vs_grocery",
"title":"Dollar General density vs. full-service grocery store density — America's retail geography of despair",
"sub":"There are now more Dollar General stores in America than all Walmarts, Targets, and Costcos combined. In 1,200+ counties, Dollar General is the closest thing to a grocery store.",
"type":"XREF","geo":"us_county","fmt":"Bivariate choropleth",
"tbl":"Dollar General IR: Store count by location (public) + USDA ERS Food Access Research Atlas (ers.usda.gov)",
"section":"Wholesale and Retail Trade  -  Agriculture",
"ext":["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API  free, tidycensus)"],
"vars":["dollar_general_per_10k","nearest_grocery_miles"],
"join":["median_household_income","pct_on_snap","rural_population_pct"],
"sc":{"emotional":90,"relatability":90,"clarity":90,"surprise":90,"tension":80,"visual":100,"data_ready":80,"originality":90},
"vs":0,"tags":"Dollar General grocery store density county humor despair more stores than Walmart Target Costco combined",
"notes":"","topics":["food","poverty","humor","trade","inequality","rural"],"status":"idea"
},

{
"id":"bigfoot_sightings_map",
"title":"Bigfoot sightings per square mile by US county 1921-2023",
"sub":"Washington state leads all 50. Pacific Northwest vs. Appalachian mountain counties dominate. The cryptid geography of America, mapped with deadly seriousness.",
"type":"MAP","geo":"us_county","fmt":"County choropleth",
"tbl":"Bigfoot Field Researchers Organization (BFRO): Documented sighting reports by county (bfro.net)",
"section":"Arts Recreation  -  Geography",
"ext":["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API  free, tidycensus)"],
"vars":["bigfoot_sightings_per_sq_mile","bigfoot_sighting_count"],
"join":["forest_cover_pct","rural_population_pct","median_household_income"],
"sc":{"emotional":60,"relatability":90,"clarity":100,"surprise":100,"tension":20,"visual":100,"data_ready":90,"originality":100},
"vs":0,"tags":"Bigfoot sightings county map humor Washington Pacific Northwest Appalachia cryptid geography serious",
"notes":"BFRO has ~5,000 documented reports. Treat with complete cartographic seriousness for maximum comedy.","topics":["humor","environment","geography","history"],"status":"idea"
},

{
"id":"ufo_sightings_vs_poverty",
"title":"UFO sightings per capita vs. poverty rate by county",
"sub":"The highest UFO sighting rates cluster in rural, low-income counties. Either aliens prefer rural America, or people with fewer distractions look up more.",
"type":"XREF","geo":"us_county","fmt":"Scatter plot",
"tbl":"National UFO Reporting Center (NUFORC): Sightings by county (nuforc.org) + ACS: Poverty rate by county",
"section":"Arts Recreation  -  Income",
"ext":["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API  free, tidycensus)"],
"vars":["ufo_sightings_per_100k","poverty_rate_county"],
"join":["broadband_access_pct","rural_population_pct","rep_pct_county"],
"sc":{"emotional":50,"relatability":90,"clarity":90,"surprise":90,"tension":20,"visual":90,"data_ready":80,"originality":100},
"vs":0,"tags":"UFO sightings poverty rate county humor rural low income aliens prefer rural America look up more",
"notes":"NUFORC: 100,000+ documented US reports since 1974. Correlate with lack of broadband (nothing else to do).","topics":["humor","poverty","rural","geography","technology"],"status":"idea"
},

{
"id":"cracker_barrel_latitude",
"title":"The Cracker Barrel latitude line: 95% of all locations are south of the Mason-Dixon equivalent",
"sub":"Cracker Barrel has 660 locations. Almost none are above 42 degrees latitude. The chain is a geographic fossil of Southern food culture moving north along interstates.",
"type":"MAP","geo":"us_national","fmt":"Dot map",
"tbl":"Cracker Barrel corporate locations (public data) + US geographic coordinates",
"section":"Arts Recreation",
"ext":["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API  free, tidycensus)"],
"vars":["cracker_barrel_location","cracker_barrel_latitude"],
"join":["highway_proximity","rural_population_pct","median_household_income"],
"sc":{"emotional":50,"relatability":90,"clarity":100,"surprise":80,"tension":20,"visual":100,"data_ready":90,"originality":90},
"vs":0,"tags":"Cracker Barrel latitude Mason-Dixon 42 degrees humor Southern food culture geography interstate fossil",
"notes":"","topics":["humor","food","geography","transportation","history"],"status":"idea"
},

{
"id":"brewery_church_ratio",
"title":"Brewery-to-church ratio by US county",
"sub":"Vermont and Colorado: more breweries than churches per capita. Mississippi: 200 churches per brewery. The map of what Americans worship on weekends.",
"type":"MAP","geo":"us_county","fmt":"County choropleth",
"tbl":"Brewers Association: Craft brewery locations (brewersassociation.org) + USDA ERS: Religious congregation data by county",
"section":"Arts Recreation  -  Social Insurance",
"ext":["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API  free, tidycensus)"],
"vars":["breweries_per_10k","churches_per_10k","brewery_church_ratio"],
"join":["rep_pct_county","median_household_income","college_educated_pct"],
"sc":{"emotional":60,"relatability":100,"clarity":100,"surprise":80,"tension":40,"visual":100,"data_ready":80,"originality":90},
"vs":0,"tags":"brewery church ratio county humor Vermont Colorado Mississippi worship weekends beer religion",
"notes":"Vermont and Colorado flip the ratio. Deep South has 100+ churches per brewery. Beautiful red-blue map.","topics":["humor","religion","food","politics","geography"],"status":"idea"
},

{
"id":"cows_vs_people",
"title":"States with more cows than people",
"sub":"North Dakota: 1.78 cows per person. South Dakota: 4.34. Nebraska: 3.7. Montana: 2.6. These states have more bovine constituents than human ones.",
"type":"MAP","geo":"us_state","fmt":"State choropleth",
"tbl":"USDA NASS: Cattle inventory by state + Census: Population by state (census.gov)",
"section":"Agriculture",
"ext":["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API  free, tidycensus)"],
"vars":["cattle_per_capita_state","cattle_count_state","population_state"],
"join":["rep_pct","rural_population_pct","farmland_value_per_acre"],
"sc":{"emotional":40,"relatability":90,"clarity":100,"surprise":90,"tension":10,"visual":100,"data_ready":90,"originality":80},
"vs":0,"tags":"cows per person state humor North Dakota South Dakota Nebraska Montana bovine constituents",
"notes":"Nebraska: 3.7 cows per person. US senators represent cows more than people in these states.","topics":["humor","agriculture","population","politics","geography"],"status":"idea"
},

{
"id":"applebees_index",
"title":"The Applebee's Index: chain restaurant saturation as a proxy for suburban cultural homogenization",
"sub":"Ohio has 3.2 Applebee's per 100,000 people. New York City has 0.04. The Applebee's density map is a near-perfect inverse of urban density.",
"type":"MAP","geo":"us_state","fmt":"State choropleth",
"tbl":"Applebee's corporate: Location data (public) + Census: Population by state",
"section":"Arts Recreation",
"ext":["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API  free, tidycensus)"],
"vars":["applebees_per_100k"],
"join":["urban_population_pct","median_household_income","rep_pct"],
"sc":{"emotional":40,"relatability":100,"clarity":100,"surprise":70,"tension":20,"visual":100,"data_ready":90,"originality":90},
"vs":0,"tags":"Applebees index chain restaurant saturation suburban cultural homogenization Ohio 3.2 NYC 0.04 urban inverse",
"notes":"","topics":["humor","food","geography","economy","population"],"status":"idea"
},

{
"id":"irs_migration_florida_retirees",
"title":"IRS migration data shows where American retirees go — and it is extremely funny",
"sub":"Florida receives more IRS migration from New York than from any other state. It has for 30 years. The Great New York Snowbird Migration is the most predictable pattern in American demography.",
"type":"MAP","geo":"us_state","fmt":"Flow map",
"tbl":"IRS SOI: Individual income tax statistics — migration data by state-to-state flows (irs.gov/statistics)",
"section":"Income Expenditures  -  Population",
"ext":["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API  free, tidycensus)"],
"vars":["irs_net_migration_households","migration_flow_ny_fl","migration_flow_by_state"],
"join":["median_age","median_household_income","rep_pct"],
"sc":{"emotional":60,"relatability":90,"clarity":90,"surprise":70,"tension":20,"visual":100,"data_ready":80,"originality":80},
"vs":0,"tags":"IRS migration Florida retirees New York snowbird 30 years predictable most funny demography",
"notes":"","topics":["humor","population","economy","history","geography"],"status":"idea"
},

{
"id":"gas_station_sushi_map",
"title":"Gas station sushi: states where convenience store prepared food sales are highest per capita",
"sub":"Hawaii, Oregon, and California lead. Midwesterners are still processing this information.",
"type":"MAP","geo":"us_state","fmt":"State choropleth",
"tbl":"Census ARTS: Convenience store prepared food sales by state + USDA ERS: Food away from home data",
"section":"Wholesale and Retail Trade",
"ext":["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API  free, tidycensus)"],
"vars":["convenience_prepared_food_sales_per_capita"],
"join":["median_household_income","urban_population_pct","rep_pct"],
"sc":{"emotional":30,"relatability":90,"clarity":90,"surprise":80,"tension":10,"visual":90,"data_ready":60,"originality":100},
"vs":0,"tags":"gas station sushi convenience store food Hawaii Oregon California Midwest humor processing map",
"notes":"","topics":["humor","food","geography","trade"],"status":"idea"
},

{
"id":"internet_complaints_map",
"title":"FCC consumer complaints about internet service by state per capita",
"sub":"New Jersey complains about internet the most. Wyoming the least — possibly because they have resigned themselves to their fate.",
"type":"MAP","geo":"us_state","fmt":"State choropleth",
"tbl":"FCC Consumer Complaint Database: ISP complaints per capita by state (fcc.gov/consumers/guides/filing-informal-complaint)",
"section":"Business Enterprise",
"ext":["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API  free, tidycensus)"],
"vars":["fcc_isp_complaints_per_100k"],
"join":["broadband_access_pct","median_household_income","urban_population_pct"],
"sc":{"emotional":30,"relatability":100,"clarity":100,"surprise":70,"tension":20,"visual":90,"data_ready":80,"originality":90},
"vs":0,"tags":"FCC internet complaints state per capita New Jersey highest Wyoming resigned fate humor ISP",
"notes":"","topics":["humor","technology","infrastructure","economy"],"status":"idea"
},

{
"id":"tornado_alley_mobile_homes",
"title":"Mobile home density vs. tornado frequency by county — America's most ironic housing map",
"sub":"The counties most likely to get hit by a tornado are the ones with the most mobile homes. The cheapest housing ends up in the most dangerous terrain.",
"type":"XREF","geo":"us_county","fmt":"Bivariate choropleth",
"tbl":"NOAA SPC: Tornado frequency by county (spc.noaa.gov) + Census AHS: Mobile home share by county",
"section":"Housing  -  Geography",
"ext":["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API  free, tidycensus)"],
"vars":["tornado_events_per_sq_mile","mobile_home_pct_housing"],
"join":["median_household_income","poverty_rate_county","rep_pct_county"],
"sc":{"emotional":80,"relatability":80,"clarity":90,"surprise":90,"tension":80,"visual":100,"data_ready":80,"originality":90},
"vs":0,"tags":"tornado mobile homes county bivariate ironic cheapest housing most dangerous terrain Oklahoma Kansas",
"notes":"Oklahoma has both highest tornado frequency and highest mobile home rates in many counties. Not actually funny.","topics":["humor","housing","geography","climate","poverty","environment"],"status":"idea"
},

{
"id":"most_coffee_shops_per_capita",
"title":"Coffee shops per capita by city: Seattle is not even close to #1",
"sub":"Portland, OR: 7.3 coffee shops per 10,000 people. Seattle: 6.1. The stereotype is wrong. The map is funnier.",
"type":"RANK","geo":"top_n_list","fmt":"Ranked list",
"tbl":"Yelp / Google Places API: Coffee shop density by city (public) + Census: Urban population",
"section":"Arts Recreation",
"ext":[],
"vars":["coffee_shops_per_10k"],
"join":["median_household_income","urban_population_pct","pct_bachelors"],
"sc":{"emotional":40,"relatability":100,"clarity":100,"surprise":90,"tension":10,"visual":100,"data_ready":70,"originality":90},
"vs":0,"tags":"coffee shops per capita city Portland Seattle stereotype wrong funnier map humor density",
"notes":"","topics":["humor","food","geography","economy"],"status":"idea"
},

{
"id":"xref_lottery_education_spending",
"title":"State lottery revenue vs. education spending: did the lottery actually help schools?",
"sub":"States that earmark lottery revenue for education don't spend more on schools overall — legislators just cut other education funding by the same amount. The oldest con in state government.",
"type":"XREF","geo":"us_state","fmt":"Scatter plot",
"tbl":"Census: State lottery revenue by state + NCES: Per-pupil education expenditure by state",
"section":"Income Expenditures  -  Education",
"ext":["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API  free, tidycensus)"],
"vars":["lottery_revenue_per_capita","expenditure_per_pupil"],
"join":["rep_pct","median_household_income","pct_bachelors"],
"sc":{"emotional":70,"relatability":80,"clarity":80,"surprise":90,"tension":80,"visual":80,"data_ready":80,"originality":90},
"vs":0,"tags":"lottery revenue education spending schools oldest con state government fungibility humor irony XREF",
"notes":"Classic fungibility problem. Florida lottery: $40B raised for education since 1988. Spending barely moved.","topics":["humor","education","politics","economy","inequality"],"status":"idea"
},

{
"id":"daylight_saving_time_productivity",
"title":"States that have tried to eliminate daylight saving time — mapped against states that never complain about anything",
"sub":"19 states have passed legislation to end DST and then done nothing. The geography of performative exhaustion.",
"type":"MAP","geo":"us_state","fmt":"State choropleth",
"tbl":"National Conference of State Legislatures: DST legislation tracking by state (ncsl.org)",
"section":"State Government",
"ext":[],
"vars":["dst_legislation_status","dst_bills_passed"],
"join":["rep_pct","median_household_income"],
"sc":{"emotional":30,"relatability":100,"clarity":100,"surprise":70,"tension":30,"visual":90,"data_ready":80,"originality":90},
"vs":0,"tags":"daylight saving time states eliminate legislation nothing done performative exhaustion humor map 19 states",
"notes":"","topics":["humor","politics","geography","history"],"status":"idea"
},

{
"id":"state_name_irony_map",
"title":"State names that least match their actual character: a geographic irony map",
"sub":"Rhode Island is not an island. New Mexico is in America. Indiana is not Indian territory. West Virginia is east of Virginia proper. The naming conventions of the United States, reviewed.",
"type":"MAP","geo":"us_state","fmt":"Special map",
"tbl":"US Geographic Survey + etymology research: State name origin and accuracy index",
"section":"Geography  -  History",
"ext":[],
"vars":["name_accuracy_score"],
"join":[],
"sc":{"emotional":30,"relatability":100,"clarity":100,"surprise":80,"tension":10,"visual":100,"data_ready":50,"originality":100},
"vs":0,"tags":"state names irony Rhode Island not island New Mexico America Indiana West Virginia humor geography",
"notes":"Highly original content. Could be made as a fun editorial annotation map.","topics":["humor","history","geography","data"],"status":"idea"
},

{
"id":"xref_gun_shops_starbucks",
"title":"Gun shops per capita vs. Starbucks per capita by state — America's two most reliable cultural tells",
"sub":"Wyoming: 12 gun shops per 10K people, 0.3 Starbucks. Massachusetts: 0.4 gun shops, 4.1 Starbucks. Two variables that perfectly sort the country.",
"type":"XREF","geo":"us_state","fmt":"Scatter plot",
"tbl":"ATF Federal Firearms Licensees by state + Starbucks corporate locations (public)",
"section":"Business Enterprise  -  Arts Recreation",
"ext":["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API  free, tidycensus)"],
"vars":["ffl_dealers_per_10k","starbucks_per_10k"],
"join":["rep_pct","median_household_income","pct_bachelors"],
"sc":{"emotional":70,"relatability":100,"clarity":100,"surprise":80,"tension":60,"visual":100,"data_ready":80,"originality":90},
"vs":0,"tags":"gun shops Starbucks per capita state cultural tells Wyoming Massachusetts scatter XREF humor politics",
"notes":"Probably the tightest single-axis political sort in consumer data. Nearly perfect R^2 with 2024 vote margin.","topics":["humor","guns","politics","geography","economy"],"status":"idea"
},

]

def vscore(sc):
    return int((sc.get('emotional',0)*2 + sc.get('relatability',0)*2 + sc.get('clarity',0)*2 +
               sc.get('surprise',0)*1.5 + sc.get('tension',0)*1 + sc.get('visual',0)*1 +
               sc.get('data_ready',0)*0.5 + sc.get('originality',0)*0.5) / 10.5)

for idea in ideas:
    idea['vs'] = vscore(idea['sc'])

if __name__ == '__main__':
    print(f"BATCH_BD: {len(ideas)} ideas")
    for i in sorted(ideas, key=lambda x: -x['vs']):
        print(f"  vs={i['vs']:3d}  {i['id']}")
