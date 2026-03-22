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
# --- Unexpected correlations viral ---
mk("hae001","Countries with Best Regulatory Quality Have Cheapest Breakfast","Good regulation = competitive food markets","XREF","World","Scatter plot","Food & Nutrition","D:/raw_data/Kaggle/archive (38)/breakfast basket.csv + D:/raw_data/Kaggle/archive (35)/historysaid-global-economic-dataset/data/core/world_bank_wgi.csv",6,7,6,9,5,7,9,75),
mk("hae002","Spotify Danceability Score vs Country GDP per Capita","Rich countries listen to less danceable music","XREF","World","Scatter plot","Entertainment","D:/raw_data/Kaggle/spotify/spotify_alltime_top100_songs.csv + world_bank.csv",6,7,5,9,4,7,9,70),
mk("hae003","UFO Sightings per Capita vs Education Level by State","More educated states report more UFOs per person","XREF","US","Scatter plot","Science & Technology","D:/raw_data/Kaggle/archive (50)/uap_reports.csv + D:/raw_data/Sage_Data/Assessment by All Students from the National Assessment of Educational Progress (NAEP) Database.csv",7,7,6,9,6,7,9,70),
mk("hae004","Marijuana Use Rate vs NAEP Scores by State","Does cannabis use correlate with test performance?","XREF","US","Scatter plot","Education","D:/raw_data/Sage_Data/Marijuana Use in the Past Month from the National Survey on Drug Use and Health (NSDUH), 2015-2019 [Archive] Database.csv + D:/raw_data/Sage_Data/Assessment by All Students from the National Assessment of Educational Progress (NAEP) Database.csv",7,7,6,8,7,7,8,80),
mk("hae005","Vehicle Registrations per Capita vs Obesity Rate by State","The most car-dependent states are also the heaviest","XREF","US","Bivariate choropleth","Health","D:/raw_data/Sage_Data/Total Vehicles Registered from the All Motor Vehicles  (Private + Public; Registered Vehicles) Database (1).csv + cdc_obesity",7,8,6,8,6,8,8,70),
mk("hae006","Religious Adherence vs Divorce Rate by State","The Bible Belt paradox: most religious yet highest divorce","XREF","US","Bivariate choropleth","Demographics","D:/raw_data/Sage_Data/Adherent Rate from the U.S. Religion Census Database.xlsx + D:/raw_data/fivethirtyeight/marriage/divorce.csv",8,8,7,9,7,8,9,75),
mk("hae007","Bitcoin Price vs Gold Price vs CPI: Triple Inflation Hedge","Which asset actually protects against inflation?","XREF","World","Line chart","Economy","D:/raw_data/Kaggle/archive (49)/BTC_prices.csv + D:/raw_data/Kaggle/archive (36)/monthly.csv + D:/raw_data/cpi/historical-cpi-u-202602.xlsx",7,7,7,8,6,7,8,80),
mk("hae008","Student Screen Time vs Physical Activity: The Inverse Relationship","Every extra hour of screen time = 0.3 fewer hours of exercise","XREF","World","Scatter plot","Health","D:/raw_data/Kaggle/mentalburnout/student_mental_health_burnout.csv",7,8,7,7,5,7,7,80),
# --- TIL-style viral maps ---
mk("hae009","Countries Where Agriculture Is Still Over 30% of GDP","The worlds last agrarian economies","MAP","World","World choropleth","Economy","D:/raw_data/Kaggle/archive (35)/historysaid-global-economic-dataset/data/core/world_bank.csv",6,6,7,8,5,8,7,85),
mk("hae010","Countries Older Than the United States","There are only about 20 - the rest are younger","MAP","World","World choropleth","History","manual_history",7,7,6,9,4,8,9,60),
mk("hae011","Every Country That Has Been Independent for Less Than 50 Years","The worlds newest nations mapped","MAP","World","World choropleth","History","manual_history",7,7,6,9,4,8,8,60),
mk("hae012","US States Named After People vs Geographic Features","The etymology of every state name","MAP","US","State choropleth","Geography & Environment","manual_geo",7,7,6,8,4,7,8,70),
mk("hae013","The Longest River in Every Country","Nile, Amazon, Yangtze - and the surprising short ones","MAP","World","World choropleth","Geography & Environment","manual_geo",6,6,6,7,4,8,7,60),
mk("hae014","Countries That Drive on the Left vs Right","The British Empire legacy mapped","MAP","World","World choropleth","History","manual_transport",7,8,6,7,4,8,7,70),
mk("hae015","Time Zones With the Most People Living in Them","UTC+8 (China) has 1.5 billion people alone","MAP","World","World choropleth","Geography & Environment","manual_tz",7,7,6,8,4,8,8,65),
# --- More data-specific deep dives ---
mk("hae016","TSMC PE Ratio Over Time: When Was It Most Overvalued?","The semiconductor king hit 40x earnings in 2021","CHART","World","Line chart","Economy","D:/raw_data/Kaggle/archive (34)/tsm_financial_ratios.csv",5,5,7,7,5,6,7,90),
mk("hae017","TSMC Cash Flow vs Capital Expenditure","The company that spends $30B/year building fabs","CHART","World","Area chart","Economy","D:/raw_data/Kaggle/archive (34)/tsm_cash_flow.csv",5,5,7,7,5,6,7,90),
mk("hae018","Iran War Day-by-Day: Brent Oil Price Tracker","Each military event annotated on the price chart","CHART","World","Line chart","History","D:/raw_data/Kaggle/irankeyevents/iran_war_key_events_timeline.csv",8,7,7,8,9,8,7,90),
mk("hae019","NVIDIA Price-to-Earnings vs TSMC Price-to-Earnings","The AI chip duopoly: who is more expensive?","XREF","World","Line chart","Economy","D:/raw_data/Kaggle/archive (45)/nvda_stock_data_master.csv + D:/raw_data/Kaggle/archive (34)/tsm_financial_ratios.csv",5,5,7,7,5,6,8,80),
mk("hae020","McDonalds Stock: The 25-Year Chart That Beats the S&P","$10K invested in 2000 became $120K by 2026","CHART","US","Line chart","Economy","D:/raw_data/Kaggle/archive (43)/MCD.csv",6,7,7,7,5,6,6,90),
]

ideas2 = [
# --- Section gap fillers ---
mk("hae021","US Counties by Dominant Industry","Agriculture in the Plains, healthcare in the Rust Belt","MAP","US","County choropleth","Labor","bls_qcew",7,7,7,7,5,8,7,60),
mk("hae022","Percentage of Workers in Remote Jobs by State","The post-COVID remote work geography","MAP","US","State choropleth","Labor","census_acs_2023",7,8,7,7,5,7,7,65),
mk("hae023","Electric Vehicle Registration Share by State","California leads at 25% but the gap is closing","MAP","US","State choropleth","Transportation","dot_ev",7,8,7,7,6,7,7,65),
mk("hae024","Internet Speed by Country: The Global Digital Divide","South Korea averages 200 Mbps while Chad gets 2 Mbps","MAP","World","World choropleth","Science & Technology","speedtest_data",7,7,7,7,5,8,6,65),
mk("hae025","Teacher Salary vs Student Performance by State","Paying teachers more doesnt always mean better scores","XREF","US","Scatter plot","Education","nces + D:/raw_data/Sage_Data/Assessment by All Students from the National Assessment of Educational Progress (NAEP) Database.csv",7,8,7,8,6,7,8,70),
mk("hae026","Homelessness Rate vs Median Rent by State","The correlation is stronger than you think","XREF","US","Scatter plot","Housing","hud_pit + zillow",8,8,7,8,7,7,8,60),
mk("hae027","Carbon Emissions per Capita vs GDP per Capita","The environmental cost of getting rich","XREF","World","Scatter plot","Climate","D:/raw_data/Our World In Data/co-emissions-per-capita.csv + D:/raw_data/Kaggle/archive (35)/historysaid-global-economic-dataset/data/core/world_bank.csv",7,7,7,7,7,7,7,75),
mk("hae028","Global Government Effectiveness Over Time","Is governance getting better or worse worldwide?","CHART","World","Line chart","International Statistics","D:/raw_data/Kaggle/archive (35)/historysaid-global-economic-dataset/data/core/world_bank_wgi.csv",6,6,7,7,6,7,7,85),
mk("hae029","Population-Weighted Average Breakfast Price by Continent","Asias 3 billion people average $2.50 for breakfast","CHART","World","Bar chart","Food & Nutrition","D:/raw_data/Kaggle/archive (38)/breakfast basket.csv + D:/raw_data/Kaggle/pop/popolazione-globale-per-paese-1950-2024.csv",6,7,7,7,5,6,7,80),
mk("hae030","The 10 Countries That Added the Most People Since 1950","India added 1.1 billion, China 950 million","RANK","World","Bar chart","Population","D:/raw_data/Kaggle/pop/popolazione-globale-per-paese-1950-2024.csv",7,7,7,7,5,7,6,90),
mk("hae031","Real Exchange Rate vs Inflation: Currency Valuation Explained","Why some currencies stay strong despite high inflation","XREF","World","Scatter plot","Economy","D:/raw_data/Kaggle/archive (35)/historysaid-global-economic-dataset/data/core/bis.csv + imf_weo.csv",5,5,7,7,6,7,7,80),
mk("hae032","Countries Where Government Debt Exceeds 100% of GDP","There are 23 of them and the list keeps growing","MAP","World","World choropleth","Economy","D:/raw_data/Kaggle/archive (35)/historysaid-global-economic-dataset/data/core/imf_weo.csv",6,7,7,7,7,8,6,90),
mk("hae033","Public School Student-Teacher Ratio by State","Which states give students the most individual attention?","MAP","US","State choropleth","Education","D:/raw_data/Public_School_Characteristics_2022-23.csv",6,7,7,6,5,7,6,90),
mk("hae034","Title I Schools as Percentage of All Schools by State","The geography of educational poverty funding","MAP","US","State choropleth","Education","D:/raw_data/Public_School_Characteristics_2022-23.csv",7,7,7,7,6,7,7,90),
mk("hae035","Magnet Schools by State: Where Choice Education Thrives","Some states have hundreds, others have zero","MAP","US","State choropleth","Education","D:/raw_data/Public_School_Characteristics_2022-23.csv",6,6,7,7,5,7,7,90),
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

print(f"BATCH_HAE: {len(all_ideas)} ideas generated")
print(f"[BATCH_HAE] Injected {len(new)} new ideas (skipped {dupes} dupes)")
