import os, sys
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
# --- TSMC / Semiconductor (archive 34) ---
mk("gz001","TSMC Stock Price vs Global Chip Shortage Timeline","How semiconductor scarcity moved markets 1997-2025","CHART","World","Line chart","Economy","D:/raw_data/Kaggle/archive (34)/tsm_stock_prices.csv",6,7,7,7,7,7,7,90),
mk("gz002","TSMC Revenue Growth vs Intel and Samsung","The semiconductor king nobody talks about","CHART","World","Bar chart","Economy","D:/raw_data/Kaggle/archive (34)/tsm_income_statement.csv",5,6,8,7,6,7,7,85),
mk("gz003","TSMC Dividend History: Most Consistent Payout in Tech?","26 years of semiconductor dividends","CHART","World","Area chart","Economy","D:/raw_data/Kaggle/archive (34)/tsm_dividends.csv",5,6,7,6,5,6,7,90),
# --- Global Trends (archive 37) ---
mk("gz004","What the World Googled in 2026: Topic Heatmap by Country","Climate, conflict, and culture dominate differently everywhere","MAP","World","World choropleth","Science & Technology","D:/raw_data/Kaggle/archive (37)/enhanced_global_trends_dataset.csv",7,8,7,7,6,8,8,85),
mk("gz005","Viral Score vs Sentiment: Do Negative Headlines Win?","Engagement patterns across 15 topic categories","CHART","World","Scatter plot","Entertainment","D:/raw_data/Kaggle/archive (37)/enhanced_global_trends_dataset.csv",7,8,7,8,7,7,8,85),
# --- Breakfast Basket Prices (archive 38) ---
mk("gz006","The Price of Breakfast Around the World","What a basic morning meal costs in 50+ cities","MAP","World","World choropleth","Food & Nutrition","D:/raw_data/Kaggle/archive (38)/breakfast basket.csv",8,9,8,7,5,8,7,90),
mk("gz007","Milk vs Eggs vs Bread: Which Breakfast Item Varies Most?","Price volatility of staples across continents","CHART","World","Bar chart","Food & Nutrition","D:/raw_data/Kaggle/archive (38)/breakfast basket.csv",7,8,8,7,5,7,7,90),
mk("gz008","The $1 Breakfast Map: Where Can You Still Eat Cheap?","Cities where a full breakfast costs under a dollar","MAP","World","Dot map","Food & Nutrition","D:/raw_data/Kaggle/archive (38)/breakfast basket.csv",8,9,7,8,5,8,8,90),
# --- AI Index (archive 40) ---
mk("gz009","AI Adoption by Country: Consumer vs Enterprise Gap","Some countries adopt AI personally but not at work","MAP","World","Bivariate choropleth","Science & Technology","D:/raw_data/Kaggle/archive (40)/ai_index_main.csv",7,7,7,8,6,8,8,85),
mk("gz010","Countries Where AI Investment Dwarfs R&D Spending","When AI gets more money than all other research combined","MAP","World","World choropleth","Science & Technology","D:/raw_data/Kaggle/archive (40)/ai_index_main.csv",6,7,7,8,7,7,8,85),
mk("gz011","AI Startups per Capita: Small Countries Punching Above Their Weight","Israel, Estonia, and Singapore lead the ratio","RANK","World","Bar chart","Science & Technology","D:/raw_data/Kaggle/archive (40)/ai_index_main.csv",6,6,8,8,5,7,8,85),
# --- AI Job Market 2026 (archive 42) ---
mk("gz012","AI Job Salaries by Country: Where Does AI Pay Best?","The global salary map for machine learning engineers","MAP","World","World choropleth","Labor","D:/raw_data/Kaggle/archive (42)/AI_Job_Market_Trends_2026.csv",7,8,7,7,6,7,7,80),
mk("gz013","Remote vs Hybrid vs Office: AI Jobs by Work Type","Which AI roles are most likely to be fully remote?","CHART","World","Bar chart","Labor","D:/raw_data/Kaggle/archive (42)/AI_Job_Market_Trends_2026.csv",7,8,7,6,5,6,7,80),
mk("gz014","Skills That Pay: Python vs SQL vs Deep Learning Premium","How each skill combination affects AI salaries","CHART","World","Scatter plot","Labor","D:/raw_data/Kaggle/archive (42)/AI_Job_Market_Trends_2026.csv",7,8,7,7,5,7,7,80),
]
ideas2 = [
# --- Richest People (archive 44) ---
mk("gz015","Where Billionaires Live: A City-Level Dot Map","The ultra-wealthy cluster in surprisingly few places","MAP","World","Dot map","Economy","D:/raw_data/Kaggle/archive (44)/richest_people_dataset.csv",7,7,7,8,6,8,7,85),
mk("gz016","Self-Made vs Inherited: The Billionaire Map","Which countries produce more self-made billionaires?","MAP","World","Bivariate choropleth","Economy","D:/raw_data/Kaggle/archive (44)/richest_people_dataset.csv",7,8,7,8,7,8,8,85),
mk("gz017","Average Billionaire Age by Industry","Finance billionaires are oldest, tech youngest","CHART","World","Bar chart","Economy","D:/raw_data/Kaggle/archive (44)/richest_people_dataset.csv",6,7,7,7,5,6,7,85),
# --- Asteroids (archive 47) ---
mk("gz018","Every Asteroid Close Approach Since 2020","Panic level vs actual risk: how scared should we be?","CHART","World","Scatter plot","Science & Technology","D:/raw_data/Kaggle/archive (47)/asteroid_dataset_20251019.csv",8,7,6,9,8,8,9,90),
mk("gz019","Asteroid Threat Categories: Monitor vs Watch vs Act","How NASA classifies near-Earth objects by panic level","CHART","World","Bar chart","Science & Technology","D:/raw_data/Kaggle/archive (47)/asteroid_dataset_20251019.csv",7,7,7,8,8,7,8,90),
# --- UAP/UFO Reports (archive 50) ---
mk("gz020","Every UFO Sighting in America: 80 Years of Reports","80,000+ civilian UAP reports mapped by location","MAP","US","Dot map","Science & Technology","D:/raw_data/Kaggle/archive (50)/uap_reports.csv",9,8,6,9,7,9,9,90),
mk("gz021","UFO Shapes Reported by State: Lights, Triangles, or Discs?","The most common UAP shapes vary surprisingly by region","MAP","US","State choropleth","Science & Technology","D:/raw_data/Kaggle/archive (50)/uap_reports.csv",8,8,6,9,7,8,9,90),
mk("gz022","UFO Sightings Over Time: Did They Spike After Each Movie?","Close Encounters, Independence Day, and sighting surges","CHART","US","Line chart","Entertainment","D:/raw_data/Kaggle/archive (50)/uap_reports.csv",8,8,7,9,6,7,9,85),
# --- Spotify (spotify folder) ---
mk("gz023","Where the Worlds Most-Streamed Artists Come From","Country of origin for Spotifys all-time top 100 songs","MAP","World","World choropleth","Entertainment","D:/raw_data/Kaggle/spotify/spotify_alltime_top100_songs.csv",8,9,7,7,5,7,7,90),
mk("gz024","BPM vs Streams: Do Faster Songs Get More Plays?","Tempo analysis of the top 100 most-streamed songs ever","CHART","World","Scatter plot","Entertainment","D:/raw_data/Kaggle/spotify/spotify_alltime_top100_songs.csv",7,8,7,7,5,7,7,90),
mk("gz025","Danceability vs Energy: The Spotify Hit Formula","What audio features predict billion-stream songs?","CHART","World","Scatter plot","Entertainment","D:/raw_data/Kaggle/spotify/spotify_alltime_top100_songs.csv",7,8,7,7,5,7,8,90),
# --- Steam Games 2026 ---
mk("gz026","Most Reviewed Games on Steam: The Popularity Chart","Which games generated the most community engagement?","RANK","World","Bar chart","Entertainment","D:/raw_data/Kaggle/steam/steam_games_2026.csv",7,8,7,6,5,6,7,85),
mk("gz027","Steam Deck Compatibility: What Percentage of Games Work?","Verified vs Playable vs Unsupported breakdown","CHART","World","Bar chart","Entertainment","D:/raw_data/Kaggle/steam/steam_games_2026.csv",6,8,7,6,5,6,7,85),
mk("gz028","Free-to-Play vs Paid: Which Games Get Better Reviews?","Review scores by price point on Steam","CHART","World","Scatter plot","Entertainment","D:/raw_data/Kaggle/steam/steam_games_2026.csv",7,8,7,7,5,7,7,85),
]
ideas3 = [
# --- Iran War / Oil Prices ---
mk("gz029","Gas Prices by State During the Iran War","Which states got hit hardest at the pump","MAP","US","State choropleth","Economy","D:/raw_data/Kaggle/archive (39)/iran_war_gas_prices_by_state.csv",8,9,8,7,9,8,7,90),
mk("gz030","Oil Price Timeline: Every Spike Since 1970","From OPEC embargo to Iran war - 55 years of crude","CHART","World","Line chart","Economy","D:/raw_data/Kaggle/archive (48)/fuel_prices_1970_2026.csv",7,8,8,7,8,8,7,90),
mk("gz031","Iran War Key Events vs Oil Price Movement","How each escalation moved the price of crude","CHART","World","Line chart","History","D:/raw_data/Kaggle/irankeyevents/iran_war_key_events_timeline.csv",8,7,7,8,9,8,8,90),
# --- Student Mental Health ---
mk("gz032","Student Burnout: Screen Time vs Anxiety Score","More screen hours correlate with higher anxiety across courses","CHART","World","Scatter plot","Health","D:/raw_data/Kaggle/mentalburnout/student_mental_health_burnout.csv",8,9,7,7,7,7,7,80),
mk("gz033","Sleep Hours vs Academic Pressure: The Student Tradeoff","Students sleeping under 5 hours report 3x the pressure","CHART","World","Scatter plot","Health","D:/raw_data/Kaggle/mentalburnout/student_mental_health_burnout.csv",8,9,7,7,7,7,7,80),
# --- Religion Census (Sage) ---
mk("gz034","Americas Religious Map: Adherent Rate by State","Which faiths dominate each state in 2020?","MAP","US","State choropleth","Demographics","D:/raw_data/Sage_Data/Adherent Rate from the U.S. Religion Census Database.xlsx",8,8,7,7,6,8,7,90),
mk("gz035","Number of Congregations per Capita by State","Where houses of worship are most concentrated","MAP","US","State choropleth","Demographics","D:/raw_data/Sage_Data/Number of Congregations from the U.S. Religion Census Database.xlsx",7,7,7,7,5,7,7,90),
# --- CPI / PPI ---
mk("gz036","US Inflation Since 1913: The Full CPI Timeline","110 years of consumer prices in one chart","CHART","US","Line chart","Economy","D:/raw_data/cpi/historical-cpi-u-202602.xlsx",7,8,8,6,7,7,6,95),
mk("gz037","Producer vs Consumer Price Index: Who Feels Inflation First?","PPI leads CPI by months - the early warning system","CHART","US","Line chart","Economy","D:/raw_data/cpi/ppi-fdallrel.xlsx",6,7,8,7,6,7,7,85),
# --- Sage Economic Data ---
mk("gz038","Real Personal Income by State: Cost-of-Living Adjusted Map","Your salary means different things in different states","MAP","US","State choropleth","Economy","D:/raw_data/Sage_Data/Real Personal Income and Regional Price Parities from the Regional Personal Income and Employment Database.csv",8,9,8,7,6,8,7,85),
mk("gz039","Vehicles Registered per Capita by State","The most car-dependent states in America","MAP","US","State choropleth","Transportation","D:/raw_data/Sage_Data/Total Vehicles Registered from the All Motor Vehicles  (Private + Public; Registered Vehicles) Database (1).csv",7,8,7,7,5,7,7,85),
mk("gz040","Marijuana Use by State: Monthly Usage Rates","Where cannabis consumption is highest vs lowest","MAP","US","State choropleth","Health","D:/raw_data/Sage_Data/Marijuana Use in the Past Month from the National Survey on Drug Use and Health (NSDUH), 2015-2019 [Archive] Database.csv",8,8,7,7,6,8,7,85),
]

# --- INJECTION ---
DATA = r"D:\projects\mapzimus-board\data.js"
with open(DATA, "r", encoding="utf-8") as f:
    blob = f.read()

tail = "]; // end D"
if tail not in blob:
    print("ERROR: tail marker not found"); sys.exit(1)

existing_ids = set()
import re
for m in re.finditer(r'id:"([^"]+)"', blob):
    existing_ids.add(m.group(1))

all_ideas = ideas + ideas2 + ideas3
new = [i for i in all_ideas if i.split('id:"')[1].split('"')[0] not in existing_ids]
dupes = len(all_ideas) - len(new)

blob = blob.replace(tail, ",\n".join(new) + ",\n" + tail)
with open(DATA, "w", encoding="utf-8") as f:
    f.write(blob)

print(f"BATCH_GZ: {len(all_ideas)} ideas generated")
print(f"[BATCH_GZ] Injected {len(new)} new ideas (skipped {dupes} dupes)")
