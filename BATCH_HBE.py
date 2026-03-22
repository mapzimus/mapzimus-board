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
# === "Invisible Geography" — things you didn't know had maps ===
mk("HBE01","The Accent Map of America","Dialect regions based on how people pronounce soda vs. pop vs. coke","MAP","US-county","County choropleth","Geography|Demographics|Entertainment","Harvard Dialect Survey (dialect.redlog.net); Cambridge Online Survey of World Englishes (cam.ac.uk)",60,85,78,75,50,82,78,72),
mk("HBE02","Americas Aquifer Map","Underground water reserves that supply 40% of US drinking water","MAP","US-national","Special map","Geography|Environment|Infrastructure","USGS: National Aquifer Map (usgs.gov); USGS: Groundwater Watch (groundwaterwatch.usgs.gov)",72,65,75,72,72,88,72,92),
mk("HBE03","Every Time Zone Boundary That Makes No Sense","Cities split by time zones and the bizarre county-level borders","MAP","US-national","Special map","Geography|Infrastructure","DOT: Time Zone Boundaries (transportation.gov); Census: County Boundaries (census.gov)",58,72,78,82,52,82,80,90),
mk("HBE04","The Tornado Alley Is Moving East","Comparing tornado frequency maps 1950-1985 vs. 1990-2024","MAP","US-state","Bivariate choropleth","Geography|Climate|Science","NOAA: Storm Prediction Center (spc.noaa.gov); NOAA: Storm Events Database (ncdc.noaa.gov)",75,72,75,80,72,82,75,90),
mk("HBE05","The Blood Type Map of the World","Geographic distribution of A B AB and O blood types","MAP","World","World choropleth","Geography|Health|Science","WHO: Blood Safety (who.int); Stanford Blood Center: Distribution Data (stanfordbloodcenter.org)",55,62,75,78,50,80,75,78),
# === "The System Is Rigged" series — high tension ===
mk("HBE06","Exposed: Where Your Tax Refund Actually Goes","Federal spending allocation per dollar of income tax paid by state","CHART","US-state","State choropleth","Economy|Politics|Inequality","IRS: SOI Data (irs.gov); USASpending: Federal Awards (usaspending.gov)",80,85,78,78,78,72,70,90),
mk("HBE07","Hospital Chargemaster Prices vs. What Insurance Actually Pays","The same procedure listed at 5x what anyone actually pays","CHART","US-national","Bar chart","Health|Economy|Inequality","CMS: Hospital Price Transparency (data.cms.gov); KFF: Employer Health Benefits (kff.org)",85,88,75,80,82,65,72,78),
mk("HBE08","Private Prison Locations vs. Lobbying Dollars","States where private prisons donate most to politicians","XREF","US-state","Bivariate choropleth","Crime|Economy|Politics","OpenSecrets: Lobbying Data (opensecrets.org); BJS: Census of State Prisons (bjs.gov)",82,72,68,78,85,78,78,78),
mk("HBE09","Insulin Price in Every Country","The same vial costs 30x more in America than in Canada","RANK","World","Bar chart","Health|International|Prices","Rand: International Drug Price Comparisons (rand.org); PharmacyChecker: International Prices (pharmacychecker.com)",88,85,82,80,85,68,68,85),
mk("HBE10","College Tuition Growth vs. Every Other Major Expense Since 1980","Tuition has outpaced housing cars food and healthcare combined","CHART","US-national","Line chart","Education|Economy|Prices","BLS: CPI All Items (bls.gov); College Board: Trends in College Pricing (collegeboard.org)",88,90,82,78,82,70,68,92),
# === Kaggle dataset × federal data mashups ===
mk("HBE11","Airbnb Density vs. Homeless Population by City","Do short-term rentals reduce housing stock for the vulnerable?","XREF","US-city","Scatter plot","Housing|Economy|Poverty","Kaggle: Airbnb Listings (kaggle.com/datasets/airbnb); HUD: Point-in-Time Count (hudexchange.info)",82,80,70,78,80,68,78,72),
mk("HBE12","Uber and Lyft Trip Density vs. DUI Arrests","Did rideshare actually reduce drunk driving?","XREF","US-city","Scatter plot","Transportation|Crime|Technology","Kaggle: Uber/Lyft Dataset (kaggle.com/datasets/brllrb/uber-and-lyft-dataset); FBI: UCR DUI Arrests (fbi.gov)",72,78,75,78,68,65,78,68),
mk("HBE13","Yelp Restaurant Ratings vs. Health Inspection Scores","Are the highest-rated restaurants actually the cleanest?","XREF","US-city","Scatter plot","Food|Health|Technology","Kaggle: Yelp Dataset (kaggle.com/datasets/yelp-dataset/yelp-dataset); NYC Open Data: Restaurant Inspections (data.cityofnewyork.us)",68,78,78,80,62,65,78,72),
# === "What $1 Buys You" series ===
mk("HBE14","What One Dollar Buys in Every Country","Purchasing power parity visualized through everyday items","MAP","World","World choropleth","Prices|International|Economy","World Bank: PPP Conversion Factors (worldbank.org); Numbeo: Cost of Living (numbeo.com)",68,78,82,72,58,78,65,88),
mk("HBE15","What One Dollar of Healthcare Buys by Country","US gets less health outcome per dollar than nearly everyone","CHART","World","Bar chart","Health|International|Prices","OECD: Health Expenditure (oecd.org); WHO: Health Statistics (who.int)",82,78,80,80,78,68,70,90),
mk("HBE16","What Your Property Tax Dollar Funds by City","Wildly different allocations: some cities spend 60% on police","CHART","US-city","Treemap","Economy|Politics|Infrastructure","Lincoln Institute: Property Tax Database (lincolninst.edu); Census: Annual Survey of Governments (census.gov)",75,80,78,75,72,72,70,82),
# === Climate × Health ===
mk("HBE17","Heat Wave Deaths Per Year vs. 20 Years Ago","The silent climate killer thats accelerating","CHART","US-national","Bar chart","Climate|Health","CDC: Heat-Related Deaths (wonder.cdc.gov); NOAA: Climate Extremes (ncei.noaa.gov)",82,75,78,75,80,65,68,88),
mk("HBE18","Asthma Rates Mapped Against Wildfire Smoke Days","Western states smoke exposure and the respiratory toll","XREF","US-state","Bivariate choropleth","Climate|Health|Environment","CDC: Asthma Data (cdc.gov/asthma); EPA: AirNow Fire and Smoke (fire.airnow.gov)",80,75,72,72,78,78,72,80),
mk("HBE19","Tick-Borne Disease Range Expansion Since 1995","Lyme disease moving north as winters warm","MAP","US-state","Animated choropleth","Climate|Health|Science","CDC: Lyme Disease Maps (cdc.gov/lyme); NOAA: Temperature Anomalies (ncei.noaa.gov)",72,70,72,78,72,80,75,85),
# === Entertainment × Demographics ===
mk("HBE20","The Netflix Password Sharing Map","Estimated accounts per household by state before the crackdown","MAP","US-state","State choropleth","Entertainment|Demographics|Technology","Statista: Netflix Subscribers (statista.com); Census: Households (census.gov)",62,82,72,72,58,72,78,55),
mk("HBE21","Americas Most Popular Music Genre by State","What Spotify streaming data reveals about regional taste","MAP","US-state","State choropleth","Entertainment|Demographics|Geography","Kaggle: Spotify Dataset (kaggle.com/datasets/maharshipandya/-spotify-tracks-dataset); Spotify: Listening Trends (newsroom.spotify.com)",60,78,78,72,52,78,72,65),
mk("HBE22","Movie Box Office Revenue vs. Rotten Tomatoes Score","Are critically acclaimed movies actually commercially successful?","XREF","US-national","Scatter plot","Entertainment|Economy","Kaggle: Movies Dataset (kaggle.com/datasets/rounakbanik/the-movies-dataset); Box Office Mojo (boxofficemojo.com)",62,72,78,72,55,65,70,82),
# === Energy × Economy ===
mk("HBE23","States That Produce the Most Oil vs. Gas Prices at the Pump","Living on top of oil doesnt mean cheap gas","XREF","US-state","Scatter plot","Energy|Economy|Prices","EIA: Crude Oil Production (eia.gov); AAA: Gas Prices (gasprices.aaa.com)",72,80,78,80,68,65,72,90),
mk("HBE24","Household Energy Cost as Percent of Income by State","Energy burden falls hardest on the South","MAP","US-state","State choropleth","Energy|Economy|Inequality","EIA: Residential Energy Consumption (eia.gov); Census: Median Income (census.gov)",78,82,78,72,75,78,68,88),
mk("HBE25","The Green Energy Jobs Map","Solar and wind jobs per capita by state","MAP","US-state","State choropleth","Energy|Labor|Economy","DOE: US Energy and Employment Report (energy.gov); BLS: Green Goods and Services (bls.gov)",68,72,78,68,62,78,65,82),
# === "Generational" comparisons ===
mk("HBE26","Median Age at First Home Purchase by Generation","Boomers bought at 28 and Gen Z is projected at 36","CHART","US-national","Bar chart","Housing|Demographics|Economy","NAR: Home Buyer Profile (nar.realtor); Census: ACS Tenure by Age (census.gov)",85,90,82,78,80,65,68,78),
mk("HBE27","Net Worth at Age 30 by Generation Adjusted for Inflation","Each generation is falling further behind at the same age","CHART","US-national","Bar chart","Economy|Demographics|Inequality","Fed: Survey of Consumer Finances (federalreserve.gov); BLS: CPI (bls.gov)",88,90,80,80,82,68,72,82),
mk("HBE28","Share of National Wealth Held by Under-40s Over Time","It went from 12% in 1990 to under 6% today","CHART","US-national","Area chart","Economy|Demographics|Inequality","Fed: Distributional Financial Accounts (federalreserve.gov)",85,85,78,80,82,68,72,88),
# === Agriculture × Economy ===
mk("HBE29","Farm Subsidies by County: Who Actually Gets the Money","80% goes to the largest 20% of farms","MAP","US-county","County choropleth","Agriculture|Economy|Inequality","EWG: Farm Subsidy Database (farm.ewg.org); USDA: Census of Agriculture (nass.usda.gov)",78,72,75,78,78,80,72,90),
mk("HBE30","Avocado Price vs. Every Other Grocery Item Since 2010","The avocado toast economy visualized","CHART","US-national","Line chart","Agriculture|Food|Prices","USDA: Fruit and Vegetable Prices (ers.usda.gov); BLS: Average Food Prices (bls.gov)",62,82,78,70,55,65,72,88),
mk("HBE31","Americas Top Agricultural Export by State","Not every state exports what you think","MAP","US-state","State choropleth","Agriculture|Economy|Trade","USDA: State Agricultural Trade (fas.usda.gov); Census: Foreign Trade (census.gov)",62,65,78,75,58,80,68,90),
# === Immigration × Crime (data-driven debunking) ===
mk("HBE32","Immigrant Share of Population vs. Crime Rate by Metro","The data shows the opposite of what most people assume","XREF","US-metro","Scatter plot","Immigration|Crime","Census: ACS Foreign-Born (census.gov); FBI: UCR Crime Data (fbi.gov)",78,72,78,82,78,65,75,85),
mk("HBE33","Border County Crime Rates vs. Interior Counties","Are border communities actually more dangerous?","XREF","US-county","Bar chart","Immigration|Crime|Geography","FBI: UCR Crime Data (fbi.gov); Census: Border County Classification (census.gov)",75,70,78,82,78,65,78,85),
# === "World Record" maps ===
mk("HBE34","The Country That Leads the World in Everything","Each countrys number-one global ranking in something","MAP","World","World choropleth","International|Geography","CIA: World Factbook (cia.gov); World Bank: World Development Indicators (worldbank.org)",62,68,72,82,55,82,80,80),
mk("HBE35","The US County That Leads America in Everything","Each countys number-one national ranking in some metric","MAP","US-county","County choropleth","Geography|Demographics","Census: ACS (census.gov); BLS: QCEW (bls.gov); CDC: WONDER (wonder.cdc.gov)",60,68,72,82,55,82,82,75),
]

# --- inject ---
with open(DATA, 'r', encoding='utf-8') as f:
    txt = f.read()
ids = set(re.findall(r'id:"([^"]+)"', txt))
new = [i for i in IDEAS if re.search(r'id:"([^"]+)"', i).group(1) not in ids]
if not new:
    print("All HBE ideas already present"); exit()
tail = "]; // end D"
txt = txt.replace(tail, ",\n".join(new) + ",\n" + tail)
with open(DATA, 'w', encoding='utf-8') as f:
    f.write(txt)
print(f"Injected {len(new)} new ideas (HBE batch)")
