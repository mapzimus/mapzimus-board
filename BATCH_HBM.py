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
# === Kaggle deep dives: correlating platform datasets with federal data ===
mk("HBM01","Reddit Sentiment by Subreddit vs. State Mental Health Rankings","Are toxic subreddits concentrated in struggling states?","XREF","US-state","Scatter plot","Technology|Psychology|Health","Kaggle: Reddit Comments (kaggle.com/datasets/reddit); CDC: Mental Health Data (cdc.gov)",68,68,65,82,65,65,82,58),
mk("HBM02","Global Terrorism Events Mapped by Decade","How the geography of terrorism has shifted since 1970","MAP","World","Animated choropleth","War|International|Crime","Kaggle: Global Terrorism Database (kaggle.com/datasets/START-UMD/gtd); START: GTD (start.umd.edu)",75,60,72,75,78,82,68,88),
mk("HBM03","IMDb Top 250 Movies by Country of Origin","Hollywood dominates but the distribution is changing","MAP","World","World choropleth","Entertainment|International","Kaggle: IMDb Movies (kaggle.com/datasets/harshitshankhdhar/imdb-dataset-of-top-1000-movies-and-tv-shows); IMDb (imdb.com)",55,62,78,72,50,78,68,82),
mk("HBM04","Airbnb Prices vs. Hotel Prices in Tourist Cities","Where Airbnb is actually cheaper and where its not","XREF","World","Scatter plot","Housing|Economy|International","Kaggle: Airbnb Listings (kaggle.com/datasets/airbnb); Booking.com: Hotel Rates",65,78,78,72,58,65,70,68),
mk("HBM05","FIFA Player Ratings vs. Country GDP","Richer countries produce higher-rated players on average","XREF","World","Scatter plot","Sports|Economy|International","Kaggle: FIFA Dataset (kaggle.com/datasets/stefanoleone992/fifa-22-complete-player-dataset); World Bank: GDP (worldbank.org)",58,60,75,78,52,65,72,80),
# === Climate × Transportation ===
mk("HBM06","Carbon Emissions Per Passenger Mile: Every Mode of Transport","Flying is bad but driving alone is often worse","RANK","US-national","Bar chart","Climate|Transportation|Energy","EPA: Emission Factors (epa.gov); DOT: National Transportation Statistics (bts.gov)",68,72,82,78,68,65,68,88),
mk("HBM07","Cities With the Most EV Charging Stations Per Capita","The infrastructure leaders and laggards","MAP","US-city","Dot map","Climate|Transportation|Technology","AFDC: Alternative Fueling Stations (afdc.energy.gov); Census: City Population (census.gov)",62,68,78,68,58,78,65,88),
mk("HBM08","Airline Routes Ranked by Carbon Per Passenger","The most and least efficient flight paths in the US","RANK","US-national","Bar chart","Climate|Transportation|Energy","ICCT: Airline Efficiency (theicct.org); BTS: T-100 Domestic Market (bts.gov)",65,65,75,78,65,65,75,78),
# === Health × Food deep dives ===
mk("HBM09","Fast Food Restaurants Per Capita vs. Diabetes Rate by County","The density-disease correlation mapped nationwide","XREF","US-county","Bivariate choropleth","Health|Food|Economy","Census: County Business Patterns NAICS 722513 (census.gov); CDC: Diabetes Atlas (cdc.gov/diabetes)",78,78,75,72,72,78,68,85),
mk("HBM10","Food Recall Frequency by Company","Which brands have the most FDA recalls per year","RANK","US-national","Bar chart","Food|Health","FDA: Recall Database (fda.gov/recalls); USDA: FSIS Recalls (fsis.usda.gov)",72,78,78,72,68,62,72,85),
mk("HBM11","Ultra-Processed Food Consumption by Country vs. Obesity","The correlation between packaged food and national waistlines","XREF","World","Scatter plot","Food|Health|International","NOVA: Food Classification Studies; WHO: Obesity Data (who.int)",75,72,72,78,72,65,72,72),
# === Economy × Infrastructure ===
mk("HBM12","Broadband Speed by County vs. Business Formation Rate","Fast internet predicts new business startups","XREF","US-county","Bivariate choropleth","Economy|Infrastructure|Technology","FCC: Broadband Data (broadbandmap.fcc.gov); Census: Business Formation Statistics (census.gov)",72,68,72,78,68,78,72,82),
mk("HBM13","Airport Proximity and Property Values","Homes within 5 miles of airports are worth less but the noise premium varies","XREF","US-metro","Scatter plot","Infrastructure|Housing|Transportation","FAA: Airport Data (faa.gov); Zillow: Home Values (zillow.com/research)",68,72,72,72,62,68,70,72),
mk("HBM14","Public Transit Coverage vs. Economic Mobility","Cities with better transit have more upward mobility","XREF","US-metro","Scatter plot","Infrastructure|Economy|Transportation","NTD: Transit Profiles (transit.dot.gov); Opportunity Insights: Mobility (opportunityinsights.org)",75,72,72,78,72,68,72,78),
# === War × Health ===
mk("HBM15","Veteran Suicide Rate by State","22 veterans a day and some states are far worse than others","MAP","US-state","State choropleth","War|Health|Military","VA: National Veteran Suicide Prevention Report (mentalhealth.va.gov); Census: ACS Veterans (census.gov)",88,75,75,72,85,78,68,85),
mk("HBM16","Agent Orange Exposure Zones and Current Health Outcomes","The Vietnam-era chemical weapon still causing cancer 50 years later","MAP","World","Dot map","War|Health|History","VA: Agent Orange Registry (va.gov); NIH: AO Health Studies (nih.gov)",82,62,68,78,80,78,75,72),
mk("HBM17","PTSD Diagnosis Rate Among Veterans by Conflict Era","Iraq and Afghanistan veterans diagnosed at 2x the rate of Gulf War vets","CHART","US-national","Bar chart","War|Health|Psychology","VA: PTSD Data (ptsd.va.gov); DoD: Health Surveillance (health.mil)",80,68,75,72,78,65,68,82),
# === Education × Geography ===
mk("HBM18","Teacher Vacancy Rate by State","The states hemorrhaging teachers the fastest","MAP","US-state","State choropleth","Education|Geography|Labor","NCES: Teacher Attrition (nces.ed.gov); Learning Policy Institute: Teacher Shortage (learningpolicyinstitute.org)",78,78,75,72,75,78,68,80),
mk("HBM19","College-Free Zones","Counties where the nearest 4-year college is 50+ miles away","MAP","US-county","County choropleth","Education|Geography|Rural","NCES: IPEDS Locations (nces.ed.gov); Census: County Centroids (census.gov)",72,70,75,75,70,82,72,85),
mk("HBM20","SAT Score by State vs. State Education Spending","More spending doesnt always mean higher scores — but the participation rate matters","XREF","US-state","Scatter plot","Education|Economy","College Board: SAT Suite (collegeboard.org); Census: School Finance (census.gov)",70,72,78,78,68,65,72,88),
# === Race × Economy ===
mk("HBM21","The Racial Wealth Gap by Metro Area","In some cities the gap is 100x between white and Black families","MAP","US-metro","Bar chart","Race|Economy|Inequality","Fed: Survey of Consumer Finances (federalreserve.gov); Brookings: Metro Data (brookings.edu)",88,78,75,80,85,68,72,78),
mk("HBM22","Black Business Ownership Rate by State","Which states have the highest rates of Black entrepreneurship","MAP","US-state","State choropleth","Race|Economy","Census: Annual Business Survey (census.gov); SBA: Minority Business Data (sba.gov)",72,70,75,72,68,78,70,82),
mk("HBM23","Lending Discrimination by ZIP Code","Mortgage denial rates for identical credit profiles by applicant race","XREF","US-county","Bivariate choropleth","Race|Economy|Housing|Finance","FFIEC: HMDA Data (ffiec.gov); Census: ACS Race (census.gov)",85,75,70,80,85,78,75,82),
# === Environment × International ===
mk("HBM24","Countries That Have Gained Forest vs. Lost Forest Since 2000","Reforestation vs. deforestation mapped globally","MAP","World","World choropleth","Environment|International|Climate","Global Forest Watch: Tree Cover (globalforestwatch.org); FAO: Forest Resources (fao.org)",72,62,78,78,72,82,72,88),
mk("HBM25","The Worlds Most Polluted Rivers","Where industrial and agricultural runoff is worst","MAP","World","Line map","Environment|International|Health","Yale: EPI Water Quality (epi.yale.edu); UNEP: GEMStat (gemstat.org)",75,60,72,72,72,82,68,78),
mk("HBM26","E-Waste Exports: Where Rich Countries Dump Their Old Electronics","The toxic journey of discarded phones and laptops","MAP","World","Line map","Environment|International|Technology","Basel Action Network: E-Waste (ban.org); UN: E-Waste Monitor (ewastemonitor.info)",78,65,68,80,78,82,78,75),
# === Politics × Demographics ===
mk("HBM27","The Median Age of Congress vs. Median Age of Americans","Representatives average 58 while Americans average 38","CHART","US-national","Line chart","Politics|Demographics|History","ProPublica: Congress API (propublica.org); Census: Median Age (census.gov)",75,78,78,78,75,65,68,90),
mk("HBM28","Millionaire Members of Congress vs. Median Net Worth of Their Constituents","The wealth gap between representatives and represented","XREF","US-state","Bar chart","Politics|Economy|Inequality","OpenSecrets: Personal Finances (opensecrets.org); Census: Median Net Worth (census.gov)",80,78,75,78,80,65,72,82),
mk("HBM29","Voter Registration Rate by Age Group Over Time","Young people register less but the gap has been narrowing","CHART","US-national","Area chart","Politics|Demographics|Democracy","Census: CPS Voting Supplement (census.gov); EAC: Election Survey (eac.gov)",68,72,78,68,65,68,65,90),
# === Final gap-fillers ===
mk("HBM30","The Genealogy Map: Where Americas Ancestors Came From by County","Self-reported ancestry from the Census paints a striking picture","MAP","US-county","County choropleth","Demographics|History|Immigration","Census: ACS Ancestry (census.gov)",62,72,78,72,55,85,68,92),
mk("HBM31","Internet Search Interest as a Proxy for Disease Outbreaks","Google Trends flu searches predicted outbreaks weeks before CDC data","XREF","US-state","Line chart","Technology|Health|Science","Google Trends: Health Topics (trends.google.com); CDC: FluView (cdc.gov/flu)",68,68,72,82,65,65,78,72),
mk("HBM32","The Gravity Model of US Migration","People move in proportion to job opportunities and inverse to distance","MAP","US-state","Line map","Demographics|Economy|Geography","Census: ACS Migration (census.gov); BLS: JOLTS (bls.gov)",62,60,68,78,58,82,78,82),
mk("HBM33","Billionaire Population Density by City","Half the worlds billionaires live in just 15 cities","MAP","World","Dot map","Economy|International|Inequality","Forbes: Billionaires List (forbes.com); Wealth-X: Billionaire Census (wealthx.com)",68,65,78,78,62,78,68,85),
mk("HBM34","National Parks Visitation vs. Staffing Levels Since 1980","Visits have doubled while ranger staffing has fallen","CHART","US-national","Line chart","Environment|Economy|Infrastructure","NPS: Visitor Use Statistics (irma.nps.gov); NPS: Budget Data (nps.gov)",72,70,75,78,72,68,72,88),
mk("HBM35","The Most Moved-To and Moved-From ZIP Codes in America","Net migration at the ZIP code level reveals surprising winners and losers","MAP","US-county","Bivariate choropleth","Demographics|Geography|Housing","USPS: Change of Address Data; Census: ACS Migration (census.gov)",72,78,75,72,65,80,72,78),
]

# --- inject ---
with open(DATA, 'r', encoding='utf-8') as f:
    txt = f.read()
ids = set(re.findall(r'id:"([^"]+)"', txt))
new = [i for i in IDEAS if re.search(r'id:"([^"]+)"', i).group(1) not in ids]
if not new:
    print("All HBM ideas already present"); exit()
tail = "]; // end D"
txt = txt.replace(tail, ",\n".join(new) + ",\n" + tail)
with open(DATA, 'w', encoding='utf-8') as f:
    f.write(txt)
print(f"Injected {len(new)} new ideas (HBM batch)")
