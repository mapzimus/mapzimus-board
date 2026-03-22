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
# --- "If X Were a Country" series ---
mk("haj001","If Every US State Were a Country: GDP Ranking","Florida would be the 16th largest economy on Earth","MAP","World","Special map","Economy","bea_gdp_state",8,9,7,8,5,8,8,70),
mk("haj002","If Every US City Had a Country-Equivalent Population","Houston = Austria, Phoenix = Switzerland, San Antonio = Norway","MAP","World","Special map","Population","census_2020",7,8,6,8,4,8,8,65),
mk("haj003","If The Great Lakes Were a Country: 20% of Global Fresh Water","More freshwater than all of Africa combined","MAP","World","Special map","Geography & Environment","usgs_water",7,7,6,9,4,8,9,65),
# --- "X vs Y: Which Would You Guess?" interactive ---
mk("haj004","Which Country Has More People: Quiz Map","Myanmar vs Australia? Ethiopia vs Germany?","MAP","World","World choropleth","Population","D:/raw_data/Kaggle/pop/popolazione-globale-per-paese-1950-2024.csv",7,8,6,8,4,8,8,90),
mk("haj005","Which US State Has Higher GDP: Quiz Chart","Illinois vs Pennsylvania? Georgia vs New Jersey?","CHART","US","Bar chart","Economy","bea_gdp_state",7,8,7,7,4,6,8,65),
# --- US Census Quirks ---
mk("haj006","US Counties Named After Presidents","There are 31 Washington counties and 26 Jefferson counties","MAP","US","County choropleth","History","census_tiger",7,7,6,8,3,8,8,70),
mk("haj007","US Counties With the Same Name in Different States","Springfield exists in 33 states, but which Springfield is biggest?","MAP","US","Dot map","Geography & Environment","census_gazetteer",7,8,6,8,3,8,8,65),
mk("haj008","Every US County Seat Mapped: Population Comparison","Some county seats have 50 people, others have millions","MAP","US","Dot map","Population","census_2020",6,6,6,7,4,8,7,65),
# --- Climate/Environment deep ---
mk("haj009","Average Annual Rainfall by Country","Colombia gets 3,000mm, Egypt gets 18mm","MAP","World","World choropleth","Climate","worldclim",6,6,6,7,4,8,6,65),
mk("haj010","Countries Most Vulnerable to Sea Level Rise","Bangladesh, Netherlands, and Pacific Islands at greatest risk","MAP","World","World choropleth","Climate","notre_dame_gain",8,7,7,8,8,8,7,65),
mk("haj011","Deforestation Rate by Country: Who Is Losing Forests Fastest?","Brazil and Indonesia dominate but Congo is catching up","MAP","World","World choropleth","Environment","gfw_tree_loss",7,7,7,7,7,8,7,65),
mk("haj012","CO2 Emissions per Capita: The Global Carbon Map","Qatar emits 35 tons per person, Chad emits 0.1","MAP","World","World choropleth","Climate","D:/raw_data/Our World In Data/co-emissions-per-capita.csv",7,7,7,7,7,8,7,80),
# --- Social media viral bait ---
mk("haj013","The Most Overrated and Underrated US States: Reddit Survey","Vermont consistently underrated, California consistently overrated","RANK","US","Bar chart","Entertainment","reddit_survey",8,9,7,7,5,6,8,50),
mk("haj014","How Americans Pronounce Caramel by Region","CAR-ml vs CARE-a-mel: the pronunciation border","MAP","US","State choropleth","Demographics","dialect_survey",8,9,6,7,4,8,8,55),
mk("haj015","Pop vs Soda vs Coke: The Great American Beverage Debate","The dialect map that starts arguments","MAP","US","County choropleth","Demographics","dialect_survey",9,9,6,7,4,8,8,60),
# --- Sport with data ---
mk("haj016","Olympic Medal Count Adjusted for Population","Tiny nations like Grenada and Bahamas dominate per-capita","MAP","World","World choropleth","Sports & Recreation","olympics_data",7,8,7,8,5,8,8,70),
mk("haj017","NFL Team Fandom by County: The Geographic Loyalty Map","Where Cowboys territory ends and Texans territory begins","MAP","US","County choropleth","Sports & Recreation","nyt_fandom_survey",8,9,6,7,4,8,7,55),
mk("haj018","World Cup Host Nations: Economic Impact Before and After","GDP growth in the 2 years surrounding every World Cup","CHART","World","Bar chart","Sports & Recreation","D:/raw_data/worldcup + D:/raw_data/Kaggle/archive (35)/historysaid-global-economic-dataset/data/core/world_bank.csv",6,6,7,8,5,7,8,70),
# --- Personal finance viral ---
mk("haj019","How Much You Need to Earn to Afford a Home in Every State","From $35k in West Virginia to $200k in Hawaii","MAP","US","State choropleth","Housing","zillow + census",8,9,8,7,7,8,7,60),
mk("haj020","Student Loan Debt by State: Average Balance at Graduation","Connecticut graduates owe $39k, Utah graduates owe $19k","MAP","US","State choropleth","Education","nces_studentloan",8,9,7,7,6,7,7,60),
]

ideas2 = [
# --- Historical trends with emotional weight ---
mk("haj021","Americas Opioid Crisis: Overdose Deaths by State 2000-2024","The epidemic that killed 100k Americans per year","MAP","US","Animated choropleth","Health","cdc_wonder",9,8,7,7,9,8,7,70),
mk("haj022","US Life Expectancy by County: The 20-Year Gap","People in some counties live to 87, others die at 67","MAP","US","County choropleth","Health","ihme_gbd",9,8,7,8,8,8,8,65),
mk("haj023","Maternal Mortality Rate by Country: A Global Shame","The US rate is 5x higher than other wealthy nations","MAP","World","World choropleth","Health","who_gho",9,7,7,8,8,8,7,65),
mk("haj024","Child Poverty Rate by US County","15 million American children live below the poverty line","MAP","US","County choropleth","Economy","census_saipe",9,8,7,7,8,8,7,65),
mk("haj025","Global Refugee Population by Host Country","Turkey hosts 3.5 million, Germany 2.1 million","MAP","World","World choropleth","International Statistics","unhcr_stats",8,7,7,7,8,8,7,65),
# --- Fun data + real local datasets ---
mk("haj026","MBTA Ridership by Station: Bostons Transit Map","Park Street gets 20k daily, some stations get 200","MAP","US","Dot map","Transportation","D:/raw_data/MBTA Data 2025",6,6,7,6,4,8,7,75),
mk("haj027","MBTA Service Reliability by Line: On-Time Performance","The Green Line is late 30% of the time","CHART","US","Bar chart","Transportation","D:/raw_data/MBTA Data 2025",6,7,7,6,5,6,7,75),
mk("haj028","Walkability Index by Census Block Group","The most and least walkable neighborhoods in America","MAP","US","County choropleth","Transportation","D:/raw_data/WalkabilityIndex",7,8,7,7,5,8,7,75),
mk("haj029","Airbnb Price vs Neighborhood Crime Rate","Tourists pay less to stay in high-crime areas","XREF","US","Scatter plot","Housing","D:/raw_data/airbnb + D:/raw_data/fbi",7,8,6,7,6,7,7,60),
mk("haj030","US Companies by Revenue: The Corporate Headquarters Map","Where Americas biggest companies are based","MAP","US","Dot map","Economy","D:/raw_data/EconData/USCompanies.csv",6,7,7,6,4,8,7,85),
# --- Final creative angles ---
mk("haj031","Countries by Timezone Offset from Greenwich","The political decisions behind where the clock line falls","MAP","World","World choropleth","Geography & Environment","manual_tz",6,6,6,7,3,8,7,65),
mk("haj032","How Every Country Votes at the UN General Assembly","Alignment with the US vs China in UN votes","MAP","World","World choropleth","International Statistics","un_voting",7,7,6,8,7,8,8,60),
mk("haj033","Countries by Rail Network Density","India has 68k km of track, Switzerland has the densest per area","MAP","World","World choropleth","Transportation","uic_rail",5,5,7,7,4,8,7,60),
mk("haj034","Minimum Legal Drinking Age by Country","From 16 in Germany to 21 in the US to none in some nations","MAP","World","World choropleth","International Statistics","who_gho_alcohol",7,8,6,7,4,8,6,65),
mk("haj035","Speed Limits by Country: The Autobahn Effect","Germany has no speed limit, others cap at 60 mph","MAP","World","World choropleth","Transportation","manual_transport",7,8,6,7,4,8,7,60),
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

print(f"BATCH_HAJ: {len(all_ideas)} ideas generated")
print(f"[BATCH_HAJ] Injected {len(new)} new ideas (skipped {dupes} dupes)")
