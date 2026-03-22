"""BATCH_GT: Hyper-specific data stories + county-level deep dives +
city comparisons + more niche viral map ideas.
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

# === COUNTY-LEVEL DEEP DIVES ===
ideas.append(mk("gt001","Americas Fastest Shrinking Counties","Counties losing 10%+ of population per decade mapped","MAP","US-County","County choropleth","Demographics","Census population change",82,78,72,72,78,82,68,85))
ideas.append(mk("gt002","The County Cancer Map: Where Cancer Rates Are Highest","Age-adjusted cancer incidence rates by county","MAP","US-County","County choropleth","Health","NCI SEER cancer data",82,82,72,68,80,82,62,85))
ideas.append(mk("gt003","Americas Heart Attack Belt: Cardiovascular Death by County","Heart disease mortality at the county level","MAP","US-County","County choropleth","Health","CDC WONDER heart disease",80,82,72,68,78,82,58,85))
ideas.append(mk("gt004","Where Nobody Has a College Degree: Education Desert Counties","Counties with less than 15% bachelors degree attainment","MAP","US-County","County choropleth","Education","Census ACS education",78,78,75,72,72,82,65,88))
ideas.append(mk("gt005","The Median Age Map: Americas Youngest and Oldest Counties","County-level median age showing generational geography","MAP","US-County","County choropleth","Demographics","Census ACS age data",68,78,78,68,58,82,60,88))
ideas.append(mk("gt006","Americas Most Diverse Counties vs Most Homogeneous","Racial diversity index mapped at the county level","MAP","US-County","County choropleth","Demographics","Census ACS race data",72,78,75,68,65,82,62,88))
ideas.append(mk("gt007","Child Poverty by County: Where Kids Grow Up Poor","Percentage of children living below the poverty line by county","MAP","US-County","County choropleth","Economy","Census ACS child poverty",88,82,72,68,85,82,60,85))
ideas.append(mk("gt008","Americas Veterans Map: Where Military Service Is a Way of Life","Veteran population as share of total population by county","MAP","US-County","County choropleth","Demographics","Census ACS veteran status",68,72,75,65,62,82,62,85))
ideas.append(mk("gt009","The Commute Map: Average Drive Time by County","Mean travel time to work at the county level","MAP","US-County","County choropleth","Transportation","Census ACS commuting",70,88,78,62,58,82,55,88))
ideas.append(mk("gt010","Americas Most Unequal Counties: Gini Coefficient Map","Income inequality measured at the county level","MAP","US-County","County choropleth","Economy","Census ACS Gini index",78,78,72,72,78,82,65,85))

# === CITY-LEVEL COMPARISONS ===
ideas.append(mk("gt011","Americas 25 Biggest Cities: How They Compare on 10 Metrics","Population, crime, income, education, transit side by side","RANK","US-City","Bar chart","Demographics","Census + FBI + ACS combined",68,85,78,62,58,78,58,85))
ideas.append(mk("gt012","Gentrification in Real Time: Americas Changing Neighborhoods","Census tracts that flipped from low to high income 2010-2023","MAP","US-City","Dot map","Housing","Census ACS tract-level income",82,85,72,72,78,82,72,82))
ideas.append(mk("gt013","The Segregation Index: Americas Most and Least Integrated Cities","Residential segregation measured by the dissimilarity index","RANK","US-City","Bar chart","Demographics","Census ACS block-level data",82,78,72,72,82,78,72,82))
ideas.append(mk("gt014","Crime Rates in Americas 50 Largest Cities: Ranked","Violent and property crime per 100k for major cities","RANK","US-City","Bar chart","Crime and Law Enforcement","FBI UCR city data",78,85,78,68,78,75,55,88))

# === WORLD COMPARISON MAPS ===
ideas.append(mk("gt015","The Age of Consent Around the World","Legal age of consent mapped by country - ranges from 12 to 21","MAP","World","World choropleth","International Statistics","legal age data",72,78,72,78,68,80,72,82))
ideas.append(mk("gt016","Countries by Alcohol Drinking Age (or Lack Thereof)","Legal drinking age by country - some have none at all","MAP","World","World choropleth","International Statistics","drinking age data",62,82,78,72,52,80,65,88))
ideas.append(mk("gt017","Mandatory Military Service: Countries That Still Draft","Nations requiring compulsory military service mapped","MAP","World","World choropleth","International Statistics","conscription data",68,72,75,72,68,80,68,85))
ideas.append(mk("gt018","The Death Penalty World Map: Who Still Executes?","Countries that retain, have abolished, or have moratorium on death penalty","MAP","World","World choropleth","International Statistics","Amnesty International data",78,72,72,68,82,80,62,88))
ideas.append(mk("gt019","Paid Maternity Leave by Country: America Stands Alone","Weeks of paid maternity leave - the U.S. is the only developed nation with zero","MAP","World","World choropleth","International Statistics","ILO maternity leave data",85,85,78,80,82,80,62,88))
ideas.append(mk("gt020","Universal Healthcare Map: Countries With vs Without","Which countries provide universal health coverage to citizens","MAP","World","World choropleth","Health","WHO healthcare coverage data",80,85,78,68,78,80,58,88))
ideas.append(mk("gt021","Corruption Perception Index: The World Map of Graft","Transparency International corruption scores by country","MAP","World","World choropleth","International Statistics","TI CPI data",75,72,75,68,78,82,62,88))
ideas.append(mk("gt022","The Gender Gap Index: Best and Worst Countries for Women","World Economic Forum gender gap scores mapped globally","MAP","World","World choropleth","International Statistics","WEF gender gap data",78,78,75,68,78,80,62,88))
ideas.append(mk("gt023","Countries with the Most Refugees and Displaced People","Refugee population by country of asylum and origin","MAP","World","World choropleth","International Statistics","UNHCR refugee data",85,78,72,68,85,80,62,88))

# === U.S. ECONOMIC / PERSONAL FINANCE VIRAL ===
ideas.append(mk("gt024","The Salary You Need to Buy a Home in Each State","Required household income to afford median home with 20% down","MAP","US-State","State choropleth","Housing","Census home values + income data",78,92,80,72,72,78,62,85))
ideas.append(mk("gt025","Americas Most Expensive Zip Codes","Top 100 zip codes by median home value mapped","MAP","US","Dot map","Housing","Zillow home value data",70,85,78,72,58,82,62,82))
ideas.append(mk("gt026","Where Americans Are Moving: Net Migration by State 2020-2025","States gaining and losing residents in the post-pandemic migration wave","MAP","US-State","State choropleth","Demographics","Census migration data",72,88,78,68,65,78,58,88))
ideas.append(mk("gt027","The Student Loan Map: Average Debt by State","Mean student loan balance for borrowers by state","MAP","US-State","State choropleth","Education","Federal Reserve student loan data",78,90,78,68,72,78,58,85))
ideas.append(mk("gt028","Americas Tipped Worker Map: States by Tipped Minimum Wage","Tipped minimum wages from $2.13 to full minimum wage by state","MAP","US-State","State choropleth","Labor","DOL wage data",72,85,78,72,70,78,65,88))

# === ENVIRONMENT / NATURE SPECIFIC ===
ideas.append(mk("gt029","Americas Wildfire Risk Map: Where Burns Are Getting Worse","Wildfire-prone areas and how burn acreage has increased over decades","MAP","US","Dot map","Climate","NIFC wildfire data",82,80,72,72,82,85,65,85))
ideas.append(mk("gt030","The Air Quality Map: Americas Most and Least Polluted Counties","EPA AQI data at the county level","MAP","US-County","County choropleth","Climate","EPA AQI data",78,85,75,68,72,82,58,85))
ideas.append(mk("gt031","Every Active Volcano in the World","1,350+ potentially active volcanoes mapped with eruption history","MAP","World","Dot map","Geography & Environment","Smithsonian GVP data",72,72,72,68,65,88,65,88))
ideas.append(mk("gt032","The Worlds Coral Reefs: Before and After Bleaching","Coral reef locations and bleaching severity over time","MAP","World","Dot map","Climate","NOAA coral reef watch",85,75,68,72,85,88,72,78))
ideas.append(mk("gt033","Americas Water Table: Aquifer Depletion Rates","Major aquifer levels and how fast theyre dropping","MAP","US","Dot map","Climate","USGS groundwater data",82,78,72,75,85,85,72,82))

# === POP CULTURE / FUN DATA ===
ideas.append(mk("gt034","Every State Named After Someone: The Origin Map","Which states are named after people, and who were they","MAP","US-State","State choropleth","History","state name etymology",55,72,72,72,42,78,72,90))
ideas.append(mk("gt035","Americas BBQ Belt: Regional BBQ Styles Mapped","Kansas City, Texas, Carolina, Memphis BBQ regions with signature styles","MAP","US","Special map","Food & Nutrition","regional cuisine data",62,85,72,68,42,82,72,82))
ideas.append(mk("gt036","The Most Misspelled Word in Each State","Google search data reveals what each state struggles to spell","MAP","US-State","State choropleth","Education","Google Trends data",58,85,72,82,42,78,78,78))
ideas.append(mk("gt037","Americas Accent Map: Regional Dialect Boundaries","Linguistic isoglosses showing where accents change across the U.S.","MAP","US","Special map","Demographics","dialect survey data",65,85,72,72,48,85,78,78))
ideas.append(mk("gt038","Every Costco Location in America","900+ Costco warehouses mapped revealing suburban density patterns","MAP","US","Dot map","Economy","Costco location data",58,82,75,65,42,82,62,85))
ideas.append(mk("gt039","The Pizza Map: Styles, Density, and Best-Rated by City","New York, Chicago, Detroit, New Haven - pizza culture geography","MAP","US","Dot map","Food & Nutrition","restaurant + review data",62,88,72,68,42,82,72,78))
ideas.append(mk("gt040","Americas Tallest Buildings by City","Skyscraper heights and density across U.S. metro areas","MAP","US-City","Dot map","Economy","CTBUH building data",55,72,75,62,42,88,62,85))

print(f"BATCH_GT: {len(ideas)} ideas generated")

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
    print("[BATCH_GT] ERROR: tail marker not found"); sys.exit(1)
raw = raw.replace(tail, "")
for idea in new_ideas:
    raw += idea + ",\n"
raw += tail + "\n"
with open(DATA_JS, "w", encoding="utf-8") as f:
    f.write(raw)
print(f"[BATCH_GT] Injected {len(new_ideas)} new ideas (skipped {skipped} dupes)")
