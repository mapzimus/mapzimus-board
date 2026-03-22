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
# --- Reddit Viral Bait ---
mk("hab001","Every McDonalds Stock Split Since 2000","MCD has quietly been one of the best long-term holds","CHART","US","Line chart","Economy","D:/raw_data/Kaggle/archive (43)/MCD.csv",6,7,7,7,5,6,7,90),
mk("hab002","Bitcoin Price: Every Halving Cycle Overlaid","The pattern that crypto bros swear by - does it hold?","CHART","World","Line chart","Economy","D:/raw_data/Kaggle/archive (49)/BTC_prices.csv",7,7,7,8,7,7,8,85),
mk("hab003","NVIDIA Stock: From Gaming Company to AI Giant","The most dramatic sector pivot in stock market history","CHART","World","Line chart","Economy","D:/raw_data/Kaggle/archive (45)/nvda_stock_data_master.csv",7,7,7,8,6,7,7,90),
mk("hab004","NVIDIA Earnings Surprises: How Often They Beat Estimates","Wall Street has consistently underestimated NVIDIA since 2020","CHART","World","Bar chart","Economy","D:/raw_data/Kaggle/archive (45)/nvda_earnings_history_alphaquery.csv",6,6,7,8,6,6,7,85),
mk("hab005","Gold Price Since 1833: Almost 200 Years of Data","The longest commodity price chart you will ever see","CHART","World","Line chart","Economy","D:/raw_data/Kaggle/archive (36)/monthly.csv",7,7,8,7,6,7,7,95),
# --- History/Geography Viral ---
mk("hab006","US Slave Population by State: 1790-1860","The geographic concentration of American slavery over 70 years","MAP","US","Animated choropleth","History","D:/raw_data/HSUS/A-Population/aaPopulation-Characteristics/Slave Population",8,7,7,7,8,8,8,80),
mk("hab007","Americas Rural vs Urban Population Shift: 1790-2020","How the country emptied and the cities filled","CHART","US","Area chart","Demographics","D:/raw_data/HSUS/A-Population/aaPopulation-Characteristics/Rural and Urban Places",8,8,8,7,6,8,7,80),
mk("hab008","Hispanic Population Growth by State Since 1850","The demographic transformation in animated form","MAP","US","Animated choropleth","Demographics","D:/raw_data/HSUS/A-Population/aaPopulation-Characteristics/Hispanic Population",8,7,7,7,6,8,7,80),
mk("hab009","Foreign-Born Population Share by State: Historical","When was America most and least immigrant?","MAP","US","State choropleth","Demographics","D:/raw_data/HSUS/A-Population/aaPopulation-Characteristics/Nativity",7,7,7,8,7,7,8,80),
mk("hab010","US State Population Rankings Over Time","Which states rose and fell in the population hierarchy","RANK","US","Line chart","Population","D:/raw_data/HSUS/A-Population/aaPopulation-Characteristics/State Populations",7,7,7,7,5,7,7,80),
# --- Iran War Deep Dives ---
mk("hab011","Every Day of the Iran War: Event Timeline with Oil Overlay","What happened each day and how markets reacted","CHART","World","Line chart","History","D:/raw_data/Kaggle/irankeyevents/iran_war_key_events_timeline.csv",8,7,7,8,9,8,8,90),
mk("hab012","Iran War Gas Prices: Regional Disparities","West Coast hit $5.50 while Gulf states stayed under $3.50","MAP","US","State choropleth","Economy","D:/raw_data/Kaggle/archive (39)/iran_war_gas_prices_by_state.csv",8,9,8,7,9,8,7,90),
mk("hab013","Oil Price Shock Comparison: 1973 vs 2022 vs 2026","Three oil crises, three different Americas","CHART","World","Line chart","History","D:/raw_data/Kaggle/archive (48)/fuel_prices_1970_2026.csv",7,7,8,8,8,7,8,90),
# --- Pew Abortion Data ---
mk("hab014","Abortion Views by State: The Pew 2026 Survey","Where Americans stand after Dobbs - state by state","MAP","US","State choropleth","Elections","D:/raw_data/Pew/2603/PP_2026.3.12_abortion_report.pdf",9,8,7,7,9,8,7,75),
# --- More Entertainment/Culture ---
mk("hab015","The Release Year Distribution of Spotifys Top 100 Songs","When were todays biggest songs actually released?","CHART","World","Bar chart","Entertainment","D:/raw_data/Kaggle/spotify/spotify_alltime_top100_songs.csv",7,8,7,7,5,6,7,90),
mk("hab016","Steam Games by Genre: Which Genres Dominate in 2026?","FPS and RPG still reign but survival games are surging","CHART","World","Bar chart","Entertainment","D:/raw_data/Kaggle/steam/steam_games_2026.csv",6,8,7,6,5,6,7,85),
mk("hab017","24-Hour Peak Players vs Review Score on Steam","Do popular games actually get good reviews?","CHART","World","Scatter plot","Entertainment","D:/raw_data/Kaggle/steam/steam_games_2026.csv",7,8,7,7,5,7,7,85),
# --- World Governance Deep Dives ---
mk("hab018","The Most Corrupt Countries: Control of Corruption Score","Transparency Internationals index mapped beautifully","MAP","World","World choropleth","International Statistics","D:/raw_data/Kaggle/archive (35)/historysaid-global-economic-dataset/data/core/world_bank_wgi.csv",7,7,7,7,7,8,6,90),
mk("hab019","Regulatory Quality Around the World","Where business regulation helps vs where it hurts","MAP","World","World choropleth","International Statistics","D:/raw_data/Kaggle/archive (35)/historysaid-global-economic-dataset/data/core/world_bank_wgi.csv",5,6,7,6,5,7,6,90),
mk("hab020","Voice and Accountability: The Global Freedom Map","Which populations have the most say in their government?","MAP","World","World choropleth","International Statistics","D:/raw_data/Kaggle/archive (35)/historysaid-global-economic-dataset/data/core/world_bank_wgi.csv",7,7,7,6,7,8,6,90),
]

ideas2 = [
# --- IMF WEO Deep Dives ---
mk("hab021","Government Debt as % of GDP: The World Map","Japan at 260%, US at 123% - who owes the most?","MAP","World","World choropleth","International Statistics","D:/raw_data/Kaggle/archive (35)/historysaid-global-economic-dataset/data/core/imf_weo.csv",7,7,8,7,7,8,6,90),
mk("hab022","Government Revenue vs Spending by Country","Which nations run the biggest deficits relative to GDP?","MAP","World","Bivariate choropleth","International Statistics","D:/raw_data/Kaggle/archive (35)/historysaid-global-economic-dataset/data/core/imf_weo.csv",6,6,7,7,7,8,7,90),
mk("hab023","GDP Growth Rate Animated: 2000-2025","Watch economic booms and busts ripple across the globe","MAP","World","Animated choropleth","Economy","D:/raw_data/Kaggle/archive (35)/historysaid-global-economic-dataset/data/core/world_bank.csv",7,7,7,7,6,8,7,85),
# --- World Bank Indicators ---
mk("hab024","Agriculture as % of GDP: The Worlds Farm Economies","Which countries still depend on farming for their GDP?","MAP","World","World choropleth","Economy","D:/raw_data/Kaggle/archive (35)/historysaid-global-economic-dataset/data/core/world_bank.csv",6,6,7,7,5,8,6,85),
mk("hab025","Industry vs Services: Every Countrys Economic Structure","The three-sector model visualized for 200 countries","MAP","World","World choropleth","Economy","D:/raw_data/Kaggle/archive (35)/historysaid-global-economic-dataset/data/core/world_bank.csv",6,6,7,7,5,8,7,85),
mk("hab026","GDP per Capita vs GNI per Capita: Where They Diverge","Countries where wealth leaves (or enters) through borders","MAP","World","Bivariate choropleth","Economy","D:/raw_data/Kaggle/archive (35)/historysaid-global-economic-dataset/data/core/world_bank.csv",5,5,7,8,6,8,8,85),
# --- Section Fillers: Housing ---
mk("hab027","Median Home Price vs Median Income by State: 2024","How many years of income does a house cost in your state?","MAP","US","State choropleth","Housing","census + zillow",8,9,8,7,7,8,7,65),
mk("hab028","Rent Burden by County: Who Spends 30%+ on Housing","The counties where housing costs eat your paycheck","MAP","US","County choropleth","Housing","census_acs",8,9,7,7,7,8,7,65),
# --- Section Fillers: Geography ---
mk("hab029","Furthest Point from the Ocean in Every Country","The continental poles of inaccessibility mapped","MAP","World","Dot map","Geography & Environment","manual_geo",7,7,6,9,4,8,9,60),
mk("hab030","US Counties Larger Than Countries","San Bernardino County is bigger than 9 nations","MAP","World","Special map","Geography & Environment","census_tiger",8,8,7,9,4,8,9,70),
# --- Section Fillers: Science ---
mk("hab031","Near-Earth Asteroid Approaches by Month: Is There a Pattern?","Seasonal clustering in asteroid detection","CHART","World","Bar chart","Science & Technology","D:/raw_data/Kaggle/archive (47)/asteroid_dataset_20251019.csv",6,6,7,8,6,7,8,90),
mk("hab032","Asteroid Velocity vs Distance: The Speed-Proximity Plot","Faster asteroids tend to pass further away - why?","CHART","World","Scatter plot","Science & Technology","D:/raw_data/Kaggle/archive (47)/asteroid_dataset_20251019.csv",5,5,6,8,6,7,8,90),
# --- Section Fillers: Sports ---
mk("hab033","Countries That Have Never Won an Olympic Gold Medal","The nations still chasing their first gold","MAP","World","World choropleth","Sports & Recreation","olympics_data",7,7,7,8,5,8,7,70),
mk("hab034","FIFA World Cup: Goals per Game by Decade","Is modern football actually more entertaining?","CHART","World","Bar chart","Sports & Recreation","D:/raw_data/worldcup",6,7,7,7,5,6,7,85),
# --- Section Fillers: Education ---
mk("hab035","NAEP Test Scores by State: Reading vs Math","Which states excel at reading but struggle at math?","MAP","US","Bivariate choropleth","Education","D:/raw_data/Sage_Data/Assessment by All Students from the National Assessment of Educational Progress (NAEP) Database.csv",7,7,8,7,6,8,7,80),
# --- Section Fillers: Climate ---
mk("hab036","Global Temperature Anomaly: Every Year Since 1880","The hockey stick chart that defines our era","CHART","World","Line chart","Climate","nasa_giss",8,7,8,7,8,8,6,70),
mk("hab037","Sea Level Rise Projections: Best vs Worst Case by 2100","The 0.3m vs 2.0m future mapped on coastal cities","MAP","World","Special map","Climate","ipcc_slr",8,7,7,8,8,8,8,60),
# --- Section Fillers: Population ---
mk("hab038","Countries Where Population Is Shrinking Right Now","The demographic crisis nobody is ready for","MAP","World","World choropleth","Population","D:/raw_data/Kaggle/archive (35)/historysaid-global-economic-dataset/data/core/world_bank.csv",7,7,7,8,8,8,7,80),
mk("hab039","Median Age by Country: The Youth vs Aging Map","Niger at 15, Japan at 49 - the age divide","MAP","World","World choropleth","Population","un_population",7,7,7,8,6,8,7,70),
mk("hab040","US Internal Migration: Which States Are Gaining People?","The great American sort continues","MAP","US","State choropleth","Population","D:/raw_data/HSUS/A-Population/acInternal-Migration + census",8,8,7,7,6,8,7,70),
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

print(f"BATCH_HAB: {len(all_ideas)} ideas generated")
print(f"[BATCH_HAB] Injected {len(new)} new ideas (skipped {dupes} dupes)")
