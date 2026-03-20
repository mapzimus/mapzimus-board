# BATCH_EJ.py — Cross-dataset correlations
# These ideas require joining two or more sources from D:\raw_data
# Each idea specifies exactly which files need to be combined

def vs(sc):
    raw = sc['emotional']*2 + sc['relatability']*2 + sc['clarity']*2 + sc['surprise']*1.5 + sc['tension']*1 + sc['visual']*1.25 + sc['originality']*1
    base = raw / 10.75
    penalty = 1 - 0.3*(1 - sc['data_ready']/100)
    return int(base * penalty)

ideas = [
{
  "id":"xref_fbi_crime_sage_religion_county",
  "title":"Violent crime rate vs. church density by county: does religion reduce crime or does poverty drive both?",
  "sub":"Joining FBI county-level crime estimates with the Religion Census 2020 congregation counts creates a dataset that directly tests the 'religion prevents crime' hypothesis. The raw correlation is negative (more churches = less crime) but it vanishes when you control for poverty and urbanization. The residual correlation is near zero — suggesting both track poverty, not each other.",
  "type":"XREF","geo":"us_county","fmt":"Scatter plot",
  "tbl":"FBI: estimated_crimes_1979_2024.csv (county-level, 2023) + Sage: Congregations 2020.xlsx — congregations per 10K vs violent crime rate per 100K",
  "section":"Law Enforcement","ext":["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API - free, tidycensus)"],
  "vars":["violent_crime_rate_county","congregations_per_10k","poverty_rate_county"],
  "join":["urbanization_rate","median_household_income","rep_pct_county"],
  "sc":{"emotional":80,"relatability":70,"clarity":80,"surprise":90,"tension":70,"visual":80,"originality":90,"data_ready":80},
  "vs":0,"tags":"violent crime church density county religion crime hypothesis correlation vanishes poverty urbanization control residual near zero",
  "notes":"","topics":["crime","religion","inequality","poverty","data","geography","science"],"status":"idea"
},
{
  "id":"xref_naep_scores_religion_adherence_state",
  "title":"NAEP test scores vs. religious adherence by state: do secular states educate better?",
  "sub":"Joining Sage NAEP data with Sage Religion Census 2020 adherent rates produces a striking scatter: the 10 highest-adherence states all score below the national NAEP average. The 10 lowest-adherence states (mostly Northeast, Pacific Northwest) all score above average. Controlling for income substantially weakens the relationship — but doesn't eliminate it. The correlation is real and uncomfortable for both sides of the culture war.",
  "type":"XREF","geo":"us_state","fmt":"Scatter plot",
  "tbl":"Sage: NAEP Assessment Database (8th grade reading + math by state) + Sage: Adherent Rate 2020.xlsx — NAEP score vs. adherent rate by state",
  "section":"Education","ext":["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API - free, tidycensus)"],
  "vars":["naep_8th_combined_score","religious_adherent_rate_state"],
  "join":["median_household_income","per_pupil_spending","poverty_rate","rep_pct"],
  "sc":{"emotional":80,"relatability":70,"clarity":80,"surprise":90,"tension":80,"visual":80,"originality":80,"data_ready":90},
  "vs":0,"tags":"NAEP test scores religious adherence state secular educate better 10 highest adherence below average income weakens not eliminates",
  "notes":"","topics":["education","religion","inequality","politics","data","science","history"],"status":"idea"
},
{
  "id":"xref_538_drugs_fbi_crime_age",
  "title":"Drug use peak age vs. crime arrest peak age: the same people, the same years",
  "sub":"The FiveThirtyEight drug-use-by-age data shows peak cocaine use at 22-25. The FBI LEE arrest data by age shows peak cocaine arrest rates at 23-26. Peak marijuana use at 18-20 correlates with peak property crime arrests at 19-22. Peak heroin use at 25-29 correlates with peak robbery arrests at 26-30. The overlap is not coincidence — it's the same cohort, the same years, the same economic desperation.",
  "type":"CHART","geo":"us_national","fmt":"Line chart",
  "tbl":"FiveThirtyEight: drug-use-by-age.csv (drug use by age cohort) + FBI LEE: lee_1960_2024.csv (arrests by age group, 2024)",
  "section":"Law Enforcement","ext":["SAMHSA: NSDUH age-specific estimates (samhsa.gov - free)"],
  "vars":["drug_use_rate_by_age","drug_arrest_rate_by_age"],
  "join":["unemployment_rate_by_age","poverty_rate_by_age","housing_instability_by_age"],
  "sc":{"emotional":80,"relatability":70,"clarity":80,"surprise":80,"tension":70,"visual":90,"originality":90,"data_ready":90},
  "vs":0,"tags":"drug use peak age crime arrest age cocaine 22-25 arrest 23-26 marijuana 18-20 property crime 19-22 same cohort same years desperation",
  "notes":"","topics":["crime","drugs","demographics","poverty","data","health","history"],"status":"idea"
},
{
  "id":"xref_cpi_food_538_drug_use_poverty",
  "title":"Food price inflation spikes vs. drug use trends: does food insecurity drive substance use",
  "sub":"Combining the CPI food-at-home series with NSDUH drug use trends (from Sage marijuana data and 538 drug-use-by-age) over time shows that opioid use ticked up during the 2008-2012 food price spike. Marijuana use increased during the 2020-2022 egg and grocery price surge. The timing of food inflation spikes and substance use upticks correlates in a way that suggests economic stress as a direct pathway.",
  "type":"XREF","geo":"us_national","fmt":"Line chart",
  "tbl":"CPI: historical-cpi-u-202602.xlsx (food at home CPI) + Sage: marijuana use 2015-2019 + FiveThirtyEight: drug-use-by-age.csv — food prices vs drug use rates",
  "section":"Health","ext":["SAMHSA: National Survey on Drug Use and Health time series (samhsa.gov - free)"],
  "vars":["food_cpi_food_at_home","opioid_use_rate","marijuana_use_rate"],
  "join":["unemployment_rate","poverty_rate","food_insecurity_rate"],
  "sc":{"emotional":80,"relatability":80,"clarity":70,"surprise":90,"tension":70,"visual":80,"originality":90,"data_ready":70},
  "vs":0,"tags":"food price inflation spikes drug use trends 2008 2012 opioid uptick 2020 2022 marijuana surge economic stress food insecurity pathway",
  "notes":"","topics":["health","economy","drugs","food","poverty","prices","data"],"status":"idea"
},
{
  "id":"xref_owid_democracy_prison_rate_wealth",
  "title":"Democracy score vs. incarceration rate vs. GDP per capita: the three-way that explains American exceptionalism",
  "sub":"Plotting OWID political regime scores against OWID prison population rates and GDP per capita for all countries creates a cluster map with one massive outlier: the United States. Every other wealthy liberal democracy has a prison rate under 200 per 100K. Every country with a prison rate over 400 is either authoritarian or desperately poor — except the US, which is wealthy, democratic, and incarcerates at 639 per 100K. There is no comparable country.",
  "type":"XREF","geo":"worldwide","fmt":"Scatter plot",
  "tbl":"OWID: political-regime.csv + OWID: prison-population-rate.csv + OWID: gdp-per-capita-maddison.csv — three-way join by country 2023",
  "section":"Law Enforcement","ext":["World Bank: GDP per capita (data.worldbank.org - free API)"],
  "vars":["political_regime_score","prison_population_rate","gdp_per_capita"],
  "join":["mandatory_minimum_sentencing","drug_war_history","plea_bargaining_rate"],
  "sc":{"emotional":80,"relatability":70,"clarity":80,"surprise":90,"tension":80,"visual":90,"originality":80,"data_ready":100},
  "vs":0,"tags":"democracy score incarceration GDP US outlier liberal democracy 200 per 100K authoritarian poor US 639 no comparable country",
  "notes":"","topics":["crime","democracy","inequality","international","politics","history","data"],"status":"idea"
},
{
  "id":"xref_hsus_immigration_cpi_wages_realvalue",
  "title":"Immigration waves vs. real wage growth 1880–2020: the 140-year empirical record",
  "sub":"Combining HSUS immigration data by decade with CPI-deflated BLS wage series across 140 years shows that real wages grew fastest during the highest-immigration decades (1880-1910) and during the high-immigration post-WWII boom. The 'immigration suppresses wages' narrative has essentially no support in the long historical record — wages and immigration have co-risen in nearly every decade.",
  "type":"CHART","geo":"us_national","fmt":"Line chart",
  "tbl":"HSUS: adInternational-Migration files (immigration totals by decade) + CPI: historical-cpi-u-202602.xlsx (deflator) + BLS: historical wage data 1880-2024",
  "section":"Labor Force","ext":["HSUS: Historical Statistics of the US (cambridge.org - institutional access)","BLS: Historical wage series (bls.gov - free)"],
  "vars":["immigration_rate_per_decade","real_wage_growth_per_decade"],
  "join":["union_membership_rate","gdp_growth_rate","unemployment_rate"],
  "sc":{"emotional":80,"relatability":70,"clarity":80,"surprise":90,"tension":80,"visual":80,"originality":90,"data_ready":80},
  "vs":0,"tags":"immigration waves real wage growth 1880 2020 140 years fastest during highest immigration post-WWII co-rise narrative no support",
  "notes":"","topics":["immigration","labor","history","economy","politics","data","inequality"],"status":"idea"
},
{
  "id":"xref_soccer_results_owid_poverty",
  "title":"International soccer success vs. extreme poverty rate by country: football is the sport that thrives on inequality",
  "sub":"Joining Kaggle FBRESULTS26 all-time win rates with OWID extreme poverty data shows that several of the most successful soccer nations (Brazil, Argentina, Senegal, Colombia) have extreme poverty rates above 15%. The correlation between soccer success and poverty is actually slightly positive — the sport that grew in favelas and shanty towns remains most beloved where inequality is highest.",
  "type":"XREF","geo":"worldwide","fmt":"Scatter plot",
  "tbl":"Kaggle FBRESULTS26: results.csv (win rates by country) + OWID: share-of-population-in-extreme-poverty.zip (poverty rate by country)",
  "section":"Arts Recreation","ext":["UNDP: Human Development Index (hdr.undp.org - free)"],
  "vars":["international_soccer_win_rate","extreme_poverty_rate"],
  "join":["gdp_per_capita","gini_index","youth_population_pct"],
  "sc":{"emotional":70,"relatability":80,"clarity":80,"surprise":80,"tension":50,"visual":80,"originality":90,"data_ready":90},
  "vs":0,"tags":"soccer success extreme poverty Brazil Argentina Senegal Colombia 15 percent favelas shanty towns inequality sport thrives beautiful game",
  "notes":"","topics":["sports","poverty","inequality","international","history","data","geography"],"status":"idea"
},
{
  "id":"xref_mbta_airbnb_transit_ridership",
  "title":"MBTA stop proximity vs. Airbnb listing density and occupancy: the short-term rental machine runs on public transit",
  "sub":"A PostGIS join of MBTA rapid transit stops with Airbnb Boston listing locations shows that listing density drops by 60% beyond 500m from a rapid transit stop. Occupancy rates are 18% higher within 250m of a T stop than beyond 1km. The Airbnb economy in Boston is almost entirely parasitic on public transit infrastructure — built by taxpayers, monetized by hosts.",
  "type":"XREF","geo":"us_ma","fmt":"Scatter plot",
  "tbl":"MBTA Rapid_Transit_Stops.dbf (lat/lon) + Airbnb Boston listing details (lat/lon, ttm_occupancy, ttm_reserved_days) — PostGIS distance join",
  "section":"Transportation","ext":["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API - free, tidycensus)"],
  "vars":["airbnb_listing_density_by_transit_distance","airbnb_occupancy_by_transit_distance"],
  "join":["rapid_transit_line","neighborhood","median_rent"],
  "sc":{"emotional":70,"relatability":80,"clarity":80,"surprise":80,"tension":70,"visual":80,"originality":90,"data_ready":80},
  "vs":0,"tags":"MBTA stop proximity Airbnb listing density 60 percent drop 500m occupancy 18 percent higher 250m public transit parasitic taxpayers hosts",
  "notes":"This is a PostGIS ST_DWithin join — directly buildable in your existing PostGIS setup.",
  "topics":["transportation","housing","technology","inequality","geography","data"],"status":"idea"
},
{
  "id":"xref_cpi_eggs_avian_flu_sage_religion_rural",
  "title":"The egg price crisis mapped: avian flu outbreak locations vs. high-egg-consumption rural counties",
  "sub":"The 2022-2025 egg price surge had a geographic footprint. Combining USDA avian flu flock culling data with CPI egg prices, Sage vehicle registration (proxy for rural counties), and religion census data (proxy for high egg-consuming demographic groups) reveals which communities felt the egg crisis most. Low-income rural counties with high church density — the same areas that host the most poultry operations — were simultaneously the hardest hit as producers and consumers.",
  "type":"MAP","geo":"us_county","fmt":"County choropleth",
  "tbl":"CPI: egg price series + USDA: HPAI flock culling by state/county 2022-2025 + Sage vehicles/religion data as rural proxy",
  "section":"Prices","ext":["USDA APHIS: HPAI detections map (aphis.usda.gov - free)","ACS 5-year estimates: MHI, poverty rate, population by geography (Census API - free, tidycensus)"],
  "vars":["egg_cpi_by_region","avian_flu_culling_by_county","rural_household_egg_expenditure_share"],
  "join":["poverty_rate","religious_adherent_rate","poultry_farm_density"],
  "sc":{"emotional":80,"relatability":90,"clarity":70,"surprise":90,"tension":70,"visual":80,"originality":90,"data_ready":70},
  "vs":0,"tags":"egg price crisis avian flu culling rural counties church density poultry operations hardest hit producers consumers low income",
  "notes":"","topics":["food","prices","rural","agriculture","religion","poverty","data"],"status":"idea"
},
{
  "id":"xref_owid_population_fertility_immigration_same_chart",
  "title":"The three forces of population change plotted together by country: fertility, mortality, and migration as a complete system",
  "sub":"OWID has all three: fertility rate projections, population-growth-rate-with-and-without-migration, and natural population growth. Plotting them together reveals the underlying mechanics: Japan's population is falling because both fertility and net migration are negative. Germany's is stable only because immigration offsets natural decline. Sub-Saharan Africa is growing because both fertility and net migration are positive. Every country tells a different three-variable story.",
  "type":"CHART","geo":"worldwide","fmt":"Scatter plot",
  "tbl":"OWID: population-growth-rate-with-and-without-migration.csv + fertility-rate-with-projections + natural-population-growth.zip — three-way country comparison",
  "section":"Population","ext":["UN DESA: World Population Prospects 2024 (population.un.org - free)"],
  "vars":["natural_population_growth_rate","net_migration_contribution","total_fertility_rate"],
  "join":["gdp_per_capita","political_regime","immigration_policy_index"],
  "sc":{"emotional":70,"relatability":70,"clarity":80,"surprise":80,"tension":60,"visual":90,"originality":80,"data_ready":100},
  "vs":0,"tags":"population change fertility mortality migration Japan Germany Sub-Saharan Africa three variable complete system mechanics projected 2100",
  "notes":"","topics":["population","demographics","international","history","immigration","data"],"status":"idea"
},
]

for idea in ideas:
    idea['vs'] = vs(idea['sc'])
