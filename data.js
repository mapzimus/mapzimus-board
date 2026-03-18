







const D = [







{id:"gop_transfers",title:"GOP vote share vs. federal transfers per capita by state",sub:"Mississippi, WV, and Kentucky top both lists â€” most federal money, most Republican votes.",type:"XREF",geo:"us_state",fmt:"Bivariate choropleth",tbl:"T573 Â· T454",section:"Social Insurance Â· Elections",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)","MIT Election Lab: presidential/congressional results (electionlab.mit.edu â€” free)"],vars:["total_transfers_per_capita","rep_pct"],join:["median_household_income","violent_crime_rate","pct_bachelors","pct_on_snap","state_unemployment_rate","pct_voted_state"],sc:{emotional:10,relatability:8,surprise:9,tension:10,visual:9,data_ready:10,originality:9},vs:97,tags:"politics federal aid red states Trump MAGA welfare Medicaid Medicare fiscal hypocrisy rural poverty republican democrat"},







{id:"abortion_state_map",title:"States with abortion provider access vs. 2024 vote margin",sub:"14 states have zero providers. The access desert and the vote geography are the same map.",type:"XREF",geo:"us_state",fmt:"State choropleth",tbl:"T454",section:"Elections",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)","MIT Election Lab: presidential/congressional results (electionlab.mit.edu â€” free)"],vars:["rep_pct","dem_pct","margin"],join:["birth_rate_state","teen_birth_rate","median_household_income","pct_births_unmarried"],sc:{emotional:10,relatability:9,surprise:7,tension:10,visual:9,data_ready:9,originality:7},vs:93,tags:"abortion Dobbs Roe reproductive rights women access SCOTUS Trump red states pro-choice pro-life vote geography"},







{id:"redlining_landcover",title:"1930s HOLC redlining grades vs. current land cover by city",sub:"The literal shade of inequality â€” 90 years of disinvestment still visible in the land.",type:"XREF",geo:"us_city",fmt:"City map",proxy:true,proxyNote:"Land cover (T413) used as proxy for urban tree canopy â€” not a direct redlining variable",tbl:"T413",section:"Geography & Environment",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)"],vars:["pct_forest","pct_cropland"],join:["median_household_income","violent_crime_rate"],sc:{emotional:9,relatability:8,surprise:7,tension:8,visual:9,data_ready:7,originality:7},vs:91,tags:"redlining race inequality environment trees climate heat island housing discrimination history Black segregation urban justice"},







{id:"crime_poverty",title:"Violent crime rate vs. median household income by state",sub:"The correlation is nearly perfect â€” less money, more violence, state by state.",type:"XREF",geo:"us_state",fmt:"Bivariate choropleth",tbl:"T340 Â· T727",section:"Law Enforcement Â· Income",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)","FBI Crime Data Explorer: UCR/NIBRS by state/agency (cde.ucr.cjis.gov â€” free)"],vars:["violent_crime_rate","median_household_income"],join:["pct_bachelors","state_unemployment_rate","pct_on_snap","rep_pct","murder_rate","total_transfers_per_capita"],sc:{emotional:9,relatability:9,surprise:6,tension:9,visual:9,data_ready:10,originality:6},vs:90,tags:"crime poverty income inequality violence murder policing race urban policy gun safety Trump law enforcement"},







{id:"education_vote",title:"College degree rate vs. 2024 presidential vote margin by state",sub:"The education-politics sort is now nearly perfectly linear across all 50 states.",type:"XREF",geo:"us_state",fmt:"Scatter plot",tbl:"T254 Â· T454",section:"Education Â· Elections",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)","MIT Election Lab: presidential/congressional results (electionlab.mit.edu â€” free)"],vars:["pct_bachelors","rep_pct","dem_pct","margin"],join:["median_household_income","violent_crime_rate","pct_voted_state","total_transfers_per_capita","state_unemployment_rate"],sc:{emotional:8,relatability:8,surprise:6,tension:9,visual:9,data_ready:10,originality:6},vs:88,tags:"education politics election Trump Biden Harris college degree polarization rural urban sorting demographics voting culture war"},







{id:"trade_deficit_country",title:"US trade deficit by country 2024",sub:"China -$298B. Mexico -$181B. Germany -$112B. Vietnam -$90B. The tariff target map.",type:"MAP",geo:"worldwide",fmt:"World choropleth",tbl:"T1310",section:"Foreign Commerce & Aid",ext:["World Bank Open Data: GDP, population, income by country (data.worldbank.org â€” free API)"],vars:["trade_balance_goods","trade_balance_services","current_account_balance"],join:["rd_pct_gdp","us_troops_overseas","population_per_sq_km"],sc:{emotional:8,relatability:7,surprise:7,tension:10,visual:9,data_ready:10,originality:7},vs:88,tags:"trade deficit China Mexico Germany Vietnam Japan tariffs Trump trade war imports exports economy manufacturing jobs MAGA"},







{id:"unmarried_births",title:"Percent of births to unmarried mothers by state 2023",sub:"Mississippi 57%. Utah 18%. The cultural geography of American family structure.",type:"MAP",geo:"us_state",fmt:"State choropleth",tbl:"T87",section:"Births Deaths Marriages",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)"],vars:["pct_births_unmarried"],join:["median_household_income","rep_pct","pct_bachelors","teen_birth_rate","pct_on_snap","birth_rate_state"],sc:{emotional:8,relatability:7,surprise:7,tension:9,visual:9,data_ready:10,originality:6},vs:88,tags:"births family marriage race poverty culture religion South politics abortion demographics inequality conservative liberal"},







{id:"teen_birth_education",title:"Teen birth rate vs. educational attainment by state",sub:"One of the tightest correlations in American social data.",type:"XREF",geo:"us_state",fmt:"Bivariate choropleth",tbl:"T86 Â· T254",section:"Births Deaths Â· Education",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)"],vars:["teen_birth_rate","pct_bachelors"],join:["median_household_income","rep_pct","pct_births_unmarried","pct_on_snap"],sc:{emotional:8,relatability:7,surprise:6,tension:8,visual:8,data_ready:10,originality:7},vs:87,tags:"teen pregnancy education poverty rural South race inequality sex education policy abortion healthcare demographics"},







{id:"bridges_condition",title:"Percent of bridges in poor structural condition by state 2024",sub:"Rhode Island 15%. Iowa 19%. West Virginia 18%. The infrastructure anxiety map.",type:"MAP",geo:"us_state",fmt:"State choropleth",tbl:"T1126",section:"Transportation",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)"],vars:["pct_bridges_poor","total_bridges"],join:["total_transfers_per_capita","state_gdp_per_capita","rep_pct"],sc:{emotional:8,relatability:8,surprise:7,tension:6,visual:9,data_ready:10,originality:6},vs:86,tags:"infrastructure bridges roads transportation safety government federal spending Iowa West Virginia Rhode Island crumbling Biden"},







{id:"car_insurance_cpi",title:"Motor vehicle insurance CPI 2000â€“2024 â€” the silent squeeze",sub:"Tripled in 24 years â€” index 257 to 843. The cost-of-living story nobody charts.",type:"CHART",geo:"us_national",fmt:"Line chart",tbl:"T770",section:"Prices",ext:["FRED: any national economic time series (fred.stlouisfed.org â€” free API)","BLS national data: employment, wages, CPI (bls.gov â€” free API)"],vars:["motor_vehicle_insurance_cpi","all_items_cpi"],join:["gasoline_cpi","housing_cpi","food_at_home_cpi"],sc:{emotional:8,relatability:9,surprise:9,tension:5,visual:8,data_ready:10,originality:9},vs:86,tags:"car insurance inflation CPI transportation cost of living budget household prices squeeze economy auto"},







{id:"egg_price_cpi",title:"Egg prices vs. overall food inflation 2019â€“2024",sub:"Egg CPI up 147%. Overall food up 27%. The most-shared grocery chart in America.",type:"CHART",geo:"us_national",fmt:"Line chart",tbl:"T770",section:"Prices",ext:["FRED: any national economic time series (fred.stlouisfed.org â€” free API)","BLS national data: employment, wages, CPI (bls.gov â€” free API)"],vars:["eggs_cpi","food_at_home_cpi","all_items_cpi"],join:["beef_and_veal_cpi","poultry_cpi","cereals_bakery_cpi","dairy_cpi"],sc:{emotional:8,relatability:10,surprise:8,tension:6,visual:8,data_ready:10,originality:7},vs:86,tags:"eggs inflation food prices grocery CPI 2023 2024 viral cost of living kitchen budget household anger grocery store"},







{id:"snap_enrollment",title:"SNAP food stamp enrollment rate by state 2023",sub:"11.7% of all Americans live in a SNAP household. The geography of hunger.",type:"MAP",geo:"us_state",fmt:"State choropleth",tbl:"T576",section:"Social Insurance",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)"],vars:["pct_on_snap","pct_on_medicaid","snap_households"],join:["rep_pct","total_transfers_per_capita","median_household_income","violent_crime_rate","pct_births_unmarried"],sc:{emotional:8,relatability:7,surprise:6,tension:9,visual:8,data_ready:10,originality:5},vs:85,tags:"SNAP food stamps poverty welfare hunger race politics Trump cuts benefits government Mississippi inequality rural Black"},







{id:"household_wealth_inequality",title:"Share of financial assets owned by US families by income quintile",sub:"Top 10% own 56% of all stocks. Bottom 20%: only 7% own any financial asset.",type:"CHART",geo:"us_national",fmt:"Bar chart",tbl:"T1207",section:"Banking Finance Insurance",ext:["FRED: any national economic time series (fred.stlouisfed.org â€” free API)","BLS national data: employment, wages, CPI (bls.gov â€” free API)"],vars:["pct_families_own_stocks","pct_families_own_retirement","median_stock_value","pct_families_own_any_asset"],join:["corporate_profits","income_tax_after_credits","credit_card_rate_all_accounts"],sc:{emotional:9,relatability:8,surprise:7,tension:9,visual:9,data_ready:10,originality:6},vs:85,tags:"wealth inequality stocks retirement savings income rich poor class divide economy Federal Reserve Wall Street billionaires"},







{id:"irs_audit_collapse",title:"IRS corporate audit rate collapse 2015â€“2022",sub:"Audit rate: 1.0% â†’ 0.2%. Recommended taxes dropped from $17.6B to $48M.",type:"CHART",geo:"us_national",fmt:"Line chart",tbl:"T794",section:"Business Enterprise",ext:["FRED: any national economic time series (fred.stlouisfed.org â€” free API)","BLS national data: employment, wages, CPI (bls.gov â€” free API)"],vars:["corp_audit_rate","recommended_additional_tax"],join:["corporate_profits","income_tax_after_credits"],sc:{emotional:8,relatability:7,surprise:9,tension:8,visual:8,data_ready:10,originality:9},vs:85,tags:"IRS audit tax corporations enforcement inequality rich wealth loopholes Trump Biden Congress cuts defunding enforcement"},







{id:"childcare_cpi",title:"Day care and preschool CPI 2000â€“2024 vs. overall inflation",sub:"Childcare cost up 136% since 2000. The inflation that forces parents out of the workforce.",type:"CHART",geo:"us_national",fmt:"Line chart",tbl:"T770",section:"Prices",ext:["FRED: any national economic time series (fred.stlouisfed.org â€” free API)","BLS national data: employment, wages, CPI (bls.gov â€” free API)"],vars:["daycare_preschool_cpi","all_items_cpi"],join:["female_lfp_rate","median_household_income","college_tuition_cpi"],sc:{emotional:9,relatability:9,surprise:7,tension:6,visual:8,data_ready:10,originality:8},vs:85,tags:"childcare daycare preschool cost inflation working parents women workforce economy inequality CPI family budget squeeze"},







{id:"voter_income",title:"Voter turnout vs. median household income by state 2024",sub:"The richer the state, the more people vote. Minnesota always breaks the rule.",type:"XREF",geo:"us_state",fmt:"Scatter plot",tbl:"T449 Â· T727",section:"Elections Â· Income",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)","MIT Election Lab: presidential/congressional results (electionlab.mit.edu â€” free)"],vars:["pct_voted_state","pct_registered_state","median_household_income"],join:["pct_bachelors","rep_pct","state_unemployment_rate","total_transfers_per_capita"],sc:{emotional:7,relatability:8,surprise:6,tension:8,visual:8,data_ready:10,originality:6},vs:85,tags:"voting turnout income democracy inequality suppression elections Trump politics Minnesota Wisconsin Mississippi Texas"},







{id:"worldwide_migration",title:"Net migration rate by country 1990â€“2024",sub:"Ukraine -205/1,000 in 2022. Cuba -43. Venezuela -66. Syria +46. The crisis, mapped.",type:"MAP",geo:"worldwide",fmt:"World choropleth",tbl:"T1360",section:"International Statistics",ext:["World Bank Open Data: GDP, population, income by country (data.worldbank.org â€” free API)"],vars:["net_migration_rate"],join:["population_pct_change_2020_2025","birth_rate","population_per_sq_km"],sc:{emotional:8,relatability:7,surprise:8,tension:7,visual:8,data_ready:10,originality:6},vs:85,tags:"migration immigration refugees Ukraine Russia war Syria Venezuela Cuba Iran Middle East Latin America Europe asylum border"},







{id:"home_price_index",title:"Single-family home price index by state 2005â€“2024",sub:"Montana +737. Colorado +697. Illinois +310. The housing divergence of the decade.",type:"MAP",geo:"us_state",fmt:"State choropleth",tbl:"T771",section:"Prices",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)"],vars:["home_price_index_2024","home_price_pct_change_2005_2024"],join:["housing_permits_total","median_household_income","mortgage_delinquency_rate"],sc:{emotional:8,relatability:9,surprise:8,tension:7,visual:9,data_ready:10,originality:5},vs:84,tags:"housing home prices real estate affordability Montana Colorado Florida Idaho Tennessee mortgage cost of living inflation"},







{id:"counties_lost_pop",title:"US counties that lost 20%+ of population since 1950",sub:"Over 800 counties have lost at least a fifth of their people. Rural America is hollowing out.",type:"MAP",geo:"us_county",fmt:"County choropleth",tbl:"Population PDF",section:"Population",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by county (bls.gov â€” free)"],vars:["population_pct_change_1950_2020"],join:["violent_crime_rate","state_unemployment_rate","pct_on_snap","total_transfers_per_capita"],sc:{emotional:8,relatability:7,surprise:7,tension:7,visual:9,data_ready:8,originality:7},vs:84,tags:"population rural decline depopulation coal agriculture manufacturing Appalachia Great Plains poverty crisis brain drain"},







{id:"airports_ontime",title:"Best and worst major US airports for on-time performance 2024",sub:"SFO worst. Salt Lake City best. Every frequent flyer has a hot take.",type:"RANK",geo:"top_n_list",fmt:"Ranked list",tbl:"T1110",section:"Transportation",ext:[],vars:["pct_ontime_arrivals","pct_ontime_departures"],join:["passengers_enplaned"],sc:{emotional:6,relatability:10,surprise:7,tension:3,visual:10,data_ready:10,originality:6},vs:84,tags:"airports travel flying airlines delays on-time SFO LAX Atlanta Chicago Dallas consumer transportation"},







{id:"worldwide_shrinking",title:"Countries losing the most population 2020â€“2025",sub:"Ukraine -16%. Cuba -9.6%. Romania -5.3%. Niger +20%. The civilizational demographic split.",type:"RANK",geo:"worldwide",fmt:"Ranked list",tbl:"International Statistics",section:"International Statistics",ext:["World Bank Open Data: GDP, population, income by country (data.worldbank.org â€” free API)"],vars:["population_pct_change_2020_2025"],join:["net_migration_rate","birth_rate","population_per_sq_km"],sc:{emotional:8,relatability:6,surprise:8,tension:7,visual:9,data_ready:10,originality:8},vs:84,tags:"population decline Ukraine war Russia Cuba Romania emigration demographics birth rate aging crisis Syria Latin America Europe"},







{id:"hospital_vs_insurance_cpi",title:"Hospital services CPI vs. health insurance CPI 2000â€“2024",sub:"Hospital CPI hit 414. Insurance CPI: 143. The gap between cost and coverage, charted.",type:"CHART",geo:"us_national",fmt:"Line chart",tbl:"T770",section:"Prices",ext:["FRED: any national economic time series (fred.stlouisfed.org â€” free API)","BLS national data: employment, wages, CPI (bls.gov â€” free API)"],vars:["hospital_services_cpi","health_insurance_cpi","physicians_services_cpi","prescription_drugs_cpi"],join:["per_capita_health_spending","total_medicare","nursing_homes_cpi"],sc:{emotional:8,relatability:8,surprise:8,tension:7,visual:8,data_ready:10,originality:8},vs:83,tags:"healthcare hospital insurance CPI inflation cost medical bills poverty access crisis ACA Obamacare Biden Trump premium"},







{id:"per_pupil_spending",title:"Per-pupil public school spending by state 2023",sub:"New York $31K. Idaho $10K. Same country, same Constitution, 3x funding gap.",type:"MAP",geo:"us_state",fmt:"State choropleth",tbl:"T258",section:"Education",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)"],vars:["expenditure_per_pupil","revenue_federal_pct","revenue_local_pct"],join:["pct_bachelors","avg_teacher_salary","median_household_income","rep_pct"],sc:{emotional:7,relatability:9,surprise:6,tension:7,visual:9,data_ready:10,originality:5},vs:83,tags:"education schools spending funding inequality children teachers taxes New York Idaho Mississippi parents policy"},







{id:"ports_tonnage",title:"Top 30 US ports by cargo tonnage 2023",sub:"Houston: 309M tons. South Louisiana: 218M. The Gulf Coast dominance surprises everyone.",type:"RANK",geo:"top_n_list",fmt:"Ranked list",tbl:"T1122",section:"Transportation",ext:[],vars:["port_total_tons","port_domestic_tons","port_foreign_tons"],join:["port_total_teus"],sc:{emotional:5,relatability:6,surprise:9,tension:2,visual:10,data_ready:10,originality:8},vs:83,tags:"ports shipping cargo Houston supply chain trade Gulf Coast oil Louisiana infrastructure economy imports exports"},







{id:"top50_airports",title:"Top 50 US airports by passenger traffic 2024",sub:"Atlanta #1 by a wide margin. Charlotte jumped to #7. The hub geography of American aviation.",type:"RANK",geo:"top_n_list",fmt:"Ranked list",tbl:"T1112",section:"Transportation",ext:[],vars:["passengers_enplaned"],join:["pct_ontime_arrivals"],sc:{emotional:6,relatability:9,surprise:6,tension:2,visual:10,data_ready:10,originality:5},vs:83,tags:"airports travel aviation Atlanta Dallas Denver Chicago Los Angeles New York flying passengers transportation hub"},







{id:"solar_noon",title:"Where solar noon actually matches clock noon across the US",sub:"Chicago: sun peaks at 12:53pm. Western Indiana: 1:27pm. Time zones are a geographic fiction.",type:"MAP",geo:"us_state",fmt:"Special map",proxy:true,proxyNote:"Derived from longitude and timezone boundaries â€” not a direct ProQuest variable",tbl:"Geography & Environment PDF",section:"Geography & Environment",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)"],vars:["mean_elevation","border_miles"],join:[],sc:{emotional:5,relatability:8,surprise:10,tension:2,visual:10,data_ready:7,originality:10},vs:83,tags:"time zones sun solar geography weird surprising science nature astronomy maps daylight strange curiosity"},







{id:"per_pupil_top50",title:"Per-pupil spending at the 50 largest US school districts",sub:"NYC $37K per student. Some Sunbelt districts under $9K. The inequality is inside cities too.",type:"RANK",geo:"top_n_list",fmt:"Ranked list",tbl:"T261",section:"Education",ext:[],vars:["expenditure_per_pupil","district_enrollment"],join:["avg_teacher_salary","pct_bachelors"],sc:{emotional:7,relatability:8,surprise:7,tension:6,visual:9,data_ready:10,originality:6},vs:81,tags:"education schools spending equity New York Utah funding children taxpayers inequality districts property tax policy"},







{id:"student_loan_growth",title:"Federal student loan debt outstanding 2000â€“2024",sub:"$1.78 trillion. From near-zero to a national crisis in 24 years.",type:"CHART",geo:"us_national",fmt:"Area chart",tbl:"T1222",section:"Banking Finance Insurance",ext:["FRED: any national economic time series (fred.stlouisfed.org â€” free API)","BLS national data: employment, wages, CPI (bls.gov â€” free API)"],vars:["student_loans_outstanding","total_consumer_credit"],join:["college_tuition_cpi","daycare_preschool_cpi","credit_card_rate_all_accounts"],sc:{emotional:9,relatability:9,surprise:5,tension:8,visual:8,data_ready:10,originality:4},vs:81,tags:"student loans debt college education Biden forgiveness crisis millennials Gen Z economy inequality federal government"},







{id:"xref_teacher_outcomes",title:"Teacher salary vs. college degree attainment rate by state",sub:"Do states that pay teachers more produce more college graduates? The answer is real but messy.",type:"XREF",geo:"us_state",fmt:"Scatter plot",tbl:"T268 Â· T254",section:"Education",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)"],vars:["avg_teacher_salary","pct_bachelors"],join:["expenditure_per_pupil","median_household_income","rep_pct"],sc:{emotional:7,relatability:8,surprise:7,tension:6,visual:8,data_ready:10,originality:7},vs:81,tags:"teachers education salary outcomes college degree spending inequality policy schools performance"},







{id:"energy_per_capita",title:"Energy consumption per capita by state 2023",sub:"Louisiana: 908 MMBtu. Rhode Island: 166. A 5.5x gap within one country.",type:"MAP",geo:"us_state",fmt:"State choropleth",tbl:"T975",section:"Energy & Utilities",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)","EIA State Energy Data System: production + consumption by state (eia.gov â€” free API)"],vars:["energy_consumption_per_capita"],join:["renewable_energy_share","coal_production_index","state_gdp_per_capita","rep_pct"],sc:{emotional:6,relatability:7,surprise:8,tension:7,visual:9,data_ready:10,originality:6},vs:82,tags:"energy climate carbon fossil fuels Louisiana Texas Wyoming electricity consumption emissions environment oil gas industrial"},







{id:"renewable_state",title:"Renewable energy share of total consumption by state 2023",sub:"Iowa near 30% wind. Washington all hydro. Wyoming still 97% fossil. The split is geographic.",type:"MAP",geo:"us_state",fmt:"State choropleth",tbl:"T976",section:"Energy & Utilities",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)","EIA State Energy Data System: production + consumption by state (eia.gov â€” free API)"],vars:["renewable_energy_share","hydroelectric_consumption"],join:["coal_production_index","energy_consumption_per_capita","rep_pct"],sc:{emotional:7,relatability:7,surprise:7,tension:7,visual:9,data_ready:10,originality:5},vs:82,tags:"renewable energy wind solar hydro climate green Iowa Washington Texas coal fossil fuels transition environment Biden Trump"},







{id:"troops_overseas",title:"US military personnel stationed overseas by country 2024",sub:"Japan 51K. Germany 35K. South Korea 23K. America's permanent military geography.",type:"MAP",geo:"worldwide",fmt:"World choropleth",tbl:"T549",section:"National Security & Veterans",ext:["World Bank Open Data: GDP, population, income by country (data.worldbank.org â€” free API)"],vars:["us_troops_overseas"],join:["defense_budget_total","total_deaths","wounded_in_action","trade_balance_goods"],sc:{emotional:7,relatability:6,surprise:7,tension:8,visual:9,data_ready:10,originality:7},vs:82,tags:"military troops overseas Japan Germany South Korea NATO war defense imperialism foreign policy budget veterans Iraq Afghanistan"},







{id:"teacher_salary",title:"Average public school teacher salary by state 2024",sub:"California $101K. Mississippi $54K. Same job, nearly 2x pay difference.",type:"MAP",geo:"us_state",fmt:"State choropleth",tbl:"T268",section:"Education",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)"],vars:["avg_teacher_salary","teacher_count"],join:["expenditure_per_pupil","pct_bachelors","median_household_income","rep_pct"],sc:{emotional:7,relatability:8,surprise:6,tension:7,visual:9,data_ready:10,originality:5},vs:81,tags:"teachers education salary pay inequality Mississippi California New York unions public schools policy workforce rural budget"},







{id:"cpi_housing_city",title:"Housing cost CPI by major US city 2024",sub:"San Diego index 455. Chicago 311. Miami 394. The cost-of-living divide, city by city.",type:"MAP",geo:"us_city",fmt:"Dot map",tbl:"T769",section:"Prices",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)"],vars:["housing_cpi_city","rent_primary_residence_cpi"],join:["home_price_index_2024","median_household_income"],sc:{emotional:7,relatability:9,surprise:7,tension:5,visual:9,data_ready:10,originality:6},vs:80,tags:"housing cost of living CPI inflation city urban rent prices San Diego San Francisco Miami New York Chicago crisis economy"},







{id:"fishing_ports",title:"Top 40 US commercial fishing ports by landed catch volume 2023",sub:"Dutch Harbor AK alone lands 780M lbs. The fishing economy is almost entirely Alaska.",type:"RANK",geo:"top_n_list",fmt:"Ranked list",tbl:"T945",section:"Forestry Fishing & Mining",ext:[],vars:["port_catch_lbs","port_catch_value"],join:["species_landed_value"],sc:{emotional:5,relatability:7,surprise:9,tension:2,visual:10,data_ready:10,originality:9},vs:80,tags:"fishing seafood ports Alaska Dutch Harbor lobster shrimp commercial fishing food ocean supply chain New Bedford industry"},







{id:"worldwide_pop_growth",title:"World population growth rate by country 2020â€“2025",sub:"Niger +20%. South Sudan +26%. Ukraine -16%. The demographic divergence is civilizational.",type:"MAP",geo:"worldwide",fmt:"World choropleth",tbl:"International Statistics",section:"International Statistics",ext:["World Bank Open Data: GDP, population, income by country (data.worldbank.org â€” free API)"],vars:["population_pct_change_2020_2025"],join:["net_migration_rate","birth_rate","population_per_sq_km"],sc:{emotional:7,relatability:6,surprise:7,tension:5,visual:9,data_ready:10,originality:5},vs:79,tags:"population growth demographics Africa Europe Ukraine Russia war fertility decline aging immigration climate future global Niger"},







{id:"theme_parks",title:"Top 15 US theme parks by attendance 2023",sub:"Disney holds 9 of 15. Magic Kingdom alone draws 17.7M â€” more than many countries.",type:"RANK",geo:"top_n_list",fmt:"Ranked list",tbl:"T1271",section:"Arts Recreation & Travel",ext:[],vars:["annual_attendance"],join:[],sc:{emotional:5,relatability:9,surprise:5,tension:2,visual:10,data_ready:10,originality:5},vs:79,tags:"theme parks Disney Universal Orlando Anaheim entertainment tourism Florida California attendance vacation family economy"},







{id:"credit_card_rates",title:"Credit card interest rates 2000â€“2024",sub:"Average rate: 14.9% in 2000, 22.9% in 2024. The slow debt trap tightening.",type:"CHART",geo:"us_national",fmt:"Line chart",tbl:"T1223",section:"Banking Finance Insurance",ext:["FRED: any national economic time series (fred.stlouisfed.org â€” free API)","BLS national data: employment, wages, CPI (bls.gov â€” free API)"],vars:["credit_card_rate_all_accounts","credit_card_rate_assessed"],join:["total_consumer_credit","student_loans_outstanding","auto_loan_rate"],sc:{emotional:8,relatability:9,surprise:6,tension:7,visual:8,data_ready:10,originality:5},vs:79,tags:"credit cards debt interest rates Federal Reserve inflation poverty banks consumer finance household debt economy trap"},







{id:"sports_attendance",title:"Most-attended live sports events in America 2025",sub:"High school sports beat MLB in total attendance. Your neighbor's kid's game is #1.",type:"RANK",geo:"us_national",fmt:"Ranked list",tbl:"T1273",section:"Arts Recreation & Travel",ext:["FRED: any national economic time series (fred.stlouisfed.org â€” free API)","BLS national data: employment, wages, CPI (bls.gov â€” free API)"],vars:["sports_attendance_12mo"],join:[],sc:{emotional:6,relatability:9,surprise:8,tension:2,visual:9,data_ready:10,originality:7},vs:79,tags:"sports attendance live baseball NFL NBA college high school fans America culture entertainment recreation surprising"},







{id:"us_trade_deficit",title:"US current account deficit 2000â€“2024",sub:"$1.185 trillion deficit in 2024 â€” the largest in US history.",type:"CHART",geo:"us_national",fmt:"Area chart",tbl:"T1306",section:"Foreign Commerce & Aid",ext:["FRED: any national economic time series (fred.stlouisfed.org â€” free API)","BLS national data: employment, wages, CPI (bls.gov â€” free API)"],vars:["balance_on_goods","balance_on_services","current_account_balance"],join:["trade_balance_goods"],sc:{emotional:7,relatability:6,surprise:7,tension:9,visual:8,data_ready:10,originality:6},vs:79,tags:"trade deficit current account imports exports China tariffs Trump Biden economy manufacturing jobs globalization history"},







{id:"fish_species_value",title:"Most valuable US commercial fish species by landed value 2023",sub:"Lobster $633M. Sea scallop $360M. Pollock $524M. The seafood economy ranked.",type:"RANK",geo:"top_n_list",fmt:"Ranked list",tbl:"T944",section:"Forestry Fishing & Mining",ext:[],vars:["species_landed_value","species_landed_lbs"],join:["port_catch_lbs"],sc:{emotional:5,relatability:7,surprise:8,tension:2,visual:10,data_ready:10,originality:8},vs:79,tags:"fishing seafood lobster scallop pollock shrimp Alaska commercial fishing food ocean value economy industry"},







{id:"war_casualties",title:"US military casualties by post-9/11 conflict",sub:"Iraq: 4,419 deaths, 31,993 wounded. Afghanistan: 2,350 deaths, 20,149 wounded.",type:"CHART",geo:"us_national",fmt:"Bar chart",tbl:"T548",section:"National Security & Veterans",ext:["FRED: any national economic time series (fred.stlouisfed.org â€” free API)","BLS national data: employment, wages, CPI (bls.gov â€” free API)"],vars:["total_deaths","hostile_deaths","wounded_in_action"],join:["defense_budget_total","us_troops_overseas"],sc:{emotional:9,relatability:7,surprise:5,tension:8,visual:8,data_ready:10,originality:5},vs:79,tags:"war military casualties Iraq Afghanistan ISIS 9/11 terrorism veterans soldiers killed wounded Trump Biden Bush Obama cost"},







{id:"median_income_state",title:"Median household income by state 2023",sub:"Maryland $98K. Mississippi $54K. The income gap within one country.",type:"MAP",geo:"us_state",fmt:"State choropleth",tbl:"T727",section:"Income Expenditures Poverty",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)"],vars:["median_household_income","pct_under_25k","pct_over_200k"],join:["violent_crime_rate","pct_bachelors","rep_pct","teen_birth_rate","pct_on_snap","pct_voted_state","state_unemployment_rate","total_transfers_per_capita","avg_teacher_salary","expenditure_per_pupil"],sc:{emotional:7,relatability:9,surprise:4,tension:6,visual:9,data_ready:10,originality:3},vs:78,tags:"income poverty inequality economy wages wealth Maryland Mississippi race policy cost of living taxes class"},







{id:"corporate_profits_tax",title:"US corporate profits and effective tax rate 2000â€“2024",sub:"$2.85T in profits in 2024. Effective rate fell from ~36% to ~19% after 2017.",type:"CHART",geo:"us_national",fmt:"Line chart",tbl:"T793",section:"Business Enterprise",ext:["FRED: any national economic time series (fred.stlouisfed.org â€” free API)","BLS national data: employment, wages, CPI (bls.gov â€” free API)"],vars:["corporate_profits","income_tax_after_credits"],join:["corp_audit_rate","pct_families_own_stocks"],sc:{emotional:8,relatability:6,surprise:7,tension:8,visual:7,data_ready:10,originality:6},vs:78,tags:"corporate profits taxes inequality economy wealth CEO stock buybacks workers wages Trump tax cut corporations business IRS"},







{id:"gasoline_by_city",title:"Regular gasoline prices by major US city 2024",sub:"San Francisco $4.65. Houston $2.83. The gas price geography that moves elections.",type:"MAP",geo:"us_city",fmt:"Dot map",tbl:"T773",section:"Prices",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)"],vars:["gasoline_price_regular"],join:["energy_consumption_per_capita","rep_pct"],sc:{emotional:7,relatability:10,surprise:5,tension:6,visual:9,data_ready:10,originality:4},vs:78,tags:"gas prices gasoline oil inflation cost of living city California Texas elections voting driving transportation energy"},







{id:"ports_containers",title:"Top 30 US container ports by TEU volume 2023",sub:"Savannah is now #4. The East Coast port shift is the freight story of the decade.",type:"RANK",geo:"top_n_list",fmt:"Ranked list",tbl:"T1123",section:"Transportation",ext:[],vars:["port_total_teus","port_inbound_teus"],join:["port_total_tons"],sc:{emotional:4,relatability:5,surprise:8,tension:2,visual:10,data_ready:10,originality:7},vs:77,tags:"ports shipping containers supply chain Savannah Los Angeles New York Long Beach trade imports exports Amazon logistics"},







{id:"metro_unemployment",title:"Highest and lowest unemployment metro areas 2024",sub:"Fresno 7.2%. South Dakota metros under 2%. The jobs divide no state map shows.",type:"RANK",geo:"us_metro",fmt:"Ranked list",tbl:"T630",section:"Labor Force",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by metro (apps.bea.gov â€” free)","BLS LAUS: unemployment + labor force by metro (bls.gov â€” free)"],vars:["metro_unemployment_rate"],join:["median_household_income","pct_bachelors"],sc:{emotional:6,relatability:7,surprise:6,tension:5,visual:9,data_ready:10,originality:6},vs:77,tags:"unemployment jobs economy metro areas cities Fresno California rural poverty labor market recession wages workforce"},







{id:"waterway_freight",title:"Freight tonnage on major US waterways 2023",sub:"The Mississippi system: 567M tons. America's invisible inland interstate.",type:"RANK",geo:"top_n_list",fmt:"Ranked list",tbl:"T1120",section:"Transportation",ext:[],vars:["waterway_freight_tons"],join:["port_total_tons"],sc:{emotional:5,relatability:5,surprise:8,tension:2,visual:9,data_ready:10,originality:8},vs:77,tags:"rivers waterways freight Mississippi Ohio shipping infrastructure grain coal oil agriculture trade barge supply chain"},







{id:"farmland_loss_state",title:"Farmland lost by state 2017â€“2022",sub:"Every state lost farmland. Texas shed 17,000 farms in 5 years.",type:"MAP",geo:"us_state",fmt:"State choropleth",tbl:"T869",section:"Agriculture",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)","USDA ERS: food environment, rural classification, farm income (ers.usda.gov â€” free)"],vars:["farms_count_2022","land_in_farms_2022"],join:["pct_cropland","median_household_income","farm_value_land"],sc:{emotional:7,relatability:6,surprise:7,tension:6,visual:9,data_ready:10,originality:7},vs:77,tags:"farming agriculture food land loss development rural food security Texas Iowa California crisis sprawl corporate farms environment"},







{id:"xref_medicare_income",title:"Medicare enrollment rate vs. per capita income by state",sub:"Poorer, older states carry far higher Medicare loads per working-age taxpayer.",type:"XREF",geo:"us_state",fmt:"Bivariate choropleth",tbl:"T150 Â· T723",section:"Health Â· Income",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)","CDC WONDER: mortality + disease rates by county/state (wonder.cdc.gov â€” free)"],vars:["total_medicare","real_per_capita_income"],join:["total_transfers_per_capita","pct_on_medicaid"],sc:{emotional:7,relatability:7,surprise:6,tension:7,visual:8,data_ready:10,originality:7},vs:79,tags:"Medicare healthcare aging income elderly poverty state funding federal spending insurance hospital"},







{id:"xref_housing_permits_pop",title:"Housing permit growth vs. population inflow by state 2020â€“2024",sub:"States building the most housing are getting the most people. Cause or effect?",type:"XREF",geo:"us_state",fmt:"Scatter plot",tbl:"T1011 Â· Population PDF",section:"Construction Â· Population",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)"],vars:["housing_permits_total","population_pct_change"],join:["home_price_index_2024","median_household_income"],sc:{emotional:7,relatability:8,surprise:6,tension:6,visual:8,data_ready:9,originality:7},vs:78,tags:"housing permits construction migration population growth Florida Texas California New York affordability supply demand"},







{id:"disability_employment",title:"Employment rate with vs. without a disability by state",sub:"24.5% labor force participation with a disability vs. 68.1% without.",type:"MAP",geo:"us_state",fmt:"State choropleth",tbl:"T626",section:"Labor Force",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)"],vars:["disability_lfp_rate","disability_unemployment"],join:["state_unemployment_rate","pct_on_snap","median_household_income"],sc:{emotional:7,relatability:7,surprise:5,tension:5,visual:8,data_ready:10,originality:7},vs:76,tags:"disability employment accessibility ADA inequality healthcare policy workers inclusion unemployment Social Security SSI poverty"},







{id:"farm_concentration",title:"Top 5% of farms produce 78% of all food sold in America",sub:"165K mega-farms: $425B in sales. 1.3M small farms: under $1B combined.",type:"CHART",geo:"us_national",fmt:"Bar chart",tbl:"T871",section:"Agriculture",ext:["FRED: any national economic time series (fred.stlouisfed.org â€” free API)","BLS national data: employment, wages, CPI (bls.gov â€” free API)","USDA ERS: food environment, rural classification, farm income (ers.usda.gov â€” free)"],vars:["farms_count_2022","farm_sales_by_size"],join:["farm_value_land","pct_cropland","land_in_farms_2022"],sc:{emotional:8,relatability:7,surprise:9,tension:7,visual:9,data_ready:10,originality:8},vs:76,tags:"agriculture farming inequality corporate farms food concentration consolidation economy rural small farms monopoly agribusiness"},







{id:"retired_military_state",title:"Retired military pension payments by state 2022",sub:"Florida: $557M/month. Virginia: $499M. The military retirement economy is concentrated.",type:"MAP",geo:"us_state",fmt:"State choropleth",tbl:"T547",section:"National Security & Veterans",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)"],vars:["military_pension_monthly","retired_military_count"],join:["total_transfers_per_capita","rep_pct","veterans_benefits"],sc:{emotional:5,relatability:6,surprise:7,tension:5,visual:9,data_ready:10,originality:7},vs:74,tags:"veterans military retirement pension Florida Texas Virginia North Carolina benefits federal spending base geography"},







{id:"fertility_below_replacement",title:"US total fertility rate by race 2010â€“2023",sub:"Every racial group in America is now below 2.1 replacement level.",type:"CHART",geo:"us_national",fmt:"Line chart",tbl:"T85",section:"Births Deaths Marriages",ext:["FRED: any national economic time series (fred.stlouisfed.org â€” free API)","BLS national data: employment, wages, CPI (bls.gov â€” free API)"],vars:["total_fertility_rate_by_race"],join:["birth_rate_state","population_pct_change","pct_births_unmarried"],sc:{emotional:7,relatability:7,surprise:8,tension:7,visual:8,data_ready:10,originality:6},vs:73,tags:"fertility birth rate population demographics race Hispanic Black White Asian decline aging immigration future replacement"},







{id:"coal_decline",title:"US coal production index 1990â€“2024",sub:"Index fell from 145 to 67 in 35 years. The energy transition in one chart.",type:"CHART",geo:"us_national",fmt:"Area chart",tbl:"T950",section:"Forestry Fishing & Mining",ext:["FRED: any national economic time series (fred.stlouisfed.org â€” free API)","BLS national data: employment, wages, CPI (bls.gov â€” free API)"],vars:["coal_production_index","oil_gas_extraction_index"],join:["renewable_energy_share","energy_consumption_per_capita","rep_pct"],sc:{emotional:7,relatability:6,surprise:6,tension:7,visual:8,data_ready:10,originality:6},vs:73,tags:"coal energy climate transition Appalachia West Virginia Wyoming jobs rural decline fossil fuels renewable policy Trump Biden"},







{id:"newspaper_collapse",title:"Newspaper industry revenue collapse 2017â€“2022",sub:"Print advertising fell from $14B to under $11B in 5 years. Local news is dying.",type:"CHART",geo:"us_national",fmt:"Bar chart",tbl:"T1174",section:"Information & Communications",ext:["FRED: any national economic time series (fred.stlouisfed.org â€” free API)","BLS national data: employment, wages, CPI (bls.gov â€” free API)"],vars:["newspaper_print_revenue","newspaper_digital_revenue","newspaper_total_revenue"],join:[],sc:{emotional:7,relatability:7,surprise:5,tension:6,visual:8,data_ready:10,originality:6},vs:73,tags:"newspapers media journalism decline news deserts advertising digital local news democracy information publishing crisis"},







{id:"mortgage_delinquency",title:"Mortgage delinquency and foreclosure rates 2000â€“2024",sub:"2010: 9.3% delinquency. 2024: 4.0%. The scar of 2008 is still readable.",type:"CHART",geo:"us_national",fmt:"Line chart",tbl:"T1225",section:"Banking Finance Insurance",ext:["FRED: any national economic time series (fred.stlouisfed.org â€” free API)","BLS national data: employment, wages, CPI (bls.gov â€” free API)"],vars:["mortgage_delinquency_rate","foreclosure_rate_total"],join:["home_price_index_2024","home_equity_loans"],sc:{emotional:7,relatability:8,surprise:5,tension:6,visual:8,data_ready:10,originality:5},vs:72,tags:"mortgage delinquency foreclosure 2008 crisis housing debt banks subprime recovery economy homeowners financial"},







{id:"farmer_demographics",title:"Who are America's farmers? Race, age, and gender 2022",sub:"Average age: 58. 94% white. 64% male. Aging out with no succession plan.",type:"CHART",geo:"us_national",fmt:"Bar chart",tbl:"T872",section:"Agriculture",ext:["FRED: any national economic time series (fred.stlouisfed.org â€” free API)","BLS national data: employment, wages, CPI (bls.gov â€” free API)","USDA ERS: food environment, rural classification, farm income (ers.usda.gov â€” free)"],vars:["farmer_avg_age","farmer_pct_white","farmer_pct_male"],join:["farms_count_2022","land_in_farms_2022"],sc:{emotional:7,relatability:6,surprise:7,tension:5,visual:8,data_ready:10,originality:7},vs:74,tags:"farming agriculture demographics race age gender white diversity rural food crisis succession land small farms future"},







{id:"active_duty_gender",title:"US active duty military by branch and gender 1960â€“2024",sub:"Women are now 17.9% of the force â€” from near-zero to 230,000 in 60 years.",type:"CHART",geo:"us_national",fmt:"Area chart",tbl:"T545",section:"National Security & Veterans",ext:["FRED: any national economic time series (fred.stlouisfed.org â€” free API)","BLS national data: employment, wages, CPI (bls.gov â€” free API)"],vars:["active_duty_total","active_duty_female_pct"],join:["defense_budget_total","total_deaths"],sc:{emotional:6,relatability:7,surprise:6,tension:5,visual:8,data_ready:10,originality:5},vs:71,tags:"military women gender Army Navy Air Force Marines diversity history service defense equality armed forces demographics"},







{id:"xref_energy_gdp",title:"Energy consumption per capita vs. state GDP per capita",sub:"Louisiana consumes the most energy but doesn't produce the most GDP. The industrial subsidy.",type:"XREF",geo:"us_state",fmt:"Scatter plot",tbl:"T975 Â· T715",section:"Energy Â· Income",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)","EIA State Energy Data System: production + consumption by state (eia.gov â€” free API)"],vars:["energy_consumption_per_capita","state_gdp_per_capita"],join:["renewable_energy_share","coal_production_index"],sc:{emotional:5,relatability:5,surprise:8,tension:4,visual:8,data_ready:10,originality:8},vs:73,tags:"energy GDP economy industrial Louisiana Texas Wyoming efficiency carbon oil gas refining manufacturing"},







{id:"xref_farm_value_income",title:"Agricultural land value vs. median household income by state",sub:"Iowa farmland is worth $277B but median household income is $70K. Wealth doesn't reach farmers.",type:"XREF",geo:"us_state",fmt:"Scatter plot",tbl:"T869 Â· T727",section:"Agriculture Â· Income",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)","USDA ERS: food environment, rural classification, farm income (ers.usda.gov â€” free)"],vars:["farm_value_land","median_household_income"],join:["farms_count_2022","pct_cropland","land_in_farms_2022"],sc:{emotional:7,relatability:6,surprise:7,tension:5,visual:7,data_ready:10,originality:8},vs:75,tags:"agriculture farmland value income inequality Iowa California Texas wealth farmers rural economy land ownership"},







{id:"tobacco_cpi",title:"Tobacco CPI 2000â€“2024 â€” up 290%",sub:"Tobacco CPI: 395 â†’ 1,541. The most inflated consumer product in America.",type:"CHART",geo:"us_national",fmt:"Line chart",tbl:"T770",section:"Prices",ext:["FRED: any national economic time series (fred.stlouisfed.org â€” free API)","BLS national data: employment, wages, CPI (bls.gov â€” free API)"],vars:["tobacco_cpi","cigarette_cpi","all_items_cpi"],join:[],sc:{emotional:6,relatability:7,surprise:7,tension:4,visual:7,data_ready:10,originality:7},vs:70,tags:"tobacco smoking cigarettes CPI inflation price elasticity health public policy regulation tax behavior economics"},







{id:"home_equity_atm",title:"Home equity loan balances 2000â€“2024",sub:"Americans extracted $561B in home equity in 2024 â€” nearly back to pre-crisis levels.",type:"CHART",geo:"us_national",fmt:"Area chart",tbl:"T1224",section:"Banking Finance Insurance",ext:["FRED: any national economic time series (fred.stlouisfed.org â€” free API)","BLS national data: employment, wages, CPI (bls.gov â€” free API)"],vars:["home_equity_loans","total_mortgage_debt"],join:["home_price_index_2024","mortgage_delinquency_rate"],sc:{emotional:7,relatability:7,surprise:7,tension:5,visual:7,data_ready:10,originality:7},vs:73,tags:"home equity mortgage debt housing wealth borrowing 2008 crisis financial risk inflation real estate"},







{id:"foreign_jobs_state",title:"Jobs at foreign-owned US companies by state 2022",sub:"8.35M Americans work for foreign companies. Michigan saw the biggest jump since 2010.",type:"MAP",geo:"us_state",fmt:"State choropleth",tbl:"T1311",section:"Foreign Commerce & Aid",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)"],vars:["foreign_affiliate_employment"],join:["state_gdp_per_capita","state_unemployment_rate"],sc:{emotional:6,relatability:6,surprise:8,tension:5,visual:9,data_ready:10,originality:7},vs:76,tags:"foreign investment jobs economy manufacturing FDI companies multinational California Texas employment globalization trade"},







{id:"rd_pct_gdp_world",title:"R&D spending as % of GDP by country 2023",sub:"South Korea: 4.96%. US: 3.45%. China: 2.49%. Who is actually investing in the future?",type:"MAP",geo:"worldwide",fmt:"World choropleth",tbl:"T842",section:"Science & Technology",ext:["World Bank Open Data: GDP, population, income by country (data.worldbank.org â€” free API)"],vars:["rd_pct_gdp"],join:["us_troops_overseas","trade_balance_goods","population_pct_change_2020_2025"],sc:{emotional:6,relatability:5,surprise:7,tension:7,visual:9,data_ready:10,originality:6},vs:76,tags:"R&D research innovation technology South Korea China Germany Japan US GDP competitiveness economy future science tech war"},







{id:"national_forest_state",title:"National Forest System acres by state 2024",sub:"Alaska 22M acres. California 21M. 27 states have essentially none. Public land is a western story.",type:"MAP",geo:"us_state",fmt:"State choropleth",tbl:"T932",section:"Forestry Fishing & Mining",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)"],vars:["national_forest_acres"],join:["pct_forest","energy_consumption_per_capita"],sc:{emotional:5,relatability:6,surprise:7,tension:5,visual:9,data_ready:10,originality:6},vs:72,tags:"forests public land federal national forest environment wilderness logging timber recreation conservation western US Alaska"},







{id:"worldwide_pop_density",title:"World population density by country 2025",sub:"Monaco: 16,024/kmÂ². Singapore: 8,576. Mongolia: 2. The extremes of human geography.",type:"MAP",geo:"worldwide",fmt:"World choropleth",tbl:"International Statistics",section:"International Statistics",ext:["World Bank Open Data: GDP, population, income by country (data.worldbank.org â€” free API)"],vars:["population_per_sq_km"],join:["population_pct_change_2020_2025","net_migration_rate"],sc:{emotional:5,relatability:6,surprise:8,tension:3,visual:9,data_ready:10,originality:4},vs:74,tags:"population density cities Bangladesh Monaco Singapore Mongolia geography land urban rural overcrowding resources global"},







{id:"beef_vs_chicken_cpi",title:"Beef vs. chicken price inflation 2000â€“2024",sub:"Beef CPI: 423. Chicken CPI: 196. Beef got twice as expensive relative to chicken.",type:"CHART",geo:"us_national",fmt:"Line chart",tbl:"T770",section:"Prices",ext:["FRED: any national economic time series (fred.stlouisfed.org â€” free API)","BLS national data: employment, wages, CPI (bls.gov â€” free API)"],vars:["beef_and_veal_cpi","poultry_cpi","all_items_cpi"],join:["food_at_home_cpi","dairy_cpi"],sc:{emotional:7,relatability:9,surprise:7,tension:3,visual:8,data_ready:10,originality:7},vs:76,tags:"beef chicken inflation food prices grocery CPI meat protein budget household cost of living diet economics"}







,{id:"rent_vs_housing_cpi",title:"Rent CPI vs. owners' equivalent rent 2000â€“2024",sub:"Rent of primary residence CPI: 420. Owners' equivalent: 412. The shelter inflation nobody charts.",type:"CHART",geo:"us_national",fmt:"Line chart",tbl:"T770",section:"Prices",ext:["FRED: any national economic time series (fred.stlouisfed.org â€” free API)","BLS national data: employment, wages, CPI (bls.gov â€” free API)"],vars:["rent_primary_residence_cpi","housing_cpi"],join:["home_price_index_2024","mortgage_delinquency_rate"],sc:{emotional:8,relatability:9,surprise:7,tension:6,visual:8,data_ready:10,originality:7},vs:79,tags:"rent housing inflation CPI shelter cost of living housing crisis affordability landlords tenants ownership homeowners"}







,{id:"college_tuition_cpi_wages",title:"College tuition CPI vs. wage growth 2000â€“2024",sub:"Tuition CPI: 937. Average wage growth: ~250. You'd need to triple your salary to keep up.",type:"CHART",geo:"us_national",fmt:"Line chart",tbl:"T770",section:"Prices",ext:["FRED: any national economic time series (fred.stlouisfed.org â€” free API)","BLS national data: employment, wages, CPI (bls.gov â€” free API)"],vars:["college_tuition_cpi","all_items_cpi"],join:["student_loans_outstanding","pct_bachelors"],sc:{emotional:9,relatability:9,surprise:7,tension:7,visual:8,data_ready:10,originality:6},vs:82,tags:"college tuition inflation CPI wages earnings student debt crisis Gen Z millennials education cost university higher education"}







,{id:"prescription_drug_cpi",title:"Prescription drugs vs. hospital services CPI 2000â€“2024",sub:"Prescription drug CPI: 557. Hospital services: 414. Two very different healthcare inflation stories.",type:"CHART",geo:"us_national",fmt:"Line chart",tbl:"T770",section:"Prices",ext:["FRED: any national economic time series (fred.stlouisfed.org â€” free API)","BLS national data: employment, wages, CPI (bls.gov â€” free API)"],vars:["prescription_drugs_cpi","hospital_services_cpi","health_insurance_cpi"],join:["per_capita_health_spending","total_medicare"],sc:{emotional:8,relatability:8,surprise:7,tension:7,visual:8,data_ready:10,originality:7},vs:78,tags:"prescription drugs hospital healthcare CPI inflation cost insulin Medicare pharma Big Pharma prices policy"}







,{id:"food_away_vs_home_cpi",title:"Food away from home vs. food at home CPI 2000â€“2024",sub:"Restaurant food CPI: 369. Grocery food: 307. Eating out got relatively more expensive.",type:"CHART",geo:"us_national",fmt:"Line chart",tbl:"T770",section:"Prices",ext:["FRED: any national economic time series (fred.stlouisfed.org â€” free API)","BLS national data: employment, wages, CPI (bls.gov â€” free API)"],vars:["food_at_home_cpi","all_items_cpi"],join:["eggs_cpi","beef_and_veal_cpi"],sc:{emotional:7,relatability:9,surprise:6,tension:3,visual:8,data_ready:10,originality:6},vs:73,tags:"restaurant food inflation grocery CPI cooking eating out budget household cost of living tipping wages minimum wage"}







,{id:"wireless_vs_landline_cpi",title:"Wireless telephone vs. landline CPI 2000â€“2024",sub:"Wireless CPI: 47. Landline CPI: 157. The only consumer category that actually got cheaper.",type:"CHART",geo:"us_national",fmt:"Line chart",tbl:"T770",section:"Prices",ext:["FRED: any national economic time series (fred.stlouisfed.org â€” free API)","BLS national data: employment, wages, CPI (bls.gov â€” free API)"],vars:["all_items_cpi"],join:[],sc:{emotional:6,relatability:8,surprise:9,tension:2,visual:8,data_ready:10,originality:8},vs:72,tags:"wireless phones cell phone CPI deflation cheaper telecom technology inflation comparison cost of living"}







,{id:"water_sewer_cpi",title:"Water and sewerage CPI 2000â€“2024 â€” the quiet infrastructure crisis",sub:"Water/sewer CPI: 693. Garbage collection: 616. Infrastructure costs are quietly tripling utility bills.",type:"CHART",geo:"us_national",fmt:"Line chart",tbl:"T770",section:"Prices",ext:["FRED: any national economic time series (fred.stlouisfed.org â€” free API)","BLS national data: employment, wages, CPI (bls.gov â€” free API)"],vars:["all_items_cpi"],join:["pct_bridges_poor"],sc:{emotional:7,relatability:7,surprise:8,tension:5,visual:7,data_ready:10,originality:9},vs:74,tags:"water sewer utilities CPI inflation infrastructure municipalities budget local government property tax aging pipes"}







,{id:"consumer_credit_breakdown",title:"Student loans vs. auto loans vs. credit cards 2000â€“2024",sub:"$1.78T student loans. $1.57T auto. $1.32T credit cards. The three pillars of American consumer debt.",type:"CHART",geo:"us_national",fmt:"Area chart",tbl:"T1222",section:"Banking Finance Insurance",ext:["FRED: any national economic time series (fred.stlouisfed.org â€” free API)","BLS national data: employment, wages, CPI (bls.gov â€” free API)"],vars:["student_loans_outstanding","total_consumer_credit","credit_card_rate_all_accounts"],join:["median_household_income","pct_families_own_any_asset"],sc:{emotional:8,relatability:9,surprise:6,tension:7,visual:9,data_ready:10,originality:6},vs:79,tags:"debt consumer credit student loans auto loans credit cards household balance sheet poverty wealth inequality economy"}







,{id:"retirement_ownership_by_age",title:"Who owns retirement accounts by age group 2022",sub:"55-64 year olds: 57% own retirement accounts. Under 35: 50%. 75+: only 42%.",type:"CHART",geo:"us_national",fmt:"Bar chart",tbl:"T1207",section:"Banking Finance Insurance",ext:["FRED: any national economic time series (fred.stlouisfed.org â€” free API)","BLS national data: employment, wages, CPI (bls.gov â€” free API)"],vars:["pct_families_own_retirement"],join:["pct_families_own_stocks","median_stock_value"],sc:{emotional:8,relatability:9,surprise:6,tension:6,visual:8,data_ready:10,originality:6},vs:77,tags:"retirement 401k savings accounts age inequality wealth gap older workers pension Social Security crisis"}







,{id:"delinquency_credit_cards_rising",title:"Credit card delinquency rates 2021â€“2024 â€” the new debt crisis",sub:"Credit card delinquency: 1.65% in 2021 â†’ 3.17% in 2024. Back to 2008 levels and rising.",type:"CHART",geo:"us_national",fmt:"Line chart",tbl:"T1226",section:"Banking Finance Insurance",ext:["FRED: any national economic time series (fred.stlouisfed.org â€” free API)","BLS national data: employment, wages, CPI (bls.gov â€” free API)"],vars:["credit_card_rate_all_accounts","total_consumer_credit"],join:["median_household_income","pct_families_own_any_asset"],sc:{emotional:8,relatability:8,surprise:7,tension:7,visual:8,data_ready:10,originality:7},vs:78,tags:"credit card delinquency debt default 2008 comparison household stress economy inflation wages poverty bank risk"}







,{id:"irs_audit_low_income",title:"IRS audits: corporations vs. poor households 2015â€“2022",sub:"Corporation audit rate fell 80%. EITC audit rate barely moved. Who actually gets audited in America.",type:"CHART",geo:"us_national",fmt:"Line chart",tbl:"T794",section:"Business Enterprise",ext:["FRED: any national economic time series (fred.stlouisfed.org â€” free API)","BLS national data: employment, wages, CPI (bls.gov â€” free API)"],vars:["corp_audit_rate","recommended_additional_tax"],join:["corporate_profits","income_tax_after_credits"],sc:{emotional:9,relatability:8,surprise:9,tension:9,visual:8,data_ready:10,originality:9},vs:87,tags:"IRS audit inequality rich poor corporate tax enforcement EITC earned income credit low income working class enforcement policy"}







,{id:"xref_home_price_vs_income",title:"Home price index vs. median income by state â€” the affordability destruction",sub:"Idaho: home prices up 649% since 2005, income up ~40%. Montana: +737%, income +~45%.",type:"XREF",geo:"us_state",fmt:"Scatter plot",tbl:"T771 Â· T727",section:"Prices Â· Income",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)"],vars:["home_price_index_2024","median_household_income"],join:["housing_permits_total","mortgage_delinquency_rate"],sc:{emotional:9,relatability:9,surprise:8,tension:7,visual:9,data_ready:10,originality:7},vs:86,tags:"housing affordability home prices income Idaho Montana Florida pandemic housing crisis real estate wealth inequality"}







,{id:"xref_credit_card_rate_vs_income",title:"Credit card interest rate burden vs. median income",sub:"The same 22.9% rate hits a $30K income household 7x harder than a $200K household.",type:"CHART",geo:"us_national",fmt:"Line chart",tbl:"T1223 Â· T727",section:"Banking Â· Income",ext:["FRED: any national economic time series (fred.stlouisfed.org â€” free API)","BLS national data: employment, wages, CPI (bls.gov â€” free API)"],vars:["credit_card_rate_all_accounts","median_household_income"],join:["total_consumer_credit","pct_families_own_any_asset"],sc:{emotional:9,relatability:9,surprise:7,tension:8,visual:8,data_ready:9,originality:9},vs:83,tags:"credit card interest rate income inequality regressive poor rich burden debt household finance bank consumer trap poverty"}







,{id:"medicaid_vs_rep_vote",title:"Medicaid enrollment rate vs. Republican vote share by state",sub:"Red states rely on Medicaid more â€” and keep voting to cut it. The coverage paradox.",type:"XREF",geo:"us_state",fmt:"Bivariate choropleth",tbl:"T576 Â· T454",section:"Social Insurance Â· Elections",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)","MIT Election Lab: presidential/congressional results (electionlab.mit.edu â€” free)"],vars:["pct_on_medicaid","rep_pct"],join:["median_household_income","total_transfers_per_capita","pct_on_snap"],sc:{emotional:9,relatability:8,surprise:8,tension:10,visual:9,data_ready:10,originality:8},vs:89,tags:"Medicaid healthcare red states Republican vote paradox poverty coverage insurance ACA Obamacare expansion rural South"}







,{id:"veterans_benefits_per_capita",title:"Veterans benefits per capita by state 2023",sub:"Virginia: $2,605 per person. Alaska: $913. South Carolina #3. The military-political geography.",type:"MAP",geo:"us_state",fmt:"State choropleth",tbl:"T573",section:"Social Insurance",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)"],vars:["veterans_benefits","total_transfers_per_capita"],join:["rep_pct","retired_military_count"],sc:{emotional:6,relatability:6,surprise:8,tension:5,visual:9,data_ready:10,originality:8},vs:75,tags:"veterans benefits military spending per capita state Virginia South Carolina Alaska defense communities Republican"}







,{id:"snap_vs_poverty_gap",title:"SNAP enrollment rate vs. poverty rate by state â€” the coverage gap",sub:"Some of the poorest states have lower SNAP enrollment. The access and stigma gap is geographic.",type:"XREF",geo:"us_state",fmt:"Scatter plot",tbl:"T576 Â· T727",section:"Social Insurance Â· Income",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)"],vars:["pct_on_snap","median_household_income"],join:["pct_on_medicaid","total_transfers_per_capita","rep_pct"],sc:{emotional:8,relatability:7,surprise:8,tension:7,visual:8,data_ready:10,originality:8},vs:81,tags:"SNAP food stamps poverty enrollment gap stigma red states access welfare rural Mississippi Alabama policy food security"}







,{id:"income_maintenance_per_capita",title:"Income maintenance benefits per capita by state 2023",sub:"California: $504 per person. Mississippi: $308. The safety net intensity doesn't match the poverty map.",type:"MAP",geo:"us_state",fmt:"State choropleth",tbl:"T573",section:"Social Insurance",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)"],vars:["total_transfers_per_capita"],join:["pct_on_snap","median_household_income","rep_pct"],sc:{emotional:7,relatability:7,surprise:8,tension:7,visual:9,data_ready:10,originality:8},vs:78,tags:"income maintenance welfare benefits per capita state safety net poverty California Mississippi inequality federal spending"}







,{id:"income_by_source_race_gap",title:"Median income by source and race 2023 â€” the wealth gap in detail",sub:"Federal retirement median: White $27K, Black $19K, Hispanic $24K. The racial wealth gap isn't just wages.",type:"CHART",geo:"us_national",fmt:"Bar chart",tbl:"T575",section:"Social Insurance",ext:["FRED: any national economic time series (fred.stlouisfed.org â€” free API)","BLS national data: employment, wages, CPI (bls.gov â€” free API)"],vars:["total_transfers_per_capita","pct_on_snap"],join:["median_household_income","pct_on_medicaid"],sc:{emotional:9,relatability:7,surprise:8,tension:8,visual:8,data_ready:10,originality:8},vs:83,tags:"income race inequality wealth gap Social Security retirement Black White Hispanic Asian poverty wealth divide systemic federal"}







,{id:"transfers_by_type_state",title:"What kind of federal money does your state actually get?",sub:"Medical payments dominate most states. Retirement dominates Florida. The transfer breakdown.",type:"MAP",geo:"us_state",fmt:"State choropleth",tbl:"T573",section:"Social Insurance",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)"],vars:["total_transfers_per_capita","veterans_benefits"],join:["rep_pct","median_household_income","pct_on_medicaid"],sc:{emotional:8,relatability:7,surprise:8,tension:7,visual:9,data_ready:10,originality:9},vs:83,tags:"federal transfers Medicaid Medicare Social Security retirement income maintenance veterans spending Florida South West Virginia poverty GOP"}







,{id:"female_lfp_rate_by_state",title:"Female labor force participation rate by state 2024",sub:"Minnesota 70%. West Virginia 52%. The 18-point gap in women's workforce participation.",type:"MAP",geo:"us_state",fmt:"State choropleth",tbl:"T629",section:"Labor Force",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)"],vars:["female_lfp_rate","state_unemployment_rate"],join:["pct_bachelors","median_household_income","daycare_preschool_cpi"],sc:{emotional:7,relatability:8,surprise:7,tension:6,visual:9,data_ready:10,originality:7},vs:78,tags:"women workforce labor participation state Minnesota West Virginia childcare economy equality wages gender inequality jobs"}







,{id:"xref_female_lfp_childcare",title:"Female labor force participation vs. childcare CPI â€” the childcare trap",sub:"States with highest childcare cost inflation have the lowest female workforce participation.",type:"XREF",geo:"us_state",fmt:"Scatter plot",tbl:"T629 Â· T770",section:"Labor Force Â· Prices",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)"],vars:["female_lfp_rate","daycare_preschool_cpi"],join:["median_household_income","pct_bachelors"],sc:{emotional:9,relatability:9,surprise:8,tension:7,visual:8,data_ready:9,originality:9},vs:86,tags:"women workforce childcare cost labor participation inequality economy mothers working parents gender gap wages policy daycare"}







,{id:"xref_unemployment_crime",title:"State unemployment rate vs. violent crime rate",sub:"One of the oldest correlations in criminology â€” but the geographic pattern surprises.",type:"XREF",geo:"us_state",fmt:"Scatter plot",tbl:"T629 Â· T340",section:"Labor Force Â· Law Enforcement",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)","FBI Crime Data Explorer: UCR/NIBRS by state/agency (cde.ucr.cjis.gov â€” free)"],vars:["state_unemployment_rate","violent_crime_rate"],join:["median_household_income","rep_pct","pct_on_snap"],sc:{emotional:8,relatability:8,surprise:6,tension:8,visual:8,data_ready:10,originality:6},vs:79,tags:"unemployment crime violence labor market poverty policing race policy economy law enforcement sociology"}







,{id:"earnings_ladder_education",title:"Mean earnings by education level 2023 â€” the complete ladder",sub:"No HS diploma: $34K. HS grad: $47K. Bachelor's: $87K. Professional degree: $184K.",type:"CHART",geo:"us_national",fmt:"Ranked list",tbl:"T253",section:"Education",ext:["FRED: any national economic time series (fred.stlouisfed.org â€” free API)","BLS national data: employment, wages, CPI (bls.gov â€” free API)"],vars:["pct_bachelors","expenditure_per_pupil"],join:["student_loans_outstanding","college_tuition_cpi"],sc:{emotional:7,relatability:9,surprise:5,tension:5,visual:9,data_ready:10,originality:4},vs:73,tags:"earnings wages education degree salary income inequality mobility doctorate professional master bachelor high school dropout"}







,{id:"federal_pct_school_revenue",title:"Share of school funding from federal vs. local taxes by state",sub:"Mississippi: 20% federal, 30% local. Connecticut: 6% federal, 58% local. Two Americas, one system.",type:"MAP",geo:"us_state",fmt:"Bivariate choropleth",tbl:"T258",section:"Education",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)"],vars:["revenue_federal_pct","revenue_local_pct","expenditure_per_pupil"],join:["pct_bachelors","median_household_income","rep_pct"],sc:{emotional:7,relatability:7,surprise:8,tension:7,visual:9,data_ready:10,originality:8},vs:79,tags:"school funding federal local property tax inequality Mississippi Connecticut revenue sources education equity race class"}







,{id:"xref_per_pupil_vs_bachelors",title:"Per-pupil school spending vs. college degree rate â€” the long-term ROI",sub:"States that spent more in 2000 have higher degree rates in 2024. The long-term payoff of education funding.",type:"XREF",geo:"us_state",fmt:"Scatter plot",tbl:"T258 Â· T254",section:"Education",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)"],vars:["expenditure_per_pupil","pct_bachelors"],join:["median_household_income","rep_pct","avg_teacher_salary"],sc:{emotional:7,relatability:8,surprise:7,tension:6,visual:8,data_ready:10,originality:8},vs:79,tags:"education spending funding outcomes college degree returns investment ROI school finance inequality long-term"}







,{id:"xref_vote_margin_transfers",title:"Vote margin vs. federal transfers per capita â€” the subsidy-resentment axis",sub:"The more federal money a state receives, the more it voted Republican in 2024. The 20-year trend intensifies.",type:"XREF",geo:"us_state",fmt:"Scatter plot",tbl:"T454 Â· T573",section:"Elections Â· Social Insurance",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)","MIT Election Lab: presidential/congressional results (electionlab.mit.edu â€” free)"],vars:["rep_pct","total_transfers_per_capita"],join:["median_household_income","pct_on_snap","violent_crime_rate"],sc:{emotional:10,relatability:8,surprise:8,tension:10,visual:9,data_ready:10,originality:8},vs:92,tags:"vote Republican federal transfers per capita subsidy resentment red states fiscal paradox MAGA Southern states poverty"}







,{id:"xref_vote_snap",title:"Republican vote share vs. SNAP enrollment rate by state",sub:"Deeply Republican states have the highest food stamp rates. The 2024 vote vs. the safety net they use.",type:"XREF",geo:"us_state",fmt:"Scatter plot",tbl:"T454 Â· T576",section:"Elections Â· Social Insurance",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)","MIT Election Lab: presidential/congressional results (electionlab.mit.edu â€” free)"],vars:["rep_pct","pct_on_snap"],join:["total_transfers_per_capita","median_household_income","violent_crime_rate"],sc:{emotional:9,relatability:8,surprise:8,tension:10,visual:8,data_ready:10,originality:7},vs:88,tags:"Republican SNAP food stamps vote paradox red states welfare poverty South Mississippi political economy policy hypocrisy"}







,{id:"xref_vote_crime",title:"Republican vote share vs. violent crime rate by state",sub:"The party of law and order comes from the states with the most violence. The crime-politics paradox.",type:"XREF",geo:"us_state",fmt:"Scatter plot",tbl:"T454 Â· T340",section:"Elections Â· Crime",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)","FBI Crime Data Explorer: UCR/NIBRS by state/agency (cde.ucr.cjis.gov â€” free)","MIT Election Lab: presidential/congressional results (electionlab.mit.edu â€” free)"],vars:["rep_pct","violent_crime_rate"],join:["median_household_income","pct_bachelors","state_unemployment_rate"],sc:{emotional:9,relatability:8,surprise:8,tension:10,visual:8,data_ready:10,originality:7},vs:87,tags:"Republican crime law order violent paradox South states policing safety politics culture war Trump voter"}







,{id:"xref_vote_bridges",title:"Republican vote share vs. bridge condition by state",sub:"States voting most Republican have the worst bridges. Infrastructure neglect and political identity.",type:"XREF",geo:"us_state",fmt:"Scatter plot",tbl:"T454 Â· T1126",section:"Elections Â· Infrastructure",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)","MIT Election Lab: presidential/congressional results (electionlab.mit.edu â€” free)"],vars:["rep_pct","pct_bridges_poor"],join:["total_transfers_per_capita","state_gdp_per_capita"],sc:{emotional:8,relatability:8,surprise:7,tension:8,visual:9,data_ready:10,originality:8},vs:81,tags:"Republican bridges infrastructure federal spending paradox Iowa West Virginia Rhode Island roads government crumbling"}







,{id:"xref_vote_teen_births",title:"Republican vote share vs. teen birth rate by state",sub:"The most Republican states have the highest teen birth rates â€” and the least comprehensive sex education.",type:"XREF",geo:"us_state",fmt:"Scatter plot",tbl:"T454 Â· T86",section:"Elections Â· Births",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)","MIT Election Lab: presidential/congressional results (electionlab.mit.edu â€” free)"],vars:["rep_pct","teen_birth_rate"],join:["pct_bachelors","median_household_income"],sc:{emotional:8,relatability:7,surprise:7,tension:9,visual:8,data_ready:10,originality:6},vs:80,tags:"Republican teen birth rate sex education abstinence religion conservative South Mississippi political culture"}







,{id:"xref_vote_renewable",title:"Republican vote share vs. renewable energy share by state",sub:"The wind belt is Republican and going renewable anyway. The politics and economics diverge.",type:"XREF",geo:"us_state",fmt:"Scatter plot",tbl:"T454 Â· T976",section:"Elections Â· Energy",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)","EIA State Energy Data System: production + consumption by state (eia.gov â€” free API)","MIT Election Lab: presidential/congressional results (electionlab.mit.edu â€” free)"],vars:["rep_pct","renewable_energy_share"],join:["energy_consumption_per_capita","coal_production_index"],sc:{emotional:7,relatability:7,surprise:8,tension:7,visual:8,data_ready:10,originality:7},vs:77,tags:"Republican renewable energy wind Iowa Kansas red states climate policy clean energy economics market forces"}







,{id:"xref_vote_teacher_salary",title:"Republican vote share vs. average teacher salary by state",sub:"The most Republican states pay teachers the least â€” and have the worst educational outcomes.",type:"XREF",geo:"us_state",fmt:"Scatter plot",tbl:"T454 Â· T268",section:"Elections Â· Education",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)","MIT Election Lab: presidential/congressional results (electionlab.mit.edu â€” free)"],vars:["rep_pct","avg_teacher_salary"],join:["pct_bachelors","expenditure_per_pupil"],sc:{emotional:8,relatability:8,surprise:6,tension:8,visual:8,data_ready:10,originality:6},vs:79,tags:"Republican teacher salary education schools funding union Mississippi California South red blue state policy"}







,{id:"xref_trade_deficit_vote",title:"Trade deficit with China vs. manufacturing job loss vs. vote shift",sub:"States that lost the most manufacturing to China swung hardest toward Trump in 2016 and held in 2024.",type:"XREF",geo:"us_state",fmt:"Scatter plot",tbl:"T1310 Â· T454",section:"Trade Â· Elections",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)","MIT Election Lab: presidential/congressional results (electionlab.mit.edu â€” free)"],vars:["trade_balance_goods","rep_pct"],join:["foreign_affiliate_employment","state_unemployment_rate"],sc:{emotional:9,relatability:8,surprise:7,tension:9,visual:8,data_ready:9,originality:7},vs:82,tags:"trade deficit China manufacturing jobs Trump 2016 2024 swing states Rust Belt Ohio Michigan Pennsylvania vote"}







,{id:"xref_tariffs_2025",title:"US trade deficit by country vs. 2025 tariff rate imposed",sub:"China: -$298B deficit, 145% tariff. Vietnam: -$90B, 46%. The Trump tariff targeting map.",type:"MAP",geo:"worldwide",fmt:"World choropleth",tbl:"T1310",section:"Trade",ext:["World Bank Open Data: GDP, population, income by country (data.worldbank.org â€” free API)"],vars:["trade_balance_goods","current_account_balance"],join:["us_troops_overseas","rd_pct_gdp"],sc:{emotional:9,relatability:8,surprise:7,tension:9,visual:9,data_ready:10,originality:9},vs:87,tags:"tariffs China Vietnam trade deficit Trump 2025 trade war import tax policy economic nationalism MAGA"}







,{id:"xref_energy_vote",title:"Energy consumption per capita vs. Republican vote share by state",sub:"High-energy states vote Republican. Low-energy states vote Democrat. The fossil fuel politics map.",type:"XREF",geo:"us_state",fmt:"Bivariate choropleth",tbl:"T975 Â· T454",section:"Energy Â· Elections",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)","EIA State Energy Data System: production + consumption by state (eia.gov â€” free API)","MIT Election Lab: presidential/congressional results (electionlab.mit.edu â€” free)"],vars:["energy_consumption_per_capita","rep_pct"],join:["coal_production_index","renewable_energy_share"],sc:{emotional:8,relatability:7,surprise:7,tension:9,visual:9,data_ready:10,originality:7},vs:82,tags:"energy consumption fossil fuels Republican vote climate politics coal oil gas Wyoming Louisiana Texas red states green energy Democrats"}







,{id:"xref_renewable_vs_income",title:"Renewable energy share vs. median income by state",sub:"Rich states aren't necessarily greener. Wyoming is wealthy and 97% fossil. Massachusetts is rich and 25% renewable.",type:"XREF",geo:"us_state",fmt:"Scatter plot",tbl:"T976 Â· T727",section:"Energy Â· Income",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)","EIA State Energy Data System: production + consumption by state (eia.gov â€” free API)"],vars:["renewable_energy_share","median_household_income"],join:["energy_consumption_per_capita","rep_pct"],sc:{emotional:6,relatability:6,surprise:8,tension:6,visual:8,data_ready:10,originality:7},vs:73,tags:"renewable energy income wealth state green clean energy climate policy Wyoming Massachusetts California Texas hydro wind solar"}







,{id:"xref_coal_vs_transfers",title:"Coal production decline vs. federal transfers per capita by state",sub:"As coal died, federal transfers filled the gap. The government replaced the mine.",type:"XREF",geo:"us_state",fmt:"Scatter plot",tbl:"T950 Â· T573",section:"Energy Â· Social Insurance",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)","EIA State Energy Data System: production + consumption by state (eia.gov â€” free API)"],vars:["coal_production_index","total_transfers_per_capita"],join:["rep_pct","state_unemployment_rate"],sc:{emotional:8,relatability:6,surprise:8,tension:7,visual:7,data_ready:10,originality:9},vs:75,tags:"coal decline federal transfers West Virginia Appalachia Kentucky replacement government subsidy mine jobs rural economy"}







,{id:"coal_production_by_region",title:"Coal production collapse by region 1990â€“2024",sub:"Appalachian coal: down 74%. Western coal held steady until 2019. Two very different coal stories.",type:"CHART",geo:"us_national",fmt:"Line chart",tbl:"T950",section:"Energy",ext:["FRED: any national economic time series (fred.stlouisfed.org â€” free API)","BLS national data: employment, wages, CPI (bls.gov â€” free API)","EIA State Energy Data System: production + consumption by state (eia.gov â€” free API)"],vars:["coal_production_index"],join:["renewable_energy_share","energy_consumption_per_capita"],sc:{emotional:7,relatability:6,surprise:7,tension:7,visual:8,data_ready:10,originality:7},vs:72,tags:"coal decline Appalachia West Virginia Kentucky region energy transition jobs rural economy fossil fuels renewable power"}







,{id:"xref_farm_subsidies_vote",title:"Agricultural transfer payments vs. Republican vote share by state",sub:"The biggest farm subsidy states vote most Republican. The farm welfare paradox.",type:"XREF",geo:"us_state",fmt:"Scatter plot",tbl:"T573 Â· T454",section:"Agriculture Â· Elections",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)","USDA ERS: food environment, rural classification, farm income (ers.usda.gov â€” free)","MIT Election Lab: presidential/congressional results (electionlab.mit.edu â€” free)"],vars:["total_transfers_per_capita","rep_pct"],join:["farms_count_2022","farm_value_land"],sc:{emotional:8,relatability:7,surprise:8,tension:9,visual:7,data_ready:10,originality:7},vs:79,tags:"farm subsidies Republican vote paradox agricultural welfare Kansas Iowa red states government spending"}







,{id:"xref_cropland_snap",title:"Cropland percentage vs. SNAP enrollment rate by state",sub:"States with the most farmland have the highest food stamp rates. The farmer poverty paradox.",type:"XREF",geo:"us_state",fmt:"Scatter plot",tbl:"T413 Â· T576",section:"Agriculture Â· Social Insurance",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)","USDA ERS: food environment, rural classification, farm income (ers.usda.gov â€” free)"],vars:["pct_cropland","pct_on_snap"],join:["farms_count_2022","median_household_income"],sc:{emotional:8,relatability:7,surprise:9,tension:7,visual:8,data_ready:10,originality:9},vs:79,tags:"cropland SNAP food stamps farmers poverty agriculture Iowa Mississippi Kansas paradox rural food insecurity"}







,{id:"xref_farm_value_snap",title:"Agricultural land value vs. SNAP enrollment rate by state",sub:"Iowa has $277B in farmland and 10% of residents on food stamps. Growing food doesn't mean feeding people.",type:"XREF",geo:"us_state",fmt:"Scatter plot",tbl:"T869 Â· T576",section:"Agriculture Â· Social Insurance",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)","USDA ERS: food environment, rural classification, farm income (ers.usda.gov â€” free)"],vars:["farm_value_land","pct_on_snap"],join:["farms_count_2022","median_household_income"],sc:{emotional:8,relatability:7,surprise:9,tension:7,visual:7,data_ready:10,originality:9},vs:78,tags:"farmland value SNAP food stamps hunger paradox Iowa agriculture wealth inequality rural food insecurity farm states"}







,{id:"farmer_count_decline",title:"Number of US farms 1935â€“2024: the 88-year collapse",sub:"7 million farms in 1935. 2 million today. The disappearance of American farm culture in one chart.",type:"CHART",geo:"us_national",fmt:"Area chart",tbl:"T869",section:"Agriculture",ext:["FRED: any national economic time series (fred.stlouisfed.org â€” free API)","BLS national data: employment, wages, CPI (bls.gov â€” free API)","USDA ERS: food environment, rural classification, farm income (ers.usda.gov â€” free)"],vars:["farms_count_2022","land_in_farms_2022"],join:["farmer_avg_age","farm_value_land"],sc:{emotional:8,relatability:7,surprise:8,tension:6,visual:8,data_ready:10,originality:7},vs:77,tags:"farms decline history 1935 1950 2024 rural America agricultural collapse consolidation corporate agribusiness family farm"}







,{id:"xref_troops_trade",title:"US troops overseas by country vs. trade deficit with that country",sub:"Germany: 35K troops, +$111B trade surplus FOR Germany. Japan: 51K troops, -$116B deficit.",type:"XREF",geo:"worldwide",fmt:"Scatter plot",tbl:"T549 Â· T1310",section:"National Security Â· Trade",ext:["World Bank Open Data: GDP, population, income by country (data.worldbank.org â€” free API)"],vars:["us_troops_overseas","trade_balance_goods"],join:["rd_pct_gdp"],sc:{emotional:8,relatability:6,surprise:9,tension:8,visual:8,data_ready:10,originality:9},vs:82,tags:"troops overseas trade deficit security subsidy Japan Germany South Korea NATO America empire foreign policy economics"}







,{id:"xref_casualties_transfers",title:"Post-9/11 military deaths by state of origin vs. federal transfers per capita",sub:"States sending the most soldiers to war also receive the most federal money. Service and dependency.",type:"XREF",geo:"us_state",fmt:"Scatter plot",tbl:"T548 Â· T573",section:"Military Â· Social Insurance",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)"],vars:["total_deaths","total_transfers_per_capita"],join:["rep_pct","veterans_benefits"],sc:{emotional:9,relatability:7,surprise:8,tension:8,visual:7,data_ready:9,originality:9},vs:78,tags:"military deaths war federal transfers veterans benefits state red blue sacrifice poverty dependency service community"}







,{id:"xref_rd_vs_trade_country",title:"R&D spending as % of GDP vs. trade balance by country",sub:"South Korea spends 5% of GDP on R&D and runs a trade surplus. US: 3.45% and a $1.2T deficit.",type:"XREF",geo:"worldwide",fmt:"Scatter plot",tbl:"T842 Â· T1310",section:"Science Â· Trade",ext:["World Bank Open Data: GDP, population, income by country (data.worldbank.org â€” free API)"],vars:["rd_pct_gdp","trade_balance_goods"],join:["us_troops_overseas","population_pct_change_2020_2025"],sc:{emotional:7,relatability:6,surprise:8,tension:7,visual:8,data_ready:10,originality:9},vs:76,tags:"R&D research innovation trade balance South Korea Germany China Japan US deficit competitiveness economic policy manufacturing"}







,{id:"worldwide_shrinking_aging",title:"Countries with both population decline and aging workforces 2025",sub:"Japan, Germany, South Korea, Italy: shrinking AND aging. The double demographic squeeze.",type:"RANK",geo:"worldwide",fmt:"Quadrant chart",tbl:"International Statistics",section:"International Statistics",ext:["World Bank Open Data: GDP, population, income by country (data.worldbank.org â€” free API)"],vars:["population_pct_change_2020_2025","net_migration_rate"],join:["birth_rate","rd_pct_gdp"],sc:{emotional:7,relatability:6,surprise:8,tension:6,visual:9,data_ready:10,originality:8},vs:74,tags:"aging population decline Japan Germany South Korea Italy workforce labor shortage pension crisis immigration demographic"}







,{id:"us_healthcare_vs_outcomes",title:"US healthcare spending vs. outcomes compared to peer nations",sub:"US spends $14K/person on healthcare â€” 2x Germany. Life expectancy: the same.",type:"CHART",geo:"worldwide",fmt:"Scatter plot",tbl:"T141",section:"Health",ext:["World Bank Open Data: GDP, population, income by country (data.worldbank.org â€” free API)","CDC WONDER: mortality + disease rates by county/state (wonder.cdc.gov â€” free)"],vars:["per_capita_health_spending"],join:["population_pct_change_2020_2025","rd_pct_gdp"],sc:{emotional:9,relatability:8,surprise:7,tension:8,visual:8,data_ready:9,originality:5},vs:79,tags:"healthcare spending outcomes US international comparison Germany UK Canada life expectancy waste efficiency system"}







,{id:"services_surplus_vs_goods_deficit",title:"US goods deficit vs. services surplus â€” we sell software, we buy stuff",sub:"America runs a $311B services surplus â€” but a $1.2T goods deficit. The structural shift since 2000.",type:"CHART",geo:"us_national",fmt:"Area chart",tbl:"T1306",section:"Foreign Commerce",ext:["FRED: any national economic time series (fred.stlouisfed.org â€” free API)","BLS national data: employment, wages, CPI (bls.gov â€” free API)"],vars:["balance_on_goods","balance_on_services","current_account_balance"],join:["rd_pct_gdp","foreign_affiliate_employment"],sc:{emotional:7,relatability:6,surprise:8,tension:7,visual:8,data_ready:10,originality:8},vs:77,tags:"services exports goods imports trade structural shift US economy software finance intellectual property manufacturing"}







,{id:"corporate_profit_share_gdp",title:"Corporate profits as share of GDP 1950â€“2024",sub:"Corporate profit share of GDP hit an all-time high of 11.2% in 2024. Labor share hit an all-time low.",type:"CHART",geo:"us_national",fmt:"Line chart",tbl:"T793",section:"Business Enterprise",ext:["FRED: any national economic time series (fred.stlouisfed.org â€” free API)","BLS national data: employment, wages, CPI (bls.gov â€” free API)"],vars:["corporate_profits","income_tax_after_credits"],join:["median_household_income","state_unemployment_rate"],sc:{emotional:9,relatability:8,surprise:8,tension:9,visual:8,data_ready:10,originality:7},vs:83,tags:"corporate profits GDP share labor share inequality class workers wages capitalism record high 2024 historical"}







,{id:"snap_enrollment_over_time",title:"SNAP enrollment 2000â€“2024: recessions, COVID, and the politics of food",sub:"From 17M to 42M enrollees since 2000. The safety net expands in crises and barely contracts after.",type:"CHART",geo:"us_national",fmt:"Area chart",tbl:"T577",section:"Social Insurance",ext:["FRED: any national economic time series (fred.stlouisfed.org â€” free API)","BLS national data: employment, wages, CPI (bls.gov â€” free API)"],vars:["snap_households","pct_on_snap"],join:["state_unemployment_rate","median_household_income"],sc:{emotional:8,relatability:7,surprise:6,tension:7,visual:8,data_ready:10,originality:6},vs:74,tags:"SNAP enrollment history 2008 COVID pandemic recession safety net food stamps trend politics"}







,{id:"us_births_deaths_crossover",title:"US births vs. deaths 2000â€“2030 â€” the natural population crossover",sub:"Natural increase (births - deaths) hit near-zero in 2020 and may go negative by 2030.",type:"CHART",geo:"us_national",fmt:"Line chart",tbl:"Population PDF Â· T80",section:"Population Â· Births",ext:["FRED: any national economic time series (fred.stlouisfed.org â€” free API)","BLS national data: employment, wages, CPI (bls.gov â€” free API)"],vars:["birth_rate_state","total_fertility_rate_by_race"],join:["net_migration_rate","population_pct_change"],sc:{emotional:8,relatability:7,surprise:9,tension:7,visual:9,data_ready:9,originality:7},vs:79,tags:"births deaths crossover natural population decline immigration dependence 2030 aging fertility replacement demographic"}







,{id:"corporate_profit_vs_wages",title:"Corporate profit growth vs. wage growth 2000â€“2024",sub:"Corporate profits: +323%. Median wages: +94%. The 3.4x divergence in who gets the economy's gains.",type:"CHART",geo:"us_national",fmt:"Line chart",tbl:"T793 Â· T727",section:"Business Â· Income",ext:["FRED: any national economic time series (fred.stlouisfed.org â€” free API)","BLS national data: employment, wages, CPI (bls.gov â€” free API)"],vars:["corporate_profits","median_household_income"],join:["income_tax_after_credits","pct_families_own_stocks"],sc:{emotional:9,relatability:8,surprise:7,tension:9,visual:8,data_ready:10,originality:6},vs:82,tags:"corporate profits wages divergence inequality class workers shareholders 2000 2024 economy gains distribution"}







,{id:"us_trade_deficit_history",title:"US trade deficit 1960â€“2024: the 60-year accumulation",sub:"From balanced trade to -$1.185 trillion. The most important economic chart nobody shows with full history.",type:"CHART",geo:"us_national",fmt:"Area chart",tbl:"T1306",section:"Foreign Commerce",ext:["FRED: any national economic time series (fred.stlouisfed.org â€” free API)","BLS national data: employment, wages, CPI (bls.gov â€” free API)"],vars:["current_account_balance","balance_on_goods"],join:["trade_balance_goods","rep_pct"],sc:{emotional:7,relatability:6,surprise:8,tension:8,visual:8,data_ready:10,originality:7},vs:76,tags:"trade deficit history 60 years 1960 2024 manufacturing globalization NAFTA China WTO import economy"}







,{id:"newspaper_employment_collapse",title:"Newspaper newsroom employment 2004â€“2024: -60%",sub:"157,000 newsroom jobs in 2004. 64,000 in 2024. The news desert was a workforce collapse first.",type:"CHART",geo:"us_national",fmt:"Area chart",tbl:"T1174",section:"Information",ext:["FRED: any national economic time series (fred.stlouisfed.org â€” free API)","BLS national data: employment, wages, CPI (bls.gov â€” free API)"],vars:["newspaper_print_revenue","newspaper_digital_revenue"],join:[],sc:{emotional:8,relatability:7,surprise:7,tension:7,visual:8,data_ready:10,originality:6},vs:75,tags:"newspaper journalism jobs decline newsrooms employment collapse local news democracy information crisis 2004 2024"}







,{id:"renewable_growth_national",title:"Renewable energy share of US consumption 1990â€“2024",sub:"Renewables went from 7% of US consumption in 1990 to 21% in 2024. The quiet energy revolution.",type:"CHART",geo:"us_national",fmt:"Area chart",tbl:"T976",section:"Energy",ext:["FRED: any national economic time series (fred.stlouisfed.org â€” free API)","BLS national data: employment, wages, CPI (bls.gov â€” free API)","EIA State Energy Data System: production + consumption by state (eia.gov â€” free API)"],vars:["renewable_energy_share","coal_production_index"],join:["energy_consumption_per_capita"],sc:{emotional:7,relatability:7,surprise:7,tension:5,visual:8,data_ready:10,originality:5},vs:72,tags:"renewable energy growth history 1990 2024 solar wind hydro fossil fuels coal transition climate policy"}







,{id:"irs_audit_vs_snap",title:"IRS corporate audit rate collapse vs. SNAP enrollment growth",sub:"As IRS stopped auditing corporations, SNAP enrollment grew. Audit less, spend more on the poor.",type:"CHART",geo:"us_national",fmt:"Line chart",tbl:"T794 Â· T577",section:"Business Â· Social Insurance",ext:["FRED: any national economic time series (fred.stlouisfed.org â€” free API)","BLS national data: employment, wages, CPI (bls.gov â€” free API)"],vars:["corp_audit_rate","pct_on_snap"],join:["corporate_profits","recommended_additional_tax"],sc:{emotional:9,relatability:7,surprise:9,tension:9,visual:8,data_ready:10,originality:10},vs:86,tags:"IRS audit corporate tax SNAP food stamps enrollment trade-off fiscal inequality poverty enforcement rich poor"}







,{id:"tuition_cpi_vs_irs_audit",title:"College tuition inflation vs. IRS enforcement collapse",sub:"Tuition CPI tripled as IRS stopped collecting from corporations. The tax-education cost connection.",type:"CHART",geo:"us_national",fmt:"Line chart",tbl:"T770 Â· T794",section:"Prices Â· Business",ext:["FRED: any national economic time series (fred.stlouisfed.org â€” free API)","BLS national data: employment, wages, CPI (bls.gov â€” free API)"],vars:["college_tuition_cpi","corp_audit_rate"],join:["student_loans_outstanding","corporate_profits"],sc:{emotional:9,relatability:7,surprise:9,tension:8,visual:8,data_ready:10,originality:10},vs:82,tags:"tuition inflation IRS audit enforcement college cost corporate tax enforcement connection policy fiscal"}







,{id:"xref_home_prices_births",title:"Home price index vs. birth rate by state",sub:"Housing is the most reliable birth control. The most expensive states have the fewest babies.",type:"XREF",geo:"us_state",fmt:"Scatter plot",tbl:"T771 Â· T81",section:"Housing Â· Births",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)","HUD Fair Market Rents + housing data by state/county (huduser.gov â€” free)"],vars:["home_price_index_2024","birth_rate_state"],join:["median_household_income","pct_bachelors"],sc:{emotional:8,relatability:8,surprise:8,tension:6,visual:8,data_ready:10,originality:8},vs:79,tags:"housing prices birth rate fertility California Idaho Colorado Montana fertility decline expensive real estate family formation"}







,{id:"xref_home_prices_crime",title:"Home price index vs. violent crime rate by state",sub:"Expensive states have less crime. But some expensive states (California) still have high crime.",type:"XREF",geo:"us_state",fmt:"Scatter plot",tbl:"T771 Â· T340",section:"Housing Â· Crime",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)","FBI Crime Data Explorer: UCR/NIBRS by state/agency (cde.ucr.cjis.gov â€” free)","HUD Fair Market Rents + housing data by state/county (huduser.gov â€” free)"],vars:["home_price_index_2024","violent_crime_rate"],join:["median_household_income","state_unemployment_rate"],sc:{emotional:7,relatability:8,surprise:7,tension:7,visual:8,data_ready:10,originality:7},vs:74,tags:"home prices crime safety violence expensive state California outlier gentrification displacement neighborhood inequality"}







,{id:"xref_home_prices_childcare",title:"Home price appreciation vs. childcare CPI by state",sub:"The two fastest-growing costs for families: housing and childcare. They're rising in the same places.",type:"XREF",geo:"us_state",fmt:"Scatter plot",tbl:"T771 Â· T770",section:"Prices",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)"],vars:["home_price_index_2024","daycare_preschool_cpi"],join:["female_lfp_rate","median_household_income"],sc:{emotional:9,relatability:9,surprise:8,tension:7,visual:8,data_ready:9,originality:8},vs:82,tags:"home prices childcare cost of living family squeeze young families housing daycare inflation parallel"}







,{id:"county_income_inequality",title:"Income inequality (Gini coefficient) by US county",sub:"The Gini coefficient by county reveals inequality within states â€” not just between them.",type:"MAP",geo:"us_county",fmt:"County choropleth",tbl:"T727",section:"Income",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by county (bls.gov â€” free)"],vars:["median_household_income","pct_under_25k","pct_over_200k"],join:["violent_crime_rate","pct_on_snap"],sc:{emotional:9,relatability:8,surprise:8,tension:8,visual:10,data_ready:8,originality:7},vs:83,tags:"Gini income inequality county within-state variation rich poor concentration wealth distribution"}







,{id:"county_snap_rate",title:"SNAP enrollment rate by US county â€” the hunger geography",sub:"Some counties have 40%+ SNAP enrollment. Others under 3%. The hunger geography within states.",type:"MAP",geo:"us_county",fmt:"County choropleth",tbl:"T576",section:"Social Insurance",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by county (bls.gov â€” free)"],vars:["pct_on_snap"],join:["median_household_income","violent_crime_rate","rep_pct"],sc:{emotional:8,relatability:7,surprise:7,tension:8,visual:10,data_ready:8,originality:5},vs:78,tags:"SNAP food stamps county hunger poverty rural urban concentration geographic within-state variation food insecurity"}







,{id:"county_violent_crime",title:"Violent crime rate by US county 2023",sub:"Some rural Southern counties: 900+/100K. Some suburban Midwest counties: under 50.",type:"MAP",geo:"us_county",fmt:"County choropleth",tbl:"T340",section:"Crime",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by county (bls.gov â€” free)","FBI Crime Data Explorer: UCR/NIBRS by state/agency (cde.ucr.cjis.gov â€” free)"],vars:["violent_crime_rate","murder_rate"],join:["median_household_income","state_unemployment_rate"],sc:{emotional:9,relatability:8,surprise:7,tension:8,visual:10,data_ready:8,originality:4},vs:79,tags:"violent crime county geography within-state Southern rural suburban urban inequality poverty police"}







,{id:"county_median_income",title:"Median household income by US county 2023",sub:"Falls Church VA: $152K. Clay County KY: $22K. The within-state income geography state maps hide.",type:"MAP",geo:"us_county",fmt:"County choropleth",tbl:"T727",section:"Income",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by county (bls.gov â€” free)"],vars:["median_household_income"],join:["violent_crime_rate","pct_on_snap","pct_bachelors"],sc:{emotional:8,relatability:9,surprise:6,tension:6,visual:10,data_ready:8,originality:3},vs:74,tags:"median income county within-state Virginia Kentucky suburban rural urban inequality wealth concentration geography"}







,{id:"county_birth_rate",title:"Birth rate by US county 2023",sub:"Utah County UT: birth rate 65/1,000 women. San Francisco County: 32/1,000.",type:"MAP",geo:"us_county",fmt:"County choropleth",tbl:"T81",section:"Births",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by county (bls.gov â€” free)"],vars:["birth_rate_state","total_fertility_rate_by_race"],join:["median_household_income","pct_on_snap"],sc:{emotional:7,relatability:6,surprise:7,tension:5,visual:10,data_ready:8,originality:5},vs:70,tags:"birth rate county fertility Utah San Francisco geography religion income within-state variation"}







,{id:"three_maps_one_story",title:"Education Â· income Â· crime: three maps that trace the same outline",sub:"The education map, the income map, and the crime map of America all have the same shape.",type:"MAP",geo:"us_state",fmt:"Special map",tbl:"T254 Â· T727 Â· T340",section:"Education Â· Income Â· Crime",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)","FBI Crime Data Explorer: UCR/NIBRS by state/agency (cde.ucr.cjis.gov â€” free)"],vars:["pct_bachelors","median_household_income","violent_crime_rate"],join:["rep_pct","pct_on_snap","teen_birth_rate"],sc:{emotional:9,relatability:8,surprise:6,tension:9,visual:10,data_ready:10,originality:8},vs:85,tags:"education income crime triptych three maps same story South inequality race poverty policy visual"}







,{id:"mississippi_vs_massachusetts",title:"Mississippi vs. Massachusetts â€” every social indicator",sub:"The two Americas exist within one country. Side-by-side on 12 indicators.",type:"CHART",geo:"us_state",fmt:"Bar chart",tbl:"Multiple",section:"Multiple",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)"],vars:["pct_bachelors","median_household_income","violent_crime_rate","pct_on_snap","teen_birth_rate","rep_pct"],join:["pct_on_medicaid","total_transfers_per_capita","avg_teacher_salary"],sc:{emotional:9,relatability:8,surprise:6,tension:9,visual:9,data_ready:10,originality:7},vs:83,tags:"Mississippi Massachusetts comparison two Americas inequality education income crime health social indicators"}







,{id:"state_misery_index",title:"Comprehensive state misery index â€” all negatives combined",sub:"Rank all 50 states by a composite of poverty + crime + low education + food stamps + poor health.",type:"RANK",geo:"us_state",fmt:"Ranked list",tbl:"Multiple",section:"Multiple",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)"],vars:["pct_on_snap","violent_crime_rate","pct_bachelors","median_household_income"],join:["teen_birth_rate","state_unemployment_rate","rep_pct"],sc:{emotional:9,relatability:8,surprise:6,tension:9,visual:9,data_ready:10,originality:7},vs:82,tags:"state ranking misery index composite poverty crime education income health Mississippi Louisiana Alabama West Virginia"}







,{id:"prosperity_vote_quadrant",title:"State prosperity vs. Republican vote â€” the four quadrants of American politics",sub:"Rich-red, rich-blue, poor-red, poor-blue. The quadrant map of American political economy.",type:"XREF",geo:"us_state",fmt:"Quadrant chart",tbl:"T727 Â· T454",section:"Income Â· Elections",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)","MIT Election Lab: presidential/congressional results (electionlab.mit.edu â€” free)"],vars:["median_household_income","rep_pct"],join:["pct_bachelors","violent_crime_rate","total_transfers_per_capita"],sc:{emotional:9,relatability:8,surprise:7,tension:9,visual:10,data_ready:10,originality:7},vs:84,tags:"prosperity vote quadrant rich poor Republican Democrat political economy state Mississippi Maryland West Virginia New Jersey"}







,{id:"coastline_per_capita",title:"Coastal access inequality â€” shoreline miles per 1,000 residents by state",sub:"Alaska: 1,800 miles of shore per 1,000 people. New Jersey: 0.3 miles. Who has access to the coast?",type:"MAP",geo:"us_state",fmt:"State choropleth",tbl:"T408",section:"Geography & Environment",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)"],vars:["coastline_miles"],join:["median_household_income","real_per_capita_income"],sc:{emotional:5,relatability:7,surprise:9,tension:3,visual:9,data_ready:10,originality:9},vs:74,tags:"coastline shoreline access inequality Alaska New Jersey geography ocean beach tourism recreation equity"}







,{id:"coastline_ranking",title:"US states ranked by coastline miles â€” the surprising list",sub:"Alaska has 33,904 miles of coastline. Florida: 1,350. The 25x difference nobody knows.",type:"RANK",geo:"us_state",fmt:"Ranked list",tbl:"T408",section:"Geography & Environment",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)"],vars:["coastline_miles"],join:["median_household_income"],sc:{emotional:5,relatability:7,surprise:10,tension:2,visual:9,data_ready:10,originality:9},vs:76,tags:"coastline shoreline states Alaska Florida ranking geography surprising ocean beach access miles weird fact"}







,{id:"water_withdrawal_per_capita",title:"Water withdrawal per day by state â€” where freshwater stress lives",sub:"California withdraws 26B gallons/day. Nevada: 6.5B from 3M people. The water scarcity geography.",type:"MAP",geo:"us_state",fmt:"State choropleth",tbl:"T415",section:"Geography & Environment",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)"],vars:["mean_elevation"],join:["pct_cropland","energy_consumption_per_capita"],sc:{emotional:7,relatability:7,surprise:8,tension:7,visual:9,data_ready:10,originality:8},vs:76,tags:"water withdrawal freshwater stress California Nevada agriculture irrigation drought climate West East divide geography"}







,{id:"xref_elevation_energy",title:"Mean state elevation vs. energy consumption per capita",sub:"High-altitude western states consume more energy â€” climate drives consumption more than wealth.",type:"XREF",geo:"us_state",fmt:"Scatter plot",tbl:"T410 Â· T975",section:"Geography Â· Energy",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)","EIA State Energy Data System: production + consumption by state (eia.gov â€” free API)"],vars:["mean_elevation","energy_consumption_per_capita"],join:["renewable_energy_share","coal_production_index"],sc:{emotional:5,relatability:5,surprise:8,tension:3,visual:7,data_ready:10,originality:9},vs:70,tags:"elevation altitude climate energy consumption geography western states Wyoming Colorado cold heating cooling"}







,{id:"xref_student_debt_fertility",title:"Student loan debt per capita vs. fertility rate by state",sub:"Higher-debt states have lower fertility. The student debt-birth rate connection is quantifiable.",type:"XREF",geo:"us_state",fmt:"Scatter plot",tbl:"T1222 Â· T81",section:"Banking Â· Births",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)"],vars:["student_loans_outstanding","birth_rate_state"],join:["median_household_income","pct_bachelors"],sc:{emotional:8,relatability:8,surprise:8,tension:6,visual:7,data_ready:10,originality:9},vs:77,tags:"student debt fertility birth rate connection young adults childlessness financial burden education loans demographics"}







,{id:"xref_hospital_profit_cpi",title:"Hospital services CPI vs. hospital industry profits 2010â€“2024",sub:"Hospital CPI up 45% since 2010. Hospital operating margins also up. The price-profit link.",type:"CHART",geo:"us_national",fmt:"Line chart",tbl:"T770 Â· T793",section:"Prices Â· Business",ext:["FRED: any national economic time series (fred.stlouisfed.org â€” free API)","BLS national data: employment, wages, CPI (bls.gov â€” free API)"],vars:["hospital_services_cpi","corporate_profits"],join:["per_capita_health_spending","health_insurance_cpi"],sc:{emotional:9,relatability:8,surprise:8,tension:9,visual:8,data_ready:9,originality:8},vs:83,tags:"hospital prices CPI profit margin healthcare industry corporation private equity costs inflation system extraction"}







,{id:"xref_farm_concentration_hunger",title:"Farm sales concentration vs. SNAP enrollment rate by state",sub:"States where 5% of farms produce 80% of food have the highest food stamp rates.",type:"XREF",geo:"us_state",fmt:"Scatter plot",tbl:"T871 Â· T576",section:"Agriculture Â· Social Insurance",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)","USDA ERS: food environment, rural classification, farm income (ers.usda.gov â€” free)"],vars:["farm_sales_by_size","pct_on_snap"],join:["median_household_income","farms_count_2022"],sc:{emotional:9,relatability:7,surprise:9,tension:8,visual:7,data_ready:10,originality:10},vs:82,tags:"farm concentration food stamps hunger inequality mega-farms agribusiness corporate food insecurity paradox"}







,{id:"xref_car_insurance_income",title:"Car insurance CPI growth vs. median income change 2000â€“2024",sub:"Insurance tripled. Median income barely doubled. Lower-income drivers spend 8%+ of income on insurance.",type:"CHART",geo:"us_national",fmt:"Line chart",tbl:"T770 Â· T727",section:"Prices Â· Income",ext:["FRED: any national economic time series (fred.stlouisfed.org â€” free API)","BLS national data: employment, wages, CPI (bls.gov â€” free API)"],vars:["motor_vehicle_insurance_cpi","median_household_income"],join:["gasoline_price_regular","all_items_cpi"],sc:{emotional:8,relatability:9,surprise:8,tension:6,visual:8,data_ready:9,originality:8},vs:80,tags:"car insurance income burden CPI growth regressive low income driver transportation cost living squeeze"}







,{id:"xref_defense_education",title:"Defense spending per capita vs. K-12 per-pupil spending by state",sub:"Virginia spends $14K per pupil on education and $4,500 per capita on defense. Mississippi: $11K education, $700 defense.",type:"XREF",geo:"us_state",fmt:"Quadrant chart",tbl:"T543 Â· T258",section:"Military Â· Education",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)"],vars:["defense_budget_total","expenditure_per_pupil"],join:["avg_teacher_salary","rep_pct"],sc:{emotional:8,relatability:7,surprise:8,tension:7,visual:8,data_ready:9,originality:8},vs:76,tags:"defense education spending tradeoff state military schools budget priorities Virginia Mississippi guns butter"}







,{id:"xref_credit_card_snap",title:"Credit card interest rate growth vs. SNAP enrollment",sub:"As credit cards hit 22.9% APR, SNAP enrollment surged. Debt as driver of food insecurity.",type:"CHART",geo:"us_national",fmt:"Line chart",tbl:"T1223 Â· T577",section:"Banking Â· Social Insurance",ext:["FRED: any national economic time series (fred.stlouisfed.org â€” free API)","BLS national data: employment, wages, CPI (bls.gov â€” free API)"],vars:["credit_card_rate_all_accounts","pct_on_snap"],join:["median_household_income","total_consumer_credit"],sc:{emotional:9,relatability:8,surprise:8,tension:8,visual:7,data_ready:10,originality:9},vs:80,tags:"credit card interest rate SNAP food stamps debt food insecurity connection low income household stress poverty"}







,{id:"murder_rate_by_state",title:"Murder rate by state 2023 â€” the violence geography nobody sees",sub:"Louisiana murder rate: 19/100K. New Hampshire: 1.1/100K. The 17x gap within the same country.",type:"MAP",geo:"us_state",fmt:"State choropleth",tbl:"T340",section:"Crime",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)","FBI Crime Data Explorer: UCR/NIBRS by state/agency (cde.ucr.cjis.gov â€” free)"],vars:["murder_rate","violent_crime_rate"],join:["median_household_income","rep_pct","pct_bachelors","state_unemployment_rate"],sc:{emotional:9,relatability:8,surprise:7,tension:8,visual:9,data_ready:10,originality:5},vs:82,tags:"murder homicide rate state Louisiana New Hampshire inequality poverty race geography crime South violence policy policing guns"}







,{id:"city_crime_ranked",title:"Highest and lowest violent crime rates in large US cities 2023",sub:"The safest and most dangerous cities â€” by the actual numbers, not the perception.",type:"RANK",geo:"us_city",fmt:"Ranked list",tbl:"T341",section:"Crime",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","FBI Crime Data Explorer: UCR/NIBRS by state/agency (cde.ucr.cjis.gov â€” free)"],vars:["violent_crime_rate"],join:["median_household_income"],sc:{emotional:8,relatability:9,surprise:7,tension:7,visual:9,data_ready:10,originality:5},vs:80,tags:"crime city violence safe dangerous urban policing race inequality murder poverty real estate neighborhood"}







,{id:"map_disposable_income",title:"Disposable personal income per capita by state vs. US average",sub:"Connecticut: 136% of US average. Mississippi: 73%. The disposable income divide, normalized.",type:"MAP",geo:"us_state",fmt:"State choropleth",tbl:"T725",section:"Income",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)"],vars:["disposable_income_per_capita"],join:["median_household_income","pct_on_snap","rep_pct"],sc:{emotional:7,relatability:8,surprise:6,tension:5,visual:9,data_ready:10,originality:5},vs:72,tags:"disposable income state Connecticut Mississippi index per capita wealth inequality spending power"}







,{id:"map_manufacturing_gdp_share",title:"Manufacturing as share of state GDP 2023",sub:"Indiana: 28% of GDP is manufacturing. Hawaii: 2%. The industrial geography of America.",type:"MAP",geo:"us_state",fmt:"State choropleth",tbl:"T712",section:"Income",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)"],vars:["state_gdp_per_capita"],join:["foreign_affiliate_employment","state_unemployment_rate"],sc:{emotional:6,relatability:7,surprise:7,tension:5,visual:9,data_ready:10,originality:6},vs:70,tags:"manufacturing GDP state share Indiana Ohio Michigan Tennessee South Carolina industrial economy reshoring jobs"}







,{id:"high_school_sports_vs_mlb",title:"High school sports attendance vs. major professional leagues 2025",sub:"38M fans attended high school events. MLB drew 71M. Your local varsity game is America's #2 sport.",type:"RANK",geo:"us_national",fmt:"Ranked list",tbl:"T1273",section:"Arts Recreation",ext:["FRED: any national economic time series (fred.stlouisfed.org â€” free API)","BLS national data: employment, wages, CPI (bls.gov â€” free API)"],vars:["sports_attendance_12mo"],join:[],sc:{emotional:6,relatability:9,surprise:9,tension:2,visual:9,data_ready:10,originality:8},vs:79,tags:"high school sports attendance MLB NBA NFL college professional leagues comparison America local community fans surprising"}







,{id:"xref_rd_income_state",title:"Business R&D intensity vs. median income by state",sub:"Washington ($77 R&D per $1K GDP) has $91K median income. Mississippi ($3/1K) has $54K. Research pays.",type:"XREF",geo:"us_state",fmt:"Scatter plot",tbl:"T844 Â· T727",section:"Science Â· Income",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)"],vars:["rd_pct_gdp","median_household_income"],join:["pct_bachelors","state_gdp_per_capita"],sc:{emotional:7,relatability:6,surprise:7,tension:5,visual:7,data_ready:10,originality:7},vs:72,tags:"R&D research income state wealth innovation economy Washington Massachusetts productivity knowledge workers"}







,{id:"xref_rd_vote",title:"State R&D spending intensity vs. Republican vote share",sub:"High-R&D states vote Democratic. Low-R&D states vote Republican. The knowledge economy politics map.",type:"XREF",geo:"us_state",fmt:"Scatter plot",tbl:"T844 Â· T454",section:"Science Â· Elections",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)","MIT Election Lab: presidential/congressional results (electionlab.mit.edu â€” free)"],vars:["rd_pct_gdp","rep_pct"],join:["pct_bachelors","median_household_income"],sc:{emotional:7,relatability:6,surprise:7,tension:7,visual:7,data_ready:10,originality:7},vs:74,tags:"R&D research Republican vote knowledge economy innovation state technology workers education politics"}







,{id:"federal_debt_pct_gdp",title:"Federal debt as % of GDP 1960â€“2024",sub:"1960: 54% of GDP. 2024: 122% of GDP. The most important fiscal chart in America, with 60 years of history.",type:"CHART",geo:"us_national",fmt:"Area chart",tbl:"T509",section:"Federal Government Finances",ext:["FRED: any national economic time series (fred.stlouisfed.org â€” free API)","BLS national data: employment, wages, CPI (bls.gov â€” free API)"],vars:["federal_debt_pct_gdp"],join:["federal_outlays_by_function","federal_tax_revenue_type"],sc:{emotional:8,relatability:7,surprise:7,tension:9,visual:8,data_ready:10,originality:5},vs:78,tags:"federal debt GDP deficit national debt 1960 2024 history fiscal crisis Republicans Democrats spending Congress"}







,{id:"federal_interest_vs_education",title:"Federal interest payments vs. education spending 2000â€“2024",sub:"Net interest on the debt: $879.9B in 2024. Federal education spending: $306B. We now pay 3x more in interest than we spend on education.",type:"CHART",geo:"us_national",fmt:"Line chart",tbl:"T510 Â· T512",section:"Federal Government Finances",ext:["FRED: any national economic time series (fred.stlouisfed.org â€” free API)","BLS national data: employment, wages, CPI (bls.gov â€” free API)"],vars:["federal_outlays_by_function"],join:["college_tuition_cpi","student_loans_outstanding"],sc:{emotional:9,relatability:8,surprise:9,tension:9,visual:8,data_ready:10,originality:8},vs:85,tags:"federal interest debt education spending comparison 2024 $879B fiscal crisis Congress priorities students"}







,{id:"federal_spending_by_function",title:"What does the US government actually spend money on? 2024",sub:"Payments to individuals: $4.45T. Defense: $873B. Interest: $880B. Everything else: $1.5T.",type:"CHART",geo:"us_national",fmt:"Treemap",tbl:"T512",section:"Federal Government Finances",ext:["FRED: any national economic time series (fred.stlouisfed.org â€” free API)","BLS national data: employment, wages, CPI (bls.gov â€” free API)"],vars:["federal_outlays_by_function"],join:["federal_debt_pct_gdp","defense_budget_total"],sc:{emotional:8,relatability:7,surprise:7,tension:7,visual:9,data_ready:10,originality:5},vs:77,tags:"federal spending budget function defense Medicare Social Security interest breakdown 2024 where money goes"}







,{id:"federal_civilian_employment_state",title:"Federal civilian employees by state 2024",sub:"DC: 162K. Maryland: 144K. Virginia: probably #3. The federal workforce geography.",type:"MAP",geo:"us_state",fmt:"State choropleth",tbl:"T537",section:"Federal Government Finances",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)"],vars:["federal_civilian_employment_state"],join:["total_transfers_per_capita","rep_pct","median_household_income"],sc:{emotional:6,relatability:6,surprise:7,tension:5,visual:9,data_ready:10,originality:7},vs:71,tags:"federal employees government workers state DC Maryland Virginia geography workers jobs economy federal workforce"}







,{id:"xref_federal_workers_vote",title:"Federal civilian employees per capita vs. Republican vote share by state",sub:"States with the most federal workers per capita vote Democratic. The government employment-politics map.",type:"XREF",geo:"us_state",fmt:"Scatter plot",tbl:"T537 Â· T454",section:"Federal Govt Â· Elections",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)","MIT Election Lab: presidential/congressional results (electionlab.mit.edu â€” free)"],vars:["federal_civilian_employment_state","rep_pct"],join:["total_transfers_per_capita","median_household_income"],sc:{emotional:7,relatability:6,surprise:7,tension:7,visual:7,data_ready:10,originality:7},vs:73,tags:"federal workers government employees Republican vote DC Maryland Virginia political geography employment federal"}







,{id:"federal_payments_for_individuals",title:"Federal payments for individuals by program 2000â€“2024",sub:"Social Security: $1.46T. Medicare: ~$1.03T. Interest on debt: $880B. The federal government is primarily a benefits + debt machine.",type:"CHART",geo:"us_national",fmt:"Area chart",tbl:"T513",section:"Federal Government Finances",ext:["FRED: any national economic time series (fred.stlouisfed.org â€” free API)","BLS national data: employment, wages, CPI (bls.gov â€” free API)"],vars:["federal_outlays_by_function","total_transfers_per_capita"],join:["total_medicare","pct_on_snap","pct_on_medicaid"],sc:{emotional:8,relatability:7,surprise:7,tension:8,visual:8,data_ready:10,originality:5},vs:75,tags:"federal payments Social Security Medicare Medicaid individuals programs 2024 spending history growth aging"}







,{id:"unclaimed_tax_refunds",title:"Unclaimed IRS tax refunds by state 2021",sub:"1.14 million Americans left $1.025B in IRS refunds unclaimed. Median unclaimed refund: $781.",type:"MAP",geo:"us_state",fmt:"State choropleth",tbl:"T534",section:"Federal Government Finances",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)"],vars:["federal_agi_by_state"],join:["median_household_income","pct_on_snap"],sc:{emotional:7,relatability:9,surprise:9,tension:2,visual:9,data_ready:10,originality:9},vs:78,tags:"unclaimed tax refund IRS state money left over 2021 free money surprising geography low income workers"}







,{id:"tax_refunds_by_state",title:"Federal tax refunds issued by state 2024",sub:"US total: $552.6B in refunds. California: $47.4B. Florida: $33.1B. The tax refund geography.",type:"MAP",geo:"us_state",fmt:"State choropleth",tbl:"T533",section:"Federal Government Finances",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)"],vars:["federal_agi_by_state"],join:["median_household_income","rep_pct"],sc:{emotional:6,relatability:8,surprise:6,tension:3,visual:9,data_ready:10,originality:6},vs:68,tags:"tax refunds state IRS 2024 California Florida New York income geography per capita returns"}







,{id:"agi_per_return_by_state",title:"Average adjusted gross income per tax return by state 2022",sub:"Connecticut: $119K average AGI. Mississippi: $45K. The income tax return geography of America.",type:"MAP",geo:"us_state",fmt:"State choropleth",tbl:"T532",section:"Federal Government Finances",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)"],vars:["federal_agi_by_state"],join:["median_household_income","pct_families_own_stocks"],sc:{emotional:7,relatability:7,surprise:7,tension:5,visual:9,data_ready:10,originality:6},vs:72,tags:"AGI adjusted gross income tax return state Connecticut Mississippi inequality wealth geography IRS"}







,{id:"lottery_revenue_per_capita",title:"State lottery revenue per capita 2023",sub:"Florida lottery: $9.43B. California: $9.26B. The regressive tax that funds education â€” and who pays it.",type:"MAP",geo:"us_state",fmt:"State choropleth",tbl:"T493",section:"State & Local Govt",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)"],vars:["lottery_revenue_per_capita"],join:["pct_on_snap","median_household_income","rep_pct"],sc:{emotional:8,relatability:8,surprise:7,tension:7,visual:9,data_ready:10,originality:7},vs:79,tags:"lottery revenue state per capita regressive tax poor gambling Florida California New York education funding"}







,{id:"sports_betting_revenue_state",title:"Sports betting tax revenue by state 2023",sub:"Illinois: $161M. New Jersey: largest market. The new state revenue stream that went from zero to $2.2B nationwide since 2018.",type:"MAP",geo:"us_state",fmt:"State choropleth",tbl:"T493",section:"State & Local Govt",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)"],vars:["sports_betting_revenue"],join:["lottery_revenue_per_capita","median_household_income"],sc:{emotional:7,relatability:8,surprise:8,tension:4,visual:9,data_ready:10,originality:8},vs:75,tags:"sports betting revenue state tax 2023 New Jersey Illinois gambling legalization 2018 growth income"}







,{id:"xref_lottery_poverty",title:"Lottery revenue per capita vs. poverty rate by state",sub:"The states with the most poverty spend the most on lottery tickets per person. The regressive tax, mapped.",type:"XREF",geo:"us_state",fmt:"Scatter plot",tbl:"T493 Â· T727",section:"State Govt Â· Income",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)"],vars:["lottery_revenue_per_capita","median_household_income"],join:["pct_on_snap","rep_pct"],sc:{emotional:9,relatability:8,surprise:7,tension:8,visual:8,data_ready:10,originality:8},vs:81,tags:"lottery poverty regressive tax poor gambling spending income inequality state hope ticket desperation"}







,{id:"state_local_taxes_by_city",title:"Total state and local tax burden for a family of three â€” by major city",sub:"Detroit family at $75K: pays $12,246 in taxes. Houston: $4,680. The 2.6x tax burden gap within America.",type:"RANK",geo:"us_city",fmt:"Bar chart",tbl:"T491",section:"State & Local Govt",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)"],vars:["state_local_revenue_per_capita"],join:["median_household_income","rep_pct"],sc:{emotional:8,relatability:9,surprise:8,tension:6,visual:9,data_ready:10,originality:8},vs:82,tags:"state local taxes family city Detroit Houston Baltimore Chicago Atlanta tax burden comparison blue red state"}







,{id:"state_general_fund_balance",title:"State general fund surplus or deficit by state 2023â€“2024",sub:"California surplus: $47B in 2023 â†’ $13B in 2024. Alaska running a deficit. The fiscal health map.",type:"MAP",geo:"us_state",fmt:"State choropleth",tbl:"T495",section:"State & Local Govt",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)"],vars:["state_local_revenue_per_capita"],join:["state_local_debt_per_capita","rep_pct"],sc:{emotional:7,relatability:7,surprise:7,tension:6,visual:9,data_ready:10,originality:7},vs:73,tags:"state budget surplus deficit fiscal health California Alaska 2024 general fund balance spending tax revenue"}







,{id:"state_local_revenue_per_capita",title:"State and local government revenue per capita by state 2022",sub:"Alaska: $42K revenue per person. California: $19K. Mississippi: $14K. Public resources vary enormously.",type:"MAP",geo:"us_state",fmt:"State choropleth",tbl:"T488",section:"State & Local Govt",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)"],vars:["state_local_revenue_per_capita"],join:["median_household_income","rep_pct","expenditure_per_pupil"],sc:{emotional:7,relatability:7,surprise:7,tension:5,visual:9,data_ready:10,originality:6},vs:72,tags:"state local government revenue per capita Alaska California Mississippi public resources spending infrastructure services"}







,{id:"state_local_debt_per_capita",title:"State and local government debt per capita 2022",sub:"Connecticut: $20K+ per person in state/local debt. Wyoming: under $5K. The public debt geography.",type:"MAP",geo:"us_state",fmt:"State choropleth",tbl:"T486",section:"State & Local Govt",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)"],vars:["state_local_debt_per_capita"],join:["state_local_revenue_per_capita","median_household_income","rep_pct"],sc:{emotional:7,relatability:7,surprise:7,tension:6,visual:9,data_ready:10,originality:6},vs:72,tags:"state local debt per capita Connecticut Wyoming fiscal liability public bonds infrastructure pension obligations"}







,{id:"state_local_workers_wages",title:"State and local government workers' average monthly earnings by state 2024",sub:"California state worker: $8,979/month. Alabama: $6,161/month. The public sector pay gap.",type:"MAP",geo:"us_state",fmt:"State choropleth",tbl:"T505",section:"State & Local Govt",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)"],vars:["state_local_avg_earnings"],join:["median_household_income","avg_teacher_salary","rep_pct"],sc:{emotional:6,relatability:7,surprise:6,tension:5,visual:8,data_ready:10,originality:5},vs:67,tags:"state local government workers wages salary California Alabama monthly earnings public sector pay equity"}







,{id:"xref_state_taxes_vote",title:"State and local tax burden vs. Republican vote share by state",sub:"High-tax states vote Democratic. Low-tax states vote Republican. But low-tax states get more federal aid.",type:"XREF",geo:"us_state",fmt:"Scatter plot",tbl:"T491 Â· T454",section:"State Govt Â· Elections",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)","MIT Election Lab: presidential/congressional results (electionlab.mit.edu â€” free)"],vars:["state_local_revenue_per_capita","rep_pct"],join:["total_transfers_per_capita","median_household_income"],sc:{emotional:8,relatability:7,surprise:6,tension:8,visual:7,data_ready:10,originality:6},vs:75,tags:"state tax burden Republican vote blue red state high low tax Connecticut Mississippi political economy"}







,{id:"manufacturing_jobs_collapse",title:"US manufacturing employment 2000â€“2024: the 5 million job collapse",sub:"17.3M manufacturing jobs in 2000. 12.8M today. The jobs that left and barely came back.",type:"CHART",geo:"us_national",fmt:"Area chart",tbl:"T1064",section:"Manufactures",ext:["FRED: any national economic time series (fred.stlouisfed.org â€” free API)","BLS national data: employment, wages, CPI (bls.gov â€” free API)"],vars:["manufacturing_employment_trend"],join:["state_unemployment_rate","foreign_affiliate_employment"],sc:{emotional:8,relatability:8,surprise:6,tension:8,visual:8,data_ready:10,originality:4},vs:76,tags:"manufacturing jobs decline 2000 2010 2024 Rust Belt trade China NAFTA offshoring reshoring recovery CHIPS"}







,{id:"manufacturing_wages_by_state",title:"Average manufacturing hourly wages by state 2024",sub:"Colorado: $32.52/hr. Connecticut: $31.38. Arkansas: $22.44. The factory pay gap within America.",type:"MAP",geo:"us_state",fmt:"State choropleth",tbl:"T1067",section:"Manufactures",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)"],vars:["manufacturing_hourly_wages_state"],join:["median_household_income","state_unemployment_rate","rep_pct"],sc:{emotional:7,relatability:8,surprise:7,tension:5,visual:9,data_ready:10,originality:6},vs:74,tags:"manufacturing wages hourly pay state Colorado Connecticut Arkansas factory workers industrial pay equity inequality"}







,{id:"xref_manufacturing_wages_income",title:"Manufacturing hourly wages vs. median household income by state",sub:"States with high manufacturing wages have higher median incomes. But the correlation isn't as tight as you'd expect.",type:"XREF",geo:"us_state",fmt:"Scatter plot",tbl:"T1067 Â· T727",section:"Manufactures Â· Income",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)"],vars:["manufacturing_hourly_wages_state","median_household_income"],join:["rep_pct","state_unemployment_rate"],sc:{emotional:7,relatability:7,surprise:7,tension:5,visual:7,data_ready:10,originality:6},vs:71,tags:"manufacturing wages household income state correlation factory workers pay median income wealth industrial"}







,{id:"manufacturing_value_added_state",title:"Manufacturing value added by state 2021",sub:"Texas: $330B value added. Indiana: $130B. 28% of Indiana's entire GDP comes from manufacturing.",type:"MAP",geo:"us_state",fmt:"State choropleth",tbl:"T1062",section:"Manufactures",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)"],vars:["manufacturing_value_added_state"],join:["state_gdp_per_capita","foreign_affiliate_employment"],sc:{emotional:6,relatability:6,surprise:7,tension:4,visual:9,data_ready:10,originality:6},vs:68,tags:"manufacturing value added state Texas Indiana GDP industrial economy production reshoring factories workers"}







,{id:"xref_manufacturing_employment_vote",title:"Manufacturing employment share vs. 2024 Republican vote share by state",sub:"Manufacturing-heavy states swung hardest toward Trump in 2016 and haven't swung back.",type:"XREF",geo:"us_state",fmt:"Scatter plot",tbl:"T1062 Â· T454",section:"Manufactures Â· Elections",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)","MIT Election Lab: presidential/congressional results (electionlab.mit.edu â€” free)"],vars:["manufacturing_employment_trend","rep_pct"],join:["state_unemployment_rate","foreign_affiliate_employment"],sc:{emotional:9,relatability:8,surprise:6,tension:9,visual:8,data_ready:10,originality:7},vs:80,tags:"manufacturing employment Republican vote Rust Belt Trump 2016 2024 Ohio Michigan Wisconsin Indiana political economy"}







,{id:"xref_manufacturing_wages_vote",title:"Manufacturing hourly wages vs. Republican vote share by state",sub:"Lower manufacturing wages â†’ more Republican. The forgotten worker political economy, state by state.",type:"XREF",geo:"us_state",fmt:"Scatter plot",tbl:"T1067 Â· T454",section:"Manufactures Â· Elections",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)","MIT Election Lab: presidential/congressional results (electionlab.mit.edu â€” free)"],vars:["manufacturing_hourly_wages_state","rep_pct"],join:["median_household_income","state_unemployment_rate"],sc:{emotional:8,relatability:7,surprise:7,tension:8,visual:7,data_ready:10,originality:7},vs:76,tags:"manufacturing wages Republican vote state workers factory pay political economy resentment low wage Trump"}







,{id:"manufacturing_employment_by_industry",title:"Manufacturing employment by industry 2000â€“2024: who survived the collapse",sub:"Computer/electronics: held steady. Apparel: down 85%. Motor vehicles: down then back up. The sectoral story.",type:"CHART",geo:"us_national",fmt:"Line chart",tbl:"T1064",section:"Manufactures",ext:["FRED: any national economic time series (fred.stlouisfed.org â€” free API)","BLS national data: employment, wages, CPI (bls.gov â€” free API)"],vars:["manufacturing_employment_trend"],join:[],sc:{emotional:7,relatability:6,surprise:8,tension:6,visual:8,data_ready:10,originality:7},vs:72,tags:"manufacturing industry employment apparel electronics auto vehicles decline survivors sectors 2000 2024 collapse"}







,{id:"retail_sales_per_capita_growth",title:"Per capita retail sales 2000â€“2022: the $10K to $20K doubling",sub:"Americans spent $10,331 per person on retail in 2000. $20,752 in 2022. But real wages barely grew.",type:"CHART",geo:"us_national",fmt:"Line chart",tbl:"T1090",section:"Wholesale & Retail Trade",ext:["FRED: any national economic time series (fred.stlouisfed.org â€” free API)","BLS national data: employment, wages, CPI (bls.gov â€” free API)"],vars:["retail_sales_per_capita"],join:["median_household_income","all_items_cpi"],sc:{emotional:7,relatability:8,surprise:6,tension:6,visual:7,data_ready:10,originality:5},vs:68,tags:"retail sales per capita growth 2000 2022 consumer spending wages inflation e-commerce economy household"}







,{id:"ecommerce_vs_traditional_retail",title:"E-commerce penetration by retail category â€” what moved online and what didn't",sub:"Clothing: 95% e-commerce. Books: 95%. Drugs and health: only 31%. The uneven digitization of shopping.",type:"CHART",geo:"us_national",fmt:"Ranked list",tbl:"T1093",section:"Wholesale & Retail Trade",ext:["FRED: any national economic time series (fred.stlouisfed.org â€” free API)","BLS national data: employment, wages, CPI (bls.gov â€” free API)"],vars:["ecommerce_sales"],join:[],sc:{emotional:6,relatability:9,surprise:8,tension:3,visual:9,data_ready:10,originality:7},vs:74,tags:"e-commerce online shopping category clothing books drugs health beauty Amazon retail digital physical stores"}







,{id:"wholesale_sales_trillion",title:"US merchant wholesale trade 2022: the $8T invisible economy",sub:"$8.06T in wholesale trade. More than half of all US GDP flows through wholesalers nobody sees.",type:"CHART",geo:"us_national",fmt:"Treemap",tbl:"T1083",section:"Wholesale & Retail Trade",ext:["FRED: any national economic time series (fred.stlouisfed.org â€” free API)","BLS national data: employment, wages, CPI (bls.gov â€” free API)"],vars:["wholesale_employees_state"],join:["port_total_tons","foreign_affiliate_employment"],sc:{emotional:5,relatability:5,surprise:8,tension:2,visual:8,data_ready:10,originality:8},vs:65,tags:"wholesale trade $8T trillion economy invisible supply chain food drugs industrial machinery sectors"}







,{id:"gasoline_station_retail_per_capita",title:"Per capita gasoline station sales 2000â€“2022",sub:"Gas station retail: $880 per person in 2000 â†’ $2,203 in 2022. The spike is inflation, not miles driven.",type:"CHART",geo:"us_national",fmt:"Line chart",tbl:"T1090",section:"Wholesale & Retail Trade",ext:["FRED: any national economic time series (fred.stlouisfed.org â€” free API)","BLS national data: employment, wages, CPI (bls.gov â€” free API)"],vars:["retail_sales_per_capita","gasoline_price_regular"],join:["all_items_cpi","energy_consumption_per_capita"],sc:{emotional:7,relatability:8,surprise:7,tension:4,visual:7,data_ready:10,originality:6},vs:68,tags:"gasoline retail sales per capita inflation 2000 2022 price spike driving consumer spending fuel"}







,{id:"xref_medicare_vote",title:"Medicare enrollment rate vs. Republican vote share by state",sub:"The states most reliant on Medicare vote most reliably Republican â€” and to cut it.",type:"XREF",geo:"us_state",fmt:"Scatter plot",tbl:"T150 Â· T454",section:"Health Â· Elections",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)","CDC WONDER: mortality + disease rates by county/state (wonder.cdc.gov â€” free)","MIT Election Lab: presidential/congressional results (electionlab.mit.edu â€” free)"],vars:["total_medicare","rep_pct"],join:["pct_on_medicaid","total_transfers_per_capita"],sc:{emotional:9,relatability:7,surprise:7,tension:10,visual:8,data_ready:10,originality:7},vs:84,tags:"Medicare Republican vote paradox healthcare elderly Southern states red states ACA cut funding aging"}







,{id:"xref_health_spending_vote",title:"Per capita health spending vs. Republican vote share by state",sub:"Low-spending red states vote against healthcare expansion. The coverage gap is political.",type:"XREF",geo:"us_state",fmt:"Scatter plot",tbl:"T141 Â· T454",section:"Health Â· Elections",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)","CDC WONDER: mortality + disease rates by county/state (wonder.cdc.gov â€” free)","MIT Election Lab: presidential/congressional results (electionlab.mit.edu â€” free)"],vars:["per_capita_health_spending","rep_pct"],join:["pct_on_medicaid","total_medicare"],sc:{emotional:8,relatability:7,surprise:7,tension:9,visual:7,data_ready:9,originality:7},vs:79,tags:"health spending Republican vote ACA Medicaid expansion red states coverage gap insurance healthcare politics"}







,{id:"xref_medicaid_unmarried_births",title:"Medicaid enrollment rate vs. births to unmarried mothers by state",sub:"Both highest in same states. Medical and family poverty overlap completely.",type:"XREF",geo:"us_state",fmt:"Bivariate choropleth",tbl:"T576 Â· T87",section:"Health Â· Births",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)","CDC WONDER: mortality + disease rates by county/state (wonder.cdc.gov â€” free)"],vars:["pct_on_medicaid","pct_births_unmarried"],join:["median_household_income","teen_birth_rate","rep_pct"],sc:{emotional:8,relatability:7,surprise:6,tension:8,visual:9,data_ready:10,originality:7},vs:78,tags:"Medicaid births unmarried mothers poverty healthcare South Mississippi West Virginia overlap geography state"}







,{id:"xref_birth_rate_vote",title:"State birth rate vs. Republican vote share 2024",sub:"The most Republican states have the highest birth rates. Demographic destiny and political geography.",type:"XREF",geo:"us_state",fmt:"Scatter plot",tbl:"T81 Â· T454",section:"Births Â· Elections",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)","MIT Election Lab: presidential/congressional results (electionlab.mit.edu â€” free)"],vars:["birth_rate_state","rep_pct"],join:["total_fertility_rate_by_race","pct_births_unmarried"],sc:{emotional:7,relatability:7,surprise:7,tension:6,visual:7,data_ready:10,originality:6},vs:73,tags:"birth rate Republican vote demographics political geography fertility population growth South rural religion"}







,{id:"xref_fertility_vote",title:"Total fertility rate vs. Republican vote share by state",sub:"Red states are having more babies than blue states. The electoral math of demographic divergence.",type:"XREF",geo:"us_state",fmt:"Scatter plot",tbl:"T85 Â· T454",section:"Births Â· Elections",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)","MIT Election Lab: presidential/congressional results (electionlab.mit.edu â€” free)"],vars:["total_fertility_rate_by_race","rep_pct"],join:["birth_rate_state","median_household_income"],sc:{emotional:7,relatability:7,surprise:7,tension:6,visual:7,data_ready:9,originality:6},vs:72,tags:"fertility Republican vote demographics electoral geography population growth red blue state political future"}







,{id:"xref_home_prices_snap",title:"Home price index vs. SNAP enrollment rate by state",sub:"As housing gets more expensive, food insecurity rises in the same places. The affordability-hunger squeeze.",type:"XREF",geo:"us_state",fmt:"Scatter plot",tbl:"T771 Â· T576",section:"Housing Â· Social Insurance",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)","HUD Fair Market Rents + housing data by state/county (huduser.gov â€” free)"],vars:["home_price_index_2024","pct_on_snap"],join:["median_household_income","housing_permits_total"],sc:{emotional:8,relatability:8,surprise:7,tension:7,visual:7,data_ready:10,originality:7},vs:75,tags:"housing prices SNAP food stamps affordability squeeze cost of living housing crisis poverty food insecurity state"}







,{id:"xref_housing_permits_unemployment",title:"New housing permits vs. unemployment rate by state",sub:"States building more housing have lower unemployment. The housing-jobs connection.",type:"XREF",geo:"us_state",fmt:"Scatter plot",tbl:"T1011 Â· T629",section:"Housing Â· Labor",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)","HUD Fair Market Rents + housing data by state/county (huduser.gov â€” free)"],vars:["housing_permits_total","state_unemployment_rate"],join:["median_household_income","population_pct_change"],sc:{emotional:6,relatability:7,surprise:6,tension:4,visual:7,data_ready:10,originality:6},vs:67,tags:"housing permits unemployment jobs construction labor market state supply economic activity growth"}







,{id:"xref_veterans_benefits_vote",title:"Veterans benefits per capita vs. Republican vote share by state",sub:"States most dependent on veterans benefits vote most reliably Republican â€” and against VA funding.",type:"XREF",geo:"us_state",fmt:"Scatter plot",tbl:"T573 Â· T454",section:"Social Insurance Â· Elections",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)","MIT Election Lab: presidential/congressional results (electionlab.mit.edu â€” free)"],vars:["veterans_benefits","rep_pct"],join:["retired_military_count","total_transfers_per_capita"],sc:{emotional:7,relatability:6,surprise:6,tension:7,visual:7,data_ready:10,originality:6},vs:72,tags:"veterans benefits Republican vote military communities Southern states red states political geography identity"}







,{id:"xref_unemployment_insurance_vote",title:"Unemployment insurance benefits per capita vs. Republican vote share",sub:"Unemployment benefits flow to red states. The safety net paradox continues.",type:"XREF",geo:"us_state",fmt:"Scatter plot",tbl:"T573 Â· T454",section:"Social Insurance Â· Elections",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)","MIT Election Lab: presidential/congressional results (electionlab.mit.edu â€” free)"],vars:["total_transfers_per_capita","rep_pct"],join:["state_unemployment_rate","median_household_income"],sc:{emotional:8,relatability:7,surprise:7,tension:9,visual:7,data_ready:10,originality:7},vs:76,tags:"unemployment insurance benefits Republican vote paradox safety net red states fiscal dependency"}







,{id:"xref_bachelors_unemployment",title:"College degree rate vs. unemployment rate by state",sub:"States with more college graduates have lower unemployment. But some high-ed states still struggle.",type:"XREF",geo:"us_state",fmt:"Scatter plot",tbl:"T254 Â· T629",section:"Education Â· Labor",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)"],vars:["pct_bachelors","state_unemployment_rate"],join:["median_household_income","rep_pct"],sc:{emotional:7,relatability:7,surprise:5,tension:5,visual:7,data_ready:10,originality:4},vs:68,tags:"education college degree unemployment labor market state economic mobility income inequality human capital"}







,{id:"xref_teacher_salary_unemployment",title:"Teacher salary vs. state unemployment rate",sub:"States that pay teachers well tend to have lower unemployment. The education-economy link.",type:"XREF",geo:"us_state",fmt:"Scatter plot",tbl:"T268 Â· T629",section:"Education Â· Labor",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)"],vars:["avg_teacher_salary","state_unemployment_rate"],join:["expenditure_per_pupil","median_household_income"],sc:{emotional:6,relatability:7,surprise:6,tension:4,visual:7,data_ready:10,originality:6},vs:66,tags:"teacher salary unemployment state economic activity labor market education spending human capital schools"}







,{id:"xref_elevation_vote",title:"Mean state elevation vs. Republican vote share",sub:"The most mountainous states lean Republican (Wyoming, Idaho) â€” except Colorado. Altitude and politics.",type:"XREF",geo:"us_state",fmt:"Scatter plot",tbl:"T410 Â· T454",section:"Geography Â· Elections",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)","MIT Election Lab: presidential/congressional results (electionlab.mit.edu â€” free)"],vars:["mean_elevation","rep_pct"],join:["energy_consumption_per_capita","median_household_income"],sc:{emotional:5,relatability:5,surprise:8,tension:4,visual:7,data_ready:10,originality:9},vs:66,tags:"elevation mountains Republican vote geography altitude Wyoming Idaho Colorado outlier political geography curious"}







,{id:"xref_coastline_income",title:"Coastal access per capita vs. median income by state",sub:"Coastal states are mostly wealthy â€” but Alaska has the most coast and is middle-income. The outlier map.",type:"XREF",geo:"us_state",fmt:"Scatter plot",tbl:"T408 Â· T727",section:"Geography Â· Income",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)"],vars:["coastline_miles","median_household_income"],join:["real_per_capita_income"],sc:{emotional:5,relatability:6,surprise:7,tension:3,visual:7,data_ready:10,originality:8},vs:65,tags:"coastline income state Alaska coastal wealth geography access ocean outlier middle income correlation"}







,{id:"voter_turnout_by_age_race",title:"Voter registration and turnout gap by race and age 2024",sub:"White 65+ turnout: 78%. Hispanic 18-24 turnout: 28%. The democracy participation gap by identity.",type:"CHART",geo:"us_national",fmt:"Bar chart",tbl:"T448",section:"Elections",ext:["FRED: any national economic time series (fred.stlouisfed.org â€” free API)","BLS national data: employment, wages, CPI (bls.gov â€” free API)","MIT Election Lab: presidential/congressional results (electionlab.mit.edu â€” free)"],vars:["pct_voted_state","pct_registered_state"],join:["rep_pct","median_household_income"],sc:{emotional:8,relatability:7,surprise:6,tension:8,visual:8,data_ready:10,originality:5},vs:77,tags:"voter turnout race age registration gap democracy Hispanic Black White Asian elderly youth 2024 inequality"}







,{id:"map_state_gdp_per_capita_2023",title:"State GDP per capita 2023 â€” the economic geography of America",sub:"New York: $107K per person. Mississippi: $45K. A 2.4x gap in economic output within one country.",type:"MAP",geo:"us_state",fmt:"State choropleth",tbl:"T715",section:"Income",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)"],vars:["state_gdp_per_capita"],join:["median_household_income","pct_bachelors","rep_pct"],sc:{emotional:7,relatability:8,surprise:5,tension:5,visual:9,data_ready:10,originality:3},vs:69,tags:"GDP per capita state economic output productivity wealth New York Mississippi California Texas income"}







,{id:"foreign_jobs_vs_vote",title:"Foreign company employment share vs. Republican vote share by state",sub:"South Carolina: 8% foreign-employed, deeply Republican. Workers at BMW and Volvo vote against free trade.",type:"XREF",geo:"us_state",fmt:"Scatter plot",tbl:"T1311 Â· T454",section:"Trade Â· Elections",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)","MIT Election Lab: presidential/congressional results (electionlab.mit.edu â€” free)"],vars:["foreign_affiliate_employment","rep_pct"],join:["median_household_income","state_unemployment_rate"],sc:{emotional:8,relatability:7,surprise:8,tension:8,visual:7,data_ready:10,originality:8},vs:79,tags:"foreign jobs Republican vote South Carolina globalization paradox BMW Toyota Honda anti-trade voters workers"}







,{id:"mean_age_first_birth_trend",title:"Mean age at first birth by race 2000â€“2023",sub:"White women: average first birth at 30. Black women: 26. The age-at-first-birth gap drives economic divergence.",type:"CHART",geo:"us_national",fmt:"Line chart",tbl:"T80",section:"Births Deaths",ext:["FRED: any national economic time series (fred.stlouisfed.org â€” free API)","BLS national data: employment, wages, CPI (bls.gov â€” free API)"],vars:["birth_rate_state","total_fertility_rate_by_race"],join:["pct_births_unmarried","median_household_income"],sc:{emotional:7,relatability:7,surprise:6,tension:6,visual:7,data_ready:10,originality:7},vs:72,tags:"age first birth race women maternal fertility wealth inequality Black White Hispanic demographic social mobility career"}







,{id:"map_water_withdrawal_state",title:"Water withdrawal per day by state â€” where freshwater stress lives",sub:"California withdraws 26B gallons per day. Nevada withdraws more per capita than anywhere. The water crisis.",type:"MAP",geo:"us_state",fmt:"State choropleth",tbl:"T415",section:"Geography & Environment",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)"],vars:["mean_elevation"],join:["pct_cropland","energy_consumption_per_capita"],sc:{emotional:7,relatability:7,surprise:8,tension:7,visual:9,data_ready:10,originality:8},vs:76,tags:"water withdrawal freshwater stress California Nevada agriculture irrigation drought climate West scarcity geography"}







,{id:"abortion_drive_time",title:"Drive time to nearest abortion provider post-Dobbs by county",sub:"14 states have zero providers. Millions of women are 4+ hours from care. The access geography, county by county.",type:"MAP",geo:"us_county",fmt:"County choropleth",tbl:"T454 Â· T87",section:"Elections Â· Births",ext:["Guttmacher Institute abortion provider locations (publicly available)"],vars:["rep_pct","pct_births_unmarried"],join:["birth_rate_state","teen_birth_rate","median_household_income"],sc:{emotional:10,relatability:9,surprise:8,tension:10,visual:9,data_ready:8,originality:9},vs:96,tags:"abortion Dobbs Roe reproductive rights women access SCOTUS Trump red states pro-choice pro-life drive time county pgRouting distance"}







,{id:"golden_hour_ambulance",title:"Golden hour ambulance coverage by county â€” can you reach a trauma center in 60 minutes?",sub:"Millions of rural Americans live more than 60 minutes from a trauma center. The map that shows who gets a death sentence on the highway.",type:"MAP",geo:"us_county",fmt:"County choropleth",tbl:"T573 Â· T141",section:"Social Insurance Â· Health",ext:["HRSA trauma center locations (publicly available via data.hrsa.gov)"],vars:["total_transfers_per_capita","per_capita_health_spending"],join:["pct_on_medicaid","median_household_income","rep_pct"],sc:{emotional:10,relatability:9,surprise:8,tension:7,visual:9,data_ready:8,originality:8},vs:95,tags:"ambulance trauma center drive time golden hour rural healthcare access death highway county pgRouting emergency EMS"}







,{id:"nicu_drive_time",title:"Drive time to nearest NICU by county",sub:"How far is the nearest neonatal intensive care unit? For millions of rural families, it's too far.",type:"MAP",geo:"us_county",fmt:"County choropleth",tbl:"T150 Â· T87",section:"Health Â· Births",ext:["CMS NICU facility data (publicly available via CMS.gov)"],vars:["total_medicare","pct_births_unmarried"],join:["birth_rate_state","teen_birth_rate","pct_on_medicaid"],sc:{emotional:10,relatability:8,surprise:8,tension:6,visual:9,data_ready:7,originality:8},vs:93,tags:"NICU neonatal intensive care drive time rural healthcare maternal infant mortality pregnancy county pgRouting access"}







,{id:"grocery_desert_drive_time",title:"Drive time to nearest full-service grocery store by county",sub:"37M Americans live in food deserts. But the drive-time map reveals which counties are truly isolated.",type:"MAP",geo:"us_county",fmt:"County choropleth",tbl:"T1090 Â· T576",section:"Retail Trade Â· Social Insurance",ext:["USDA Food Access Research Atlas (publicly available via ers.usda.gov)"],vars:["retail_sales_per_capita","pct_on_snap"],join:["median_household_income","rep_pct"],sc:{emotional:9,relatability:9,surprise:7,tension:7,visual:9,data_ready:8,originality:7},vs:88,tags:"food desert grocery store drive time rural access USDA county SNAP food insecurity poor nutrition health"}







,{id:"redlining_home_values",title:"1930s HOLC redlining grades vs. current home price appreciation by neighborhood",sub:"Neighborhoods graded 'D' (hazardous) in the 1930s have appreciated 3x less than 'A' (best) neighborhoods since 1980.",type:"XREF",geo:"us_city",fmt:"City map",tbl:"T771",section:"Prices",ext:["Mapping Inequality HOLC shapefiles (mappinginequality.org â€” publicly available)"],vars:["home_price_index_2024","home_price_pct_change_2005_2024"],join:["median_household_income","pct_on_snap"],sc:{emotional:9,relatability:8,surprise:7,tension:9,visual:10,data_ready:8,originality:8},vs:89,tags:"redlining HOLC home values appreciation neighborhood race inequality housing discrimination 1930s history wealth gap Black"}







,{id:"redlining_income_today",title:"1930s HOLC redlining grades vs. median household income today",sub:"90 years later, the HOLC grade map and the income map are nearly identical. Redlining's legacy is income.",type:"XREF",geo:"us_city",fmt:"City map",tbl:"T727",section:"Income",ext:["Mapping Inequality HOLC shapefiles (mappinginequality.org â€” publicly available)"],vars:["median_household_income"],join:["violent_crime_rate","pct_on_snap","pct_bachelors"],sc:{emotional:9,relatability:8,surprise:6,tension:9,visual:10,data_ready:8,originality:7},vs:87,tags:"redlining HOLC income today neighborhood race inequality wealth gap Black history discrimination housing 90 years"}







,{id:"superfund_demographics",title:"Superfund toxic waste sites and nearby demographic composition",sub:"Who lives within 1 mile of a Superfund site â€” and why is it always the same demographic profile?",type:"XREF",geo:"us_county",fmt:"County choropleth",tbl:"T573 Â· T340",section:"Social Insurance Â· Law Enforcement",ext:["EPA Superfund National Priorities List (publicly available via epa.gov)"],vars:["total_transfers_per_capita","violent_crime_rate"],join:["median_household_income","pct_on_snap","rep_pct"],sc:{emotional:9,relatability:7,surprise:7,tension:9,visual:8,data_ready:7,originality:8},vs:85,tags:"Superfund toxic waste pollution race environmental justice EPA county demographics Black Hispanic poor health cancer"}







,{id:"flood_zone_no_insurance",title:"Properties in FEMA flood zones with no flood insurance by county",sub:"The disaster waiting to happen. Millions of homeowners in flood zones carry no insurance â€” concentrated in low-income counties.",type:"XREF",geo:"us_county",fmt:"County choropleth",tbl:"T771 Â· T727",section:"Housing Â· Income",ext:["FEMA National Flood Insurance Program data (publicly available via fema.gov)"],vars:["home_price_index_2024","median_household_income"],join:["housing_permits_total","mortgage_delinquency_rate"],sc:{emotional:8,relatability:7,surprise:7,tension:7,visual:9,data_ready:7,originality:8},vs:79,tags:"flood zone FEMA insurance housing risk disaster coastal river climate Louisiana Florida Texas poverty uninsured homes"}







,{id:"mental_health_provider_desert",title:"Mental health provider deserts by county",sub:"Millions of Americans live in counties with zero mental health providers. The crisis is geographic.",type:"MAP",geo:"us_county",fmt:"County choropleth",tbl:"T576 Â· T150",section:"Social Insurance Â· Health",ext:["SAMHSA/HRSA provider locator data (publicly available via findtreatment.gov)"],vars:["pct_on_medicaid","total_medicare"],join:["state_unemployment_rate","pct_on_snap","median_household_income"],sc:{emotional:9,relatability:9,surprise:7,tension:7,visual:9,data_ready:7,originality:7},vs:87,tags:"mental health provider desert county rural access therapy counseling suicide depression opioids Medicaid shortage workforce"}







,{id:"xref_low_health_spending_gofundme",title:"Per capita health spending vs. GoFundMe medical campaigns â€” states that crowdfund their healthcare",sub:"States where Medicaid doesn't cover enough have the most medical crowdfunding per capita. The safety net failure, measured in GoFundMe campaigns.",type:"XREF",geo:"us_state",fmt:"Scatter plot",tbl:"T141 Â· T576",section:"Health Â· Social Insurance",ext:["GoFundMe public campaign data (publicly available via GoFundMe)"],vars:["per_capita_health_spending","pct_on_medicaid"],join:["median_household_income","rep_pct"],sc:{emotional:10,relatability:9,surprise:9,tension:9,visual:8,data_ready:7,originality:10},vs:91,tags:"GoFundMe medical crowdfunding health spending Medicaid gap insurance coverage state poor access healthcare crisis"}







,{id:"irs_migration_post_covid",title:"IRS county-to-county migration flows post-COVID 2020â€“2023",sub:"Florida +380K net households. California -300K. New York -180K. The great reshuffling, told through tax returns.",type:"MAP",geo:"us_state",fmt:"Dot map",tbl:"T727 Â· T629",section:"Income Â· Labor",ext:["IRS Statistics of Income county-to-county migration data (publicly available via irs.gov)"],vars:["median_household_income","state_unemployment_rate"],join:["home_price_index_2024","housing_permits_total"],sc:{emotional:8,relatability:9,surprise:8,tension:6,visual:9,data_ready:8,originality:9},vs:87,tags:"IRS migration flows COVID pandemic work from home Florida California New York Texas Tennessee moving population shift"}







,{id:"xref_migration_income_destination",title:"IRS migration destination income vs. origin income â€” are movers going up or down?",sub:"People leaving California average $95K AGI. People staying average $74K. The wealth-sorting of American migration.",type:"XREF",geo:"us_state",fmt:"Scatter plot",tbl:"T727",section:"Income",ext:["IRS Statistics of Income county-to-county migration data (publicly available via irs.gov)"],vars:["median_household_income"],join:["home_price_index_2024","state_unemployment_rate"],sc:{emotional:8,relatability:8,surprise:8,tension:6,visual:8,data_ready:8,originality:9},vs:81,tags:"IRS migration income sorting California leaving staying wealth movers destination origin AGI inequality wealth"}







,{id:"dollar_general_vs_retail_sales",title:"Dollar General density vs. per capita retail sales by county",sub:"Counties with the highest Dollar General density have the lowest overall retail sales. Dollar General is the symptom of retail collapse.",type:"XREF",geo:"us_county",fmt:"Scatter plot",tbl:"T1090 Â· T576",section:"Retail Trade Â· Social Insurance",ext:["Dollar General store locations (publicly available via corporate disclosures and OpenStreetMap)"],vars:["retail_sales_per_capita","pct_on_snap"],join:["median_household_income","rep_pct"],sc:{emotional:8,relatability:9,surprise:8,tension:7,visual:9,data_ready:7,originality:9},vs:84,tags:"Dollar General retail desert food desert county SNAP poverty rural low income store closure Walmart Amazon economic collapse"}







,{id:"xref_low_retail_snap_dollar_general",title:"Low retail sales per capita + SNAP enrollment + Dollar General density â€” the poverty retail triangle",sub:"The three markers of retail poverty overlap perfectly. Where people are poor, food stamps are common, and Dollar General is the only store.",type:"XREF",geo:"us_county",fmt:"County choropleth",tbl:"T1090 Â· T576",section:"Retail Â· Social Insurance",ext:["Dollar General store locations (publicly available via corporate disclosures and OpenStreetMap)"],vars:["retail_sales_per_capita","pct_on_snap"],join:["median_household_income"],sc:{emotional:9,relatability:8,surprise:8,tension:7,visual:9,data_ready:7,originality:10},vs:84,tags:"Dollar General SNAP retail poverty triangle county overlap map low income food access rural desert deprivation"}







,{id:"brewery_church_ratio",title:"Brewery-to-church ratio by US county",sub:"Boulder CO: 18 breweries per church. Wayne County MS: 0.04. The cultural geography of America, one pint at a time.",type:"MAP",geo:"us_county",fmt:"County choropleth",tbl:"T493 Â· T576",section:"State Govt Â· Social Insurance",ext:["IRS 501c3 nonprofit data for churches (publicly available via IRS EO BMF file)", "USDA brewery data / OpenStreetMap"],vars:["lottery_revenue_per_capita","pct_on_snap"],join:["rep_pct","median_household_income"],sc:{emotional:6,relatability:9,surprise:8,tension:5,visual:9,data_ready:7,originality:9},vs:81,tags:"brewery church ratio county culture Bible Belt South rural urban religion craft beer Colorado Mississippi funny lifestyle map"}







,{id:"h3_lightning_density",title:"Lightning strike density H3 hexbin map â€” lower 48",sub:"Florida averages 1.4 million strikes/year. Oklahoma/Kansas corridors light up. The lightning geography of America.",type:"MAP",geo:"us_state",fmt:"H3 hexbin map",tbl:"T415",section:"Geography & Environment",ext:["VAISALA National Lightning Detection Network (publicly available summary data)"],vars:["mean_elevation"],join:["energy_consumption_per_capita"],sc:{emotional:5,relatability:7,surprise:8,tension:2,visual:10,data_ready:7,originality:9},vs:76,tags:"lightning strike density H3 hexbin Florida Oklahoma Kansas geography weather storms risk outdoor nature surprising map"}







,{id:"h3_airbnb_density_income",title:"Airbnb listing density vs. median income â€” who profits from the sharing economy?",sub:"Manhattan: 47K listings. Rural counties: near zero. The sharing economy concentrates wealth where wealth already is.",type:"XREF",geo:"us_county",fmt:"H3 hexbin map",tbl:"T727 Â· T726",section:"Income",ext:["Inside Airbnb public dataset (publicly available via insideairbnb.com)"],vars:["median_household_income","metro_per_capita_income"],join:["home_price_index_2024","housing_permits_total"],sc:{emotional:7,relatability:8,surprise:7,tension:6,visual:9,data_ready:7,originality:8},vs:77,tags:"Airbnb sharing economy density income inequality housing rental short-term gentrification H3 hexbin county wealth"}







,{id:"county_vote_swing_2016_2024",title:"County-level vote swing from 2016 to 2024 â€” the 8-year realignment map",sub:"Some Ohio counties swung 30 points toward Republicans. Some suburban Atlanta counties swung 20 points toward Democrats.",type:"MAP",geo:"us_county",fmt:"County choropleth",tbl:"T454",section:"Elections",ext:["MIT Election Lab county-level election results (publicly available via electionlab.mit.edu)"],vars:["rep_pct","dem_pct","margin"],join:["median_household_income","pct_bachelors","state_unemployment_rate"],sc:{emotional:9,relatability:8,surprise:8,tension:9,visual:10,data_ready:8,originality:7},vs:88,tags:"county vote swing 2016 2024 realignment Trump Republican Democrat Ohio Georgia suburban rural urban political geography map"}







,{id:"xref_income_change_vote_swing",title:"Income change 2016â€“2024 vs. vote swing by county",sub:"Counties where incomes grew fastest swung most toward Democrats. Counties where incomes stagnated swung toward Trump.",type:"XREF",geo:"us_county",fmt:"Scatter plot",tbl:"T727 Â· T454",section:"Income Â· Elections",ext:["MIT Election Lab county-level election results (publicly available via electionlab.mit.edu)"],vars:["median_household_income","rep_pct"],join:["state_unemployment_rate","pct_bachelors"],sc:{emotional:9,relatability:8,surprise:8,tension:9,visual:8,data_ready:8,originality:9},vs:87,tags:"income change vote swing county 2016 2024 Trump Democrat economic anxiety prosperity resentment political economy geography"}







,{id:"foreign_born_doctors_by_state",title:"Foreign-born physicians as % of all physicians by state",sub:"New Jersey: 41% of doctors are foreign-born. Idaho: 14%. The immigrant doctor geography that keeps American healthcare running.",type:"MAP",geo:"us_state",fmt:"State choropleth",tbl:"T150 Â· T141",section:"Health",ext:["ACS PUMS physician occupation + nativity (publicly available via Census Bureau)"],vars:["total_medicare","per_capita_health_spending"],join:["pct_on_medicaid","median_household_income"],sc:{emotional:8,relatability:7,surprise:8,tension:7,visual:9,data_ready:7,originality:8},vs:80,tags:"foreign born doctors physicians immigrant healthcare state New Jersey Idaho nativity ACS Census immigration medicine"}







,{id:"missing_men_map",title:"The missing men map â€” skewed sex ratios by county",sub:"Some rural counties: 140 men per 100 women (prisons, military, mining). Some urban counties: 85 men per 100 women. The gender geography of America.",type:"MAP",geo:"us_county",fmt:"County choropleth",tbl:"T629 Â· T340",section:"Labor Â· Crime",ext:["ACS sex ratio by county (publicly available via Census Bureau)"],vars:["state_unemployment_rate","violent_crime_rate"],join:["median_household_income","pct_on_snap"],sc:{emotional:7,relatability:7,surprise:9,tension:5,visual:9,data_ready:8,originality:9},vs:79,tags:"sex ratio men women county missing men prison military mining rural urban gender geography surprising America ACS Census"}







,{id:"commute_time_by_county",title:"Average commute time by county â€” who's spending their life in traffic?",sub:"Mega-commuter counties around NYC: 50+ minutes each way. Some rural counties: 12 minutes. The time tax of American housing.",type:"MAP",geo:"us_county",fmt:"County choropleth",tbl:"T727 Â· T629",section:"Income Â· Labor",ext:["ACS commute time data (publicly available via Census Bureau)"],vars:["median_household_income","state_unemployment_rate"],join:["home_price_index_2024","housing_permits_total"],sc:{emotional:7,relatability:9,surprise:6,tension:5,visual:9,data_ready:8,originality:6},vs:74,tags:"commute time county traffic hours life New York New Jersey suburban rural time cost housing affordability American daily life"}







,{id:"xref_commute_time_home_prices",title:"Average commute time vs. home price index by county",sub:"The longer the commute, the cheaper the house. Americans are trading hours for square footage.",type:"XREF",geo:"us_county",fmt:"Scatter plot",tbl:"T771 Â· T727",section:"Housing Â· Labor",ext:["ACS commute time data (publicly available via Census Bureau)"],vars:["home_price_index_2024","median_household_income"],join:["housing_permits_total","state_unemployment_rate"],sc:{emotional:7,relatability:9,surprise:7,tension:5,visual:8,data_ready:8,originality:7},vs:75,tags:"commute time home prices county tradeoff suburb exurb housing affordability drive hours sacrifice square footage"}







,{id:"language_diversity_county",title:"Languages spoken at home by county â€” the linguistic geography of America",sub:"Queens NY: 130+ languages in one county. The linguistic diversity map reveals the hidden cosmopolitan geography of America.",type:"MAP",geo:"us_county",fmt:"County choropleth",tbl:"T573 Â· T727",section:"Social Insurance Â· Income",ext:["ACS language spoken at home by county (publicly available via Census Bureau)"],vars:["total_transfers_per_capita","median_household_income"],join:["pct_bachelors","rep_pct"],sc:{emotional:6,relatability:7,surprise:8,tension:4,visual:9,data_ready:8,originality:7},vs:73,tags:"languages spoken home county diversity Queens New York linguistic geography immigration cosmopolitan rural monolingual America"}







,{id:"xref_internet_access_income",title:"Broadband internet access rate vs. median income by county",sub:"The digital divide is an income divide. Counties below $40K median income average 68% broadband adoption vs. 91% above $80K.",type:"XREF",geo:"us_county",fmt:"Scatter plot",tbl:"T727",section:"Income",ext:["FCC Form 477 broadband availability data (publicly available via fcc.gov)"],vars:["median_household_income"],join:["pct_bachelors","state_unemployment_rate","rep_pct"],sc:{emotional:8,relatability:8,surprise:6,tension:6,visual:8,data_ready:8,originality:5},vs:74,tags:"broadband internet access income digital divide county FCC rural urban low income high income economy education"}







,{id:"xref_broadband_income_vote",title:"Broadband access rate vs. Republican vote share by county",sub:"Low-broadband counties vote Republican by 30+ points. The digital divide is also a political divide.",type:"XREF",geo:"us_county",fmt:"Scatter plot",tbl:"T454 Â· T727",section:"Elections Â· Income",ext:["FCC Form 477 broadband availability data (publicly available via fcc.gov)"],vars:["rep_pct","median_household_income"],join:["pct_bachelors","rural_population_pct"],sc:{emotional:8,relatability:7,surprise:7,tension:7,visual:7,data_ready:8,originality:7},vs:77,tags:"broadband internet Republican vote county digital divide political rural urban FCC low income conservative"}







,{id:"xref_crime_energy_boom",title:"Oil boom counties vs. violent crime rate â€” the resource curse",sub:"North Dakota Bakken counties saw violent crime triple during the 2010s oil boom. Prosperity and violence arrive together.",type:"XREF",geo:"us_county",fmt:"Scatter plot",tbl:"T340 Â· T975",section:"Crime Â· Energy",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by county (bls.gov â€” free)","FBI Crime Data Explorer: UCR/NIBRS by state/agency (cde.ucr.cjis.gov â€” free)","EIA State Energy Data System: production + consumption by state (eia.gov â€” free API)"],vars:["violent_crime_rate","energy_consumption_per_capita"],join:["state_unemployment_rate","median_household_income"],sc:{emotional:8,relatability:6,surprise:9,tension:7,visual:8,data_ready:9,originality:9},vs:78,tags:"oil boom crime violence North Dakota Bakken fracking resource curse county energy workers transient population"}







,{id:"xref_crime_agriculture",title:"Agricultural employment % vs. violent crime rate by state",sub:"The most agricultural states have the most violent crime. Rural poverty, not rural peace.",type:"XREF",geo:"us_state",fmt:"Scatter plot",tbl:"T340 Â· T869",section:"Crime Â· Agriculture",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)","FBI Crime Data Explorer: UCR/NIBRS by state/agency (cde.ucr.cjis.gov â€” free)","USDA ERS: food environment, rural classification, farm income (ers.usda.gov â€” free)"],vars:["violent_crime_rate","farms_count_2022"],join:["median_household_income","pct_on_snap"],sc:{emotional:7,relatability:6,surprise:8,tension:6,visual:7,data_ready:10,originality:7},vs:71,tags:"agriculture crime rural violent poverty farm states Mississippi Arkansas Louisiana murder rate safety myth"}







,{id:"xref_murder_manufacturing_loss",title:"Manufacturing job loss 2000â€“2020 vs. murder rate increase by county",sub:"Counties that lost the most factory jobs had the sharpest increases in murder rates. The deindustrialization-violence pipeline.",type:"XREF",geo:"us_county",fmt:"Scatter plot",tbl:"T340 Â· T1064",section:"Crime Â· Manufactures",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by county (bls.gov â€” free)","FBI Crime Data Explorer: UCR/NIBRS by state/agency (cde.ucr.cjis.gov â€” free)"],vars:["murder_rate","manufacturing_employment_trend"],join:["state_unemployment_rate","median_household_income"],sc:{emotional:9,relatability:7,surprise:8,tension:9,visual:8,data_ready:8,originality:9},vs:83,tags:"manufacturing job loss murder crime violence deindustrialization Rust Belt county despair poverty Ohio Michigan"}







,{id:"xref_education_military_enlistment",title:"College degree rate vs. military enlistment rate by state",sub:"States with fewer college graduates send more soldiers. Military service as the alternative to education.",type:"XREF",geo:"us_state",fmt:"Scatter plot",tbl:"T254 Â· T545",section:"Education Â· Military",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)"],vars:["pct_bachelors","active_duty_total"],join:["median_household_income","rep_pct"],sc:{emotional:8,relatability:7,surprise:7,tension:7,visual:7,data_ready:9,originality:7},vs:75,tags:"education military enlistment college degree alternative South rural states economic draft poverty service"}







,{id:"xref_education_trade_deficit",title:"State education spending vs. share of jobs lost to trade by state",sub:"States that invested least in education lost the most jobs to trade. The education-trade vulnerability connection.",type:"XREF",geo:"us_state",fmt:"Scatter plot",tbl:"T254 Â· T1310",section:"Education Â· Trade",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)"],vars:["pct_bachelors","trade_balance_goods"],join:["manufacturing_employment_trend","state_unemployment_rate"],sc:{emotional:8,relatability:7,surprise:7,tension:8,visual:7,data_ready:9,originality:8},vs:75,tags:"education trade deficit jobs lost globalization manufacturing low degree states Rust Belt vulnerability workers"}







,{id:"xref_per_pupil_bridges",title:"Per-pupil school spending vs. bridge condition by state",sub:"States that can't fund schools also can't fix bridges. The dual infrastructure neglect map.",type:"XREF",geo:"us_state",fmt:"Scatter plot",tbl:"T258 Â· T1126",section:"Education Â· Transportation",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)"],vars:["expenditure_per_pupil","pct_bridges_poor"],join:["rep_pct","median_household_income"],sc:{emotional:8,relatability:7,surprise:7,tension:7,visual:8,data_ready:10,originality:8},vs:76,tags:"school funding bridges infrastructure neglect state dual poverty disinvestment Iowa West Virginia Rhode Island education"}







,{id:"xref_teacher_salary_energy_state",title:"Teacher salary vs. energy sector GDP share by state",sub:"Oil-rich Wyoming pays teachers $67K. Oil-poor Massachusetts pays $95K. Energy wealth doesn't become school wealth.",type:"XREF",geo:"us_state",fmt:"Scatter plot",tbl:"T268 Â· T975",section:"Education Â· Energy",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)","EIA State Energy Data System: production + consumption by state (eia.gov â€” free API)"],vars:["avg_teacher_salary","energy_consumption_per_capita"],join:["state_gdp_per_capita","rep_pct"],sc:{emotional:7,relatability:6,surprise:8,tension:6,visual:7,data_ready:10,originality:8},vs:70,tags:"teacher salary energy wealth state Wyoming oil gas school funding Massachusetts paradox resource wealth education"}







,{id:"xref_health_spending_energy",title:"Per capita health spending vs. energy consumption by state",sub:"High-energy industrial states spend less on healthcare per person. Energy extraction and health investment trade off.",type:"XREF",geo:"us_state",fmt:"Scatter plot",tbl:"T141 Â· T975",section:"Health Â· Energy",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)","CDC WONDER: mortality + disease rates by county/state (wonder.cdc.gov â€” free)","EIA State Energy Data System: production + consumption by state (eia.gov â€” free API)"],vars:["per_capita_health_spending","energy_consumption_per_capita"],join:["rep_pct","median_household_income"],sc:{emotional:6,relatability:5,surprise:8,tension:5,visual:7,data_ready:10,originality:8},vs:68,tags:"health spending energy consumption state industrial Wyoming Louisiana Texas tradeoff workers oil gas extraction"}







,{id:"xref_life_expectancy_income_state",title:"Life expectancy vs. median income by state â€” the 8-year gap",sub:"Colorado: life expectancy 80.8. Mississippi: 74.4. A 6-year gap that maps almost perfectly onto income.",type:"XREF",geo:"us_state",fmt:"Scatter plot",tbl:"T141 Â· T727",section:"Health Â· Income",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)","CDC WONDER: mortality + disease rates by county/state (wonder.cdc.gov â€” free)"],vars:["per_capita_health_spending","median_household_income"],join:["pct_on_medicaid","rep_pct","violent_crime_rate"],sc:{emotional:9,relatability:8,surprise:6,tension:8,visual:8,data_ready:9,originality:5},vs:79,tags:"life expectancy income state inequality Mississippi Colorado gap wealth health outcomes poverty race mortality"}







,{id:"xref_hospital_cpi_military_spending",title:"Hospital services CPI vs. defense spending by state",sub:"High-defense states don't have better healthcare. The guns-vs-butter trade-off within state economies.",type:"XREF",geo:"us_state",fmt:"Scatter plot",tbl:"T770 Â· T543",section:"Health Â· Military",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)","CDC WONDER: mortality + disease rates by county/state (wonder.cdc.gov â€” free)"],vars:["hospital_services_cpi","defense_budget_total"],join:["per_capita_health_spending","rep_pct"],sc:{emotional:7,relatability:5,surprise:8,tension:6,visual:7,data_ready:9,originality:8},vs:69,tags:"hospital prices defense spending guns butter state tradeoff military health care cost priorities Virginia"}







,{id:"xref_prescription_drug_trade",title:"US pharmaceutical trade balance vs. domestic prescription drug CPI",sub:"The US imports $140B in pharmaceuticals while domestic drug prices triple. The trade-price paradox in medicine.",type:"CHART",geo:"us_national",fmt:"Line chart",tbl:"T770 Â· T1310",section:"Health Â· Trade",ext:["FRED: any national economic time series (fred.stlouisfed.org â€” free API)","BLS national data: employment, wages, CPI (bls.gov â€” free API)","CDC WONDER: mortality + disease rates by county/state (wonder.cdc.gov â€” free)"],vars:["prescription_drugs_cpi","trade_balance_goods"],join:["per_capita_health_spending","health_insurance_cpi"],sc:{emotional:8,relatability:7,surprise:8,tension:7,visual:7,data_ready:9,originality:9},vs:74,tags:"pharmaceutical trade balance drug prices CPI import export prescription insulin price gouging trade policy health"}







,{id:"xref_bridge_condition_income",title:"Bridge condition vs. median income by state â€” infrastructure as wealth proxy",sub:"Poor states have worse bridges. The infrastructure gap is an income gap in concrete.",type:"XREF",geo:"us_state",fmt:"Bivariate choropleth",tbl:"T1126 Â· T727",section:"Transportation Â· Income",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)"],vars:["pct_bridges_poor","median_household_income"],join:["rep_pct","total_transfers_per_capita"],sc:{emotional:8,relatability:7,surprise:6,tension:7,visual:9,data_ready:10,originality:6},vs:76,tags:"bridges income state infrastructure wealth poor Mississippi Iowa West Virginia Rhode Island crumbling inequality"}







,{id:"xref_port_tonnage_trade_deficit",title:"US port tonnage by direction â€” inbound vs. outbound and the trade gap",sub:"US ports handle 3x more inbound tonnage than outbound. The physical manifestation of the $1.2T trade deficit.",type:"CHART",geo:"us_national",fmt:"Bar chart",tbl:"T1122 Â· T1306",section:"Transportation Â· Trade",ext:["FRED: any national economic time series (fred.stlouisfed.org â€” free API)","BLS national data: employment, wages, CPI (bls.gov â€” free API)"],vars:["port_total_tons","current_account_balance"],join:["balance_on_goods","trade_balance_goods"],sc:{emotional:7,relatability:6,surprise:8,tension:7,visual:8,data_ready:10,originality:9},vs:73,tags:"port tonnage trade deficit inbound outbound import export physical goods supply chain visualization"}







,{id:"xref_waterway_freight_agriculture",title:"Inland waterway freight vs. agricultural export value by state",sub:"The Mississippi system carries 60% of US grain exports. The agricultural economy floats on a river.",type:"XREF",geo:"us_state",fmt:"Scatter plot",tbl:"T1120 Â· T869",section:"Transportation Â· Agriculture",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)","USDA ERS: food environment, rural classification, farm income (ers.usda.gov â€” free)"],vars:["waterway_freight_tons","farm_value_land"],join:["port_total_tons","pct_cropland"],sc:{emotional:6,relatability:6,surprise:8,tension:4,visual:9,data_ready:10,originality:8},vs:71,tags:"waterway freight agriculture Mississippi grain export barge river Iowa Illinois supply chain food infrastructure"}







,{id:"xref_airport_traffic_income",title:"Air travel frequency vs. median income by metro",sub:"High-income metros have 4x more flight departures per capita. Flying is a class marker.",type:"XREF",geo:"us_metro",fmt:"Scatter plot",tbl:"T1112 Â· T726",section:"Transportation Â· Income",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by metro (apps.bea.gov â€” free)","BLS LAUS: unemployment + labor force by metro (bls.gov â€” free)"],vars:["passengers_enplaned","metro_per_capita_income"],join:["median_household_income","pct_bachelors"],sc:{emotional:7,relatability:8,surprise:6,tension:5,visual:8,data_ready:10,originality:6},vs:71,tags:"air travel income class flying metro wealth inequality passengers airports frequency business travel leisure"}







,{id:"xref_snap_coastline",title:"SNAP enrollment vs. coastal access by state â€” does nature offset poverty?",sub:"Coastal poor states still have high SNAP rates. Access to the ocean doesn't feed people.",type:"XREF",geo:"us_state",fmt:"Scatter plot",tbl:"T576 Â· T408",section:"Social Insurance Â· Geography",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)"],vars:["pct_on_snap","coastline_miles"],join:["median_household_income","rep_pct"],sc:{emotional:5,relatability:5,surprise:7,tension:3,visual:7,data_ready:10,originality:8},vs:62,tags:"SNAP food stamps coastline coastal states poverty geography nature access Alaska Maine Louisiana Mississippi ocean"}







,{id:"xref_transfers_elevation",title:"Federal transfers per capita vs. mean elevation by state",sub:"The highest states get the most federal money. Geography and dependency overlap in the mountain West.",type:"XREF",geo:"us_state",fmt:"Scatter plot",tbl:"T573 Â· T410",section:"Social Insurance Â· Geography",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)"],vars:["total_transfers_per_capita","mean_elevation"],join:["rep_pct","median_household_income"],sc:{emotional:5,relatability:4,surprise:8,tension:4,visual:7,data_ready:10,originality:9},vs:64,tags:"federal transfers elevation geography mountain West Wyoming Alaska Colorado government spending dependency altitude"}







,{id:"xref_snap_national_forest",title:"SNAP enrollment vs. national forest acres by state",sub:"States with the most public land have some of the highest food stamp rates. The protected-land poverty overlap.",type:"XREF",geo:"us_state",fmt:"Scatter plot",tbl:"T576 Â· T932",section:"Social Insurance Â· Forestry",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)"],vars:["pct_on_snap","national_forest_acres"],join:["median_household_income","rep_pct"],sc:{emotional:7,relatability:5,surprise:9,tension:5,visual:8,data_ready:10,originality:9},vs:71,tags:"SNAP food stamps national forest public land poverty locked out resources federal land West rural states"}







,{id:"xref_rd_manufacturing_wages",title:"Business R&D spending vs. manufacturing hourly wages by state",sub:"High-R&D states pay factory workers more. Innovation raises the floor for blue-collar wages.",type:"XREF",geo:"us_state",fmt:"Scatter plot",tbl:"T844 Â· T1067",section:"Science Â· Manufactures",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)"],vars:["rd_pct_gdp","manufacturing_hourly_wages_state"],join:["median_household_income","pct_bachelors"],sc:{emotional:7,relatability:6,surprise:7,tension:5,visual:7,data_ready:10,originality:8},vs:70,tags:"R&D research manufacturing wages blue collar innovation states Washington Massachusetts factory workers pay floor"}







,{id:"xref_rd_spending_trade_surplus",title:"R&D spending as % of GDP vs. trade balance by country â€” the innovation-trade link",sub:"Every country that runs a trade surplus spends at least 3% of GDP on R&D. No exceptions.",type:"XREF",geo:"worldwide",fmt:"Scatter plot",tbl:"T842 Â· T1310",section:"Science Â· Trade",ext:["World Bank Open Data: GDP, population, income by country (data.worldbank.org â€” free API)"],vars:["rd_pct_gdp","trade_balance_goods"],join:["us_troops_overseas","population_pct_change_2020_2025"],sc:{emotional:8,relatability:6,surprise:8,tension:7,visual:8,data_ready:10,originality:8},vs:76,tags:"R&D research trade surplus innovation South Korea Germany Japan US China competitiveness GDP spending manufacturing"}







,{id:"university_rd_by_state",title:"University R&D spending by state 2023",sub:"California: $11.5B in university R&D. Wyoming: $200M. The knowledge economy is geographically concentrated.",type:"MAP",geo:"us_state",fmt:"State choropleth",tbl:"T846",section:"Science",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)"],vars:["rd_pct_gdp"],join:["pct_bachelors","state_gdp_per_capita","median_household_income"],sc:{emotional:6,relatability:6,surprise:7,tension:4,visual:9,data_ready:10,originality:6},vs:68,tags:"university R&D research spending state California Wyoming knowledge economy geography concentration STEM innovation"}







,{id:"xref_fishing_value_snap",title:"Commercial fishing landed value vs. SNAP enrollment by coastal state",sub:"Maine lands $700M in fish â€” and 12% of residents are on food stamps. The fishermen are poor.",type:"XREF",geo:"us_state",fmt:"Scatter plot",tbl:"T945 Â· T576",section:"Fishing Â· Social Insurance",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)"],vars:["port_catch_value","pct_on_snap"],join:["median_household_income","port_catch_lbs"],sc:{emotional:8,relatability:6,surprise:9,tension:6,visual:7,data_ready:10,originality:9},vs:74,tags:"fishing SNAP poverty coastal states Maine Louisiana Alaska fishermen food stamps industry workers hunger"}







,{id:"fishing_employment_decline",title:"Commercial fishing employment 1990â€“2024: the long collapse",sub:"From 280K jobs to under 90K. Automation, regulation, and climate change hollowed out the fishing industry.",type:"CHART",geo:"us_national",fmt:"Area chart",tbl:"T942",section:"Fishing",ext:["FRED: any national economic time series (fred.stlouisfed.org â€” free API)","BLS national data: employment, wages, CPI (bls.gov â€” free API)"],vars:["port_catch_lbs","species_landed_value"],join:["port_catch_value"],sc:{emotional:7,relatability:5,surprise:7,tension:6,visual:7,data_ready:9,originality:7},vs:67,tags:"commercial fishing employment decline 1990 2024 jobs workers industry collapse automation climate change regulations"}







,{id:"xref_fishing_income_port_city",title:"Commercial fishing landed value vs. median income in fishing port cities",sub:"Gloucester MA: $50M in fish landed, $65K median income. New Bedford: $700M landed, $47K. The paradox of abundance.",type:"XREF",geo:"us_city",fmt:"Scatter plot",tbl:"T945 Â· T726",section:"Fishing Â· Income",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)"],vars:["port_catch_value","metro_per_capita_income"],join:["port_catch_lbs","species_landed_value"],sc:{emotional:7,relatability:6,surprise:8,tension:5,visual:7,data_ready:9,originality:9},vs:70,tags:"fishing income port city New Bedford Gloucester paradox abundance poverty seafood workers wages economy coastal"}







,{id:"cpi_shelter_vs_food",title:"Shelter CPI vs. food at home CPI 2000â€“2024 â€” the two-headed squeeze",sub:"Shelter up 234%. Food at home up 307%. The two biggest household costs both tripled. The American budget in crisis.",type:"CHART",geo:"us_national",fmt:"Line chart",tbl:"T770",section:"Prices",ext:["FRED: any national economic time series (fred.stlouisfed.org â€” free API)","BLS national data: employment, wages, CPI (bls.gov â€” free API)"],vars:["housing_cpi","food_at_home_cpi","all_items_cpi"],join:["eggs_cpi","daycare_preschool_cpi"],sc:{emotional:9,relatability:10,surprise:7,tension:8,visual:8,data_ready:10,originality:7},vs:84,tags:"shelter food inflation CPI household squeeze budget crisis housing grocery 2000 2024 rent homeowner grocery"}







,{id:"cpi_medical_vs_wages",title:"Medical care CPI vs. wage growth â€” the healthcare affordability collapse",sub:"Medical care CPI up 440% since 1983. Wages up ~250%. The gap that explains medical bankruptcy.",type:"CHART",geo:"us_national",fmt:"Line chart",tbl:"T770",section:"Prices",ext:["FRED: any national economic time series (fred.stlouisfed.org â€” free API)","BLS national data: employment, wages, CPI (bls.gov â€” free API)"],vars:["hospital_services_cpi","physicians_services_cpi","prescription_drugs_cpi","all_items_cpi"],join:["per_capita_health_spending","health_insurance_cpi"],sc:{emotional:9,relatability:9,surprise:7,tension:8,visual:8,data_ready:10,originality:6},vs:82,tags:"medical care CPI wages healthcare affordability collapse bankruptcy hospital doctor prescription drug inflation gap"}







,{id:"cpi_education_vs_recreation",title:"Education CPI vs. recreation CPI 2000â€“2024 â€” what got cheaper and what didn't",sub:"College tuition CPI: 937. Recreation/entertainment: 141. One thing Americans prioritize priced them out.",type:"CHART",geo:"us_national",fmt:"Line chart",tbl:"T770",section:"Prices",ext:["FRED: any national economic time series (fred.stlouisfed.org â€” free API)","BLS national data: employment, wages, CPI (bls.gov â€” free API)"],vars:["college_tuition_cpi","all_items_cpi"],join:["daycare_preschool_cpi","student_loans_outstanding"],sc:{emotional:7,relatability:8,surprise:8,tension:5,visual:8,data_ready:10,originality:7},vs:74,tags:"education recreation CPI comparison tuition entertainment inflation cost culture leisure cheaper expensive tradeoff budget"}







,{id:"cpi_new_vs_used_vehicles",title:"New vs. used vehicle CPI 2015â€“2024 â€” the pandemic car crisis",sub:"Used car CPI peaked at 179 in 2022 â€” briefly more expensive than new cars. The supply chain failure visualized.",type:"CHART",geo:"us_national",fmt:"Line chart",tbl:"T770",section:"Prices",ext:["FRED: any national economic time series (fred.stlouisfed.org â€” free API)","BLS national data: employment, wages, CPI (bls.gov â€” free API)"],vars:["all_items_cpi","motor_vehicle_insurance_cpi"],join:["gasoline_cpi"],sc:{emotional:7,relatability:9,surprise:9,tension:5,visual:8,data_ready:10,originality:8},vs:76,tags:"new used cars CPI 2022 pandemic supply chain chip shortage vehicle prices used car market inflation spike weird"}







,{id:"cpi_winners_losers",title:"The 10 most and least inflated consumer categories 2000â€“2024",sub:"Hospital services: +414%. Wireless phones: -53%. The full spectrum of American price changes in one chart.",type:"RANK",geo:"us_national",fmt:"Bar chart",tbl:"T770",section:"Prices",ext:["FRED: any national economic time series (fred.stlouisfed.org â€” free API)","BLS national data: employment, wages, CPI (bls.gov â€” free API)"],vars:["hospital_services_cpi","college_tuition_cpi","tobacco_cpi","motor_vehicle_insurance_cpi","all_items_cpi","daycare_preschool_cpi"],join:[],sc:{emotional:8,relatability:10,surprise:9,tension:5,visual:10,data_ready:10,originality:8},vs:85,tags:"CPI inflation winners losers categories hospitals phones wireless college tobacco cars food 2000 2024 full spectrum"}







,{id:"which_red_counties_get_most_federal_aid",title:"Federal aid per capita in the 100 most Republican counties",sub:"The 100 most Trump-voting counties average $8,200 in federal transfers per person. The dependency is concentrated.",type:"MAP",geo:"us_county",fmt:"County choropleth",tbl:"T573 Â· T454",section:"Elections Â· Social Insurance",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by county (bls.gov â€” free)","MIT Election Lab: presidential/congressional results (electionlab.mit.edu â€” free)"],vars:["total_transfers_per_capita","rep_pct"],join:["pct_on_snap","pct_on_medicaid","median_household_income"],sc:{emotional:10,relatability:8,surprise:9,tension:10,visual:9,data_ready:9,originality:9},vs:93,tags:"Republican counties federal aid transfers per capita paradox MAGA welfare dependency most Trump voting aid money"}







,{id:"map_where_people_work_born_same_county",title:"Counties where people still live and work where they were born",sub:"Some Appalachian counties: 70%+ born and still living locally. Some DC suburbs: under 5%. The mobility divide.",type:"MAP",geo:"us_county",fmt:"County choropleth",tbl:"T629",section:"Labor",ext:["ACS place of birth vs. residence data (publicly available via Census Bureau)"],vars:["state_unemployment_rate","median_household_income"],join:["population_pct_change","pct_bachelors"],sc:{emotional:7,relatability:8,surprise:8,tension:4,visual:9,data_ready:7,originality:9},vs:76,tags:"born same county live work mobility immobility Appalachia DC suburb geographic roots community rootedness stayers movers"}







,{id:"most_transient_counties",title:"Most and least transient counties in America â€” who stays and who goes",sub:"Some military counties: 70% of residents have been there under 1 year. Some rural Vermont counties: 95% long-term.",type:"RANK",geo:"us_county",fmt:"Ranked list",tbl:"T629",section:"Labor",ext:["ACS residential tenure data (publicly available via Census Bureau)"],vars:["state_unemployment_rate"],join:["median_household_income","population_pct_change"],sc:{emotional:6,relatability:7,surprise:8,tension:3,visual:9,data_ready:7,originality:8},vs:70,tags:"transient county military bases turnover residential stability stays moves Vermont rural base housing roots temporary"}







,{id:"counties_where_women_outlive_men_most",title:"The counties where women outlive men the most â€” and the least",sub:"Some rural Southern counties: women live 9+ years longer than men. Manhattan: gap is under 4 years. The mortality divide.",type:"MAP",geo:"us_county",fmt:"County choropleth",tbl:"T629 Â· T340",section:"Labor Â· Crime",ext:["CDC life expectancy by county and sex (publicly available via CDC Wonder)"],vars:["state_unemployment_rate","violent_crime_rate"],join:["median_household_income","pct_on_snap"],sc:{emotional:8,relatability:7,surprise:8,tension:6,visual:9,data_ready:7,originality:8},vs:77,tags:"life expectancy gender gap women men county South rural mortality divide CDC age death health inequality"}







,{id:"where_landlines_still_exist",title:"Where people still have landlines â€” the holdout geography of old America",sub:"West Virginia: 36% of households still have a landline. Oregon: 12%. The last analog Americans.",type:"MAP",geo:"us_state",fmt:"State choropleth",tbl:"T770",section:"Prices",ext:["FCC telephone subscription data (publicly available via FCC)"],vars:["all_items_cpi"],join:["median_household_income","rep_pct"],sc:{emotional:5,relatability:8,surprise:9,tension:2,visual:9,data_ready:8,originality:9},vs:73,tags:"landlines telephone analog holdout geography West Virginia Oregon elderly rural old technology phone subscriber curious"}







,{id:"breweries_per_capita_ranked",title:"Breweries per capita by state â€” the craft beer geography",sub:"Vermont: 12 breweries per 100K people. Mississippi: 0.8. The beer map is also the education map.",type:"MAP",geo:"us_state",fmt:"State choropleth",tbl:"T493",section:"State Govt",ext:["USDA brewery data / TTB permit registry (publicly available)"],vars:["lottery_revenue_per_capita"],join:["pct_bachelors","median_household_income","rep_pct"],sc:{emotional:5,relatability:8,surprise:7,tension:2,visual:9,data_ready:8,originality:7},vs:70,tags:"breweries per capita craft beer state Vermont Mississippi education income blue red state geography beer culture"}







,{id:"xref_fast_food_density_diabetes",title:"Fast food restaurant density vs. diabetes rate by county",sub:"Counties with the most fast food chains per capita have diabetes rates 3x higher. The food environment maps to disease.",type:"XREF",geo:"us_county",fmt:"Scatter plot",tbl:"T576 Â· T141",section:"Health Â· Social Insurance",ext:["CDC diabetes rate by county (publicly available via CDC PLACES)", "USDA food environment atlas data (publicly available)"],vars:["per_capita_health_spending","pct_on_medicaid"],join:["median_household_income","pct_on_snap"],sc:{emotional:9,relatability:9,surprise:7,tension:8,visual:9,data_ready:7,originality:8},vs:84,tags:"fast food diabetes county density disease food environment health outcomes obesity poor income chain restaurants"}







,{id:"xref_income_change_vs_birth_rate",title:"Income change 2010â€“2023 vs. birth rate change by state",sub:"States where incomes rose fastest had the sharpest birth rate declines. Prosperity is the best contraceptive.",type:"XREF",geo:"us_state",fmt:"Scatter plot",tbl:"T727 Â· T81",section:"Income Â· Births",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)"],vars:["median_household_income","birth_rate_state"],join:["total_fertility_rate_by_race","pct_bachelors"],sc:{emotional:8,relatability:8,surprise:8,tension:5,visual:7,data_ready:10,originality:8},vs:77,tags:"income birth rate fertility prosperity demographic transition wealthy states fewer children low income more children"}







,{id:"world_birth_rate_collapse",title:"Global total fertility rate by country 2024 â€” the worldwide birth crash",sub:"119 countries are below replacement fertility. The demographic transition is global and accelerating.",type:"MAP",geo:"worldwide",fmt:"World choropleth",tbl:"International Statistics",section:"International Statistics",ext:["World Bank Open Data: GDP, population, income by country (data.worldbank.org â€” free API)"],vars:["birth_rate","net_migration_rate"],join:["population_pct_change_2020_2025","population_per_sq_km"],sc:{emotional:8,relatability:7,surprise:8,tension:7,visual:9,data_ready:10,originality:6},vs:78,tags:"global fertility birth rate collapse replacement 2024 worldwide demographic crisis South Korea Japan Italy aging population"}







,{id:"world_military_spending_gdp",title:"Military spending as % of GDP by country 2024",sub:"Ukraine: 37% of GDP on defense. US: 3.4%. Russia: 7.1%. Israel: 8.2%. The war economy map.",type:"MAP",geo:"worldwide",fmt:"World choropleth",tbl:"T543",section:"National Security",ext:["World Bank Open Data: GDP, population, income by country (data.worldbank.org â€” free API)"],vars:["defense_budget_total","us_troops_overseas"],join:["rd_pct_gdp","trade_balance_goods"],sc:{emotional:8,relatability:6,surprise:7,tension:9,visual:9,data_ready:9,originality:6},vs:76,tags:"military spending GDP country Ukraine US Russia Israel war defense 2024 global security NATO arms burden"}







,{id:"countries_losing_working_age_pop",title:"Countries losing working-age population fastest 2020â€“2030",sub:"Bulgaria -18%. Serbia -14%. South Korea facing labor shortage by 2028. The pension math is unworkable.",type:"RANK",geo:"worldwide",fmt:"Ranked list",tbl:"International Statistics",section:"International Statistics",ext:["World Bank Open Data: GDP, population, income by country (data.worldbank.org â€” free API)"],vars:["population_pct_change_2020_2025","net_migration_rate"],join:["birth_rate","rd_pct_gdp"],sc:{emotional:8,relatability:6,surprise:8,tension:8,visual:9,data_ready:9,originality:7},vs:76,tags:"working age population decline Bulgaria Serbia South Korea pension crisis labor shortage 2030 demographic collapse aging"}







,{id:"us_vs_peer_nations_inequality",title:"Income inequality (Gini) â€” US vs. peer nations",sub:"US Gini: 0.41. Canada: 0.31. Germany: 0.29. Denmark: 0.28. America is the most unequal wealthy democracy.",type:"RANK",geo:"worldwide",fmt:"Ranked list",tbl:"T727",section:"Income",ext:["World Bank Open Data: GDP, population, income by country (data.worldbank.org â€” free API)"],vars:["median_household_income","pct_over_200k"],join:["pct_families_own_stocks","corporate_profits"],sc:{emotional:8,relatability:7,surprise:7,tension:8,visual:8,data_ready:9,originality:5},vs:75,tags:"income inequality Gini US Canada Germany Denmark international comparison wealthy democracy most unequal peer nations"}







,{id:"new_england_fishing_economy",title:"New England commercial fishing economy by port 2023",sub:"New Bedford still #2 in the US by value. Gloucester declining. The historic fishing ports in numbers.",type:"RANK",geo:"top_n_list",fmt:"Ranked list",tbl:"T945",section:"Fishing",ext:[],vars:["port_catch_value","port_catch_lbs"],join:["species_landed_value"],sc:{emotional:6,relatability:7,surprise:7,tension:3,visual:9,data_ready:10,originality:7},vs:69,tags:"New England fishing economy ports New Bedford Gloucester Boston Providence Maine Massachusetts Rhode Island seafood value history"}







,{id:"xref_cycling_infrastructure_income",title:"Bike commuting rate vs. median income by city",sub:"Portland OR: 7% bike commute. Davis CA: 20%. Car-free transportation is a wealth signal, not a poverty one.",type:"XREF",geo:"us_city",fmt:"Scatter plot",tbl:"T727 Â· T629",section:"Income Â· Transportation",ext:["ACS commuting mode share by city (publicly available via Census Bureau)"],vars:["metro_per_capita_income","state_unemployment_rate"],join:["housing_cpi_city","pct_bachelors"],sc:{emotional:6,relatability:7,surprise:7,tension:4,visual:7,data_ready:7,originality:7},vs:67,tags:"cycling bike commute income city Portland Davis wealth infrastructure green transportation mode share Census ACS"}







,{id:"xref_weather_events_vs_income",title:"Billion-dollar weather disasters vs. median income by state",sub:"States with the most weather disasters per capita are often the poorest. Climate risk concentrates where wealth doesn't.",type:"XREF",geo:"us_state",fmt:"Scatter plot",tbl:"T727",section:"Income",ext:["NOAA billion-dollar weather events by state (publicly available via ncdc.noaa.gov)"],vars:["median_household_income"],join:["pct_on_snap","rep_pct","housing_permits_total"],sc:{emotional:8,relatability:7,surprise:8,tension:7,visual:8,data_ready:7,originality:8},vs:75,tags:"weather disasters income state NOAA climate risk poverty concentration flood tornado hurricane Alabama Mississippi Texas"}







,{id:"road_trip_america_county_choropleth",title:"Counties Americans drive through vs. counties Americans live in",sub:"The Great Plains: vast, road-tripped, sparsely lived. The coasts: dense, flown over, rarely driven. The two Americas.",type:"MAP",geo:"us_county",fmt:"County choropleth",tbl:"T1126",section:"Transportation",ext:["FHWA annual highway traffic volume by county (publicly available via fhwa.dot.gov)"],vars:["pct_bridges_poor"],join:["waterway_freight_tons","population_pct_change"],sc:{emotional:6,relatability:8,surprise:8,tension:2,visual:10,data_ready:7,originality:9},vs:72,tags:"road trip drive through county highway traffic Great Plains coast density live vs drive America geography curious visual"}







,{id:"xref_coal_county_income",title:"Coal production by county vs. median income â€” coal doesn't pay its workers",sub:"The 50 highest coal-producing counties average $42K median income. The resource is extracted; the wealth leaves.",type:"XREF",geo:"us_county",fmt:"Scatter plot",tbl:"T950 Â· T727",section:"Forestry Mining Â· Income",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by county (bls.gov â€” free)"],vars:["coal_production_index","median_household_income"],join:["state_unemployment_rate","pct_on_snap"],sc:{emotional:8,relatability:6,surprise:8,tension:7,visual:8,data_ready:9,originality:8},vs:75,tags:"coal county income wealth extraction poverty Appalachia West Virginia Kentucky resource curse workers wages stay leave"}







,{id:"xref_mining_fatalities_income",title:"Mining fatality rate vs. median income by state",sub:"The states where mining is most dangerous are also the poorest. Risk and poverty are the same map.",type:"XREF",geo:"us_state",fmt:"Scatter plot",tbl:"T949 Â· T727",section:"Mining Â· Income",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)"],vars:["coal_production_index","median_household_income"],join:["state_unemployment_rate","rep_pct"],sc:{emotional:8,relatability:5,surprise:7,tension:7,visual:7,data_ready:9,originality:7},vs:70,tags:"mining fatalities income poverty dangerous states Appalachia Wyoming coal metal risk MSHA workers safety"}







,{id:"mining_employment_vs_transfers",title:"Mining employment decline vs. federal transfer growth by state 2000â€“2024",sub:"As coal jobs disappeared, federal disability and Social Security payments grew to fill the gap. The replacement economy.",type:"XREF",geo:"us_state",fmt:"Scatter plot",tbl:"T950 Â· T573",section:"Mining Â· Social Insurance",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)"],vars:["coal_production_index","total_transfers_per_capita"],join:["state_unemployment_rate","rep_pct"],sc:{emotional:8,relatability:6,surprise:8,tension:7,visual:8,data_ready:9,originality:8},vs:74,tags:"mining employment decline federal transfers disability Social Security replacement economy Appalachia West Virginia Kentucky"}







,{id:"xref_construction_spending_income",title:"Construction spending growth vs. median income by state",sub:"States building the most are getting richer. The construction-prosperity feedback loop.",type:"XREF",geo:"us_state",fmt:"Scatter plot",tbl:"T1013 Â· T727",section:"Construction Â· Income",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)"],vars:["housing_permits_total","median_household_income"],join:["population_pct_change","home_price_index_2024"],sc:{emotional:6,relatability:7,surprise:6,tension:4,visual:7,data_ready:9,originality:6},vs:66,tags:"construction spending income state prosperity feedback loop building housing permits Florida Texas economy growth"}







,{id:"xref_housing_permits_snap",title:"New housing permits per capita vs. SNAP enrollment by state",sub:"States building more housing have lower food insecurity. Supply-side housing policy has bottom-line social effects.",type:"XREF",geo:"us_state",fmt:"Scatter plot",tbl:"T1011 Â· T576",section:"Construction Â· Social Insurance",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)"],vars:["housing_permits_total","pct_on_snap"],join:["median_household_income","home_price_index_2024"],sc:{emotional:7,relatability:7,surprise:8,tension:6,visual:7,data_ready:10,originality:8},vs:73,tags:"housing permits SNAP food stamps construction supply state connection affordability hunger poverty zoning reform"}







,{id:"data_center_construction_boom",title:"Data center construction spending 2015â€“2024 â€” the AI infrastructure gold rush",sub:"Data center construction went from $15B to $49B in 10 years. The physical infrastructure of the AI economy.",type:"CHART",geo:"us_national",fmt:"Area chart",tbl:"T1013",section:"Construction",ext:["FRED: any national economic time series (fred.stlouisfed.org â€” free API)","BLS national data: employment, wages, CPI (bls.gov â€” free API)"],vars:["data_center_construction"],join:["rd_pct_gdp","state_gdp_per_capita"],sc:{emotional:7,relatability:7,surprise:8,tension:5,visual:8,data_ready:10,originality:9},vs:74,tags:"data center construction AI infrastructure boom 2024 investment spending physical cloud computing hyperscaler Microsoft Amazon"}







,{id:"xref_aging_population_transfers",title:"65+ population share vs. federal transfers per capita by state",sub:"Florida: 22% elderly, $8,100 per person in transfers. The age-dependency math made geographic.",type:"XREF",geo:"us_state",fmt:"Scatter plot",tbl:"T573 Â· Population PDF",section:"Social Insurance Â· Population",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)"],vars:["total_transfers_per_capita","population_pct_change"],join:["total_medicare","pct_on_medicaid","rep_pct"],sc:{emotional:7,relatability:7,surprise:6,tension:7,visual:8,data_ready:9,originality:6},vs:72,tags:"aging elderly population federal transfers state Florida dependency ratio Medicare Social Security age 65 geography"}







,{id:"xref_foreign_born_pct_income",title:"Foreign-born population % vs. median income by state",sub:"High-immigrant states are mostly high-income states. The economic contribution of immigration, state by state.",type:"XREF",geo:"us_state",fmt:"Scatter plot",tbl:"T727 Â· Population PDF",section:"Income Â· Population",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)"],vars:["median_household_income","population_pct_change"],join:["pct_bachelors","rep_pct","state_unemployment_rate"],sc:{emotional:8,relatability:7,surprise:7,tension:7,visual:7,data_ready:8,originality:6},vs:74,tags:"immigrants foreign born income state economic contribution California New York Texas wealth prosperity vote immigration policy"}







,{id:"us_racial_wealth_gap_over_time",title:"Racial wealth gap 1989â€“2022 â€” the gap that doesn't close",sub:"White median household wealth: $285K. Black: $44K. Hispanic: $61K. The ratio barely changed in 33 years.",type:"CHART",geo:"us_national",fmt:"Line chart",tbl:"T1207",section:"Banking Finance Insurance",ext:["FRED: any national economic time series (fred.stlouisfed.org â€” free API)","BLS national data: employment, wages, CPI (bls.gov â€” free API)"],vars:["pct_families_own_stocks","pct_families_own_retirement","median_stock_value"],join:["median_household_income","pct_families_own_any_asset"],sc:{emotional:9,relatability:8,surprise:7,tension:9,visual:8,data_ready:9,originality:5},vs:81,tags:"racial wealth gap Black White Hispanic 1989 2022 33 years unchanged persistent inequality Federal Reserve survey wealth"}







,{id:"xref_immigration_snap_paradox",title:"Immigration rate vs. SNAP enrollment by state â€” immigrants don't take benefits",sub:"High-immigrant states have LOWER SNAP enrollment. Immigrants use fewer benefits per capita than native-born residents.",type:"XREF",geo:"us_state",fmt:"Scatter plot",tbl:"T576 Â· Population PDF",section:"Social Insurance Â· Population",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)"],vars:["pct_on_snap","population_pct_change"],join:["median_household_income","rep_pct","pct_bachelors"],sc:{emotional:9,relatability:8,surprise:9,tension:9,visual:8,data_ready:8,originality:9},vs:87,tags:"immigration SNAP food stamps paradox immigrants benefits usage native born myth welfare state California Texas data truth"}







,{id:"xref_federal_workers_income_state",title:"Federal civilian workers per capita vs. median income by state",sub:"Maryland has the most federal workers per capita AND the highest median income. Government employment pays.",type:"XREF",geo:"us_state",fmt:"Scatter plot",tbl:"T537 Â· T727",section:"Federal Govt Â· Income",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)"],vars:["federal_civilian_employment_state","median_household_income"],join:["total_transfers_per_capita","rep_pct"],sc:{emotional:7,relatability:6,surprise:7,tension:5,visual:7,data_ready:10,originality:7},vs:70,tags:"federal workers income state Maryland government employment pays well DC suburbs Virginia wealth prosperity stability"}







,{id:"federal_interest_vs_everything",title:"Federal interest payments vs. education, defense, and NASA 2024",sub:"$880B in debt interest. $873B in defense. $306B in education. $25B in NASA. Interest now exceeds defense.",type:"CHART",geo:"us_national",fmt:"Bar chart",tbl:"T512",section:"Federal Government Finances",ext:["FRED: any national economic time series (fred.stlouisfed.org â€” free API)","BLS national data: employment, wages, CPI (bls.gov â€” free API)"],vars:["federal_outlays_by_function","federal_debt_pct_gdp"],join:["defense_budget_total","college_tuition_cpi"],sc:{emotional:9,relatability:8,surprise:9,tension:9,visual:9,data_ready:10,originality:8},vs:86,tags:"federal interest debt defense education NASA 2024 exceeds comparison spending priorities fiscal crisis $880B Congress"}







,{id:"xref_federal_spending_vote",title:"Federal spending per capita by state vs. Republican vote share",sub:"The 10 states that get the most federal spending per capita all voted Republican in 2024. The dependency map.",type:"XREF",geo:"us_state",fmt:"Bivariate choropleth",tbl:"T573 Â· T454",section:"Federal Govt Â· Elections",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)","MIT Election Lab: presidential/congressional results (electionlab.mit.edu â€” free)"],vars:["total_transfers_per_capita","rep_pct"],join:["federal_civilian_employment_state","pct_on_snap"],sc:{emotional:10,relatability:8,surprise:8,tension:10,visual:9,data_ready:10,originality:7},vs:91,tags:"federal spending Republican vote state per capita dependency paradox MAGA red states government money fiscal hypocrisy"}







,{id:"federal_debt_by_president",title:"Federal debt added by each US president 1981â€“2024",sub:"Reagan +189%. Obama +88%. Trump +39% in 4 years. Biden +32%. The fiscal record vs. the fiscal rhetoric.",type:"CHART",geo:"us_national",fmt:"Bar chart",tbl:"T509",section:"Federal Government Finances",ext:["FRED: any national economic time series (fred.stlouisfed.org â€” free API)","BLS national data: employment, wages, CPI (bls.gov â€” free API)"],vars:["federal_debt_pct_gdp","federal_outlays_by_function"],join:["defense_budget_total"],sc:{emotional:9,relatability:8,surprise:8,tension:9,visual:9,data_ready:10,originality:7},vs:84,tags:"federal debt president Reagan Bush Obama Trump Biden fiscal record spending deficit added history comparison rhetoric reality"}







,{id:"xref_state_revenue_education",title:"State government revenue per capita vs. per-pupil school spending",sub:"Alaska: $42K revenue per person, $19K per pupil. Mississippi: $14K revenue, $11K per pupil. Revenue follows to schools.",type:"XREF",geo:"us_state",fmt:"Scatter plot",tbl:"T488 Â· T258",section:"State Govt Â· Education",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)"],vars:["state_local_revenue_per_capita","expenditure_per_pupil"],join:["revenue_federal_pct","avg_teacher_salary"],sc:{emotional:7,relatability:7,surprise:6,tension:5,visual:7,data_ready:10,originality:6},vs:69,tags:"state revenue education per pupil spending Alaska Mississippi school funding government resources investment children"}







,{id:"xref_lottery_education_spending",title:"Lottery revenue per capita vs. per-pupil education spending by state",sub:"States with the most lottery revenue don't spend more on schools. The lottery earmark is largely a shell game.",type:"XREF",geo:"us_state",fmt:"Scatter plot",tbl:"T493 Â· T258",section:"State Govt Â· Education",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)"],vars:["lottery_revenue_per_capita","expenditure_per_pupil"],join:["pct_on_snap","median_household_income"],sc:{emotional:8,relatability:7,surprise:8,tension:7,visual:7,data_ready:10,originality:8},vs:75,tags:"lottery education spending shell game earmark schools promise myth revenue displacement fungibility state Georgia Florida"}







,{id:"xref_state_debt_income",title:"State and local debt per capita vs. median income by state",sub:"Connecticut: $20K debt per person, $91K income. Wyoming: $5K debt, $70K income. Debt doesn't correlate with wealth.",type:"XREF",geo:"us_state",fmt:"Scatter plot",tbl:"T486 Â· T727",section:"State Govt Â· Income",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)"],vars:["state_local_debt_per_capita","median_household_income"],join:["state_general_fund_balance","rep_pct"],sc:{emotional:7,relatability:6,surprise:7,tension:5,visual:7,data_ready:10,originality:7},vs:68,tags:"state debt income per capita Connecticut Wyoming correlation fiscal liability bonds pension income wealth government"}







,{id:"xref_sports_betting_lottery_income",title:"Sports betting + lottery revenue vs. median income by state",sub:"Lower-income states spend more per capita on gambling. The regressive tax is growing with sports betting.",type:"XREF",geo:"us_state",fmt:"Scatter plot",tbl:"T493 Â· T727",section:"State Govt Â· Income",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)"],vars:["lottery_revenue_per_capita","median_household_income"],join:["sports_betting_revenue","pct_on_snap","rep_pct"],sc:{emotional:8,relatability:8,surprise:7,tension:7,visual:8,data_ready:10,originality:7},vs:77,tags:"gambling lottery sports betting income regressive tax poor spending state desperation hope poverty New Jersey Illinois revenue"}







,{id:"xref_manufacturing_gdp_transfers",title:"Manufacturing share of state GDP vs. federal transfers per capita",sub:"High-manufacturing states get LESS federal aid. They make things and subsidize the states that don't.",type:"XREF",geo:"us_state",fmt:"Scatter plot",tbl:"T1062 Â· T573",section:"Manufactures Â· Social Insurance",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)"],vars:["manufacturing_value_added_state","total_transfers_per_capita"],join:["rep_pct","state_unemployment_rate"],sc:{emotional:8,relatability:6,surprise:8,tension:7,visual:7,data_ready:10,originality:8},vs:74,tags:"manufacturing GDP federal transfers subsidize Indiana Ohio Wisconsin Pennsylvania Michigan makes things wealth redistribution"}







,{id:"manufacturing_wages_by_industry_2024",title:"Average manufacturing wages by industry 2024 â€” the pay hierarchy",sub:"Petroleum/coal products workers: $48/hr. Apparel workers: $17/hr. The same 'factory job' has a 3x pay gap.",type:"RANK",geo:"us_national",fmt:"Ranked list",tbl:"T1067",section:"Manufactures",ext:["FRED: any national economic time series (fred.stlouisfed.org â€” free API)","BLS national data: employment, wages, CPI (bls.gov â€” free API)"],vars:["manufacturing_hourly_wages_state"],join:["manufacturing_employment_trend"],sc:{emotional:7,relatability:7,surprise:8,tension:4,visual:9,data_ready:10,originality:7},vs:73,tags:"manufacturing wages industry hierarchy petroleum apparel pay gap factory job not equal 2024 sector worker wages"}







,{id:"xref_manufacturing_shipments_trade",title:"State manufacturing shipments vs. trade deficit â€” do we make enough to close the gap?",sub:"US manufactures $7T in goods annually â€” but imports $3T net. The production-consumption gap is structural.",type:"CHART",geo:"us_national",fmt:"Line chart",tbl:"T1063 Â· T1306",section:"Manufactures Â· Trade",ext:["FRED: any national economic time series (fred.stlouisfed.org â€” free API)","BLS national data: employment, wages, CPI (bls.gov â€” free API)"],vars:["manufacturing_shipments_state","current_account_balance"],join:["trade_balance_goods","foreign_affiliate_employment"],sc:{emotional:7,relatability:6,surprise:8,tension:7,visual:7,data_ready:10,originality:8},vs:72,tags:"manufacturing shipments trade deficit structural gap $7T production imports goods balance America makes buys more"}







,{id:"xref_retail_sales_snap",title:"Per capita retail sales vs. SNAP enrollment by state â€” the retail desert",sub:"The lowest retail-sales states have the highest SNAP rates. Where there's no commerce, there's hunger.",type:"XREF",geo:"us_state",fmt:"Scatter plot",tbl:"T1090 Â· T576",section:"Retail Â· Social Insurance",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)"],vars:["retail_sales_per_capita","pct_on_snap"],join:["median_household_income","rep_pct"],sc:{emotional:7,relatability:7,surprise:7,tension:6,visual:7,data_ready:10,originality:7},vs:70,tags:"retail sales SNAP food stamps state desert low commerce hunger food insecurity Mississippi Arkansas poor economy"}







,{id:"motor_vehicle_retail_boom_bust",title:"Motor vehicle retail sales 2015â€“2024 â€” pandemic boom, rate bust",sub:"New vehicle sales hit $1.56T in 2021 as low rates drove buying. Then rates rose and sales collapsed. The boom-bust.",type:"CHART",geo:"us_national",fmt:"Area chart",tbl:"T1096",section:"Wholesale & Retail Trade",ext:["FRED: any national economic time series (fred.stlouisfed.org â€” free API)","BLS national data: employment, wages, CPI (bls.gov â€” free API)"],vars:["retail_sales_per_capita"],join:["motor_vehicle_insurance_cpi","mortgage_delinquency_rate"],sc:{emotional:6,relatability:8,surprise:7,tension:5,visual:8,data_ready:10,originality:6},vs:68,tags:"motor vehicle retail sales pandemic boom 2021 rate hike bust 2022 2023 2024 cars trucks dealerships inflation Fed"}







,{id:"ecommerce_displacement_employment",title:"E-commerce growth vs. retail employment 2000â€“2024 â€” the jobs that disappeared",sub:"E-commerce went from 1% to 22% of retail. 700,000 retail jobs were displaced. The Amazon effect in two lines.",type:"CHART",geo:"us_national",fmt:"Line chart",tbl:"T1093 Â· T629",section:"Retail Â· Labor",ext:["FRED: any national economic time series (fred.stlouisfed.org â€” free API)","BLS national data: employment, wages, CPI (bls.gov â€” free API)"],vars:["ecommerce_sales","state_unemployment_rate"],join:["retail_sales_per_capita"],sc:{emotional:8,relatability:8,surprise:7,tension:7,visual:8,data_ready:9,originality:7},vs:76,tags:"e-commerce retail employment displacement Amazon 2000 2024 jobs displaced workers stores closures automation internet shopping"}







,{id:"map_opioid_deaths_by_county",title:"Opioid overdose death rate by county 2023",sub:"McDowell County WV: 90 deaths per 100K. Some suburban counties: under 3. The opioid geography of despair.",type:"MAP",geo:"us_county",fmt:"County choropleth",tbl:"T573 Â· T141",section:"Social Insurance Â· Health",ext:["CDC overdose death data by county (publicly available via CDC WONDER)"],vars:["total_transfers_per_capita","per_capita_health_spending"],join:["state_unemployment_rate","pct_on_snap","median_household_income"],sc:{emotional:10,relatability:9,surprise:7,tension:9,visual:9,data_ready:8,originality:7},vs:90,tags:"opioid overdose death county McDowell West Virginia despair fentanyl geography Appalachia rural poverty crisis CDC epidemic"}







,{id:"xref_corporate_profit_vs_homelessness",title:"Corporate profit growth vs. homelessness rate by state",sub:"Corporate profits tripled since 2000. Homelessness in California, Washington, and Oregon also tripled. The divergence is geographic.",type:"XREF",geo:"us_state",fmt:"Scatter plot",tbl:"T793 Â· T727",section:"Business Â· Income",ext:["HUD Annual Homeless Assessment Report by state (publicly available via hud.gov)"],vars:["corporate_profits","median_household_income"],join:["home_price_index_2024","housing_permits_total"],sc:{emotional:9,relatability:8,surprise:8,tension:9,visual:8,data_ready:8,originality:8},vs:84,tags:"corporate profits homelessness state California Washington Oregon inequality housing affordability tent cities wealth divergence"}







,{id:"map_eviction_rate_county",title:"Eviction rate by county â€” the hidden housing crisis",sub:"Some Southern counties evict 1 in 10 renters annually. Some Minneapolis suburbs: under 1 in 200. The eviction geography.",type:"MAP",geo:"us_county",fmt:"County choropleth",tbl:"T771 Â· T727",section:"Housing Â· Income",ext:["Princeton Eviction Lab county eviction data (publicly available via evictionlab.org)"],vars:["home_price_index_2024","median_household_income"],join:["pct_on_snap","mortgage_delinquency_rate"],sc:{emotional:9,relatability:8,surprise:8,tension:8,visual:9,data_ready:8,originality:8},vs:84,tags:"eviction rate county housing crisis renters South Georgia Virginia Carolina poor tenants court landlord inequality displacement"}







,{id:"map_gun_deaths_by_state",title:"Gun death rate by state 2023 â€” the full picture including suicide",sub:"Mississippi: 33 gun deaths per 100K. Hawaii: 3.4. The 10x gap the debate always misses.",type:"MAP",geo:"us_state",fmt:"State choropleth",tbl:"T340",section:"Law Enforcement",ext:["CDC gun death data by state (publicly available via CDC WONDER)"],vars:["violent_crime_rate","murder_rate"],join:["rep_pct","median_household_income","pct_bachelors"],sc:{emotional:9,relatability:8,surprise:8,tension:9,visual:9,data_ready:8,originality:6},vs:84,tags:"gun deaths state 2023 suicide total Mississippi Hawaii rate inequality CDC policy debate full picture Republican vote"}







,{id:"xref_gun_ownership_gun_deaths",title:"Gun ownership rate vs. gun death rate by state",sub:"States with the most guns have the most gun deaths. The correlation is 0.84 â€” one of the strongest in public health.",type:"XREF",geo:"us_state",fmt:"Scatter plot",tbl:"T340",section:"Law Enforcement",ext:["Rand State Firearm Law Database / CDC gun death data (publicly available)"],vars:["violent_crime_rate","murder_rate"],join:["rep_pct","median_household_income"],sc:{emotional:9,relatability:8,surprise:7,tension:9,visual:8,data_ready:8,originality:7},vs:83,tags:"gun ownership gun deaths correlation state public health 0.84 strongest relationship policy debate data evidence"}







,{id:"xref_social_mobility_parents_income",title:"Economic mobility â€” what your parents earned predicts what you'll earn",sub:"Kids born in the bottom quintile in Mississippi have a 4.5% chance of reaching the top quintile. In Utah: 11.5%.",type:"MAP",geo:"us_state",fmt:"State choropleth",tbl:"T727",section:"Income",ext:["Raj Chetty Opportunity Atlas mobility data (publicly available via opportunityinsights.org)"],vars:["median_household_income","pct_under_25k"],join:["pct_bachelors","rep_pct","violent_crime_rate"],sc:{emotional:10,relatability:9,surprise:8,tension:9,visual:9,data_ready:8,originality:7},vs:90,tags:"social mobility income parents children quintile Mississippi Utah opportunity geography class race American dream myth data"}







,{id:"xref_ceo_pay_worker_pay",title:"CEO-to-worker pay ratio by industry 2023",sub:"Fast food CEOs earn 1,000x their median worker. Hospital CEOs: 820x. Tech CEOs: 670x. The ratio, ranked.",type:"RANK",geo:"us_national",fmt:"Ranked list",tbl:"T793",section:"Business Enterprise",ext:["AFL-CIO Executive PayWatch (publicly available via aflcio.org)"],vars:["corporate_profits","income_tax_after_credits"],join:["median_household_income","state_unemployment_rate"],sc:{emotional:9,relatability:9,surprise:8,tension:9,visual:9,data_ready:8,originality:7},vs:85,tags:"CEO worker pay ratio 1000x fast food hospital tech industry inequality class executives compensation wages gap"}







,{id:"us_incarceration_vs_world",title:"US incarceration rate vs. peer nations â€” we are the outlier",sub:"US: 531 per 100K incarcerated. Canada: 104. Germany: 69. UK: 126. The American exception in criminal justice.",type:"RANK",geo:"worldwide",fmt:"Ranked list",tbl:"T340",section:"Law Enforcement",ext:["World Prison Brief incarceration data (publicly available via prisonstudies.org)"],vars:["violent_crime_rate","murder_rate"],join:["rep_pct","median_household_income"],sc:{emotional:9,relatability:8,surprise:8,tension:8,visual:9,data_ready:8,originality:6},vs:82,tags:"incarceration prison rate US world comparison Canada Germany UK outlier criminal justice mass incarceration policy race"}







,{id:"world_obesity_rate_by_country",title:"Obesity rate by country vs. per capita income",sub:"Pacific island nations: 50%+ obesity. Japan: 4%. US: 42%. The wealth-obesity relationship is not what you'd expect.",type:"XREF",geo:"worldwide",fmt:"Scatter plot",tbl:"T141",section:"Health",ext:["WHO Global Health Observatory obesity data (publicly available via who.int)"],vars:["per_capita_health_spending"],join:["population_pct_change_2020_2025","rd_pct_gdp"],sc:{emotional:7,relatability:7,surprise:8,tension:5,visual:8,data_ready:8,originality:7},vs:72,tags:"obesity rate country income WHO wealth Pacific Islands Japan US 42% international health comparison lifestyle diet"}







,{id:"us_vacation_days_vs_world",title:"Mandated paid vacation days by country â€” the US has zero",sub:"France: 30 mandated days. Germany: 24. Japan: 10. United States: 0. The only wealthy country with no minimum.",type:"RANK",geo:"worldwide",fmt:"Ranked list",tbl:"T629",section:"Labor",ext:["OECD employment conditions data (publicly available via oecd.org)"],vars:["state_unemployment_rate","female_lfp_rate"],join:["median_household_income","rd_pct_gdp"],sc:{emotional:8,relatability:9,surprise:8,tension:6,visual:9,data_ready:8,originality:5},vs:79,tags:"vacation days mandated paid leave US zero France Germany Japan international comparison labor rights work life balance"}







,{id:"world_child_poverty_rate",title:"Child poverty rate by wealthy nation â€” the US is last",sub:"US child poverty: 17.4%. Denmark: 3.7%. Germany: 11.4%. In child poverty, the US ranks worst among peer nations.",type:"RANK",geo:"worldwide",fmt:"Ranked list",tbl:"T576",section:"Social Insurance",ext:["UNICEF child poverty data (publicly available via data.unicef.org)"],vars:["pct_on_snap","pct_on_medicaid"],join:["teen_birth_rate","median_household_income"],sc:{emotional:9,relatability:8,surprise:7,tension:8,visual:9,data_ready:8,originality:5},vs:80,tags:"child poverty US worst peer nations Denmark Germany UNICEF ranking wealthy countries policy social safety net kids"}







,{id:"soccer_participation_vs_income",title:"Youth soccer participation rate vs. median income by county",sub:"Youth soccer is a wealthy-suburb sport. Participation collapses in low-income areas â€” the pay-to-play barrier.",type:"XREF",geo:"us_county",fmt:"Scatter plot",tbl:"T727 Â· T1273",section:"Income Â· Recreation",ext:["US Youth Soccer participation data / ACS income by county (publicly available)"],vars:["median_household_income","sports_attendance_12mo"],join:["pct_bachelors","rep_pct"],sc:{emotional:6,relatability:7,surprise:7,tension:5,visual:8,data_ready:7,originality:8},vs:69,tags:"soccer youth participation income county pay to play wealthy suburb barrier sport access inequality race class travel team"}







,{id:"fishing_license_revenue_by_state",title:"Fishing license revenue by state â€” where Americans still fish",sub:"Wisconsin: $56M in fishing licenses. Texas: $52M. The fishing economy geography.",type:"MAP",geo:"us_state",fmt:"State choropleth",tbl:"T942",section:"Forestry Fishing",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)"],vars:["port_catch_lbs","port_catch_value"],join:["national_forest_acres","median_household_income"],sc:{emotional:5,relatability:7,surprise:6,tension:2,visual:9,data_ready:9,originality:6},vs:65,tags:"fishing license revenue state Wisconsin Texas sportfishing recreational anglers freshwater saltwater economy culture outdoor"}







,{id:"bike_commute_mode_share_trend",title:"Bike commuting mode share 2005â€“2024 â€” the boom that wasn't",sub:"Bike commuting peaked at 0.6% in 2014 and fell back to 0.4% in 2024. Despite billions in infrastructure.",type:"CHART",geo:"us_national",fmt:"Line chart",tbl:"T629",section:"Labor",ext:["ACS commuting mode share by year (publicly available via Census Bureau)"],vars:["state_unemployment_rate"],join:["housing_cpi_city","metro_per_capita_income"],sc:{emotional:6,relatability:7,surprise:7,tension:4,visual:7,data_ready:8,originality:7},vs:66,tags:"bike commute mode share trend 2005 2024 failed peak cycling infrastructure spending decline car dependence urban planning"}







,{id:"xref_weather_outdoor_recreation",title:"Sunshine hours vs. outdoor recreation economy by state",sub:"Colorado: 300 sunny days, $34B outdoor recreation economy. Arizona: 300 days, $26B. Weather and recreation align.",type:"XREF",geo:"us_state",fmt:"Scatter plot",tbl:"T727",section:"Income",ext:["NOAA sunshine hours by state (publicly available via NOAA)", "BEA outdoor recreation satellite account (publicly available)"],vars:["median_household_income","real_per_capita_income"],join:["national_forest_acres","energy_consumption_per_capita"],sc:{emotional:5,relatability:7,surprise:7,tension:2,visual:7,data_ready:7,originality:7},vs:64,tags:"sunshine hours outdoor recreation economy state Colorado Arizona weather climate tourism hiking skiing biking fishing revenue"}







,{id:"life_expectancy_by_state",title:"Life expectancy at birth by state 2021 â€” the 8-year gap",sub:"Hawaii: 79.9 years. Mississippi: 71.9. West Virginia: 72.8. The geography of how long Americans live.",type:"MAP",geo:"us_state",fmt:"State choropleth",tbl:"T105",section:"Births Deaths",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)","CDC WONDER: mortality + disease rates by county/state (wonder.cdc.gov â€” free)"],vars:["birth_rate_state","total_fertility_rate_by_race"],join:["median_household_income","pct_on_snap","rep_pct"],sc:{emotional:9,relatability:9,surprise:7,tension:8,visual:9,data_ready:10,originality:5},vs:83,tags:"life expectancy state 2021 Hawaii Mississippi West Virginia gap income poverty health racial inequality geography mortality"}







,{id:"infant_mortality_by_race_state",title:"Infant mortality rate by race and state 2023",sub:"Black infant mortality: 10.9 per 1,000. White: 4.5. The 2.4x racial gap exists in every state.",type:"MAP",geo:"us_state",fmt:"State choropleth",tbl:"T115",section:"Births Deaths",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)","CDC WONDER: mortality + disease rates by county/state (wonder.cdc.gov â€” free)"],vars:["birth_rate_state","total_fertility_rate_by_race"],join:["pct_births_unmarried","teen_birth_rate","median_household_income"],sc:{emotional:10,relatability:8,surprise:7,tension:9,visual:9,data_ready:10,originality:6},vs:87,tags:"infant mortality race Black White state 2023 gap 2.4x racial inequality healthcare prenatal poverty systematic"}







,{id:"death_rate_cause_over_time",title:"Death rates by major cause 1960â€“2023 â€” what's killing Americans now vs. then",sub:"Heart disease down 65%. Alzheimer's up 700%. Cancer largely flat. The cause-of-death revolution.",type:"CHART",geo:"us_national",fmt:"Line chart",tbl:"T117",section:"Births Deaths",ext:["FRED: any national economic time series (fred.stlouisfed.org â€” free API)","BLS national data: employment, wages, CPI (bls.gov â€” free API)"],vars:["birth_rate_state","total_fertility_rate_by_race"],join:["per_capita_health_spending","pct_on_medicaid"],sc:{emotional:8,relatability:8,surprise:8,tension:6,visual:9,data_ready:10,originality:6},vs:78,tags:"death cause heart disease Alzheimer cancer 1960 2023 trend decline rise history mortality shift healthcare medicine"}







,{id:"life_expectancy_race_1940_2022",title:"Life expectancy by race 1940â€“2022 â€” the gap that COVID briefly closed then reopened",sub:"In 1980: Black LE 68.1, White 74.4. In 2019: Black 74.7, White 78.8. COVID hit Black Americans hardest, reset progress.",type:"CHART",geo:"us_national",fmt:"Line chart",tbl:"T103",section:"Births Deaths",ext:["FRED: any national economic time series (fred.stlouisfed.org â€” free API)","BLS national data: employment, wages, CPI (bls.gov â€” free API)"],vars:["birth_rate_state","total_fertility_rate_by_race"],join:["pct_on_medicaid","per_capita_health_spending","pct_on_snap"],sc:{emotional:9,relatability:8,surprise:8,tension:9,visual:9,data_ready:10,originality:7},vs:84,tags:"life expectancy race Black White 1940 2022 COVID gap progress reset history inequality racial health systematic disparity"}







,{id:"maternal_mortality_by_race",title:"Maternal mortality rate by race 2018â€“2023",sub:"Black maternal mortality: 37.1 per 100K live births. White: 14.5. Hispanic: 11.3. The 2.5x racial gap.",type:"CHART",geo:"us_national",fmt:"Line chart",tbl:"T116",section:"Births Deaths",ext:["FRED: any national economic time series (fred.stlouisfed.org â€” free API)","BLS national data: employment, wages, CPI (bls.gov â€” free API)"],vars:["birth_rate_state","pct_births_unmarried"],join:["pct_on_medicaid","per_capita_health_spending","teen_birth_rate"],sc:{emotional:10,relatability:8,surprise:7,tension:9,visual:8,data_ready:10,originality:6},vs:85,tags:"maternal mortality race Black White Hispanic 2023 gap childbirth death obstetric healthcare inequality racial systematic bias"}







,{id:"abortion_rates_by_state_2022",title:"Abortion rate and out-of-state travel by state 2022",sub:"Some states saw 500%+ increases in out-of-state abortion seekers post-Dobbs. The access geography in hard numbers.",type:"MAP",geo:"us_state",fmt:"State choropleth",tbl:"T100",section:"Births Deaths",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)","MIT Election Lab: presidential/congressional results (electionlab.mit.edu â€” free)"],vars:["pct_births_unmarried","birth_rate_state"],join:["rep_pct","teen_birth_rate","median_household_income"],sc:{emotional:10,relatability:8,surprise:8,tension:10,visual:9,data_ready:10,originality:8},vs:91,tags:"abortion rate state 2022 Dobbs out of state travel access map post-Roe geography seeking care Guttmacher ProQuest"}







,{id:"hate_crimes_trend",title:"Hate crimes 2010â€“2023 â€” the surge that nobody calls a trend",sub:"Hate crime incidents: 6,628 in 2010. 11,862 in 2023. An 79% increase. Anti-Black hate crimes still #1.",type:"CHART",geo:"us_national",fmt:"Line chart",tbl:"T348",section:"Law Enforcement",ext:["FRED: any national economic time series (fred.stlouisfed.org â€” free API)","BLS national data: employment, wages, CPI (bls.gov â€” free API)"],vars:["violent_crime_rate","murder_rate"],join:["rep_pct","median_household_income"],sc:{emotional:9,relatability:7,surprise:8,tension:9,visual:8,data_ready:10,originality:7},vs:82,tags:"hate crimes trend 2010 2023 surge 79% increase anti-Black anti-Asian anti-LGBTQ racial religion bias incidents FBI UCR"}







,{id:"prison_population_by_state",title:"Prison population rate by state 2023",sub:"Mississippi: 625 per 100K residents incarcerated. Massachusetts: 118. The 5x incarceration gap within America.",type:"MAP",geo:"us_state",fmt:"State choropleth",tbl:"T388",section:"Law Enforcement",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)","FBI Crime Data Explorer: UCR/NIBRS by state/agency (cde.ucr.cjis.gov â€” free)"],vars:["violent_crime_rate","murder_rate"],join:["median_household_income","rep_pct","pct_on_snap"],sc:{emotional:9,relatability:7,surprise:7,tension:8,visual:9,data_ready:10,originality:5},vs:80,tags:"incarceration prison population rate state Mississippi Massachusetts 5x gap inequality race poverty criminal justice policy"}







,{id:"bankruptcy_filings_by_state",title:"Personal bankruptcy filings by state 2024 â€” the financial distress map",sub:"Tennessee: 420 filings per 100K residents. North Dakota: 47. The 9x bankruptcy rate gap across America.",type:"MAP",geo:"us_state",fmt:"State choropleth",tbl:"T816",section:"Business Enterprise",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)"],vars:["mortgage_delinquency_rate","credit_card_rate_all_accounts"],join:["median_household_income","state_unemployment_rate","rep_pct"],sc:{emotional:8,relatability:8,surprise:8,tension:7,visual:9,data_ready:10,originality:7},vs:78,tags:"bankruptcy filings state 2024 Tennessee North Dakota financial distress debt households personal chapter 7 13 rate per capita"}







,{id:"internet_crime_loss_by_state",title:"Internet crime reported losses by state 2024",sub:"California: $2.2B in reported internet crime losses. The FBI IC3 fraud geography.",type:"MAP",geo:"us_state",fmt:"State choropleth",tbl:"T353",section:"Law Enforcement",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)","FBI Crime Data Explorer: UCR/NIBRS by state/agency (cde.ucr.cjis.gov â€” free)"],vars:["violent_crime_rate"],join:["median_household_income","pct_bachelors"],sc:{emotional:7,relatability:8,surprise:7,tension:5,visual:9,data_ready:10,originality:8},vs:72,tags:"internet crime fraud loss state 2024 FBI IC3 scam cyber phishing identity theft California geographic financial"}







,{id:"xref_incarceration_race",title:"Incarceration rate by race and state â€” the racial disparity map",sub:"Black incarceration rate: 4.8x white rate nationally. But in some states the gap is 10x or more.",type:"MAP",geo:"us_state",fmt:"Bivariate choropleth",tbl:"T389 Â· T388",section:"Law Enforcement",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)","FBI Crime Data Explorer: UCR/NIBRS by state/agency (cde.ucr.cjis.gov â€” free)"],vars:["violent_crime_rate","murder_rate"],join:["median_household_income","rep_pct","pct_on_snap"],sc:{emotional:10,relatability:7,surprise:7,tension:9,visual:9,data_ready:9,originality:7},vs:85,tags:"incarceration race Black White disparity 4.8x state gap racial inequality criminal justice systemic bias mass incarceration"}







,{id:"death_penalty_executions_by_state",title:"Executions by state 1977â€“2024 â€” who still uses the death penalty",sub:"Texas: 587 executions. Oklahoma: 127. Florida: 106. 21 states have abolished it. The death penalty geography.",type:"MAP",geo:"us_state",fmt:"State choropleth",tbl:"T391",section:"Law Enforcement",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)","FBI Crime Data Explorer: UCR/NIBRS by state/agency (cde.ucr.cjis.gov â€” free)"],vars:["violent_crime_rate","murder_rate"],join:["rep_pct","median_household_income"],sc:{emotional:8,relatability:6,surprise:7,tension:8,visual:9,data_ready:10,originality:6},vs:75,tags:"death penalty executions state 1977 2024 Texas Oklahoma Florida abolished 21 states capital punishment geography justice"}







,{id:"minority_owned_firms_by_type",title:"Minority-owned employer firms: share of all businesses by state",sub:"1.33M minority-owned firms. $2.1T in revenue. 10.8M employees. The minority business economy mapped.",type:"MAP",geo:"us_state",fmt:"State choropleth",tbl:"T810",section:"Business Enterprise",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)"],vars:["corporate_profits","state_gdp_per_capita"],join:["median_household_income","pct_bachelors","rep_pct"],sc:{emotional:7,relatability:7,surprise:7,tension:5,visual:9,data_ready:10,originality:7},vs:72,tags:"minority owned firms businesses state employer revenue employees Black Hispanic Asian diversity business economy share geography"}







,{id:"black_owned_firms_revenue_share",title:"Black-owned employer firms: revenue vs. population share by state",sub:"Black Americans are 13% of the population. Black-owned firms generate 2.8% of employer revenue. The wealth gap in business.",type:"MAP",geo:"us_state",fmt:"State choropleth",tbl:"T812",section:"Business Enterprise",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)"],vars:["corporate_profits"],join:["median_household_income","violent_crime_rate","rep_pct"],sc:{emotional:9,relatability:7,surprise:8,tension:8,visual:8,data_ready:9,originality:8},vs:80,tags:"Black owned businesses revenue share population gap wealth inequality 2.8% 13% systemic economic disparity race business"}







,{id:"patents_issued_by_state",title:"Patents issued per capita by state 2023",sub:"Massachusetts: 4.2 patents per 1,000 residents. Mississippi: 0.3. The innovation geography of America.",type:"MAP",geo:"us_state",fmt:"State choropleth",tbl:"T818",section:"Science & Technology",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)"],vars:["rd_pct_gdp"],join:["pct_bachelors","median_household_income","state_gdp_per_capita"],sc:{emotional:6,relatability:6,surprise:7,tension:5,visual:9,data_ready:10,originality:7},vs:69,tags:"patents per capita state innovation Massachusetts Mississippi geography knowledge economy tech California New York Texas USPTO"}







,{id:"telework_rate_by_industry",title:"Telework arrangements by industry 2022 â€” who got to stay home",sub:"Information sector: 45% remote-capable. Retail: 5%. Food service: 2%. The remote work divide by industry.",type:"RANK",geo:"top_n_list",fmt:"Ranked list",tbl:"T800",section:"Business Enterprise",ext:[],vars:["corporate_profits","state_gdp_per_capita"],join:["state_unemployment_rate","median_household_income"],sc:{emotional:7,relatability:9,surprise:7,tension:5,visual:9,data_ready:10,originality:7},vs:74,tags:"remote work telework industry 2022 information retail food service divide class white collar blue collar geography COVID"}







,{id:"xref_patents_income_state",title:"Patents per capita vs. median income by state",sub:"States that innovate more earn more. The patent-prosperity correlation is 0.78.",type:"XREF",geo:"us_state",fmt:"Scatter plot",tbl:"T818 Â· T727",section:"Science Â· Income",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)"],vars:["rd_pct_gdp","median_household_income"],join:["pct_bachelors","state_gdp_per_capita","rep_pct"],sc:{emotional:7,relatability:6,surprise:7,tension:5,visual:7,data_ready:10,originality:7},vs:69,tags:"patents income state prosperity correlation 0.78 innovation wealth Massachusetts California New York Mississippi knowledge economy"}







,{id:"startup_birth_death_rate",title:"Business establishment births vs. deaths by industry 2022",sub:"Bars and restaurants: highest death rate. Professional services: highest birth rate. The business Darwinism data.",type:"CHART",geo:"us_national",fmt:"Scatter plot",tbl:"T806",section:"Business Enterprise",ext:["FRED: any national economic time series (fred.stlouisfed.org â€” free API)","BLS national data: employment, wages, CPI (bls.gov â€” free API)"],vars:["corporate_profits"],join:["state_unemployment_rate","ecommerce_sales"],sc:{emotional:7,relatability:7,surprise:7,tension:4,visual:8,data_ready:10,originality:7},vs:69,tags:"business startup birth death rate industry 2022 restaurant bar professional services churn survival failure innovation economy"}







,{id:"outdoor_recreation_by_state",title:"Outdoor recreation sector gross output by state 2023",sub:"Colorado: $32B outdoor recreation economy. California: $86B. Montana: $10B on just 1M people.",type:"MAP",geo:"us_state",fmt:"State choropleth",tbl:"T1264",section:"Arts Recreation",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)"],vars:["annual_attendance","sports_attendance_12mo"],join:["national_forest_acres","median_household_income","coastline_miles"],sc:{emotional:6,relatability:8,surprise:8,tension:3,visual:9,data_ready:10,originality:8},vs:73,tags:"outdoor recreation economy state Colorado California Montana GDP per capita hiking skiing fishing biking nature tourism industry"}







,{id:"national_parks_visits_by_state",title:"National Park visits by state 2024 â€” who actually uses public land",sub:"Arizona national parks: 11.2M visits. Wyoming: 9.8M. California: 32M. The public land usage geography.",type:"MAP",geo:"us_state",fmt:"State choropleth",tbl:"T1278",section:"Arts Recreation",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)"],vars:["annual_attendance","national_forest_acres"],join:["median_household_income","energy_consumption_per_capita"],sc:{emotional:5,relatability:7,surprise:7,tension:3,visual:9,data_ready:10,originality:7},vs:67,tags:"national parks visits state 2024 Arizona Wyoming California public land recreation tourism access nature outdoor per capita usage"}







,{id:"wildlife_recreation_spending",title:"Wildlife-related recreation spending 2022 â€” hunting, fishing, wildlife watching",sub:"Americans spent $182B on wildlife recreation in 2022. Wildlife watching alone: $55B. More than the NFL.",type:"CHART",geo:"us_national",fmt:"Treemap",tbl:"T1281",section:"Arts Recreation",ext:["FRED: any national economic time series (fred.stlouisfed.org â€” free API)","BLS national data: employment, wages, CPI (bls.gov â€” free API)"],vars:["sports_attendance_12mo","annual_attendance"],join:["national_forest_acres","coastline_miles"],sc:{emotional:5,relatability:7,surprise:8,tension:2,visual:9,data_ready:10,originality:8},vs:68,tags:"wildlife recreation spending 2022 hunting fishing wildlife watching $182B birding nature outdoor economy NFL comparison surprising"}







,{id:"foreign_tourists_by_country",title:"Foreign tourists to the US by country of origin 2023",sub:"Canada: 20M visitors. Mexico: 25M. UK: 5.2M. South Korea: 1.4M. The inbound tourism geography.",type:"MAP",geo:"worldwide",fmt:"World choropleth",tbl:"T1291",section:"Arts Recreation",ext:["World Bank Open Data: GDP, population, income by country (data.worldbank.org â€” free API)"],vars:["annual_attendance"],join:["net_migration_rate","trade_balance_goods"],sc:{emotional:5,relatability:7,surprise:7,tension:2,visual:9,data_ready:10,originality:6},vs:65,tags:"foreign tourists US 2023 Canada Mexico UK South Korea visitors inbound tourism international travel origin country map"}







,{id:"arts_attendance_by_type_income",title:"Arts event attendance by income level â€” who goes to the symphony",sub:"Symphony and opera attendance: 40% from households over $100K. Sports events: much more democratic.",type:"CHART",geo:"us_national",fmt:"Bar chart",tbl:"T1262",section:"Arts Recreation",ext:["FRED: any national economic time series (fred.stlouisfed.org â€” free API)","BLS national data: employment, wages, CPI (bls.gov â€” free API)"],vars:["annual_attendance","sports_attendance_12mo","state_arts_appropriation"],join:["median_household_income","pct_bachelors"],sc:{emotional:7,relatability:8,surprise:7,tension:5,visual:8,data_ready:10,originality:8},vs:74,tags:"arts attendance income symphony opera jazz museum sports concert event class wealthy poor who goes culture access"}







,{id:"airfare_cost_trend",title:"Average domestic airfare 1995â€“2024 â€” the long deflation reversed",sub:"Domestic airfare in 2024 dollars: down 20% from 1995 to 2019. Then up 40% post-COVID. The airline price whipsaw.",type:"CHART",geo:"us_national",fmt:"Line chart",tbl:"T1293",section:"Arts Recreation",ext:["FRED: any national economic time series (fred.stlouisfed.org â€” free API)","BLS national data: employment, wages, CPI (bls.gov â€” free API)"],vars:["passengers_enplaned","pct_ontime_arrivals"],join:["all_items_cpi","median_household_income"],sc:{emotional:7,relatability:8,surprise:7,tension:4,visual:8,data_ready:10,originality:6},vs:70,tags:"airfare domestic price trend 1995 2024 inflation deflation COVID post-pandemic reversal airline travel cost consumer"}







,{id:"digital_economy_gdp_share",title:"Digital economy share of US GDP 2017â€“2023",sub:"The digital economy grew from 9.4% to 10.3% of GDP. $2.6T in value added â€” but only 7M workers.",type:"CHART",geo:"us_national",fmt:"Area chart",tbl:"T1169",section:"Information",ext:["FRED: any national economic time series (fred.stlouisfed.org â€” free API)","BLS national data: employment, wages, CPI (bls.gov â€” free API)"],vars:["newspaper_print_revenue","newspaper_digital_revenue"],join:["rd_pct_gdp","state_gdp_per_capita","median_household_income"],sc:{emotional:7,relatability:7,surprise:7,tension:6,visual:8,data_ready:10,originality:7},vs:72,tags:"digital economy GDP share 2017 2023 10.3% value added 7M workers productivity automation technology sector growth"}







,{id:"social_media_use_by_age",title:"Social media use by age 2025 â€” who's online and who's not",sub:"Ages 18-29: 84% use social media. Ages 65+: 46%. The digital participation gap by generation.",type:"CHART",geo:"us_national",fmt:"Bar chart",tbl:"T1194",section:"Information",ext:["FRED: any national economic time series (fred.stlouisfed.org â€” free API)","BLS national data: employment, wages, CPI (bls.gov â€” free API)"],vars:["newspaper_print_revenue"],join:["median_household_income","pct_bachelors"],sc:{emotional:6,relatability:9,surprise:5,tension:3,visual:8,data_ready:10,originality:4},vs:66,tags:"social media use age 2025 18-29 65+ digital divide generation platform Facebook Instagram TikTok YouTube participation"}







,{id:"broadband_adoption_by_income",title:"Home broadband access by income 2024 â€” the digital divide is an income divide",sub:"Households over $100K: 97% have home broadband. Under $25K: 57%. The digital divide in hard numbers.",type:"CHART",geo:"us_national",fmt:"Bar chart",tbl:"T1187",section:"Information",ext:["FRED: any national economic time series (fred.stlouisfed.org â€” free API)","BLS national data: employment, wages, CPI (bls.gov â€” free API)"],vars:["newspaper_print_revenue"],join:["median_household_income","pct_on_snap"],sc:{emotional:8,relatability:8,surprise:6,tension:6,visual:8,data_ready:10,originality:6},vs:74,tags:"broadband internet home access income 2024 97% 57% digital divide inequality low income connectivity work school access"}







,{id:"recorded_music_streaming_vs_physical",title:"Recorded music revenue 2000â€“2024 â€” the death and rebirth",sub:"$14B in 2000. Collapsed to $6.7B by 2015. Back to $14.2B in 2024 â€” all streaming. The format revolution.",type:"CHART",geo:"us_national",fmt:"Area chart",tbl:"T1178",section:"Information",ext:["FRED: any national economic time series (fred.stlouisfed.org â€” free API)","BLS national data: employment, wages, CPI (bls.gov â€” free API)"],vars:["newspaper_print_revenue","newspaper_digital_revenue"],join:[],sc:{emotional:6,relatability:8,surprise:7,tension:4,visual:9,data_ready:10,originality:6},vs:69,tags:"recorded music revenue streaming physical CD download 2000 2024 collapse rebirth Napster Spotify format transition industry"}







,{id:"wireless_vs_landline_subscribers",title:"Wireless vs. landline telephone subscribers 2000â€“2024",sub:"Landlines: 190M in 2000. Under 30M today. Wireless: 350M. The most complete technology replacement ever.",type:"CHART",geo:"us_national",fmt:"Line chart",tbl:"T1184",section:"Information",ext:["FRED: any national economic time series (fred.stlouisfed.org â€” free API)","BLS national data: employment, wages, CPI (bls.gov â€” free API)"],vars:["all_items_cpi"],join:[],sc:{emotional:5,relatability:8,surprise:6,tension:2,visual:8,data_ready:10,originality:5},vs:62,tags:"wireless landline telephone subscribers 2000 2024 replacement technology mobile cell phone 190M 30M history fastest replacement"}







,{id:"public_library_usage_decline",title:"Public library visits per capita 2000â€“2022 â€” the decline nobody talks about",sub:"Library visits per capita: down 42% since 2009. But e-content downloads: up 500%. Libraries are changing, not dying.",type:"CHART",geo:"us_national",fmt:"Line chart",tbl:"T1195",section:"Information",ext:["FRED: any national economic time series (fred.stlouisfed.org â€” free API)","BLS national data: employment, wages, CPI (bls.gov â€” free API)"],vars:["newspaper_print_revenue"],join:["median_household_income","pct_bachelors"],sc:{emotional:6,relatability:7,surprise:8,tension:4,visual:7,data_ready:10,originality:7},vs:67,tags:"public library visits per capita decline 2009 2022 digital ebook download shift transformation changing not dying visits usage"}







,{id:"metro_income_inequality_ranked",title:"Income inequality (Gini) by metro area â€” the most and least equal cities",sub:"New York: Gini 0.50. Salt Lake City: 0.42. The cities where inequality is built into the geography.",type:"RANK",geo:"us_metro",fmt:"Ranked list",tbl:"T726",section:"Income",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by metro (apps.bea.gov â€” free)","BLS LAUS: unemployment + labor force by metro (bls.gov â€” free)"],vars:["metro_per_capita_income"],join:["median_household_income","pct_bachelors"],sc:{emotional:8,relatability:8,surprise:7,tension:7,visual:9,data_ready:9,originality:6},vs:76,tags:"metro income inequality Gini New York Salt Lake City city geography urban economics wealth gap most least equal ranked"}







,{id:"metro_housing_affordability_ranked",title:"Housing affordability index by metro â€” where the math doesn't work",sub:"San Jose: median home is 13x median income. Pittsburgh: 3x. The metro affordability crisis in one ranking.",type:"RANK",geo:"us_metro",fmt:"Ranked list",tbl:"T771 Â· T726",section:"Housing Â· Income",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by metro (apps.bea.gov â€” free)","BLS LAUS: unemployment + labor force by metro (bls.gov â€” free)","HUD Fair Market Rents + housing data by state/county (huduser.gov â€” free)"],vars:["home_price_index_2024","metro_per_capita_income"],join:["housing_permits_total","median_household_income"],sc:{emotional:9,relatability:9,surprise:7,tension:8,visual:9,data_ready:9,originality:6},vs:83,tags:"housing affordability metro San Jose Pittsburgh price to income ratio 13x 3x crisis ranked most least affordable cities"}







,{id:"metro_population_growth_ranked",title:"Fastest and slowest growing metros 2015â€“2024",sub:"Austin +34%. Phoenix +28%. San Francisco -4%. The metro population boom-bust in one ranking.",type:"RANK",geo:"us_metro",fmt:"Ranked list",tbl:"Metropolitan PDF",section:"Population",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by metro (apps.bea.gov â€” free)","BLS LAUS: unemployment + labor force by metro (bls.gov â€” free)"],vars:["population_pct_change","metro_per_capita_income"],join:["housing_permits_total","home_price_index_2024"],sc:{emotional:7,relatability:8,surprise:7,tension:5,visual:9,data_ready:9,originality:5},vs:72,tags:"metro population growth 2015 2024 Austin Phoenix San Francisco boom bust ranked fastest slowest migration suburban urban shift"}







,{id:"metro_wage_growth_vs_rent",title:"Wage growth vs. rent growth by metro 2019â€“2024 â€” who's falling behind",sub:"Nashville: rents up 42%, wages up 28%. Austin: rents up 39%, wages up 31%. Only a few metros broke even.",type:"XREF",geo:"us_metro",fmt:"Scatter plot",tbl:"T726 Â· T770",section:"Income Â· Prices",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by metro (apps.bea.gov â€” free)","BLS LAUS: unemployment + labor force by metro (bls.gov â€” free)","HUD Fair Market Rents + housing data by state/county (huduser.gov â€” free)"],vars:["metro_per_capita_income","rent_primary_residence_cpi"],join:["housing_permits_total","home_price_index_2024"],sc:{emotional:9,relatability:9,surprise:8,tension:8,visual:8,data_ready:9,originality:8},vs:84,tags:"metro wage growth rent growth 2019 2024 Nashville Austin falling behind affordability squeeze workers renters inequality city"}







,{id:"metro_job_concentration_single_employer",title:"Metros most dependent on a single employer or industry",sub:"Detroit and autos. Houston and oil. San Jose and tech. The economic monoculture risk map.",type:"RANK",geo:"us_metro",fmt:"Ranked list",tbl:"T630 Â· T726",section:"Labor Â· Income",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by metro (apps.bea.gov â€” free)","BLS LAUS: unemployment + labor force by metro (bls.gov â€” free)"],vars:["metro_unemployment_rate","metro_per_capita_income"],join:["median_household_income","state_unemployment_rate"],sc:{emotional:7,relatability:7,surprise:8,tension:6,visual:8,data_ready:8,originality:8},vs:72,tags:"metro single employer industry concentration monoculture Detroit autos Houston oil San Jose tech risk vulnerability economic"}







,{id:"accommodation_food_employment",title:"Restaurant and food service employment by state â€” the hidden workforce",sub:"California: 1.8M restaurant workers. Texas: 1.3M. Florida: 1.1M. The most common job in America, mapped.",type:"MAP",geo:"us_state",fmt:"State choropleth",tbl:"T1303",section:"Accommodation Services",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)"],vars:["retail_sales_per_capita","state_unemployment_rate"],join:["median_household_income","pct_on_snap","rep_pct"],sc:{emotional:6,relatability:8,surprise:6,tension:3,visual:9,data_ready:10,originality:5},vs:66,tags:"restaurant food service employment state California Texas Florida workers 1.8M most common job service economy map"}







,{id:"xref_restaurant_density_obesity",title:"Restaurant density vs. obesity rate by county â€” the food environment link",sub:"Counties with the most fast food per capita have obesity rates 8 points higher than counties with the least.",type:"XREF",geo:"us_county",fmt:"Scatter plot",tbl:"T1303 Â· T576",section:"Health Â· Accommodation",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by county (bls.gov â€” free)","CDC WONDER: mortality + disease rates by county/state (wonder.cdc.gov â€” free)","USDA ERS: food environment, rural classification, farm income (ers.usda.gov â€” free)"],vars:["per_capita_health_spending","pct_on_medicaid"],join:["median_household_income","pct_on_snap"],sc:{emotional:8,relatability:8,surprise:7,tension:7,visual:8,data_ready:8,originality:7},vs:76,tags:"restaurant density obesity county food environment fast food link health outcomes poor income nutrition access disease"}







,{id:"nonprofit_sector_by_state",title:"Nonprofit sector employment share by state",sub:"Washington DC: 15% of workers are nonprofit employees. Mississippi: 6%. The charitable economy geography.",type:"MAP",geo:"us_state",fmt:"State choropleth",tbl:"T1305",section:"Business Enterprise",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)"],vars:["corporate_profits","state_gdp_per_capita"],join:["median_household_income","pct_bachelors","rep_pct"],sc:{emotional:5,relatability:5,surprise:7,tension:3,visual:8,data_ready:9,originality:7},vs:63,tags:"nonprofit sector employment state DC Mississippi charitable economy workers share geography hospitals churches universities"}







,{id:"xref_hate_crimes_vote_swing",title:"Hate crime rate vs. vote swing toward Republicans 2016â€“2024",sub:"Counties with the highest hate crime rates had the largest Republican swings. The resentment-violence geography.",type:"XREF",geo:"us_state",fmt:"Scatter plot",tbl:"T348 Â· T454",section:"Law Enforcement Â· Elections",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)","FBI Crime Data Explorer: UCR/NIBRS by state/agency (cde.ucr.cjis.gov â€” free)","MIT Election Lab: presidential/congressional results (electionlab.mit.edu â€” free)"],vars:["violent_crime_rate","rep_pct"],join:["median_household_income","pct_bachelors"],sc:{emotional:9,relatability:7,surprise:8,tension:9,visual:7,data_ready:8,originality:9},vs:81,tags:"hate crimes vote swing Republican 2016 2024 resentment violence geography correlation political radicalization anger bias"}







,{id:"xref_life_expectancy_vote",title:"Life expectancy by state vs. Republican vote share",sub:"The shortest-lived states vote most Republican. The states voting to cut healthcare have the worst health outcomes.",type:"XREF",geo:"us_state",fmt:"Scatter plot",tbl:"T105 Â· T454",section:"Health Â· Elections",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)","CDC WONDER: mortality + disease rates by county/state (wonder.cdc.gov â€” free)","MIT Election Lab: presidential/congressional results (electionlab.mit.edu â€” free)"],vars:["per_capita_health_spending","rep_pct"],join:["pct_on_medicaid","median_household_income","total_medicare"],sc:{emotional:10,relatability:8,surprise:8,tension:10,visual:8,data_ready:9,originality:8},vs:89,tags:"life expectancy Republican vote state paradox shortest lives cut healthcare Mississippi Alabama West Virginia Louisiana vote"}







,{id:"xref_infant_mortality_vote",title:"Infant mortality rate vs. Republican vote share by state",sub:"The states with the highest infant death rates vote most reliably Republican. And most reliably against Medicaid.",type:"XREF",geo:"us_state",fmt:"Scatter plot",tbl:"T115 Â· T454",section:"Health Â· Elections",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)","CDC WONDER: mortality + disease rates by county/state (wonder.cdc.gov â€” free)","MIT Election Lab: presidential/congressional results (electionlab.mit.edu â€” free)"],vars:["birth_rate_state","rep_pct"],join:["pct_on_medicaid","teen_birth_rate","median_household_income"],sc:{emotional:10,relatability:8,surprise:8,tension:10,visual:8,data_ready:10,originality:8},vs:89,tags:"infant mortality Republican vote state paradox babies dying Medicaid cut Mississippi Alabama Arkansas healthcare politics"}







,{id:"income_quintile_share_over_time",title:"Share of income going to top 5% vs. bottom 20% â€” 1970 to 2023",sub:"Top 5% income share: 16.8% in 1970. 23.1% in 2023. Bottom 20%: stuck at 3.4%. The divergence is 50 years old.",type:"CHART",geo:"us_national",fmt:"Line chart",tbl:"T739",section:"Income",ext:["FRED: any national economic time series (fred.stlouisfed.org â€” free API)","BLS national data: employment, wages, CPI (bls.gov â€” free API)"],vars:["median_household_income","pct_over_200k","pct_under_25k"],join:["corporate_profits","pct_families_own_stocks"],sc:{emotional:10,relatability:8,surprise:7,tension:10,visual:9,data_ready:10,originality:6},vs:87,tags:"income inequality top 5% bottom 20% share 1970 2023 50 years divergence rich poor wealth class distribution"}







,{id:"poverty_rate_by_state_2023",title:"Poverty rate by state 2023 â€” the geography of 40 million Americans",sub:"Mississippi: 19.5% in poverty. New Hampshire: 7.2%. 40.8M total Americans below the poverty line.",type:"MAP",geo:"us_state",fmt:"State choropleth",tbl:"T751",section:"Income",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)"],vars:["median_household_income","pct_under_25k"],join:["pct_on_snap","violent_crime_rate","rep_pct"],sc:{emotional:9,relatability:8,surprise:5,tension:8,visual:9,data_ready:10,originality:3},vs:78,tags:"poverty rate state 2023 Mississippi New Hampshire 40 million geography income inequality poor gap"}







,{id:"child_poverty_race_history",title:"Child poverty rate by race 1990â€“2023 â€” the gap that barely closed",sub:"Black child poverty: 44% in 1990. 22% in 2023. White: 15% to 9%. Progress, but still a 2.4x gap.",type:"CHART",geo:"us_national",fmt:"Line chart",tbl:"T754",section:"Income",ext:["FRED: any national economic time series (fred.stlouisfed.org â€” free API)","BLS national data: employment, wages, CPI (bls.gov â€” free API)"],vars:["pct_under_25k","median_household_income"],join:["pct_on_snap","pct_on_medicaid","teen_birth_rate"],sc:{emotional:9,relatability:8,surprise:7,tension:9,visual:8,data_ready:10,originality:6},vs:83,tags:"child poverty race Black White 1990 2023 gap progress 44% 22% historical inequality income progress systemic"}







,{id:"income_by_race_national",title:"Median household income by race and Hispanic origin 2023",sub:"Asian: $108K. White non-Hispanic: $81K. Hispanic: $62K. Black: $52K. The racial income hierarchy in one chart.",type:"CHART",geo:"us_national",fmt:"Bar chart",tbl:"T736",section:"Income",ext:["FRED: any national economic time series (fred.stlouisfed.org â€” free API)","BLS national data: employment, wages, CPI (bls.gov â€” free API)"],vars:["median_household_income","pct_under_25k","pct_over_200k"],join:["pct_on_snap","pct_on_medicaid","violent_crime_rate"],sc:{emotional:9,relatability:8,surprise:5,tension:8,visual:9,data_ready:10,originality:3},vs:79,tags:"median income race Asian White Hispanic Black $108K $81K $62K $52K hierarchy inequality 2023 gap systematic"}







,{id:"spending_by_income_quintile",title:"How different income groups spend their money â€” 2023",sub:"Bottom quintile: 75% on housing + food. Top quintile: 29% on housing + food. The spending squeeze mapped.",type:"CHART",geo:"us_national",fmt:"Bar chart",tbl:"T732",section:"Income",ext:["FRED: any national economic time series (fred.stlouisfed.org â€” free API)","BLS national data: employment, wages, CPI (bls.gov â€” free API)"],vars:["median_household_income","pct_under_25k"],join:["food_at_home_cpi","housing_cpi","motor_vehicle_insurance_cpi"],sc:{emotional:9,relatability:9,surprise:7,tension:7,visual:9,data_ready:10,originality:7},vs:83,tags:"spending income quintile housing food 75% 29% squeeze bottom top class different priorities CES budget allocation"}







,{id:"working_poor_by_state",title:"Working poor â€” people employed full time but still below poverty",sub:"3.5M full-time workers live below the poverty line. Single mothers: 13.6% work full-time and remain poor.",type:"CHART",geo:"us_national",fmt:"Bar chart",tbl:"T756",section:"Income",ext:["FRED: any national economic time series (fred.stlouisfed.org â€” free API)","BLS national data: employment, wages, CPI (bls.gov â€” free API)"],vars:["pct_under_25k","median_household_income"],join:["pct_on_snap","state_unemployment_rate","female_lfp_rate"],sc:{emotional:9,relatability:8,surprise:8,tension:9,visual:8,data_ready:10,originality:7},vs:83,tags:"working poor full time below poverty 3.5M single mothers 13.6% employment poverty wages minimum wage gap"}







,{id:"uninsured_rate_by_state",title:"Uninsured rate by state 2023 â€” who doesn't have health coverage",sub:"Texas: 16.6% uninsured. Massachusetts: 2.5%. The 7x coverage gap within the same country.",type:"MAP",geo:"us_state",fmt:"State choropleth",tbl:"T161",section:"Health",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)","CDC WONDER: mortality + disease rates by county/state (wonder.cdc.gov â€” free)"],vars:["per_capita_health_spending","pct_on_medicaid"],join:["rep_pct","median_household_income","total_medicare"],sc:{emotional:9,relatability:9,surprise:6,tension:9,visual:9,data_ready:10,originality:4},vs:82,tags:"uninsured rate state 2023 Texas 16.6% Massachusetts 2.5% 7x gap healthcare coverage ACA Medicaid expansion"}







,{id:"medical_debt_by_race",title:"Medical debt: who carries it and how much â€” 2023",sub:"Black households: 24.3% have medical debt. White: 15.6%. Asian: 8%. The medical debt divide is a racial divide.",type:"CHART",geo:"us_national",fmt:"Bar chart",tbl:"T191",section:"Health",ext:["FRED: any national economic time series (fred.stlouisfed.org â€” free API)","BLS national data: employment, wages, CPI (bls.gov â€” free API)"],vars:["per_capita_health_spending","health_insurance_cpi"],join:["pct_on_medicaid","median_household_income","pct_on_snap"],sc:{emotional:9,relatability:9,surprise:7,tension:8,visual:8,data_ready:10,originality:8},vs:84,tags:"medical debt race Black White Asian 24.3% 15.6% 8% racial divide healthcare financial burden hospital bills"}







,{id:"medicare_pct_gdp_projections",title:"Medicare as % of GDP 1980â€“2045 â€” the fiscal trajectory",sub:"Medicare was 1.3% of GDP in 1980. 3.8% today. Projected 6.7% by 2045. The math that keeps actuaries up at night.",type:"CHART",geo:"us_national",fmt:"Area chart",tbl:"T160",section:"Health",ext:["FRED: any national economic time series (fred.stlouisfed.org â€” free API)","BLS national data: employment, wages, CPI (bls.gov â€” free API)"],vars:["total_medicare","per_capita_health_spending"],join:["federal_debt_pct_gdp","federal_outlays_by_function"],sc:{emotional:8,relatability:7,surprise:8,tension:9,visual:8,data_ready:10,originality:7},vs:79,tags:"Medicare GDP 1980 2045 projection fiscal actuarial crisis aging spending trajectory 1.3% 3.8% 6.7%"}







,{id:"xref_uninsured_vote",title:"Uninsured rate vs. Republican vote share by state",sub:"States that voted most against the ACA have the highest uninsured rates. 10 of the 11 highest-uninsured states voted Republican.",type:"XREF",geo:"us_state",fmt:"Scatter plot",tbl:"T161 Â· T454",section:"Health Â· Elections",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)","CDC WONDER: mortality + disease rates by county/state (wonder.cdc.gov â€” free)","MIT Election Lab: presidential/congressional results (electionlab.mit.edu â€” free)"],vars:["per_capita_health_spending","rep_pct"],join:["pct_on_medicaid","median_household_income"],sc:{emotional:10,relatability:8,surprise:7,tension:10,visual:8,data_ready:10,originality:7},vs:88,tags:"uninsured Republican vote ACA Obamacare healthcare state paradox 10 of 11 Texas Mississippi coverage gap politics"}







,{id:"cancer_rates_by_race",title:"Cancer incidence rates by race and type 2018â€“2022",sub:"Prostate cancer in Black men: 194 per 100K. In Asian men: 64. The 3x racial gap in cancer risk.",type:"CHART",geo:"us_national",fmt:"Bar chart",tbl:"T193",section:"Health",ext:["FRED: any national economic time series (fred.stlouisfed.org â€” free API)","BLS national data: employment, wages, CPI (bls.gov â€” free API)"],vars:["per_capita_health_spending"],join:["pct_on_medicaid","median_household_income"],sc:{emotional:8,relatability:7,surprise:7,tension:7,visual:8,data_ready:10,originality:6},vs:73,tags:"cancer rates race Black Asian White prostate breast lung colon 3x racial gap incidence systematic disparity SEER"}







,{id:"co2_emissions_per_capita_state",title:"Energy-related CO2 emissions per capita by state 2022",sub:"Alaska: 56 metric tons per person. DC: 3.9. Wyoming: 88. The carbon inequality within America.",type:"MAP",geo:"us_state",fmt:"State choropleth",tbl:"T977",section:"Geography & Environment",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)","EIA State Energy Data System: production + consumption by state (eia.gov â€” free API)"],vars:["energy_consumption_per_capita","coal_production_index"],join:["renewable_energy_share","rep_pct","median_household_income"],sc:{emotional:8,relatability:7,surprise:8,tension:8,visual:9,data_ready:10,originality:7},vs:79,tags:"CO2 emissions per capita state 2022 Alaska Wyoming DC carbon inequality climate geography fossil fuels energy"}







,{id:"greenhouse_gas_by_source_trend",title:"US greenhouse gas emissions by source 1990â€“2022",sub:"Total emissions down 3% from 1990 â€” but transportation emissions rose 16%. The uneven decarbonization.",type:"CHART",geo:"us_national",fmt:"Area chart",tbl:"T420",section:"Geography & Environment",ext:["FRED: any national economic time series (fred.stlouisfed.org â€” free API)","BLS national data: employment, wages, CPI (bls.gov â€” free API)","EIA State Energy Data System: production + consumption by state (eia.gov â€” free API)"],vars:["energy_consumption_per_capita","coal_production_index"],join:["renewable_energy_share"],sc:{emotional:7,relatability:7,surprise:7,tension:7,visual:8,data_ready:10,originality:6},vs:72,tags:"greenhouse gas emissions source 1990 2022 transportation energy agriculture waste uneven decarbonization progress"}







,{id:"wildfire_acres_burned_trend",title:"Wildfire acres burned 1970â€“2024 â€” the catastrophic acceleration",sub:"2015, 2017, 2020: each over 10 million acres. 2024: 8.9M acres. The new normal is not normal.",type:"CHART",geo:"us_national",fmt:"Area chart",tbl:"T440",section:"Geography & Environment",ext:["FRED: any national economic time series (fred.stlouisfed.org â€” free API)","BLS national data: employment, wages, CPI (bls.gov â€” free API)"],vars:["mean_elevation","national_forest_acres"],join:["energy_consumption_per_capita","housing_permits_total"],sc:{emotional:8,relatability:8,surprise:7,tension:8,visual:9,data_ready:10,originality:5},vs:77,tags:"wildfire acres 1970 2024 acceleration climate catastrophic new normal 10 million Western states Oregon Texas California"}







,{id:"toxic_releases_by_state",title:"Toxic chemical releases by state 2023 â€” the pollution burden map",sub:"Nevada: highest toxic releases due to mining. Louisiana: chemical refining. Alaska. The pollution geography.",type:"MAP",geo:"us_state",fmt:"State choropleth",tbl:"T427",section:"Geography & Environment",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)"],vars:["mean_elevation","pct_forest","national_forest_acres"],join:["median_household_income","pct_on_snap","rep_pct"],sc:{emotional:8,relatability:7,surprise:7,tension:7,visual:9,data_ready:10,originality:7},vs:75,tags:"toxic chemical releases state 2023 Nevada Louisiana Alaska mining refining pollution burden environmental justice map"}







,{id:"air_quality_unhealthy_days_metro",title:"Unhealthy air quality days by metro 2023",sub:"Bakersfield CA: 70 unhealthy days. San Francisco: 25. Detroit: 7. Salt Lake City: 33. The air you breathe by city.",type:"RANK",geo:"top_n_list",fmt:"Ranked list",tbl:"T422",section:"Geography & Environment",ext:[],vars:["mean_elevation"],join:["energy_consumption_per_capita","median_household_income"],sc:{emotional:7,relatability:8,surprise:7,tension:6,visual:9,data_ready:10,originality:7},vs:73,tags:"air quality unhealthy days metro AQI 2023 Bakersfield San Francisco Detroit Salt Lake City breathing pollution"}







,{id:"severe_weather_losses_trend",title:"Billion-dollar weather disaster losses 2000â€“2024",sub:"Hurricane property losses alone hit $15B in 2022. Total severe weather losses in 2024: $13B+ from floods alone. The rising toll.",type:"CHART",geo:"us_national",fmt:"Bar chart",tbl:"T438",section:"Geography & Environment",ext:["FRED: any national economic time series (fred.stlouisfed.org â€” free API)","BLS national data: employment, wages, CPI (bls.gov â€” free API)"],vars:["mean_elevation","coastline_miles"],join:["housing_permits_total","home_price_index_2024"],sc:{emotional:8,relatability:8,surprise:7,tension:7,visual:8,data_ready:10,originality:5},vs:74,tags:"severe weather disaster losses 2000 2024 billion dollar hurricanes floods tornadoes climate rising toll insurance"}







,{id:"homeownership_rate_by_race",title:"Homeownership rate by race 2000â€“2024 â€” the wealth gap you can measure",sub:"White homeownership: 74.3%. Black: 45.7%. A 28.6 point gap that has barely changed in 60 years.",type:"CHART",geo:"us_national",fmt:"Line chart",tbl:"T1039",section:"Housing",ext:["FRED: any national economic time series (fred.stlouisfed.org â€” free API)","BLS national data: employment, wages, CPI (bls.gov â€” free API)"],vars:["home_price_index_2024","housing_permits_total"],join:["median_household_income","pct_on_snap","mortgage_delinquency_rate"],sc:{emotional:9,relatability:8,surprise:7,tension:9,visual:8,data_ready:10,originality:5},vs:81,tags:"homeownership race Black White 74.3% 45.7% 28.6 gap 60 years wealth building inequality housing discrimination"}







,{id:"homeownership_rate_by_state",title:"Homeownership rate by state 2024",sub:"West Virginia: 78%. California: 55%. New York: 53%. The most and least owner-occupied states in America.",type:"MAP",geo:"us_state",fmt:"State choropleth",tbl:"T1041",section:"Housing",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)","HUD Fair Market Rents + housing data by state/county (huduser.gov â€” free)"],vars:["home_price_index_2024","housing_permits_total"],join:["median_household_income","mortgage_delinquency_rate","rep_pct"],sc:{emotional:7,relatability:8,surprise:6,tension:5,visual:9,data_ready:10,originality:4},vs:71,tags:"homeownership rate state 2024 West Virginia 78% California 55% New York 53% owner occupied geography housing"}







,{id:"median_home_value_by_state",title:"Median owner-occupied home value by state 2023",sub:"Hawaii: $846K median value. West Virginia: $138K. The 6x home value gap â€” and monthly costs follow.",type:"MAP",geo:"us_state",fmt:"State choropleth",tbl:"T1044",section:"Housing",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)","HUD Fair Market Rents + housing data by state/county (huduser.gov â€” free)"],vars:["home_price_index_2024"],join:["median_household_income","housing_permits_total","mortgage_delinquency_rate"],sc:{emotional:7,relatability:8,surprise:6,tension:5,visual:9,data_ready:10,originality:3},vs:70,tags:"median home value state 2023 Hawaii $846K West Virginia $138K 6x gap housing wealth inequality geography"}







,{id:"energy_insecurity_by_income",title:"Household energy insecurity â€” who can't afford to heat or cool their home",sub:"27.2% of all US households experienced energy insecurity in 2020. The South: 30%. Low-income households: 40%+.",type:"CHART",geo:"us_national",fmt:"Bar chart",tbl:"T1052",section:"Housing",ext:["FRED: any national economic time series (fred.stlouisfed.org â€” free API)","BLS national data: employment, wages, CPI (bls.gov â€” free API)"],vars:["housing_permits_total"],join:["energy_consumption_per_capita","pct_on_snap","median_household_income"],sc:{emotional:9,relatability:8,surprise:8,tension:7,visual:7,data_ready:10,originality:8},vs:79,tags:"energy insecurity heat cool home 27.2% South 30% low income 40% household poverty utility bills electricity gas"}







,{id:"xref_homeownership_wealth",title:"Homeownership rate vs. median net worth by demographic group",sub:"Homeowner net worth: $396K median. Renter net worth: $10K. The 40x wealth gap that homeownership creates.",type:"CHART",geo:"us_national",fmt:"Bar chart",tbl:"T1039 Â· T1207",section:"Housing Â· Banking",ext:["FRED: any national economic time series (fred.stlouisfed.org â€” free API)","BLS national data: employment, wages, CPI (bls.gov â€” free API)"],vars:["home_price_index_2024","pct_families_own_any_asset"],join:["median_household_income","pct_on_snap","mortgage_delinquency_rate"],sc:{emotional:9,relatability:9,surprise:8,tension:8,visual:8,data_ready:9,originality:7},vs:84,tags:"homeownership wealth $396K $10K 40x net worth renter owner wealth building inequality race income housing equity"}







,{id:"solar_generation_by_state",title:"Solar energy generation by state 2023 â€” who's actually doing it",sub:"California: 68.8B kWh. Texas: 50.7B. Florida: 17.8B. And West Virginia: 37M kWh. The solar geography.",type:"MAP",geo:"us_state",fmt:"State choropleth",tbl:"T991",section:"Energy",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)","EIA State Energy Data System: production + consumption by state (eia.gov â€” free API)"],vars:["renewable_energy_share","coal_production_index"],join:["rep_pct","energy_consumption_per_capita","median_household_income"],sc:{emotional:7,relatability:8,surprise:7,tension:6,visual:9,data_ready:10,originality:6},vs:74,tags:"solar generation state 2023 California Texas Florida West Virginia geography energy transition per capita map"}







,{id:"renewable_capacity_projections_2050",title:"Renewable energy capacity projections 2024â€“2050 â€” the coming transformation",sub:"Solar capacity to grow 7.6x by 2050. Offshore wind: from 0.2 GW to 46 GW. The energy transition is now inevitable.",type:"CHART",geo:"us_national",fmt:"Area chart",tbl:"T990",section:"Energy",ext:["FRED: any national economic time series (fred.stlouisfed.org â€” free API)","EIA State Energy Data System: production + consumption by state (eia.gov â€” free API)"],vars:["renewable_energy_share","coal_production_index"],join:["energy_consumption_per_capita","rd_pct_gdp"],sc:{emotional:7,relatability:7,surprise:8,tension:5,visual:9,data_ready:10,originality:7},vs:74,tags:"renewable energy capacity projections 2024 2050 solar 7.6x offshore wind EIA transformation inevitability future"}







,{id:"coal_capacity_collapse",title:"Coal power plant capacity 2000â€“2023 â€” the fastest industrial retirement in history",sub:"Coal electric capacity: 315 GW in 2000. 178 GW in 2023. A 44% collapse in 23 years. Natural gas and renewables won.",type:"CHART",geo:"us_national",fmt:"Area chart",tbl:"T994",section:"Energy",ext:["FRED: any national economic time series (fred.stlouisfed.org â€” free API)","EIA State Energy Data System: production + consumption by state (eia.gov â€” free API)"],vars:["coal_production_index","renewable_energy_share"],join:["energy_consumption_per_capita","rep_pct"],sc:{emotional:7,relatability:7,surprise:8,tension:7,visual:8,data_ready:10,originality:7},vs:74,tags:"coal power plant capacity 2000 2023 collapse 44% fastest industrial retirement natural gas renewables won energy"}







,{id:"electricity_price_by_state",title:"Average residential electricity price by state 2023",sub:"Hawaii: 37 cents/kWh. Louisiana: 10 cents. The 3.7x electricity price gap within one grid.",type:"MAP",geo:"us_state",fmt:"State choropleth",tbl:"T999",section:"Energy",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)","EIA State Energy Data System: production + consumption by state (eia.gov â€” free API)"],vars:["energy_consumption_per_capita","renewable_energy_share"],join:["median_household_income","coal_production_index","rep_pct"],sc:{emotional:7,relatability:8,surprise:7,tension:5,visual:9,data_ready:10,originality:5},vs:72,tags:"electricity price residential state 2023 Hawaii 37 cents Louisiana 10 cents 3.7x gap grid cost energy utility"}







,{id:"xref_co2_per_capita_vs_income",title:"CO2 emissions per capita vs. median income by state",sub:"The most polluting states per capita are often the poorest. Wyoming emits 88 tons per person, income $70K.",type:"XREF",geo:"us_state",fmt:"Scatter plot",tbl:"T977 Â· T727",section:"Energy Â· Income",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)","EIA State Energy Data System: production + consumption by state (eia.gov â€” free API)"],vars:["energy_consumption_per_capita","median_household_income"],join:["coal_production_index","renewable_energy_share","rep_pct"],sc:{emotional:7,relatability:6,surprise:8,tension:6,visual:7,data_ready:10,originality:7},vs:71,tags:"CO2 per capita income state Wyoming 88 tons $70K pollution poverty industrial extraction energy inequality geography"}







,{id:"fastest_growing_occupations_2033",title:"Fastest growing jobs 2023â€“2033 â€” the BLS projection",sub:"Wind turbine technician: +60%. Solar installer: +48%. Nurse practitioner: +46%. The economy being built.",type:"RANK",geo:"top_n_list",fmt:"Ranked list",tbl:"T655",section:"Labor Force",ext:[],vars:["state_unemployment_rate","female_lfp_rate"],join:["rd_pct_gdp","pct_bachelors"],sc:{emotional:7,relatability:8,surprise:8,tension:4,visual:9,data_ready:10,originality:6},vs:74,tags:"fastest growing jobs 2023 2033 BLS wind turbine solar nurse practitioner data scientist future economy occupation"}







,{id:"job_growth_by_industry_2033",title:"Largest absolute job growth by industry 2023â€“2033",sub:"Elder care services: +614K jobs. Computer systems design: +488K. Home health: +325K. Aging America, building its workforce.",type:"RANK",geo:"top_n_list",fmt:"Ranked list",tbl:"T656",section:"Labor Force",ext:[],vars:["state_unemployment_rate"],join:["pct_on_medicaid","total_medicare","rd_pct_gdp"],sc:{emotional:7,relatability:7,surprise:7,tension:4,visual:9,data_ready:10,originality:6},vs:70,tags:"job growth industry 2023 2033 elder care 614K computer systems 488K home health aging workforce future BLS sector"}







,{id:"self_employed_by_industry",title:"Self-employed workers by industry 2000â€“2024",sub:"9.9M self-employed Americans. Construction: 1.6M. Agriculture: 661K. Gig transport doubled since 2015. The new workforce.",type:"CHART",geo:"us_national",fmt:"Area chart",tbl:"T642",section:"Labor Force",ext:["FRED: any national economic time series (fred.stlouisfed.org â€” free API)","BLS national data: employment, wages, CPI (bls.gov â€” free API)"],vars:["state_unemployment_rate","female_lfp_rate"],join:["ecommerce_sales","retail_sales_per_capita"],sc:{emotional:6,relatability:8,surprise:6,tension:3,visual:7,data_ready:10,originality:5},vs:65,tags:"self employed workers industry 2000 2024 construction agriculture gig transport 9.9M workforce independent contractor"}







,{id:"multiple_jobholders_by_reason",title:"Americans working multiple jobs 2024 â€” who and why",sub:"8.3M Americans hold multiple jobs. 68% do it to pay bills. Only 13% do it because they want variety.",type:"CHART",geo:"us_national",fmt:"Bar chart",tbl:"T643",section:"Labor Force",ext:["FRED: any national economic time series (fred.stlouisfed.org â€” free API)","BLS national data: employment, wages, CPI (bls.gov â€” free API)"],vars:["state_unemployment_rate","female_lfp_rate"],join:["median_household_income","pct_on_snap"],sc:{emotional:8,relatability:9,surprise:6,tension:6,visual:7,data_ready:10,originality:6},vs:74,tags:"multiple jobs workers 2024 8.3M 68% pay bills 13% variety gig economy second job hustle necessity income survival"}







,{id:"unemployment_by_education_race",title:"Unemployment rate by education and race 2024 â€” the degree still doesn't close the gap",sub:"Black workers with bachelor's degrees: 3.5% unemployment. White workers with bachelor's: 2.1%. The degree doesn't erase race.",type:"CHART",geo:"us_national",fmt:"Bar chart",tbl:"T664",section:"Labor Force",ext:["FRED: any national economic time series (fred.stlouisfed.org â€” free API)","BLS national data: employment, wages, CPI (bls.gov â€” free API)"],vars:["state_unemployment_rate","female_lfp_rate"],join:["pct_bachelors","median_household_income"],sc:{emotional:9,relatability:8,surprise:8,tension:9,visual:8,data_ready:10,originality:7},vs:83,tags:"unemployment rate education race Black White college degree 3.5% 2.1% racial gap not closed degree labor market"}







,{id:"volunteering_rate_by_state",title:"Volunteering rate by state 2023 â€” America's informal social fabric",sub:"Montana: 37.2% volunteer. Connecticut: 37.4%. Nevada: 18.6%. The civic engagement geography.",type:"MAP",geo:"us_state",fmt:"State choropleth",tbl:"T617",section:"Social Insurance",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)"],vars:["total_transfers_per_capita","pct_on_snap"],join:["median_household_income","pct_bachelors","rep_pct"],sc:{emotional:5,relatability:6,surprise:7,tension:2,visual:9,data_ready:10,originality:7},vs:65,tags:"volunteering rate state 2023 Montana 37% Connecticut Nevada 18% civic engagement geography social fabric AmeriCorps"}







,{id:"homeless_population_trend",title:"Homeless population 2010â€“2024 â€” the crisis that grew despite the economy",sub:"Homeless Americans: 647K in 2010. 771K in 2024. Up 19% in 14 years despite economic growth. The housing failure.",type:"CHART",geo:"us_national",fmt:"Area chart",tbl:"T613",section:"Social Insurance",ext:["FRED: any national economic time series (fred.stlouisfed.org â€” free API)","BLS national data: employment, wages, CPI (bls.gov â€” free API)"],vars:["total_transfers_per_capita","pct_on_snap"],join:["home_price_index_2024","housing_permits_total","median_household_income"],sc:{emotional:9,relatability:8,surprise:8,tension:8,visual:8,data_ready:10,originality:6},vs:82,tags:"homeless population 2010 2024 647K 771K 19% increase economic growth housing failure point in time count HUD"}







,{id:"social_security_beneficiaries_by_type",title:"Social Security beneficiaries by type 1990â€“2024",sub:"Total: 72.5M beneficiaries in 2024. $1.46T paid. Disability insurance recipients grew 85% since 1990.",type:"CHART",geo:"us_national",fmt:"Area chart",tbl:"T579",section:"Social Insurance",ext:["FRED: any national economic time series (fred.stlouisfed.org â€” free API)","BLS national data: employment, wages, CPI (bls.gov â€” free API)"],vars:["total_transfers_per_capita","pct_on_medicaid"],join:["federal_debt_pct_gdp","federal_outlays_by_function"],sc:{emotional:7,relatability:7,surprise:6,tension:7,visual:7,data_ready:10,originality:4},vs:68,tags:"Social Security beneficiaries 72.5M $1.46T disability 85% growth 1990 2024 aging population retirement OASDI"}







,{id:"pension_coverage_by_worker_type",title:"Pension and retirement plan access by worker characteristics",sub:"Private sector workers with pension access: 53%. Part-time workers: 26%. Low-wage workers: 23%. The coverage gap.",type:"CHART",geo:"us_national",fmt:"Bar chart",tbl:"T582",section:"Social Insurance",ext:["FRED: any national economic time series (fred.stlouisfed.org â€” free API)","BLS national data: employment, wages, CPI (bls.gov â€” free API)"],vars:["pct_families_own_retirement","total_transfers_per_capita"],join:["median_household_income","state_unemployment_rate"],sc:{emotional:8,relatability:8,surprise:6,tension:7,visual:7,data_ready:10,originality:6},vs:74,tags:"pension retirement plan access worker 53% part time 26% low wage 23% coverage gap private sector benefits inequality"}







,{id:"tanf_recipients_by_state",title:"TANF (welfare) recipients per 1,000 poor families by state",sub:"California: 80 TANF recipients per 100 poor families. Mississippi: 5. The welfare access collapse, mapped.",type:"MAP",geo:"us_state",fmt:"State choropleth",tbl:"T598",section:"Social Insurance",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)"],vars:["pct_on_snap","total_transfers_per_capita"],join:["median_household_income","rep_pct","pct_under_25k"],sc:{emotional:9,relatability:7,surprise:9,tension:8,visual:9,data_ready:10,originality:9},vs:83,tags:"TANF welfare recipients state California 80 Mississippi 5 welfare reform collapse access poor families gap state policy"}







,{id:"naep_scores_by_race_state",title:"8th grade reading proficiency by state and race â€” the education gap inside states",sub:"Massachusetts white 8th graders: 46% proficient. Mississippi Black 8th graders: 11%. The gap is 4x within one country.",type:"MAP",geo:"us_state",fmt:"State choropleth",tbl:"T282",section:"Education",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)"],vars:["pct_bachelors","expenditure_per_pupil"],join:["median_household_income","rep_pct","avg_teacher_salary"],sc:{emotional:9,relatability:8,surprise:7,tension:9,visual:9,data_ready:10,originality:6},vs:83,tags:"NAEP 8th grade reading proficiency state race Massachusetts 46% Mississippi 11% 4x gap education achievement racial"}







,{id:"charter_school_enrollment_by_state",title:"Charter school enrollment share by state 2022",sub:"Arizona: 20% of students in charters. DC: 47%. Wyoming: near zero. The charter school geography.",type:"MAP",geo:"us_state",fmt:"State choropleth",tbl:"T281",section:"Education",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)"],vars:["pct_bachelors","expenditure_per_pupil"],join:["pct_bachelors","median_household_income","rep_pct"],sc:{emotional:6,relatability:7,surprise:7,tension:5,visual:9,data_ready:10,originality:6},vs:69,tags:"charter school enrollment state 2022 Arizona 20% DC 47% Wyoming zero geography school choice policy education map"}







,{id:"high_school_dropout_rate_by_race",title:"High school dropout rate by race 2000â€“2022 â€” the persistence of the gap",sub:"Hispanic dropout rate: 16.9% in 2000. 7.1% in 2022. Progress â€” but still 3x the white rate.",type:"CHART",geo:"us_national",fmt:"Line chart",tbl:"T287",section:"Education",ext:["FRED: any national economic time series (fred.stlouisfed.org â€” free API)","BLS national data: employment, wages, CPI (bls.gov â€” free API)"],vars:["pct_bachelors","pct_hs_grad"],join:["teen_birth_rate","state_unemployment_rate","median_household_income"],sc:{emotional:8,relatability:7,surprise:6,tension:7,visual:7,data_ready:10,originality:5},vs:73,tags:"high school dropout rate race Hispanic 16.9% 7.1% 2000 2022 progress 3x white rate gap education completion"}







,{id:"gender_gap_college_enrollment",title:"College enrollment by sex 1970â€“2022 â€” the great reversal",sub:"Women: 57% of college students in 2022. In 1970: 40%. Men have been the minority on campus for 20 years.",type:"CHART",geo:"us_national",fmt:"Line chart",tbl:"T294",section:"Education",ext:["FRED: any national economic time series (fred.stlouisfed.org â€” free API)","BLS national data: employment, wages, CPI (bls.gov â€” free API)"],vars:["pct_bachelors"],join:["female_lfp_rate","teen_birth_rate","median_household_income"],sc:{emotional:7,relatability:8,surprise:7,tension:5,visual:8,data_ready:10,originality:5},vs:72,tags:"college enrollment gender women 57% men 1970 2022 reversal campus minority higher education degree sex gap"}







,{id:"foreign_students_stem_visas",title:"Foreign temporary visa holders awarded STEM doctorates 2023",sub:"64% of US computer science PhD graduates are foreign-born. 57% of engineering PhDs. America trains the world's scientists â€” and most go home.",type:"CHART",geo:"us_national",fmt:"Bar chart",tbl:"T848",section:"Science",ext:["FRED: any national economic time series (fred.stlouisfed.org â€” free API)","BLS national data: employment, wages, CPI (bls.gov â€” free API)"],vars:["rd_pct_gdp"],join:["pct_bachelors","state_gdp_per_capita"],sc:{emotional:8,relatability:6,surprise:9,tension:7,visual:7,data_ready:10,originality:8},vs:77,tags:"foreign students STEM doctorates visa 64% computer science 57% engineering PhD immigration brain drain America trains"}







,{id:"stem_metro_concentration",title:"Top 25 metros by STEM workers as % of employment",sub:"San Jose: 26% STEM. Seattle: 17%. Washington DC: 15%. The knowledge economy is hyper-concentrated.",type:"RANK",geo:"top_n_list",fmt:"Ranked list",tbl:"T858",section:"Science",ext:[],vars:["rd_pct_gdp"],join:["median_household_income","pct_bachelors","state_gdp_per_capita"],sc:{emotional:6,relatability:6,surprise:7,tension:4,visual:9,data_ready:10,originality:6},vs:67,tags:"STEM workers metro concentration San Jose 26% Seattle DC knowledge economy hyper concentrated cities tech science"}







,{id:"cpi_food_breakdown_2024",title:"Food CPI breakdown by subcategory 2000-2024 â€” every grocery aisle inflated differently",sub:"Fats and oils: up 380%. Cereals: up 215%. Eggs: up 270%. Fresh fruits: up 140%. The grocery inflation mosaic.",type:"CHART",geo:"us_national",fmt:"Bar chart",tbl:"T770",section:"Prices",ext:["FRED: any national economic time series (fred.stlouisfed.org â€” free API)","BLS national data: employment, wages, CPI (bls.gov â€” free API)"],vars:["food_at_home_cpi","eggs_cpi","beef_and_veal_cpi","dairy_cpi","cereals_bakery_cpi"],join:["all_items_cpi","pct_on_snap"],sc:{emotional:8,relatability:10,surprise:8,tension:5,visual:9,data_ready:10,originality:7},vs:80,tags:"food CPI subcategory 2000 2024 fats oils eggs cereals fruits grocery aisle inflation mosaic breakdown shopping"}







,{id:"housing_costs_renter_vs_owner",title:"Monthly housing cost burden â€” renters vs. owners by income 2023",sub:"Renters in the bottom quintile spend 54% of income on housing. Owners in the same bracket: 38%. Renting costs more.",type:"CHART",geo:"us_national",fmt:"Bar chart",tbl:"T1045",section:"Prices",ext:["FRED: any national economic time series (fred.stlouisfed.org â€” free API)","BLS national data: employment, wages, CPI (bls.gov â€” free API)"],vars:["rent_primary_residence_cpi","housing_cpi"],join:["home_price_index_2024","median_household_income","pct_on_snap"],sc:{emotional:9,relatability:9,surprise:7,tension:8,visual:8,data_ready:10,originality:7},vs:83,tags:"housing cost renter owner income bottom quintile 54% 38% burden tenure affordability cost-burdened housing crisis"}







,{id:"medical_care_cpi_components",title:"Medical care CPI: what's driving healthcare inflation 2000-2024",sub:"Nursing home care: up 210%. Hospital services: up 190%. Physician services: up 110%. The cost driver breakdown.",type:"CHART",geo:"us_national",fmt:"Line chart",tbl:"T770",section:"Prices",ext:["FRED: any national economic time series (fred.stlouisfed.org â€” free API)","BLS national data: employment, wages, CPI (bls.gov â€” free API)"],vars:["hospital_services_cpi","physicians_services_cpi","nursing_homes_cpi","prescription_drugs_cpi","health_insurance_cpi"],join:["per_capita_health_spending","total_medicare"],sc:{emotional:8,relatability:8,surprise:7,tension:7,visual:8,data_ready:10,originality:7},vs:77,tags:"medical care CPI nursing home hospital physician prescription drug health insurance driver inflation 2000 2024"}







,{id:"construction_materials_ppi",title:"Construction materials PPI 2010-2024 â€” the cost of building America",sub:"Lumber PPI doubled between 2019 and 2021. Steel: up 80%. The materials inflation that stopped housing supply.",type:"CHART",geo:"us_national",fmt:"Line chart",tbl:"T1017",section:"Prices",ext:["FRED: any national economic time series (fred.stlouisfed.org â€” free API)","BLS national data: employment, wages, CPI (bls.gov â€” free API)"],vars:["home_price_index_2024","housing_permits_total"],join:["all_items_cpi","manufacturing_employment_trend"],sc:{emotional:7,relatability:7,surprise:8,tension:6,visual:7,data_ready:10,originality:7},vs:72,tags:"construction materials PPI lumber steel 2019 2021 doubled housing supply inflation producer price index building"}







,{id:"household_production_value",title:"The unpaid economy: household production value 1965-2020",sub:"Unpaid household work â€” cooking, childcare, home repair â€” is worth $3.8T annually. It never shows up in GDP.",type:"CHART",geo:"us_national",fmt:"Area chart",tbl:"T717",section:"Income",ext:["FRED: any national economic time series (fred.stlouisfed.org â€” free API)","BLS national data: employment, wages, CPI (bls.gov â€” free API)"],vars:["median_household_income","disposable_income_per_capita"],join:["female_lfp_rate","daycare_preschool_cpi"],sc:{emotional:8,relatability:8,surprise:9,tension:4,visual:7,data_ready:10,originality:9},vs:76,tags:"unpaid household production value $3.8T cooking childcare home repair GDP invisible economy women labor 1965 2020"}







,{id:"personal_consumption_by_function",title:"Where Americans spend their money by function 2023",sub:"Housing + utilities: $4.1T. Healthcare: $3.2T. Food: $2.8T. Transportation: $1.9T. The personal consumption breakdown.",type:"CHART",geo:"us_national",fmt:"Treemap",tbl:"T720",section:"Income",ext:["FRED: any national economic time series (fred.stlouisfed.org â€” free API)","BLS national data: employment, wages, CPI (bls.gov â€” free API)"],vars:["disposable_income_per_capita","median_household_income"],join:["housing_cpi","per_capita_health_spending","food_at_home_cpi"],sc:{emotional:7,relatability:8,surprise:6,tension:4,visual:9,data_ready:10,originality:5},vs:70,tags:"personal consumption expenditures 2023 housing healthcare food transportation breakdown spending categories $4.1T"}







,{id:"income_source_by_age",title:"Income by source and age group â€” how Americans earn money at each life stage",sub:"Under 35: 85% from wages. Over 65: 40% Social Security, 25% pension/retirement. The income lifecycle.",type:"CHART",geo:"us_national",fmt:"Bar chart",tbl:"T574",section:"Income",ext:["FRED: any national economic time series (fred.stlouisfed.org â€” free API)","BLS national data: employment, wages, CPI (bls.gov â€” free API)"],vars:["median_household_income","total_transfers_per_capita"],join:["pct_families_own_retirement","total_medicare"],sc:{emotional:7,relatability:8,surprise:7,tension:4,visual:8,data_ready:10,originality:7},vs:72,tags:"income source age group wages salary Social Security pension retirement lifecycle 35 65 how Americans earn money"}







,{id:"xref_gdp_per_capita_happiness",title:"State GDP per capita vs. wellbeing index â€” does money buy happiness?",sub:"Connecticut: highest GDP, middle wellbeing. Hawaii: medium GDP, highest wellbeing. Wyoming: high GDP, low wellbeing.",type:"XREF",geo:"us_state",fmt:"Scatter plot",tbl:"T715",section:"Income",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API â€” free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov â€” free)","Census Population Estimates: annual population by state/county (census.gov â€” free)","BLS LAUS: unemployment + labor force by state (bls.gov â€” free)"],vars:["state_gdp_per_capita","median_household_income"],join:["coastline_miles","national_forest_acres","energy_consumption_per_capita"],sc:{emotional:7,relatability:8,surprise:8,tension:4,visual:7,data_ready:8,originality:9},vs:73,tags:"GDP wellbeing happiness state Connecticut Hawaii Wyoming money buy happiness quality of life index beyond GDP"}







,{id:"us_foreign_aid_by_country",title:"US foreign aid by recipient country 2024",sub:"Ukraine: $61B. Israel: $3.8B. Egypt: $1.5B. Jordan: $1.7B. The geography of American largesse.",type:"MAP",geo:"worldwide",fmt:"World choropleth",tbl:"Foreign Commerce PDF",section:"Foreign Commerce",ext:["World Bank Open Data: GDP, population, income by country (data.worldbank.org â€” free API)"],vars:["current_account_balance","trade_balance_goods"],join:["us_troops_overseas","rd_pct_gdp"],sc:{emotional:8,relatability:7,surprise:8,tension:8,visual:9,data_ready:9,originality:7},vs:79,tags:"US foreign aid country 2024 Ukraine $61B Israel $3.8B Egypt Jordan American money largesse geography policy"}







,{id:"crude_oil_imports_by_country",title:"Where US crude oil imports come from 2024",sub:"Canada: 52% of US crude imports. Mexico: 11%. Saudi Arabia: 6%. The petroleum dependency map most Americans don't know.",type:"MAP",geo:"worldwide",fmt:"World choropleth",tbl:"T984",section:"Foreign Commerce",ext:["World Bank Open Data: GDP, population, income by country (data.worldbank.org â€” free API)"],vars:["trade_balance_goods","current_account_balance"],join:["us_troops_overseas","energy_consumption_per_capita"],sc:{emotional:7,relatability:7,surprise:8,tension:7,visual:9,data_ready:10,originality:7},vs:75,tags:"crude oil imports US 2024 Canada 52% Mexico Saudi Arabia petroleum dependency map energy security trade"}







,{id:"us_services_exports_breakdown",title:"US services exports by category 2023 â€” what America actually sells the world",sub:"Travel: $250B. Financial services: $175B. IP royalties: $150B. Education exports: $48B. The invisible export economy.",type:"CHART",geo:"us_national",fmt:"Treemap",tbl:"T1309",section:"Foreign Commerce",ext:["FRED: any national economic time series (fred.stlouisfed.org â€” free API)","BLS national data: employment, wages, CPI (bls.gov â€” free API)"],vars:["balance_on_services","current_account_balance"],join:["rd_pct_gdp","trade_balance_goods"],sc:{emotional:7,relatability:6,surprise:8,tension:5,visual:8,data_ready:10,originality:7},vs:72,tags:"US services exports 2023 travel financial IP royalties education invisible economy what America sells world $250B"}







,{id:"xref_trade_deficit_jobs",title:"Trade deficit growth vs. manufacturing job loss 1990-2024 â€” the numbers connect",sub:"Every $1B increase in the goods deficit correlates with ~13,000 manufacturing jobs lost. The math of deindustrialization.",type:"CHART",geo:"us_national",fmt:"Scatter plot",tbl:"T1306 Â· T1064",section:"Foreign Commerce",ext:["FRED: any national economic time series (fred.stlouisfed.org â€” free API)","BLS national data: employment, wages, CPI (bls.gov â€” free API)"],vars:["current_account_balance","balance_on_goods","manufacturing_employment_trend"],join:["trade_balance_goods","state_unemployment_rate"],sc:{emotional:9,relatability:7,surprise:7,tension:9,visual:7,data_ready:10,originality:8},vs:81,tags:"trade deficit manufacturing job loss 1990 2024 $1B 13000 jobs correlation deindustrialization NAFTA China WTO math"}







,{id:"us_population_by_state_growth",title:"Fastest and slowest growing states by population 2020-2024",sub:"Florida +8.3%. Montana +6.9%. California -1.8%. New York -1.6%. The great domestic migration, state by state.",type:"MAP",geo:"us_state",fmt:"State choropleth",tbl:"Population PDF",section:"Population",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API - free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov - free)","Census Population Estimates: annual population by state/county (census.gov - free)","BLS LAUS: unemployment + labor force by state (bls.gov - free)"],vars:["population_pct_change"],join:["median_household_income","housing_permits_total","rep_pct"],sc:{emotional:7,relatability:8,surprise:6,tension:5,visual:9,data_ready:10,originality:4},vs:70,tags:"population growth state 2020 2024 Florida Montana California New York domestic migration fastest slowest"}







,{id:"dependency_ratio_by_state",title:"Age dependency ratio by state 2024 - who supports whom",sub:"Florida: 62 dependents per 100 working-age adults. Utah: 53. DC: 38. The fiscal burden geography.",type:"MAP",geo:"us_state",fmt:"State choropleth",tbl:"Population PDF",section:"Population",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API - free, tidycensus)","Census Population Estimates: annual population by state/county (census.gov - free)","BLS LAUS: unemployment + labor force by state (bls.gov - free)"],vars:["population_pct_change","total_medicare"],join:["total_transfers_per_capita","rep_pct","median_household_income"],sc:{emotional:7,relatability:6,surprise:7,tension:7,visual:8,data_ready:9,originality:7},vs:71,tags:"dependency ratio state 2024 Florida Utah DC fiscal burden elderly children workers support aging"}







,{id:"immigration_by_origin_country",title:"US immigrant population by country of origin 2023",sub:"Mexico: 10.8M. India: 2.9M. China: 2.7M. Philippines: 2.1M. The immigration geography of the United States.",type:"MAP",geo:"worldwide",fmt:"World choropleth",tbl:"Population PDF",section:"Population",ext:["World Bank Open Data: GDP, population, income by country (data.worldbank.org - free API)"],vars:["net_migration_rate","population_pct_change_2020_2025"],join:["trade_balance_goods","us_troops_overseas"],sc:{emotional:7,relatability:7,surprise:6,tension:7,visual:9,data_ready:9,originality:5},vs:71,tags:"immigrants US 2023 Mexico 10.8M India China Philippines origin country foreign born population geography map"}







,{id:"us_population_2100_scenarios",title:"US population projections to 2100 - three scenarios",sub:"High immigration: 571M by 2100. Low immigration: 320M. Zero immigration: 226M - below today. The numbers tell the story.",type:"CHART",geo:"us_national",fmt:"Line chart",tbl:"Population PDF",section:"Population",ext:["FRED: any national economic time series (fred.stlouisfed.org - free API)"],vars:["population_pct_change","net_migration_rate"],join:["birth_rate_state","total_fertility_rate_by_race"],sc:{emotional:9,relatability:8,surprise:8,tension:8,visual:8,data_ready:9,originality:7},vs:82,tags:"US population 2100 scenarios immigration projection 571M 320M 226M future demographic trajectory policy"}







,{id:"xref_immigration_gdp_growth",title:"Immigration rate vs. GDP growth by state",sub:"High-immigration states grow faster economically. Florida, Texas, New York: the immigration-growth correlation.",type:"XREF",geo:"us_state",fmt:"Scatter plot",tbl:"Population PDF Â· T715",section:"Population Â· Income",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API - free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov - free)","Census Population Estimates: annual population by state/county (census.gov - free)","BLS LAUS: unemployment + labor force by state (bls.gov - free)"],vars:["population_pct_change","state_gdp_per_capita"],join:["housing_permits_total","median_household_income","rep_pct"],sc:{emotional:8,relatability:7,surprise:7,tension:7,visual:7,data_ready:8,originality:7},vs:74,tags:"immigration GDP growth state correlation Florida Texas New York economic contribution policy debate evidence"}







,{id:"billionaire_wealth_vs_bottom_50pct",title:"US billionaire wealth vs. bottom 50% total wealth 2024",sub:"The 737 US billionaires hold more wealth than the bottom 165 million Americans combined. The extreme concentration.",type:"CHART",geo:"us_national",fmt:"Bar chart",tbl:"T1207",section:"Banking Finance Insurance",ext:["FRED: any national economic time series (fred.stlouisfed.org - free API)","BLS national data: employment, wages, CPI (bls.gov - free API)"],vars:["pct_families_own_stocks","pct_families_own_any_asset","median_stock_value"],join:["corporate_profits","income_tax_after_credits","pct_over_200k"],sc:{emotional:10,relatability:9,surprise:8,tension:10,visual:9,data_ready:8,originality:6},vs:88,tags:"billionaire wealth bottom 50% 737 billionaires 165 million Americans extreme concentration inequality Forbes"}







,{id:"wealth_by_generation",title:"Median net worth by generation 2024 - the great wealth transfer that hasn't happened",sub:"Boomers: median $409K net worth. Gen X: $243K. Millennials: $127K. Gen Z: $48K. The generational wealth cliff.",type:"CHART",geo:"us_national",fmt:"Bar chart",tbl:"T1207",section:"Banking Finance Insurance",ext:["FRED: any national economic time series (fred.stlouisfed.org - free API)","BLS national data: employment, wages, CPI (bls.gov - free API)"],vars:["pct_families_own_retirement","pct_families_own_stocks","median_stock_value"],join:["college_tuition_cpi","home_price_index_2024","student_loans_outstanding"],sc:{emotional:9,relatability:10,surprise:7,tension:9,visual:8,data_ready:8,originality:6},vs:85,tags:"net worth generation Boomers Gen X Millennials Gen Z $409K $243K $127K $48K wealth cliff generational gap"}







,{id:"xref_inheritance_mobility",title:"Inheritance expectation vs. actual intergenerational mobility by state",sub:"States with more inherited wealth have less mobility. The inheritance-opportunity tradeoff is geographic.",type:"XREF",geo:"us_state",fmt:"Scatter plot",tbl:"T1207 Â· T727",section:"Banking Â· Income",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API - free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov - free)","Census Population Estimates: annual population by state/county (census.gov - free)","BLS LAUS: unemployment + labor force by state (bls.gov - free)","MIT Election Lab: presidential/congressional results (electionlab.mit.edu - free)"],vars:["pct_families_own_any_asset","median_household_income"],join:["pct_over_200k","pct_under_25k","rep_pct"],sc:{emotional:9,relatability:8,surprise:8,tension:8,visual:7,data_ready:7,originality:9},vs:81,tags:"inheritance mobility state wealth transfer opportunity geographic tradeoff rich poor class social ladder"}







,{id:"nurse_to_patient_ratio_by_state",title:"Registered nurses per 1,000 residents by state",sub:"Massachusetts: 12.7 nurses per 1,000. Nevada: 5.4. The 2.4x nurse shortage geography.",type:"MAP",geo:"us_state",fmt:"State choropleth",tbl:"T174",section:"Health",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API - free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov - free)","Census Population Estimates: annual population by state/county (census.gov - free)","BLS LAUS: unemployment + labor force by state (bls.gov - free)","CDC WONDER: mortality + disease rates by county/state (wonder.cdc.gov - free)"],vars:["per_capita_health_spending","total_medicare"],join:["pct_on_medicaid","median_household_income","rep_pct"],sc:{emotional:8,relatability:7,surprise:7,tension:7,visual:9,data_ready:10,originality:6},vs:74,tags:"nurses per capita state Massachusetts 12.7 Nevada 5.4 shortage workforce healthcare access staffing map"}







,{id:"hospital_beds_per_capita_state",title:"Hospital beds per 1,000 residents by state",sub:"North Dakota: 4.3 beds per 1,000. California: 1.8. The hospital capacity geography that COVID exposed.",type:"MAP",geo:"us_state",fmt:"State choropleth",tbl:"T190",section:"Health",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API - free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov - free)","Census Population Estimates: annual population by state/county (census.gov - free)","BLS LAUS: unemployment + labor force by state (bls.gov - free)","CDC WONDER: mortality + disease rates by county/state (wonder.cdc.gov - free)"],vars:["per_capita_health_spending","hospital_services_cpi"],join:["pct_on_medicaid","total_medicare","median_household_income"],sc:{emotional:8,relatability:7,surprise:7,tension:7,visual:9,data_ready:9,originality:6},vs:73,tags:"hospital beds per capita state North Dakota 4.3 California 1.8 capacity COVID geography shortage rural urban"}







,{id:"er_wait_time_by_region",title:"Emergency room wait times by region and hospital type 2023",sub:"Average ER wait: 2hrs 12min. Rural hospitals: 1hr 45min. Urban teaching hospitals: 3hr 20min. The wait time geography.",type:"CHART",geo:"us_national",fmt:"Bar chart",tbl:"T183",section:"Health",ext:["FRED: any national economic time series (fred.stlouisfed.org - free API)","BLS national data: employment, wages, CPI (bls.gov - free API)"],vars:["per_capita_health_spending","hospital_services_cpi"],join:["pct_on_medicaid","total_medicare"],sc:{emotional:7,relatability:9,surprise:6,tension:5,visual:7,data_ready:10,originality:6},vs:71,tags:"ER emergency room wait time 2023 2hr 12min rural urban teaching hospital region geography access healthcare"}







,{id:"health_spending_by_condition",title:"US health spending by medical condition 2021",sub:"Cardiovascular: $393B. Musculoskeletal: $261B. Mental health: $225B. Cancer: $211B. Where the health money goes.",type:"CHART",geo:"us_national",fmt:"Ranked list",tbl:"T148",section:"Health",ext:["FRED: any national economic time series (fred.stlouisfed.org - free API)","BLS national data: employment, wages, CPI (bls.gov - free API)"],vars:["per_capita_health_spending","health_insurance_cpi"],join:["hospital_services_cpi","total_medicare"],sc:{emotional:7,relatability:7,surprise:7,tension:4,visual:8,data_ready:10,originality:7},vs:70,tags:"health spending medical condition cardiovascular $393B musculoskeletal mental health cancer 2021 top conditions"}







,{id:"mental_health_facilities_by_state",title:"Mental health treatment facilities per 100K residents by state",sub:"Vermont: 34 facilities per 100K. Nevada: 6. The mental health infrastructure desert.",type:"MAP",geo:"us_state",fmt:"State choropleth",tbl:"T179",section:"Health",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API - free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov - free)","Census Population Estimates: annual population by state/county (census.gov - free)","BLS LAUS: unemployment + labor force by state (bls.gov - free)","CDC WONDER: mortality + disease rates by county/state (wonder.cdc.gov - free)"],vars:["per_capita_health_spending","pct_on_medicaid"],join:["state_unemployment_rate","median_household_income","rep_pct"],sc:{emotional:9,relatability:8,surprise:7,tension:7,visual:9,data_ready:9,originality:6},vs:78,tags:"mental health facilities state Vermont 34 Nevada 6 infrastructure desert access treatment per 100K map"}







,{id:"recidivism_rate_by_state",title:"Recidivism rate by state - who keeps going back to prison",sub:"National 3-year recidivism: 44%. Arkansas: 59%. Maine: 22%. The revolving door is not evenly distributed.",type:"MAP",geo:"us_state",fmt:"State choropleth",tbl:"T388",section:"Law Enforcement",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API - free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov - free)","Census Population Estimates: annual population by state/county (census.gov - free)","BLS LAUS: unemployment + labor force by state (bls.gov - free)","FBI Crime Data Explorer: UCR/NIBRS by state/agency (cde.ucr.cjis.gov - free)"],vars:["violent_crime_rate","murder_rate"],join:["median_household_income","rep_pct","pct_on_snap"],sc:{emotional:8,relatability:6,surprise:7,tension:7,visual:9,data_ready:8,originality:7},vs:72,tags:"recidivism rate state 3-year 44% Arkansas 59% Maine 22% revolving door prison reentry criminal justice reform"}







,{id:"police_spending_vs_social_services",title:"Police spending vs. social service spending per capita by city",sub:"Some cities spend 5x more on police than social services. Others are at parity. The defund debate in hard numbers.",type:"XREF",geo:"us_city",fmt:"Scatter plot",tbl:"T362 Â· T491",section:"Law Enforcement",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API - free, tidycensus)"],vars:["violent_crime_rate"],join:["median_household_income","state_unemployment_rate","pct_on_snap"],sc:{emotional:8,relatability:7,surprise:7,tension:8,visual:7,data_ready:7,originality:8},vs:74,tags:"police spending social services city 5x parity defund debate budget priorities crime prevention poverty"}







,{id:"drug_arrest_race_disparity",title:"Drug arrest rates by race vs. drug use rates by race",sub:"Black Americans are arrested for drugs at 3.7x the rate of white Americans - despite nearly equal drug use rates.",type:"CHART",geo:"us_national",fmt:"Bar chart",tbl:"T368",section:"Law Enforcement",ext:["FRED: any national economic time series (fred.stlouisfed.org - free API)","BLS national data: employment, wages, CPI (bls.gov - free API)"],vars:["violent_crime_rate","murder_rate"],join:["median_household_income","pct_on_snap"],sc:{emotional:10,relatability:7,surprise:8,tension:10,visual:8,data_ready:8,originality:7},vs:86,tags:"drug arrest race disparity Black 3.7x white equal use rate criminal justice systematic bias policy war on drugs"}







,{id:"active_shooter_incidents_trend",title:"Active shooter incidents 2000-2024 - the acceleration",sub:"2000: 3 incidents. 2020: 40. 2024: 79. The 26x increase in 24 years that no policy has stopped.",type:"CHART",geo:"us_national",fmt:"Area chart",tbl:"T358",section:"Law Enforcement",ext:["FRED: any national economic time series (fred.stlouisfed.org - free API)","BLS national data: employment, wages, CPI (bls.gov - free API)"],vars:["violent_crime_rate","murder_rate"],join:["rep_pct","median_household_income"],sc:{emotional:10,relatability:9,surprise:8,tension:10,visual:8,data_ready:10,originality:5},vs:87,tags:"active shooter incidents 2000 2024 3 to 79 26x increase acceleration mass shooting policy gun violence schools"}







,{id:"child_abuse_rate_by_state",title:"Child abuse and neglect victims per 1,000 children by state 2023",sub:"Montana: 9.1 per 1,000. Missouri: 2.8. The child welfare crisis geography.",type:"MAP",geo:"us_state",fmt:"State choropleth",tbl:"T386",section:"Law Enforcement",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API - free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov - free)","Census Population Estimates: annual population by state/county (census.gov - free)","BLS LAUS: unemployment + labor force by state (bls.gov - free)","CDC WONDER: mortality + disease rates by county/state (wonder.cdc.gov - free)"],vars:["violent_crime_rate"],join:["pct_on_snap","median_household_income","pct_births_unmarried"],sc:{emotional:9,relatability:6,surprise:7,tension:8,visual:9,data_ready:9,originality:7},vs:76,tags:"child abuse neglect victims per 1000 state 2023 Montana Missouri welfare crisis geography maltreatment foster"}







,{id:"wage_growth_by_industry_decade",title:"Wage growth by industry 2014-2024 - who won the decade",sub:"Tech workers: +62% real wages. Retail workers: +28%. Nurses: +41%. The decade of divergence by industry.",type:"CHART",geo:"us_national",fmt:"Ranked list",tbl:"T653",section:"Labor Force",ext:["FRED: any national economic time series (fred.stlouisfed.org - free API)","BLS national data: employment, wages, CPI (bls.gov - free API)"],vars:["state_unemployment_rate","manufacturing_hourly_wages_state"],join:["median_household_income","college_tuition_cpi"],sc:{emotional:8,relatability:9,surprise:7,tension:7,visual:8,data_ready:10,originality:6},vs:76,tags:"wage growth industry decade 2014 2024 tech retail nurses divergence winner loser salary pay real wages"}







,{id:"gig_economy_workers_by_state",title:"Gig economy workers as % of workforce by state",sub:"California: 16% of workers are gig/independent contractors. Vermont: 8%. The platform economy geography.",type:"MAP",geo:"us_state",fmt:"State choropleth",tbl:"T652",section:"Labor Force",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API - free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov - free)","Census Population Estimates: annual population by state/county (census.gov - free)","BLS LAUS: unemployment + labor force by state (bls.gov - free)"],vars:["state_unemployment_rate","female_lfp_rate"],join:["median_household_income","ecommerce_sales","rep_pct"],sc:{emotional:6,relatability:8,surprise:6,tension:4,visual:8,data_ready:9,originality:6},vs:66,tags:"gig economy workers state California 16% Vermont platform contractor independent worker Uber Lyft DoorDash"}







,{id:"labor_force_participation_men_declining",title:"Male labor force participation 1948-2024 - the long withdrawal",sub:"Prime-age male LFP: 98% in 1954. 89% today. 11 million men who would have worked in 1954 are not working now.",type:"CHART",geo:"us_national",fmt:"Line chart",tbl:"T621",section:"Labor Force",ext:["FRED: any national economic time series (fred.stlouisfed.org - free API)","BLS national data: employment, wages, CPI (bls.gov - free API)"],vars:["female_lfp_rate","state_unemployment_rate"],join:["median_household_income","pct_on_snap","opioid_deaths_per_capita"],sc:{emotional:9,relatability:8,surprise:8,tension:8,visual:8,data_ready:10,originality:7},vs:82,tags:"male labor force participation 1948 2024 98% 89% withdrawal 11 million men working opioids disability despair"}







,{id:"occupational_segregation_by_race",title:"Occupation share by race - who works where",sub:"Black workers are 14% of nursing aides but 4% of physicians. Hispanic workers are 43% of farm workers but 8% of managers.",type:"CHART",geo:"us_national",fmt:"Bar chart",tbl:"T651",section:"Labor Force",ext:["FRED: any national economic time series (fred.stlouisfed.org - free API)","BLS national data: employment, wages, CPI (bls.gov - free API)"],vars:["state_unemployment_rate"],join:["median_household_income","pct_on_snap","pct_bachelors"],sc:{emotional:8,relatability:7,surprise:7,tension:8,visual:8,data_ready:10,originality:6},vs:75,tags:"occupational segregation race Black nursing Hispanic farm workers managers physicians occupation distribution inequality"}







,{id:"part_time_involuntary_rate",title:"Involuntary part-time workers by industry 2024",sub:"15% of retail workers want full-time but can only get part-time. Food service: 12%. The underemployment nobody measures.",type:"CHART",geo:"us_national",fmt:"Ranked list",tbl:"T647",section:"Labor Force",ext:["FRED: any national economic time series (fred.stlouisfed.org - free API)","BLS national data: employment, wages, CPI (bls.gov - free API)"],vars:["state_unemployment_rate","female_lfp_rate"],join:["median_household_income","pct_on_snap"],sc:{emotional:8,relatability:8,surprise:7,tension:6,visual:7,data_ready:10,originality:7},vs:73,tags:"involuntary part time workers retail 15% food service underemployment industry 2024 full time hours poverty wages"}







,{id:"farm_consolidation_trend",title:"Average farm size 1950-2024 - the disappearing small farm",sub:"Average US farm: 195 acres in 1950. 463 acres in 2024. The number of farms cut in half. Big Ag won.",type:"CHART",geo:"us_national",fmt:"Line chart",tbl:"T869",section:"Agriculture",ext:["FRED: any national economic time series (fred.stlouisfed.org - free API)","BLS national data: employment, wages, CPI (bls.gov - free API)","USDA ERS: food environment, rural classification, farm income (ers.usda.gov - free)"],vars:["farms_count_2022","farm_value_land"],join:["pct_cropland","median_household_income"],sc:{emotional:7,relatability:7,surprise:7,tension:6,visual:7,data_ready:10,originality:6},vs:70,tags:"farm consolidation 1950 2024 average size 195 463 acres small farm disappearing Big Ag corporate agriculture"}







,{id:"food_desert_county_map",title:"Food deserts by county - where grocery stores don't exist",sub:"19 million Americans live in food deserts. Rural counties in the South and Great Plains are most affected.",type:"MAP",geo:"us_county",fmt:"County choropleth",tbl:"T576",section:"Agriculture",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API - free, tidycensus)","Census Population Estimates: annual population by state/county (census.gov - free)","BLS LAUS: unemployment + labor force by county (bls.gov - free)","USDA ERS: food environment, rural classification, farm income (ers.usda.gov - free)"],vars:["pct_on_snap","farms_count_2022"],join:["median_household_income","pct_cropland","rural_population_pct"],sc:{emotional:8,relatability:7,surprise:7,tension:7,visual:9,data_ready:8,originality:6},vs:75,tags:"food desert county 19 million rural South Great Plains grocery store access low income USDA ERS map"}







,{id:"crop_insurance_subsidies_by_state",title:"Federal crop insurance subsidies per farm acre by state",sub:"Iowa: $42/acre in federal crop insurance subsidies. Texas: $38. New Hampshire: $2. The farm welfare map.",type:"MAP",geo:"us_state",fmt:"State choropleth",tbl:"T869",section:"Agriculture",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API - free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov - free)","Census Population Estimates: annual population by state/county (census.gov - free)","BLS LAUS: unemployment + labor force by state (bls.gov - free)","USDA ERS: food environment, rural classification, farm income (ers.usda.gov - free)"],vars:["pct_cropland","farms_count_2022"],join:["rep_pct","median_household_income","total_transfers_per_capita"],sc:{emotional:8,relatability:6,surprise:8,tension:7,visual:9,data_ready:8,originality:8},vs:75,tags:"crop insurance subsidies federal farm acre Iowa Texas New Hampshire farm welfare map agricultural policy USDA"}







,{id:"xref_farm_income_food_stamps",title:"Farm income per county vs. SNAP enrollment - the agricultural poverty paradox",sub:"The counties that grow America's food have the highest food stamp enrollment. The farm-hunger paradox.",type:"XREF",geo:"us_county",fmt:"Scatter plot",tbl:"T869 Â· T576",section:"Agriculture Â· Social Insurance",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API - free, tidycensus)","Census Population Estimates: annual population by state/county (census.gov - free)","BLS LAUS: unemployment + labor force by county (bls.gov - free)","USDA ERS: food environment, rural classification, farm income (ers.usda.gov - free)"],vars:["pct_on_snap","farms_count_2022"],join:["pct_cropland","median_household_income","rural_population_pct"],sc:{emotional:9,relatability:7,surprise:9,tension:8,visual:7,data_ready:8,originality:9},vs:82,tags:"farm income SNAP food stamps county paradox grow food hunger agricultural poverty workers low wage rural"}







,{id:"ev_adoption_by_state",title:"Electric vehicle registrations per capita by state 2024",sub:"California: 42 EVs per 1,000 residents. Wyoming: 3. The EV geography mirrors the political map almost perfectly.",type:"MAP",geo:"us_state",fmt:"State choropleth",tbl:"T1126",section:"Transportation",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API - free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov - free)","Census Population Estimates: annual population by state/county (census.gov - free)","BLS LAUS: unemployment + labor force by state (bls.gov - free)","EIA State Energy Data System: production + consumption by state (eia.gov - free API)"],vars:["pct_bridges_poor","passengers_enplaned"],join:["renewable_energy_share","median_household_income","rep_pct"],sc:{emotional:7,relatability:8,surprise:7,tension:6,visual:9,data_ready:8,originality:6},vs:72,tags:"EV electric vehicle registrations state 2024 California 42 Wyoming 3 per 1000 political map geography adoption"}







,{id:"commute_time_by_metro",title:"Average commute time by metro area - who spends life in traffic",sub:"New York: 37 min average commute. Atlanta: 32 min. Buffalo: 20 min. Time is the hidden cost of where you live.",type:"RANK",geo:"us_metro",fmt:"Ranked list",tbl:"T1126",section:"Transportation",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API - free, tidycensus)","BEA Regional: GDP + personal income per capita by metro (apps.bea.gov - free)","BLS LAUS: unemployment + labor force by metro (bls.gov - free)"],vars:["metro_per_capita_income"],join:["median_household_income","housing_permits_total"],sc:{emotional:7,relatability:9,surprise:6,tension:4,visual:8,data_ready:9,originality:5},vs:70,tags:"commute time metro average New York 37 Atlanta 32 Buffalo 20 traffic hidden cost life hours lost geography"}







,{id:"truck_freight_by_state",title:"Truck freight tonnage by state - the hidden backbone",sub:"Texas handles 1.3B tons of truck freight. California: 1.1B. The freight geography of the American economy.",type:"MAP",geo:"us_state",fmt:"State choropleth",tbl:"T1120",section:"Transportation",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API - free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov - free)","Census Population Estimates: annual population by state/county (census.gov - free)","BLS LAUS: unemployment + labor force by state (bls.gov - free)"],vars:["pct_bridges_poor","waterway_freight_tons"],join:["port_total_tons","energy_consumption_per_capita","state_gdp_per_capita"],sc:{emotional:5,relatability:6,surprise:7,tension:3,visual:8,data_ready:9,originality:6},vs:62,tags:"truck freight tonnage state Texas 1.3B California 1.1B transportation backbone economy logistics supply chain map"}







,{id:"public_transit_ridership_decline",title:"Public transit ridership 2019-2024 - the COVID collapse that never recovered",sub:"National transit ridership: down 27% from 2019 even in 2024. NYC at 80%. Bus systems across the South: 60% of pre-COVID.",type:"CHART",geo:"us_national",fmt:"Line chart",tbl:"T1126",section:"Transportation",ext:["FRED: any national economic time series (fred.stlouisfed.org - free API)","BLS national data: employment, wages, CPI (bls.gov - free API)"],vars:["passengers_enplaned","pct_bridges_poor"],join:["metro_per_capita_income","housing_permits_total"],sc:{emotional:7,relatability:8,surprise:7,tension:6,visual:7,data_ready:8,originality:6},vs:70,tags:"public transit ridership 2019 2024 COVID collapse recovery 27% NYC 80% bus South 60% urban transportation"}







,{id:"credit_card_debt_by_state",title:"Credit card debt per capita by state 2024",sub:"Alaska: $8,100 average credit card debt per person. Iowa: $4,200. The debt geography of American spending.",type:"MAP",geo:"us_state",fmt:"State choropleth",tbl:"T1207",section:"Banking Finance Insurance",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API - free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov - free)","Census Population Estimates: annual population by state/county (census.gov - free)","BLS LAUS: unemployment + labor force by state (bls.gov - free)"],vars:["credit_card_rate_all_accounts","mortgage_delinquency_rate"],join:["median_household_income","pct_on_snap","rep_pct"],sc:{emotional:7,relatability:8,surprise:6,tension:5,visual:8,data_ready:8,originality:5},vs:68,tags:"credit card debt per capita state 2024 Alaska $8100 Iowa $4200 spending geography American households"}







,{id:"student_loan_debt_by_state",title:"Student loan debt per borrower by state 2024",sub:"Georgia: $42,000 average per borrower. Utah: $18,000. The student debt geography and why Georgia is such an outlier.",type:"MAP",geo:"us_state",fmt:"State choropleth",tbl:"T1207",section:"Banking Finance Insurance",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API - free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov - free)","Census Population Estimates: annual population by state/county (census.gov - free)","BLS LAUS: unemployment + labor force by state (bls.gov - free)"],vars:["student_loans_outstanding","college_tuition_cpi"],join:["pct_bachelors","median_household_income","state_unemployment_rate"],sc:{emotional:8,relatability:9,surprise:7,tension:7,visual:8,data_ready:8,originality:6},vs:77,tags:"student loan debt per borrower state 2024 Georgia $42000 Utah $18000 HBCU for-profit college education debt"}







,{id:"unbanked_households_by_state",title:"Unbanked households by state - who has no bank account",sub:"Mississippi: 11% of households have no bank account. New Hampshire: 2%. The financial exclusion geography.",type:"MAP",geo:"us_state",fmt:"State choropleth",tbl:"T1207",section:"Banking Finance Insurance",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API - free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov - free)","Census Population Estimates: annual population by state/county (census.gov - free)","BLS LAUS: unemployment + labor force by state (bls.gov - free)"],vars:["pct_families_own_any_asset","credit_card_rate_all_accounts"],join:["median_household_income","pct_on_snap","rep_pct"],sc:{emotional:7,relatability:6,surprise:7,tension:6,visual:8,data_ready:8,originality:6},vs:68,tags:"unbanked households state Mississippi 11% New Hampshire 2% financial exclusion no bank account geography"}







,{id:"household_debt_to_income_trend",title:"Household debt-to-income ratio 1980-2024 - the leverage buildup",sub:"1980: households owed 0.6x income in debt. Peak 2008: 1.3x. Today: 0.97x. Still near historic highs.",type:"CHART",geo:"us_national",fmt:"Line chart",tbl:"T1207",section:"Banking Finance Insurance",ext:["FRED: any national economic time series (fred.stlouisfed.org - free API)","BLS national data: employment, wages, CPI (bls.gov - free API)"],vars:["mortgage_delinquency_rate","credit_card_rate_all_accounts"],join:["home_price_index_2024","student_loans_outstanding","federal_debt_pct_gdp"],sc:{emotional:7,relatability:7,surprise:7,tension:7,visual:7,data_ready:9,originality:5},vs:70,tags:"household debt income ratio 1980 2024 0.6x 1.3x 0.97x leverage buildup historic highs mortgage financial crisis"}







,{id:"voter_turnout_by_county",title:"Voter turnout by county 2024 - who actually votes",sub:"Some Montana counties: 85% turnout. Some urban Texas counties: 38%. The participation gap is enormous and geographic.",type:"MAP",geo:"us_county",fmt:"County choropleth",tbl:"T454",section:"Elections",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API - free, tidycensus)","Census Population Estimates: annual population by state/county (census.gov - free)","BLS LAUS: unemployment + labor force by county (bls.gov - free)","MIT Election Lab: presidential/congressional results (electionlab.mit.edu - free)"],vars:["rep_pct"],join:["median_household_income","pct_bachelors","pct_on_snap"],sc:{emotional:8,relatability:8,surprise:7,tension:7,visual:9,data_ready:9,originality:5},vs:77,tags:"voter turnout county 2024 Montana 85% Texas 38% participation gap geographic democracy who votes"}







,{id:"xref_income_voter_turnout",title:"Median income vs. voter turnout by county",sub:"High-income counties vote at 72% rates. Low-income counties: 49%. The turnout gap is a class gap.",type:"XREF",geo:"us_county",fmt:"Scatter plot",tbl:"T454 Â· T727",section:"Elections Â· Income",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API - free, tidycensus)","Census Population Estimates: annual population by state/county (census.gov - free)","BLS LAUS: unemployment + labor force by county (bls.gov - free)","MIT Election Lab: presidential/congressional results (electionlab.mit.edu - free)"],vars:["rep_pct","median_household_income"],join:["pct_bachelors","pct_on_snap","violent_crime_rate"],sc:{emotional:9,relatability:8,surprise:7,tension:9,visual:7,data_ready:9,originality:7},vs:82,tags:"income voter turnout county class gap 72% 49% wealth voting participation democracy representation power"}







,{id:"rural_urban_vote_swing_2000_2024",title:"Rural vs. urban vote swing 2000-2024 - the great political realignment",sub:"Rural counties: 54% Republican in 2000. 70% in 2024. Urban counties: 56% Democrat in 2000. 72% in 2024. The sorting is complete.",type:"CHART",geo:"us_national",fmt:"Line chart",tbl:"T454",section:"Elections",ext:["FRED: any national economic time series (fred.stlouisfed.org - free API)","MIT Election Lab: presidential/congressional results (electionlab.mit.edu - free)"],vars:["rep_pct","rural_population_pct"],join:["median_household_income","pct_bachelors","manufacturing_employment_trend"],sc:{emotional:9,relatability:8,surprise:6,tension:8,visual:8,data_ready:9,originality:6},vs:80,tags:"rural urban vote swing 2000 2024 realignment 54% 70% Republican 56% 72% Democrat sorting complete political geography"}







,{id:"third_party_vote_by_state_history",title:"Third-party vote share by state 1992-2024 - where protest votes concentrate",sub:"Maine: 21% third-party in 1992. Utah: 21% in 2016. The geography of political dissatisfaction.",type:"MAP",geo:"us_state",fmt:"State choropleth",tbl:"T454",section:"Elections",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API - free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov - free)","Census Population Estimates: annual population by state/county (census.gov - free)","BLS LAUS: unemployment + labor force by state (bls.gov - free)","MIT Election Lab: presidential/congressional results (electionlab.mit.edu - free)"],vars:["rep_pct"],join:["median_household_income","pct_bachelors","state_unemployment_rate"],sc:{emotional:6,relatability:6,surprise:7,tension:5,visual:8,data_ready:9,originality:7},vs:66,tags:"third party vote state 1992 2024 Maine 21% Utah Ross Perot Gary Johnson protest vote dissatisfaction geography"}







,{id:"xref_church_attendance_divorce",title:"Church attendance vs. divorce rate by state",sub:"The Bible Belt has the highest divorce rates in America. Oklahoma: 5.1 per 1,000. Massachusetts: 2.3. God and marriage don't align geographically.",type:"XREF",geo:"us_state",fmt:"Scatter plot",tbl:"T79 Â· T454",section:"Births Deaths Â· Elections",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API - free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov - free)","Census Population Estimates: annual population by state/county (census.gov - free)","BLS LAUS: unemployment + labor force by state (bls.gov - free)","MIT Election Lab: presidential/congressional results (electionlab.mit.edu - free)"],vars:["birth_rate_state","pct_births_unmarried"],join:["rep_pct","median_household_income","teen_birth_rate"],sc:{emotional:9,relatability:8,surprise:10,tension:8,visual:7,data_ready:7,originality:9},vs:87,tags:"church attendance divorce rate state Bible Belt Oklahoma 5.1 Massachusetts 2.3 paradox religion marriage counterintuitive"}







,{id:"xref_sex_ed_teen_pregnancy",title:"Abstinence-only sex ed states vs. teen birth rates",sub:"States with abstinence-only sex education have teen birth rates 2x higher. The policy produces the opposite of its intent.",type:"XREF",geo:"us_state",fmt:"Scatter plot",tbl:"T86 Â· T454",section:"Births Deaths Â· Elections",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API - free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov - free)","Census Population Estimates: annual population by state/county (census.gov - free)","BLS LAUS: unemployment + labor force by state (bls.gov - free)","MIT Election Lab: presidential/congressional results (electionlab.mit.edu - free)"],vars:["teen_birth_rate","pct_births_unmarried"],join:["rep_pct","birth_rate_state","median_household_income"],sc:{emotional:9,relatability:8,surprise:9,tension:9,visual:7,data_ready:7,originality:8},vs:86,tags:"abstinence sex ed teen birth rate states 2x opposite policy intent paradox counterintuitive pregnancy Republican"}







,{id:"xref_crime_rate_police_spending",title:"Police spending per capita vs. violent crime rate by city",sub:"Cities that spend the most on police per capita don't have the lowest crime rates. The spending-safety disconnect.",type:"XREF",geo:"us_city",fmt:"Scatter plot",tbl:"T340 Â· T364",section:"Law Enforcement",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API - free, tidycensus)"],vars:["violent_crime_rate","murder_rate"],join:["median_household_income","pct_on_snap","state_unemployment_rate"],sc:{emotional:8,relatability:7,surprise:8,tension:7,visual:7,data_ready:7,originality:8},vs:75,tags:"police spending violent crime rate city disconnect paradox safety spending more not safer budget priorities policy"}







,{id:"xref_gun_control_laws_gun_deaths",title:"Strength of gun laws vs. gun death rate by state",sub:"California gun law score: A. Gun death rate: 8.5 per 100K. Mississippi: F. Gun death rate: 33. The correlation is 0.85.",type:"XREF",geo:"us_state",fmt:"Scatter plot",tbl:"T340 Â· T454",section:"Law Enforcement Â· Elections",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API - free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov - free)","Census Population Estimates: annual population by state/county (census.gov - free)","BLS LAUS: unemployment + labor force by state (bls.gov - free)","CDC WONDER: mortality + disease rates by county/state (wonder.cdc.gov - free)","MIT Election Lab: presidential/congressional results (electionlab.mit.edu - free)"],vars:["violent_crime_rate","murder_rate"],join:["rep_pct","median_household_income"],sc:{emotional:9,relatability:8,surprise:7,tension:9,visual:7,data_ready:8,originality:6},vs:82,tags:"gun laws gun death rate state California A Mississippi F 0.85 correlation evidence policy Giffords law center"}







,{id:"xref_college_towns_inequality",title:"College town income inequality vs. surrounding county",sub:"College towns have higher Gini coefficients than their surrounding counties. Professors and service workers: the campus inequality.",type:"XREF",geo:"us_city",fmt:"Scatter plot",tbl:"T727 Â· T291",section:"Income Â· Education",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API - free, tidycensus)"],vars:["median_household_income","pct_bachelors"],join:["pct_under_25k","pct_over_200k","state_unemployment_rate"],sc:{emotional:7,relatability:7,surprise:8,tension:5,visual:6,data_ready:7,originality:9},vs:71,tags:"college town income inequality Gini surrounding county professors service workers campus paradox higher education"}







,{id:"world_gdp_per_capita_vs_happiness",title:"GDP per capita vs. life satisfaction by country",sub:"Luxembourg: highest GDP, 7.2/10 happiness. Finland: $55K GDP, 7.8/10. Costa Rica: $22K, 7.0. Money matters less above $75K.",type:"XREF",geo:"worldwide",fmt:"Scatter plot",tbl:"International Statistics",section:"International Statistics",ext:["World Bank Open Data: GDP, population, income by country (data.worldbank.org - free API)"],vars:["trade_balance_goods","rd_pct_gdp"],join:["population_pct_change_2020_2025","net_migration_rate"],sc:{emotional:7,relatability:8,surprise:7,tension:4,visual:8,data_ready:8,originality:5},vs:70,tags:"GDP happiness life satisfaction country Luxembourg Finland Costa Rica money threshold World Happiness Report"}







,{id:"world_corruption_index_income",title:"Corruption perception index vs. per capita income by country",sub:"The 20 most corrupt countries average $4,200 GDP per capita. The 20 least corrupt: $52,000. Corruption IS poverty.",type:"XREF",geo:"worldwide",fmt:"Scatter plot",tbl:"International Statistics",section:"International Statistics",ext:["World Bank Open Data: GDP, population, income by country (data.worldbank.org - free API)"],vars:["rd_pct_gdp","trade_balance_goods"],join:["net_migration_rate","population_pct_change_2020_2025"],sc:{emotional:8,relatability:6,surprise:7,tension:7,visual:8,data_ready:8,originality:7},vs:74,tags:"corruption perception income country $4200 $52000 Transparency International poverty development causation GDP"}







,{id:"countries_losing_population_fastest",title:"Countries losing population fastest 2020-2030",sub:"Bulgaria: -6.5% by 2030. Lithuania: -5.8%. Latvia: -5.1%. The Eastern European demographic collapse.",type:"RANK",geo:"worldwide",fmt:"Ranked list",tbl:"International Statistics",section:"International Statistics",ext:["World Bank Open Data: GDP, population, income by country (data.worldbank.org - free API)"],vars:["population_pct_change_2020_2025","net_migration_rate"],join:["birth_rate","rd_pct_gdp"],sc:{emotional:7,relatability:6,surprise:8,tension:7,visual:8,data_ready:9,originality:6},vs:73,tags:"population loss fastest country 2020 2030 Bulgaria Lithuania Latvia Eastern Europe demographic collapse emigration"}







,{id:"world_urbanization_rate_change",title:"Urbanization rate change by country 2000-2025",sub:"China went from 36% urban to 66% in 25 years. Nigeria: 36% to 54%. The fastest urbanization in human history.",type:"MAP",geo:"worldwide",fmt:"World choropleth",tbl:"International Statistics",section:"International Statistics",ext:["World Bank Open Data: GDP, population, income by country (data.worldbank.org - free API)"],vars:["population_pct_change_2020_2025","population_per_sq_km"],join:["trade_balance_goods","net_migration_rate"],sc:{emotional:6,relatability:6,surprise:8,tension:4,visual:9,data_ready:9,originality:6},vs:68,tags:"urbanization rate country 2000 2025 China 36% 66% Nigeria fastest history rural urban migration cities growth"}







,{id:"veterans_by_state_per_capita",title:"Veterans as % of adult population by state 2024",sub:"Alaska: 12% veterans. Virginia: 11%. California: 6%. The military geography of America.",type:"MAP",geo:"us_state",fmt:"State choropleth",tbl:"T543",section:"National Security",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API - free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov - free)","Census Population Estimates: annual population by state/county (census.gov - free)","BLS LAUS: unemployment + labor force by state (bls.gov - free)"],vars:["defense_budget_total","active_duty_total"],join:["median_household_income","rep_pct","state_unemployment_rate"],sc:{emotional:6,relatability:6,surprise:7,tension:3,visual:8,data_ready:9,originality:5},vs:63,tags:"veterans per capita state 2024 Alaska 12% Virginia California military geography adult population service"}







,{id:"xref_military_bases_local_income",title:"Counties with military bases vs. median income",sub:"Military base counties average 18% higher median income than comparable non-base rural counties. Defense spending as regional development.",type:"XREF",geo:"us_county",fmt:"Scatter plot",tbl:"T543 Â· T727",section:"National Security Â· Income",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API - free, tidycensus)","Census Population Estimates: annual population by state/county (census.gov - free)","BLS LAUS: unemployment + labor force by county (bls.gov - free)"],vars:["defense_budget_total","median_household_income"],join:["active_duty_total","total_transfers_per_capita","rep_pct"],sc:{emotional:7,relatability:5,surprise:8,tension:5,visual:6,data_ready:7,originality:8},vs:67,tags:"military bases county income 18% higher rural regional development defense spending economic benefit Keynesian"}







,{id:"us_troops_overseas_by_country",title:"US military personnel stationed overseas by country 2024",sub:"Japan: 54,000 troops. Germany: 35,000. South Korea: 28,000. The American empire in headcount.",type:"MAP",geo:"worldwide",fmt:"World choropleth",tbl:"T543",section:"National Security",ext:["World Bank Open Data: GDP, population, income by country (data.worldbank.org - free API)"],vars:["us_troops_overseas","defense_budget_total"],join:["trade_balance_goods","rd_pct_gdp"],sc:{emotional:7,relatability:6,surprise:7,tension:7,visual:9,data_ready:9,originality:5},vs:71,tags:"US troops overseas country 2024 Japan 54000 Germany 35000 South Korea 28000 military empire headcount bases"}







,{id:"defense_spending_by_state_per_gdp",title:"Defense contract spending as % of state GDP",sub:"Virginia: 16% of GDP from defense. Hawaii: 11%. Texas: 4%. Connecticut: 7%. The defense-dependent economies.",type:"MAP",geo:"us_state",fmt:"State choropleth",tbl:"T543",section:"National Security",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API - free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov - free)","Census Population Estimates: annual population by state/county (census.gov - free)","BLS LAUS: unemployment + labor force by state (bls.gov - free)"],vars:["defense_budget_total","active_duty_total"],join:["state_gdp_per_capita","median_household_income","rep_pct"],sc:{emotional:7,relatability:5,surprise:8,tension:5,visual:8,data_ready:8,originality:7},vs:69,tags:"defense contract spending state GDP Virginia 16% Hawaii Texas Connecticut dependent economies military industrial"}







,{id:"puerto_rico_income_vs_states",title:"Puerto Rico median income vs. all 50 states - the 51st comparison",sub:"Puerto Rico median income: $23,000. The poorest state (Mississippi): $49,000. Puerto Rico would be the poorest by far.",type:"RANK",geo:"top_n_list",fmt:"Ranked list",tbl:"Puerto Rico PDF",section:"Population",ext:[],vars:["median_household_income"],join:["pct_on_snap","total_transfers_per_capita","pct_on_medicaid"],sc:{emotional:9,relatability:7,surprise:8,tension:8,visual:9,data_ready:9,originality:8},vs:82,tags:"Puerto Rico income vs states $23000 Mississippi $49000 poorest 51st comparison territory inequality federal policy"}







,{id:"puerto_rico_population_decline",title:"Puerto Rico population 2000-2024 - the collapse",sub:"Puerto Rico population: 3.8M in 2000. 3.2M today. 600,000 people left. Hurricane Maria accelerated an already ongoing crisis.",type:"CHART",geo:"us_national",fmt:"Area chart",tbl:"Puerto Rico PDF",section:"Population",ext:["FRED: any national economic time series (fred.stlouisfed.org - free API)"],vars:["population_pct_change","net_migration_rate"],join:["birth_rate_state","median_household_income"],sc:{emotional:8,relatability:6,surprise:7,tension:7,visual:7,data_ready:9,originality:7},vs:73,tags:"Puerto Rico population 2000 2024 3.8M 3.2M 600000 left Maria hurricane decline migration collapse territory"}







,{id:"opioid_deaths_vs_manufacturing_loss_county",title:"Opioid death rate vs. manufacturing job loss by county",sub:"Counties that lost 30%+ of manufacturing jobs have 4x the opioid death rates of counties that didn't. The despair pipeline.",type:"XREF",geo:"us_county",fmt:"Scatter plot",tbl:"T340 Â· T1064",section:"Health Â· Manufactures",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API - free, tidycensus)","Census Population Estimates: annual population by state/county (census.gov - free)","BLS LAUS: unemployment + labor force by county (bls.gov - free)","CDC WONDER: mortality + disease rates by county/state (wonder.cdc.gov - free)"],vars:["violent_crime_rate","manufacturing_employment_trend"],join:["pct_on_snap","median_household_income","state_unemployment_rate"],sc:{emotional:10,relatability:8,surprise:7,tension:9,visual:7,data_ready:8,originality:8},vs:87,tags:"opioid death manufacturing job loss county 4x despair pipeline correlation deindustrialization fentanyl Appalachia Rust Belt"}







,{id:"life_expectancy_by_county",title:"Life expectancy by county - the 20-year gap within America",sub:"Summit County CO: 86.8 years. Oglala Lakota County SD: 66.8. A 20-year life expectancy gap within one country.",type:"MAP",geo:"us_county",fmt:"County choropleth",tbl:"T105",section:"Health",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API - free, tidycensus)","Census Population Estimates: annual population by state/county (census.gov - free)","BLS LAUS: unemployment + labor force by county (bls.gov - free)","CDC WONDER: mortality + disease rates by county/state (wonder.cdc.gov - free)"],vars:["birth_rate_state","total_fertility_rate_by_race"],join:["median_household_income","pct_on_snap","violent_crime_rate"],sc:{emotional:10,relatability:8,surprise:8,tension:9,visual:9,data_ready:8,originality:6},vs:87,tags:"life expectancy county Summit CO 86.8 Oglala Lakota SD 66.8 20 year gap within America health inequality race income"}







,{id:"remote_work_county_migration",title:"Counties gaining population from remote work migration 2020-2024",sub:"Rural mountain counties gained 15-25% population. Ski towns, lake districts, and small cities in the Rockies boomed.",type:"MAP",geo:"us_county",fmt:"County choropleth",tbl:"Population PDF",section:"Population",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API - free, tidycensus)","Census Population Estimates: annual population by state/county (census.gov - free)","BLS LAUS: unemployment + labor force by county (bls.gov - free)"],vars:["population_pct_change"],join:["home_price_index_2024","housing_permits_total","median_household_income"],sc:{emotional:7,relatability:9,surprise:7,tension:5,visual:9,data_ready:8,originality:7},vs:76,tags:"remote work county migration 2020 2024 rural mountain 15-25% ski towns lake Rockies boom population shift COVID"}







,{id:"childcare_cost_vs_minimum_wage",title:"Childcare cost vs. minimum wage by state - the impossible math",sub:"In 33 states, full-time childcare costs more than the state minimum wage earns in a year. The childcare math is broken.",type:"XREF",geo:"us_state",fmt:"Scatter plot",tbl:"T770 Â· T609",section:"Prices Â· Social Insurance",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API - free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov - free)","Census Population Estimates: annual population by state/county (census.gov - free)","BLS LAUS: unemployment + labor force by state (bls.gov - free)"],vars:["daycare_preschool_cpi","median_household_income"],join:["female_lfp_rate","pct_on_snap","birth_rate_state"],sc:{emotional:10,relatability:9,surprise:8,tension:9,visual:7,data_ready:9,originality:8},vs:88,tags:"childcare cost minimum wage state 33 states impossible math broken annual full time more than earn year women"}







,{id:"rent_burden_by_city",title:"Share of renters paying 30%+ of income on rent by city",sub:"Miami: 63% of renters are cost-burdened. Los Angeles: 58%. Pittsburgh: 38%. The rent burden geography.",type:"RANK",geo:"us_city",fmt:"Ranked list",tbl:"T771",section:"Housing",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API - free, tidycensus)"],vars:["rent_primary_residence_cpi","home_price_index_2024"],join:["median_household_income","housing_permits_total","pct_on_snap"],sc:{emotional:9,relatability:9,surprise:6,tension:8,visual:8,data_ready:9,originality:5},vs:81,tags:"rent burden 30% income city Miami 63% Los Angeles 58% Pittsburgh 38% cost burdened renters housing crisis"}







,{id:"grocery_price_index_by_category",title:"Grocery price inflation by food category 2019-2024",sub:"Eggs: +147%. Butter: +71%. Chicken: +38%. Lettuce: +9%. The great pantry inflation in one chart.",type:"CHART",geo:"us_national",fmt:"Ranked list",tbl:"T770",section:"Prices",ext:["FRED: any national economic time series (fred.stlouisfed.org - free API)","BLS national data: employment, wages, CPI (bls.gov - free API)"],vars:["food_at_home_cpi","eggs_cpi"],join:["all_items_cpi","median_household_income"],sc:{emotional:8,relatability:10,surprise:8,tension:6,visual:8,data_ready:10,originality:6},vs:80,tags:"grocery price inflation category 2019 2024 eggs 147% butter 71% chicken 38% lettuce 9% pantry food CPI shopping"}







,{id:"insurance_cost_vs_wages",title:"Auto and home insurance CPI vs. wage growth 2015-2024",sub:"Auto insurance: up 76% since 2015. Home insurance: up 52%. Wages: up 34%. The protection-affordability crisis.",type:"CHART",geo:"us_national",fmt:"Line chart",tbl:"T770",section:"Prices",ext:["FRED: any national economic time series (fred.stlouisfed.org - free API)","BLS national data: employment, wages, CPI (bls.gov - free API)"],vars:["motor_vehicle_insurance_cpi","all_items_cpi"],join:["median_household_income","home_price_index_2024"],sc:{emotional:8,relatability:8,surprise:8,tension:7,visual:7,data_ready:10,originality:7},vs:78,tags:"auto home insurance CPI wages 2015 2024 76% 52% 34% protection affordability crisis climate rate increases"}







,{id:"pet_ownership_by_state",title:"Pet ownership rate by state - cats vs. dogs geography",sub:"Vermont: 71% of households own a pet. DC: 37%. And the cat-vs-dog divide follows political lines almost exactly.",type:"MAP",geo:"us_state",fmt:"State choropleth",tbl:"T1267",section:"Arts Recreation",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API - free, tidycensus)","Census Population Estimates: annual population by state/county (census.gov - free)"],vars:["annual_attendance"],join:["median_household_income","rep_pct","rural_population_pct"],sc:{emotional:5,relatability:9,surprise:7,tension:2,visual:9,data_ready:8,originality:8},vs:69,tags:"pet ownership state Vermont 71% DC 37% cat dog divide political cultural geography household fun curious"}







,{id:"reading_habits_by_income",title:"Reading rate by income level - who still reads books",sub:"Households over $75K: 61% read a book in the past year. Under $30K: 28%. The reading class divide.",type:"CHART",geo:"us_national",fmt:"Bar chart",tbl:"T1263",section:"Arts Recreation",ext:["FRED: any national economic time series (fred.stlouisfed.org - free API)","BLS national data: employment, wages, CPI (bls.gov - free API)"],vars:["annual_attendance"],join:["median_household_income","pct_bachelors"],sc:{emotional:6,relatability:8,surprise:6,tension:4,visual:7,data_ready:10,originality:7},vs:66,tags:"reading books income level $75K 61% $30K 28% class divide literacy cultural habit who reads households"}







,{id:"sports_betting_revenue_by_state",title:"Sports betting revenue by state 2024 - the gambling gold rush",sub:"New York: $1.9B in sports betting revenue. New Jersey: $1.4B. The overnight gambling economy.",type:"MAP",geo:"us_state",fmt:"State choropleth",tbl:"T493",section:"State Govt",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API - free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov - free)","Census Population Estimates: annual population by state/county (census.gov - free)","BLS LAUS: unemployment + labor force by state (bls.gov - free)"],vars:["lottery_revenue_per_capita","sports_betting_revenue"],join:["median_household_income","rep_pct","pct_on_snap"],sc:{emotional:6,relatability:7,surprise:7,tension:4,visual:8,data_ready:9,originality:6},vs:66,tags:"sports betting revenue state 2024 New York $1.9B New Jersey $1.4B gambling gold rush DraftKings FanDuel"}







,{id:"social_isolation_by_state",title:"People who report having no close friends - the loneliness map",sub:"23% of Americans report having no close friends. Some states hit 30%. The loneliness epidemic in geographic form.",type:"MAP",geo:"us_state",fmt:"State choropleth",tbl:"T1272",section:"Arts Recreation",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API - free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov - free)","Census Population Estimates: annual population by state/county (census.gov - free)","BLS LAUS: unemployment + labor force by state (bls.gov - free)"],vars:["annual_attendance","sports_attendance_12mo"],join:["median_household_income","rep_pct","state_unemployment_rate"],sc:{emotional:9,relatability:9,surprise:7,tension:7,visual:8,data_ready:7,originality:8},vs:82,tags:"social isolation loneliness no close friends 23% 30% epidemic geographic map mental health modern crisis America"}







,{id:"ncaa_sports_gender_participation",title:"NCAA sports participation by sex 1972-2024 - Title IX's 50 years",sub:"Women's NCAA athletes: 30,000 in 1972. 230,000 in 2024. Men's: 170,000 to 280,000. The Title IX transformation.",type:"CHART",geo:"us_national",fmt:"Line chart",tbl:"T1274",section:"Arts Recreation",ext:["FRED: any national economic time series (fred.stlouisfed.org - free API)","BLS national data: employment, wages, CPI (bls.gov - free API)"],vars:["annual_attendance","sports_attendance_12mo"],join:["pct_bachelors","female_lfp_rate"],sc:{emotional:7,relatability:7,surprise:6,tension:4,visual:7,data_ready:10,originality:5},vs:66,tags:"NCAA sports gender participation 1972 2024 Title IX women 30000 230000 men 170000 280000 transformation college"}







,{id:"us_trade_deficit_by_country",title:"US goods trade balance by country 2024 - where the deficit lives",sub:"China: -$279B deficit. Mexico: -$152B. Vietnam: -$104B. Ireland: -$87B. The geography of what we owe.",type:"MAP",geo:"worldwide",fmt:"World choropleth",tbl:"T1306",section:"Foreign Commerce",ext:["World Bank Open Data: GDP, population, income by country (data.worldbank.org - free API)"],vars:["trade_balance_goods","current_account_balance"],join:["balance_on_goods","foreign_affiliate_employment"],sc:{emotional:8,relatability:7,surprise:8,tension:8,visual:9,data_ready:10,originality:6},vs:78,tags:"US trade deficit country 2024 China -$279B Mexico -$152B Vietnam Ireland what we owe goods balance geography"}







,{id:"us_exports_by_product_category",title:"Top US export categories 2024 - what America actually sells",sub:"Refined petroleum: $196B. Aircraft: $130B. Semiconductors: $65B. Soybeans: $26B. The export economy revealed.",type:"RANK",geo:"top_n_list",fmt:"Ranked list",tbl:"T1307",section:"Foreign Commerce",ext:[],vars:["trade_balance_goods","balance_on_goods"],join:["current_account_balance","foreign_affiliate_employment"],sc:{emotional:6,relatability:6,surprise:8,tension:4,visual:8,data_ready:10,originality:6},vs:66,tags:"US exports product category 2024 petroleum $196B aircraft semiconductor soybeans what America sells economy"}







,{id:"remittances_sent_from_us_by_country",title:"Remittances sent from the US by destination country 2024",sub:"Mexico receives $63B from US-based Mexicans annually. India: $32B. Guatemala: $20B. The money America sends home.",type:"MAP",geo:"worldwide",fmt:"World choropleth",tbl:"T1310",section:"Foreign Commerce",ext:["World Bank Open Data: GDP, population, income by country (data.worldbank.org - free API)"],vars:["current_account_balance","balance_on_services"],join:["net_migration_rate","trade_balance_goods"],sc:{emotional:7,relatability:6,surprise:8,tension:5,visual:9,data_ready:8,originality:8},vs:73,tags:"remittances sent US country 2024 Mexico $63B India $32B Guatemala money home immigrants World Bank"}







,{id:"xref_happiness_commute_time",title:"Commute time vs. self-reported happiness by metro",sub:"Every 10 extra minutes of commute drops life satisfaction by 0.15 points. The most measurable source of unhappiness.",type:"XREF",geo:"us_metro",fmt:"Scatter plot",tbl:"T726 Â· T1265",section:"Transportation Â· Income",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API - free, tidycensus)","BEA Regional: GDP + personal income per capita by metro (apps.bea.gov - free)","BLS LAUS: unemployment + labor force by metro (bls.gov - free)"],vars:["metro_per_capita_income"],join:["median_household_income","housing_permits_total"],sc:{emotional:8,relatability:9,surprise:7,tension:5,visual:7,data_ready:7,originality:8},vs:76,tags:"commute time happiness life satisfaction metro 10 minutes 0.15 points measurable unhappiness wellbeing urban planning"}







,{id:"xref_inequality_health_outcomes",title:"Income inequality (Gini) vs. multiple health outcomes by state",sub:"The most unequal states have the worst health outcomes on nearly every measure - not just the poorest states.",type:"XREF",geo:"us_state",fmt:"Scatter plot",tbl:"T727 Â· T141",section:"Income Â· Health",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API - free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov - free)","Census Population Estimates: annual population by state/county (census.gov - free)","BLS LAUS: unemployment + labor force by state (bls.gov - free)","CDC WONDER: mortality + disease rates by county/state (wonder.cdc.gov - free)"],vars:["median_household_income","per_capita_health_spending"],join:["pct_over_200k","violent_crime_rate","pct_on_snap"],sc:{emotional:9,relatability:7,surprise:8,tension:8,visual:7,data_ready:8,originality:8},vs:81,tags:"income inequality Gini health outcomes state worst not just poorest status anxiety Spirit Level Wilkinson Pickett"}







,{id:"xref_social_trust_income_growth",title:"Social trust levels vs. economic growth by state over 20 years",sub:"States where people trust their neighbors more have grown faster economically. Social capital is economic capital.",type:"XREF",geo:"us_state",fmt:"Scatter plot",tbl:"T715 Â· T617",section:"Income Â· Social Insurance",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API - free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov - free)","Census Population Estimates: annual population by state/county (census.gov - free)","BLS LAUS: unemployment + labor force by state (bls.gov - free)"],vars:["state_gdp_per_capita","median_household_income"],join:["pct_on_snap","rep_pct","violent_crime_rate"],sc:{emotional:7,relatability:6,surprise:8,tension:5,visual:6,data_ready:7,originality:9},vs:70,tags:"social trust economic growth state 20 years volunteering neighbors capital Putnam Bowling Alone community development"}







,{id:"xref_nature_access_mental_health",title:"Proximity to parks and green space vs. mental health outcomes by county",sub:"Counties with more parkland per capita have measurably lower rates of depression and anxiety. Nature is medicine.",type:"XREF",geo:"us_county",fmt:"Scatter plot",tbl:"T1278 Â· T178",section:"Arts Recreation Â· Health",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API - free, tidycensus)","Census Population Estimates: annual population by state/county (census.gov - free)","BLS LAUS: unemployment + labor force by county (bls.gov - free)","CDC WONDER: mortality + disease rates by county/state (wonder.cdc.gov - free)","USDA ERS: food environment, rural classification, farm income (ers.usda.gov - free)"],vars:["national_forest_acres","per_capita_health_spending"],join:["median_household_income","state_unemployment_rate"],sc:{emotional:7,relatability:7,surprise:7,tension:4,visual:7,data_ready:7,originality:8},vs:68,tags:"nature access parks green space mental health county depression anxiety parkland medicine wellbeing outdoor"}







,{id:"flood_zone_vs_race_county",title:"FEMA flood zone overlap with minority population by county",sub:"Black and Hispanic Americans are 40% more likely to live in a FEMA flood zone than white Americans. The geography of environmental racism.",type:"XREF",geo:"us_county",fmt:"Bivariate choropleth",tbl:"T439",section:"Geography & Environment",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API - free, tidycensus)","Census Population Estimates: annual population by state/county (census.gov - free)","BLS LAUS: unemployment + labor force by county (bls.gov - free)","USDA ERS: food environment, rural classification, farm income (ers.usda.gov - free)"],vars:["coastline_miles","mean_elevation"],join:["median_household_income","pct_on_snap","rep_pct"],sc:{emotional:9,relatability:7,surprise:8,tension:9,visual:9,data_ready:7,originality:8},vs:84,tags:"flood zone race county Black Hispanic 40% more likely environmental racism FEMA climate justice geography"}







,{id:"superfund_sites_vs_race",title:"Superfund toxic waste sites proximity to minority communities",sub:"Communities within 1 mile of a Superfund site are 52% more likely to be majority-minority. Toxic waste as a race issue.",type:"MAP",geo:"us_county",fmt:"County choropleth",tbl:"T428",section:"Geography & Environment",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API - free, tidycensus)","Census Population Estimates: annual population by state/county (census.gov - free)","BLS LAUS: unemployment + labor force by county (bls.gov - free)","CDC WONDER: mortality + disease rates by county/state (wonder.cdc.gov - free)"],vars:["mean_elevation","national_forest_acres"],join:["median_household_income","pct_on_snap","violent_crime_rate"],sc:{emotional:9,relatability:6,surprise:8,tension:8,visual:9,data_ready:7,originality:7},vs:79,tags:"Superfund toxic waste minority communities 52% environmental racism proximity race income justice EPA cleanup"}







,{id:"drought_vs_agriculture_income",title:"Drought severity vs. farm income loss by county 2000-2024",sub:"Western counties in severe drought lose 35% of farm income in drought years. The climate-agriculture feedback.",type:"XREF",geo:"us_county",fmt:"Scatter plot",tbl:"T443 Â· T869",section:"Geography & Environment Â· Agriculture",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API - free, tidycensus)","Census Population Estimates: annual population by state/county (census.gov - free)","BLS LAUS: unemployment + labor force by county (bls.gov - free)","USDA ERS: food environment, rural classification, farm income (ers.usda.gov - free)"],vars:["mean_elevation","farms_count_2022"],join:["pct_cropland","median_household_income","energy_consumption_per_capita"],sc:{emotional:7,relatability:6,surprise:7,tension:7,visual:7,data_ready:7,originality:7},vs:69,tags:"drought severity farm income county 35% Western climate agriculture feedback 2000 2024 crop loss water stress"}







,{id:"air_quality_vs_asthma_race",title:"Air quality index vs. childhood asthma rate by race and neighborhood",sub:"Black children in high-pollution zip codes have asthma rates 3x higher than white children in clean-air suburbs.",type:"XREF",geo:"us_county",fmt:"Scatter plot",tbl:"T422 Â· T141",section:"Geography & Environment Â· Health",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API - free, tidycensus)","Census Population Estimates: annual population by state/county (census.gov - free)","BLS LAUS: unemployment + labor force by county (bls.gov - free)","CDC WONDER: mortality + disease rates by county/state (wonder.cdc.gov - free)"],vars:["mean_elevation","per_capita_health_spending"],join:["median_household_income","pct_on_snap","pct_on_medicaid"],sc:{emotional:9,relatability:7,surprise:7,tension:8,visual:7,data_ready:7,originality:7},vs:78,tags:"air quality asthma race childhood Black 3x white suburb clean pollution zip neighborhood environmental justice"}







,{id:"wildfire_homes_at_risk_by_state",title:"Single-family homes at wildfire risk by state",sub:"California: 2.7M homes at high or extreme wildfire risk. Colorado: 380K. The insurance crisis has a geographic cause.",type:"MAP",geo:"us_state",fmt:"State choropleth",tbl:"T441",section:"Geography & Environment",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API - free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov - free)","Census Population Estimates: annual population by state/county (census.gov - free)","BLS LAUS: unemployment + labor force by state (bls.gov - free)"],vars:["national_forest_acres","mean_elevation"],join:["home_price_index_2024","housing_permits_total","motor_vehicle_insurance_cpi"],sc:{emotional:8,relatability:8,surprise:7,tension:8,visual:9,data_ready:10,originality:7},vs:79,tags:"wildfire homes at risk state California 2.7M Colorado 380K insurance crisis geographic cause Western climate"}







,{id:"rent_vs_buy_breakeven_by_city",title:"Rent vs. buy breakeven point by city 2024",sub:"San Francisco: need to stay 11 years to break even buying vs. renting. Detroit: 2 years. The math of homeownership.",type:"RANK",geo:"top_n_list",fmt:"Ranked list",tbl:"T1025 Â· T771",section:"Housing",ext:[],vars:["home_price_index_2024","rent_primary_residence_cpi"],join:["median_household_income","housing_permits_total","mortgage_delinquency_rate"],sc:{emotional:8,relatability:9,surprise:7,tension:6,visual:8,data_ready:8,originality:7},vs:76,tags:"rent buy breakeven city 2024 San Francisco 11 years Detroit 2 years homeownership math affordability decision"}







,{id:"housing_vacancy_rate_by_state",title:"Housing vacancy rate by state 2024",sub:"Mississippi: 21% of housing units vacant. D.C.: 7%. Vermont: 21%. The vacant housing geography surprises.",type:"MAP",geo:"us_state",fmt:"State choropleth",tbl:"T1034",section:"Housing",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API - free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov - free)","Census Population Estimates: annual population by state/county (census.gov - free)","BLS LAUS: unemployment + labor force by state (bls.gov - free)","HUD Fair Market Rents + housing data by state/county (huduser.gov - free)"],vars:["home_price_index_2024","housing_permits_total"],join:["median_household_income","population_pct_change","mortgage_delinquency_rate"],sc:{emotional:7,relatability:7,surprise:8,tension:5,visual:9,data_ready:10,originality:6},vs:71,tags:"housing vacancy rate state 2024 Mississippi 21% DC 7% Vermont vacant housing geography surprising rural decline"}







,{id:"aging_in_place_housing_gap",title:"Aging-ready housing units vs. 65+ population by region",sub:"Only 4% of US housing units are accessible for older adults. But 19% of Americans are over 65. The aging-in-place gap.",type:"CHART",geo:"us_national",fmt:"Bar chart",tbl:"T1028",section:"Housing",ext:["FRED: any national economic time series (fred.stlouisfed.org - free API)","BLS national data: employment, wages, CPI (bls.gov - free API)"],vars:["home_price_index_2024"],join:["total_medicare","pct_on_medicaid","median_household_income"],sc:{emotional:8,relatability:7,surprise:8,tension:7,visual:7,data_ready:10,originality:8},vs:75,tags:"aging in place housing 4% accessible 65+ 19% gap older adults mobility wheelchair ramp bathroom grab bar"}







,{id:"new_home_size_trend",title:"Average new single-family home size 1973-2024 - the supersizing of America",sub:"Average new home: 1,525 sq ft in 1973. 2,273 in 2024. 49% larger - but household sizes shrank 25%. Americans house space, not people.",type:"CHART",geo:"us_national",fmt:"Line chart",tbl:"T1016",section:"Housing",ext:["FRED: any national economic time series (fred.stlouisfed.org - free API)","BLS national data: employment, wages, CPI (bls.gov - free API)"],vars:["housing_permits_total","home_price_index_2024"],join:["median_household_income","housing_cpi","birth_rate_state"],sc:{emotional:6,relatability:8,surprise:8,tension:4,visual:7,data_ready:10,originality:7},vs:71,tags:"new home size 1973 2024 1525 2273 sq ft 49% larger household shrunk 25% supersizing Americans space culture"}







,{id:"manufactured_homes_by_state",title:"Manufactured (mobile) home share of housing stock by state",sub:"South Carolina: 19% of homes are manufactured. New Hampshire: 5%. The affordable housing geography nobody talks about.",type:"MAP",geo:"us_state",fmt:"State choropleth",tbl:"T1023",section:"Housing",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API - free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov - free)","Census Population Estimates: annual population by state/county (census.gov - free)","BLS LAUS: unemployment + labor force by state (bls.gov - free)","HUD Fair Market Rents + housing data by state/county (huduser.gov - free)"],vars:["home_price_index_2024","housing_permits_total"],join:["median_household_income","pct_on_snap","rep_pct"],sc:{emotional:6,relatability:6,surprise:7,tension:4,visual:8,data_ready:9,originality:7},vs:65,tags:"manufactured mobile homes state South Carolina 19% New Hampshire 5% affordable housing geography rural poverty"}







,{id:"space_economy_by_sector",title:"US space industry gross output by sector 2023",sub:"Space manufacturing: $58B. Space services: $148B. Defense space: $31B. The $237B space economy breakdown.",type:"CHART",geo:"us_national",fmt:"Treemap",tbl:"T860",section:"Science",ext:["FRED: any national economic time series (fred.stlouisfed.org - free API)","BLS national data: employment, wages, CPI (bls.gov - free API)"],vars:["rd_pct_gdp"],join:["defense_budget_total","state_gdp_per_capita"],sc:{emotional:7,relatability:6,surprise:8,tension:4,visual:9,data_ready:10,originality:8},vs:71,tags:"space economy sector 2023 manufacturing $58B services $148B defense $31B $237B total breakdown gross output"}







,{id:"federal_rd_by_agency",title:"Federal R&D budget by agency 2024 - where science money goes",sub:"NIH: $47B. DOD: $130B. NASA: $9B. DOE: $22B. NSF: $9.5B. The federal science priorities in dollars.",type:"RANK",geo:"top_n_list",fmt:"Ranked list",tbl:"T841",section:"Science",ext:[],vars:["rd_pct_gdp"],join:["defense_budget_total","state_gdp_per_capita"],sc:{emotional:6,relatability:6,surprise:7,tension:5,visual:8,data_ready:10,originality:5},vs:64,tags:"federal R&D budget agency 2024 NIH $47B DOD $130B NASA DOE NSF science priorities money spending research"}







,{id:"xref_rd_spending_patent_output",title:"R&D spending vs. patents issued by state - return on investment",sub:"Some states spend heavily on R&D and produce few patents. Others punch above their weight. The innovation efficiency map.",type:"XREF",geo:"us_state",fmt:"Scatter plot",tbl:"T844 Â· T818",section:"Science",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API - free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov - free)","Census Population Estimates: annual population by state/county (census.gov - free)","BLS LAUS: unemployment + labor force by state (bls.gov - free)"],vars:["rd_pct_gdp"],join:["pct_bachelors","state_gdp_per_capita","median_household_income"],sc:{emotional:6,relatability:5,surprise:7,tension:4,visual:7,data_ready:10,originality:7},vs:64,tags:"R&D spending patents state return investment innovation efficiency punch above weight research output per dollar"}







,{id:"stem_degree_vs_stem_jobs_mismatch",title:"STEM degrees awarded vs. STEM jobs by field - the supply-demand mismatch",sub:"Computer science graduates: 90K/year. Computing job openings: 400K/year. Biology degrees: 120K. Bio jobs: 40K. The STEM mismatch.",type:"CHART",geo:"us_national",fmt:"Bar chart",tbl:"T849 Â· T855",section:"Science",ext:["FRED: any national economic time series (fred.stlouisfed.org - free API)","BLS national data: employment, wages, CPI (bls.gov - free API)"],vars:["rd_pct_gdp"],join:["pct_bachelors","state_unemployment_rate"],sc:{emotional:7,relatability:8,surprise:8,tension:5,visual:7,data_ready:9,originality:8},vs:72,tags:"STEM degrees jobs mismatch computer science 90K 400K biology 120K 40K supply demand field higher education career"}







,{id:"marriage_rate_decline_by_state",title:"Marriage rate by state 2023 vs. 1990 - the retreat from marriage",sub:"National marriage rate: 10.6 per 1,000 in 1990. 6.2 in 2023. Nevada still leads. But every state declined.",type:"MAP",geo:"us_state",fmt:"State choropleth",tbl:"T79",section:"Births Deaths",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API - free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov - free)","Census Population Estimates: annual population by state/county (census.gov - free)","BLS LAUS: unemployment + labor force by state (bls.gov - free)"],vars:["birth_rate_state","pct_births_unmarried"],join:["median_household_income","rep_pct","teen_birth_rate"],sc:{emotional:7,relatability:7,surprise:6,tension:5,visual:8,data_ready:10,originality:5},vs:68,tags:"marriage rate state 2023 1990 decline 10.6 6.2 Nevada leads retreat institution demographic cultural shift"}







,{id:"single_parent_households_by_race",title:"Single-parent household rate by race - the family structure divide",sub:"Black children: 65% live with a single parent. White: 24%. Hispanic: 42%. The family structure map of America.",type:"CHART",geo:"us_national",fmt:"Bar chart",tbl:"T93",section:"Births Deaths",ext:["FRED: any national economic time series (fred.stlouisfed.org - free API)","BLS national data: employment, wages, CPI (bls.gov - free API)"],vars:["pct_births_unmarried","birth_rate_state"],join:["pct_on_snap","median_household_income","teen_birth_rate"],sc:{emotional:8,relatability:7,surprise:6,tension:7,visual:7,data_ready:10,originality:4},vs:73,tags:"single parent household race Black 65% White 24% Hispanic 42% family structure divide America children poverty"}







,{id:"childlessness_rate_by_cohort",title:"Childless at 40 by birth year cohort - the accelerating trend",sub:"Women born in 1950: 10% childless at 40. Born in 1985: projected 27%. The voluntary childlessness trajectory.",type:"CHART",geo:"us_national",fmt:"Line chart",tbl:"T92",section:"Births Deaths",ext:["FRED: any national economic time series (fred.stlouisfed.org - free API)","BLS national data: employment, wages, CPI (bls.gov - free API)"],vars:["total_fertility_rate_by_race","birth_rate_state"],join:["median_household_income","college_tuition_cpi","home_price_index_2024"],sc:{emotional:8,relatability:8,surprise:7,tension:6,visual:7,data_ready:9,originality:7},vs:74,tags:"childless 40 birth year cohort 1950 10% 1985 27% voluntary childlessness trend demographic accelerating women"}







,{id:"ivf_usage_by_income",title:"Assisted reproductive technology usage by income level",sub:"ART usage: 5x higher in households above $100K vs. below $50K. Fertility treatment is a luxury good.",type:"CHART",geo:"us_national",fmt:"Bar chart",tbl:"T98",section:"Births Deaths",ext:["FRED: any national economic time series (fred.stlouisfed.org - free API)","BLS national data: employment, wages, CPI (bls.gov - free API)"],vars:["birth_rate_state","total_fertility_rate_by_race"],join:["median_household_income","pct_over_200k","health_insurance_cpi"],sc:{emotional:7,relatability:6,surprise:8,tension:5,visual:6,data_ready:9,originality:8},vs:68,tags:"IVF ART assisted reproductive technology income 5x luxury good fertility treatment $100K $50K class disparity"}







,{id:"nearest_grocery_drive_time_county",title:"Drive time to nearest grocery store by county",sub:"15 million Americans live more than 10 miles from a grocery store. Rural counties in the West and South worst affected.",type:"MAP",geo:"us_county",fmt:"County choropleth",tbl:"T576",section:"Agriculture",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API - free, tidycensus)","Census Population Estimates: annual population by state/county (census.gov - free)","BLS LAUS: unemployment + labor force by county (bls.gov - free)","USDA ERS: food environment, rural classification, farm income (ers.usda.gov - free)"],vars:["pct_on_snap","farms_count_2022"],join:["median_household_income","rural_population_pct","pct_cropland"],sc:{emotional:8,relatability:8,surprise:7,tension:7,visual:9,data_ready:7,originality:7},vs:76,tags:"drive time grocery store county 15 million 10 miles rural food desert West South pgRouting access food"}







,{id:"dollar_general_vs_grocery_routing",title:"Dollar General locations vs. nearest full grocery by county",sub:"In 1,200 US counties, Dollar General is closer than any full grocery store. The Dollar General as America's food system.",type:"MAP",geo:"us_county",fmt:"County choropleth",tbl:"T576",section:"Agriculture",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API - free, tidycensus)","Census Population Estimates: annual population by state/county (census.gov - free)","BLS LAUS: unemployment + labor force by county (bls.gov - free)","USDA ERS: food environment, rural classification, farm income (ers.usda.gov - free)"],vars:["pct_on_snap","retail_sales_per_capita"],join:["median_household_income","rural_population_pct","rep_pct"],sc:{emotional:9,relatability:9,surprise:9,tension:8,visual:9,data_ready:7,originality:9},vs:88,tags:"Dollar General vs grocery county 1200 counties closer full store food system rural poverty pgRouting routing"}







,{id:"va_hospital_drive_time",title:"Drive time to nearest VA hospital by county - veterans left stranded",sub:"In 280 counties, veterans must drive more than 2 hours to reach a VA hospital. The veterans access crisis.",type:"MAP",geo:"us_county",fmt:"County choropleth",tbl:"T543",section:"National Security",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API - free, tidycensus)","Census Population Estimates: annual population by state/county (census.gov - free)","BLS LAUS: unemployment + labor force by county (bls.gov - free)"],vars:["defense_budget_total","active_duty_total"],join:["median_household_income","per_capita_health_spending","rep_pct"],sc:{emotional:8,relatability:7,surprise:7,tension:7,visual:9,data_ready:6,originality:7},vs:73,tags:"VA hospital drive time county 280 counties 2 hours veterans access crisis pgRouting rural stranded healthcare"}







,{id:"trauma_center_drive_time_county",title:"Drive time to nearest Level 1 trauma center by county",sub:"In rural America, 44 million people live more than 60 minutes from a Level 1 trauma center. The golden hour geography.",type:"MAP",geo:"us_county",fmt:"County choropleth",tbl:"T185",section:"Health",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API - free, tidycensus)","Census Population Estimates: annual population by state/county (census.gov - free)","BLS LAUS: unemployment + labor force by county (bls.gov - free)","CDC WONDER: mortality + disease rates by county/state (wonder.cdc.gov - free)"],vars:["per_capita_health_spending","hospital_services_cpi"],join:["pct_on_medicaid","median_household_income","rural_population_pct"],sc:{emotional:9,relatability:7,surprise:7,tension:8,visual:9,data_ready:6,originality:7},vs:79,tags:"trauma center drive time county Level 1 44 million 60 minutes golden hour rural emergency care pgRouting"}







,{id:"dialysis_center_drive_time",title:"Drive time to nearest dialysis center vs. diabetes rate by county",sub:"High-diabetes rural counties often have the worst dialysis access. The kidney failure geography of neglect.",type:"XREF",geo:"us_county",fmt:"Scatter plot",tbl:"T141 Â· T185",section:"Health",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API - free, tidycensus)","Census Population Estimates: annual population by state/county (census.gov - free)","BLS LAUS: unemployment + labor force by county (bls.gov - free)","CDC WONDER: mortality + disease rates by county/state (wonder.cdc.gov - free)"],vars:["per_capita_health_spending","pct_on_medicaid"],join:["median_household_income","pct_on_snap","rural_population_pct"],sc:{emotional:8,relatability:5,surprise:8,tension:7,visual:6,data_ready:6,originality:8},vs:71,tags:"dialysis center drive time diabetes county rural access kidney failure neglect pgRouting healthcare geography"}







,{id:"irs_migration_flows_covid",title:"IRS tax return migration flows 2019-2022 - the great COVID reshuffling",sub:"2 million tax filers moved from NY, CA, IL. Florida, Texas, Arizona gained. The largest domestic migration since WWII.",type:"MAP",geo:"us_state",fmt:"State choropleth",tbl:"T629",section:"Population",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API - free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov - free)","Census Population Estimates: annual population by state/county (census.gov - free)","BLS LAUS: unemployment + labor force by state (bls.gov - free)"],vars:["population_pct_change"],join:["median_household_income","home_price_index_2024","rep_pct"],sc:{emotional:8,relatability:8,surprise:7,tension:6,visual:9,data_ready:8,originality:7},vs:76,tags:"IRS migration flows 2019 2022 COVID reshuffling NY CA IL Florida Texas Arizona WWII domestic migration IRS SOI"}







,{id:"snowbird_population_flow",title:"Seasonal population shifts - where snowbirds actually go",sub:"Florida gains 750,000 people November-March. Arizona: 320,000. The snowbird economy quantified.",type:"MAP",geo:"us_state",fmt:"State choropleth",tbl:"T629",section:"Population",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API - free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov - free)","Census Population Estimates: annual population by state/county (census.gov - free)","BLS LAUS: unemployment + labor force by state (bls.gov - free)"],vars:["population_pct_change"],join:["median_household_income","total_medicare","rep_pct"],sc:{emotional:6,relatability:7,surprise:7,tension:2,visual:9,data_ready:7,originality:8},vs:67,tags:"snowbirds seasonal population Florida 750000 Arizona 320000 November March winter warm climate retirement mobility"}







,{id:"college_enrollment_origin_state",title:"Where college students come from vs. where they go to school",sub:"Massachusetts exports 40% of its students. North Dakota imports 20% from other states. The education migration map.",type:"MAP",geo:"us_state",fmt:"State choropleth",tbl:"T295",section:"Education",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API - free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov - free)","Census Population Estimates: annual population by state/county (census.gov - free)","BLS LAUS: unemployment + labor force by state (bls.gov - free)"],vars:["pct_bachelors","expenditure_per_pupil"],join:["median_household_income","population_pct_change","state_gdp_per_capita"],sc:{emotional:6,relatability:7,surprise:7,tension:4,visual:8,data_ready:7,originality:8},vs:67,tags:"college enrollment origin state Massachusetts 40% North Dakota 20% import export education migration students flow"}







,{id:"retirement_savings_by_age_cohort",title:"Median retirement savings by age group 2024 - the inadequacy map",sub:"Americans 55-64 median retirement savings: $185K. Needed for 20 years: $1M+. 50% of Americans have nothing saved.",type:"CHART",geo:"us_national",fmt:"Bar chart",tbl:"T588",section:"Social Insurance",ext:["FRED: any national economic time series (fred.stlouisfed.org - free API)","BLS national data: employment, wages, CPI (bls.gov - free API)"],vars:["pct_families_own_retirement","total_transfers_per_capita"],join:["median_household_income","federal_debt_pct_gdp","total_medicare"],sc:{emotional:9,relatability:9,surprise:7,tension:9,visual:7,data_ready:9,originality:5},vs:82,tags:"retirement savings age cohort 55-64 $185K $1M needed 50% nothing saved inadequacy crisis Americans future"}







,{id:"social_security_trust_fund_depletion",title:"Social Security trust fund trajectory 2024-2035",sub:"At current trajectory, Social Security trust fund depleted by 2035. Benefits cut 17% automatically. The countdown clock.",type:"CHART",geo:"us_national",fmt:"Area chart",tbl:"T581",section:"Social Insurance",ext:["FRED: any national economic time series (fred.stlouisfed.org - free API)","BLS national data: employment, wages, CPI (bls.gov - free API)"],vars:["total_transfers_per_capita","pct_on_medicaid"],join:["federal_debt_pct_gdp","total_medicare"],sc:{emotional:9,relatability:9,surprise:7,tension:9,visual:8,data_ready:10,originality:5},vs:84,tags:"Social Security trust fund 2035 depletion 17% cut benefits countdown automatic crisis retirement seniors OASDI"}







,{id:"defined_benefit_vs_defined_contribution_shift",title:"Pension vs. 401(k) coverage 1983-2024 - the risk transfer",sub:"Private sector defined benefit pension coverage: 38% in 1983. 11% in 2024. The risk shifted from employers to workers.",type:"CHART",geo:"us_national",fmt:"Line chart",tbl:"T586",section:"Social Insurance",ext:["FRED: any national economic time series (fred.stlouisfed.org - free API)","BLS national data: employment, wages, CPI (bls.gov - free API)"],vars:["pct_families_own_retirement","pct_families_own_stocks"],join:["median_household_income","state_unemployment_rate"],sc:{emotional:8,relatability:8,surprise:7,tension:7,visual:7,data_ready:10,originality:6},vs:75,tags:"pension 401k defined benefit contribution 1983 2024 38% 11% risk transfer employers workers retirement shift"}







,{id:"xref_stock_ownership_wealth",title:"Stock ownership rate vs. median wealth by income quintile",sub:"Bottom 50%: 12% own stocks. Top 10%: 87%. The stock market is a wealth machine for those already wealthy.",type:"CHART",geo:"us_national",fmt:"Bar chart",tbl:"T1207",section:"Banking Finance Insurance",ext:["FRED: any national economic time series (fred.stlouisfed.org - free API)","BLS national data: employment, wages, CPI (bls.gov - free API)"],vars:["pct_families_own_stocks","pct_families_own_retirement"],join:["median_household_income","pct_over_200k","corporate_profits"],sc:{emotional:8,relatability:7,surprise:7,tension:8,visual:7,data_ready:9,originality:5},vs:74,tags:"stock ownership wealth income quintile bottom 50% 12% top 10% 87% market machine wealthy already rich"}







,{id:"gender_pay_gap_by_industry",title:"Gender pay gap by industry 2024 - where women earn the most and least relative to men",sub:"Financial advisors: women earn 61 cents/dollar. Healthcare: 86 cents. Education: 90 cents. The industry pay gap spectrum.",type:"RANK",geo:"us_national",fmt:"Ranked list",tbl:"T653",section:"Labor Force",ext:["FRED: any national economic time series (fred.stlouisfed.org - free API)","BLS national data: employment, wages, CPI (bls.gov - free API)"],vars:["female_lfp_rate","state_unemployment_rate"],join:["median_household_income","pct_bachelors"],sc:{emotional:8,relatability:9,surprise:7,tension:7,visual:8,data_ready:10,originality:5},vs:77,tags:"gender pay gap industry 2024 women 61 cents financial 86 cents healthcare 90 cents education spectrum inequality"}







,{id:"female_ceo_rate_by_industry",title:"Female CEO rate by industry sector 2024",sub:"Consumer staples: 24% female CEOs. Tech: 8%. Finance: 12%. Energy: 4%. The glass ceiling is industry-specific.",type:"RANK",geo:"top_n_list",fmt:"Ranked list",tbl:"T808",section:"Business Enterprise",ext:[],vars:["corporate_profits","state_gdp_per_capita"],join:["median_household_income","female_lfp_rate"],sc:{emotional:7,relatability:7,surprise:7,tension:6,visual:7,data_ready:8,originality:6},vs:68,tags:"female CEO rate industry 2024 consumer staples 24% tech 8% finance energy glass ceiling Fortune 500 sector"}







,{id:"maternal_labor_force_return",title:"Mothers returning to work by income level and child age",sub:"High-income mothers: 78% back at work when child is 1. Low-income: 52%. The childcare cost is the barrier.",type:"CHART",geo:"us_national",fmt:"Line chart",tbl:"T650",section:"Labor Force",ext:["FRED: any national economic time series (fred.stlouisfed.org - free API)","BLS national data: employment, wages, CPI (bls.gov - free API)"],vars:["female_lfp_rate","daycare_preschool_cpi"],join:["median_household_income","birth_rate_state","pct_on_snap"],sc:{emotional:8,relatability:8,surprise:6,tension:6,visual:7,data_ready:9,originality:6},vs:73,tags:"mothers return work income child age 1 78% high income 52% low income childcare cost barrier employment"}







,{id:"xref_womens_education_fertility",title:"Women's educational attainment vs. fertility rate by state",sub:"States with more college-educated women have dramatically lower fertility rates. The education-family tradeoff.",type:"XREF",geo:"us_state",fmt:"Scatter plot",tbl:"T254 Â· T85",section:"Education Â· Births Deaths",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API - free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov - free)","Census Population Estimates: annual population by state/county (census.gov - free)","BLS LAUS: unemployment + labor force by state (bls.gov - free)"],vars:["total_fertility_rate_by_race","pct_bachelors"],join:["median_household_income","birth_rate_state","female_lfp_rate"],sc:{emotional:7,relatability:7,surprise:7,tension:5,visual:7,data_ready:10,originality:6},vs:70,tags:"womens education fertility rate state college educated dramatically lower demographic transition tradeoff choice"}







,{id:"rural_hospital_closures_by_state",title:"Rural hospital closures 2010-2024 by state",sub:"180 rural hospitals closed since 2010. Texas: 26 closures. Tennessee: 14. The rural healthcare desert spreading.",type:"MAP",geo:"us_state",fmt:"State choropleth",tbl:"T190",section:"Health",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API - free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov - free)","Census Population Estimates: annual population by state/county (census.gov - free)","BLS LAUS: unemployment + labor force by state (bls.gov - free)","CDC WONDER: mortality + disease rates by county/state (wonder.cdc.gov - free)"],vars:["per_capita_health_spending","hospital_services_cpi"],join:["pct_on_medicaid","median_household_income","rep_pct"],sc:{emotional:9,relatability:7,surprise:7,tension:8,visual:9,data_ready:8,originality:7},vs:79,tags:"rural hospital closures state 2010 2024 180 Texas 26 Tennessee 14 healthcare desert spreading access mortality"}







,{id:"county_without_doctor",title:"Counties without a single practicing physician",sub:"More than 80 US counties have zero practicing physicians. An additional 450 have fewer than 5. The doctor desert.",type:"MAP",geo:"us_county",fmt:"County choropleth",tbl:"T173",section:"Health",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API - free, tidycensus)","Census Population Estimates: annual population by state/county (census.gov - free)","BLS LAUS: unemployment + labor force by county (bls.gov - free)","CDC WONDER: mortality + disease rates by county/state (wonder.cdc.gov - free)"],vars:["per_capita_health_spending"],join:["median_household_income","rural_population_pct","pct_on_medicaid"],sc:{emotional:9,relatability:7,surprise:9,tension:8,visual:9,data_ready:7,originality:7},vs:82,tags:"county no doctor zero physician 80 counties 450 fewer than 5 rural desert access healthcare crisis America"}







,{id:"rural_broadband_gap_by_county",title:"Households without broadband access by county",sub:"25 million Americans lack access to broadband. Rural counties in Appalachia and the Mississippi Delta worst affected.",type:"MAP",geo:"us_county",fmt:"County choropleth",tbl:"T1189",section:"Information",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API - free, tidycensus)","Census Population Estimates: annual population by state/county (census.gov - free)","BLS LAUS: unemployment + labor force by county (bls.gov - free)"],vars:["newspaper_print_revenue"],join:["median_household_income","pct_on_snap","rural_population_pct"],sc:{emotional:8,relatability:7,surprise:6,tension:7,visual:9,data_ready:7,originality:5},vs:73,tags:"broadband access county 25 million rural Appalachia Mississippi Delta digital divide internet infrastructure gap"}







,{id:"xref_rural_urban_life_expectancy_gap",title:"Rural vs. urban life expectancy gap 1980-2024 - the divergence",sub:"Rural-urban life expectancy gap: 1 year in 1980. 4.5 years in 2024. The gap that keeps growing despite parity myths.",type:"CHART",geo:"us_national",fmt:"Line chart",tbl:"T112",section:"Health",ext:["FRED: any national economic time series (fred.stlouisfed.org - free API)","BLS national data: employment, wages, CPI (bls.gov - free API)"],vars:["birth_rate_state"],join:["per_capita_health_spending","pct_on_medicaid","pct_on_snap"],sc:{emotional:8,relatability:7,surprise:7,tension:7,visual:7,data_ready:9,originality:7},vs:74,tags:"rural urban life expectancy gap 1980 2024 1 year 4.5 years divergence growing parity myth mortality healthcare"}







,{id:"effective_tax_rate_by_income",title:"Effective federal tax rate by income level 2023 - what people actually pay",sub:"Bottom quintile: 2.1% effective rate. Top 1%: 26.2%. Billionaires: ~8% (Buffett rule). The true tax burden chart.",type:"CHART",geo:"us_national",fmt:"Bar chart",tbl:"T535",section:"Federal Government Finances",ext:["FRED: any national economic time series (fred.stlouisfed.org - free API)","BLS national data: employment, wages, CPI (bls.gov - free API)"],vars:["income_tax_after_credits","federal_outlays_by_function"],join:["corporate_profits","pct_over_200k","median_household_income"],sc:{emotional:9,relatability:9,surprise:7,tension:9,visual:8,data_ready:9,originality:6},vs:84,tags:"effective tax rate income 2023 bottom 2.1% top 1% 26.2% billionaires 8% Buffett rule burden truth IRS"}







,{id:"state_tax_burden_regressivity",title:"State and local tax burden as % of income - most regressive to most progressive",sub:"Washington state takes 17.8% from the poorest 20% in taxes. Only 3.5% from the top 1%. The regressivity champion.",type:"RANK",geo:"us_state",fmt:"Ranked list",tbl:"T488",section:"State Govt",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API - free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov - free)","Census Population Estimates: annual population by state/county (census.gov - free)","BLS LAUS: unemployment + labor force by state (bls.gov - free)"],vars:["state_local_revenue_per_capita","lottery_revenue_per_capita"],join:["median_household_income","pct_under_25k","rep_pct"],sc:{emotional:8,relatability:8,surprise:8,tension:8,visual:8,data_ready:8,originality:7},vs:79,tags:"state local tax burden regressivity Washington 17.8% poorest 3.5% top 1% ITEP regressive progressive sales income"}







,{id:"corporate_tax_rate_effective_vs_statutory",title:"Corporate effective vs. statutory tax rate 2000-2024",sub:"Statutory rate: 35% until 2017, now 21%. Effective rate corporations actually pay: 12-15%. The loophole economy.",type:"CHART",geo:"us_national",fmt:"Line chart",tbl:"T535",section:"Federal Government Finances",ext:["FRED: any national economic time series (fred.stlouisfed.org - free API)","BLS national data: employment, wages, CPI (bls.gov - free API)"],vars:["corporate_profits","income_tax_after_credits"],join:["federal_debt_pct_gdp","federal_outlays_by_function"],sc:{emotional:8,relatability:7,surprise:8,tension:8,visual:7,data_ready:9,originality:6},vs:77,tags:"corporate tax rate effective statutory 35% 21% 12-15% loophole economy 2000 2024 TCJA cuts companies avoid"}







,{id:"irs_audit_rate_by_income",title:"IRS audit rate by income level - who gets audited",sub:"Millionaires audit rate: 2.4%. Earned Income Tax Credit filers (working poor): 1.3%. The IRS goes where it is cheapest.",type:"CHART",geo:"us_national",fmt:"Bar chart",tbl:"T794",section:"Business Enterprise",ext:["FRED: any national economic time series (fred.stlouisfed.org - free API)","BLS national data: employment, wages, CPI (bls.gov - free API)"],vars:["income_tax_after_credits","corporate_profits"],join:["median_household_income","pct_under_25k","pct_over_200k"],sc:{emotional:9,relatability:8,surprise:9,tension:9,visual:7,data_ready:10,originality:7},vs:84,tags:"IRS audit rate income millionaires 2.4% EITC 1.3% working poor cheapest enforcement disparity regressive scrutiny"}







,{id:"undocumented_population_by_state",title:"Estimated undocumented immigrant population by state",sub:"California: 2.3M undocumented. Texas: 1.7M. New York: 725K. The shadow population that powers the economy.",type:"MAP",geo:"us_state",fmt:"State choropleth",tbl:"Population PDF",section:"Population",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API - free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov - free)","Census Population Estimates: annual population by state/county (census.gov - free)","BLS LAUS: unemployment + labor force by state (bls.gov - free)"],vars:["population_pct_change","net_migration_rate"],join:["state_gdp_per_capita","median_household_income","rep_pct"],sc:{emotional:9,relatability:7,surprise:7,tension:9,visual:9,data_ready:7,originality:6},vs:79,tags:"undocumented immigrants state California 2.3M Texas 1.7M New York shadow population economy unauthorized"}







,{id:"xref_immigration_crime_rate",title:"Immigration rate vs. crime rate by state - the myth quantified",sub:"The 10 highest-immigration states have crime rates 18% BELOW the national average. The data kills the narrative.",type:"XREF",geo:"us_state",fmt:"Scatter plot",tbl:"Population PDF Â· T340",section:"Population Â· Law Enforcement",ext:["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API - free, tidycensus)","BEA Regional: GDP + personal income per capita by state (apps.bea.gov - free)","Census Population Estimates: annual population by state/county (census.gov - free)","BLS LAUS: unemployment + labor force by state (bls.gov - free)","FBI Crime Data Explorer: UCR/NIBRS by state/agency (cde.ucr.cjis.gov - free)"],vars:["violent_crime_rate","net_migration_rate"],join:["rep_pct","median_household_income","pct_bachelors"],sc:{emotional:10,relatability:8,surprise:9,tension:10,visual:7,data_ready:8,originality:8},vs:91,tags:"immigration crime rate state myth 10 highest 18% below national average data kills narrative evidence policy debate"}







,{id:"naturalization_rate_by_country",title:"Naturalization rate of immigrants by country of origin",sub:"Indian immigrants: 71% naturalize within 10 years. Mexican immigrants: 39%. The citizenship commitment varies enormously.",type:"CHART",geo:"us_national",fmt:"Bar chart",tbl:"Population PDF",section:"Population",ext:["FRED: any national economic time series (fred.stlouisfed.org - free API)","BLS national data: employment, wages, CPI (bls.gov - free API)"],vars:["net_migration_rate","population_pct_change_2020_2025"],join:["median_household_income","pct_bachelors"],sc:{emotional:6,relatability:6,surprise:7,tension:4,visual:7,data_ready:7,originality:7},vs:65,tags:"naturalization rate immigrants country India 71% Mexico 39% 10 years citizenship commitment variation integration"}







]; // end D







