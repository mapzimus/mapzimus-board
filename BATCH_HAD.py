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
# --- Real Exchange Rate (BIS data) ---
mk("had001","Real Effective Exchange Rate: Strongest and Weakest Currencies","Which currencies are overvalued vs undervalued right now?","MAP","World","World choropleth","Economy","D:/raw_data/Kaggle/archive (35)/historysaid-global-economic-dataset/data/core/bis.csv",6,6,7,7,6,8,7,85),
mk("had002","Currency Strength Over 60 Years: The Dollar vs The World","How the USD real exchange rate shifted since 1964","CHART","World","Line chart","Economy","D:/raw_data/Kaggle/archive (35)/historysaid-global-economic-dataset/data/core/bis.csv",6,6,7,7,6,7,7,85),
# --- Global Population (Kaggle pop) ---
mk("had003","World Population by Country: 1950-2024 Animated","Watch India overtake China in real time","MAP","World","Animated choropleth","Population","D:/raw_data/Kaggle/pop/popolazione-globale-per-paese-1950-2024.csv",7,7,7,7,6,8,6,90),
mk("had004","Countries That Doubled Their Population Since 2000","The fastest-growing nations of the 21st century","MAP","World","World choropleth","Population","D:/raw_data/Kaggle/pop/popolazione-globale-per-paese-1950-2024.csv",7,7,7,8,6,8,7,90),
mk("had005","Population Growth Rate: Fastest vs Slowest Since 1950","Some countries grew 20x while others barely changed","RANK","World","Bar chart","Population","D:/raw_data/Kaggle/pop/popolazione-globale-per-paese-1950-2024.csv",7,7,7,8,6,7,7,90),
# --- Regional Economic Aggregates ---
mk("had006","GDP by World Region: How Economic Power Shifted Since 1960","East Asia went from 5% to 30% of world GDP","CHART","World","Area chart","Economy","D:/raw_data/Kaggle/archive (35)/historysaid-global-economic-dataset/data/aggregates/regional_aggregates.csv",7,7,7,8,6,8,7,85),
mk("had007","EU GDP vs US GDP: 60 Years of Divergence","Europe and America were equal in 2008. Not anymore.","CHART","World","Line chart","Economy","D:/raw_data/Kaggle/archive (35)/historysaid-global-economic-dataset/data/aggregates/regional_aggregates.csv",7,7,8,8,7,7,7,85),
# --- All Indicators Unified Dataset ---
mk("had008","Every Country by Every Metric: The Ultimate Scatter Explorer","17 indicators for 200 countries in one interactive viz","CHART","World","Scatter plot","International Statistics","D:/raw_data/Kaggle/archive (35)/historysaid-global-economic-dataset/data/unified/all_indicators.csv",5,5,6,6,4,7,8,85),
# --- Deep Cross-refs: Population x Economics ---
mk("had009","Population Growth vs GDP Growth by Country Since 1960","Do bigger populations mean bigger economies?","XREF","World","Scatter plot","Economy","D:/raw_data/Kaggle/pop/popolazione-globale-per-paese-1950-2024.csv + D:/raw_data/Kaggle/archive (35)/historysaid-global-economic-dataset/data/core/world_bank.csv",6,6,7,7,5,7,7,85),
mk("had010","Population Decline vs Government Debt: The Aging Bomb","Shrinking populations correlate with ballooning national debt","XREF","World","Scatter plot","Economy","D:/raw_data/Kaggle/pop/popolazione-globale-per-paese-1950-2024.csv + D:/raw_data/Kaggle/archive (35)/historysaid-global-economic-dataset/data/core/imf_weo.csv",7,7,7,8,7,7,8,80),
# --- More Viral US Maps ---
mk("had011","The Most Common Job in Every US State","Truck driver dominates but healthcare is taking over","MAP","US","State choropleth","Labor","bls_oes",8,9,7,7,5,8,7,65),
mk("had012","Average Commute Time by County","The counties where people spend 2+ hours driving to work","MAP","US","County choropleth","Transportation","census_acs",8,9,7,7,6,8,7,65),
mk("had013","Counties Where More People Moved Out Than In","The shrinking heart of rural America","MAP","US","County choropleth","Population","census_migration",8,7,7,7,7,8,7,65),
mk("had014","Percentage of Income Spent on Gas by State","With Iran War prices, some states spend 8% of income at the pump","XREF","US","State choropleth","Economy","D:/raw_data/Kaggle/archive (39)/iran_war_gas_prices_by_state.csv + D:/raw_data/Sage_Data/Real Personal Income and Regional Price Parities from the Regional Personal Income and Employment Database.csv",8,9,7,8,8,8,8,80),
mk("had015","States Where Religion Is Growing vs Declining","The Bible Belt is holding but New England collapsed","MAP","US","State choropleth","Demographics","D:/raw_data/Sage_Data/Adherent Rate from the U.S. Religion Census Database.xlsx",7,7,7,8,6,8,7,85),
# --- More Entertainment Viral ---
mk("had016","Valence vs Energy: The Spotify Mood Quadrant","Happy+energetic, happy+chill, sad+intense, sad+calm","CHART","World","Scatter plot","Entertainment","D:/raw_data/Kaggle/spotify/spotify_alltime_top100_songs.csv",7,8,7,7,5,8,8,90),
mk("had017","Games With 1M+ Reviews on Steam","Only 15 games have crossed the million-review threshold","RANK","World","Bar chart","Entertainment","D:/raw_data/Kaggle/steam/steam_games_2026.csv",7,8,7,7,5,6,7,85),
mk("had018","Steam Games by Release Year: The Annual Flood","More games released in 2025 than 2010-2015 combined","CHART","World","Bar chart","Entertainment","D:/raw_data/Kaggle/steam/steam_games_2026.csv",6,7,7,7,5,6,7,85),
# --- More Global Comparison ---
mk("had019","Government Revenue as % of GDP: Who Taxes Most?","Scandinavian countries collect 50%+ of GDP in taxes","MAP","World","World choropleth","International Statistics","D:/raw_data/Kaggle/archive (35)/historysaid-global-economic-dataset/data/core/imf_weo.csv",6,7,7,7,6,8,6,90),
mk("had020","Net Government Lending: Countries Running Surpluses","Only 15 countries spend less than they earn","MAP","World","World choropleth","International Statistics","D:/raw_data/Kaggle/archive (35)/historysaid-global-economic-dataset/data/core/imf_weo.csv",5,6,7,7,6,8,7,90),
]

ideas2 = [
# --- XREF: Breakfast x Population ---
mk("had021","Breakfast Cost vs Population Density by City","Dense cities pay more per meal - the space premium","XREF","World","Scatter plot","Food & Nutrition","D:/raw_data/Kaggle/archive (38)/breakfast basket.csv + D:/raw_data/Kaggle/pop/popolazione-globale-per-paese-1950-2024.csv",6,7,6,7,5,7,7,80),
# --- XREF: Currency x Trade ---
mk("had022","Real Exchange Rate vs GDP per Capita","Strong currencies in rich countries - chicken or egg?","XREF","World","Scatter plot","Economy","D:/raw_data/Kaggle/archive (35)/historysaid-global-economic-dataset/data/core/bis.csv + world_bank.csv",5,5,7,7,5,7,7,80),
# --- XREF: AI x Population ---
mk("had023","AI Adoption vs Population: Do Bigger Countries Adopt Slower?","India and China lag despite massive populations","XREF","World","Scatter plot","Science & Technology","D:/raw_data/Kaggle/archive (40)/ai_index_main.csv + D:/raw_data/Kaggle/pop/popolazione-globale-per-paese-1950-2024.csv",6,6,7,8,5,7,8,80),
# --- XREF: Steam x AI Jobs ---
mk("had024","Gaming Industry Growth vs AI Job Postings","Both sectors exploding but gaming started first","XREF","World","Line chart","Entertainment","D:/raw_data/Kaggle/steam/steam_games_2026.csv + D:/raw_data/Kaggle/archive (42)/AI_Job_Market_Trends_2026.csv",5,6,6,7,5,6,8,75),
# --- Deep Geography ---
mk("had025","Airbnb Price vs Walkability Score","The most walkable neighborhoods charge 2x premium","XREF","US","Scatter plot","Housing","D:/raw_data/airbnb + D:/raw_data/WalkabilityIndex",8,8,7,7,5,7,8,65),
mk("had026","Public School Count per 10k Population by State","Which states have the most schools relative to population?","MAP","US","State choropleth","Education","D:/raw_data/Public_School_Characteristics_2022-23.csv",6,7,7,7,5,7,7,90),
mk("had027","Charter Schools as Percentage of All Public Schools by State","The states leading the charter school movement","MAP","US","State choropleth","Education","D:/raw_data/Public_School_Characteristics_2022-23.csv",6,7,7,7,6,7,7,90),
# --- Mega 4+ Dataset Cross-refs ---
mk("had028","The American Wellbeing Index: Income + Health + Education + Crime","A composite score from 4 datasets by state","XREF","US","State choropleth","Demographics","D:/raw_data/Sage_Data + D:/raw_data/fbi + D:/raw_data/fivethirtyeight + census",7,8,7,7,6,8,8,65),
mk("had029","The Global Development Dashboard: GDP + Governance + Health + Education","4 indicators per country in one bivariate grid","XREF","World","Scatter plot","International Statistics","D:/raw_data/Kaggle/archive (35)/historysaid-global-economic-dataset/data/unified/all_indicators.csv",6,6,6,7,5,7,8,85),
mk("had030","Oil + Gas + Vehicles + Income: The Full Energy Cost Chain by State","From crude to consumer impact in 4 linked datasets","XREF","US","State choropleth","Economy","D:/raw_data/Kaggle/archive (39) + D:/raw_data/Sage_Data + D:/raw_data/Kaggle/archive (48)/fuel_prices_1970_2026.csv",7,8,7,7,8,8,8,75),
# --- Fun/Viral Standalone ---
mk("had031","Countries Where Breakfast Costs More Than an Hours Minimum Wage","In 12 countries, you cant afford breakfast on minimum wage","MAP","World","World choropleth","Food & Nutrition","D:/raw_data/Kaggle/archive (38)/breakfast basket.csv + ilo_wages",8,9,7,9,7,8,9,65),
mk("had032","The UFO Shape Taxonomy: A Visual Guide","From orbs to chevrons - every shape reported to NUFORC","CHART","US","Bar chart","Science & Technology","D:/raw_data/Kaggle/archive (50)/uap_reports.csv",7,7,6,8,5,8,8,90),
mk("had033","Most Streamed Song from Each Country","Only 12 countries have produced a billion-stream hit","MAP","World","World choropleth","Entertainment","D:/raw_data/Kaggle/spotify/spotify_alltime_top100_songs.csv",8,8,7,8,5,8,8,90),
mk("had034","The Gold Standard Era vs Fiat Era: Price Stability Comparison","Prices barely moved 1833-1933, then everything changed","CHART","World","Line chart","Economy","D:/raw_data/Kaggle/archive (36)/monthly.csv",7,7,7,8,6,7,8,95),
mk("had035","Student Depression Score by Gender and Year of Study","Female 3rd-year students score highest on depression measures","CHART","World","Bar chart","Health","D:/raw_data/Kaggle/mentalburnout/student_mental_health_burnout.csv",8,8,7,7,6,6,7,80),
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

print(f"BATCH_HAD: {len(all_ideas)} ideas generated")
print(f"[BATCH_HAD] Injected {len(new)} new ideas (skipped {dupes} dupes)")
