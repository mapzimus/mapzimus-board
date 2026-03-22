import re, os
DATA = os.path.join(os.path.dirname(__file__), 'data.js')

def mk(id,title,sub,typ,geo,fmt,sect,tbl,e,r,c,s,t,v,o,dr):
    raw=e*2+r*2+c*1.25+s*1.5+t*1.5+v*2.0+o*1.5
    vs=int((raw/11.75)*(1-0.5*(1-dr/100)))
    return ('{id:"'+id+'",title:"'+title+'",sub:"'+sub+'",type:"'+typ+'",'
            'geo:"'+geo+'",fmt:"'+fmt+'",section:"'+sect+'",tbl:"'+tbl+'",'
            'sc:{emotional:'+str(e)+',relatability:'+str(r)+',clarity:'+str(c)
            +',surprise:'+str(s)+',tension:'+str(t)+',visual:'+str(v)
            +',originality:'+str(o)+',data_ready:'+str(dr)+'}'
            ',vs:'+str(vs)+',topics:[],ext:[],status:"idea",notes:""}')

IDEAS = [
# === "The Map That Makes You Angry" series ===
mk("HBB01","Tax Dollars Per Mile of Road by State","Some states pay 10x more per highway mile than others","RANK","US-state","Bar chart","Infrastructure|Economy|Transportation","FHWA: Highway Statistics (fhwa.dot.gov); Census: State Tax Revenue (census.gov)",78,82,80,78,75,68,72,90),
mk("HBB02","How Much of Your Rent Goes to Your Landlords Mortgage","Rent-to-mortgage-payment ratio in every US metro","CHART","US-metro","Bar chart","Housing|Economy|Inequality","Zillow: Rental Data (zillow.com/research); Freddie Mac: Mortgage Rates (freddiemac.com)",88,90,78,75,82,65,72,82),
mk("HBB03","Emergency Room Bills for the Same Procedure Across States","The same broken arm costs 400 in Mississippi and 4000 in California","RANK","US-state","Bar chart","Health|Economy|Inequality","CMS: Hospital Compare (data.cms.gov); KFF: Health Costs (kff.org)",85,88,80,82,80,65,70,85),
mk("HBB04","CEO Pay vs. Median Worker Pay Since 1965","The ratio was 20:1 in 1965 and 399:1 in 2021","CHART","US-national","Area chart","Economy|Inequality|Labor","EPI: CEO Compensation (epi.org); BLS: Occupational Employment (bls.gov)",88,85,82,78,85,72,68,92),
mk("HBB05","What a Dollar of Federal Tax Buys You by Category","Pennies on the dollar breakdown that most people get completely wrong","CHART","US-national","Treemap","Economy|Politics","CBO: Budget and Economic Data (cbo.gov); USASpending.gov (usaspending.gov)",72,82,85,75,68,78,65,95),
# === "Unexplained Correlations" series ===
mk("HBB06","Per Capita Cheese Consumption vs. Deaths by Bedsheet Tangling","The absurd correlation that launched a thousand stats lessons","XREF","US-national","Line chart","Food|Health|Science","USDA: Dairy Data (ers.usda.gov); CDC: WONDER Mortality (wonder.cdc.gov)",60,72,78,90,55,62,88,88),
mk("HBB07","Nicolas Cage Movies Released vs. Pool Drownings","The classic spurious correlation visualized beautifully","XREF","US-national","Line chart","Entertainment|Health|Science","IMDb: Filmography (imdb.com); CDC: Injury Prevention (cdc.gov/injury)",55,70,80,92,50,62,85,85),
mk("HBB08","Divorce Rate in Maine vs. Per Capita Margarine Consumption","Another absurd correlation that teaches a vital data literacy lesson","XREF","US-state","Line chart","Demographics|Food|Science","CDC: Marriage and Divorce (cdc.gov); USDA: Fats and Oils (ers.usda.gov)",55,68,78,90,50,60,85,82),
# === Triple-source deep mashups ===
mk("HBB09","Obesity + Fast Food Density + Walkability Score","The three-variable map of why Americans are overweight","XREF","US-county","Bivariate choropleth","Health|Food|Infrastructure","CDC: BRFSS Obesity (cdc.gov/brfss); Census: County Business Patterns (census.gov); Walk Score (walkscore.com)",82,85,72,70,75,80,72,78),
mk("HBB10","Student Debt + Home Ownership + Birth Rate by Metro","Three metrics that define the millennial economic trap","XREF","US-metro","Scatter plot","Education|Housing|Demographics","Fed: Student Loan Data (newyorkfed.org); Census: ACS Housing (census.gov); CDC: Natality (cdc.gov)",88,90,75,78,82,68,78,82),
mk("HBB11","Broadband Speed + Median Income + Educational Attainment","The digital divide is really just the inequality divide","XREF","US-county","Bivariate choropleth","Technology|Economy|Education","FCC: Broadband Map (broadbandmap.fcc.gov); Census: ACS Income (census.gov); Census: ACS Education (census.gov)",75,78,72,70,72,78,70,88),
mk("HBB12","Life Expectancy + Air Quality + Poverty Rate","The three horsemen of Americas health divide","XREF","US-county","Bivariate choropleth","Health|Environment|Inequality","CDC: WONDER Life Tables (wonder.cdc.gov); EPA: AQI Data (aqs.epa.gov); Census: SAIPE (census.gov)",85,78,72,72,80,78,70,88),
# === "What Happens When..." time-event analysis ===
mk("HBB13","What Happens to Crime When a Walmart Opens","Crime rates within 5 miles of new Walmart locations before and after","XREF","US-county","Line chart","Crime|Economy|Business","FBI: UCR Crime Data (fbi.gov); Walmart: Store Locations (corporate.walmart.com)",78,80,72,82,75,65,80,62),
mk("HBB14","What Happens to Rent When a Tech Company Moves In","Rent trajectory in neighborhoods before and after major tech office openings","XREF","US-metro","Line chart","Housing|Technology|Economy","Zillow: Rental Data (zillow.com/research); Crunchbase: Company HQ (crunchbase.com)",82,85,75,78,80,68,78,70),
mk("HBB15","What Happens to Property Values When a Prison Opens","Home values within 10 miles of new prison construction","XREF","US-county","Line chart","Housing|Crime|Economy","Zillow: Home Values (zillow.com/research); BJS: Census of Jails (bjs.gov)",78,72,70,80,78,65,82,65),
mk("HBB16","What Happens to Student Test Scores When School Funding Doubles","Districts that saw major funding increases vs. academic outcome changes","XREF","US-state","Scatter plot","Education|Economy","NAEP: Nations Report Card (nces.ed.gov); Census: School Finance (census.gov)",80,78,72,78,75,65,75,72),
# === "America by the Numbers" geographic curiosities ===
mk("HBB17","The Farthest You Can Be From a McDonalds in America","The most remote point from any McDonalds franchise in the lower 48","MAP","US-national","Special map","Food|Geography","OpenStreetMap: POI Data (openstreetmap.org); McDonalds: Restaurant Locator (mcdonalds.com)",62,78,80,82,55,85,80,78),
mk("HBB18","If Every State Were a Country","GDP-matched countries for each US state","MAP","US-state","State choropleth","Economy|Geography|International","BEA: GDP by State (bea.gov); World Bank: GDP (worldbank.org)",65,78,82,80,58,80,72,92),
mk("HBB19","The Center of Population Has Moved 1000 Miles","Animated path of Americas population center since 1790","MAP","US-national","Animated choropleth","Demographics|Geography|History","Census: Center of Population (census.gov)",72,70,78,78,62,85,75,95),
mk("HBB20","Every County Where More People Died Than Were Born Last Year","Natural population decrease is spreading across rural America","MAP","US-county","County choropleth","Demographics|Geography|Rural","Census: Population Estimates Components of Change (census.gov)",80,72,78,78,78,82,72,92),
# === Kaggle dataset deep dives ===
mk("HBB21","Steam Gaming Hours vs. Unemployment Rate","Do people game more where there are fewer jobs?","XREF","US-state","Scatter plot","Entertainment|Economy|Technology","Kaggle: Steam Store Games (kaggle.com/datasets/nikdavis/steam-store-games); BLS: LAUS (bls.gov)",68,75,72,78,62,65,78,70),
mk("HBB22","Spotify Streaming Patterns During Economic Downturns","Does sad music consumption spike when markets crash?","XREF","World","Line chart","Entertainment|Economy|Psychology","Kaggle: Spotify Dataset (kaggle.com/datasets/maharshipandya/-spotify-tracks-dataset); Yahoo Finance: Market Data (finance.yahoo.com)",72,78,68,82,70,62,85,60),
mk("HBB23","Global Happiness Score vs. Social Media Penetration","Are the happiest countries the ones least addicted to social media?","XREF","World","Scatter plot","Psychology|Technology|International","Kaggle: World Happiness Report (kaggle.com/datasets/unsdsn/world-happiness); Statista: Social Media Users (statista.com)",78,75,72,80,72,68,78,78),
mk("HBB24","Countries with Most McDonald\\'s vs. Diabetes Prevalence","The Golden Arches Theory of metabolic disease","XREF","World","Scatter plot","Food|Health|International","Kaggle: McDonalds Locations (kaggle.com/datasets/mcdonalds/nutrition); WHO: Diabetes Country Profiles (who.int)",75,78,78,78,72,68,72,75),
# === "One Chart" viral format ===
mk("HBB25","One Chart That Shows Why Young People Cant Buy Homes","Home price to income ratio by decade from 1960 to 2024","CHART","US-national","Line chart","Housing|Economy|Inequality","FRED: Median Home Price (fred.stlouisfed.org); Census: Median Income (census.gov)",90,92,85,78,85,72,70,92),
mk("HBB26","One Chart That Shows Americas Drug Overdose Crisis","Overdose deaths by substance stacked area from 1999 to present","CHART","US-national","Area chart","Health|Drugs","CDC: WONDER Drug Overdose (wonder.cdc.gov)",88,80,82,72,85,75,65,95),
mk("HBB27","One Chart That Shows the Hollowing Out of the Middle Class","Income distribution shift from 1970 to today","CHART","US-national","Area chart","Economy|Inequality|Demographics","Census: Income Distribution (census.gov); Pew: Middle Class (pewresearch.org)",88,85,80,75,82,72,68,90),
mk("HBB28","One Chart That Shows How Fast the Arctic Is Disappearing","September Arctic sea ice extent from 1979 to present","CHART","World","Area chart","Climate|Environment|Science","NSIDC: Sea Ice Index (nsidc.org)",85,72,82,75,85,78,65,95),
# === Data literacy / debunking ===
mk("HBB29","Maps That Lie: Population Maps vs. Per Capita Maps","The same data shown two ways tells completely different stories","CHART","US-state","State choropleth","Science|Education|Media","Census: Population Estimates (census.gov)",65,72,88,80,62,82,85,95),
mk("HBB30","Correlation Is Not Causation: The Greatest Hits","Six famously spurious correlations visualized side by side","CHART","US-national","Line chart","Science|Education","Various: Compiled Spurious Correlations (tylervigen.com)",60,72,85,88,55,68,82,90),
mk("HBB31","The Gerrymandering Gallery","Most extreme congressional district shapes vs. competitiveness","MAP","US-state","Special map","Politics|Democracy|Geography","Census: Congressional Districts (census.gov); Cook Political Report (cookpolitical.com)",78,72,72,78,80,85,72,88),
mk("HBB32","How Changing the Y-Axis Changes the Story","The same economic data presented with manipulated and honest axes","CHART","US-national","Line chart","Science|Education|Media","FRED: Various Economic Series (fred.stlouisfed.org)",62,70,88,82,65,72,85,92),
# === International eye-openers ===
mk("HBB33","Countries Where Women Couldnt Open a Bank Account Until After 1970","A timeline of financial independence rights globally","CHART","World","World choropleth","Gender|International|History","World Bank: Women Business and Law (worldbank.org)",82,78,75,85,78,78,80,82),
mk("HBB34","The World Split Into Two Halves of Equal GDP","One tiny cluster of countries produces half the worlds wealth","MAP","World","World choropleth","Economy|International|Inequality","World Bank: GDP (worldbank.org)",72,68,80,88,70,82,80,92),
mk("HBB35","Every Border Drawn by a European Colonial Power","How straight lines on a map created a century of conflict","MAP","World","World choropleth","International|History|War","LSMS: Colonial Borders Dataset (worldbank.org); Natural Earth: Admin Boundaries (naturalearthdata.com)",80,65,72,78,80,85,78,80),
]

# --- inject ---
with open(DATA, 'r', encoding='utf-8') as f:
    txt = f.read()
ids = set(re.findall(r'id:"([^"]+)"', txt))
new = [i for i in IDEAS if re.search(r'id:"([^"]+)"', i).group(1) not in ids]
if not new:
    print("All HBB ideas already present"); exit()
tail = "]; // end D"
txt = txt.replace(tail, ",\n".join(new) + ",\n" + tail)
with open(DATA, 'w', encoding='utf-8') as f:
    f.write(txt)
print(f"Injected {len(new)} new ideas (HBB batch)")
