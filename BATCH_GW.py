"""BATCH_GW: Deep-cut data stories + final cross-refs + exhaustive last round.
Filling remaining section gaps and targeting max virality.
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

# === DEEP-CUT CROSS-REFS USING YOUR ACTUAL LOCAL DATA ===
ideas.append(mk("gw001","CPI Inflation vs FBI Crime: Does Inflation Cause Crime?","Consumer price index spikes aligned with crime rate changes over 45 years","XREF","US","Line chart","Crime and Law Enforcement","D:/raw_data/cpi + D:/raw_data/fbi/estimated_crimes",78,78,72,78,78,75,75,88))
ideas.append(mk("gw002","Airbnb Prices vs Walkability: Does Walkability Drive Tourism?","Boston Airbnb nightly rates vs walkability scores by neighborhood","XREF","US-City","Scatter plot","Housing","D:/raw_data/airbnb + WalkabilityIndex",72,78,72,72,58,78,75,78))
ideas.append(mk("gw003","MBTA Transit Access vs School Quality in Greater Boston","Public transit stop density vs school performance metrics","XREF","US-City","Bivariate choropleth","Education","MBTA shapefiles + school data",75,80,72,70,68,82,72,78))
ideas.append(mk("gw004","FBI Hate Crimes vs PPI Economic Stress Indicators","Do producer price spikes precede hate crime increases?","XREF","US","Line chart","Crime and Law Enforcement","D:/raw_data/fbi/hate_crime + D:/raw_data/cpi/ppi",78,72,68,78,80,72,78,78))
ideas.append(mk("gw005","FiveThirtyEight Bad Drivers vs Sage Vehicle Registration","States with more cars per capita vs states with worse drivers","XREF","US-State","Bivariate choropleth","Transportation","D:/raw_data/fivethirtyeight/bad-drivers + Sage vehicles",68,82,75,72,62,80,68,88))
ideas.append(mk("gw006","World Cup Viewership vs Beer Consumption by Country","Does FIFA fandom correlate with alcohol consumption?","XREF","World","Scatter plot","Sports & Recreation","D:/raw_data/worldcup + fivethirtyeight/drinks",62,78,68,78,48,75,78,88))
ideas.append(mk("gw007","Sage Religion Data vs OWID Democracy: Does Faith Predict Freedom?","Religious adherence rates vs political regime type across countries","XREF","World","Scatter plot","International Statistics","Sage religion + OWID political-regime",72,68,68,78,72,75,78,78))
ideas.append(mk("gw008","HSUS Slave Population vs OWID Prison Rate: The 200-Year Thread","Historical slavery geography vs modern mass incarceration by state","XREF","US-State","Bivariate choropleth","History","HSUS slave pop + OWID prison rate",92,78,68,80,92,82,85,75))
ideas.append(mk("gw009","Kaggle Fuel Prices vs CPI: Which Drives Which?","56 years of fuel price data aligned with consumer price inflation","XREF","US","Line chart","Economy","Kaggle fuel_prices + CPI data",72,82,78,68,68,72,62,92))
ideas.append(mk("gw010","OWID CO2 vs Kaggle Temperature: The Warming Correlation","Per-capita CO2 emissions vs mean annual temperature changes globally","XREF","World","Scatter plot","Climate","OWID co2 + Kaggle temperature",82,75,72,72,80,78,65,82))

# === INTERNATIONAL COMPARISON VIRAL ===
ideas.append(mk("gw011","The Size of Africa vs Everything Else: Mercator Lies","True size comparison showing Africa contains the US, China, India, and Europe","MAP","World","Special map","Geography & Environment","land area data",72,78,72,88,55,88,82,90))
ideas.append(mk("gw012","Americas Military Bases Around the World: 750+ Installations","Every known U.S. military installation on foreign soil","MAP","World","Dot map","International Statistics","DoD base structure report",78,72,72,78,78,85,72,82))
ideas.append(mk("gw013","How Many Countries Fit Inside the U.S.?","Overlay of European countries inside the continental U.S. for scale","MAP","World","Special map","Geography & Environment","land area data",62,78,78,82,48,88,78,90))
ideas.append(mk("gw014","The World Map Upside Down: What If South Were Up?","Flipping the standard orientation challenges geographic bias","MAP","World","Special map","Geography & Environment","standard projection data",55,65,70,85,42,88,88,90))
ideas.append(mk("gw015","Countries Without a McDonalds: The Last Holdouts","The shrinking list of nations without a McDonalds franchise","MAP","World","World choropleth","Economy","McDonalds international data",58,78,75,78,48,80,72,85))

# === INFRASTRUCTURE / ENGINEERING ===
ideas.append(mk("gw016","Americas Crumbling Infrastructure: Bridge Condition by State","Structurally deficient bridges as percentage of total by state","MAP","US-State","State choropleth","Transportation","FHWA NBI bridge data",78,82,75,68,78,78,62,85))
ideas.append(mk("gw017","Every Railroad in America: The Rail Network Map","Complete freight and passenger rail lines across the U.S.","MAP","US","Line map","Transportation","FRA rail network data",58,68,78,62,48,90,62,85))
ideas.append(mk("gw018","Americas Dam Safety Map: High-Hazard Dams","Dams rated as high hazard potential by the Army Corps of Engineers","MAP","US","Dot map","Geography & Environment","NID dam inventory data",75,72,72,72,78,85,68,82))
ideas.append(mk("gw019","The Interstate Highway System: Traffic Volume by Segment","Average annual daily traffic for every interstate highway segment","MAP","US","Line map","Transportation","FHWA HPMS traffic data",62,78,78,62,48,88,58,82))
ideas.append(mk("gw020","Americas Power Grid: Transmission Lines Mapped","High-voltage transmission infrastructure across the country","MAP","US","Line map","Climate","EIA power line data",65,68,75,68,58,90,65,82))

# === DEMOGRAPHICS DEEP DIVES ===
ideas.append(mk("gw021","Americas Racial Dot Map: One Dot Per Person","5-color dot density map with one dot per census respondent","MAP","US","Dot map","Demographics","Census race data",78,82,72,72,72,92,68,82))
ideas.append(mk("gw022","The Language Map: Most Spoken Non-English Language by County","What language besides English is most common in each county","MAP","US-County","County choropleth","Demographics","Census ACS language data",68,82,78,72,55,82,68,85))
ideas.append(mk("gw023","Americas Aging Map: Median Age Change by County 2000-2025","Which counties are aging fastest vs getting younger","MAP","US-County","County choropleth","Demographics","Census age data",72,78,72,68,68,82,65,82))
ideas.append(mk("gw024","Where Immigrants From Each Country Live in the U.S.","Indian-Americans in NJ, Vietnamese in TX, Somalis in MN - origin-specific maps","MAP","US-State","State choropleth","Demographics","Census ACS ancestry data",70,82,75,72,58,80,68,85))
ideas.append(mk("gw025","Americas 100 Most Populated Zip Codes","The densest zip codes in the country ranked and mapped","MAP","US","Dot map","Demographics","Census ZCTA data",62,78,78,68,52,82,62,85))

# === FINAL CROSS-REFS: ALL LOCAL DATA COMBOS ===
ideas.append(mk("gw026","FiveThirtyEight Drug Use by Age vs OWID Life Expectancy","Age-specific drug usage rates plotted against longevity trends","XREF","US","Scatter plot","Health","fivethirtyeight drug-use + OWID life-expectancy",75,78,68,75,72,75,72,82))
ideas.append(mk("gw027","Kaggle Student Habits vs FiveThirtyEight College Majors","Study patterns correlated with choice of major and earnings","XREF","US","Scatter plot","Education","Kaggle student habits + fivethirtyeight recent-grads",68,82,72,72,58,72,72,82))
ideas.append(mk("gw028","Sage NAEP Scores vs OWID Education Spending","Do countries that spend more on education score better?","XREF","World","Scatter plot","Education","Sage NAEP + OWID research-spending",70,78,75,68,62,75,65,82))
ideas.append(mk("gw029","HSUS Historical Population vs Modern Census: State Trajectories","200-year population curves for every state overlaid","CHART","US-State","Line chart","Demographics","HSUS state pop + Census 2020",68,75,78,65,58,78,65,78))
ideas.append(mk("gw030","FBI UCR Participation vs Actual Crime Reporting Gaps","States that report less to the FBI: what are they hiding?","XREF","US-State","Bivariate choropleth","Crime and Law Enforcement","FBI UCR participation + actual crime data",72,68,68,78,75,78,78,85))

# === REMAINING SECTION FILLERS ===
ideas.append(mk("gw031","Americas Fishing Industry: Catch by Port and Species","Commercial fish landings at major ports across the U.S.","MAP","US","Dot map","Food & Nutrition","NOAA fisheries data",58,68,72,62,48,82,65,82))
ideas.append(mk("gw032","The Global Arms Trade: Who Sells Weapons to Whom","Arms export and import flows between nations","MAP","World","Flow map","International Statistics","SIPRI arms transfer data",78,68,70,72,82,85,72,82))
ideas.append(mk("gw033","Americas Weather Station Network","Every NOAA weather station location showing coverage gaps","MAP","US","Dot map","Climate","NOAA weather station data",52,62,75,58,42,85,62,88))
ideas.append(mk("gw034","The Speed Limit Map: Maximum Allowed Speed by State","Highway speed limits across America from 55 to 85 mph","MAP","US-State","State choropleth","Transportation","state speed limit data",55,82,80,62,42,78,55,92))
ideas.append(mk("gw035","Child Care Deserts: Where Affordable Day Care Doesnt Exist","Counties where childcare supply falls far short of demand","MAP","US-County","County choropleth","Education","child care data + Census",82,88,72,68,78,82,65,78))
ideas.append(mk("gw036","Americas Superfund Sites: Toxic Waste Near You","EPA Superfund National Priorities List sites mapped","MAP","US","Dot map","Geography & Environment","EPA Superfund data",78,82,72,72,78,85,65,88))
ideas.append(mk("gw037","The Global Refugee Route Map: How People Flee","Major refugee movement corridors from conflict to asylum","MAP","World","Flow map","International Statistics","UNHCR refugee flow data",88,78,68,72,88,88,72,78))
ideas.append(mk("gw038","Americas Homecoming: Boomerang Migration by State","People who moved away and then moved back to their birth state","MAP","US-State","State choropleth","Demographics","Census ACS migration data",65,78,72,72,55,78,72,78))
ideas.append(mk("gw039","The World Map of Coastline Length","Countries ranked by total coastline - Norway beats most despite its small size","MAP","World","World choropleth","Geography & Environment","coastline measurement data",55,62,75,78,42,82,72,88))
ideas.append(mk("gw040","Americas Flood Insurance Map: Who Pays vs Who Floods","NFIP flood insurance policies vs actual flood damage by county","XREF","US-County","Bivariate choropleth","Climate","FEMA NFIP + flood damage data",75,82,72,72,72,82,68,78))

print(f"BATCH_GW: {len(ideas)} ideas generated")

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
    print("[BATCH_GW] ERROR: tail marker not found"); sys.exit(1)
raw = raw.replace(tail, "")
for idea in new_ideas:
    raw += idea + ",\n"
raw += tail + "\n"
with open(DATA_JS, "w", encoding="utf-8") as f:
    f.write(raw)
print(f"[BATCH_GW] Injected {len(new_ideas)} new ideas (skipped {skipped} dupes)")
