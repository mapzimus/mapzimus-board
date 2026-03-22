"""BATCH_GY: Final exhaustive round. Remaining untapped angles,
election deniers deep-cut, divorce data specifics, and more
creative cross-refs using actual columns.
"""
import re, sys
DATA_JS = r"D:\projects\mapzimus-board\data.js"

def mk(id,title,sub,typ,geo,fmt,sect,tbl,e,r,c,s,t,v,o,dr):
    raw=e*2+r*2+c*1.25+s*1.5+t*1.5+v*2.0+o*1.5
    vs=int((raw/11.75)*(1-0.5*(1-dr/100)))
    return ('{id:"'+id+'",title:"'+title+'",sub:"'+sub+'",type:"'+typ+'",'
            'geo:"'+geo+'",fmt:"'+fmt+'",section:"'+sect+'",tbl:"'+tbl+'",'
            'sc:{emotional:'+str(e)+',relatability:'+str(r)+',clarity:'+str(c)
            +',surprise:'+str(s)+',tension:'+str(t)+',visual:'+str(v)
            +',originality:'+str(o)+',data_ready:'+str(dr)+'}'
            ',vs:'+str(vs)+',topics:[],ext:[],status:"idea",notes:""}')

ideas = []

# === ELECTION DENIERS SPECIFICS ===
ideas.append(mk("gy001","The Election Denier Map: Fully Denied vs Raised Questions","Granular stance breakdown of election deniers in Congress by state","MAP","US-State","State choropleth","Elections","D:/raw_data/fivethirtyeight/election_deniers col:Stance",80,78,72,72,82,78,65,95))
ideas.append(mk("gy002","Senate vs House: Election Denial by Chamber","How election denial concentrated differently in Senate vs House races","CHART","US","Bar chart","Elections","D:/raw_data/fivethirtyeight/election_deniers col:Office",75,72,72,72,78,70,65,95))
ideas.append(mk("gy003","Incumbent Election Deniers: Who Got Re-Elected?","Sitting members who denied the 2020 election and still won re-election","MAP","US-State","State choropleth","Elections","D:/raw_data/fivethirtyeight/election_deniers cols:Incumbent+Stance",78,75,72,72,80,78,68,92))

# === DIVORCE DATA: EDUCATION-SPECIFIC ===
ideas.append(mk("gy004","The Education-Divorce Gradient: College Grads Divorce Less","Divorce rates by education level showing the graduate degree advantage","CHART","US","Line chart","Demographics","D:/raw_data/fivethirtyeight/divorce cols:HS+SC+BA+GD",78,85,78,72,68,72,65,95))
ideas.append(mk("gy005","Rich, Poor, and Marriage: Divorce Rates by Income Class","How wealth brackets affect likelihood of divorce over 60 years","CHART","US","Line chart","Demographics","D:/raw_data/fivethirtyeight/divorce cols:poor+mid+rich",78,88,78,72,68,72,62,95))
ideas.append(mk("gy006","The Age of Divorce: 35-44 vs 45-54 Year Olds","Which age group divorces more and how the gap has changed","CHART","US","Line chart","Demographics","D:/raw_data/fivethirtyeight/divorce cols:3544+4554",72,82,75,68,65,72,62,95))

# === BIOPICS: SPECIFIC ANALYSES ===
ideas.append(mk("gy007","Who Hollywood Thinks Is Worth a Biopic: Subject Type Breakdown","Criminal, musician, athlete, politician - which type gets the most films?","CHART","World","Bar chart","Entertainment","D:/raw_data/fivethirtyeight/biopics col:type_of_subject",65,72,72,72,58,70,72,92))
ideas.append(mk("gy008","The Race of Biopic Subjects: Hollywoods Diversity Problem","Person of color representation in biographical films over decades","CHART","US","Line chart","Entertainment","D:/raw_data/fivethirtyeight/biopics cols:person_of_color+year",78,72,68,72,75,70,72,92))
ideas.append(mk("gy009","Male vs Female Biopic Subjects: The Gender Gap in Film","Women represent a small fraction of biographical film subjects","CHART","World","Bar chart","Entertainment","D:/raw_data/fivethirtyeight/biopics col:subject_sex",75,72,72,72,72,70,68,92))

# === POLITICAL REGIME: TEMPORAL ===
ideas.append(mk("gy010","237 Years of Political Regimes: From 1789 to 2025","Every country's regime type animated year by year from the French Revolution","MAP","World","Animated choropleth","History","D:/raw_data/Our World In Data/political-regime 1789-2025",80,72,72,72,78,88,72,92))
ideas.append(mk("gy011","The Third Wave: Democracies Gained and Lost Since 1975","Huntingtons third wave of democratization tracked in data","CHART","World","Line chart","International Statistics","D:/raw_data/Our World In Data/political-regime 1975-2025",75,72,72,72,72,75,72,88))

# === WOMEN IN STEM: SPECIFIC ===
ideas.append(mk("gy012","Computer Science: The Gender Reversal","Women were 37% of CS grads in 1985 but only 18% now - what happened?","CHART","US","Line chart","Education","D:/raw_data/fivethirtyeight/women-stem + historical",82,82,72,82,75,72,75,88))
ideas.append(mk("gy013","The STEM Pay Penalty for Women: Median Earnings by Gender","Male vs female median earnings for the same STEM major","CHART","US","Bar chart","Education","D:/raw_data/fivethirtyeight/women-stem col:Median+ShareWomen",78,82,75,72,78,72,65,92))

# === MORE CROSS-REFS: COLUMN-SPECIFIC ===
ideas.append(mk("gy014","Speeding Deaths vs Insurance Premiums: Do States Learn?","States with high speeding fatalities vs their insurance premium rates","XREF","US-State","Scatter plot","Transportation","bad-drivers cols:speeding+premiums",68,82,75,72,62,75,65,95))
ideas.append(mk("gy015","Non-Citizen Share vs Hate Crimes: Testing the Narrative","FiveThirtyEight data: immigrant population share vs hate crime rates","XREF","US-State","Scatter plot","Demographics","hate_crimes cols:share_non_citizen+hatecrimes",80,75,68,78,82,75,75,95))
ideas.append(mk("gy016","Education Level vs Hate Crimes: Does Schooling Reduce Bigotry?","High school degree share vs hate crime rate by state","XREF","US-State","Scatter plot","Education","hate_crimes cols:hs_degree+hatecrimes",72,78,72,72,68,75,68,95))
ideas.append(mk("gy017","White Poverty vs Total Hate Crimes by State","Share of white population in poverty vs hate crime rates","XREF","US-State","Scatter plot","Crime and Law Enforcement","hate_crimes cols:white_poverty+hatecrimes",78,72,68,78,78,75,72,95))
ideas.append(mk("gy018","Cocaine vs Hallucinogen Use by Age: Different Curves","Cocaine use peaks in 20s while hallucinogen use spans wider range","CHART","US","Line chart","Health","drug-use cols:cocaine+hallucinogen by age",68,72,72,72,65,72,68,95))

# === COMBINED LOCAL DATA DEEP XREFS ===
ideas.append(mk("gy019","Bad Drivers + Hate Crimes + Divorce: States That Have It All","Triple-threat states that rank poorly on driving, hate, and divorce","XREF","US-State","State choropleth","Demographics","fivethirtyeight bad-drivers+hate_crimes+divorce",72,82,68,82,68,78,82,88))
ideas.append(mk("gy020","College Major Gender Gap vs Drug Use by Age: Cultural Shifts","How changing career patterns align with shifting substance use","XREF","US","Line chart","Education","recent-grads ShareWomen + drug-use trends",65,72,65,75,62,72,78,82))
ideas.append(mk("gy021","FBI Officer Gender Ratios vs State Political Lean","States with more female police officers vs political partisanship","XREF","US-State","Scatter plot","Crime and Law Enforcement","FBI lee officers + election data",68,68,68,75,65,75,78,82))
ideas.append(mk("gy022","Airline Fatalities Then vs Now: Before and After 2000","Comparing airline safety records 1985-1999 vs 2000-2014","CHART","World","Bar chart","Transportation","airline-safety cols:85_99+00_14",72,78,78,68,62,72,60,95))
ideas.append(mk("gy023","Available Seat KM vs Safety: Do Bigger Airlines Fly Safer?","Fleet size vs fatal accident rate - scale might matter","XREF","World","Scatter plot","Transportation","airline-safety cols:avail_seat_km+fatalities",65,72,72,72,58,72,68,92))

# === REMAINING MISSING TOPICS / SECTION FILLERS ===
ideas.append(mk("gy024","World Population Density: One Map to Show Everything","People per square km mapped at the subnational level globally","MAP","World","World choropleth","Population","OWID + SEDAC population density",68,75,78,58,55,85,55,85))
ideas.append(mk("gy025","The Global Literacy Timeline: World Literacy Rate 1800-2025","How global literacy went from 12% to 87% in 225 years","CHART","World","Line chart","Education","OWID literacy historical data",72,75,78,68,62,72,62,85))
ideas.append(mk("gy026","Americas Most Isolated Communities","Towns farthest from any city of 50,000+ people mapped","MAP","US","Dot map","Demographics","Census + geographic distance",72,78,72,72,62,82,72,78))
ideas.append(mk("gy027","The Global Clean Energy Race: Solar and Wind Capacity by Country","Renewable energy installed capacity mapped worldwide","MAP","World","World choropleth","Climate","IRENA renewable energy data",72,72,78,68,65,82,62,85))
ideas.append(mk("gy028","Americas Food Stamp Map: SNAP Recipients by County","Supplemental Nutrition Assistance Program participation rates","MAP","US-County","County choropleth","Economy","USDA SNAP data",80,85,72,65,78,82,55,85))
ideas.append(mk("gy029","The Worlds Deadliest Roads: Traffic Deaths by Country","Road traffic fatalities per 100k people mapped globally","MAP","World","World choropleth","Transportation","WHO road safety data",78,78,75,68,78,80,58,85))
ideas.append(mk("gy030","Americas Electric Grid Vulnerability: Outage-Prone Areas","Power outage frequency and duration mapped at the county level","MAP","US-County","County choropleth","Science & Technology","EIA power outage data",75,82,72,68,72,82,65,78))
ideas.append(mk("gy031","The Global Debt Map: Government Debt as % of GDP","Which countries are drowning in debt and which are fiscally sound","MAP","World","World choropleth","Economy","IMF WEO col:GGXWDG_NGDP",72,72,75,68,72,80,58,88))
ideas.append(mk("gy032","Americas Childless Counties: Where Birth Rates Are Below Replacement","Counties with crude birth rates below 10 per 1,000","MAP","US-County","County choropleth","Demographics","CDC vital statistics data",78,78,72,72,75,82,68,82))
ideas.append(mk("gy033","The Nuclear Test Map: Every Nuclear Detonation Since 1945","2,056 nuclear tests mapped by location, yield, and country","MAP","World","Dot map","History","CTBTO nuclear test data",78,68,72,78,78,85,75,85))
ideas.append(mk("gy034","Americas Prison Gerrymandering Problem","Inmates counted in prison locations vs home districts distorts representation","MAP","US","Dot map","Elections","Census prisoner reallocation data",78,72,68,78,78,82,78,78))
ideas.append(mk("gy035","The World Map of Average Working Hours","Annual hours worked per worker by country - some work twice as much","MAP","World","World choropleth","Labor","OECD working hours data",72,85,78,72,65,80,62,85))

print(f"BATCH_GY: {len(ideas)} ideas generated")

# === INJECTION LOGIC ===
with open(DATA_JS, encoding="utf-8") as f:
    raw = f.read()
existing_ids = set(re.findall(r'id:"([^"]+)"', raw))
new_ideas = []
skipped = 0
for idea in ideas:
    m = re.search(r'id:"([^"]+)"', idea)
    if m and m.group(1) not in existing_ids:
        new_ideas.append(idea)
    else:
        skipped += 1
tail = "]; // end D"
if tail not in raw:
    print("[BATCH_GY] ERROR: tail marker not found"); sys.exit(1)
raw = raw.replace(tail, "")
for idea in new_ideas:
    raw += idea + ",\n"
raw += tail + "\n"
with open(DATA_JS, "w", encoding="utf-8") as f:
    f.write(raw)
print(f"[BATCH_GY] Injected {len(new_ideas)} new ideas (skipped {skipped} dupes)")
