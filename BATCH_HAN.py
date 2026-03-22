import os, sys, re
sys.path.insert(0, r"D:\projects\mapzimus-board")

def mk(id,title,sub,typ,geo,fmt,sect,tbl,e,r,c,s,t,v,o,dr):
    raw=e*2+r*2+c*1.25+s*1.5+t*1.5+v*2.0+o*1.5
    vs=int((raw/11.75)*(1-0.5*(1-dr/100)))
    return ('{id:"'+id+'",title:"'+title+'",sub:"'+sub+'",type:"'+typ+'",'
            'geo:"'+geo+'",fmt:"'+fmt+'",section:"'+sect+'",tbl:"'+tbl+'",'
            'sc:{emotional:'+str(e)+',relatability:'+str(r)+',clarity:'+str(c)
            +',surprise:'+str(s)+',tension:'+str(t)+',visual:'+str(v)
            +',originality:'+str(o)+',data_ready:'+str(dr)+'}'
            ',vs:'+str(vs)+',topics:[],ext:[],status:"idea",notes:""}')

ideas = [
# --- "Mapped by Decade" time travel series ---
mk("han001","Americas Largest City by Decade: 1800-2020","New York wasnt always #1 - Philadelphia held the crown until 1810","MAP","US","Animated choropleth","History","census_historical",7,7,7,8,5,8,8,70),
mk("han002","Most Popular Baby Name by State: 1960 vs 1990 vs 2024","Jennifer dominated the 70s, Liam dominates now","MAP","US","State choropleth","Demographics","ssa_baby_names",7,8,6,7,4,8,7,70),
mk("han003","Average Home Price by State: 2000 vs 2012 vs 2024","The bubble, the crash, and the new bubble","MAP","US","State choropleth","Housing","zillow",8,9,7,7,7,8,7,55),
mk("han004","Top Export Product by Country: 2000 vs 2024","Oil countries are diversifying, tech is taking over","MAP","World","World choropleth","Economy","un_comtrade",6,6,7,7,5,8,7,60),
mk("han005","Internet Penetration by Country: 2005 vs 2015 vs 2025","From 15% to 65% global average in 20 years","MAP","World","World choropleth","Science & Technology","itu_ict",6,6,7,7,5,8,6,60),
# --- "Double Take" maps (things that seem wrong but are true) ---
mk("han006","More People Live in This Circle Than Outside It","60% of humanity lives in a circle centered on Southeast Asia","MAP","World","Special map","Population","D:/raw_data/Kaggle/pop/popolazione-globale-per-paese-1950-2024.csv",7,7,6,9,4,8,9,85),
mk("han007","The True Size of Africa: Every Other Continent Fits Inside","US + China + Europe + India + Japan all fit in Africa","MAP","World","Special map","Geography & Environment","manual_geo",7,7,6,9,4,8,9,60),
mk("han008","Countries Closer to Space Than to Their Nearest Neighbor","Some islands are more isolated than the space station","MAP","World","Dot map","Geography & Environment","manual_geo",6,7,5,9,3,8,9,50),
mk("han009","The Pacific Ocean Is Bigger Than All Land on Earth Combined","You can fit every continent in the Pacific with room to spare","MAP","World","Special map","Geography & Environment","manual_geo",7,7,6,9,4,8,9,55),
mk("han010","Half the World Lives North of This Line","The 25th parallel north splits global population 50/50","MAP","World","Special map","Population","D:/raw_data/Kaggle/pop/popolazione-globale-per-paese-1950-2024.csv",6,6,5,9,4,8,9,75),
# --- "The Gap" inequality maps ---
mk("han011","Richest vs Poorest County in Every State","In New York, the gap is $128k to $35k median income","MAP","US","State choropleth","Economy","census_acs",8,8,7,8,7,8,8,60),
mk("han012","Life Expectancy Gap Between Richest and Poorest Counties","The 20-year gap within the same country","MAP","US","County choropleth","Health","ihme_gbd",9,8,7,8,8,8,8,60),
mk("han013","Gender Pay Gap by Country: Women Earn X Cents per Dollar","From 0.98 in Iceland to 0.55 in South Korea","MAP","World","World choropleth","Labor","ilo_wages",8,8,7,7,7,8,7,60),
mk("han014","Racial Wealth Gap by State: White vs Black Median Net Worth","The gap ranges from 5x to 20x depending on the state","MAP","US","Bivariate choropleth","Economy","fed_scf",8,7,7,8,8,8,8,55),
mk("han015","Urban vs Rural Life Expectancy Gap by State","Rural Americans live 5 fewer years on average","MAP","US","Bivariate choropleth","Health","cdc_nchs",8,8,7,7,7,8,7,60),
# --- Fresh viral standalone ideas ---
mk("han016","Countries You Can Drive Across in Under 1 Hour","Luxembourg, Singapore, and 10 others you didnt expect","MAP","World","World choropleth","Geography & Environment","manual_geo",7,8,5,8,3,8,8,55),
mk("han017","The Antipode Map: Whats on the Exact Opposite Side of Earth?","Spoiler: for most of the US, its the Indian Ocean","MAP","World","Special map","Geography & Environment","manual_geo",7,8,5,9,3,8,9,55),
mk("han018","How Many Countries Can You See From the Top of Each Mountain?","Mont Blanc: 3 countries. Everest: 2. Denali: just Alaska.","MAP","World","Dot map","Geography & Environment","manual_geo",6,7,5,8,3,8,9,45),
mk("han019","The Most Visited City in Every Country","Paris dominates France but Marrakech isnt Moroccos #1","MAP","World","World choropleth","Economy","unwto_tourism",7,8,6,7,4,8,7,55),
mk("han020","Countries That Changed Their System of Government Since 2000","17 countries shifted between democracy, autocracy, or hybrid","MAP","World","World choropleth","International Statistics","v_dem_data",7,7,6,8,7,8,8,55),
]

ideas2 = [
# --- Final exhaust of all local data cross-ref combos ---
mk("han021","TSMC Revenue Growth vs NVIDIA Revenue Growth","The chip maker and the chip designer rose together","XREF","World","Line chart","Economy","D:/raw_data/Kaggle/archive (34)/tsm_income_statement.csv + D:/raw_data/Kaggle/archive (45)/nvda_stock_data_master.csv",5,5,7,7,5,7,7,85),
mk("han022","Gold Price vs CPI: 200 Years of the Inflation Hedge Debate","Gold tracks inflation over centuries but not over decades","XREF","World","Line chart","Economy","D:/raw_data/Kaggle/archive (36)/monthly.csv + D:/raw_data/cpi/historical-cpi-u-202602.xlsx",6,6,7,8,5,7,8,85),
mk("han023","Student Burnout by Gender: Who Suffers More?","Female students score 15% higher on burnout across all metrics","CHART","World","Bar chart","Health","D:/raw_data/Kaggle/mentalburnout/student_mental_health_burnout.csv",7,8,7,7,5,6,7,80),
mk("han024","UFO Sighting Day of Week: Fridays and Saturdays Dominate","Weekend nights produce 3x more reports than weekdays","CHART","US","Bar chart","Science & Technology","D:/raw_data/Kaggle/archive (50)/uap_reports.csv",6,7,6,8,4,6,8,85),
mk("han025","Steam Game Tags Word Cloud: The Most Popular Tags","FPS, Multiplayer, and Indie are the holy trinity of Steam","CHART","World","Treemap","Entertainment","D:/raw_data/Kaggle/steam/steam_games_2026.csv",5,6,6,6,3,7,7,85),
mk("han026","Iran War Event Categories: How the Conflict Evolved","From airstrikes to ground ops to ceasefire negotiations","CHART","World","Bar chart","History","D:/raw_data/Kaggle/irankeyevents/iran_war_key_events_timeline.csv",7,6,7,7,8,6,7,90),
mk("han027","TSMC vs Intel Market Cap Over Time","When TSMC overtook Intel as the worlds most valuable chipmaker","CHART","World","Line chart","Economy","D:/raw_data/Kaggle/archive (34)/tsm_stock_prices.csv + intel_stock",5,5,7,7,5,7,7,80),
mk("han028","Breakfast Price Seasonality: Do Eggs Cost More in Winter?","Monthly price patterns across hemispheres","CHART","World","Line chart","Food & Nutrition","D:/raw_data/Kaggle/archive (38)/breakfast basket.csv",6,7,6,7,4,6,7,85),
mk("han029","McDonalds vs NVIDIA vs Bitcoin: The $10k Investment Race","If you invested $10k in each in 2015, who won?","CHART","World","Line chart","Economy","D:/raw_data/Kaggle/archive (43)/MCD.csv + D:/raw_data/Kaggle/archive (45)/nvda_stock_data_master.csv + D:/raw_data/Kaggle/archive (49)/BTC_prices.csv",7,8,7,8,5,7,8,80),
mk("han030","Global Population Weighted Breakfast Cost","The average human spends $1.80 on breakfast","CHART","World","Bar chart","Food & Nutrition","D:/raw_data/Kaggle/archive (38)/breakfast basket.csv + D:/raw_data/Kaggle/pop/popolazione-globale-per-paese-1950-2024.csv",6,7,6,7,4,6,7,80),
# --- Absolute final format fillers ---
mk("han031","Every Heatmap Calendar Youll Ever Need: US Shooting Deaths by Day","365 cells, each colored by daily death count","MAP","US","Heatmap calendar","Crime and Law Enforcement","gun_violence_archive",8,7,6,7,8,8,7,55),
mk("han032","Heatmap Calendar: Daily COVID Deaths in the US","The waves are visible as seasonal color bands","MAP","US","Heatmap calendar","Health","jhu_covid",7,7,7,7,7,8,7,60),
mk("han033","Polygon Map: Congressional Districts by Partisan Lean","Every district colored from deep blue to deep red","MAP","US","Polygon map","Elections","cook_pvi",7,7,7,6,7,8,6,60),
mk("han034","Treemap: World GDP by Country and Region","Nested rectangles showing economic share visually","CHART","World","Treemap","Economy","D:/raw_data/Kaggle/archive (35)/historysaid-global-economic-dataset/data/core/world_bank.csv",6,6,7,6,5,8,6,85),
mk("han035","Animated Bar Chart Race: GDP by Country 1960-2025","The most shared format on YouTube data channels","CHART","World","Animated bar chart","Economy","D:/raw_data/Kaggle/archive (35)/historysaid-global-economic-dataset/data/core/world_bank.csv",7,7,7,7,6,8,7,85),
]

# --- INJECTION ---
DATA = r"D:\projects\mapzimus-board\data.js"
with open(DATA, "r", encoding="utf-8") as f:
    blob = f.read()

tail = "]; // end D"
if tail not in blob:
    print("ERROR: tail marker not found"); sys.exit(1)

existing_ids = set()
for m in re.finditer(r'id:"([^"]+)"', blob):
    existing_ids.add(m.group(1))

all_ideas = ideas + ideas2
new = [i for i in all_ideas if i.split('id:"')[1].split('"')[0] not in existing_ids]
dupes = len(all_ideas) - len(new)

blob = blob.replace(tail, ",\n".join(new) + ",\n" + tail)
with open(DATA, "w", encoding="utf-8") as f:
    f.write(blob)

print(f"BATCH_HAN: {len(all_ideas)} ideas generated")
print(f"[BATCH_HAN] Injected {len(new)} new ideas (skipped {dupes} dupes)")
