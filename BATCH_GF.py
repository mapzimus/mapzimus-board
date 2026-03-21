"""
BATCH_GF.py — US-focused deep dive: FBI granular, Census, schools, FTE extras,
public health, economic, food, entertainment, sports
Gap-fill: Entertainment (23), Food & Nutrition (34), Sports (43), Climate (10), Treemap, Dot map
"""
import re, sys

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
# ENTERTAINMENT gap-fill (only 23 ideas!)
# ============================================================
ideas.append(mk("ent_oscar_diversity_timeline","The Oscars Diversity Problem in Numbers","Best Picture and Best Director nominees by race and gender 1929-2025","CHART","us_national","Bar chart","Entertainment","Academy Awards database https://www.oscars.org/oscars/ceremonies",75,70,75,60,75,60,60,90))
ideas.append(mk("ent_netflix_most_watched_map","What the World Watches on Netflix","Most popular Netflix titles by country show cultural divides","MAP","worldwide","World choropleth","Entertainment","Netflix Top 10 Global data https://top10.netflix.com",60,80,75,65,35,85,55,90))
ideas.append(mk("ent_video_game_revenue_vs_movies","Video Games Make More Money Than Movies and Music Combined","Annual revenue comparison of gaming vs film vs music industries","CHART","worldwide","Bar chart","Entertainment","Newzoo + MPAA + IFPI industry reports https://newzoo.com",55,75,80,75,30,65,60,90))
ideas.append(mk("ent_spotify_streams_by_country","Where People Stream the Most Music","Spotify streams per capita by country","MAP","worldwide","World choropleth","Entertainment","Spotify/Luminate streaming data https://newsroom.spotify.com",55,75,80,60,30,85,55,85))
ideas.append(mk("ent_book_bans_by_state","Book Bans Are Surging in American Schools","Number of books challenged or banned by state in 2023-2024","MAP","us_state","State choropleth","Entertainment","ALA Banned Books data https://www.ala.org/advocacy/bbooks",80,80,75,65,85,80,60,90))
ideas.append(mk("ent_movie_budgets_vs_returns","Hollywood Spends More But Earns Less","Average movie budget has tripled but average ROI has fallen","CHART","worldwide","Scatter plot","Entertainment","The Numbers movie database https://www.the-numbers.com",55,65,75,70,45,60,65,90))
ideas.append(mk("ent_theme_park_attendance","The Worlds Most Visited Theme Parks","Annual attendance at top 25 theme parks globally","RANK","worldwide","Bar chart","Entertainment","TEA/AECOM Theme Index https://aecom.com/theme-index/",45,70,80,55,25,60,50,90))
ideas.append(mk("ent_podcast_listening_by_age","The Podcast Generation Gap","Weekly podcast listening rates by age group show massive generational divide","CHART","us_national","Bar chart","Entertainment","Edison Research Infinite Dial https://www.edisonresearch.com",55,80,80,55,30,60,50,90))
ideas.append(mk("ent_box_office_china_vs_us","When China Overtook Americas Box Office","Annual box office revenue US vs China 2010-2025","CHART","worldwide","Line chart","Entertainment","Comscore + Maoyan box office data https://www.comscore.com",55,60,80,70,40,60,60,90))
ideas.append(mk("ent_esports_prize_pools","Esports Prize Pools Now Rival Traditional Sports","Top tournament prize pools in gaming vs tennis golf etc","RANK","worldwide","Bar chart","Entertainment","Esports Earnings database https://www.esportsearnings.com",50,65,80,70,30,55,65,90))
ideas.append(mk("ent_social_media_users_by_platform","The Rise and Fall of Social Media Platforms","Monthly active users for every major platform from 2004 to 2025","CHART","worldwide","Area chart","Entertainment","DataReportal + Statista + company reports https://datareportal.com",60,85,80,55,40,70,50,95))
ideas.append(mk("ent_music_genre_popularity_shift","How Americas Music Taste Changed in 30 Years","Genre share of recorded music revenue from 1990 to today","CHART","us_national","Area chart","Entertainment","RIAA sales data https://www.riaa.com/u-s-sales-database/",60,80,75,60,35,70,55,90))
ideas.append(mk("ent_tv_ratings_decline","TV Ratings Have Collapsed","Average viewers for top-rated shows from 1960 to today","CHART","us_national","Line chart","Entertainment","Nielsen ratings historical data https://www.nielsen.com",55,80,80,60,40,60,55,90))

# ============================================================
# FOOD & NUTRITION gap-fill (only 34 ideas!)
# ============================================================
ideas.append(mk("food_fast_food_density_map","Fast Food Restaurants Per Capita by County","The geography of fast food access in America","MAP","us_county","County choropleth","Food & Nutrition","Census County Business Patterns + USDA Food Atlas https://www.census.gov/programs-surveys/cbp.html",55,80,80,55,40,85,50,95))
ideas.append(mk("food_food_deserts_map","Americas Food Deserts","USDA food desert census tracts where residents lack nearby grocery stores","MAP","us_national","Dot map","Food & Nutrition","USDA Food Access Research Atlas https://www.ers.usda.gov/data-products/food-access-research-atlas/",80,80,80,60,65,85,50,95))
ideas.append(mk("food_obesity_rate_by_state","Obesity Rates by State","Adult obesity prevalence ranges from 24% to 42% across states","MAP","us_state","State choropleth","Food & Nutrition","CDC BRFSS https://www.cdc.gov/brfss/",70,85,85,50,55,80,40,95))
ideas.append(mk("food_organic_farm_growth","The Organic Farming Boom","Certified organic farms in the US have tripled since 2000","CHART","us_national","Line chart","Food & Nutrition","USDA NASS Census of Agriculture https://www.nass.usda.gov/",50,60,80,55,35,60,55,90))
ideas.append(mk("food_meat_consumption_world","The Worlds Biggest Meat Eaters","Meat consumption per capita by country","MAP","worldwide","World choropleth","Food & Nutrition","FAO + OWID https://ourworldindata.org/meat-production",60,75,85,55,45,85,50,95))
ideas.append(mk("food_sugar_consumption_100yr","Americas Sugar Addiction Over 100 Years","Per capita sugar consumption has tripled since 1900","CHART","us_national","Line chart","Food & Nutrition","USDA ERS Sugar and Sweeteners data https://www.ers.usda.gov",65,80,80,60,50,60,55,90))
ideas.append(mk("food_farm_size_concentration","Farms Are Getting Bigger and Fewer","Average farm size and number of farms since 1900","CHART","us_national","Line chart","Food & Nutrition","USDA NASS Census of Agriculture https://www.nass.usda.gov/",55,60,80,60,45,60,55,90))
ideas.append(mk("food_calorie_sources_shift","Where Americas Calories Come From Has Changed Drastically","Fat sugar and grain consumption per capita over 50 years","CHART","us_national","Area chart","Food & Nutrition","USDA ERS Loss-Adjusted Food Availability https://www.ers.usda.gov",55,75,75,60,40,65,55,90))
ideas.append(mk("food_coffee_consumption_world","The Worlds Biggest Coffee Drinkers","Annual coffee consumption per capita - Scandinavians drink the most","MAP","worldwide","World choropleth","Food & Nutrition","ICO + FAO coffee consumption data https://www.ico.org",55,80,85,55,30,85,50,90))
ideas.append(mk("food_restaurant_spending_vs_grocery","Americans Now Spend More Eating Out Than Cooking","Restaurant spending surpassed grocery spending for the first time","CHART","us_national","Line chart","Food & Nutrition","BLS CES + Census Retail Trade https://www.bls.gov",60,85,80,65,40,60,55,95))

# ============================================================
# SPORTS gap-fill (only 43 ideas!)
# ============================================================
ideas.append(mk("sport_nfl_stadium_map","Every NFL Stadium in America","32 stadiums mapped with capacity and age","MAP","us_national","Dot map","Sports & Recreation","NFL stadium data https://www.nfl.com",45,75,80,40,25,85,45,95))
ideas.append(mk("sport_athlete_salary_by_sport","Highest Paid Athletes by Sport","Average and max salaries across MLB NBA NFL NHL MLS","RANK","us_national","Bar chart","Sports & Recreation","Spotrac + public salary data https://www.spotrac.com",50,75,80,60,35,55,50,90))
ideas.append(mk("sport_super_bowl_viewership","Super Bowl Viewership Over 58 Years","From 51 million in 1967 to 123 million in 2024","CHART","us_national","Line chart","Sports & Recreation","Nielsen + NFL viewership data https://www.nielsen.com",50,80,85,50,30,60,45,95))
ideas.append(mk("sport_college_athletics_revenue","College Sports Is a Billion Dollar Business","Athletic department revenue by school - football subsidizes everything","RANK","us_national","Bar chart","Sports & Recreation","NCAA Financial Database + DOE Equity in Athletics https://ope.ed.gov/athletics/",55,70,80,60,55,55,55,90))
ideas.append(mk("sport_marathon_times_improving","Marathon World Records Keep Falling","The progression of marathon world record times from 1900 to today","CHART","worldwide","Line chart","Sports & Recreation","World Athletics records database https://worldathletics.org",45,55,85,50,25,60,50,95))
ideas.append(mk("sport_soccer_transfer_inflation","Soccer Transfer Fees Have Gone Insane","Top transfer fees by year from 1990 to present","CHART","worldwide","Scatter plot","Sports & Recreation","Transfermarkt data https://www.transfermarkt.com",50,65,80,65,35,60,55,90))
ideas.append(mk("sport_youth_sports_decline","American Kids Are Quitting Sports","Youth sports participation has dropped 30% in two decades","CHART","us_national","Line chart","Sports & Recreation","Aspen Institute Project Play + SFIA https://www.aspenprojectplay.org",70,80,75,65,55,60,55,90))
ideas.append(mk("sport_olympics_host_cities","Every Olympics Host City Mapped","Summer and Winter Olympic host cities from 1896 to 2032","MAP","worldwide","Dot map","Sports & Recreation","IOC official data https://olympics.com",45,60,80,50,25,85,50,95))
ideas.append(mk("sport_cte_nfl_players","The CTE Crisis in Football","Percentage of deceased NFL players diagnosed with CTE by position","CHART","us_national","Bar chart","Sports & Recreation","Boston University CTE Center https://www.bu.edu/cte/",80,70,75,65,80,55,55,90))
ideas.append(mk("sport_baseball_analytics_shift","The Moneyball Revolution in Numbers","How batting average declined while walks and strikeouts skyrocketed","CHART","us_national","Line chart","Sports & Recreation","Baseball Reference + FanGraphs https://www.baseball-reference.com",45,65,80,60,30,60,60,95))

# ============================================================
# CLIMATE gap-fill (only 10 ideas!)
# ============================================================
ideas.append(mk("climate_warming_stripes_us","Americas Warming Stripes","Annual average temperature by state since 1895 as warming stripes","MAP","us_state","State choropleth","Climate","NOAA Climate at a Glance https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/",70,75,85,55,70,80,55,95))
ideas.append(mk("climate_sea_level_projections","Sea Level Rise Will Swallow Coastlines","Projected sea level rise under different scenarios to 2100","CHART","worldwide","Area chart","Climate","NOAA Sea Level Rise + IPCC AR6 https://tidesandcurrents.noaa.gov/sltrends/",80,75,80,65,80,65,55,95))
ideas.append(mk("climate_wildfire_acres_burned","Wildfire Acres Burned Have Doubled Since 2000","Annual acres burned in US wildfires from 1983 to present","CHART","us_national","Bar chart","Climate","NIFC Wildfire Statistics https://www.nifc.gov/fire-information/statistics",75,75,85,60,70,60,45,95))
ideas.append(mk("climate_billion_dollar_disasters","Billion Dollar Weather Disasters Are Accelerating","Number of billion-dollar climate disasters by year since 1980","CHART","us_national","Bar chart","Climate","NOAA Billion-Dollar Weather and Climate Disasters https://www.ncei.noaa.gov/access/billions/",75,80,85,65,70,65,50,95))
ideas.append(mk("climate_arctic_ice_minimum","The Vanishing Arctic","September Arctic sea ice extent from 1979 to present","CHART","worldwide","Line chart","Climate","NSIDC Sea Ice Index https://nsidc.org/data/seaice_index",75,60,85,60,80,60,50,95))
ideas.append(mk("climate_hottest_years_ever","The 10 Hottest Years on Record All Happened Recently","Global average temperature anomaly by year since 1880","CHART","worldwide","Bar chart","Climate","NASA GISS Surface Temperature Analysis https://data.giss.nasa.gov/gistemp/",75,75,85,55,75,65,45,95))
ideas.append(mk("climate_flood_risk_coastal_cities","Which Coastal Cities Face the Worst Flood Risk","Population in the 100-year flood zone by major coastal city","RANK","worldwide","Bar chart","Climate","Climate Central Coastal Risk Screening https://www.climatecentral.org",80,75,80,65,80,60,60,90))
ideas.append(mk("climate_renewable_energy_growth_state","Americas Renewable Energy Leaders by State","Share of electricity from renewables by state","MAP","us_state","State choropleth","Climate","EIA State Energy Data System https://www.eia.gov/electricity/data/state/",60,70,85,55,55,80,50,95))
ideas.append(mk("climate_carbon_footprint_by_income","The Rich Pollute More","Per capita CO2 emissions by income decile within countries","CHART","worldwide","Bar chart","Climate","Oxfam + World Inequality Database https://wid.world",75,70,75,75,70,60,70,85))
ideas.append(mk("climate_permafrost_thaw_map","Permafrost Is Thawing Across the Arctic","Ground temperature changes in permafrost regions since 1950","MAP","worldwide","Special map","Climate","NSIDC + Copernicus Climate Data https://nsidc.org",70,45,75,70,75,80,65,85))
ideas.append(mk("climate_heat_related_deaths","Heat Is Americas Deadliest Weather Event","Heat-related deaths by state and year show an accelerating trend","MAP","us_state","State choropleth","Climate","CDC WONDER + NWS https://wonder.cdc.gov",80,80,80,60,70,80,50,90))
ideas.append(mk("climate_glacier_retreat","The Worlds Glaciers Are Disappearing","Cumulative glacier mass loss worldwide since 1960","CHART","worldwide","Line chart","Climate","WGMS Glacier Monitoring Data https://wgms.ch",70,55,80,60,75,60,55,90))

# ============================================================
# SCIENCE & TECHNOLOGY gap-fill (only 34 ideas!)
# ============================================================
ideas.append(mk("tech_ai_investment_by_country","The AI Arms Race by Country","Annual private AI investment by nation - US and China dominate","MAP","worldwide","World choropleth","Science & Technology","Stanford AI Index https://aiindex.stanford.edu",60,60,80,70,65,85,60,90))
ideas.append(mk("tech_broadband_speed_by_state","Internet Speed Varies 5x Across States","Average broadband download speeds by state","MAP","us_state","State choropleth","Science & Technology","Ookla Speedtest Intelligence + FCC https://www.speedtest.net/global-index",55,80,80,55,35,80,50,95))
ideas.append(mk("tech_stem_workforce_by_state","Americas STEM Workers Are Concentrated in a Few States","Share of workforce in STEM occupations by state","MAP","us_state","State choropleth","Science & Technology","BLS OES + NSF Science and Engineering Indicators https://www.bls.gov/oes/",55,70,80,60,35,80,50,95))
ideas.append(mk("tech_patent_filings_by_country","Who Files the Most Patents","Annual patent applications by country - China now leads the world","MAP","worldwide","World choropleth","Science & Technology","WIPO IP Statistics https://www.wipo.int/ipstats/",50,50,80,65,40,85,55,95))
ideas.append(mk("tech_smartphone_adoption_by_country","The Smartphone Conquered the World in 10 Years","Smartphone ownership rates by country from 2010 to present","MAP","worldwide","World choropleth","Science & Technology","Pew Global + GSMA Intelligence https://www.gsma.com/mobileeconomy/",55,75,80,55,30,85,45,95))
ideas.append(mk("tech_space_launches_by_country","The New Space Race","Annual orbital launches by country - China and SpaceX changed everything","CHART","worldwide","Area chart","Science & Technology","UCS Satellite Database + Jonathan McDowell https://planet4589.org/space/gcat/",55,55,80,70,45,70,65,95))
ideas.append(mk("tech_nuclear_reactors_map","Every Nuclear Power Plant on Earth","Operating nuclear reactors mapped by country and capacity","MAP","worldwide","Dot map","Science & Technology","IAEA Power Reactor Information System https://pris.iaea.org",50,50,80,55,50,85,55,95))
ideas.append(mk("tech_ev_sales_by_country","The Electric Vehicle Revolution by Country","EV market share of new car sales by country","MAP","worldwide","World choropleth","Science & Technology","IEA Global EV Data Explorer https://www.iea.org/data-and-statistics/data-tools/global-ev-data-explorer",55,65,80,60,40,85,50,95))
ideas.append(mk("tech_scientific_papers_by_country","Which Countries Produce the Most Science","Annual scientific publications by country","MAP","worldwide","World choropleth","Science & Technology","Scopus + NSF Science and Engineering Indicators https://www.nsf.gov/statistics/seind/",45,45,80,55,35,85,55,95))
ideas.append(mk("tech_semiconductor_manufacturing","The World Depends on a Few Chip Factories","Global semiconductor manufacturing capacity by country - TSMC dominates","CHART","worldwide","Treemap","Science & Technology","SIA + SEMI semiconductor data https://www.semiconductors.org",60,55,80,75,65,70,70,90))

# ============================================================
# MORE US-FOCUSED IDEAS (Census, health, economy)
# ============================================================
ideas.append(mk("us_languages_spoken_map","Americas Linguistic Map","Most common non-English language spoken at home by county","MAP","us_county","County choropleth","Demographics","Census ACS B16001 https://data.census.gov",60,75,80,65,45,85,55,95))
ideas.append(mk("us_commute_times_by_county","Americas Longest Commutes","Average one-way commute time by county","MAP","us_county","County choropleth","Transportation","Census ACS B08303 https://data.census.gov",60,85,80,55,45,85,50,95))
ideas.append(mk("us_median_age_by_county","Americas Youngest and Oldest Counties","Median age by county shows college towns vs retirement havens","MAP","us_county","County choropleth","Demographics","Census ACS B01002 https://data.census.gov",55,70,80,55,35,85,50,95))
ideas.append(mk("us_health_insurance_uninsured","Where Americans Dont Have Health Insurance","Uninsured rate by county varies from 3% to 30%","MAP","us_county","County choropleth","Health","Census ACS + CDC https://data.census.gov",75,80,80,55,65,85,45,95))
ideas.append(mk("us_veteran_population_map","Where Americas Veterans Live","Veteran population share by county","MAP","us_county","County choropleth","Demographics","Census ACS B21001 https://data.census.gov",55,65,80,50,40,85,50,95))
ideas.append(mk("us_poverty_rate_by_county","The Geography of Poverty in America","Poverty rate by county shows persistent pockets in the South and Appalachia","MAP","us_county","County choropleth","Economy","Census ACS S1701 https://data.census.gov",80,80,85,50,65,85,40,95))
ideas.append(mk("us_home_ownership_by_county","Where Americans Own vs Rent","Homeownership rate by county","MAP","us_county","County choropleth","Housing","Census ACS B25003 https://data.census.gov",55,80,80,50,40,85,45,95))
ideas.append(mk("us_broadband_access_rural","Rural Americas Digital Divide","Share of households without broadband internet by county","MAP","us_county","County choropleth","Science & Technology","Census ACS + FCC Broadband Data https://broadbandmap.fcc.gov",70,75,80,55,55,85,50,95))
ideas.append(mk("us_overdose_deaths_by_county","Americas Overdose Crisis County by County","Drug overdose death rates by county","MAP","us_county","County choropleth","Health","CDC WONDER Multiple Cause of Death https://wonder.cdc.gov",85,80,80,55,80,85,45,95))
ideas.append(mk("us_life_expectancy_by_county","Your Zip Code Determines How Long You Live","Life expectancy at birth varies 20 years between Americas best and worst counties","MAP","us_county","County choropleth","Health","CDC US Small-area Life Expectancy Estimates https://www.cdc.gov/nchs/nvss/usaleep/usaleep.html",85,85,80,65,75,85,50,95))
ideas.append(mk("us_median_income_by_county","Americas Income Map","Median household income by county from under 25K to over 150K","MAP","us_county","County choropleth","Economy","Census ACS B19013 https://data.census.gov",60,80,85,45,45,85,40,95))
ideas.append(mk("us_college_degree_by_county","Americas Education Divide","Share of adults with bachelors degree by county","MAP","us_county","County choropleth","Education","Census ACS S1501 https://data.census.gov",55,75,80,50,45,85,45,95))
ideas.append(mk("us_gun_store_density","Gun Stores Per Capita by State","Federal firearms licensees per 100K residents by state","MAP","us_state","State choropleth","Crime and Law Enforcement","ATF Federal Firearms License data https://www.atf.gov/firearms/listing-federal-firearms-licensees",60,70,80,65,60,80,55,95))
ideas.append(mk("us_maternal_mortality_state","Americas Maternal Mortality Crisis","Maternal deaths per 100K births by state - US worst among rich nations","MAP","us_state","State choropleth","Health","CDC WONDER + WHO https://wonder.cdc.gov",85,75,80,65,80,80,55,90))
ideas.append(mk("us_student_loan_debt_state","Student Loan Debt by State","Average student debt at graduation varies from 20K to 40K by state","MAP","us_state","State choropleth","Education","TICAS Project on Student Debt https://ticas.org",70,85,80,55,60,80,45,90))
ideas.append(mk("us_minimum_wage_map","The Minimum Wage Patchwork","State and local minimum wages range from 7.25 to 17 dollars","MAP","us_state","State choropleth","Labor","DOL Minimum Wage data https://www.dol.gov/agencies/whd/minimum-wage/state",65,85,85,55,55,80,45,95))

# ============================================================
# TREEMAP gap-fill (only 10 ideas!)
# ============================================================
ideas.append(mk("tree_federal_budget","Where Your Tax Dollars Go","Federal budget spending by department and program as a treemap","CHART","us_national","Treemap","Economy","USAspending.gov https://www.usaspending.gov",65,85,85,55,50,75,50,95))
ideas.append(mk("tree_world_gdp","The World Economy at a Glance","Every countrys GDP as a share of the global total","CHART","worldwide","Treemap","Economy","World Bank GDP data https://data.worldbank.org",55,60,85,50,30,75,45,95))
ideas.append(mk("tree_us_energy_sources","Americas Energy Sources","US energy consumption by source as a treemap","CHART","us_national","Treemap","Environment","EIA Monthly Energy Review https://www.eia.gov/totalenergy/data/monthly/",50,60,85,45,35,75,45,95))
ideas.append(mk("tree_global_religions","The Worlds Religions by Size","Global religious affiliation as a treemap","CHART","worldwide","Treemap","Demographics","Pew Research Center + ARDA https://www.pewresearch.org/religion/",55,65,80,50,40,75,50,90))
ideas.append(mk("tree_us_imports_by_country","Where Americas Imports Come From","US imports by country of origin as a treemap","CHART","us_national","Treemap","Economy","Census Bureau Foreign Trade https://www.census.gov/foreign-trade/",50,60,85,50,40,75,50,95))
ideas.append(mk("tree_causes_of_death_us","What Actually Kills Americans","Annual causes of death in the US as a treemap","CHART","us_national","Treemap","Health","CDC WONDER Leading Causes of Death https://wonder.cdc.gov",70,80,85,50,40,75,45,95))
ideas.append(mk("tree_global_arms_trade","Who Sells Weapons to Whom","Global arms exports by country and recipient as a treemap","CHART","worldwide","Treemap","History","SIPRI Arms Transfers Database https://www.sipri.org/databases/armstransfers",60,50,80,70,70,75,65,90))
ideas.append(mk("tree_us_crop_production","Americas Agricultural Output","US crop production by type as a treemap - corn dominates everything","CHART","us_national","Treemap","Food & Nutrition","USDA NASS Crop Production https://www.nass.usda.gov/",45,55,80,50,30,75,50,95))

# ============================================================
# INJECTION LOGIC
# ============================================================
with open(DATA_JS, encoding="utf-8") as f:
    raw = f.read()
existing_ids = set(re.findall(r'id:"([^"]+)"', raw))
print("Existing ideas: %d" % len(existing_ids))
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
tail = "]; // end D"
if tail not in raw:
    print("ERROR: Cannot find tail marker")
    sys.exit(1)
raw = raw.replace(tail, "")
for idea in new_ideas:
    raw += idea + ",\n"
raw += tail + "\n"
with open(DATA_JS, "w", encoding="utf-8") as f:
    f.write(raw)
print("Injected %d ideas. Total now: %d" % (len(new_ideas), len(existing_ids) + len(new_ideas)))
