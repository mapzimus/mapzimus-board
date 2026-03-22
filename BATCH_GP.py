"""BATCH_GP: Deep cross-reference round 2.
More creative, unexpected, and viral-worthy dataset combinations.
Focus on surprising correlations and emotionally resonant contrasts.
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

# === SURPRISING CORRELATIONS ===
ideas.append(mk("gp001","States with the Most Churches Also Have the Most Strip Clubs","Religious congregation density vs adult entertainment per capita by state","XREF","US-State","Bivariate choropleth","Demographics","Sage_Data religion + business data",78,82,72,92,68,78,90,72))
ideas.append(mk("gp002","Countries That Drink the Most Also Live the Longest?","Alcohol consumption vs life expectancy - the French Paradox at global scale","XREF","World","Scatter plot","Health","fivethirtyeight drinks + OWID life-expectancy",72,82,72,88,62,75,85,85))
ideas.append(mk("gp003","More Guns, Less Crime? The State-Level Data","Firearms ownership rates vs violent crime rates by state","XREF","US-State","Bivariate choropleth","Crime and Law Enforcement","gun ownership surveys + FBI crime",82,85,70,80,90,80,72,78))
ideas.append(mk("gp004","Fast Food Density vs Obesity: The Drive-Thru Effect","Fast food restaurants per capita vs obesity rates by state","XREF","US-State","Bivariate choropleth","Health","restaurant data + CDC obesity",78,88,75,72,68,78,68,78))
ideas.append(mk("gp005","Where Coffee Shops Cluster vs Where People Are Happiest","Coffee shop density vs life satisfaction scores by metro area","XREF","US-Metro","Bivariate choropleth","Food & Nutrition","business data + wellbeing surveys",65,82,70,78,52,78,82,72))
ideas.append(mk("gp006","Student Debt vs Birth Rates: Too Broke for Babies","Average student loan burden vs fertility rate by state","XREF","US-State","Bivariate choropleth","Economy","student debt data + vital statistics",88,90,72,78,82,78,82,78))
ideas.append(mk("gp007","Military Spending vs Happiness: Armed but Miserable?","Defense expenditure vs World Happiness Index by country","XREF","World","Scatter plot","International Statistics","OWID military + happiness data",72,72,68,82,72,75,82,82))
ideas.append(mk("gp008","Prison Population vs College Enrollment by State","Inmates per capita vs college students per capita side by side","XREF","US-State","Bivariate choropleth","Education","OWID prison + NCES enrollment",88,82,72,80,88,80,82,78))

# === TEMPORAL / ANIMATED COMBOS ===
ideas.append(mk("gp009","Americas Center of Population: 230 Years of Westward Drift","The geographic center of U.S. population animated from 1790 to today","MAP","US","Dot map","Demographics","HSUS population + Census centers",72,78,78,72,62,88,78,85))
ideas.append(mk("gp010","GDP Growth vs Life Expectancy: The Race Over 50 Years","Animated scatter plot showing countries getting richer AND healthier","XREF","World","Scatter plot","Economy","world_bank GDP + OWID life expectancy",75,78,78,68,65,82,65,88))
ideas.append(mk("gp011","The Great Inversion: Urban vs Rural Population Crossover by State","Animated map showing when each state flipped from rural to urban majority","MAP","US-State","Animated choropleth","Demographics","HSUS urban-rural by state",75,78,72,72,68,85,78,78))
ideas.append(mk("gp012","Crime and Punishment: 45 Years of Crime vs Incarceration","Crime rates fell while prison populations soared - animated divergence","XREF","US","Line chart","Crime and Law Enforcement","FBI crime + OWID prison rates",82,80,75,78,82,78,75,88))

# === GEOGRAPHIC PATTERN IDEAS ===
ideas.append(mk("gp013","The I-95 Corridor: Americas East Coast Megacity by the Numbers","Population density, GDP, crime, traffic along the I-95 spine","MAP","US","Line map","Demographics","Census + BEA + FBI along I-95",72,80,75,68,62,85,75,78))
ideas.append(mk("gp014","The Mississippi River Divide: East vs West in Every Metric","Comparing states east and west of the Mississippi on 10 indicators","MAP","US-State","Bivariate choropleth","Geography & Environment","multiple datasets split by geography",72,78,75,72,65,82,78,78))
ideas.append(mk("gp015","North vs South: The Mason-Dixon Line Still Divides","Every major socioeconomic indicator mapped above and below the line","MAP","US-State","Bivariate choropleth","Demographics","multiple datasets by region",78,82,72,72,72,80,72,78))
ideas.append(mk("gp016","The Rust Belt Recovery Map: Then and Now","Manufacturing employment 1980 vs 2024 in Great Lakes states","MAP","US-State","Bivariate choropleth","Economy","BLS manufacturing + current employment",78,78,72,68,72,80,68,82))
ideas.append(mk("gp017","Coastal vs Inland: Two Americas in Every Stat","50-mile coastal buffer vs interior on income, education, health, politics","XREF","US","Bivariate choropleth","Demographics","Census + geography buffers",75,80,72,75,68,82,78,72))

# === EMOTION-DRIVEN VIRAL COMBOS ===
ideas.append(mk("gp018","The Loneliness Epidemic in One Chart","Time spent alone by age + declining marriage rates + social media growth","XREF","US","Line chart","Demographics","OWID time-with-people + marriage + social data",90,92,78,78,82,75,78,82))
ideas.append(mk("gp019","Every Animal Killed for Food in the Time Youve Been Reading This","Real-time counter of global animal slaughter rates","CHART","World","Infographic","Food & Nutrition","Kaggle animals-slaughtered",85,78,72,82,80,75,80,88))
ideas.append(mk("gp020","Americas Quiet Crisis: Towns That Are Disappearing","Rural towns losing 25%+ of population since 2000","MAP","US-County","County choropleth","Demographics","Census population change",85,82,72,72,82,82,78,82))
ideas.append(mk("gp021","The Cost of Being Born: Hospital Birth Costs by State","Average childbirth costs vs maternal mortality rates","XREF","US-State","Bivariate choropleth","Health","hospital cost data + CDC maternal mortality",88,88,72,78,85,78,72,72))
ideas.append(mk("gp022","How Far a Minimum Wage Hour Gets You at McDonalds Worldwide","Big Mac minutes: time to earn a Big Mac at local minimum wage by country","MAP","World","World choropleth","Economy","minimum wage + Big Mac index",82,92,82,78,72,80,78,78))
ideas.append(mk("gp023","The Water Stress Map: Where Taps Will Run Dry","Groundwater depletion + drought risk + population growth by region","XREF","US","Dot map","Climate","GIS_Data groundwater + drought + population",85,82,72,78,88,82,78,75))

# === CULTURE + DATA COMBOS ===
ideas.append(mk("gp024","Classic Rock Stations vs Median Age by Metro Area","Where classic rock radio thrives aligned with population age","XREF","US-Metro","Dot map","Entertainment","fivethirtyeight classic-rock + Census age",62,78,68,78,48,75,82,72))
ideas.append(mk("gp025","Biopics vs Actual Historical Importance: Whos Overrepresented?","Hollywood biographical film subjects vs encyclopedia significance","XREF","World","Bar chart","Entertainment","fivethirtyeight biopics + historical data",68,72,70,80,60,70,85,78))
ideas.append(mk("gp026","The Spotify vs Economic Stress Map","Music streaming patterns vs unemployment and economic anxiety by country","XREF","World","Bivariate choropleth","Entertainment","Kaggle spotify + economic indicators",68,75,65,78,62,78,82,72))

# === INFRASTRUCTURE + EQUITY ===
ideas.append(mk("gp027","School Quality vs Home Prices: The Zip Code Lottery","NAEP scores and school characteristics vs median home values by district","XREF","US-County","Bivariate choropleth","Education","Sage NAEP + public schools + housing",82,90,72,72,78,82,68,78))
ideas.append(mk("gp028","Airbnb Prices vs Rent Burden: Tourism Displaces Locals","Airbnb nightly rates vs rent-to-income ratio in major cities","XREF","US-City","Bivariate choropleth","Housing","airbnb data + Census rent burden",82,85,72,75,80,78,75,78))
ideas.append(mk("gp029","Every Dollar of CPI Inflation: What You Actually Pay More For","Weighted contribution of each CPI category to total inflation over time","CHART","US","Stacked area chart","Economy","CPI detailed categories",78,90,78,72,72,78,65,92))
ideas.append(mk("gp030","The Car Dependency Score: Transit + Walkability + Sprawl","Combining walkability, transit coverage, and vehicle ownership into one index","XREF","US","Bivariate choropleth","Transportation","WalkabilityIndex + MBTA + vehicles registered",72,85,72,68,62,82,72,78))

# === GLOBAL DEVELOPMENT PARADOXES ===
ideas.append(mk("gp031","Rich Countries Shrink: Population Growth vs Development Level","Developed nations are depopulating while developing nations boom","XREF","World","Bivariate choropleth","Demographics","OWID population-growth-rate-by-level + GDP",78,78,75,72,78,80,68,88))
ideas.append(mk("gp032","The Sanitation Paradox: Clean Water vs Still Dying","Countries with improved sanitation but persistent child mortality","XREF","World","Bivariate choropleth","Health","OWID sanitation + child-mortality",78,72,68,78,75,80,75,82))
ideas.append(mk("gp033","Education vs Autocracy: Literate but Not Free","Countries with high literacy rates under authoritarian regimes","XREF","World","Bivariate choropleth","International Statistics","OWID literacy + political-regime",75,72,70,80,78,80,80,82))
ideas.append(mk("gp034","Agricultural Countries vs Hungry Countries","Share of workforce in agriculture vs prevalence of undernourishment","XREF","World","Bivariate choropleth","Food & Nutrition","OWID agriculture-employment + undernourishment",78,72,70,82,78,80,78,82))
ideas.append(mk("gp035","The Contraception-Prosperity Link","Countries with higher contraceptive prevalence have higher GDP per capita","XREF","World","Scatter plot","Health","OWID contraceptive + world_bank GDP",72,72,70,75,68,75,72,82))

# === U.S. HISTORICAL DEEP DIVES ===
ideas.append(mk("gp036","The Great Migration in Data: Black Population Shift 1910-1970","State-by-state Black population change during the Great Migration","MAP","US-State","Animated choropleth","History","HSUS race data + Census",88,82,72,72,82,85,78,78))
ideas.append(mk("gp037","Americas Population Pyramid Through the Ages","Animated population pyramids from 1790 to 2020 showing demographic transitions","CHART","US","Animated bar chart","Demographics","HSUS age-sex data",72,78,78,68,65,85,72,78))
ideas.append(mk("gp038","When Each State Hit 1 Million People","Timeline map showing population milestones for every U.S. state","MAP","US-State","Animated choropleth","Demographics","HSUS state populations",68,75,75,72,62,82,72,82))
ideas.append(mk("gp039","The Immigrant Wave Pattern: 200 Years of Peaks and Valleys","Foreign-born share of population with annotated historical context","CHART","US","Line chart","Demographics","HSUS nativity + immigration events",75,80,78,72,70,78,68,80))
ideas.append(mk("gp040","Birth and Death Rates: Americas Demographic Transitions","200-year animated view of births and deaths per 1000 population","CHART","US","Line chart","Demographics","HSUS vital statistics",70,75,75,65,65,75,65,80))

print(f"BATCH_GP: {len(ideas)} ideas generated")

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
    print("[BATCH_GP] ERROR: tail marker not found in data.js")
    sys.exit(1)

raw = raw.replace(tail, "")
for idea in new_ideas:
    raw += idea + ",\n"
raw += tail + "\n"

with open(DATA_JS, "w", encoding="utf-8") as f:
    f.write(raw)

print(f"[BATCH_GP] Injected {len(new_ideas)} new ideas (skipped {skipped} dupes)")
