"""BATCH_GO: Mega cross-reference batch.
Combines datasets from ALL sources against each other for correlation,
contrast, and pattern ideas.
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

# ============================================================
# CRIME x ECONOMY cross-refs
# ============================================================
ideas.append(mk("go001","Do Richer States Have Less Crime?","FBI crime rates vs real personal income by state","XREF","US-State","Bivariate choropleth","Crime and Law Enforcement","D:/raw_data/fbi/estimated_crimes_1979_2024.csv + D:/raw_data/Sage_Data/Real Personal Income",82,85,72,75,78,82,72,85))
ideas.append(mk("go002","Hate Crimes Track Income Inequality - Heres the Proof","FiveThirtyEight hate crime data vs Gini coefficient by state","XREF","US-State","Bivariate choropleth","Crime and Law Enforcement","D:/raw_data/fivethirtyeight/hate_crimes.csv + Kaggle inequality",85,78,70,78,85,82,75,85))
ideas.append(mk("go003","Prison Rates vs GDP: The Wealth-Incarceration Paradox","Countries with higher GDP dont always have fewer prisoners","XREF","World","Bivariate choropleth","Crime and Law Enforcement","OWID prison-population-rate + world_bank GDP",80,75,70,80,78,82,78,82))
ideas.append(mk("go004","Homicide and Inequality: The Global Correlation","Countries with higher Gini coefficients have more murders","XREF","World","Bivariate choropleth","Crime and Law Enforcement","OWID homicide-rate + Kaggle inequality",85,78,68,78,85,82,78,82))

# ============================================================
# HEALTH x ECONOMY cross-refs
# ============================================================
ideas.append(mk("go005","Life Expectancy vs GDP: The Curve That Flattens","More money helps lifespan - but only up to a point","XREF","World","Scatter plot","Health","OWID life-expectancy + world_bank GDP",78,80,78,72,68,78,65,88))
ideas.append(mk("go006","Drug Use vs Income: Do Rich States Get Higher?","Marijuana usage rates vs median income by state","XREF","US-State","Bivariate choropleth","Health","Sage_Data marijuana + personal income",72,82,72,75,65,78,72,85))
ideas.append(mk("go007","Mental Health Risk vs Internet Access by Country","Do more connected countries report more mental health issues?","XREF","World","Bivariate choropleth","Health","Kaggle mental health + OWID internet access",78,78,68,80,72,80,82,78))
ideas.append(mk("go008","Vaccination Rates vs Child Mortality: The Lifesaving Map","Countries with higher vaccination coverage have dramatically lower child death rates","XREF","World","Bivariate choropleth","Health","OWID vaccination + child-mortality",82,78,75,65,75,82,62,85))
ideas.append(mk("go009","ICU Beds vs COVID Death Rates: Were We Prepared?","Metro areas with fewer ICU beds per capita vs pandemic mortality","XREF","US-Metro","Bivariate choropleth","Health","fivethirtyeight icu-beds + COVID data",82,85,72,75,82,78,72,78))

# ============================================================
# EDUCATION x ECONOMY cross-refs
# ============================================================
ideas.append(mk("go010","NAEP Scores vs State Spending: Does Money Buy Education?","State education test scores vs per-pupil spending","XREF","US-State","Bivariate choropleth","Education","Sage_Data NAEP + education spending",75,85,75,72,70,80,70,85))
ideas.append(mk("go011","College Major vs Unemployment: The Degree Payoff Map","Which degrees lead to jobs and which leave you jobless","XREF","US","Scatter plot","Education","fivethirtyeight recent-grads earnings vs unemployment",72,90,80,68,68,75,62,92))
ideas.append(mk("go012","Literacy Rate vs GDP Per Capita: Education Drives Wealth","Cross-country comparison of reading rates and economic output","XREF","World","Bivariate choropleth","Education","OWID literacy + world_bank GDP per capita",72,75,78,65,62,80,62,85))
ideas.append(mk("go013","Title I Schools vs Crime: The Poverty-Crime Nexus","Mapping poverty schools alongside crime rates by county","XREF","US-County","Bivariate choropleth","Education","Public_School_Characteristics + FBI crime",82,80,68,72,82,82,75,78))

# ============================================================
# DEMOGRAPHICS x ENVIRONMENT cross-refs
# ============================================================
ideas.append(mk("go014","Population Growth vs CO2: Who Bears the Climate Burden?","Fast-growing populations vs per-capita emissions by country","XREF","World","Bivariate choropleth","Climate","OWID population-growth + co2-per-capita",80,75,72,78,80,82,75,85))
ideas.append(mk("go015","Sea Level Rise vs Property Values: Coastal Risk Assessment","Groundwater vulnerability areas overlaid with housing price data","XREF","US","Dot map","Climate","GIS_Data groundwater + housing data",85,82,72,78,88,82,80,78))
ideas.append(mk("go016","Walkability Index vs Obesity Rates by Metro Area","Do more walkable places have healthier populations?","XREF","US","Bivariate choropleth","Health","WalkabilityIndex + CDC obesity data",78,88,75,72,62,80,72,82))
ideas.append(mk("go017","Urbanization vs Fertility: City Life Kills Birth Rates","Urban population share vs children per woman by country","XREF","World","Bivariate choropleth","Demographics","HSUS urban-rural + OWID fertility",75,78,75,72,72,80,70,82))

# ============================================================
# TRANSPORTATION x DEMOGRAPHICS cross-refs
# ============================================================
ideas.append(mk("go018","Bad Drivers vs Car Ownership: More Cars = More Crashes?","Vehicles per capita vs fatal accident rates by state","XREF","US-State","Bivariate choropleth","Transportation","Sage_Data vehicles + fivethirtyeight bad-drivers",72,82,75,72,68,80,68,88))
ideas.append(mk("go019","Transit Deserts vs Poverty: Who Gets Left Behind in Boston","MBTA coverage gaps overlaid with income and minority population data","XREF","US-City","Dot map","Transportation","MBTA shapefiles + Census demographics",82,82,72,72,80,85,78,82))
ideas.append(mk("go020","Airline Safety vs Ticket Prices: Do You Get What You Pay For?","Safety records vs average fare by airline","XREF","World","Scatter plot","Transportation","fivethirtyeight airline-safety + fare data",68,82,75,72,65,70,72,78))

# ============================================================
# RELIGION x POLITICS x DEMOGRAPHICS cross-refs
# ============================================================
ideas.append(mk("go021","The Religion-Divorce Paradox: Bible Belt Has Highest Divorce","Religious adherent rates vs divorce rates by state","XREF","US-State","Bivariate choropleth","Demographics","Sage_Data religion + fivethirtyeight divorce",82,85,72,85,72,80,82,85))
ideas.append(mk("go022","Cousin Marriage Laws vs Religious Adherence by State","Do more religious states allow or ban cousin marriage?","XREF","US-State","Bivariate choropleth","Demographics","fivethirtyeight cousin-marriage + Sage_Data religion",68,72,70,80,60,78,82,88))
ideas.append(mk("go023","Democracy vs Development: The Political Regime Scorecard","Political freedom index vs Human Development Index by country","XREF","World","Bivariate choropleth","International Statistics","OWID political-regime + human-development-index",75,72,72,72,75,82,70,88))
ideas.append(mk("go024","Election Denial vs Education Levels by Congressional District","2020 election denier representatives vs district education attainment","XREF","US-State","Bivariate choropleth","Elections","fivethirtyeight election_deniers + Census education",80,78,68,78,82,78,78,78))

# ============================================================
# IMMIGRATION x ECONOMY cross-refs
# ============================================================
ideas.append(mk("go025","Immigration Waves vs Economic Booms: 200 Years of Correlation","Historical immigration flows aligned with GDP growth periods","XREF","US","Line chart","Demographics","HSUS nativity + GDP historical data",75,78,72,72,70,75,75,78))
ideas.append(mk("go026","Asylum Backlogs vs Border Apprehensions: The Overwhelm Map","Asylum case volumes vs border enforcement data over time","XREF","US","Line chart","Demographics","Kaggle asylum + GIS_Data border control",78,72,68,70,80,72,70,82))
ideas.append(mk("go027","Where Immigrants Settle vs Where Jobs Are","Foreign-born population distribution vs employment growth by state","XREF","US-State","Bivariate choropleth","Demographics","GIS_Data foreign-born + BLS employment",72,78,72,68,65,80,68,82))
ideas.append(mk("go028","Detention Length vs Source Country: Who Waits Longest?","Immigration detention stays by nationality reveal disparities","XREF","US","Bar chart","Demographics","Kaggle detention + asylum source data",78,70,68,72,80,68,72,82))

# ============================================================
# HISTORICAL cross-refs
# ============================================================
ideas.append(mk("go029","Slave Population vs Modern Black Population by State","1860 slave census vs 2020 Black population by state - legacies persist","XREF","US-State","Bivariate choropleth","History","HSUS slave pop + Census 2020",90,82,70,78,90,85,80,82))
ideas.append(mk("go030","200 Years of Urbanization vs 200 Years of GDP Growth","U.S. rural-to-urban shift aligned with economic growth","XREF","US","Line chart","History","HSUS urban-rural + GDP historical",72,75,75,68,65,75,68,78))
ideas.append(mk("go031","Antiquities Act Monuments vs Modern Land Values","Presidential national monuments overlaid with current property values","XREF","US","Dot map","History","fivethirtyeight antiquities + property data",68,65,68,72,65,80,78,72))

# ============================================================
# SPORTS x DEMOGRAPHICS x ECONOMY cross-refs
# ============================================================
ideas.append(mk("go032","World Cup Performance vs GDP: Can You Buy Football Success?","FIFA ranking vs GDP per capita by country","XREF","World","Bivariate choropleth","Sports & Recreation","worldcup FIFA + world_bank GDP",68,78,72,72,58,80,72,85))
ideas.append(mk("go033","Football Talent Production vs Population Size","Players per capita vs total population by country","XREF","World","Bivariate choropleth","Sports & Recreation","Kaggle player profiles + OWID population",65,72,72,72,55,80,72,85))
ideas.append(mk("go034","Drinks Map vs Football Culture: Beer Nations Play Different","Alcohol consumption patterns vs World Cup viewership and performance","XREF","World","Bivariate choropleth","Entertainment","fivethirtyeight drinks + FIFA audience",65,75,68,78,52,78,80,82))

# ============================================================
# FOOD x ECONOMICS x HEALTH cross-refs
# ============================================================
ideas.append(mk("go035","Caloric Intake vs Obesity: The Overfed World Map","Daily calories per capita vs obesity rates by country","XREF","World","Bivariate choropleth","Food & Nutrition","OWID caloric-supply + WHO obesity",78,82,75,68,68,80,65,82))
ideas.append(mk("go036","Meat Consumption vs Heart Disease by Country","Animals slaughtered per capita vs cardiovascular death rates","XREF","World","Bivariate choropleth","Health","Kaggle animals-slaughtered + OWID cause-of-death",78,78,72,75,72,80,75,78))
ideas.append(mk("go037","Fuel Prices vs CPI: Gas Drives Everything","Historical fuel prices aligned with consumer price inflation","XREF","US","Line chart","Economy","Kaggle fuel prices + CPI historical",72,85,78,68,70,72,60,92))
ideas.append(mk("go038","Candy Preferences vs Diabetes Rates by State","Halloween candy rankings vs state diabetes prevalence","XREF","US-State","Bivariate choropleth","Health","fivethirtyeight candy + CDC diabetes data",68,80,68,78,60,75,80,72))

# ============================================================
# TECHNOLOGY x SOCIETY cross-refs
# ============================================================
ideas.append(mk("go039","Internet Access vs Democracy Score by Country","Do connected populations demand more political freedom?","XREF","World","Bivariate choropleth","Science & Technology","OWID internet + political-regime",75,72,68,78,75,82,78,85))
ideas.append(mk("go040","Space Launches vs Military Spending: The Dual-Use Rocket","Countries that launch the most objects also spend the most on defense","XREF","World","Bivariate choropleth","Science & Technology","OWID space-launches + military-spending",70,68,68,75,72,80,78,85))
ideas.append(mk("go041","R&D Spending vs Patent Output by Country","Does research spending translate to innovation output?","XREF","World","Bivariate choropleth","Science & Technology","OWID research-spending + patent data",68,68,72,72,62,78,72,82))
ideas.append(mk("go042","Apple Stock Price vs iPhone Sales by Country","AAPL market cap growth aligned with smartphone adoption rates","XREF","World","Line chart","Economy","Kaggle apple stock + OWID internet access",65,72,72,68,60,72,68,82))

# ============================================================
# CLIMATE x ECONOMY x ENERGY cross-refs
# ============================================================
ideas.append(mk("go043","Energy Consumption vs CO2 vs GDP: The Triple Bind","Per-capita energy use, emissions, and economic output by country","XREF","World","Bivariate choropleth","Climate","OWID energy + co2 + world_bank GDP",78,72,68,72,78,80,72,82))
ideas.append(mk("go044","Temperature Change vs Agricultural Employment","Countries warming fastest vs share of workforce in agriculture","XREF","World","Bivariate choropleth","Climate","Kaggle temperature + OWID agriculture employment",78,72,68,78,80,80,80,78))
ideas.append(mk("go045","Electricity Access vs CO2 Per Capita: The Development Dilemma","Expanding electricity access increases emissions - whos paying the price?","XREF","World","Bivariate choropleth","Climate","OWID electricity-access + co2-per-capita",78,72,70,75,78,82,75,85))

# ============================================================
# MEGA 3+ DATASET COMBOS
# ============================================================
ideas.append(mk("go046","The American Paradox: Rich, Religious, and Divorced","Income + religious adherence + divorce rates by state reveal contradictions","XREF","US-State","State choropleth","Demographics","Sage income + religion + 538 divorce",85,88,72,85,75,78,85,82))
ideas.append(mk("go047","Immigration, Crime, and Employment: Debunking the Myth","Immigrant population share vs crime rates vs unemployment by state","XREF","US-State","State choropleth","Demographics","GIS immigration + FBI crime + BLS employment",85,82,72,78,85,78,78,78))
ideas.append(mk("go048","The Global Human Capital Index","Literacy + schooling + internet access + R&D spending combined index","XREF","World","World choropleth","International Statistics","OWID literacy + schooling + internet + research",72,72,72,65,62,82,72,82))
ideas.append(mk("go049","Slavery to Segregation to Incarceration: 200 Year Pipeline","Historical slave pop + jail racial composition + modern demographics by state","XREF","US-State","State choropleth","History","HSUS slave pop + Sage jail data + Census",92,80,68,82,92,82,85,78))
ideas.append(mk("go050","Birth Rates vs Wealth vs Education: Why the World Stopped Having Babies","Fertility + GDP per capita + female education rates by country","XREF","World","Bivariate choropleth","Demographics","OWID fertility + GDP + schooling",82,82,75,78,78,80,72,85))
ideas.append(mk("go051","The Complete Country Scorecard: 12 Metrics for Every Nation","HDI + GDP + Democracy + Crime + Health + Education + Climate + Military in one viz","XREF","World","World choropleth","International Statistics","OWID + world_bank + Kaggle combined",72,75,72,65,60,85,70,78))
ideas.append(mk("go052","Americas Transit Inequality: Walkability + Transit + Income","Walkability index + MBTA coverage + income levels mapped together","XREF","US-City","Dot map","Transportation","WalkabilityIndex + MBTA + Census income",78,82,72,72,75,85,78,78))
ideas.append(mk("go053","The Climate Justice Map: Who Pollutes vs Who Suffers","CO2 emissions + sea level rise vulnerability + GDP per capita","XREF","World","Bivariate choropleth","Climate","OWID co2 + GIS_Data groundwater + GDP",88,78,68,80,88,82,82,78))
ideas.append(mk("go054","Modern Slavery vs GDP vs Governance Quality","Slavery prevalence + economic development + corruption index by country","XREF","World","Bivariate choropleth","International Statistics","Kaggle modern slavery + GDP + WGI governance",88,75,68,80,88,80,78,78))
ideas.append(mk("go055","The Full Stack: Crime + Poverty + Education + Health by U.S. County","FBI crime + Title I schools + life expectancy + income in one visualization","XREF","US-County","County choropleth","Demographics","FBI + schools + OWID + Sage combined",82,85,68,72,80,85,72,72))

print(f"BATCH_GO: {len(ideas)} ideas generated")

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
    print("[BATCH_GO] ERROR: tail marker not found in data.js")
    sys.exit(1)

raw = raw.replace(tail, "")
for idea in new_ideas:
    raw += idea + ",\n"
raw += tail + "\n"

with open(DATA_JS, "w", encoding="utf-8") as f:
    f.write(raw)

print(f"[BATCH_GO] Injected {len(new_ideas)} new ideas (skipped {skipped} dupes)")
