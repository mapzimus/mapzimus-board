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
# --- "What $100 Buys You" series ---
mk("hal001","What $100 Buys at the Grocery Store by Country","120 eggs in India, 15 eggs in Switzerland","MAP","World","World choropleth","Food & Nutrition","D:/raw_data/Kaggle/archive (38)/breakfast basket.csv",8,9,7,8,5,8,8,80),
mk("hal002","What $100 of Gas Gets You: Miles by State","1,000 miles in Mississippi, 600 in California at Iran War prices","MAP","US","State choropleth","Transportation","D:/raw_data/Kaggle/archive (39)/iran_war_gas_prices_by_state.csv",8,9,7,7,7,7,8,90),
mk("hal003","What $100 Worth of Bitcoin Bought You Each Year Since 2010","$100 in 2010 would be worth $75 million today","CHART","World","Bar chart","Economy","D:/raw_data/Kaggle/archive (49)/BTC_prices.csv",8,8,7,9,6,7,8,85),
# --- "Maps That Will Start an Argument" ---
mk("hal004","The Best State to Live In: A Composite Ranking","Combining income, safety, health, education, and weather","RANK","US","State choropleth","Demographics","composite",8,9,7,7,5,8,8,55),
mk("hal005","The Most Boring State: A Data-Driven Assessment","Flatness + weather variety + entertainment options","RANK","US","Bar chart","Entertainment","composite",8,9,6,7,4,6,9,45),
mk("hal006","Americas Most Dangerous Intersections","The 50 intersections with the most traffic fatalities","MAP","US","Dot map","Transportation","nhtsa_fars",7,8,6,7,6,8,7,60),
mk("hal007","The Worst US Airport by Delay Rate","Newark wins (or loses) with 28% of flights delayed","RANK","US","Bar chart","Transportation","bts_ontime",7,8,7,7,5,6,7,65),
mk("hal008","Americas Most Complained-About Companies","Which companies get the most consumer complaints per customer?","RANK","US","Bar chart","Economy","cfpb_complaints",7,8,7,7,5,6,7,60),
# --- "Map Challenge" viral format ---
mk("hal009","Can You Name Every Country in Africa?","The quiz that goes viral every 6 months","MAP","World","World choropleth","Geography & Environment","manual_geo",7,8,5,7,4,8,7,60),
mk("hal010","Can You Name Every European Country Under 5 Minutes?","Kosovo, Montenegro, and North Macedonia trip everyone up","MAP","World","World choropleth","Geography & Environment","manual_geo",7,8,5,7,4,8,7,60),
# --- Environment deep dives ---
mk("hal011","Countries by Clean Energy Investment: 2024","China invested $800B, the US invested $300B","MAP","World","World choropleth","Environment","bnef_data",6,6,7,7,6,8,7,60),
mk("hal012","Carbon Emissions per Dollar of GDP by Country","Who pollutes most per unit of economic output?","MAP","World","World choropleth","Climate","D:/raw_data/Our World In Data/co-emissions-per-capita.csv + D:/raw_data/Kaggle/archive (35)/historysaid-global-economic-dataset/data/core/world_bank.csv",6,6,7,7,6,8,7,75),
mk("hal013","Endangered Species by Country: The Red List Map","Madagascar has 600+ endangered species, more than most continents","MAP","World","World choropleth","Environment","iucn_redlist",7,6,6,7,6,8,7,60),
mk("hal014","Air Quality Index by City: The Worlds Most Polluted Places","Delhi, Lahore, and Dhaka consistently top the worst list","MAP","World","Dot map","Health","iqair_aqi",7,7,7,7,6,8,7,65),
mk("hal015","Glacier Retreat: Before and After Satellite Photos","How much ice has disappeared in 30 years","MAP","World","Special map","Climate","nasa_earth_obs",8,7,6,8,8,9,8,55),
# --- "Things You Didnt Know Had Data" ---
mk("hal016","Global Happiness Score by Country: UN World Happiness Report","Finland is #1 for the 7th year. Afghanistan is last.","MAP","World","World choropleth","International Statistics","unsdsn_whr",7,8,7,7,5,8,6,70),
mk("hal017","Sleep Duration by Country: Who Sleeps the Most?","Netherlands averages 8.5 hours, Japan averages 6.5","MAP","World","World choropleth","Health","fitbit_global",7,8,6,7,4,8,7,55),
mk("hal018","Left-Handedness Rate by Country","Netherlands has 13% lefties, Japan has 4%","MAP","World","World choropleth","Science & Technology","research_study",6,7,5,8,3,8,8,50),
mk("hal019","Average Number of Friends by Country","Americans average 5 close friends, Japanese average 2","MAP","World","World choropleth","Demographics","pew_global",7,8,5,8,4,7,8,50),
mk("hal020","How Much Toilet Paper Each Country Uses Per Year","Americans use 141 rolls per person, Chinese use 49","MAP","World","World choropleth","Demographics","statista_tp",7,9,5,8,3,7,8,55),
]

ideas2 = [
# --- Data viz meta ---
mk("hal021","The Most Common Chart Type on Reddit DataIsBeautiful","Choropleth maps dominate with 34% of all submissions","CHART","World","Bar chart","Science & Technology","reddit_dib_scrape",6,7,6,7,4,6,8,50),
mk("hal022","Color Palettes Used Most in Data Visualization","Viridis overtook rainbow in 2019 and never looked back","CHART","World","Bar chart","Science & Technology","github_analysis",5,5,6,7,3,7,8,45),
# --- Technology/internet ---
mk("hal023","Most Visited Websites by Country","Google dominates everywhere except China, Russia, and South Korea","MAP","World","World choropleth","Science & Technology","similarweb",7,8,6,7,4,8,7,55),
mk("hal024","Average Data Usage per Smartphone User by Country","Saudis use 40GB/month, Americans use 15GB","MAP","World","World choropleth","Science & Technology","gsma_mobile",6,7,6,7,4,8,7,55),
mk("hal025","Programming Languages Used by Country: Stack Overflow Survey","Python dominates globally but Rust is surging in Germany","MAP","World","World choropleth","Science & Technology","so_survey",6,7,6,7,4,8,7,60),
# --- The remaining untouched ProQuest sections ---
mk("hal026","US Natural Gas Production by State","Pennsylvania and Texas produce 60% of all US natural gas","MAP","US","State choropleth","Environment","eia_natgas",5,5,7,6,5,7,6,65),
mk("hal027","Renewable Energy Jobs by State","California leads with 500k clean energy workers","MAP","US","State choropleth","Labor","doe_useer",6,7,7,6,5,7,7,60),
mk("hal028","Foreign Direct Investment by Country: Inflows Map","The US, China, and Ireland attract the most FDI","MAP","World","World choropleth","Economy","unctad_fdi",5,5,7,7,5,8,7,60),
mk("hal029","Remittances as Percentage of GDP by Country","In Tajikistan, remittances are 35% of GDP","MAP","World","World choropleth","Economy","worldbank_remittances",6,6,7,8,5,8,7,65),
mk("hal030","Military Spending as Percentage of GDP by Country","Ukraine now spends 37% of GDP on defense","MAP","World","World choropleth","International Statistics","sipri_milex",7,7,7,7,7,8,7,65),
# --- Cross-refs nobody has tried ---
mk("hal031","Happiness Score vs Government Debt by Country","Happy countries tend to have moderate debt, not zero debt","XREF","World","Scatter plot","International Statistics","unsdsn_whr + D:/raw_data/Kaggle/archive (35)/historysaid-global-economic-dataset/data/core/imf_weo.csv",6,6,6,8,5,7,8,65),
mk("hal032","Asteroid Panic Level vs Actual Distance: The Overreaction Index","Media panic is inversely correlated with actual risk","XREF","World","Scatter plot","Science & Technology","D:/raw_data/Kaggle/archive (47)/asteroid_dataset_20251019.csv",6,6,6,9,5,7,9,90),
mk("hal033","Steam Game Review Score vs Estimated Owners","Popular games cluster at 75-85% positive reviews","XREF","World","Scatter plot","Entertainment","D:/raw_data/Kaggle/steam/steam_games_2026.csv",6,7,7,6,4,7,7,85),
mk("hal034","Student Years of Experience vs Salary in AI Jobs","Each year of experience adds $15k on average","XREF","World","Scatter plot","Labor","D:/raw_data/Kaggle/archive (42)/AI_Job_Market_Trends_2026.csv",6,7,7,6,5,7,7,80),
mk("hal035","Every TSMC Technical Indicator on One Dashboard","RSI, MACD, Bollinger Bands - the complete picture","CHART","World","Line chart","Economy","D:/raw_data/Kaggle/archive (34)/tsm_technical_indicators.csv",4,4,6,6,4,6,7,90),
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

print(f"BATCH_HAL: {len(all_ideas)} ideas generated")
print(f"[BATCH_HAL] Injected {len(new)} new ideas (skipped {dupes} dupes)")
