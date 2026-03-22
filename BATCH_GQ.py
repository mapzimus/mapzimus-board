"""BATCH_GQ: ProQuest Statistical Abstract-inspired ideas + more standalone
ideas from underexplored topics and viral formats.
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

# === ProQuest Statistical Abstract Topic Areas ===

# ACCOMMODATION & FOOD SERVICES
ideas.append(mk("gq001","Hotel Room Rates by State: Where Americas Most Expensive to Sleep","Average nightly hotel rates and occupancy rates by state","MAP","US-State","State choropleth","Economy","ProQuest StatAbstract - Accommodation",68,85,78,65,55,78,58,82))
ideas.append(mk("gq002","The Coffee Shop Explosion: Growth of Cafes Per Capita by State","How coffee shops have multiplied across America since 2000","MAP","US-State","State choropleth","Food & Nutrition","ProQuest StatAbstract - Food Services",65,82,75,68,48,75,62,78))
ideas.append(mk("gq003","Casino Hotels: Americas Gambling Geography","Casino hotel revenue and employment by state","MAP","US-State","State choropleth","Entertainment","ProQuest StatAbstract - Casino Hotels",68,78,72,70,62,78,65,80))

# AGRICULTURE
ideas.append(mk("gq004","Americas Farming Footprint: Cropland by County","Agricultural land use mapped at the county level across the U.S.","MAP","US-County","County choropleth","Geography & Environment","ProQuest StatAbstract - Agriculture",62,68,78,58,48,85,58,82))
ideas.append(mk("gq005","What America Grows: Top Crops by State","Leading agricultural products by dollar value for each state","MAP","US-State","State choropleth","Food & Nutrition","ProQuest StatAbstract - Agriculture",65,78,78,62,48,80,60,82))

# BANKING & FINANCE
ideas.append(mk("gq006","Bank Branches Per Capita: The Financial Desert Map","Areas with the fewest bank branches per person - financial deserts","MAP","US-County","County choropleth","Economy","ProQuest StatAbstract - Banking",72,80,72,70,68,78,68,78))
ideas.append(mk("gq007","Average Insurance Premiums by State","Health, auto, and home insurance costs mapped across America","MAP","US-State","State choropleth","Economy","ProQuest StatAbstract - Insurance",72,90,78,65,62,75,55,82))

# BIRTHS, DEATHS, MARRIAGES
ideas.append(mk("gq008","The Marriage Map: Which States Still Say I Do?","Marriage rates per 1,000 population by state - Las Vegas skews Nevada","MAP","US-State","State choropleth","Demographics","ProQuest StatAbstract - Marriages",68,85,78,68,55,75,60,85))
ideas.append(mk("gq009","Americas Opioid Geography: Drug Overdose Deaths by County","Drug overdose mortality rates mapped at the county level","MAP","US-County","County choropleth","Health","ProQuest StatAbstract - Deaths",90,82,72,72,92,82,65,85))
ideas.append(mk("gq010","Teen Birth Rates: The State-Level Divide","Teen pregnancy rates by state showing persistent geographic patterns","MAP","US-State","State choropleth","Health","ProQuest StatAbstract - Births",78,82,72,68,75,78,60,85))

# CONSTRUCTION & HOUSING
ideas.append(mk("gq011","Americas Building Boom: New Housing Permits by Metro Area","Where the most new homes are being built right now","MAP","US-Metro","Dot map","Housing","ProQuest StatAbstract - Construction",68,82,75,62,58,78,58,82))
ideas.append(mk("gq012","Median Home Price by State: The Affordability Crisis Map","State-level median home values showing the coastal premium","MAP","US-State","State choropleth","Housing","ProQuest StatAbstract - Housing",78,92,80,65,75,78,55,88))
ideas.append(mk("gq013","Homeownership Rate by State: The American Dream Map","Which states have the highest and lowest homeownership rates","MAP","US-State","State choropleth","Housing","ProQuest StatAbstract - Housing",72,88,80,62,68,78,55,85))

# EDUCATION
ideas.append(mk("gq014","Teacher Pay vs Student Performance by State","Average teacher salary mapped against standardized test scores","XREF","US-State","Bivariate choropleth","Education","ProQuest StatAbstract - Education",78,85,75,72,72,80,65,82))
ideas.append(mk("gq015","College Enrollment Rates by State: Who Goes to College?","Percentage of 18-24 year olds enrolled in higher education by state","MAP","US-State","State choropleth","Education","ProQuest StatAbstract - Education",70,82,78,62,62,78,55,85))

# ELECTIONS
ideas.append(mk("gq016","Voter Turnout by State: Who Actually Votes?","Percentage of eligible population that voted in the last election by state","MAP","US-State","State choropleth","Elections","ProQuest StatAbstract - Elections",72,82,80,65,68,78,58,88))
ideas.append(mk("gq017","Campaign Contributions by Zip Code: Follow the Money","Where political donations come from mapped at the zip code level","MAP","US","Dot map","Elections","ProQuest StatAbstract - Elections",75,78,72,72,72,82,72,78))

# ENERGY
ideas.append(mk("gq018","Americas Energy Portfolio by State","Electricity generation sources - coal, gas, nuclear, wind, solar - by state","MAP","US-State","State choropleth","Climate","ProQuest StatAbstract - Energy",70,78,78,68,65,82,62,85))
ideas.append(mk("gq019","The Solar Belt vs The Wind Corridor","Renewable energy capacity mapped - where sun and wind power dominate","MAP","US-State","State choropleth","Climate","ProQuest StatAbstract - Energy",72,78,78,68,62,85,68,85))

# FOREIGN COMMERCE
ideas.append(mk("gq020","Americas Top Trading Partners: Import/Export Flows","Trade volumes with each country visualized as flow lines","MAP","World","Flow map","Economy","ProQuest StatAbstract - Foreign Commerce",68,72,75,65,62,82,62,82))
ideas.append(mk("gq021","The Trade Deficit Map: Who America Buys More From Than Sells To","Trade balance by country - red for deficit, green for surplus","MAP","World","World choropleth","Economy","ProQuest StatAbstract - Foreign Commerce",72,72,75,70,72,80,65,82))

# GOVERNMENT
ideas.append(mk("gq022","Federal Spending Per Capita by State: Who Gets the Most?","Federal government expenditure per person mapped by state","MAP","US-State","State choropleth","Economy","ProQuest StatAbstract - Federal Finance",75,82,78,72,72,78,62,85))
ideas.append(mk("gq023","State and Local Tax Burden: Where You Pay the Most","Combined state and local tax rates as share of income by state","MAP","US-State","State choropleth","Economy","ProQuest StatAbstract - State Finance",75,92,80,68,68,78,58,88))

# HEALTH & NUTRITION  
ideas.append(mk("gq024","The Diabetes Belt: Type 2 Prevalence by County","Diabetes rates mapped at the county level showing the Southern cluster","MAP","US-County","County choropleth","Health","ProQuest StatAbstract - Health",80,82,75,68,78,82,58,85))
ideas.append(mk("gq025","Healthcare Spending Per Capita: Which States Spend Most?","Total healthcare expenditure per person by state","MAP","US-State","State choropleth","Health","ProQuest StatAbstract - Health",72,85,78,65,68,78,55,85))
ideas.append(mk("gq026","Food Insecurity by County: Where America Goes Hungry","Percentage of households experiencing food insecurity","MAP","US-County","County choropleth","Food & Nutrition","ProQuest StatAbstract - Nutrition",85,82,72,72,82,82,65,82))

# INCOME & POVERTY
ideas.append(mk("gq027","The Poverty Map: Below the Line by County","Poverty rates mapped at the county level across America","MAP","US-County","County choropleth","Economy","ProQuest StatAbstract - Poverty",82,85,78,68,80,82,55,88))
ideas.append(mk("gq028","Wealth Inequality: Top 1% Share by State","Share of total income held by the top 1% in each state","MAP","US-State","State choropleth","Economy","ProQuest StatAbstract - Wealth",80,82,72,75,82,78,68,82))

# LABOR
ideas.append(mk("gq029","Unemployment by County: Americas Jobless Geography","Unemployment rates at the county level showing regional patterns","MAP","US-County","County choropleth","Labor","ProQuest StatAbstract - Labor",78,88,80,65,72,82,55,90))
ideas.append(mk("gq030","The Gender Pay Gap by State","Womens earnings as percentage of mens earnings mapped by state","MAP","US-State","State choropleth","Labor","ProQuest StatAbstract - Labor",82,85,75,68,80,78,62,85))
ideas.append(mk("gq031","Union Membership by State: The Organized Labor Map","Percentage of workforce in labor unions by state","MAP","US-State","State choropleth","Labor","ProQuest StatAbstract - Labor",70,78,75,68,68,78,65,85))

# LAW ENFORCEMENT
ideas.append(mk("gq032","Police Officers Per Capita by State","Law enforcement staffing levels relative to population","MAP","US-State","State choropleth","Crime and Law Enforcement","ProQuest StatAbstract - Law Enforcement",68,72,78,65,68,75,62,85))

# MANUFACTURING
ideas.append(mk("gq033","Americas Manufacturing Map: Factory Jobs by County","Manufacturing employment concentration at the county level","MAP","US-County","County choropleth","Economy","ProQuest StatAbstract - Manufactures",68,75,75,65,62,80,60,82))

# METRO AREAS
ideas.append(mk("gq034","Americas 50 Fastest-Growing Metro Areas","Population growth rates for MSAs showing Sun Belt dominance","MAP","US-Metro","Dot map","Demographics","ProQuest StatAbstract - Metro Areas",70,82,78,65,62,80,58,85))

# NATIONAL SECURITY
ideas.append(mk("gq035","Veterans Per Capita by State: Where Military Service Is Highest","Share of population with veteran status by state","MAP","US-State","State choropleth","Demographics","ProQuest StatAbstract - Veterans",68,75,75,65,62,78,62,85))

# SCIENCE & TECHNOLOGY
ideas.append(mk("gq036","Patents Filed by State: Americas Innovation Hubs","Patent applications per capita showing where innovation concentrates","MAP","US-State","State choropleth","Science & Technology","ProQuest StatAbstract - Science",68,72,75,70,58,78,68,82))
ideas.append(mk("gq037","Broadband Access by County: The Digital Divide","Percentage of households with broadband internet at the county level","MAP","US-County","County choropleth","Science & Technology","ProQuest StatAbstract - Communications",75,82,78,68,72,80,62,82))

# TRANSPORTATION
ideas.append(mk("gq038","Americas Deadliest Roads: Traffic Fatalities by State","Motor vehicle deaths per 100k population by state","MAP","US-State","State choropleth","Transportation","ProQuest StatAbstract - Transportation",78,85,78,68,78,78,55,88))
ideas.append(mk("gq039","How Americans Get to Work: Commute Mode by Metro Area","Driving, transit, biking, walking, remote work shares by city","MAP","US-Metro","Bar chart","Transportation","ProQuest StatAbstract - Transportation",68,85,78,62,52,78,58,85))

# WHOLESALE & RETAIL
ideas.append(mk("gq040","Retail Sales Per Capita by State: Americas Shopping Map","Total retail sales divided by population for each state","MAP","US-State","State choropleth","Economy","ProQuest StatAbstract - Retail",62,78,78,62,48,75,55,82))

# === MORE VIRAL FORMAT IDEAS ===
ideas.append(mk("gq041","The True Size of Africas Economy in One Map","Africas GDP compared to U.S. states - Texas alone beats most African nations","MAP","World","World choropleth","Economy","world_bank GDP + state GDP",78,78,72,82,68,82,80,85))
ideas.append(mk("gq042","If States Were Countries: GDP Equivalents","Each U.S. state matched to the country with the closest GDP","MAP","US-State","State choropleth","Economy","BEA state GDP + world_bank country GDP",72,82,80,80,58,82,82,88))
ideas.append(mk("gq043","The Population of Earth on One Street","If 8 billion people lived on one street, where would each country be?","CHART","World","Infographic","Population","OWID population data",78,80,75,78,55,82,85,88))
ideas.append(mk("gq044","Every Country Scaled to Population, Not Land Area","Cartogram distorting country sizes by population","MAP","World","Special map","Demographics","OWID population + land area",72,78,72,78,58,88,80,88))
ideas.append(mk("gq045","One Pixel Per Person: World Population Density","Interactive dot density map with one pixel representing one person","MAP","World","Dot map","Population","OWID population + grid data",72,75,72,72,55,90,82,78))

# === THRIFT/EBAY DATA (from your D:\eBay and C:\Users\mhowe\Downloads\thrift.xls) ===
ideas.append(mk("gq046","The Geography of Thrift: Where America Resells","Thrift store and secondhand market density by region","MAP","US-State","State choropleth","Economy","D:/eBay + thrift.xls",65,82,72,68,52,75,68,72))

# === PUBLIC SCHOOL GIS DEEP DIVES ===
ideas.append(mk("gq047","Magnet Schools vs Charter Schools: The Geography of Choice","Where magnet and charter schools concentrate across America","MAP","US","Dot map","Education","D:/raw_data/Public_School_Characteristics_2022-23.csv",68,78,72,65,60,80,68,90))
ideas.append(mk("gq048","Student-Teacher Ratios by State: Class Size Inequality","Average students per teacher mapped showing overcrowded states","MAP","US-State","State choropleth","Education","D:/raw_data/Public_School_Characteristics_2022-23.csv",72,85,78,62,68,75,58,92))
ideas.append(mk("gq049","Rural Schools: How Far Kids Travel to Learn","Distance and accessibility of schools in rural vs urban areas","MAP","US","Dot map","Education","D:/raw_data/Public_School_Characteristics_2022-23.csv",75,78,72,68,65,80,72,88))
ideas.append(mk("gq050","Free and Reduced Lunch: The School Poverty Map","Percentage of students receiving free/reduced lunch by school","MAP","US","Dot map","Education","D:/raw_data/Public_School_Characteristics_2022-23.csv",80,85,75,65,78,80,60,92))

print(f"BATCH_GQ: {len(ideas)} ideas generated")

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
    print("[BATCH_GQ] ERROR: tail marker not found in data.js")
    sys.exit(1)

raw = raw.replace(tail, "")
for idea in new_ideas:
    raw += idea + ",\n"
raw += tail + "\n"

with open(DATA_JS, "w", encoding="utf-8") as f:
    f.write(raw)

print(f"[BATCH_GQ] Injected {len(new_ideas)} new ideas (skipped {skipped} dupes)")
