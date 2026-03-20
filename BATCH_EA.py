# BATCH_EA.py — FBI Crime Data (estimated_crimes_1979_2024.csv, lee_1960_2024.csv)
# Source: FBI UCR / Crime Data Explorer — estimated_crimes_1979_2024.csv (2388 rows),
#         lee_1960_2024.csv (768K rows, agency-level officers 1960-2024)

def vs(sc):
    raw = sc['emotional']*2 + sc['relatability']*2 + sc['clarity']*2 + sc['surprise']*1.5 + sc['tension']*1 + sc['visual']*1.25 + sc['originality']*1
    base = raw / 10.75
    penalty = 1 - 0.3*(1 - sc['data_ready']/100)
    return int(base * penalty)

ideas = [
{
  "id":"fbi_violent_crime_1979_2024_state",
  "title":"Violent crime rate by state 1979–2024: the 45-year arc that nobody talks about",
  "sub":"The US violent crime rate peaked in 1991 at 758 per 100K and has fallen 52% since — but the decline was uneven by state. Some states hit new lows in 2023 while others remain at 1990s levels. The map of who improved and who didn't tracks almost perfectly with incarceration policy, not policing levels.",
  "type":"MAP","geo":"us_state","fmt":"State choropleth",
  "tbl":"FBI UCR: estimated_crimes_1979_2024.csv — violent_crime / population by state and year",
  "section":"Law Enforcement","ext":["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API - free, tidycensus)"],
  "vars":["violent_crime_rate_change_1991_2024"],"join":["incarceration_rate","poverty_rate","rep_pct"],
  "sc":{"emotional":80,"relatability":80,"clarity":80,"surprise":80,"tension":70,"visual":80,"originality":70,"data_ready":100},
  "vs":0,"tags":"violent crime rate state 1979 2024 45 year peak 1991 decline uneven incarceration policy FBI UCR",
  "notes":"","topics":["crime","history","politics","inequality","geography"],"status":"idea"
},
{
  "id":"fbi_homicide_rate_state_2024",
  "title":"Homicide rate by state 2023: the murder map that flips every assumption",
  "sub":"The five states with the highest homicide rates in 2023 are all in the South and rural Midwest — not the urban Northeast that dominates the conversation. Mississippi homicide rate is 3x New York's. The safest states by homicide are New England. The political narrative and the data point in opposite directions.",
  "type":"MAP","geo":"us_state","fmt":"State choropleth",
  "tbl":"FBI UCR: estimated_crimes_1979_2024.csv — homicide / population 2023",
  "section":"Law Enforcement","ext":["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API - free, tidycensus)","MIT Election Lab: presidential/congressional results (electionlab.mit.edu - free)"],
  "vars":["murder_rate"],"join":["rep_pct","poverty_rate","rural_population_pct","gun_ownership_rate_proxy"],
  "sc":{"emotional":90,"relatability":80,"clarity":90,"surprise":100,"tension":90,"visual":90,"originality":80,"data_ready":100},
  "vs":0,"tags":"homicide rate state 2023 Mississippi 3x New York South rural Midwest safest New England narrative flips",
  "notes":"This is one of the strongest political identity maps on the board. The South leads on homicide yet leads the 'law and order' narrative. Data is clean and current.",
  "topics":["crime","politics","geography","race","inequality","history"],"status":"idea"
},
{
  "id":"fbi_crime_trend_animated_1979_2024",
  "title":"US crime rate animated 1979–2024: watch the crime wave rise and fall in real time",
  "sub":"Every crime category — violent, property, burglary, auto theft — follows the same arc: rise through the 1980s, peak around 1990–1993, dramatic fall through 2014, then a small post-COVID uptick. Animated as a line chart, the rise and fall is one of the most dramatic public health stories of the last 50 years that most people don't know happened.",
  "type":"CHART","geo":"us_national","fmt":"Line chart",
  "tbl":"FBI UCR: estimated_crimes_1979_2024.csv — all crime categories, national totals by year",
  "section":"Law Enforcement","ext":["FRED: any national economic time series (fred.stlouisfed.org - free API)"],
  "vars":["violent_crime_rate","property_crime_rate","homicide","burglary","motor_vehicle_theft"],
  "join":["incarceration_rate","unemployment_rate","crack_epidemic_timeline"],
  "sc":{"emotional":80,"relatability":80,"clarity":90,"surprise":90,"tension":70,"visual":90,"originality":70,"data_ready":100},
  "vs":0,"tags":"US crime rate animated 1979 2024 rise fall peak 1991 1993 decline post-COVID uptick violent property line chart",
  "notes":"","topics":["crime","history","politics","economy","data"],"status":"idea"
},
{
  "id":"fbi_property_crime_vs_violent_divergence",
  "title":"Property crime and violent crime have diverged since 2014 — they used to move together",
  "sub":"From 1979 to 2014, property crime and violent crime tracked each other almost perfectly. Since 2014 they've split: property crime continued declining while violent crime plateaued then rose post-2020. The divergence suggests different drivers — economic conditions drive property crime, something else drives violence.",
  "type":"CHART","geo":"us_national","fmt":"Line chart",
  "tbl":"FBI UCR: estimated_crimes_1979_2024.csv — violent_crime vs property_crime national totals 1979-2024",
  "section":"Law Enforcement","ext":["FRED: any national economic time series (fred.stlouisfed.org - free API)"],
  "vars":["violent_crime_rate","property_crime_rate"],
  "join":["unemployment_rate","poverty_rate","housing_cost_burden"],
  "sc":{"emotional":60,"relatability":60,"clarity":80,"surprise":90,"tension":60,"visual":80,"originality":90,"data_ready":100},
  "vs":0,"tags":"property crime violent crime diverge 2014 tracked together split plateau violent post 2020 economic drivers",
  "notes":"","topics":["crime","history","economy","data","science"],"status":"idea"
},
{
  "id":"fbi_officers_per_capita_state",
  "title":"Police officers per 1,000 residents by state: the geography of over- and under-policing",
  "sub":"The states with the most police officers per capita are not the states with the most crime. Washington DC leads at 7x the national average. States with the lowest officer-to-population ratios include Oregon, Utah, and Idaho — low-crime Western states. The mismatch between officers and crime is nearly total.",
  "type":"MAP","geo":"us_state","fmt":"State choropleth",
  "tbl":"FBI LEE: lee_1960_2024.csv — officer counts 2024 by state, summed + ACS population denominators",
  "section":"Law Enforcement","ext":["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API - free, tidycensus)"],
  "vars":["police_officers_per_1000"],"join":["violent_crime_rate","poverty_rate","rep_pct","urban_population_pct"],
  "sc":{"emotional":70,"relatability":70,"clarity":80,"surprise":90,"tension":70,"visual":80,"originality":80,"data_ready":90},
  "vs":0,"tags":"police officers per capita state DC 7x national average mismatch crime geography over under policing",
  "notes":"","topics":["crime","politics","inequality","geography","race"],"status":"idea"
},
{
  "id":"fbi_female_officers_trend",
  "title":"Female police officers as share of all officers by state 2024: who is modernizing law enforcement",
  "sub":"The share of female officers nationally has grown from under 5% in 1980 to about 13% in 2024. But the state-by-state variation is enormous: some agencies top 25% female while rural Southern departments are still under 5%. The pattern tracks education levels, not crime rates or political affiliation in the way you'd expect.",
  "type":"MAP","geo":"us_state","fmt":"State choropleth",
  "tbl":"FBI LEE: lee_1960_2024.csv — female_officer_ct / officer_ct by state 2024",
  "section":"Law Enforcement","ext":["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API - free, tidycensus)"],
  "vars":["female_officer_share"],"join":["pct_bachelors","urban_population_pct","rep_pct"],
  "sc":{"emotional":70,"relatability":70,"clarity":80,"surprise":70,"tension":50,"visual":70,"originality":70,"data_ready":90},
  "vs":0,"tags":"female police officers share state 2024 5 percent 1980 13 percent 2024 variation rural Southern education",
  "notes":"","topics":["gender","crime","labor","history","geography"],"status":"idea"
},
{
  "id":"fbi_burglary_collapse",
  "title":"Burglary has collapsed 80% since 1980 — nobody noticed because nobody reports on crime going down",
  "sub":"US burglary peaked at 3.8 million incidents in 1980. In 2023 it was 748K — a 80% decline over 43 years. Home security systems, neighborhood watch, and changing drug markets explain most of it. This is one of the great untold success stories of American public safety that gets zero coverage because good news doesn't trend.",
  "type":"CHART","geo":"us_national","fmt":"Line chart",
  "tbl":"FBI UCR: estimated_crimes_1979_2024.csv — burglary totals 1979-2024",
  "section":"Law Enforcement","ext":["FRED: any national economic time series (fred.stlouisfed.org - free API)"],
  "vars":["burglary"],"join":["home_security_adoption","crack_epidemic_timeline","population"],
  "sc":{"emotional":70,"relatability":80,"clarity":90,"surprise":100,"tension":50,"visual":80,"originality":80,"data_ready":100},
  "vs":0,"tags":"burglary 80 percent decline 1980 2023 peak 3.8 million 748K home security untold success good news",
  "notes":"","topics":["crime","history","technology","humor","data"],"status":"idea"
},
{
  "id":"fbi_hate_crimes_trend_2000_2024",
  "title":"Hate crimes reported to the FBI 2000–2024: the data behind the debate",
  "sub":"FBI hate crime reporting shows a clear spike in 2020-2021 that has partially receded. But the data has a massive asterisk: fewer than 15% of agencies fully report, and participation has actually increased over time — so part of the trend is more reporting, not more crimes. This is a story about data quality as much as actual hate.",
  "type":"CHART","geo":"us_national","fmt":"Line chart",
  "tbl":"FBI hate_crime.zip: hate crime incidents by year, motivation, and victim type 2000-2024",
  "section":"Law Enforcement","ext":["FBI: ucr_participation_1960_2024.csv — reporting agency count by year"],
  "vars":["hate_crime_incidents","hate_crime_reporting_agencies"],
  "join":["rep_pct","social_media_usage","ucr_participation_rate"],
  "sc":{"emotional":80,"relatability":70,"clarity":80,"surprise":80,"tension":80,"visual":70,"originality":80,"data_ready":90},
  "vs":0,"tags":"hate crimes FBI 2000 2024 spike 2020 2021 15 percent agencies report data quality participation reporting",
  "notes":"","topics":["crime","politics","race","media","data","history"],"status":"idea"
},
{
  "id":"fbi_auto_theft_spike_2020_2024",
  "title":"Auto theft spiked 104% from 2019 to 2023 — the Hyundai TikTok challenge in the data",
  "sub":"Motor vehicle theft fell steadily from 1991 to 2019 then doubled in four years. The Hyundai/Kia theft vulnerability (exposed on TikTok in 2021) explains much of the spike — those two brands accounted for over 50% of new thefts in some cities. One viral social media trend reversed 30 years of decline in a single metric.",
  "type":"CHART","geo":"us_national","fmt":"Line chart",
  "tbl":"FBI UCR: estimated_crimes_1979_2024.csv — motor_vehicle_theft 1979-2024",
  "section":"Law Enforcement","ext":["FRED: any national economic time series (fred.stlouisfed.org - free API)"],
  "vars":["motor_vehicle_theft"],"join":["hyundai_kia_market_share","tiktok_adoption_rate"],
  "sc":{"emotional":80,"relatability":90,"clarity":90,"surprise":100,"tension":60,"visual":80,"originality":90,"data_ready":100},
  "vs":0,"tags":"auto theft spike 104 percent 2019 2023 Hyundai Kia TikTok challenge vulnerability 30 years decline reversed viral",
  "notes":"One viral social media post reversed 30 years of a federal crime statistic. The hook writes itself.",
  "topics":["crime","technology","media","history","humor","data"],"status":"idea"
},
{
  "id":"fbi_crime_rank_state_vs_perception",
  "title":"How safe do people feel vs. how safe they actually are by state: the perception-reality gap",
  "sub":"Gallup surveys show that Americans consistently overestimate local crime rates, and the overestimation is highest in low-crime states. New Hampshire residents feel less safe than Louisianans, despite having a homicide rate 8x lower. The gap between perceived safety and actual safety tracks with media consumption patterns, not crime statistics.",
  "type":"XREF","geo":"us_state","fmt":"Scatter plot",
  "tbl":"FBI UCR: estimated_crimes_1979_2024.csv + Gallup: crime perception surveys by state",
  "section":"Law Enforcement","ext":["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API - free, tidycensus)"],
  "vars":["violent_crime_rate","crime_perception_index"],
  "join":["local_news_consumption","rep_pct","median_household_income"],
  "sc":{"emotional":80,"relatability":90,"clarity":80,"surprise":90,"tension":70,"visual":80,"originality":80,"data_ready":70},
  "vs":0,"tags":"perception reality gap crime state Gallup feel safe actual safe New Hampshire Louisiana 8x lower media consumption",
  "notes":"","topics":["crime","media","politics","psychology","geography","data"],"status":"idea"
},
]

for idea in ideas:
    idea['vs'] = vs(idea['sc'])
