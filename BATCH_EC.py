# BATCH_EC.py — Our World in Data (population, political regime, prison, undernourishment,
#               CO2, internet, electricity, life expectancy, military spending, research spending)

def vs(sc):
    raw = sc['emotional']*2 + sc['relatability']*2 + sc['clarity']*2 + sc['surprise']*1.5 + sc['tension']*1 + sc['visual']*1.25 + sc['originality']*1
    base = raw / 10.75
    penalty = 1 - 0.3*(1 - sc['data_ready']/100)
    return int(base * penalty)

ideas = [
{
  "id":"owid_political_regime_change_2000_2025",
  "title":"Every country that became more autocratic since 2000 vs. every country that democratized: the great backslide mapped",
  "sub":"OWID's political regime dataset (V-Dem based, 1789–present) shows 42 countries scored lower on democracy in 2024 than in 2000. Only 14 improved significantly. The backsliders include Hungary, Turkey, India, Tunisia, and Bangladesh. The improvers include Armenia, The Gambia, and Zambia. The world's democratic regression is a matter of measurable record.",
  "type":"MAP","geo":"worldwide","fmt":"World choropleth",
  "tbl":"OWID: political-regime/political-regime.csv — Political regime score by country and year 0-3 scale",
  "section":"Elections","ext":["V-Dem: democracy indices (v-dem.net - free for research)"],
  "vars":["political_regime_change_2000_2024"],
  "join":["gdp_per_capita","press_freedom_index","incarceration_rate"],
  "sc":{"emotional":80,"relatability":70,"clarity":80,"surprise":80,"tension":90,"visual":90,"originality":70,"data_ready":100},
  "vs":0,"tags":"autocratic democratic 2000 2025 backslide Hungary Turkey India Tunisia improvers Armenia Gambia Zambia V-Dem",
  "notes":"","topics":["democracy","international","politics","history","geography"],"status":"idea"
},
{
  "id":"owid_prison_population_rate_world",
  "title":"Prison population rate by country 2023: the US outlier has company it doesn't want",
  "sub":"The US incarcerates 639 people per 100K — more than Russia (328), more than China (121), more than any Western democracy by 5x or more. But the company the US keeps is revealing: El Salvador (900+, post-Bukele), Turkmenistan, Cuba, and Rwanda. The US clusters with authoritarian states, not peer democracies, on this metric.",
  "type":"MAP","geo":"worldwide","fmt":"World choropleth",
  "tbl":"OWID: prison-population-rate/prison-population-rate.csv — Prison population rate per 100K by country and year",
  "section":"Law Enforcement","ext":["World Prison Brief: prisonstudies.org (free)"],
  "vars":["prison_population_rate"],"join":["political_regime","gdp_per_capita","violent_crime_rate_world"],
  "sc":{"emotional":80,"relatability":70,"clarity":90,"surprise":90,"tension":80,"visual":90,"originality":70,"data_ready":100},
  "vs":0,"tags":"prison population rate US 639 per 100K Russia 328 China 121 El Salvador Turkmenistan Cuba Rwanda authoritarian peer democracies",
  "notes":"","topics":["crime","inequality","politics","international","history","law"],"status":"idea"
},
{
  "id":"owid_young_working_elderly_projections",
  "title":"Young vs. working vs. elderly population ratio by country 2024–2100: the dependency time bomb mapped",
  "sub":"Japan, South Korea, and Southern Europe are entering a zone where the elderly population will outnumber the working-age population. Sub-Saharan Africa is going the opposite direction — exploding youth bulge with the fastest-growing working-age population on Earth. The two trajectories will define geopolitics, migration pressure, and economic power for the rest of the century.",
  "type":"MAP","geo":"worldwide","fmt":"World choropleth",
  "tbl":"OWID: population-young-working-elderly-with-projections.csv — dependency ratios by country 2024-2100",
  "section":"Population","ext":["UN DESA: World Population Prospects 2024 (population.un.org - free)"],
  "vars":["old_age_dependency_ratio","youth_dependency_ratio","working_age_population_share"],
  "join":["fertility_rate","immigration_rate","pension_system_funded_ratio"],
  "sc":{"emotional":80,"relatability":70,"clarity":80,"surprise":80,"tension":80,"visual":100,"originality":70,"data_ready":100},
  "vs":0,"tags":"young working elderly dependency ratio Japan South Korea Southern Europe elderly outnumber Sub-Saharan Africa youth bulge 2100",
  "notes":"","topics":["population","international","demographics","history","economy","geography"],"status":"idea"
},
{
  "id":"owid_fertility_rate_projections_2100",
  "title":"Fertility rate by country 2024 with projections to 2100: who is still having children",
  "sub":"South Korea's fertility rate hit 0.72 in 2023 — the lowest ever recorded for a major country. Niger is at 6.8. The gap between the two is 9.4 children per woman per generation. OWID projects this gap to narrow by 2100 but never close. The demographic futures of these two countries are so different they barely share a planet.",
  "type":"MAP","geo":"worldwide","fmt":"World choropleth",
  "tbl":"OWID: fertility-rate-with-projections/children-born-per-woman.csv — TFR by country 1800-2100",
  "section":"Population","ext":["UN DESA: World Population Prospects 2024 (population.un.org - free)"],
  "vars":["total_fertility_rate"],"join":["gdp_per_capita","female_education_years","urbanization_rate","infant_mortality"],
  "sc":{"emotional":80,"relatability":70,"clarity":90,"surprise":80,"tension":70,"visual":90,"originality":60,"data_ready":100},
  "vs":0,"tags":"fertility rate South Korea 0.72 Niger 6.8 gap 9.4 children per woman projections 2100 demographic futures different planet",
  "notes":"","topics":["population","international","demographics","history","education","geography"],"status":"idea"
},
{
  "id":"owid_co2_per_capita_vs_cumulative",
  "title":"CO2 per capita today vs. cumulative historical emissions: who caused the problem vs. who emits now",
  "sub":"Qatar and UAE lead current per-capita emissions. But when you look at cumulative historical emissions since 1750, the UK emitted more per capita than China ever has today. The countries most vulnerable to climate change — Bangladesh, Pacific Islands, Sub-Saharan Africa — contributed least historically and emit least today. The geography of cause and consequence almost perfectly misaligns.",
  "type":"XREF","geo":"worldwide","fmt":"Scatter plot",
  "tbl":"OWID: co-emissions-per-capita.zip — CO2 per capita + cumulative emissions by country 1750-2024",
  "section":"Geography","ext":["Global Carbon Project: globalcarbonproject.org (free)"],
  "vars":["co2_per_capita","cumulative_co2_emissions_per_capita"],
  "join":["climate_vulnerability_index","gdp_per_capita","sea_level_exposure"],
  "sc":{"emotional":90,"relatability":70,"clarity":80,"surprise":90,"tension":90,"visual":80,"originality":80,"data_ready":100},
  "vs":0,"tags":"CO2 per capita cumulative historical Qatar UAE UK China Bangladesh Pacific Islands misaligns cause consequence vulnerability",
  "notes":"","topics":["climate","inequality","international","history","geography","data","environment"],"status":"idea"
},
{
  "id":"owid_electricity_by_source_country",
  "title":"How every country generates electricity in 2023: the energy transition mapped globally",
  "sub":"France gets 70% of its electricity from nuclear. Iceland gets 100% from geothermal and hydro. Poland gets 70% from coal. Norway gets 90% from hydro. The variation within Europe alone tells the story of different path dependencies, resource endowments, and political choices. The global energy mix is not converging — it's diverging along cultural and geographic fault lines.",
  "type":"MAP","geo":"worldwide","fmt":"World choropleth",
  "tbl":"OWID: electricity-prod-source-stacked.zip — electricity generation by source (coal, gas, nuclear, solar, wind, hydro, other) by country 2023",
  "section":"Energy","ext":["IEA: World Energy Statistics (iea.org - some free data)"],
  "vars":["electricity_share_renewable","electricity_share_nuclear","electricity_share_coal"],
  "join":["co2_per_capita","gdp_per_capita","carbon_price"],
  "sc":{"emotional":60,"relatability":70,"clarity":90,"surprise":80,"tension":60,"visual":100,"originality":70,"data_ready":100},
  "vs":0,"tags":"electricity source country 2023 France nuclear Iceland geothermal Poland coal Norway hydro diverging cultural geographic path dependency",
  "notes":"","topics":["energy","international","climate","geography","history","data"],"status":"idea"
},
{
  "id":"owid_internet_access_vs_gdp_trend",
  "title":"Internet access rate by country 2000–2024: the fastest technology adoption in human history",
  "sub":"Global internet adoption went from 7% in 2000 to 67% in 2024 — adding 5.4 billion people in 24 years. No technology has ever spread this fast across this many people. Sub-Saharan Africa went from under 1% to 37%. The countries still below 20% access cluster around the conflict states and the poorest agricultural economies — the digital divide is increasingly a governance divide.",
  "type":"MAP","geo":"worldwide","fmt":"World choropleth",
  "tbl":"OWID: share-of-individuals-using-the-internet.zip — internet access % by country 1990-2024",
  "section":"Information","ext":["ITU: ICT data (itu.int - free)"],
  "vars":["internet_access_pct"],"join":["gdp_per_capita","political_regime","mobile_penetration"],
  "sc":{"emotional":70,"relatability":80,"clarity":90,"surprise":80,"tension":50,"visual":90,"originality":60,"data_ready":100},
  "vs":0,"tags":"internet access 7 percent 2000 67 percent 2024 5.4 billion fastest adoption Sub-Saharan Africa digital divide governance",
  "notes":"","topics":["technology","international","history","inequality","data","geography"],"status":"idea"
},
{
  "id":"owid_military_spending_gdp_trend",
  "title":"Military spending as % of GDP by country 2024 vs. 1990: who rearmed after Ukraine",
  "sub":"Ukraine triggered a global military spending surge. Germany crossed 2% NATO target for the first time ever in 2024. Poland now spends 4% — the highest in NATO. Meanwhile Japan doubled its defense budget, breaking a 70-year post-WWII cap. The OWID SIPRI data shows the peace dividend of the 1990s being completely unwound in under five years.",
  "type":"MAP","geo":"worldwide","fmt":"World choropleth",
  "tbl":"OWID: military-spending-as-a-share-of-gdp-sipri.zip — military spending % GDP by country 1988-2024",
  "section":"National Security","ext":["SIPRI: sipri.org/databases/milex (free)"],
  "vars":["military_spending_pct_gdp"],"join":["nato_member","proximity_to_russia","political_regime"],
  "sc":{"emotional":70,"relatability":70,"clarity":80,"surprise":80,"tension":80,"visual":90,"originality":70,"data_ready":100},
  "vs":0,"tags":"military spending GDP 2024 1990 Ukraine Germany 2 percent Poland 4 percent NATO Japan doubled post-WWII cap peace dividend unwound",
  "notes":"","topics":["military","international","war","history","politics","geography"],"status":"idea"
},
{
  "id":"owid_extreme_poverty_decline",
  "title":"Share of population in extreme poverty by region 1820–2024: the greatest story never told",
  "sub":"In 1820, 84% of the world lived in extreme poverty. In 2024 it's under 9%. The fastest decline happened in East Asia (China primarily) between 1980 and 2010. Sub-Saharan Africa is the last major region still above 35%. This is arguably the most important positive trend in human history and receives almost no media coverage because progress doesn't trend.",
  "type":"CHART","geo":"worldwide","fmt":"Line chart",
  "tbl":"OWID: share-of-population-in-extreme-poverty.zip — extreme poverty % by region and country 1820-2024",
  "section":"Income","ext":["World Bank: PovcalNet / Poverty and Inequality Platform (pip.worldbank.org - free)"],
  "vars":["extreme_poverty_rate"],"join":["gdp_per_capita","trade_openness","urbanization_rate"],
  "sc":{"emotional":80,"relatability":70,"clarity":90,"surprise":90,"tension":60,"visual":90,"originality":70,"data_ready":100},
  "vs":0,"tags":"extreme poverty 84 percent 1820 9 percent 2024 East Asia China fastest decline Sub-Saharan Africa most important positive trend history",
  "notes":"","topics":["poverty","international","history","economy","data","inequality"],"status":"idea"
},
{
  "id":"owid_research_spending_gdp",
  "title":"R&D spending as % of GDP by country 2024: who is investing in the future",
  "sub":"Israel leads the world at 6.3% of GDP on R&D. South Korea is at 5.2%. The US is at 3.5% — below both Asian innovation leaders. Germany is at 3.1%, France at 2.2%, UK at 1.7%. China crossed 2.5% in 2023 and is accelerating. Among large economies, the US is being lapped on research investment as a share of economic output — not on absolute dollars.",
  "type":"MAP","geo":"worldwide","fmt":"World choropleth",
  "tbl":"OWID: research-spending-gdp/research-spending-gdp.csv — R&D % GDP by country and year",
  "section":"Science","ext":["OECD: Main Science and Technology Indicators (oecd.org - free)"],
  "vars":["rd_pct_gdp"],"join":["patent_output","gdp_per_capita","ai_investment_index"],
  "sc":{"emotional":60,"relatability":60,"clarity":90,"surprise":80,"tension":70,"visual":80,"originality":70,"data_ready":100},
  "vs":0,"tags":"R&D spending GDP Israel 6.3 South Korea 5.2 US 3.5 Germany France UK China 2.5 accelerating lapped absolute dollars",
  "notes":"","topics":["science","technology","international","economy","history","data"],"status":"idea"
},
]

for idea in ideas:
    idea['vs'] = vs(idea['sc'])
