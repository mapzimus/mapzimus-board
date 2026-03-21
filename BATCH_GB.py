"""
BATCH_GB.py — Idea injection from D:\raw_data non-Kaggle sources
Sources: FiveThirtyEight, FBI, CPI/PPI, Sage Data, Our World In Data,
         World Cup, Public Schools, Airbnb Boston, MBTA, Walkability Index
Run: cd D:\projects\mapzimus-board && $py BATCH_GB.py && $py maintain.py
"""
import re, os, sys

DATA_JS = r"D:\projects\mapzimus-board\data.js"

# v4 algorithm
def mk(id,title,sub,typ,geo,fmt,sect,tbl,e,r,c,s,t,v,o,dr):
    raw=e*2+r*2+c*1.25+s*1.5+t*1.5+v*2.0+o*1.5
    vs=int((raw/11.75)*(1-0.5*(1-dr/100)))
    return ('{id:"'+id+'",title:"'+title+'",sub:"'+sub+'",type:"'+typ+'",'
            'geo:"'+geo+'",fmt:"'+fmt+'",section:"'+sect+'",tbl:"'+tbl+'",'
            'sc:{emotional:'+str(e)+',relatability:'+str(r)+',clarity:'+str(c)
            +',surprise:'+str(s)+',tension:'+str(t)+',visual:'+str(v)
            +',originality:'+str(o)+',data_ready:'+str(dr)+'}'
            ',vs:'+str(vs)+',topics:[],ext:[],status:"idea",notes:""}')

ideas = []

# ============================================================
# FIVETHIRTYEIGHT — bad-drivers.csv (51 states, fatal collisions)
# ============================================================
ideas.append(mk("fte_bad_drivers_speeding_by_state","States Where Speeders Kill the Most","The percentage of fatal crashes involving speeding varies wildly by state","MAP","us_state","State choropleth","Crime and Law Enforcement","FiveThirtyEight bad-drivers.csv https://github.com/fivethirtyeight/data/tree/master/bad-drivers",70,85,80,60,55,80,55,95))
ideas.append(mk("fte_bad_drivers_drunk_by_state","Americas Drunkest Drivers by State","Which states have the highest share of alcohol-impaired fatal crashes","MAP","us_state","State choropleth","Crime and Law Enforcement","FiveThirtyEight bad-drivers.csv https://github.com/fivethirtyeight/data/tree/master/bad-drivers",75,85,80,65,70,80,55,95))
ideas.append(mk("fte_bad_drivers_insurance_premiums","Car Insurance Premiums vs Crash Rates by State","Do states with more dangerous drivers actually pay more for insurance","XREF","us_state","Scatter plot","Economy","FiveThirtyEight bad-drivers.csv https://github.com/fivethirtyeight/data/tree/master/bad-drivers",55,80,75,70,50,65,70,95))
ideas.append(mk("fte_bad_drivers_no_previous_accidents","States Where First-Time Crashers Kill","Share of fatal collisions where the driver had zero prior accidents","MAP","us_state","State choropleth","Crime and Law Enforcement","FiveThirtyEight bad-drivers.csv https://github.com/fivethirtyeight/data/tree/master/bad-drivers",65,75,75,70,55,75,60,95))

# ============================================================
# FIVETHIRTYEIGHT — hate_crimes.csv (51 states, socioeconomic + hate crime rates)
# ============================================================
ideas.append(mk("fte_hate_crimes_by_state","Hate Crimes per Capita by State","The states with the highest reported hate crime rates might surprise you","MAP","us_state","State choropleth","Crime and Law Enforcement","FiveThirtyEight hate_crimes.csv https://github.com/fivethirtyeight/data/tree/master/hate-crimes",85,80,80,75,85,80,55,95))
ideas.append(mk("fte_hate_crimes_vs_trump_vote","Hate Crimes vs Trump Vote Share","Do states that voted more heavily for Trump have higher hate crime rates","XREF","us_state","Scatter plot","Crime and Law Enforcement","FiveThirtyEight hate_crimes.csv https://github.com/fivethirtyeight/data/tree/master/hate-crimes",80,75,75,80,90,65,75,95))
ideas.append(mk("fte_hate_crimes_vs_inequality","Hate Crime Rates vs Income Inequality","States with higher Gini coefficients report more hate crimes per capita","XREF","us_state","Scatter plot","Crime and Law Enforcement","FiveThirtyEight hate_crimes.csv https://github.com/fivethirtyeight/data/tree/master/hate-crimes",75,70,75,80,80,65,75,95))
ideas.append(mk("fte_hate_crimes_vs_education","Hate Crimes and Education Levels by State","Does higher education actually correlate with fewer hate crimes","XREF","us_state","Scatter plot","Crime and Law Enforcement","FiveThirtyEight hate_crimes.csv https://github.com/fivethirtyeight/data/tree/master/hate-crimes",65,75,70,75,75,60,70,95))

# ============================================================
# FIVETHIRTYEIGHT — drinks.csv (193 countries, alcohol by type)
# ============================================================
ideas.append(mk("fte_beer_consumption_world","The Worlds Biggest Beer Drinkers","Beer servings per capita by country - who drinks the most","MAP","worldwide","World choropleth","Food & Nutrition","FiveThirtyEight drinks.csv https://github.com/fivethirtyeight/data/tree/master/alcohol-consumption",70,80,85,60,40,85,50,95))
ideas.append(mk("fte_wine_vs_spirits_world","Wine Countries vs Spirit Countries","Which nations prefer wine and which prefer hard liquor","MAP","worldwide","World choropleth","Food & Nutrition","FiveThirtyEight drinks.csv https://github.com/fivethirtyeight/data/tree/master/alcohol-consumption",60,75,80,70,40,85,65,95))
ideas.append(mk("fte_total_alcohol_world","Total Pure Alcohol Consumption by Country","Liters of pure alcohol consumed per capita across the world","MAP","worldwide","World choropleth","Food & Nutrition","FiveThirtyEight drinks.csv https://github.com/fivethirtyeight/data/tree/master/alcohol-consumption",65,80,85,55,45,85,45,95))

# ============================================================
# FIVETHIRTYEIGHT — drug-use-by-age.csv
# ============================================================
ideas.append(mk("fte_drug_use_by_age","Drug Use Peaks at 20 Then Drops Off a Cliff","Usage rates for every major substance by age group","CHART","us_national","Area chart","Health","FiveThirtyEight drug-use-by-age.csv https://github.com/fivethirtyeight/data/tree/master/drug-use-by-age",75,85,80,65,60,70,55,95))
ideas.append(mk("fte_cocaine_vs_marijuana_by_age","Marijuana vs Cocaine Use by Age","When does cocaine use overtake marijuana frequency","CHART","us_national","Line chart","Health","FiveThirtyEight drug-use-by-age.csv https://github.com/fivethirtyeight/data/tree/master/drug-use-by-age",65,80,75,70,60,65,60,95))

# ============================================================
# FIVETHIRTYEIGHT — airline-safety.csv
# ============================================================
ideas.append(mk("fte_airline_safety_85_vs_00","Airlines That Got Safer (and Didnt)","Fatal accidents per airline: 1985-1999 vs 2000-2014","CHART","worldwide","Bar chart","Transportation","FiveThirtyEight airline-safety.csv https://github.com/fivethirtyeight/data/tree/master/airline-safety",70,75,80,65,55,70,60,95))
ideas.append(mk("fte_deadliest_airlines","The Deadliest Airlines in Modern History","Total fatalities by airline from 1985 to 2014","RANK","worldwide","Bar chart","Transportation","FiveThirtyEight airline-safety.csv https://github.com/fivethirtyeight/data/tree/master/airline-safety",75,70,85,70,65,65,55,95))

# ============================================================
# FIVETHIRTYEIGHT — cousin-marriage-data.csv (70 countries)
# ============================================================
ideas.append(mk("fte_cousin_marriage_world","Where Marrying Your Cousin Is Normal","Consanguinity rates range from 0.1% to 65.8% worldwide","MAP","worldwide","World choropleth","Demographics","FiveThirtyEight cousin-marriage-data.csv https://github.com/fivethirtyeight/data/tree/master/cousin-marriage",65,70,80,90,75,85,80,95))

# ============================================================
# FIVETHIRTYEIGHT — candy-data.csv (85 candies ranked)
# ============================================================
ideas.append(mk("fte_best_candy_in_america","Americas Favorite Halloween Candy Ranked","Win percentage for 85 candies based on 269K head-to-head matchups","RANK","us_national","Bar chart","Entertainment","FiveThirtyEight candy-data.csv https://github.com/fivethirtyeight/data/tree/master/candy-power-ranking",50,90,85,55,30,65,50,95))
ideas.append(mk("fte_chocolate_vs_fruity","Chocolate vs Fruity Candy: The Data","Americans overwhelmingly prefer chocolate-based candy in blind tests","CHART","us_national","Bar chart","Entertainment","FiveThirtyEight candy-data.csv https://github.com/fivethirtyeight/data/tree/master/candy-power-ranking",45,90,80,55,35,65,55,95))

# ============================================================
# FIVETHIRTYEIGHT — biopics.csv (761 films)
# ============================================================
ideas.append(mk("fte_biopics_race_gender","Who Gets a Biopic? Race and Gender in Hollywood","Only 10% of biopic subjects are people of color","CHART","worldwide","Bar chart","Entertainment","FiveThirtyEight biopics.csv https://github.com/fivethirtyeight/data/tree/master/biopics",80,70,75,75,80,60,70,95))

# ============================================================
# FIVETHIRTYEIGHT — classic-rock-song-list.csv
# ============================================================
ideas.append(mk("fte_most_played_classic_rock","The Most Overplayed Classic Rock Songs in America","2,229 songs tracked across radio stations - some play 142 times","RANK","us_national","Bar chart","Entertainment","FiveThirtyEight classic-rock-song-list.csv https://github.com/fivethirtyeight/data/tree/master/classic-rock",50,85,80,55,30,55,50,95))

# ============================================================
# FIVETHIRTYEIGHT — college major data (recent-grads, all-ages, women-stem)
# ============================================================
ideas.append(mk("fte_highest_earning_majors","College Majors That Actually Pay","Median earnings by major - engineering dominates but some surprises","RANK","us_national","Bar chart","Economy","FiveThirtyEight recent-grads.csv https://github.com/fivethirtyeight/data/tree/master/college-majors",65,90,85,60,45,60,45,95))
ideas.append(mk("fte_women_in_stem_majors","The Gender Gap in STEM Majors","Share of women in each STEM field - some fields are 80% male","CHART","us_national","Bar chart","Demographics","FiveThirtyEight women-stem.csv https://github.com/fivethirtyeight/data/tree/master/college-majors",75,80,80,60,65,65,50,95))
ideas.append(mk("fte_unemployment_by_major","Which College Degrees Leave You Jobless","Unemployment rates vary 10x between the best and worst majors","RANK","us_national","Bar chart","Labor","FiveThirtyEight recent-grads.csv https://github.com/fivethirtyeight/data/tree/master/college-majors",70,90,80,70,55,60,50,95))

# ============================================================
# FIVETHIRTYEIGHT — movies.csv (Bechdel test, 1794 films)
# ============================================================
ideas.append(mk("fte_bechdel_test_by_year","The Bechdel Test Over Time","What share of Hollywood films pass the basic women-talking test each year","CHART","worldwide","Line chart","Entertainment","FiveThirtyEight movies.csv https://github.com/fivethirtyeight/data/tree/master/bechdel",75,70,75,65,70,60,65,95))
ideas.append(mk("fte_bechdel_vs_box_office","Do Bechdel-Passing Films Make More Money","Comparing box office revenue for films that pass vs fail the Bechdel test","XREF","worldwide","Bar chart","Entertainment","FiveThirtyEight movies.csv https://github.com/fivethirtyeight/data/tree/master/bechdel",70,70,70,75,65,55,70,95))

# ============================================================
# FIVETHIRTYEIGHT — US births (1994-2014)
# ============================================================
ideas.append(mk("fte_births_day_of_week","Americans Avoid Having Babies on Weekends","Birth rates by day of week show a massive weekday spike from scheduled C-sections","CHART","us_national","Line chart","Demographics","FiveThirtyEight US_births CSVs https://github.com/fivethirtyeight/data/tree/master/births",60,80,80,75,40,65,60,95))

# ============================================================
# FIVETHIRTYEIGHT — election deniers (552 candidates)
# ============================================================
ideas.append(mk("fte_election_deniers_map","Every Election Denier Who Ran for Office in 2022","552 candidates mapped by state and their stance on the 2020 election","MAP","us_state","State choropleth","Elections","FiveThirtyEight fivethirtyeight_election_deniers.csv https://github.com/fivethirtyeight/data/tree/master/election-deniers",80,75,80,65,90,75,60,95))

# ============================================================
# FIVETHIRTYEIGHT — mmsa-icu-beds.csv (ICU capacity by metro)
# ============================================================
ideas.append(mk("fte_icu_beds_per_at_risk","ICU Beds vs At-Risk Population by Metro","Some metros have 4,500 high-risk people per ICU bed","MAP","us_metro","Dot map","Health","FiveThirtyEight mmsa-icu-beds.csv https://github.com/fivethirtyeight/data/tree/master/covid-geography",80,80,75,70,70,75,60,95))

# ============================================================
# FBI — estimated_crimes_1979_2024.csv (2,388 rows by state/year)
# ============================================================
ideas.append(mk("fbi_violent_crime_trend_1979_2024","45 Years of Violent Crime in America","How violent crime rose through the 90s crack epidemic then steadily fell","CHART","us_national","Line chart","Crime and Law Enforcement","FBI UCR estimated_crimes_1979_2024.csv https://cde.ucr.cjis.gov",80,80,85,55,70,70,50,95))
ideas.append(mk("fbi_murder_rate_by_state_2024","Murder Rates by State in 2024","Homicide per 100K varies 10x between the safest and most dangerous states","MAP","us_state","State choropleth","Crime and Law Enforcement","FBI UCR estimated_crimes_1979_2024.csv https://cde.ucr.cjis.gov",85,85,85,60,80,85,50,95))
ideas.append(mk("fbi_robbery_vs_burglary_trend","Robbery Fell But Burglary Fell Faster","Property crime and violent crime have diverged dramatically since 1990","CHART","us_national","Line chart","Crime and Law Enforcement","FBI UCR estimated_crimes_1979_2024.csv https://cde.ucr.cjis.gov",55,70,80,65,55,65,55,95))
ideas.append(mk("fbi_crime_drop_biggest_states","Which States Saw the Biggest Crime Drop","Change in violent crime rate from peak 1990s to 2024 by state","MAP","us_state","State choropleth","Crime and Law Enforcement","FBI UCR estimated_crimes_1979_2024.csv https://cde.ucr.cjis.gov",70,80,80,70,65,80,65,95))
ideas.append(mk("fbi_aggravated_assault_by_state","Aggravated Assault Rates by State","The geography of aggravated assault looks different from murder","MAP","us_state","State choropleth","Crime and Law Enforcement","FBI UCR estimated_crimes_1979_2024.csv https://cde.ucr.cjis.gov",70,80,80,65,70,80,55,95))
ideas.append(mk("fbi_rape_rate_change_decade","How Rape Reporting Changed State by State","Comparing legacy vs revised rape definitions reveals reporting shifts","MAP","us_state","State choropleth","Crime and Law Enforcement","FBI UCR estimated_crimes_1979_2024.csv https://cde.ucr.cjis.gov",75,65,70,75,80,75,70,95))

# ============================================================
# FBI — lee_1960_2024.csv (768K rows, law enforcement officers killed/assaulted)
# ============================================================
ideas.append(mk("fbi_officers_killed_by_decade","Police Officers Killed in the Line of Duty by Decade","How officer fatalities have changed from 1960 to 2024","CHART","us_national","Bar chart","Crime and Law Enforcement","FBI LEOKA lee_1960_2024.csv https://cde.ucr.cjis.gov",80,70,80,55,70,60,50,95))
ideas.append(mk("fbi_officers_killed_by_state","Where Police Officers Are Most Likely to Die","Officer deaths per capita by state over 60 years","MAP","us_state","State choropleth","Crime and Law Enforcement","FBI LEOKA lee_1960_2024.csv https://cde.ucr.cjis.gov",80,70,80,65,75,80,55,95))

# ============================================================
# FBI — territories crime data
# ============================================================
ideas.append(mk("fbi_territory_crime_rates","Crime in Americas Forgotten Territories","Puerto Rico and other US territories have very different crime patterns","MAP","us_national","Bar chart","Crime and Law Enforcement","FBI UCR territories_1995_2024.csv https://cde.ucr.cjis.gov",70,65,75,75,70,60,70,95))

# ============================================================
# CPI — historical-cpi-u-202602.xlsx (1913-2026 monthly)
# ============================================================
ideas.append(mk("cpi_inflation_113_years","113 Years of American Inflation","Monthly CPI-U from 1913 to 2026 shows every crisis and boom","CHART","us_national","Line chart","Economy","BLS CPI-U historical-cpi-u-202602.xlsx https://www.bls.gov/cpi/",65,80,80,55,55,65,45,95))
ideas.append(mk("cpi_worst_inflation_months","Americas Worst Inflation Months Ever","The months when prices rose fastest - 1940s wartime and 2022 both feature","RANK","us_national","Bar chart","Economy","BLS CPI-U historical-cpi-u-202602.xlsx https://www.bls.gov/cpi/",70,80,80,70,60,60,55,95))

# ============================================================
# SAGE DATA — Religion Census 2020 (3,154 county-level rows)
# ============================================================
ideas.append(mk("sage_religion_adherent_rate_county","Americas Most and Least Religious Counties","Adherent rate from the 2020 US Religion Census by county","MAP","us_county","County choropleth","Demographics","Sage Data / ARDA U.S. Religion Census 2020 https://www.thearda.com/us-religion/census",75,80,80,65,60,85,55,95))
ideas.append(mk("sage_religion_congregations_county","Where Churches Outnumber Gas Stations","Number of congregations per capita by county","MAP","us_county","County choropleth","Demographics","Sage Data / ARDA U.S. Religion Census 2020 https://www.thearda.com/us-religion/census",60,75,80,75,50,85,65,95))
ideas.append(mk("sage_religion_bible_belt_map","Mapping the Bible Belt With Data","Which counties have the highest evangelical Protestant adherent rates","MAP","us_county","County choropleth","Demographics","Sage Data / ARDA U.S. Religion Census 2020 https://www.thearda.com/us-religion/census",70,80,80,55,60,85,55,95))
ideas.append(mk("sage_religion_catholic_vs_protestant","The Catholic-Protestant Divide in America","County-level dominant denomination shows a stark geographic split","MAP","us_county","Bivariate choropleth","Demographics","Sage Data / ARDA U.S. Religion Census 2020 https://www.thearda.com/us-religion/census",65,75,75,70,65,85,70,95))

# ============================================================
# SAGE DATA — Inmates by Race
# ============================================================
ideas.append(mk("sage_inmates_race_disparity","The Racial Makeup of Americas Jails","Black Americans are jailed at 5x the rate of white Americans","CHART","us_national","Bar chart","Crime and Law Enforcement","Sage Data / Annual Survey of Jails https://bjs.ojp.gov/data-collection/annual-survey-jails",85,75,80,55,90,60,45,95))
ideas.append(mk("sage_inmates_race_trend","How Jail Racial Disparities Have Changed Over Time","Tracking the Black-white incarceration gap from the 1990s to today","CHART","us_national","Line chart","Crime and Law Enforcement","Sage Data / Annual Survey of Jails https://bjs.ojp.gov/data-collection/annual-survey-jails",80,75,80,65,85,65,55,95))

# ============================================================
# SAGE DATA — Arrests by Race
# ============================================================
ideas.append(mk("sage_arrests_race_offense","Arrest Rates by Race and Offense Type","Racial disparities in arrests vary dramatically by crime category","CHART","us_national","Bar chart","Crime and Law Enforcement","Sage Data / FBI UCR Arrests Database https://cde.ucr.cjis.gov",80,70,75,65,90,60,55,95))

# ============================================================
# SAGE DATA — Marijuana Use by State (NSDUH)
# ============================================================
ideas.append(mk("sage_marijuana_use_by_state","Where Americans Smoke the Most Weed","Past-month marijuana use rates by state from federal survey data","MAP","us_state","State choropleth","Health","Sage Data / NSDUH 2015-2019 https://www.samhsa.gov/data/nsduh",65,85,80,60,50,80,50,90))

# ============================================================
# SAGE DATA — Vehicle Registration by State
# ============================================================
ideas.append(mk("sage_vehicles_per_capita_state","Cars Per Person by State","Vehicle registration rates reveal Americas most car-dependent states","MAP","us_state","State choropleth","Transportation","Sage Data / All Motor Vehicles Database https://highways.dot.gov",55,80,80,60,35,80,50,90))

# ============================================================
# SAGE DATA — Personal Income by NAICS Industry
# ============================================================
ideas.append(mk("sage_income_by_industry_state","Dominant Industry by State Income","Which NAICS sector generates the most personal income in each state","MAP","us_state","State choropleth","Economy","Sage Data / BEA Regional Personal Income https://www.bea.gov/data/income-saving/personal-income-county-metro-and-other-areas",60,75,75,65,45,80,60,90))

# ============================================================
# SAGE DATA — NAEP Assessment Scores
# ============================================================
ideas.append(mk("sage_naep_scores_by_state","Americas Smartest Students by State","National Assessment of Educational Progress scores by state","MAP","us_state","State choropleth","Education","Sage Data / NAEP Database https://nces.ed.gov/nationsreportcard/",70,85,80,55,55,80,45,90))

# ============================================================
# OUR WORLD IN DATA — Population, Demographics, Global
# ============================================================
ideas.append(mk("owid_fertility_rate_world","The World Fertility Collapse","Children per woman has halved globally since 1960 and keeps dropping","MAP","worldwide","World choropleth","Demographics","Our World In Data - Fertility Rate https://ourworldindata.org/fertility-rate",80,75,85,70,70,85,50,95))
ideas.append(mk("owid_population_growth_rate","Where the World Is Growing (and Shrinking)","Population growth rates by country - Africa booms while Europe declines","MAP","worldwide","World choropleth","Demographics","Our World In Data - Population Growth https://ourworldindata.org/population-growth",70,75,85,60,55,85,45,95))
ideas.append(mk("owid_child_mortality_drop","The Greatest Success Story Never Told","Child mortality has fallen 90% in 200 years but nobody talks about it","MAP","worldwide","World choropleth","Health","Our World In Data - Child Mortality https://ourworldindata.org/child-mortality",85,70,85,70,55,85,55,95))
ideas.append(mk("owid_life_expectancy_world","How Long You Live Depends on Where You Were Born","Life expectancy varies from 53 to 85 years across countries","MAP","worldwide","World choropleth","Health","Our World In Data - Life Expectancy https://ourworldindata.org/life-expectancy",80,85,85,55,60,85,45,95))
ideas.append(mk("owid_democracy_vs_autocracy","Half the World Lives in an Autocracy","Countries classified by political regime - democracy is losing ground","MAP","worldwide","World choropleth","History","Our World In Data - Political Regime https://ourworldindata.org/democracy",80,70,80,70,80,85,60,95))
ideas.append(mk("owid_homicide_rate_world","Murder Rates Around the World","Intentional homicide rates per 100K reveal Latin Americas deadly outlier status","MAP","worldwide","World choropleth","Crime and Law Enforcement","Our World In Data - Homicide https://ourworldindata.org/homicides",80,75,85,65,80,85,50,95))
ideas.append(mk("owid_military_spending_gdp","Military Spending as Share of GDP","Which countries spend the most on their militaries relative to their economy","MAP","worldwide","World choropleth","History","Our World In Data - Military Spending https://ourworldindata.org/military-spending",65,65,80,65,70,85,50,95))
ideas.append(mk("owid_internet_access_world","The Digital Divide","Share of population using the internet by country","MAP","worldwide","World choropleth","Science & Technology","Our World In Data - Internet https://ourworldindata.org/internet",60,75,85,50,40,85,40,95))
ideas.append(mk("owid_co2_per_capita_world","CO2 Emissions Per Person by Country","The gulf between the biggest and smallest per-capita emitters is staggering","MAP","worldwide","World choropleth","Climate","Our World In Data - CO2 Emissions https://ourworldindata.org/co2-emissions",75,70,85,60,75,85,45,95))
ideas.append(mk("owid_prison_rate_world","The Worlds Biggest Jailers","Incarceration rate per 100K - the US leads by a mile","MAP","worldwide","World choropleth","Crime and Law Enforcement","Our World In Data - Prison Population https://ourworldindata.org/incarceration",80,75,85,65,80,85,50,95))
ideas.append(mk("owid_literacy_rate_world","Where People Still Cant Read","Global literacy rates - most of the world can read but pockets remain","MAP","worldwide","World choropleth","Education","Our World In Data - Literacy https://ourworldindata.org/literacy",70,70,85,55,55,85,45,95))
ideas.append(mk("owid_extreme_poverty_decline","The World Is Leaving Poverty Behind","Share of population in extreme poverty has plummeted from 75% to under 10%","CHART","worldwide","Area chart","Economy","Our World In Data - Poverty https://ourworldindata.org/extreme-poverty",80,70,85,70,50,70,55,95))
ideas.append(mk("owid_vaccination_coverage","Global Vaccination Coverage","Which countries vaccinate nearly all children vs which have massive gaps","MAP","worldwide","World choropleth","Health","Our World In Data - Vaccination https://ourworldindata.org/vaccination",70,70,85,55,50,85,45,95))
ideas.append(mk("owid_deaths_by_cause_world","What Actually Kills People Around the World","Annual deaths by cause - heart disease and cancer dominate globally","CHART","worldwide","Treemap","Health","Our World In Data - Causes of Death https://ourworldindata.org/causes-of-death",75,80,80,55,50,70,50,95))
ideas.append(mk("owid_armed_conflicts_by_region","Where Wars Are Being Fought Right Now","Deaths in armed conflicts by world region from 1946 to present","CHART","worldwide","Area chart","History","Our World In Data - War and Peace https://ourworldindata.org/war-and-peace",80,65,80,60,85,65,55,95))
ideas.append(mk("owid_lgbt_rights_world","Countries That Protect vs Criminalize LGBT Rights","Legal status of same-sex relationships varies wildly across the globe","MAP","worldwide","World choropleth","Demographics","Our World In Data - LGBT Rights https://ourworldindata.org/lgbt-rights",80,70,80,60,80,85,55,95))
ideas.append(mk("owid_caloric_supply_world","Daily Calories Per Person by Country","Some countries average 3,800 calories per day while others get 1,700","MAP","worldwide","World choropleth","Food & Nutrition","Our World In Data - Food Supply https://ourworldindata.org/food-supply",65,75,85,65,55,85,55,95))
ideas.append(mk("owid_energy_per_capita","Energy Consumption Per Person Worldwide","Per capita energy use reveals the fossil fuel divide between rich and poor nations","MAP","worldwide","World choropleth","Environment","Our World In Data - Energy https://ourworldindata.org/energy",60,65,80,55,55,85,50,95))
ideas.append(mk("owid_schooling_years_world","Average Years of Schooling by Country","Mean years of education ranges from 1 to 14 across nations","MAP","worldwide","World choropleth","Education","Our World In Data - Education https://ourworldindata.org/global-education",65,70,85,55,50,85,45,95))
ideas.append(mk("owid_objects_in_space","The Explosion of Objects in Outer Space","Yearly launches have gone from dozens to thousands in the SpaceX era","CHART","worldwide","Area chart","Science & Technology","Our World In Data - Space Exploration https://ourworldindata.org/space-exploration-satellites",55,60,80,75,35,70,70,95))
ideas.append(mk("owid_contraceptive_prevalence","Contraceptive Use Around the World","The gap between any method and modern methods reveals access inequalities","MAP","worldwide","World choropleth","Health","Our World In Data - Contraception https://ourworldindata.org/contraceptives",65,65,80,60,55,85,55,95))
ideas.append(mk("owid_research_spending_gdp","Which Countries Invest Most in Research","R&D spending as share of GDP - Israel and South Korea lead the world","MAP","worldwide","World choropleth","Science & Technology","Our World In Data - Research and Development https://ourworldindata.org/research-and-development",55,60,80,65,40,85,55,95))
ideas.append(mk("owid_electricity_by_source","How the World Powers Itself","Electricity production by source - fossil fuels still dominate globally","CHART","worldwide","Area chart","Environment","Our World In Data - Electricity Mix https://ourworldindata.org/electricity-mix",60,65,80,50,55,70,45,95))
ideas.append(mk("owid_undernourishment_world","The Hunger Map","Prevalence of undernourishment by country","MAP","worldwide","World choropleth","Food & Nutrition","Our World In Data - Hunger https://ourworldindata.org/hunger-and-undernourishment",80,70,85,55,65,85,45,95))
ideas.append(mk("owid_access_to_electricity","1 Billion People Still Live Without Electricity","Share of population with access to electricity by country","MAP","worldwide","World choropleth","Environment","Our World In Data - Energy Access https://ourworldindata.org/energy-access",75,70,85,65,60,85,50,95))
ideas.append(mk("owid_clean_water_access","Where Clean Drinking Water Is Still a Luxury","Population using at least basic drinking water services","MAP","worldwide","World choropleth","Health","Our World In Data - Water Access https://ourworldindata.org/water-access",80,70,85,55,60,85,50,95))
ideas.append(mk("owid_sanitation_access","The Sanitation Crisis Hiding in Plain Sight","Share of population with improved sanitation - billions lack basic toilets","MAP","worldwide","World choropleth","Health","Our World In Data - Sanitation https://ourworldindata.org/sanitation",75,65,85,60,55,85,50,95))
ideas.append(mk("owid_ag_employment_share","Where Farming Is Still the Only Job","Share of labor force in agriculture ranges from 1% to 80%","MAP","worldwide","World choropleth","Labor","Our World In Data - Employment in Agriculture https://ourworldindata.org/employment-in-agriculture",60,65,80,65,45,85,55,95))
ideas.append(mk("owid_age_dependency_ratio","The Young Countries and the Old Countries","Median age and age dependency ratio reveal two very different demographic worlds","MAP","worldwide","World choropleth","Demographics","Our World In Data - Age Structure https://ourworldindata.org/age-structure",65,65,80,65,55,85,55,95))

# ============================================================
# WORLD CUP DATA (matches_1930_2022.csv, 964 matches with xG)
# ============================================================
ideas.append(mk("wc_biggest_upsets_xg","The Biggest World Cup Upsets by Expected Goals","Matches where the winner had far lower xG than the loser","RANK","worldwide","Bar chart","Sports & Recreation","World Cup matches_1930_2022.csv https://www.kaggle.com/datasets",65,70,75,80,55,60,75,95))
ideas.append(mk("wc_home_advantage_hosts","World Cup Home Advantage Is Real","Host nations significantly outperform their FIFA ranking in tournament results","CHART","worldwide","Bar chart","Sports & Recreation","World Cup matches + world_cup.csv https://www.kaggle.com/datasets",60,75,80,70,45,60,65,95))
ideas.append(mk("wc_goals_per_match_trend","World Cup Goals Per Match Over 92 Years","Average goals per match has shifted dramatically since 1930","CHART","worldwide","Line chart","Sports & Recreation","World Cup matches_1930_2022.csv https://www.kaggle.com/datasets",50,70,80,60,35,65,55,95))
ideas.append(mk("wc_attendance_growth","From 363K to 3.5 Million: World Cup Attendance Growth","Total attendance has grown 10x since the first tournament in 1930","CHART","worldwide","Bar chart","Sports & Recreation","World Cup world_cup.csv https://www.kaggle.com/datasets",45,65,80,55,30,65,50,95))

# ============================================================
# PUBLIC SCHOOLS (101,390 schools with lat/lon, Title I, enrollment)
# ============================================================
ideas.append(mk("schools_title_i_map","Where Americas Poorest Schools Are","101,000 public schools mapped by Title I status","MAP","us_national","Dot map","Education","NCES Public School Characteristics 2022-23 https://nces.ed.gov/ccd/schoolsearch/",80,85,80,60,70,85,55,95))
ideas.append(mk("schools_enrollment_density","The Geography of American Education","Every public school in America plotted by enrollment size","MAP","us_national","Dot map","Education","NCES Public School Characteristics 2022-23 https://nces.ed.gov/ccd/schoolsearch/",55,75,80,55,35,90,55,95))
ideas.append(mk("schools_charter_vs_public_map","Charter Schools vs Traditional Public Schools","Mapping the spread of charter schools across the country","MAP","us_national","Dot map","Education","NCES Public School Characteristics 2022-23 https://nces.ed.gov/ccd/schoolsearch/",65,75,75,65,65,85,60,95))
ideas.append(mk("schools_rural_school_access","Rural Americas Vanishing Schools","Students in rural counties travel farther to school than ever before","MAP","us_county","County choropleth","Education","NCES Public School Characteristics 2022-23 https://nces.ed.gov/ccd/schoolsearch/",75,80,75,65,60,80,65,90))

# ============================================================
# AIRBNB BOSTON (1,741 listings with revenue, occupancy, ratings)
# ============================================================
ideas.append(mk("airbnb_boston_revenue_map","Airbnb Revenue Hotspots in Boston","Monthly revenue by neighborhood - Back Bay and South End dominate","MAP","us_city","City map","Economy","AirDNA Airbnb Boston data https://www.airdna.co",60,75,75,60,50,80,55,90))
ideas.append(mk("airbnb_boston_occupancy_map","Where Bostons Airbnbs Are Always Booked","Occupancy rates by neighborhood reveal tourism patterns","MAP","us_city","City map","Economy","AirDNA Airbnb Boston data https://www.airdna.co",55,75,75,55,45,80,50,90))

# ============================================================
# MBTA DATA (transit shapefiles)
# ============================================================
ideas.append(mk("mbta_transit_desert_boston","Bostons Transit Deserts","Areas more than 1 mile from any MBTA stop mapped against poverty rates","MAP","us_city","City map","Transportation","MBTA GTFS 2025 + Census ACS https://www.mbta.com/developers",80,80,75,70,70,80,70,85))
ideas.append(mk("mbta_bus_vs_rail_equity","Who Gets the Bus and Who Gets the Train","MBTA bus routes serve lower-income neighborhoods while rail serves wealthier ones","MAP","us_city","Bivariate choropleth","Transportation","MBTA GTFS 2025 + Census ACS https://www.mbta.com/developers",80,80,75,75,80,80,70,85))
ideas.append(mk("mbta_commuter_rail_coverage","The Commuter Rail Gap","348 commuter rail stations mapped against population density","MAP","us_city","Dot map","Transportation","MBTA GTFS 2025 https://www.mbta.com/developers",60,75,75,55,50,80,55,90))

# ============================================================
# WALKABILITY INDEX (EPA, census block group level, nationwide)
# ============================================================
ideas.append(mk("epa_walkability_us","The Most and Least Walkable Places in America","EPA National Walkability Index at census block group level","MAP","us_national","County choropleth","Transportation","EPA National Walkability Index https://www.epa.gov/smartgrowth/smart-location-mapping",65,85,80,55,40,85,45,95))
ideas.append(mk("epa_walkability_vs_obesity","Walkability vs Obesity Rates","Do more walkable areas have lower obesity rates","XREF","us_county","Scatter plot","Health","EPA National Walkability Index + CDC PLACES https://www.epa.gov/smartgrowth/smart-location-mapping",70,80,75,70,50,65,70,85))

# ============================================================
# FIVETHIRTYEIGHT — additional unique ideas
# ============================================================
ideas.append(mk("fte_antiquities_act_timeline","Every National Monument Created Under the Antiquities Act","344 actions from 1906-2017 mapped by president and acreage","CHART","us_national","Bar chart","Environment","FiveThirtyEight actions_under_antiquities_act.csv https://github.com/fivethirtyeight/data",55,60,75,65,55,65,65,95))
ideas.append(mk("fte_cabinet_turnover_by_president","Which Presidents Burn Through Cabinet Members Fastest","Average cabinet member tenure by president","RANK","us_national","Bar chart","History","FiveThirtyEight cabinet-turnover.csv https://github.com/fivethirtyeight/data",55,70,75,70,55,55,60,95))
ideas.append(mk("fte_candidate_visits_2024_map","Where 2024 Candidates Spent Their Time","1,649 campaign visits mapped by city and state","MAP","us_state","Dot map","Elections","FiveThirtyEight candidate_visits_2024-01-11.csv https://github.com/fivethirtyeight/data",65,80,80,60,55,80,50,95))
ideas.append(mk("fte_divorce_education_gap","The Education Divorce Gap","College graduates divorce at half the rate of those without degrees","CHART","us_national","Line chart","Demographics","FiveThirtyEight divorce.csv https://github.com/fivethirtyeight/data",70,85,75,70,55,60,60,95))
ideas.append(mk("fte_fifa_audience_vs_population","FIFA TV Audience vs Country Population","Countries whose football audience vastly exceeds their population share","CHART","worldwide","Scatter plot","Sports & Recreation","FiveThirtyEight fifa_countries_audience.csv https://github.com/fivethirtyeight/data",50,65,75,65,35,60,65,95))
ideas.append(mk("fte_obama_commutations","Obama Commuted 7,077 Sentences","The largest use of executive clemency in modern history mapped","CHART","us_national","Bar chart","Crime and Law Enforcement","FiveThirtyEight obama_commutations.csv https://github.com/fivethirtyeight/data",65,60,70,70,65,55,60,95))
ideas.append(mk("fte_senate_poll_accuracy","How Wrong Were Senate Polls","Historical Senate polling error by state from 1990-2016","MAP","us_state","State choropleth","Elections","FiveThirtyEight august_senate_polls.csv https://github.com/fivethirtyeight/data",55,70,70,70,50,75,65,95))

# ============================================================
# SINGULAR IDEAS from interesting dataset angles
# ============================================================
ideas.append(mk("pokemon_type_distribution","The Imbalance of Pokemon Types","Water and Normal types vastly outnumber Ice and Ghost types","CHART","worldwide","Treemap","Entertainment","Pokemon DB dataset (F: drive) https://pokemondb.net",40,65,75,55,20,65,55,95))
ideas.append(mk("pl_home_advantage_2324","Premier League Home Advantage in 2023-24","Home vs away goal difference by club shows the 12th man effect","CHART","worldwide","Bar chart","Sports & Recreation","FBref Premier League 2023-24 (F: drive) https://fbref.com",55,70,80,55,40,60,50,95))
ideas.append(mk("ma_population_1930_2023","Massachusetts Population Change 1930-2023","93 years of town-by-town population change across the Commonwealth","MAP","us_ma","City map","Demographics","UMDI Population Projections (F: drive) https://datacommon.mapc.org",65,75,80,55,40,80,55,95))
ideas.append(mk("ma_population_projection_2050","Massachusetts in 2050: Who Grows and Who Shrinks","Long-term population projections for every MA city and town to 2050","MAP","us_ma","City map","Demographics","UMDI V2024 Long-Term Population Projections (F: drive) https://datacommon.mapc.org",65,75,75,65,45,80,60,90))
ideas.append(mk("springfield_cso_map","Springfields Combined Sewer Overflow Problem","Mapping every CSO discharge point in Springfield MA","MAP","us_ma","City map","Environment","MassDEP CSO data + QGIS project (F: drive) https://www.mass.gov/info-details/combined-sewer-overflows",65,55,75,60,60,75,70,85))
ideas.append(mk("ev_charging_stations_map","Americas Electric Vehicle Charging Infrastructure","Every EV charging station in the country mapped","MAP","us_national","Dot map","Transportation","DOE AFDC EV Charging Stations (F: drive) https://afdc.energy.gov",60,75,80,50,40,85,45,95))
ideas.append(mk("congo_drc_osm_infrastructure","Mapping the Congo: Where Roads Dont Exist","OSM road network density in DRC reveals vast ungoverned spaces","MAP","worldwide","Special map","Transportation","OpenStreetMap DRC shapefiles (F: drive) https://www.openstreetmap.org",60,50,70,80,65,80,80,90))
ideas.append(mk("ne_county_population_density","New Englands Population Density by County","The urban-rural divide across all six New England states","MAP","us_new_england","County choropleth","Demographics","NE Counties shapefile + Census (F: drive) https://www.census.gov",55,75,80,45,30,80,40,95))
ideas.append(mk("us_primary_roads_network","The Arterial Map of America","Every primary road in the US Census TIGER dataset","MAP","us_national","Special map","Transportation","Census TIGER US Primary Roads (F: drive) https://www.census.gov/geographies/mapping-files/time-series/geo/tiger-line-file.html",45,60,80,50,25,90,50,95))
ideas.append(mk("maine_conservation_areas","Maines Protected Lands","Mapping every conservation area in the Pine Tree State","MAP","us_state","Special map","Environment","Maine Conservation Areas (F: drive) https://www.maine.gov/dacf/mnap/",50,50,80,50,30,85,55,85))

# ============================================================
# INJECTION LOGIC
# ============================================================
with open(DATA_JS, encoding="utf-8") as f:
    raw = f.read()

existing_ids = set(re.findall(r'id:"([^"]+)"', raw))
print("Existing ideas: %d" % len(existing_ids))

# Dedupe
new_ideas = []
dupes = 0
for idea in ideas:
    m = re.search(r'id:"([^"]+)"', idea)
    if m and m.group(1) not in existing_ids:
        new_ideas.append(idea)
    else:
        dupes += 1

print("New ideas to inject: %d (skipped %d dupes)" % (len(new_ideas), dupes))

if len(new_ideas) == 0:
    print("Nothing to inject.")
    sys.exit(0)

# Strip tail, append, re-add tail
tail = "]; // end D"
if tail not in raw:
    print("ERROR: Cannot find tail marker '%s'" % tail)
    sys.exit(1)

raw = raw.replace(tail, "")
for idea in new_ideas:
    raw += idea + ",\n"
raw += tail + "\n"

with open(DATA_JS, "w", encoding="utf-8") as f:
    f.write(raw)

print("Injected %d ideas. Total now: %d" % (len(new_ideas), len(existing_ids) + len(new_ideas)))
print("Run maintain.py next!")
