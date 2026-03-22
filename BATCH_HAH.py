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
# --- "The Map That Will Make You Think" series ---
mk("hah001","Countries Where More People Die Than Are Born Each Year","The natural decrease map - 35 countries are shrinking naturally","MAP","World","World choropleth","Population","un_vitals",7,7,7,8,7,8,7,65),
mk("hah002","US States With More Guns Than People","There are at least 15 states where firearms outnumber residents","MAP","US","State choropleth","Crime and Law Enforcement","atf_firearms",8,8,6,8,7,8,7,60),
mk("hah003","Countries Where the Median Age Will Double by 2060","The aging crisis accelerates: from 20 to 40 in one generation","MAP","World","World choropleth","Population","un_population",7,7,7,8,7,8,8,60),
mk("hah004","US Counties That Lost Population Every Decade Since 1950","The places America is abandoning","MAP","US","County choropleth","Population","census_historical",8,7,7,8,7,8,8,65),
mk("hah005","Countries Where Life Expectancy Decreased in the Last Decade","Shocking reversals in health progress","MAP","World","World choropleth","Health","who_gho",8,7,7,8,8,8,8,65),
# --- Hot-button viral (carefully factual) ---
mk("hah006","Immigration Rate vs GDP Growth by Country: 1990-2024","Do immigrants help or hurt economic growth? The data says...","XREF","World","Scatter plot","Economy","D:/raw_data/Kaggle/archive (35)/historysaid-global-economic-dataset/data/core/world_bank.csv + un_migration",7,7,7,8,8,7,8,60),
mk("hah007","Minimum Wage vs Big Mac Price by Country","The Big Mac Index meets the minimum wage debate","XREF","World","Scatter plot","Economy","D:/raw_data/Kaggle/archive (38)/breakfast basket.csv + ilo_wages",8,9,7,8,6,7,8,60),
mk("hah008","Prison Population per Capita vs Crime Rate by Country","More prisoners doesnt always mean less crime","XREF","World","Scatter plot","Crime and Law Enforcement","world_prison_brief + D:/raw_data/Our World In Data/homicide-rate-unodc.csv",7,7,7,8,8,7,8,60),
mk("hah009","Healthcare Spending vs Life Expectancy: The US Outlier","America spends the most and doesnt live the longest","XREF","World","Scatter plot","Health","who_gho + D:/raw_data/Kaggle/archive (35)/historysaid-global-economic-dataset/data/core/world_bank.csv",8,8,7,8,7,7,7,65),
mk("hah010","Education Spending vs Test Scores by Country","Throwing money at education doesnt always work","XREF","World","Scatter plot","Education","D:/raw_data/Kaggle/archive (35)/historysaid-global-economic-dataset/data/core/world_bank.csv + pisa_scores",7,7,7,8,6,7,8,60),
# --- "Numbers That Will Blow Your Mind" series ---
mk("hah011","How Many Earths Fit in Jupiter?","Solar system objects scaled to visual comparison","CHART","World","Infographic","Science & Technology","nasa_jpl",7,7,6,8,4,9,8,65),
mk("hah012","If The World Were 100 People: A Demographic Breakdown","60 Asian, 17 African, 10 European, 8 Latin American, 5 North American","CHART","World","Infographic","Demographics","un_population",8,8,7,7,4,8,8,70),
mk("hah013","Every Dollar the US Government Spends: A Treemap","Social Security 23%, Defense 13%, Medicare 12%...","CHART","US","Treemap","Economy","usaspending",7,8,8,6,6,8,6,70),
mk("hah014","Every Dollar of US Tax Revenue: Where It Comes From","Individual income tax 50%, payroll tax 36%, corporate 7%","CHART","US","Treemap","Economy","irs_soi",7,8,8,6,5,8,6,70),
mk("hah015","The Scale of US National Debt Visualized","$34 trillion in $100 bills would cover Manhattan 3 times","CHART","US","Infographic","Economy","treasury_debt",8,8,7,8,7,8,8,70),
# --- Completionist: underrepresented section coverage ---
mk("hah016","Nuclear Power Plants by Country","32 countries have them, 13 are building new ones","MAP","World","Dot map","Science & Technology","iaea_pris",6,6,7,7,6,8,7,70),
mk("hah017","Countries Currently at War or Armed Conflict","There are 56 active conflicts right now","MAP","World","World choropleth","International Statistics","acled_conflict",8,7,7,7,9,8,7,65),
mk("hah018","Languages at Risk of Extinction: Mapped","2,500 languages have fewer than 1,000 speakers","MAP","World","Dot map","Demographics","unesco_atlas",7,7,5,8,7,8,8,55),
mk("hah019","Volcano Locations and Last Eruption Date","The Ring of Fire visualized with temporal data","MAP","World","Dot map","Geography & Environment","smithsonian_gvp",6,6,6,7,5,8,7,70),
mk("hah020","Earthquake Epicenters: Every 5+ Magnitude Since 2000","Tectonic plate boundaries light up in seismic data","MAP","World","Dot map","Geography & Environment","usgs_earthquake",7,6,6,7,6,9,7,75),
]

ideas2 = [
# --- "By the Numbers" viral ---
mk("hah021","Every Country That Gained Independence from Britain","A quarter of the worlds countries were once British colonies","MAP","World","World choropleth","History","manual_history",7,7,6,8,5,8,7,65),
mk("hah022","Countries That Changed Their Capital City","Brazil, Nigeria, Pakistan, Myanmar, and 20+ others","MAP","World","World choropleth","History","manual_history",7,7,6,8,4,8,8,60),
mk("hah023","The 20 Newest Countries in the World","South Sudan (2011) is the newest, but Kosovo and others are disputed","MAP","World","World choropleth","History","manual_history",7,7,6,8,5,8,7,65),
mk("hah024","US Interstate Highway System: Every Route Mapped","The 50,000-mile network that changed America","MAP","US","Line map","Transportation","fhwa_nhpn",6,7,7,6,4,9,6,70),
mk("hah025","Amtrak Ridership by Route: The Lines Nobody Rides","The Northeast Corridor carries 80% of all Amtrak passengers","MAP","US","Line map","Transportation","amtrak_ridership",6,7,7,7,5,8,7,65),
# --- Remaining cross-refs with every local dataset combo ---
mk("hah026","Arrest Rate vs Real Personal Income by State","Richer states have lower arrest rates - but not always","XREF","US","Scatter plot","Crime and Law Enforcement","D:/raw_data/Sage_Data/Arrests by Race from the Arrests Database.csv + D:/raw_data/Sage_Data/Real Personal Income and Regional Price Parities from the Regional Personal Income and Employment Database.csv",7,7,7,7,6,7,7,80),
mk("hah027","NAEP Math Score vs Manufacturing Employment Share","Deindustrialized states have lower math performance","XREF","US","Scatter plot","Education","D:/raw_data/Sage_Data/Assessment by All Students from the National Assessment of Educational Progress (NAEP) Database.csv + D:/raw_data/Sage_Data/State and Local  Personal Income and Employment by NAICS Industry (1998 - Current) from the Regional Personal Income and Employment Database.csv",6,6,7,8,6,7,8,80),
mk("hah028","Marijuana Use vs Congregations per Capita by State","The spiritual vs secular lifestyle map","XREF","US","Bivariate choropleth","Demographics","D:/raw_data/Sage_Data/Marijuana Use in the Past Month from the National Survey on Drug Use and Health (NSDUH), 2015-2019 [Archive] Database.csv + D:/raw_data/Sage_Data/Number of Congregations from the U.S. Religion Census Database.xlsx",7,7,6,8,6,8,8,80),
mk("hah029","Iran War Gas Spike vs Charter School Density by State","A random-seeming cross-ref that actually reveals economic vulnerability","XREF","US","Scatter plot","Economy","D:/raw_data/Kaggle/archive (39)/iran_war_gas_prices_by_state.csv + D:/raw_data/Public_School_Characteristics_2022-23.csv",5,5,5,7,5,6,8,80),
mk("hah030","GDP per Capita vs Asteroid Detection Funding","Rich countries find more asteroids because they look harder","XREF","World","Scatter plot","Science & Technology","D:/raw_data/Kaggle/archive (47)/asteroid_dataset_20251019.csv + D:/raw_data/Kaggle/archive (35)/historysaid-global-economic-dataset/data/core/world_bank.csv",5,5,6,8,5,7,8,70),
mk("hah031","Steam Games Released per Year vs AI Job Postings","Two tech sectors exploding in parallel","XREF","World","Line chart","Science & Technology","D:/raw_data/Kaggle/steam/steam_games_2026.csv + D:/raw_data/Kaggle/archive (42)/AI_Job_Market_Trends_2026.csv",5,5,6,7,5,6,7,75),
mk("hah032","Spotify Song Valence vs Country Corruption Score","Happier music comes from less corrupt countries","XREF","World","Scatter plot","Entertainment","D:/raw_data/Kaggle/spotify/spotify_alltime_top100_songs.csv + D:/raw_data/Kaggle/archive (35)/historysaid-global-economic-dataset/data/core/world_bank_wgi.csv",5,6,5,9,4,7,9,65),
mk("hah033","Global Population Weighted by GDP: The Economic Map","Redrawing the world map where area = GDP contribution","MAP","World","Special map","Economy","D:/raw_data/Kaggle/pop/popolazione-globale-per-paese-1950-2024.csv + D:/raw_data/Kaggle/archive (35)/historysaid-global-economic-dataset/data/core/world_bank.csv",6,6,6,8,5,8,9,75),
mk("hah034","Student Sleep Hours by Gender and Stress Level","Female students with high stress sleep 1.5 hours less","CHART","World","Bar chart","Health","D:/raw_data/Kaggle/mentalburnout/student_mental_health_burnout.csv",7,8,7,7,5,6,7,80),
mk("hah035","McDonalds Stock During Recessions: The Comfort Food Trade","MCD outperforms the market during every recession","CHART","US","Line chart","Economy","D:/raw_data/Kaggle/archive (43)/MCD.csv",7,8,7,8,5,7,7,90),
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

print(f"BATCH_HAH: {len(all_ideas)} ideas generated")
print(f"[BATCH_HAH] Injected {len(new)} new ideas (skipped {dupes} dupes)")
