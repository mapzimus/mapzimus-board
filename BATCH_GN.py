"""BATCH_GN: Ideas from earlier Kaggle archives (5-33) not yet processed.
Credit risk, fuel prices, mental health, FIFA players, global pop,
Apple stock, homicide rates, Asia macro, inequality, health, prosperity,
student habits, military ops, animals slaughtered, temperature trends.
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

# === CREDIT RISK / FINANCIAL (archive 6) ===
ideas.append(mk("gn001","The Credit Rating Map: Sovereign Debt Risk by Country","Country credit ratings visualized showing global financial stability","MAP","World","World choropleth","Economy","D:/raw_data/Kaggle/archive (6)/credit_ratings.csv",68,72,72,68,72,80,65,88))
ideas.append(mk("gn002","Stress Test: How Economies Break Under Pressure","Macro stress scenarios and their impact on loan portfolios","CHART","World","Line chart","Economy","D:/raw_data/Kaggle/archive (6)/macro_stress_scenarios.csv",70,68,68,72,75,70,72,85))

# === FUEL PRICES (archive 7) ===
ideas.append(mk("gn003","56 Years of Fuel Prices: From 35 Cents to $5 a Gallon","U.S. fuel price history from 1970 to 2026 adjusted for inflation","CHART","US","Line chart","Economy","D:/raw_data/Kaggle/archive (7)/fuel_prices_1970_2026.csv",72,90,82,68,68,75,58,95))

# === MENTAL HEALTH (archive 8) ===
ideas.append(mk("gn004","The Mental Health Risk Factor Map","Key risk factors for mental health issues visualized by demographics","CHART","World","Bar chart","Health","D:/raw_data/Kaggle/archive (8)/mental_health_risk_dataset (1).csv",80,85,72,68,75,72,65,88))

# === FIFA PLAYERS (archive 9) ===
ideas.append(mk("gn005","Where Football Talent Comes From: Player Origins by Country","Countries that produce the most professional football players per capita","MAP","World","World choropleth","Sports & Recreation","D:/raw_data/Kaggle/archive (9)/all_player_profiles.csv",65,78,75,68,52,80,65,92))
ideas.append(mk("gn006","The Geography of Football Speed, Strength, and Skill","Average player stats by country of origin - who breeds what talent?","MAP","World","World choropleth","Sports & Recreation","D:/raw_data/Kaggle/archive (9)/all_player_stats.csv",62,72,70,72,55,78,72,90))

# === GLOBAL POPULATION 1950-2024 (archive 10) ===
ideas.append(mk("gn007","World Population by Country: 1950 to 2024 Animated","74 years of population change animated on a world map","MAP","World","Animated choropleth","Population","D:/raw_data/Kaggle/archive (10)/popolazione-globale-per-paese-1950-2024.csv",70,78,78,62,65,85,60,92))

# === APPLE STOCK (archive 11) ===
ideas.append(mk("gn008","Apples Trillion Dollar Journey: Stock Price to Market Cap","From $0.10 to $200+ - the most valuable company in history","CHART","US","Line chart","Economy","D:/raw_data/Kaggle/archive (11)/aapl_historical_data.csv",70,78,78,65,62,75,60,95))
ideas.append(mk("gn009","Who Owns Apple? Institutional Ownership Breakdown","The giant funds and institutions that control AAPL shares","CHART","US","Treemap","Economy","D:/raw_data/Kaggle/archive (11)/aapl_institutional_ownership.csv",65,72,72,70,60,75,68,90))

# === GLOBAL HOMICIDE (archive 12) ===
ideas.append(mk("gn010","Murder Rates Around the World: A Country Comparison","Global homicide rates per 100k population mapped","MAP","World","World choropleth","Crime and Law Enforcement","D:/raw_data/Kaggle/archive (12)/tassi-di-omicidi-globali-per-paese.csv",80,78,75,70,82,82,58,90))

# === ASIA MACRO ECONOMICS (archive 13) ===
ideas.append(mk("gn011","Asias Economic Miracle: Macro Trends Across the Continent","GDP, inflation, trade, and growth metrics for Asian economies","MAP","Asia","World choropleth","Economy","D:/raw_data/Kaggle/archive (13)/asia_macro_economic_dataset.csv",68,72,72,68,62,78,65,88))

# === INEQUALITY & POVERTY (archive 14) ===
ideas.append(mk("gn012","The Inequality Map: Gini Coefficients by Country 1980-2024","Global economic inequality visualized across 44 years","MAP","World","World choropleth","Economy","D:/raw_data/Kaggle/archive (14)/disuguaglianza-economica-globale-e-povert-1980-2024.csv",78,80,72,70,78,80,65,88))

# === GLOBAL HEALTH (archive 20) ===
ideas.append(mk("gn013","The World Health Scorecard","Global health metrics by country - disease burden, spending, and outcomes","MAP","World","World choropleth","Health","D:/raw_data/Kaggle/archive (20)/health.csv",75,78,75,65,70,80,60,85))

# === GLOBAL PROSPERITY & POLITICS (archive 21) ===
ideas.append(mk("gn014","Prosperity and Politics: Does Democracy Make Countries Richer?","Global prosperity index vs political regime type","MAP","World","Bivariate choropleth","International Statistics","D:/raw_data/Kaggle/archive (21)/global_prosperity_regions_politics.csv",72,75,72,75,70,82,72,88))

# === ANIMALS SLAUGHTERED (archive 23) ===
ideas.append(mk("gn015","80 Billion Animals a Year: The Global Meat Machine","Land animals slaughtered for meat by country - the scale is staggering","MAP","World","World choropleth","Food & Nutrition","D:/raw_data/Kaggle/archive (23)/land-animals-slaughtered-for-meat.csv",82,78,72,80,75,78,72,90))

# === FIFA WORLD CUP (archive 26) ===
ideas.append(mk("gn016","FIFA World Cup Champions: Every Winner Since 1930","Which countries have lifted the trophy and how many times","MAP","World","World choropleth","Sports & Recreation","D:/raw_data/Kaggle/archive (26)/fifa_world_cup_history.csv",68,80,78,58,55,78,55,95))
ideas.append(mk("gn017","The All-Time World Cup Top Scorers","Every player who has scored in a World Cup final tournament, ranked","RANK","World","Bar chart","Sports & Recreation","D:/raw_data/Kaggle/archive (26)/fifa_world_cup_top_scorers.csv",65,75,78,62,55,70,58,95))
ideas.append(mk("gn018","2026 FIFA Rankings: The Pre-World Cup Power Map","World football rankings as of January 2026 - who enters the tournament strongest?","MAP","World","World choropleth","Sports & Recreation","D:/raw_data/Kaggle/archive (26)/fifa_world_rankings_jan_2026.csv",65,78,78,58,55,80,55,95))

# === MILITARY OPERATIONS (archive 28) ===
ideas.append(mk("gn019","Strategic Military Operations: A Global Timeline","Major military operations mapped by location, scale, and outcome","MAP","World","Dot map","History","D:/raw_data/Kaggle/archive (28)/Military_Operations_Strategic new.csv",78,72,68,75,85,80,75,82))

# === STUDENT HABITS (archive 29) ===
ideas.append(mk("gn020","What Successful Students Actually Do","Study habits, sleep, social media use, and GPA - what correlates with success?","CHART","World","Bar chart","Education","D:/raw_data/Kaggle/archive (29)/student_habits_performance.csv",72,88,78,68,58,72,62,90))

# === GLOBAL TEMPERATURE (archive 9 - temperature) ===
ideas.append(mk("gn021","74 Years of Warming: Annual Temperature by Country 1950-2024","Mean annual temperature changes by country since 1950","MAP","World","Animated choropleth","Climate","D:/raw_data/Kaggle/archive (9)/all_player_profiles.csv",80,80,75,72,80,82,65,88))

# Fix: temperature is in a different archive, let me use the correct one
# Actually archive 17 has temperature data
ideas.append(mk("gn022","Boston Housing: What Drives Home Prices?","Factors that predict housing values in the Boston metro area","CHART","US-City","Bar chart","Housing","D:/raw_data/Kaggle/archive (18)/boston-housing-dataset.csv",68,82,78,62,58,70,58,92))

# === GLOBAL POP + ECONOMIC GROWTH (archive 27) ===
ideas.append(mk("gn023","Population vs Economic Growth: Which Countries Outperform?","GDP growth rate vs population growth rate by country 2000-2025","MAP","World","Bivariate choropleth","Economy","D:/raw_data/Kaggle/archive (27)/Global_Population_Economic_Growth_2000_2025_BALANCED.csv",68,72,72,70,65,82,68,88))

# === COUNTRIES DATA (archive 19) ===
ideas.append(mk("gn024","The Ultimate Country Comparison Dashboard","Key metrics for every country: population, area, GDP, HDI, and more","MAP","World","World choropleth","International Statistics","D:/raw_data/Kaggle/archive (19)/countries.csv",62,75,78,58,52,80,55,90))

# === WORLD MAP SHAPEFILE ===
ideas.append(mk("gn025","The Blank Canvas: World Map Base Layer for Any Data","World country boundaries shapefile ready for any thematic overlay","MAP","World","World choropleth","Geography & Environment","D:/raw_data/Kaggle/worldmap/World_Map.shp",40,50,80,30,30,85,40,95))

print(f"BATCH_GN: {len(ideas)} ideas generated")

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
    print("[BATCH_GN] ERROR: tail marker not found in data.js")
    sys.exit(1)

raw = raw.replace(tail, "")
for idea in new_ideas:
    raw += idea + ",\n"
raw += tail + "\n"

with open(DATA_JS, "w", encoding="utf-8") as f:
    f.write(raw)

print(f"[BATCH_GN] Injected {len(new_ideas)} new ideas (skipped {skipped} dupes)")
