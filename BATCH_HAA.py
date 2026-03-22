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
# --- XREF: AI x Economy ---
mk("haa001","AI Adoption vs GDP per Capita: Does Wealth Drive AI?","Rich countries adopt faster but the gap is closing","XREF","World","Scatter plot","Science & Technology","D:/raw_data/Kaggle/archive (40)/ai_index_main.csv + D:/raw_data/Kaggle/archive (35)/historysaid-global-economic-dataset/data/core/world_bank.csv",7,7,7,8,6,7,8,80),
mk("haa002","AI Job Salaries vs Cost of Living by Country","Where AI pay actually goes furthest after expenses","XREF","World","Scatter plot","Labor","D:/raw_data/Kaggle/archive (42)/AI_Job_Market_Trends_2026.csv + D:/raw_data/Kaggle/archive (38)/breakfast basket.csv",7,8,7,8,6,7,8,75),
mk("haa003","AI Startups per Capita vs Government Effectiveness","Do well-run governments produce more AI companies?","XREF","World","Scatter plot","Science & Technology","D:/raw_data/Kaggle/archive (40)/ai_index_main.csv + D:/raw_data/Kaggle/archive (35)/historysaid-global-economic-dataset/data/core/world_bank_wgi.csv",6,6,7,8,6,7,9,75),
# --- XREF: Breakfast Prices x Economics ---
mk("haa004","Breakfast Cost vs GDP per Capita: The Egg McMuffin Index","A better purchasing power comparison than Big Macs?","XREF","World","Scatter plot","Food & Nutrition","D:/raw_data/Kaggle/archive (38)/breakfast basket.csv + D:/raw_data/Kaggle/archive (35)/historysaid-global-economic-dataset/data/core/world_bank.csv",8,9,7,8,5,7,9,80),
mk("haa005","Milk Price vs Government Corruption Score","Corrupt countries pay more for basic dairy","XREF","World","Scatter plot","Food & Nutrition","D:/raw_data/Kaggle/archive (38)/breakfast basket.csv + D:/raw_data/Kaggle/archive (35)/historysaid-global-economic-dataset/data/core/world_bank_wgi.csv",7,8,6,9,6,7,9,75),
# --- XREF: Religion x Demographics ---
mk("haa006","Religious Adherence vs Median Age by State","Younger states are less religious - how strong is the trend?","XREF","US","Scatter plot","Demographics","D:/raw_data/Sage_Data/Adherent Rate from the U.S. Religion Census Database.xlsx + D:/raw_data/fivethirtyeight/bad-drivers/bad-drivers.csv",7,7,7,8,7,7,8,80),
mk("haa007","Congregations per Capita vs Poverty Rate by State","More churches in poorer states or richer ones?","XREF","US","Bivariate choropleth","Demographics","D:/raw_data/Sage_Data/Number of Congregations from the U.S. Religion Census Database.xlsx + census",7,7,7,8,7,8,8,70),
# --- XREF: UFO x Demographics ---
mk("haa008","UFO Sightings per Capita vs Light Pollution by State","Do people see more UFOs where skies are darker?","XREF","US","Bivariate choropleth","Science & Technology","D:/raw_data/Kaggle/archive (50)/uap_reports.csv + D:/raw_data/Our World In Data/outdoor-air-pollution.csv",8,7,6,9,6,8,9,70),
mk("haa009","UFO Sightings vs Military Base Proximity","Are UAPs clustered near military installations?","XREF","US","Dot map","Science & Technology","D:/raw_data/Kaggle/archive (50)/uap_reports.csv + military_bases",8,7,6,9,8,8,9,65),
mk("haa010","UFO Report Duration vs Shape: Which Shapes Linger Longest?","Triangles are reported for minutes, lights for seconds","XREF","World","Bar chart","Science & Technology","D:/raw_data/Kaggle/archive (50)/uap_reports.csv",7,7,6,8,6,7,8,90),
# --- XREF: Spotify x Country Data ---
mk("haa011","Spotify Hit BPM by Artist Country of Origin","Latin artists trend slower, Nordic artists trend faster","XREF","World","World choropleth","Entertainment","D:/raw_data/Kaggle/spotify/spotify_alltime_top100_songs.csv",7,8,6,7,5,7,8,90),
mk("haa012","Explicit Lyrics vs Streams: Does Swearing Sell?","Comparing clean vs explicit tracks in the top 100","XREF","World","Bar chart","Entertainment","D:/raw_data/Kaggle/spotify/spotify_alltime_top100_songs.csv",7,8,7,7,5,6,7,90),
# --- XREF: Gas Prices x Elections/Politics ---
mk("haa013","Gas Price Spike by State vs 2024 Presidential Vote","Red states hit harder or blue states? The Iran War pump map","XREF","US","Bivariate choropleth","Elections","D:/raw_data/Kaggle/archive (39)/iran_war_gas_prices_by_state.csv + D:/raw_data/fivethirtyeight/election-deniers/fivethirtyeight_election_deniers.csv",8,9,7,8,9,8,9,85),
mk("haa014","Gas Prices vs Vehicle Registrations by State","States with the most cars feel pain at the pump most","XREF","US","Bivariate choropleth","Transportation","D:/raw_data/Kaggle/archive (39)/iran_war_gas_prices_by_state.csv + D:/raw_data/Sage_Data/Total Vehicles Registered from the All Motor Vehicles  (Private + Public; Registered Vehicles) Database (1).csv",7,8,7,7,7,8,8,80),
# --- XREF: Student Mental Health x Economics ---
mk("haa015","Financial Stress vs Depression Score in College Students","Money worries are the strongest predictor of student depression","XREF","World","Scatter plot","Health","D:/raw_data/Kaggle/mentalburnout/student_mental_health_burnout.csv",8,9,7,7,7,7,7,80),
mk("haa016","Physical Activity Hours vs Anxiety: The Exercise Effect","Students who exercise 2+ hours daily score 40% lower on anxiety","XREF","World","Scatter plot","Health","D:/raw_data/Kaggle/mentalburnout/student_mental_health_burnout.csv",8,9,7,7,6,7,7,80),
# --- XREF: Oil Price x Global Governance ---
mk("haa017","Oil Price Spikes vs Political Stability Index","Every major price shock aligned with governance collapse","XREF","World","Line chart","Economy","D:/raw_data/Kaggle/archive (48)/fuel_prices_1970_2026.csv + D:/raw_data/Kaggle/archive (35)/historysaid-global-economic-dataset/data/core/world_bank_wgi.csv",7,7,7,8,8,7,8,75),
# --- XREF: Steam x AI ---
mk("haa018","AI-Tagged Games on Steam: Fastest Growing Genre?","Games with AI tags doubled between 2023 and 2026","XREF","World","Line chart","Entertainment","D:/raw_data/Kaggle/steam/steam_games_2026.csv",7,7,7,8,6,7,8,85),
# --- XREF: Asteroid x Media ---
mk("haa019","Asteroid Close Approaches vs Google Search Trends","Each near-miss generates a panic spike online","XREF","World","Line chart","Science & Technology","D:/raw_data/Kaggle/archive (47)/asteroid_dataset_20251019.csv + google_trends",7,7,6,9,7,7,9,70),
# --- XREF: Billionaire x Governance ---
mk("haa020","Billionaires per Capita vs Rule of Law Score","Countries with stronger rule of law create more wealth","XREF","World","Scatter plot","Economy","D:/raw_data/Kaggle/archive (44)/richest_people_dataset.csv + D:/raw_data/Kaggle/archive (35)/historysaid-global-economic-dataset/data/core/world_bank_wgi.csv",6,6,7,8,6,7,8,75),
]

ideas2 = [
# --- XREF: CPI x Wages ---
mk("haa021","Inflation vs Wage Growth: When Workers Fall Behind","Decades where CPI outpaced earnings","XREF","US","Area chart","Economy","D:/raw_data/cpi/historical-cpi-u-202602.xlsx + bls_wages",7,8,8,7,8,7,7,75),
# --- XREF: Real Income x Education ---
mk("haa022","Real Personal Income vs NAEP Test Scores by State","Do richer states produce smarter students?","XREF","US","Scatter plot","Education","D:/raw_data/Sage_Data/Real Personal Income and Regional Price Parities from the Regional Personal Income and Employment Database.csv + D:/raw_data/Sage_Data/Assessment by All Students from the National Assessment of Educational Progress (NAEP) Database.csv",7,7,7,8,6,7,8,80),
# --- XREF: Marijuana x Crime ---
mk("haa023","Marijuana Use Rate vs Arrest Rate by State","Do high-use states arrest more or less?","XREF","US","Bivariate choropleth","Crime and Law Enforcement","D:/raw_data/Sage_Data/Marijuana Use in the Past Month from the National Survey on Drug Use and Health (NSDUH), 2015-2019 [Archive] Database.csv + D:/raw_data/Sage_Data/Arrests by Race from the Arrests Database.csv",8,7,7,8,8,8,8,80),
# --- XREF: Vehicles x Walkability ---
mk("haa024","Cars per Capita vs Walkability Score: Americas Transit Divide","States with the most cars have the least walkable neighborhoods","XREF","US","Bivariate choropleth","Transportation","D:/raw_data/Sage_Data/Total Vehicles Registered from the All Motor Vehicles  (Private + Public; Registered Vehicles) Database (1).csv + D:/raw_data/WalkabilityIndex",7,8,7,7,6,8,8,75),
# --- XREF: Breakfast x Governance ---
mk("haa025","Cost of Eggs vs Voice and Accountability Score","Democratic countries have cheaper eggs - coincidence?","XREF","World","Scatter plot","International Statistics","D:/raw_data/Kaggle/archive (38)/breakfast basket.csv + D:/raw_data/Kaggle/archive (35)/historysaid-global-economic-dataset/data/core/world_bank_wgi.csv",7,7,6,9,6,7,9,75),
# --- XREF: TSMC x Global Chip Demand ---
mk("haa026","TSMC Stock vs Global GDP Growth Rate","The semiconductor bellwether for the world economy","XREF","World","Line chart","Economy","D:/raw_data/Kaggle/archive (34)/tsm_stock_prices.csv + D:/raw_data/Kaggle/archive (35)/historysaid-global-economic-dataset/data/core/imf_weo.csv",6,6,7,7,6,7,8,80),
# --- XREF: Iran War x TSMC ---
mk("haa027","Iran War Oil Spike vs TSMC Stock Crash","Geopolitics crushed tech and energy simultaneously","XREF","World","Line chart","Economy","D:/raw_data/Kaggle/irankeyevents/iran_war_key_events_timeline.csv + D:/raw_data/Kaggle/archive (34)/tsm_stock_prices.csv",7,6,7,8,9,7,8,80),
# --- XREF: Religion x Drug Use ---
mk("haa028","Religious Adherence vs Marijuana Use by State","The Bible Belt smokes less - or does it?","XREF","US","Bivariate choropleth","Demographics","D:/raw_data/Sage_Data/Adherent Rate from the U.S. Religion Census Database.xlsx + D:/raw_data/Sage_Data/Marijuana Use in the Past Month from the National Survey on Drug Use and Health (NSDUH), 2015-2019 [Archive] Database.csv",8,8,7,8,7,8,8,80),
# --- XREF: Billionaire x AI ---
mk("haa029","Tech Billionaire Wealth vs AI Investment by Country","Where billionaire money and national AI spending align","XREF","World","Scatter plot","Economy","D:/raw_data/Kaggle/archive (44)/richest_people_dataset.csv + D:/raw_data/Kaggle/archive (40)/ai_index_main.csv",6,6,7,8,6,7,8,75),
# --- XREF: Student Burnout x Screen Time x Sleep ---
mk("haa030","The Triple Threat: Screen Time + Low Sleep + High Pressure","Students hitting all three risk factors score worst on depression","XREF","World","Scatter plot","Health","D:/raw_data/Kaggle/mentalburnout/student_mental_health_burnout.csv",8,9,7,7,7,7,8,80),
# --- Multi-dataset mega xrefs ---
mk("haa031","Government Debt vs Corruption vs GDP Growth","The triangle of national economic health","XREF","World","Scatter plot","International Statistics","D:/raw_data/Kaggle/archive (35)/historysaid-global-economic-dataset/data/core/imf_weo.csv + world_bank_wgi.csv + world_bank.csv",6,6,7,8,7,7,8,80),
mk("haa032","AI Adoption vs Internet Penetration vs Education Index","The three pillars of national AI readiness","XREF","World","Scatter plot","Science & Technology","D:/raw_data/Kaggle/archive (40)/ai_index_main.csv",6,6,7,7,5,7,8,85),
mk("haa033","Oil Price vs Gas by State vs Vehicle Registrations","The full chain from crude to consumer pain","XREF","US","State choropleth","Economy","D:/raw_data/Kaggle/archive (48)/fuel_prices_1970_2026.csv + D:/raw_data/Kaggle/archive (39)/iran_war_gas_prices_by_state.csv + D:/raw_data/Sage_Data/Total Vehicles Registered from the All Motor Vehicles  (Private + Public; Registered Vehicles) Database (1).csv",7,8,7,7,8,8,8,80),
mk("haa034","UFO Sightings + Military Spending + Population Density","The three variables that best predict UAP hotspots","XREF","US","Dot map","Science & Technology","D:/raw_data/Kaggle/archive (50)/uap_reports.csv + census + military",8,7,6,9,7,8,9,65),
mk("haa035","Spotify Streams + GDP per Capita + Internet Penetration","Rich connected countries dominate global music consumption","XREF","World","Scatter plot","Entertainment","D:/raw_data/Kaggle/spotify/spotify_alltime_top100_songs.csv + world_bank.csv + ai_index_main.csv",6,7,6,7,5,7,8,70),
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

print(f"BATCH_HAA: {len(all_ideas)} ideas generated")
print(f"[BATCH_HAA] Injected {len(new)} new ideas (skipped {dupes} dupes)")
