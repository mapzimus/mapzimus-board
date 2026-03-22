"""
BATCH_GK.py — Cross-reference ideas: novel combos between new Kaggle datasets
and existing data sources. Patterns, correlations, and surprising connections.
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
# UFO x GEOGRAPHY / DEMOGRAPHICS / MILITARY
# ============================================================
ideas.append(mk("xr_ufo_vs_military_bases","UFO Sightings Cluster Near Military Bases","UAP report density vs proximity to DOD installations","XREF","us_national","Dot map","Science & Technology","Kaggle UAP + DOD Base Structure Report",65,55,80,75,55,90,75,80))
ideas.append(mk("xr_ufo_vs_population_density","Do More People Just Mean More UFO Reports","UFO sighting rate per capita by state vs population density","XREF","us_state","Bivariate choropleth","Science & Technology","Kaggle UAP + Census ACS",50,55,80,65,35,85,60,90))
ideas.append(mk("xr_ufo_vs_light_pollution","UFO Sightings Track Light Pollution Not Aliens","Sighting density vs dark sky index by county","XREF","us_county","Bivariate choropleth","Science & Technology","Kaggle UAP + NOAA VIIRS Nighttime Lights",55,50,80,75,40,85,75,75))
ideas.append(mk("xr_ufo_vs_drinking_rates","States That Drink More Report More UFOs","Alcohol consumption per capita vs UFO sighting rate by state","XREF","us_state","Scatter plot","Science & Technology","Kaggle UAP + NIAAA Alcohol Epidemiologic Data",50,60,80,80,35,60,80,80))
ideas.append(mk("xr_ufo_shapes_over_time","UFO Shapes Have Changed With Popular Culture","Triangle sightings spiked after stealth bomber reveal in 1988","CHART","us_national","Area chart","Science & Technology","Kaggle UAP reports shape + datetime fields",55,55,80,75,40,60,75,95))

# ============================================================
# IRAN WAR x ECONOMY / ENERGY / ELECTIONS
# ============================================================
ideas.append(mk("xr_iran_gas_vs_ev_adoption","Iran War Gas Spike Accelerates EV Sales","States with biggest gas price increases vs EV registration growth","XREF","us_state","Bivariate choropleth","Economy","Kaggle Iran War Gas + DOE AFDC EV Data",65,70,80,65,55,85,70,80))
ideas.append(mk("xr_iran_gas_vs_commute_cost","The Iran War Tax on American Commuters","Gas price increase x average commute distance by state","XREF","us_state","State choropleth","Economy","Kaggle Iran War Gas + Census ACS commute data",75,85,85,55,65,80,60,90))
ideas.append(mk("xr_iran_oil_vs_historical_crises","2026 Iran War Oil Spike vs Every Past Oil Crisis","Overlaid oil price charts for 1973 1979 1990 2008 2022 2026","XREF","worldwide","Line chart","Economy","Kaggle Iran War Oil + Historical Oil Prices",65,60,80,70,70,65,60,95))
ideas.append(mk("xr_iran_gas_vs_approval_rating","Gas Prices and Presidential Approval Move Together","Iran war gas spike timeline vs presidential approval polls","XREF","us_national","Line chart","Elections","Kaggle Iran War Gas + Gallup/538 Approval Data",65,70,80,60,65,60,60,75))
ideas.append(mk("xr_iran_reaction_vs_oil_dependence","Countries Dependent on Iranian Oil Stayed Neutral","International reaction stance vs Iranian oil import share","XREF","worldwide","World choropleth","International Statistics","Kaggle Iran War Reactions + EIA Oil Trade Data",60,45,80,70,65,80,70,80))

# ============================================================
# FOOTBALL x GEOPOLITICS / ECONOMICS / DEMOGRAPHICS
# ============================================================
ideas.append(mk("xr_football_wins_vs_gdp","Rich Countries Win More Football Matches","All-time win percentage vs GDP per capita by country","XREF","worldwide","Scatter plot","Sports & Recreation","Kaggle Football Results + World Bank GDP",50,50,80,60,40,60,65,90))
ideas.append(mk("xr_football_vs_conflict","Countries at War Still Play Football","International matches played during active conflicts","XREF","worldwide","Special map","History","Kaggle Football Results + UCDP Armed Conflict Data",55,45,80,75,55,70,80,75))
ideas.append(mk("xr_football_home_vs_altitude","Altitude Explains Home Advantage","Home win rate vs stadium altitude - Bolivia La Paz effect","XREF","worldwide","Scatter plot","Sports & Recreation","Kaggle Football Results + Geographic elevation data",45,50,80,75,40,60,80,80))
ideas.append(mk("xr_football_goals_vs_population","Bigger Countries Score More Goals","Population vs all-time international goals scored","XREF","worldwide","Scatter plot","Sports & Recreation","Kaggle Football + World Population",40,45,80,55,30,60,55,90))
ideas.append(mk("xr_football_renamed_nations_map","Playing Football Under a Different Flag","36 nations that changed names mapped with their football history","MAP","worldwide","Special map","History","Kaggle Football former_names + World Map",50,45,80,70,40,80,75,95))

# ============================================================
# BREAKFAST PRICES x ECONOMY / WAGES / QUALITY OF LIFE
# ============================================================
ideas.append(mk("xr_breakfast_vs_minimum_wage","How Many Hours of Work to Buy Breakfast","Breakfast basket cost vs local minimum wage by country","XREF","worldwide","World choropleth","Food & Nutrition","Kaggle Breakfast Basket + ILO Wage Data",70,80,80,65,55,80,65,80))
ideas.append(mk("xr_breakfast_vs_gdp","Breakfast Costs Track GDP Almost Perfectly","Breakfast basket price vs GDP per capita by country","XREF","worldwide","Scatter plot","Food & Nutrition","Kaggle Breakfast Basket + World Bank GDP",45,55,80,55,30,60,50,90))
ideas.append(mk("xr_egg_price_vs_avian_flu","Avian Flu Outbreaks Spike Egg Prices Globally","Egg price inflation by region vs H5N1 outbreak timeline","XREF","worldwide","Line chart","Food & Nutrition","Kaggle Breakfast Basket + WHO Avian Flu Reports",65,70,80,60,55,60,65,75))
ideas.append(mk("xr_breakfast_inflation_vs_instability","Food Inflation Predicts Political Instability","Countries with highest breakfast price increases vs political stability index","XREF","worldwide","Scatter plot","Food & Nutrition","Kaggle Breakfast Basket + WGI Political Stability",70,55,80,70,70,60,70,85))

# ============================================================
# AI x ECONOMY / EDUCATION / GEOPOLITICS
# ============================================================
ideas.append(mk("xr_ai_adoption_vs_gdp_growth","AI Adoption Correlates with GDP Growth","Countries with higher AI adoption see faster economic growth","XREF","worldwide","Scatter plot","Science & Technology","Kaggle AI Index + World Bank GDP Growth",50,50,80,60,40,60,60,90))
ideas.append(mk("xr_ai_jobs_vs_education_level","AI Jobs Require Masters Degrees in Most Countries","Education level distribution of AI job postings by country","XREF","worldwide","Bar chart","Labor","Kaggle AI Jobs + AI Index education_index",55,65,80,55,40,55,55,95))
ideas.append(mk("xr_ai_talent_vs_brain_drain","AI Talent Concentrates in Rich Countries","AI talent rank vs net migration rate by country","XREF","worldwide","Scatter plot","Science & Technology","Kaggle AI Index + UN Migration Data",55,50,80,65,50,60,65,80))
ideas.append(mk("xr_ai_regulation_vs_innovation","Heavy AI Regulation Doesnt Kill Innovation","AI regulation score vs AI research papers per capita","XREF","worldwide","Scatter plot","Science & Technology","Kaggle AI Index regulation vs research fields",55,50,80,70,50,60,70,95))
ideas.append(mk("xr_ai_investment_vs_military","Countries Investing in AI Also Spend More on Military","AI investment as share of GDP vs military spending share","XREF","worldwide","Scatter plot","Science & Technology","Kaggle AI Index + SIPRI Military Spending",50,45,80,65,55,60,70,80))

# ============================================================
# BILLIONAIRES x INEQUALITY / CORRUPTION / GEOGRAPHY
# ============================================================
ideas.append(mk("xr_billionaires_vs_poverty","Countries With Most Billionaires Also Have Most Poverty","Billionaire count vs poverty headcount by country","XREF","worldwide","Scatter plot","Economy","Kaggle Richest People + World Bank Poverty Data",75,65,80,65,70,60,65,80))
ideas.append(mk("xr_billionaires_vs_corruption","Billionaires Thrive Where Corruption Is High","Billionaire count vs corruption control index","XREF","worldwide","Scatter plot","Economy","Kaggle Richest People + WGI Corruption Index",65,55,80,70,65,60,70,80))
ideas.append(mk("xr_billionaire_cities_vs_cost_of_living","Billionaire Cities Are Unaffordable for Everyone Else","Billionaire count by city vs median rent","XREF","worldwide","Scatter plot","Housing","Kaggle Richest People + Numbeo Cost of Living",70,75,80,55,55,60,60,75))
ideas.append(mk("xr_billionaire_industry_vs_country","Tech Billionaires in America Manufacturing in Asia","Dominant billionaire industry by country mapped","MAP","worldwide","World choropleth","Economy","Kaggle Richest People industry + country fields",50,50,80,60,40,80,60,95))
ideas.append(mk("xr_billionaires_per_capita_vs_tax","Low Tax Countries Have More Billionaires Per Capita","Billionaires per million people vs top marginal tax rate","XREF","worldwide","Scatter plot","Economy","Kaggle Richest People + OECD Tax Database",55,55,80,65,50,60,65,80))

# ============================================================
# POPULATION x ENVIRONMENT / ECONOMY / CONFLICT
# ============================================================
ideas.append(mk("xr_pop_growth_vs_water_stress","Fastest Growing Populations Are in Water-Stressed Regions","Population growth rate vs water stress index by country","XREF","worldwide","Bivariate choropleth","Demographics","Kaggle World Pop + WRI Aqueduct Water Risk",70,50,80,65,70,85,65,80))
ideas.append(mk("xr_pop_decline_vs_immigration","Shrinking Countries Are Opening Borders","Population decline rate vs net immigration rate in Europe","XREF","europe","Scatter plot","Demographics","Kaggle World Pop + Eurostat Migration",55,50,80,60,50,60,60,85))
ideas.append(mk("xr_pop_growth_vs_conflict","Population Booms Precede Conflict","Youth bulge countries have higher conflict rates","XREF","worldwide","Scatter plot","Demographics","Kaggle World Pop + UCDP Armed Conflict",60,45,80,70,65,60,70,75))

# ============================================================
# SPOTIFY x CULTURE / ECONOMY / DEMOGRAPHICS
# ============================================================
ideas.append(mk("xr_spotify_country_vs_english","Non-English Songs Are Breaking Through on Spotify","Artist country vs language of top streamed songs 2025","XREF","worldwide","World choropleth","Entertainment","Kaggle Spotify artist_country + primary_genre",50,60,80,65,30,80,65,95))
ideas.append(mk("xr_spotify_bpm_vs_country","Musical Tempo Varies by Culture","Average BPM of top songs by artist country of origin","XREF","worldwide","World choropleth","Entertainment","Kaggle Spotify bpm + artist_country fields",40,50,80,65,25,80,70,95))
ideas.append(mk("xr_spotify_grammy_vs_streams","Grammys Dont Predict Spotify Success","Grammy wins vs total streams for top 50 artists","XREF","worldwide","Scatter plot","Entertainment","Kaggle Spotify grammy_wins + monthly_listeners fields",45,60,80,65,35,55,60,95))

# ============================================================
# STUDENT BURNOUT x ECONOMY / SOCIAL MEDIA / CULTURE
# ============================================================
ideas.append(mk("xr_burnout_vs_country_pressure","Academic Pressure Is Highest in Engineering Programs","Burnout level by course type - BTech leads all programs","XREF","worldwide","Bar chart","Education","Kaggle Student Burnout course + burnout_level fields",65,75,80,55,50,55,55,95))
ideas.append(mk("xr_student_attendance_vs_burnout","Burned Out Students Stop Showing Up","Attendance percentage vs burnout level","XREF","worldwide","Scatter plot","Education","Kaggle Student Burnout attendance + burnout fields",60,75,80,50,45,55,50,95))
ideas.append(mk("xr_student_anxiety_vs_study_year","First Year Students Are More Anxious","Anxiety and depression scores by year of study","XREF","worldwide","Bar chart","Education","Kaggle Student Burnout year + anxiety fields",60,75,80,55,45,55,55,95))

# ============================================================
# ECONOMY CROSS-REFS (World Bank/IMF/WGI combined)
# ============================================================
ideas.append(mk("xr_corruption_vs_gdp_growth","Corruption Kills Economic Growth","Control of corruption index vs GDP growth rate by country","XREF","worldwide","Scatter plot","Economy","Kaggle WGI Corruption + World Bank GDP Growth",55,50,80,55,50,60,55,90))
ideas.append(mk("xr_debt_vs_political_stability","Indebted Countries Are Less Stable","Government debt as pct of GDP vs political stability index","XREF","worldwide","Scatter plot","Economy","Kaggle IMF Debt + WGI Political Stability",55,45,80,60,55,60,60,85))
ideas.append(mk("xr_rule_of_law_vs_investment","Investors Follow the Rule of Law","Rule of law estimate vs foreign direct investment by country","XREF","worldwide","Scatter plot","Economy","Kaggle WGI Rule of Law + World Bank FDI",45,40,80,55,40,60,55,85))
ideas.append(mk("xr_govt_effectiveness_vs_health","Effective Governments Keep People Healthier","Government effectiveness index vs life expectancy","XREF","worldwide","Scatter plot","Health","Kaggle WGI Govt Effectiveness + WHO Life Expectancy",55,45,80,55,40,60,55,85))
ideas.append(mk("xr_agriculture_gdp_vs_hunger","Countries Dependent on Agriculture Still Go Hungry","Agriculture share of GDP vs undernourishment rate","XREF","worldwide","Scatter plot","Food & Nutrition","Kaggle World Bank Agriculture + FAO Hunger Data",65,50,80,65,55,60,65,80))

# ============================================================
# ASTEROIDS x POP CULTURE / RISK
# ============================================================
ideas.append(mk("xr_asteroid_close_calls_vs_movies","Asteroid Movies Spike After Real Close Calls","Near-miss asteroid events timeline vs disaster movie releases","XREF","worldwide","Line chart","Entertainment","Kaggle Asteroids + IMDb disaster film data",45,55,80,75,35,55,80,70))
ideas.append(mk("xr_asteroid_risk_vs_detection","We Are Finding More Asteroids Not Getting Hit More","Detection rate vs actual close approach rate over time","XREF","worldwide","Line chart","Science & Technology","Kaggle Asteroids detection + approach fields",50,45,80,65,55,55,65,95))

# ============================================================
# MEGA CROSS-REFS (3+ datasets combined)
# ============================================================
ideas.append(mk("xr_mega_iran_gas_breakfast_cost","Iran War Raised Both Gas and Grocery Prices","Gas price spike by state overlaid with breakfast basket inflation","XREF","us_state","Bivariate choropleth","Economy","Kaggle Iran War Gas + Breakfast Basket + CPI",75,85,85,55,70,85,65,80))
ideas.append(mk("xr_mega_ai_billionaires_jobs","AI Created More Billionaires Than Jobs","AI investment growth vs billionaire count in tech vs AI job postings","XREF","worldwide","Line chart","Economy","Kaggle AI Index + Richest People + AI Jobs",70,60,80,70,65,55,75,80))
ideas.append(mk("xr_mega_football_pop_gdp","Football Success = Population x Money","Country football win rate vs population x GDP interaction","XREF","worldwide","Scatter plot","Sports & Recreation","Kaggle Football + World Pop + World Bank GDP",45,50,80,60,35,60,65,85))
ideas.append(mk("xr_mega_ufo_iran_gas","UFO Sightings During the Iran War","Did UAP reports change during the 2026 conflict and military mobilization","XREF","us_national","Line chart","Science & Technology","Kaggle UAP + Iran War timeline",45,45,75,75,45,55,80,70))
ideas.append(mk("xr_mega_corruption_billionaires_poverty","Corruption Creates Billionaires and Poverty Simultaneously","WGI corruption index vs billionaire count vs poverty rate triple plot","XREF","worldwide","Scatter plot","Economy","Kaggle WGI + Richest People + World Bank Poverty",70,55,80,70,65,60,75,75))

# ============================================================
# INJECTION LOGIC
# ============================================================
print(f"[BATCH_GK] {len(ideas)} ideas ready")

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
    print("[BATCH_GK] ERROR: tail marker not found in data.js")
    sys.exit(1)

raw = raw.replace(tail, "")
for idea in new_ideas:
    raw += idea + ",\n"
raw += tail + "\n"

with open(DATA_JS, "w", encoding="utf-8") as f:
    f.write(raw)

print(f"[BATCH_GK] Injected {len(new_ideas)} new ideas ({skipped} dupes skipped)")
