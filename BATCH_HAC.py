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
# --- Niche Viral: Food Economics ---
mk("hac001","The Cheapest City for Coffee in the World","From $0.30 in Cairo to $6.50 in Zurich","RANK","World","Bar chart","Food & Nutrition","D:/raw_data/Kaggle/archive (38)/breakfast basket.csv",8,9,7,7,5,6,7,90),
mk("hac002","Bread Price Around the World: A Loaf-by-Loaf Comparison","The staple that tells you everything about an economy","MAP","World","World choropleth","Food & Nutrition","D:/raw_data/Kaggle/archive (38)/breakfast basket.csv",7,9,7,7,5,8,7,90),
mk("hac003","Breakfast Basket Price Change: October 2025 to Now","Which cities saw breakfast costs spike the most?","MAP","World","World choropleth","Food & Nutrition","D:/raw_data/Kaggle/archive (38)/breakfast basket.csv",7,8,7,7,6,7,7,85),
# --- Niche Viral: Space/Astronomy ---
mk("hac004","The Largest Asteroids to Pass Within 0.05 AU","Ranked by absolute magnitude - the scariest near-misses","RANK","World","Bar chart","Science & Technology","D:/raw_data/Kaggle/archive (47)/asteroid_dataset_20251019.csv",8,7,6,9,8,7,8,90),
mk("hac005","Asteroid Risk Score Distribution: How Worried Should We Be?","99% are harmless, but that 1% keeps NASA up at night","CHART","World","Bar chart","Science & Technology","D:/raw_data/Kaggle/archive (47)/asteroid_dataset_20251019.csv",7,7,6,8,7,7,8,90),
# --- Deep History ---
mk("hac006","Americas Sex Ratio by State Over 200 Years","From male-dominated frontiers to female-majority cities","MAP","US","Animated choropleth","Demographics","D:/raw_data/HSUS/A-Population/aaPopulation-Characteristics/Sex, Age, Race, and Marital Status",7,7,7,8,5,8,8,80),
mk("hac007","Marriage Rate in America: 1900-2020","The dramatic decline of the institution of marriage","CHART","US","Line chart","Demographics","D:/raw_data/HSUS/A-Population/abVital-Statistics",7,8,8,7,7,7,7,80),
mk("hac008","International Migration to the US by Decade","Which decades brought the biggest waves of immigrants?","CHART","US","Bar chart","Demographics","D:/raw_data/HSUS/A-Population/adInternational-Migration",7,7,7,7,6,7,7,80),
mk("hac009","Average Household Size in America: 1790-2020","From 5.8 to 2.5 people per home in 230 years","CHART","US","Line chart","Demographics","D:/raw_data/HSUS/A-Population/aeFamily and Household Composition",7,8,8,7,5,7,7,80),
# --- AI Deep Dives ---
mk("hac010","AI Research Papers by Country: Who Publishes Most?","China overtook the US in 2018 and hasnt looked back","MAP","World","World choropleth","Science & Technology","D:/raw_data/Kaggle/archive (40)/ai_index_main.csv",7,6,7,8,7,8,7,85),
mk("hac011","Cloud Infrastructure Score vs AI Adoption","You need the cloud before you can adopt AI","XREF","World","Scatter plot","Science & Technology","D:/raw_data/Kaggle/archive (40)/ai_index_main.csv",5,5,7,7,5,6,7,85),
mk("hac012","AI Policy Score by Country: Who Regulates AI Best?","The EU leads regulation, the US leads adoption","MAP","World","World choropleth","Science & Technology","D:/raw_data/Kaggle/archive (40)/ai_index_main.csv",6,6,7,7,6,7,7,85),
# --- Financial Markets ---
mk("hac013","Every 20%+ Market Crash Since 1970 Overlaid","Recovery times ranged from 4 months to 6 years","CHART","World","Line chart","Economy","historical_sp500",7,8,7,7,8,7,7,70),
mk("hac014","TSMC Technical Indicators: RSI vs Price Action","When the RSI screamed buy and when it screamed sell","CHART","World","Line chart","Economy","D:/raw_data/Kaggle/archive (34)/tsm_technical_indicators.csv",5,5,7,7,5,6,7,90),
mk("hac015","McDonalds Stock vs CPI: The Fast Food Inflation Hedge","MCD beats inflation in 22 of the last 25 years","XREF","US","Line chart","Economy","D:/raw_data/Kaggle/archive (43)/MCD.csv + D:/raw_data/cpi/historical-cpi-u-202602.xlsx",7,8,7,8,5,7,8,85),
# --- Transportation Deep ---
mk("hac016","Vehicles per Capita vs Public Transit Ridership by State","The states that drive vs the states that ride","XREF","US","Bivariate choropleth","Transportation","D:/raw_data/Sage_Data/Total Vehicles Registered from the All Motor Vehicles  (Private + Public; Registered Vehicles) Database (1).csv + D:/raw_data/MBTA Data 2025",7,7,7,7,6,8,7,75),
# --- Crime Deep Dives ---
mk("hac017","Arrest Rates by Race Over Time: The Disparity Chart","How racial gaps in arrests have changed since 2000","CHART","US","Line chart","Crime and Law Enforcement","D:/raw_data/Sage_Data/Arrests by Race from the Arrests Database.csv",8,7,7,7,9,7,7,80),
mk("hac018","Jail Inmates by Race: 10-Year Trend","Which racial groups are increasingly overrepresented?","CHART","US","Line chart","Crime and Law Enforcement","D:/raw_data/Sage_Data/Inmates by Race from the Annual Survey of Jails (United States) Database.csv",8,7,7,7,9,7,7,85),
# --- Employment by Industry ---
mk("hac019","Which States Depend Most on Government Employment?","Federal, state, and local jobs as % of total employment","MAP","US","State choropleth","Labor","D:/raw_data/Sage_Data/State and Local  Personal Income and Employment by NAICS Industry (1998 - Current) from the Regional Personal Income and Employment Database.csv",6,7,7,7,5,7,7,85),
mk("hac020","Manufacturing Employment Share by State Since 1998","The Rust Belt decline visualized year by year","MAP","US","Animated choropleth","Labor","D:/raw_data/Sage_Data/State and Local  Personal Income and Employment by NAICS Industry (1998 - Current) from the Regional Personal Income and Employment Database.csv",7,7,7,7,7,8,7,85),
]

ideas2 = [
# --- More Cross-refs with new datasets ---
mk("hac021","Bitcoin Price vs Gold Price: The Digital Gold Debate","Do they actually move together or is it a myth?","XREF","World","Line chart","Economy","D:/raw_data/Kaggle/archive (49)/BTC_prices.csv + D:/raw_data/Kaggle/archive (36)/monthly.csv",7,7,7,8,6,7,8,85),
mk("hac022","NVIDIA Stock vs AI Investment by Country Over Time","Did national AI spending predict NVIDIAs rise?","XREF","World","Line chart","Economy","D:/raw_data/Kaggle/archive (45)/nvda_stock_data_master.csv + D:/raw_data/Kaggle/archive (40)/ai_index_main.csv",6,5,6,8,6,7,8,75),
mk("hac023","Student Anxiety Score vs Course Type","Engineering students report highest stress, arts lowest","CHART","World","Bar chart","Education","D:/raw_data/Kaggle/mentalburnout/student_mental_health_burnout.csv",7,8,7,7,5,6,7,80),
mk("hac024","UFO Sighting Duration by Decade: Getting Shorter?","Modern sightings average 30 seconds, 1960s averaged 5 minutes","CHART","US","Line chart","Science & Technology","D:/raw_data/Kaggle/archive (50)/uap_reports.csv",7,7,6,8,5,6,8,85),
mk("hac025","Steam Game Prices vs Review Scores: Is Expensive Better?","The $60 game sweet spot vs the $5 gem phenomenon","XREF","World","Scatter plot","Entertainment","D:/raw_data/Kaggle/steam/steam_games_2026.csv",7,8,7,7,5,7,7,85),
# --- Global Development Paradoxes ---
mk("hac026","Countries Where GDP Grew But Life Got Worse","GDP up, political stability down - the paradox nations","XREF","World","Scatter plot","International Statistics","D:/raw_data/Kaggle/archive (35)/historysaid-global-economic-dataset/data/core/world_bank.csv + world_bank_wgi.csv",7,7,7,9,7,7,9,75),
mk("hac027","GNI per Capita vs Government Effectiveness","Do richer countries govern better or do better-governed countries get rich?","XREF","World","Scatter plot","International Statistics","D:/raw_data/Kaggle/archive (35)/historysaid-global-economic-dataset/data/core/world_bank.csv + world_bank_wgi.csv",6,6,7,8,6,7,8,80),
mk("hac028","PPP GDP vs Nominal GDP: Where the Gap Is Largest","Countries where purchasing power far exceeds their dollar GDP","MAP","World","Bivariate choropleth","Economy","D:/raw_data/Kaggle/archive (35)/historysaid-global-economic-dataset/data/core/world_bank.csv",6,6,7,8,5,8,8,85),
# --- More Section Fillers ---
mk("hac029","PPI Commodity Weights: What Drives Producer Prices?","Energy and food dominate the producer price basket","CHART","US","Treemap","Economy","D:/raw_data/cpi/ppi-comrlp.xlsx",5,5,7,6,5,7,7,90),
mk("hac030","Global Trends Sentiment by Language","Which languages skew most negative in news coverage?","CHART","World","Bar chart","International Statistics","D:/raw_data/Kaggle/archive (37)/enhanced_global_trends_dataset.csv",6,6,6,8,6,6,8,85),
mk("hac031","Engagement Score by Topic Category: What the World Cares About","Climate and conflict generate 3x more engagement than tech","CHART","World","Bar chart","Science & Technology","D:/raw_data/Kaggle/archive (37)/enhanced_global_trends_dataset.csv",6,7,7,7,5,6,7,85),
mk("hac032","The Most Streamed Genre on Spotify: Its Not What You Think","Pop dominates but Latin music is closing the gap fast","CHART","World","Bar chart","Entertainment","D:/raw_data/Kaggle/spotify/spotify_alltime_top100_songs.csv",7,8,7,7,5,6,7,90),
mk("hac033","Real Personal Income Growth by State: 2000-2024","Which states actually got richer after adjusting for cost of living?","MAP","US","State choropleth","Economy","D:/raw_data/Sage_Data/Real Personal Income and Regional Price Parities from the Regional Personal Income and Employment Database.csv",7,8,8,7,6,8,7,85),
mk("hac034","NAICS Industry Employment Shift: Healthcare vs Manufacturing","Healthcare overtook manufacturing as #1 employer in 2018","CHART","US","Area chart","Labor","D:/raw_data/Sage_Data/State and Local  Personal Income and Employment by NAICS Industry (1998 - Current) from the Regional Personal Income and Employment Database.csv",7,7,7,7,6,7,7,85),
mk("hac035","Population Base Change by State: 1980-2020 Religion Census","Which states grew fastest and how it reshaped American religion","MAP","US","State choropleth","Demographics","D:/raw_data/Sage_Data/Population Base from the U.S. Religion Census Database.xlsx",6,6,7,7,5,7,7,85),
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

print(f"BATCH_HAC: {len(all_ideas)} ideas generated")
print(f"[BATCH_HAC] Injected {len(new)} new ideas (skipped {dupes} dupes)")
