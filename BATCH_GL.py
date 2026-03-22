"""BATCH_GL: Ideas from raw_data non-Kaggle sources.
FBI, FiveThirtyEight, CPI/PPI, Our World In Data, Sage Data,
HSUS, Airbnb, MBTA shapefiles, Walkability Index, World Cup.
"""
import re, sys, os
DATA_JS = r"D:\projects\mapzimus-board\data.js"

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
# FBI CRIME DATA (estimated_crimes_1979_2024.csv, hate_crime, etc.)
# ============================================================
ideas.append(mk("gl001","How U.S. Crime Has Changed Since 1979","Violent and property crime trends across 45 years of FBI UCR data","CHART","US","Animated line chart","Crime and Law Enforcement","D:/raw_data/fbi/estimated_crimes_1979_2024.csv",72,85,80,60,70,75,55,95))
ideas.append(mk("gl002","The Geography of Hate in America","FBI hate crime incidents mapped by state, 2024","MAP","US-State","State choropleth","Crime and Law Enforcement","D:/raw_data/fbi/hate_crime.zip",85,78,70,72,88,80,68,90))
ideas.append(mk("gl003","Which States Report the Most Crime to the FBI?","UCR participation rates vary wildly - some states barely report","MAP","US-State","State choropleth","Crime and Law Enforcement","D:/raw_data/fbi/ucr_participation_1960_2024.csv",55,65,75,78,60,72,70,92))
ideas.append(mk("gl004","Officers Killed and Assaulted: The LEOKA Map","Law enforcement officers killed or assaulted in the line of duty by state","MAP","US-State","State choropleth","Crime and Law Enforcement","D:/raw_data/fbi/LEOKA_1995_2024.zip",80,70,68,65,85,75,62,88))
ideas.append(mk("gl005","Human Trafficking Hotspots in the U.S.","FBI human trafficking cases by state and territory, 2013-2024","MAP","US-State","State choropleth","Crime and Law Enforcement","D:/raw_data/fbi/HT_2013-2024.zip",88,72,65,75,90,78,72,85))
ideas.append(mk("gl006","The 45-Year Murder Rate: Which States Got Safer?","State-level homicide rate changes from 1979 to 2024","MAP","US-State","Bivariate choropleth","Crime and Law Enforcement","D:/raw_data/fbi/estimated_crimes_1979_2024.csv",78,82,72,70,80,82,68,92))
ideas.append(mk("gl007","Americas Crime Clock: Offenses Per Minute","How many violent crimes, burglaries, and thefts happen every 60 seconds in the U.S.","CHART","US","Infographic","Crime and Law Enforcement","D:/raw_data/fbi/estimated_crimes_1979_2024.csv",75,88,85,72,68,80,65,95))

# ============================================================
# FIVETHIRTYEIGHT DATASETS (29 curated CSVs)
# ============================================================
ideas.append(mk("gl008","Which Airlines Are Actually the Safest?","Fatal accidents and incidents per trillion seat-miles by airline","RANK","World","Bar chart","Transportation","D:/raw_data/fivethirtyeight/airline-safety.csv",72,85,80,68,65,70,60,95))
ideas.append(mk("gl009","Americas Worst Drivers by State","Bad driving metrics: fatalities, DUI, speeding, distracted driving","MAP","US-State","State choropleth","Transportation","D:/raw_data/fivethirtyeight/bad-drivers.csv",70,90,82,65,62,78,58,95))
ideas.append(mk("gl010","The World Drinks Map","Average servings of beer, wine, and spirits by country","MAP","World","World choropleth","Food & Nutrition","D:/raw_data/fivethirtyeight/drinks.csv",68,85,80,72,50,82,62,95))
ideas.append(mk("gl011","Drug Use by Age: When America Gets High","Usage rates for 13 substances across age groups from 12 to 65+","CHART","US","Stacked area chart","Health","D:/raw_data/fivethirtyeight/drug-use-by-age.csv",78,82,72,75,72,75,68,95))
ideas.append(mk("gl012","Americas Cousin Marriage Map","States where cousin marriage is legal, illegal, or complicated","MAP","US-State","State choropleth","Demographics","D:/raw_data/fivethirtyeight/cousin-marriage-data.csv",65,78,80,82,55,72,75,95))
ideas.append(mk("gl013","The Divorce Belt: Where Marriages Fail Most","State-by-state divorce rates mapped across America","MAP","US-State","State choropleth","Demographics","D:/raw_data/fivethirtyeight/divorce.csv",75,88,78,62,68,75,58,92))
ideas.append(mk("gl014","Hate Crimes and Income Inequality","States with higher income inequality have more hate crimes per capita","MAP","US-State","Bivariate choropleth","Crime and Law Enforcement","D:/raw_data/fivethirtyeight/hate_crimes.csv",82,78,68,75,85,80,72,92))
ideas.append(mk("gl015","The College Majors That Pay (and Dont)","Median earnings and unemployment rates by college major","RANK","US","Bar chart","Education","D:/raw_data/fivethirtyeight/recent-grads.csv",72,90,82,68,65,70,60,95))
ideas.append(mk("gl016","Where Women Dominate STEM","Share of women in each STEM field, ranked and visualized","CHART","US","Bar chart","Education","D:/raw_data/fivethirtyeight/women-stem.csv",70,80,78,65,62,72,65,95))
ideas.append(mk("gl017","When Are Americans Born?","Daily birth frequency patterns - which day of the year has the most babies?","CHART","US","Heatmap calendar","Demographics","D:/raw_data/fivethirtyeight/US_births_1994-2003_CDC_NCHS.csv",65,88,82,72,45,80,68,95))
ideas.append(mk("gl018","The Most Overrated Halloween Candy","Power ranking of 85 candy types by winpercent in head-to-head matchups","RANK","US","Bar chart","Food & Nutrition","D:/raw_data/fivethirtyeight/candy-data.csv",60,85,78,68,48,72,65,95))
ideas.append(mk("gl019","Classic Rock Is Just 40 Songs on Repeat","Most-played songs on classic rock radio reveal shocking repetition","RANK","US","Bar chart","Entertainment","D:/raw_data/fivethirtyeight/classic-rock-song-list.csv",65,82,75,78,52,68,72,95))
ideas.append(mk("gl020","Hollywood Biopics: Who Gets Their Story Told?","Race, gender, and subject type of biographical films over decades","CHART","US","Stacked bar chart","Entertainment","D:/raw_data/fivethirtyeight/biopics.csv",68,75,72,70,65,70,72,92))
ideas.append(mk("gl021","How Obama Used His Clemency Power","Map and timeline of 1,927 commutations granted by President Obama","MAP","US-State","Dot map","History","D:/raw_data/fivethirtyeight/obama_commutations.csv",72,70,68,68,65,72,65,90))
ideas.append(mk("gl022","Where FIFA Fans Actually Watch","TV audience share for the World Cup by country","MAP","World","World choropleth","Sports & Recreation","D:/raw_data/fivethirtyeight/fifa_countries_audience.csv",65,80,75,68,50,78,62,95))
ideas.append(mk("gl023","The ICU Bed Shortage Map","Metro areas with the fewest intensive care beds per capita","MAP","US-Metro","Dot map","Health","D:/raw_data/fivethirtyeight/mmsa-icu-beds.csv",80,82,72,70,82,75,65,92))
ideas.append(mk("gl024","2024 Election Deniers in Congress","Every member of Congress who denied the 2020 election results","MAP","US-State","State choropleth","Elections","D:/raw_data/fivethirtyeight/fivethirtyeight_election_deniers.csv",78,75,70,65,82,72,68,92))
ideas.append(mk("gl025","Where Foul Balls Go in a Baseball Stadium","Mapping the landing zones of foul balls by section and speed","MAP","Other","Dot map","Sports & Recreation","D:/raw_data/fivethirtyeight/foul-balls.csv",55,72,70,75,52,80,78,90))
ideas.append(mk("gl026","Cabinet Turnover: Which Presidents Lost Staff Fastest?","Rate of cabinet departures by president from Truman to Biden","CHART","US","Bar chart","History","D:/raw_data/fivethirtyeight/cabinet-turnover.csv",65,72,75,70,68,68,68,92))
ideas.append(mk("gl027","Presidential Campaign Trail: Where Candidates Go","Map of 2024 candidate visits by state - who gets ignored?","MAP","US-State","State choropleth","Elections","D:/raw_data/fivethirtyeight/candidate_visits_2024-01-11.csv",70,78,75,68,65,78,65,90))
ideas.append(mk("gl028","The Antiquities Act: 100+ Years of Presidential Land Grabs","Every national monument created by presidential proclamation","MAP","US","Dot map","Geography & Environment","D:/raw_data/fivethirtyeight/actions_under_antiquities_act.csv",68,65,72,72,62,80,75,90))

# ============================================================
# CPI / PPI DATA
# ============================================================
ideas.append(mk("gl029","46 Years of Inflation: What Got More Expensive?","CPI-U category breakdown showing which items outpaced general inflation","CHART","US","Animated line chart","Economy","D:/raw_data/cpi/historical-cpi-u-202602.xlsx",75,88,78,68,72,75,60,95))
ideas.append(mk("gl030","Producer vs Consumer: Who Feels Inflation First?","PPI vs CPI trends showing how price shocks flow through the economy","CHART","US","Line chart","Economy","D:/raw_data/cpi/ppi-fdallrel.xlsx",65,72,70,72,68,68,70,90))

# ============================================================
# OUR WORLD IN DATA (30+ datasets)
# ============================================================
ideas.append(mk("gl031","The World Is Getting Older: Median Age by Country","Global map of median age showing the demographic divide","MAP","World","World choropleth","Demographics","D:/raw_data/Our World In Data/population-growth-rate-vs-median-age/population-growth-rate-vs-median-age.csv",72,80,78,68,72,82,62,95))
ideas.append(mk("gl032","8 Billion and Counting: World Population Growth by Region","Animated stacked area chart of population growth by world region","CHART","World","Animated line chart","Population","D:/raw_data/Our World In Data/population/population.csv",70,82,80,62,65,78,55,95))
ideas.append(mk("gl033","The Countries Where People Live the Longest","Life expectancy world map - a 40-year gap between richest and poorest","MAP","World","World choropleth","Health","D:/raw_data/Our World In Data/life-expectancy.zip",78,85,80,65,72,82,58,92))
ideas.append(mk("gl034","Where Democracy Is Thriving - and Where Its Dying","Political regime type by country: democracy to autocracy spectrum","MAP","World","World choropleth","International Statistics","D:/raw_data/Our World In Data/political-regime/political-regime.csv",80,78,72,70,85,82,68,95))
ideas.append(mk("gl035","CO2 Per Capita: The Worlds Biggest Polluters Arent Who You Think","Per-capita carbon emissions tell a different story than total emissions","MAP","World","World choropleth","Climate","D:/raw_data/Our World In Data/co-emissions-per-capita.zip",82,80,75,78,75,82,72,92))
ideas.append(mk("gl036","The Global Fertility Collapse","Children per woman has halved since 1960 in most of the world","MAP","World","World choropleth","Demographics","D:/raw_data/Our World In Data/children-born-per-woman.zip",80,82,78,75,80,80,70,92))
ideas.append(mk("gl037","How Death Has Changed: Global Causes Over 30 Years","Shifting causes of death worldwide from infectious to chronic disease","CHART","World","Stacked area chart","Health","D:/raw_data/Our World In Data/annual-number-of-deaths-by-cause.png",78,80,75,70,72,78,65,88))
ideas.append(mk("gl038","The World Map of Extreme Poverty","Share of population living on less than $2.15/day by country","MAP","World","World choropleth","Economy","D:/raw_data/Our World In Data/share-of-population-in-extreme-poverty/share-of-population-in-extreme-poverty.csv",85,82,78,68,80,82,62,95))
ideas.append(mk("gl039","Every Country That Protects LGBT Rights","Which nations have legal protections vs criminalization of homosexuality","MAP","World","World choropleth","International Statistics","D:/raw_data/Our World In Data/countries-protecting-core-lgbt-rights.zip",78,80,72,68,82,80,70,90))
ideas.append(mk("gl040","The Internet Divide: Who Is Still Offline?","Share of individuals using the internet by country","MAP","World","World choropleth","Science & Technology","D:/raw_data/Our World In Data/share-of-individuals-using-the-internet/share-of-individuals-using-the-internet.csv",70,82,80,65,62,78,60,95))
ideas.append(mk("gl041","Humanitys Energy Appetite: 200 Years of Fuel Transitions","Global energy consumption by source from coal to renewables","CHART","World","Stacked area chart","Climate","D:/raw_data/Our World In Data/global-energy-substitution.zip",72,75,72,70,68,80,68,90))
ideas.append(mk("gl042","Military Spending as % of GDP: Who Is Most Militarized?","Defense expenditure relative to economy size by country","MAP","World","World choropleth","International Statistics","D:/raw_data/Our World In Data/military-spending-as-a-share-of-gdp-sipri.zip",75,72,72,70,80,80,65,90))
ideas.append(mk("gl043","The Homicide Rate World Map","Intentional homicides per 100k population by country","MAP","World","World choropleth","Crime and Law Enforcement","D:/raw_data/Our World In Data/homicide-rate-unodc.zip",80,78,75,68,82,82,60,90))
ideas.append(mk("gl044","How Quickly Countries Are Losing Their Youth","Projected decline in under-15 population by country through 2100","MAP","World","World choropleth","Demographics","D:/raw_data/Our World In Data/population-younger-than-15-with-projections/population-younger-than-15-with-projections.csv",75,78,72,72,75,78,70,88))
ideas.append(mk("gl045","The Space Race 2.0: Objects Launched Into Orbit by Country","Yearly objects launched into space - from Cold War to SpaceX era","CHART","World","Stacked area chart","Science & Technology","D:/raw_data/Our World In Data/yearly-number-of-objects-launched-into-outer-space/yearly-number-of-objects-launched-into-outer-space.csv",72,75,72,78,65,80,75,95))
ideas.append(mk("gl046","The Prison Map: Incarceration Rates Around the World","Prison population per 100k people - the U.S. leads by a mile","MAP","World","World choropleth","Crime and Law Enforcement","D:/raw_data/Our World In Data/prison-population-rate/prison-population-rate.csv",82,80,75,72,82,80,65,95))
ideas.append(mk("gl047","Who Feeds the World: Agricultural Employment by Country","Share of labor force working in agriculture reveals economic development","MAP","World","World choropleth","Labor","D:/raw_data/Our World In Data/share-of-the-labor-force-employed-in-agriculture/share-of-the-labor-force-employed-in-agriculture.csv",65,72,75,68,58,78,62,92))
ideas.append(mk("gl048","The Vaccination Map: Global Coverage for Key Diseases","Childhood vaccination rates by country - coverage gaps persist","MAP","World","World choropleth","Health","D:/raw_data/Our World In Data/global-vaccination-coverage.zip",75,80,75,62,72,78,58,88))
ideas.append(mk("gl049","R&D Spending: Which Countries Invest Most in Innovation?","Research and development expenditure as % of GDP by country","MAP","World","World choropleth","Science & Technology","D:/raw_data/Our World In Data/research-spending-gdp/research-spending-gdp.csv",68,72,75,70,62,78,68,95))
ideas.append(mk("gl050","Access to Clean Water: The Global Divide","Share of population using at least basic drinking water by country","MAP","World","World choropleth","Health","D:/raw_data/Our World In Data/population-using-at-least-basic-drinking-water/population-using-at-least-basic-drinking-water.csv",82,80,78,62,78,80,58,92))
ideas.append(mk("gl051","The Human Development Index World Map","HDI scores visualized - health, education, and income combined","MAP","World","World choropleth","International Statistics","D:/raw_data/Our World In Data/human-development-index.zip",72,78,80,60,65,82,58,90))
ideas.append(mk("gl052","Child Mortality: The Map That Shows How Far Weve Come","Under-5 mortality rate by country, then and now","MAP","World","World choropleth","Health","D:/raw_data/Our World In Data/child-mortality.zip",85,82,75,65,78,80,62,90))
ideas.append(mk("gl053","Who Gets Electricity? The Access Map","Share of population with access to electricity by country","MAP","World","World choropleth","Science & Technology","D:/raw_data/Our World In Data/share-of-the-population-with-access-to-electricity/share-of-the-population-with-access-to-electricity.csv",72,78,80,65,68,80,60,92))
ideas.append(mk("gl054","The Literacy Gap: Global Reading and Writing Rates","Cross-country literacy rates show education inequality","MAP","World","World choropleth","Education","D:/raw_data/Our World In Data/cross-country-literacy-rates.zip",72,78,78,62,68,78,60,88))
ideas.append(mk("gl055","How Much Meat Does the World Kill?","Land animals slaughtered annually for meat by country","MAP","World","World choropleth","Food & Nutrition","D:/raw_data/Our World In Data/prevalence-of-undernourishment/prevalence-of-undernourishment.csv",75,72,70,72,70,78,68,90))
ideas.append(mk("gl056","Who Time Is Spent With by Age","Americans spend increasing time alone as they age - relationship time peaks in 20s","CHART","US","Line chart","Demographics","D:/raw_data/Our World In Data/time-spent-with-relationships-by-age-us/time-spent-with-relationships-by-age-us.csv",88,92,80,78,72,75,75,95))
ideas.append(mk("gl057","The Global Calorie Map","Daily per capita caloric supply by country","MAP","World","World choropleth","Food & Nutrition","D:/raw_data/Our World In Data/daily-per-capita-caloric-supply.zip",65,80,78,65,58,78,58,88))
ideas.append(mk("gl058","Birth Rate vs Death Rate: The Demographic Crossover","Countries where deaths now outnumber births - population decline begins","MAP","World","Bivariate choropleth","Demographics","D:/raw_data/Our World In Data/birth-rate-vs-death-rate.zip",78,80,72,75,78,82,72,90))
ideas.append(mk("gl059","The Sanitation Divide: Improved Facilities by Country","Access to improved sanitation worldwide","MAP","World","World choropleth","Health","D:/raw_data/Our World In Data/share-of-population-with-improved-sanitation-faciltities/share-of-population-with-improved-sanitation-faciltities.csv",70,75,75,60,65,78,58,92))

# ============================================================
# SAGE DATA (religion, crime, education, income, vehicles)
# ============================================================
ideas.append(mk("gl060","Americas Religion Map: Adherent Rates by County","Religious adherent rates from the U.S. Religion Census by county","MAP","US-County","County choropleth","Demographics","D:/raw_data/Sage_Data/Adherent Rate from the U.S. Religion Census Database.xlsx",78,82,72,70,65,85,68,90))
ideas.append(mk("gl061","The Arrest Race Gap by State","Arrests broken down by race from national arrest database","MAP","US-State","State choropleth","Crime and Law Enforcement","D:/raw_data/Sage_Data/Arrests by Race from the Arrests Database.csv",80,78,68,72,85,78,65,90))
ideas.append(mk("gl062","Americas Religious Congregations: Where Faith Gathers","Number of congregations per capita by county","MAP","US-County","County choropleth","Demographics","D:/raw_data/Sage_Data/Number of Congregations from the U.S. Religion Census Database.xlsx",65,72,70,68,55,78,68,88))
ideas.append(mk("gl063","The Jail Inequality Map","Inmates by race as share of jail population vs general population by state","MAP","US-State","Bivariate choropleth","Crime and Law Enforcement","D:/raw_data/Sage_Data/Inmates by Race from the Annual Survey of Jails (United States) Database.csv",82,75,68,72,88,78,70,88))
ideas.append(mk("gl064","Americas Marijuana Belt","Past-month marijuana use rates by state from NSDUH survey","MAP","US-State","State choropleth","Health","D:/raw_data/Sage_Data/Marijuana Use in the Past Month from the National Survey on Drug Use and Health (NSDUH), 2015-2019 [Archive] Database.csv",70,82,75,68,58,75,62,90))
ideas.append(mk("gl065","Real Personal Income: Where Your Dollar Goes Furthest","Cost-of-living adjusted personal income by state using regional price parities","MAP","US-State","State choropleth","Economy","D:/raw_data/Sage_Data/Real Personal Income and Regional Price Parities from the Regional Personal Income and Employment Database.csv",72,88,82,68,62,78,60,95))
ideas.append(mk("gl066","Cars Per Capita: Americas Most Vehicle-Dependent States","Total registered vehicles per capita by state","MAP","US-State","State choropleth","Transportation","D:/raw_data/Sage_Data/Total Vehicles Registered from the All Motor Vehicles  (Private + Public; Registered Vehicles) Database (1).csv",60,78,78,65,50,72,58,92))
ideas.append(mk("gl067","NAEP Scores by State: Americas Education Report Card","National Assessment of Educational Progress scores mapped","MAP","US-State","State choropleth","Education","D:/raw_data/Sage_Data/Assessment by All Students from the National Assessment of Educational Progress (NAEP) Database.csv",70,82,78,62,65,75,58,92))

# ============================================================
# MBTA SHAPEFILES (Boston transit data 2025)
# ============================================================
ideas.append(mk("gl068","Bostons Transit Desert: Where the T Doesnt Go","MBTA service coverage gaps overlaid with demographic data","MAP","US-City","Dot map","Transportation","D:/raw_data/MBTA Data 2025/MBTA_Extended_Service_Area/MBTA_Extended_Service_Area.shp",75,78,72,70,72,82,72,88))
ideas.append(mk("gl069","Every Bus Stop in Boston: A Transit Density Map","All 7,700+ MBTA bus stops mapped showing transit infrastructure density","MAP","US-City","Dot map","Transportation","D:/raw_data/MBTA Data 2025/Bus_Stops/Bus_Stops.shp",60,72,75,65,50,85,68,95))
ideas.append(mk("gl070","Bostons Commuter Rail Network Visualized","Full MBTA commuter rail system with stations and routes","MAP","US-City","Line map","Transportation","D:/raw_data/MBTA Data 2025/Commuter_Rail_Routes/Commuter_Rail_Routes.shp",55,68,78,58,48,85,62,95))

# ============================================================
# WALKABILITY INDEX (National GDB)
# ============================================================
ideas.append(mk("gl071","The Most Walkable Places in America","National Walkability Index scores mapped at the census block group level","MAP","US","County choropleth","Transportation","D:/raw_data/WalkabilityIndex/Natl_WI.gdb",78,88,78,68,60,85,65,95))

# ============================================================
# WORLD CUP DATA
# ============================================================
ideas.append(mk("gl072","Every World Cup Match Ever Played: 1930-2022","Complete results of all FIFA World Cup matches mapped and visualized","MAP","World","World choropleth","Sports & Recreation","D:/raw_data/worldcup/matches_1930_2022.csv",68,78,75,62,55,78,65,95))
ideas.append(mk("gl073","FIFA World Rankings: The Global Football Hierarchy","Current FIFA rankings mapped showing football power centers","MAP","World","World choropleth","Sports & Recreation","D:/raw_data/worldcup/fifa_ranking_2022-10-06.csv",60,75,78,58,50,80,55,92))

# ============================================================
# HSUS (Historical Statistics of the US)
# ============================================================
ideas.append(mk("gl074","Americas Slave Population by State: 1790-1860","Historical census data showing the geography of slavery decade by decade","MAP","US-State","Animated choropleth","History","D:/raw_data/HSUS/A-Population/aaPopulation-Characteristics/Slave Population/Aa2093-2140.xls",90,82,72,72,92,85,78,85))
ideas.append(mk("gl075","200 Years of U.S. State Populations","Animated map of state populations from 1790 to present","MAP","US-State","Animated choropleth","Demographics","D:/raw_data/HSUS/A-Population/aaPopulation-Characteristics/State Populations/Aa2244-2340.xls",72,80,75,68,65,85,70,85))
ideas.append(mk("gl076","Americas Urban Explosion: Rural to Urban Shift Since 1790","Share of population in urban vs rural areas over 230 years","CHART","US","Stacked area chart","Demographics","D:/raw_data/HSUS/A-Population/aaPopulation-Characteristics/Rural and Urban Places/Aa684-698.xls",70,78,75,68,65,78,65,82))
ideas.append(mk("gl077","The Foreign-Born Population of America: 1850 to Today","Nativity data showing waves of immigration across U.S. history","CHART","US","Stacked area chart","Demographics","D:/raw_data/HSUS/A-Population/aaPopulation-Characteristics/Nativity/Aa1896-1921.xls",75,80,72,70,72,75,68,82))
ideas.append(mk("gl078","The Hispanic Growth Wave: Population by State Since 1980","Hispanic population growth mapped by state over 4 decades","MAP","US-State","Animated choropleth","Demographics","D:/raw_data/HSUS/A-Population/aaPopulation-Characteristics/Hispanic Population/Aa2189-2215.xls",72,82,75,65,68,80,62,82))
ideas.append(mk("gl079","How America Aged: Sex and Age Distribution Since 1790","Population pyramids for the U.S. animated from founding to present","CHART","US","Animated bar chart","Demographics","D:/raw_data/HSUS/A-Population/aaPopulation-Characteristics/Sex, Age, Race, and Marital Status/Aa110-124.xls",70,78,72,68,65,82,68,80))

# ============================================================
# AIRBNB (Boston data)
# ============================================================
ideas.append(mk("gl080","Bostons Airbnb Pricing Heat Map","Average nightly Airbnb prices by neighborhood in Boston","MAP","US-City","Dot map","Housing","D:/raw_data/airbnb/bosotn/part-00385-88821d72-4721-46b8-b7e6-f25dd1c1dd91.c000.csv",68,80,78,62,55,82,60,88))

print(f"BATCH_GL: {len(ideas)} ideas generated")

# === INJECTION LOGIC ===
with open(DATA_JS, encoding="utf-8") as f:
    raw = f.read()

existing_ids = set(re.findall(r'id:"([^"]+)"', raw))
new_ideas = []
skipped = 0
for idea in ideas:
    m = re.search(r'id:"([^"]+)"', idea)
    if m and m.group(1) not in existing_ids:
        new_ideas.append(idea)
    else:
        skipped += 1

tail = "]; // end D"
if tail not in raw:
    print("[BATCH_GL] ERROR: tail marker not found in data.js")
    sys.exit(1)

raw = raw.replace(tail, "")
for idea in new_ideas:
    raw += idea + ",\n"
raw += tail + "\n"

with open(DATA_JS, "w", encoding="utf-8") as f:
    f.write(raw)

print(f"[BATCH_GL] Injected {len(new_ideas)} new ideas (skipped {skipped} dupes)")
