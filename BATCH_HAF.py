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
# --- "One Stat" viral maps (Reddit gold) ---
mk("haf001","Average Annual Sunshine Hours by Country","From Yuma AZ at 4000 hrs to Torshavn at 800","MAP","World","World choropleth","Climate","nasa_solar",7,8,7,7,4,8,7,65),
mk("haf002","The Worlds Busiest Airports by Passenger Volume","Atlanta has been #1 for 25 years straight","RANK","World","Bar chart","Transportation","aci_airports",7,7,7,7,5,7,6,65),
mk("haf003","Countries by Number of UNESCO World Heritage Sites","Italy and China are tied at the top","MAP","World","World choropleth","History","unesco_whc",7,7,7,7,4,8,6,70),
mk("haf004","Percentage of Land That Is Forest by Country","Suriname is 98% forest, Qatar is 0%","MAP","World","World choropleth","Geography & Environment","fao_forest",7,7,7,8,4,8,7,70),
mk("haf005","Average Height by Country: The Tallest and Shortest Nations","The Netherlands at 6ft vs Timor-Leste at 5ft 2in","MAP","World","World choropleth","Health","ncd_risc",8,9,6,7,4,8,7,65),
mk("haf006","Coffee Consumption per Capita by Country","Finland drinks 4x more coffee than Italy","MAP","World","World choropleth","Food & Nutrition","ico_coffee",8,9,7,8,4,8,7,70),
mk("haf007","Most Spoken Languages by Number of Countries","English is official in 59 countries, French in 29","MAP","World","World choropleth","Demographics","ethnologue",7,7,6,7,4,8,7,65),
mk("haf008","Countries That Have Never Had a Female Head of State","A surprising majority of the world","MAP","World","World choropleth","History","manual_politics",7,7,7,8,6,8,7,60),
mk("haf009","Alcohol Consumption per Capita: The Worlds Heaviest Drinkers","Eastern Europe dominates, the Middle East barely registers","MAP","World","World choropleth","Health","who_gho",7,8,7,7,5,8,6,70),
mk("haf010","Countries with Compulsory Voting","23 countries require citizens to vote by law","MAP","World","World choropleth","Elections","manual_elections",6,7,7,8,5,8,7,65),
# --- US County-level viral ---
mk("haf011","Most Common Surname by US County","Smith dominates the East, Garcia the West","MAP","US","County choropleth","Demographics","census_surnames",8,9,6,7,4,8,8,60),
mk("haf012","Average Elevation by US County","From Death Valley to the Colorado Rockies","MAP","US","County choropleth","Geography & Environment","usgs_ned",6,6,6,7,4,8,7,65),
mk("haf013","US Counties Where Nobody Lives","There are 15 census tracts with literally zero population","MAP","US","County choropleth","Population","census_2020",7,7,6,8,4,8,8,70),
mk("haf014","Nearest Walmart Distance by US County","The Walmart desert map reveals Americas retail gaps","MAP","US","County choropleth","Economy","walmart_stores",8,9,6,7,5,8,8,60),
mk("haf015","Counties That Flipped from Obama to Trump to Biden","The 200 swing counties that decide every election","MAP","US","County choropleth","Elections","mit_election_lab",8,8,7,7,8,8,7,70),
# --- Animated / time-series ---
mk("haf016","Global GDP Animation: 1960-2025","Watch economic power shift from West to East","MAP","World","Animated choropleth","Economy","D:/raw_data/Kaggle/archive (35)/historysaid-global-economic-dataset/data/core/world_bank.csv",7,7,7,7,6,8,7,85),
mk("haf017","US Religious Adherence: 1980 vs 2000 vs 2020","Three snapshots showing Americas secularization","MAP","US","State choropleth","Demographics","D:/raw_data/Sage_Data/Adherent Rate from the U.S. Religion Census Database.xlsx",7,7,7,7,6,8,7,85),
mk("haf018","Crude Oil Price: Every War Spike Annotated","From Yom Kippur to Iran - 50 years of war premiums","CHART","World","Line chart","History","D:/raw_data/Kaggle/archive (48)/fuel_prices_1970_2026.csv",8,7,8,7,8,8,7,90),
mk("haf019","Bitcoin Halving Cycles Overlaid on Gold Bear Markets","When BTC rallies, gold often dips - and vice versa","XREF","World","Line chart","Economy","D:/raw_data/Kaggle/archive (49)/BTC_prices.csv + D:/raw_data/Kaggle/archive (36)/monthly.csv",6,6,6,8,6,7,8,85),
mk("haf020","AI Research Papers Growth: 2015-2025 by Country","Chinas exponential curve vs Americas linear growth","CHART","World","Line chart","Science & Technology","D:/raw_data/Kaggle/archive (40)/ai_index_main.csv",6,6,7,8,6,7,7,85),
]

ideas2 = [
# --- Niche deep-cut cross-refs ---
mk("haf021","Breakfast Egg Price vs Chicken Population by Country","Countries with more chickens dont always have cheaper eggs","XREF","World","Scatter plot","Food & Nutrition","D:/raw_data/Kaggle/archive (38)/breakfast basket.csv + D:/raw_data/Our World In Data/animals-slaughtered-for-meat.csv",6,7,5,9,4,7,9,70),
mk("haf022","Student Social Support Score vs Depression: The Buffer Effect","High social support cuts depression scores by half","XREF","World","Scatter plot","Health","D:/raw_data/Kaggle/mentalburnout/student_mental_health_burnout.csv",8,9,7,7,5,7,7,80),
mk("haf023","Iran War Gas Spike vs Real Personal Income by State","Low-income states got crushed hardest by gas prices","XREF","US","Bivariate choropleth","Economy","D:/raw_data/Kaggle/archive (39)/iran_war_gas_prices_by_state.csv + D:/raw_data/Sage_Data/Real Personal Income and Regional Price Parities from the Regional Personal Income and Employment Database.csv",8,9,7,8,8,8,8,80),
mk("haf024","Asteroid Detection Rate Over Time: Were Getting Better","We found 3x more near-Earth objects in 2024 than 2014","CHART","World","Line chart","Science & Technology","D:/raw_data/Kaggle/archive (47)/asteroid_dataset_20251019.csv",6,6,7,7,5,7,7,90),
mk("haf025","Steam Game Discount Percentage vs Review Score","The deepest discounts are on the worst-reviewed games","XREF","World","Scatter plot","Entertainment","D:/raw_data/Kaggle/steam/steam_games_2026.csv",7,8,7,7,5,7,7,85),
# --- Final section gap-fillers ---
mk("haf026","Countries by Government Net Surplus/Deficit Trend: 2000-2025","Who went from surplus to deficit and who recovered?","CHART","World","Line chart","International Statistics","D:/raw_data/Kaggle/archive (35)/historysaid-global-economic-dataset/data/core/imf_weo.csv",5,5,7,7,6,7,7,85),
mk("haf027","GDP PPP vs Nominal: The Top 20 Economies Reranked","China is already #1 by PPP but #2 by nominal","RANK","World","Bar chart","Economy","D:/raw_data/Kaggle/archive (35)/historysaid-global-economic-dataset/data/core/world_bank.csv",6,7,7,8,5,7,7,85),
mk("haf028","Political Stability Score: The Most and Least Stable Countries","The index that predicted every recent revolution","MAP","World","World choropleth","International Statistics","D:/raw_data/Kaggle/archive (35)/historysaid-global-economic-dataset/data/core/world_bank_wgi.csv",7,7,7,7,7,8,7,90),
mk("haf029","GNI per Capita vs GDP per Capita: Where Income Leaves","Ireland, Luxembourg, and Singapore show the biggest gaps","MAP","World","Bivariate choropleth","Economy","D:/raw_data/Kaggle/archive (35)/historysaid-global-economic-dataset/data/core/world_bank.csv",5,5,7,8,5,8,8,85),
mk("haf030","Congregations per 1000 People: Americas Religious Density Map","Mississippi has 15 churches per 1000 people","MAP","US","State choropleth","Demographics","D:/raw_data/Sage_Data/Number of Congregations from the U.S. Religion Census Database.xlsx",7,7,7,7,5,7,7,90),
mk("haf031","NAICS Employment by State: The Specialization Map","Every state has a dominant industry - whats yours?","MAP","US","State choropleth","Labor","D:/raw_data/Sage_Data/State and Local  Personal Income and Employment by NAICS Industry (1998 - Current) from the Regional Personal Income and Employment Database.csv",7,7,7,7,5,7,7,85),
mk("haf032","Arrest Rate Trend by State: 2000-2022","Most states show declining arrests but a few bucked the trend","MAP","US","State choropleth","Crime and Law Enforcement","D:/raw_data/Sage_Data/Arrests by Race from the Arrests Database.csv",7,6,7,7,6,7,7,80),
mk("haf033","Inmate Population by Race Over Time: National Trend","The slow decline in incarceration and its racial dimensions","CHART","US","Line chart","Crime and Law Enforcement","D:/raw_data/Sage_Data/Inmates by Race from the Annual Survey of Jails (United States) Database.csv",8,7,7,7,8,7,7,85),
mk("haf034","Global Trends: Which Countries Generate the Most Viral Content?","The US and India dominate but Turkey punches above its weight","MAP","World","World choropleth","Science & Technology","D:/raw_data/Kaggle/archive (37)/enhanced_global_trends_dataset.csv",6,6,6,7,5,7,7,85),
mk("haf035","Population Growth vs GDP Growth: The Decoupling Chart","Rich countries grow economies without growing population","XREF","World","Scatter plot","Economy","D:/raw_data/Kaggle/pop/popolazione-globale-per-paese-1950-2024.csv + D:/raw_data/Kaggle/archive (35)/historysaid-global-economic-dataset/data/core/world_bank.csv",6,6,7,8,6,7,8,85),
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

print(f"BATCH_HAF: {len(all_ideas)} ideas generated")
print(f"[BATCH_HAF] Injected {len(new)} new ideas (skipped {dupes} dupes)")
