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
# --- "Did You Know?" viral series ---
mk("hag001","Countries Where the Average Person Earns Less Than $5/Day","Still over 1 billion people live on almost nothing","MAP","World","World choropleth","Economy","D:/raw_data/Kaggle/archive (35)/historysaid-global-economic-dataset/data/core/world_bank.csv",8,7,7,8,7,8,7,85),
mk("hag002","US States Where the Average Home Costs 10+ Years of Income","California, Hawaii, and New York lead the unaffordability crisis","MAP","US","State choropleth","Housing","zillow + census",8,9,8,7,7,8,7,60),
mk("hag003","Countries With No Army","28 countries have no military at all","MAP","World","World choropleth","International Statistics","manual_military",7,7,6,9,5,8,8,60),
mk("hag004","Most Landlocked Country in the World: Distance to Ocean","Uzbekistan is doubly landlocked - surrounded by landlocked countries","MAP","World","Special map","Geography & Environment","manual_geo",7,7,6,9,4,8,9,60),
mk("hag005","Countries Smaller Than Rhode Island","There are over 40 sovereign nations smaller than the smallest US state","MAP","World","Special map","Geography & Environment","manual_geo",7,8,6,9,4,8,8,65),
mk("hag006","US States by Coastline Length: Alaska Has More Than All Others Combined","Alaska: 33,904 miles. Florida: 8,436. Everyone else: less.","RANK","US","Bar chart","Geography & Environment","noaa_shoreline",7,7,7,9,4,7,8,70),
mk("hag007","Countries That Changed Their Name in the Last 50 Years","From Rhodesia to Zimbabwe, Burma to Myanmar, and Swaziland to Eswatini","MAP","World","World choropleth","History","manual_history",7,7,6,8,4,8,8,65),
mk("hag008","Fastest Shrinking Cities in the US: Population Loss Since 2010","Detroit, St. Louis, and Cleveland lead the exodus","MAP","US","Dot map","Population","census_2020",8,8,7,7,7,8,7,65),
mk("hag009","US Counties Accessible Only by Boat or Plane","No road access to these remote American communities","MAP","US","Dot map","Geography & Environment","manual_transport",7,7,5,9,4,8,9,55),
mk("hag010","Countries Where Women Outnumber Men by 10%+","The gender imbalance map - Eastern Europe and Russia stand out","MAP","World","World choropleth","Demographics","un_population",7,7,6,8,5,8,7,65),
# --- "Comparison" viral format ---
mk("hag011","Californias GDP Compared to Entire Countries","If CA were a country it would be the 5th largest economy","MAP","World","Special map","Economy","D:/raw_data/Kaggle/archive (35)/historysaid-global-economic-dataset/data/core/world_bank.csv",8,9,7,8,5,8,8,80),
mk("hag012","Texas Population vs European Countries","Texas has more people than the Netherlands, Belgium, and Switzerland combined","MAP","World","Special map","Population","D:/raw_data/Kaggle/pop/popolazione-globale-per-paese-1950-2024.csv",7,8,7,8,5,8,8,85),
mk("hag013","NYC GDP vs African Countries","New York City produces more economic output than 46 African nations","MAP","World","Special map","Economy","bea + D:/raw_data/Kaggle/archive (35)/historysaid-global-economic-dataset/data/core/world_bank.csv",7,7,7,9,6,8,8,75),
mk("hag014","Amazon Rainforest Size vs European Countries Overlaid","The Amazon would cover 75% of the EU","MAP","World","Special map","Geography & Environment","manual_geo",7,7,6,8,5,8,8,65),
mk("hag015","Lake Superiors Volume vs Other Great Lakes Combined","Superior holds 10% of all surface freshwater on Earth","CHART","US","Bar chart","Geography & Environment","usgs_water",6,6,6,8,4,7,8,65),
# --- Instagram carousel-friendly series ---
mk("hag016","Top 10 Most Expensive Cities for a Cup of Coffee","From Seoul to Zurich - the latte index","RANK","World","Bar chart","Food & Nutrition","D:/raw_data/Kaggle/archive (38)/breakfast basket.csv",8,9,7,7,5,6,7,90),
mk("hag017","Top 10 Safest Countries in the World by Political Stability","Iceland, New Zealand, and Switzerland top the list","RANK","World","Bar chart","International Statistics","D:/raw_data/Kaggle/archive (35)/historysaid-global-economic-dataset/data/core/world_bank_wgi.csv",7,7,7,7,5,7,6,90),
mk("hag018","Top 10 Countries by AI Research Papers per Capita","Small nations like Singapore and Israel dominate per-capita","RANK","World","Bar chart","Science & Technology","D:/raw_data/Kaggle/archive (40)/ai_index_main.csv",6,6,7,8,5,6,8,85),
mk("hag019","Top 10 Fastest-Growing Populations: 2000-2024","Qatar grew 370% in 24 years due to migrant workers","RANK","World","Bar chart","Population","D:/raw_data/Kaggle/pop/popolazione-globale-per-paese-1950-2024.csv",7,7,7,8,5,7,7,90),
mk("hag020","Top 10 US States by Gas Price Increase During Iran War","California, Nevada, and Washington hit hardest","RANK","US","Bar chart","Economy","D:/raw_data/Kaggle/archive (39)/iran_war_gas_prices_by_state.csv",7,8,7,7,8,6,7,90),
]

ideas2 = [
# --- Deeper data cross-refs nobody has done ---
mk("hag021","Global Trends Engagement by Continent Over Time","When does each region pay attention to global events?","CHART","World","Area chart","Science & Technology","D:/raw_data/Kaggle/archive (37)/enhanced_global_trends_dataset.csv",5,5,6,7,5,7,7,85),
mk("hag022","TSMC Balance Sheet vs Revenue Growth","How TSMC funds its $30B annual capex","CHART","World","Area chart","Economy","D:/raw_data/Kaggle/archive (34)/tsm_balance_sheet.csv",4,4,7,6,4,6,7,90),
mk("hag023","TSMC Quarterly Revenue Trend: The AI Demand Curve","Revenue doubled in 2 years from AI chip orders","CHART","World","Bar chart","Economy","D:/raw_data/Kaggle/archive (34)/tsm_quarterly_financials.csv",5,5,7,7,5,6,7,90),
mk("hag024","UFO Reports per Year: The Exponential Rise Since 1990","Internet access = more reporting or more sightings?","CHART","US","Line chart","Science & Technology","D:/raw_data/Kaggle/archive (50)/uap_reports.csv",7,7,6,8,5,7,8,90),
mk("hag025","Student Burnout by Course: Which Majors Suffer Most?","BTech and nursing lead in burnout scores","CHART","World","Bar chart","Education","D:/raw_data/Kaggle/mentalburnout/student_mental_health_burnout.csv",7,8,7,7,5,6,7,80),
mk("hag026","Spotify Acousticness vs Streams: Do Acoustic Songs Chart?","The most-streamed songs have near-zero acousticness","CHART","World","Scatter plot","Entertainment","D:/raw_data/Kaggle/spotify/spotify_alltime_top100_songs.csv",6,7,6,7,4,7,7,90),
mk("hag027","Steam Estimated Owners vs Price: The Free-to-Play Dominance","F2P games own 80% of the player base","CHART","World","Scatter plot","Entertainment","D:/raw_data/Kaggle/steam/steam_games_2026.csv",6,7,7,7,5,7,7,85),
# --- Weather + economy + behavior crossovers ---
mk("hag028","Sunshine Hours vs GDP per Capita: The Productivity Paradox","Less sunny countries tend to be richer - why?","XREF","World","Scatter plot","Economy","nasa_solar + D:/raw_data/Kaggle/archive (35)/historysaid-global-economic-dataset/data/core/world_bank.csv",6,6,6,9,5,7,9,60),
mk("hag029","Coffee Consumption vs Productivity by Country","The Nordic coffee-productivity connection","XREF","World","Scatter plot","Economy","ico_coffee + D:/raw_data/Kaggle/archive (35)/historysaid-global-economic-dataset/data/core/world_bank.csv",7,8,6,9,4,7,9,55),
mk("hag030","Alcohol Consumption vs Life Expectancy by Country","France drinks heavily but lives long - the French Paradox mapped","XREF","World","Scatter plot","Health","who_gho + D:/raw_data/Our World In Data/life-expectancy.csv",7,8,6,9,5,7,8,65),
# --- Final mega xrefs ---
mk("hag031","Religious Adherence + Income + Education + Vehicles by State","The four-dimensional American lifestyle map","XREF","US","State choropleth","Demographics","D:/raw_data/Sage_Data/Adherent Rate from the U.S. Religion Census Database.xlsx + D:/raw_data/Sage_Data/Real Personal Income and Regional Price Parities from the Regional Personal Income and Employment Database.csv + D:/raw_data/Sage_Data/Assessment by All Students from the National Assessment of Educational Progress (NAEP) Database.csv + D:/raw_data/Sage_Data/Total Vehicles Registered from the All Motor Vehicles  (Private + Public; Registered Vehicles) Database (1).csv",6,7,6,7,5,7,8,75),
mk("hag032","AI Adoption + GDP + Education + Internet: The National Tech Readiness Score","A composite index ranking 50 countries on digital readiness","XREF","World","World choropleth","Science & Technology","D:/raw_data/Kaggle/archive (40)/ai_index_main.csv",6,6,7,7,5,7,8,85),
mk("hag033","Gas Price + Vehicle Registrations + Religion + Real Income: Red State vs Blue State","Do conservative states drive more, pray more, and earn less?","XREF","US","Bivariate choropleth","Elections","D:/raw_data/Kaggle/archive (39) + D:/raw_data/Sage_Data + D:/raw_data/fivethirtyeight",7,7,6,8,7,8,8,70),
mk("hag034","Breakfast Cost + Governance + GDP + Population: The Global Wellbeing Scatter","Four metrics that together paint a complete country portrait","XREF","World","Scatter plot","International Statistics","D:/raw_data/Kaggle/archive (38)/breakfast basket.csv + world_bank_wgi + world_bank + pop",5,5,6,7,5,7,8,65),
mk("hag035","NVIDIA + TSMC + Bitcoin + Gold + Oil: The 5 Asset Portfolio Chart","The assets that defined the 2020s economy in one chart","XREF","World","Line chart","Economy","D:/raw_data/Kaggle/archive (45) + archive (34) + archive (49) + archive (36) + archive (48)",6,6,7,8,6,7,8,75),
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

print(f"BATCH_HAG: {len(all_ideas)} ideas generated")
print(f"[BATCH_HAG] Injected {len(new)} new ideas (skipped {dupes} dupes)")
