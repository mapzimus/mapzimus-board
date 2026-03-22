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
# === Poverty × Crime ===
mk("HBP01","Poverty Rate vs. Property Crime by Metro","Economic desperation mapped against theft and burglary","XREF","US-metro","Scatter plot","Poverty|Crime|Economy","Census: SAIPE (census.gov); FBI: UCR Property Crime (fbi.gov)",75,72,75,72,72,65,68,88),
mk("HBP02","Homeless Encampment Size by City vs. Cost of Living","Where the crisis is most visible and why","XREF","US-city","Scatter plot","Poverty|Housing|Crime","HUD: Point-in-Time Count (hudexchange.info); BEA: Regional Price Parities (bea.gov)",80,78,72,72,78,68,70,75),
# === Democracy × Race ===
mk("HBP03","Polling Place Closures by County and Racial Composition","Majority-minority counties lost the most polling locations since 2013","XREF","US-county","Bivariate choropleth","Democracy|Race|Politics","Leadership Conference: Polling Place Report (civilrights.org); Census: ACS Race (census.gov)",82,72,68,78,85,78,78,78),
mk("HBP04","Voter ID Law Strictness vs. Minority Turnout Change","What happened to minority voting after strict ID laws passed","XREF","US-state","Scatter plot","Democracy|Race|Politics|Law","NCSL: Voter ID Laws (ncsl.org); Census: CPS Voting Supplement (census.gov)",80,68,70,78,82,65,78,78),
# === Energy × Rural ===
mk("HBP05","Wind Farm Revenue Sharing With Local Communities","How much rural counties earn from wind turbines on their land","MAP","US-county","County choropleth","Energy|Rural|Economy","AWEA: Wind Benefits (cleanpower.org); LBNL: Wind Community Benefits (lbl.gov)",65,65,72,72,58,78,72,72),
mk("HBP06","Energy Poverty in Rural America","Households spending over 10% of income on energy bills","MAP","US-county","County choropleth","Energy|Rural|Poverty","EIA: Residential Energy Consumption (eia.gov); Census: ACS Income (census.gov)",78,75,72,72,75,78,68,82),
# === Media × Economy ===
mk("HBP07","Local Newspaper Revenue Collapse Over 20 Years","Ad revenue fell from 49B to 9B and took journalism with it","CHART","US-national","Area chart","Media|Economy|History","Pew: State of News Media (pewresearch.org); NAA: Newspaper Revenue (newsmediaalliance.org)",78,72,78,78,78,68,68,88),
mk("HBP08","Podcast Listener Demographics vs. Traditional Radio","Who is migrating from AM/FM to on-demand audio","CHART","US-national","Bar chart","Media|Technology|Demographics","Edison: Infinite Dial (edisonresearch.com); Nielsen: Audio Data (nielsen.com)",58,72,75,68,52,65,68,78),
# === Children × Health ===
mk("HBP09","Childhood Obesity Rate by State Over 20 Years","The trend is alarming and accelerating","MAP","US-state","Animated choropleth","Children|Health|Food","CDC: Youth Risk Behavior Survey (cdc.gov/yrbs); CDC: BRFSS (cdc.gov/brfss)",78,78,78,72,75,78,65,88),
mk("HBP10","Childhood Vaccination Rate by State","Exemptions are rising and herd immunity is eroding in pockets","MAP","US-state","State choropleth","Children|Health|Education","CDC: School Vaccination Coverage (cdc.gov); NCSL: Immunization Exemptions (ncsl.org)",78,78,78,72,78,78,68,88),
# === Finance × Geography ===
mk("HBP11","Payday Lender Density by County vs. Bank Density","Financial deserts rely on predatory lending","MAP","US-county","Bivariate choropleth","Finance|Geography|Poverty","CFPB: Payday Lending Data (consumerfinance.gov); FDIC: Summary of Deposits (fdic.gov)",80,72,72,78,78,78,72,82),
mk("HBP12","Cryptocurrency Mining Locations vs. Electricity Cost","Cheap power attracts miners creating weird energy hotspots","MAP","US-state","Scatter plot","Finance|Energy|Technology","Cambridge: Bitcoin Mining Map (ccaf.io); EIA: Electricity Prices (eia.gov)",62,58,72,78,62,68,78,75),
# === History × Crime ===
mk("HBP13","Lynching Sites in America Mapped","Every documented lynching from 1877 to 1950 geolocated","MAP","US-state","Dot map","History|Crime|Race","EJI: Lynching in America (eji.org); Monroe and Florence Work Today (plaintalkhistory.com)",88,65,68,78,88,82,72,78),
mk("HBP14","Prohibition Enforcement Intensity by State","Some states barely enforced it and others went all in","MAP","US-state","State choropleth","History|Crime|Politics","Historical: Prohibition Enforcement Records; Smithsonian: Prohibition Data (si.edu)",62,62,72,78,62,78,75,68),
# === Transportation × Politics ===
mk("HBP15","Gas Tax by State vs. Road Quality","States that invest more in roads through gas tax have better pavement","XREF","US-state","Scatter plot","Transportation|Politics|Infrastructure","API: State Motor Fuel Taxes (api.org); FHWA: Highway Statistics (fhwa.dot.gov)",68,72,78,72,65,65,68,90),
mk("HBP16","Red State vs. Blue State Public Transit Investment Per Capita","The partisan divide in how Americans get around","XREF","US-state","Bar chart","Transportation|Politics|Infrastructure","NTD: Transit Profiles (transit.dot.gov); MIT: Election Lab (electionlab.mit.edu)",72,68,72,78,72,65,72,82),
# === Space × International ===
mk("HBP17","Active Satellites by Country","The US leads but Chinas count is exploding","CHART","World","Bar chart","Space|International|Technology","UCS: Satellite Database (ucsusa.org); UN: OOSA (unoosa.org)",62,55,78,72,60,68,65,90),
mk("HBP18","Countries With Active Space Programs","From NASA to ISRO to private companies — whos reaching for the stars","MAP","World","World choropleth","Space|International|Technology","Various: National Space Agencies; Bryce Tech: State of Space (brycetech.com)",58,55,75,72,55,78,65,82),
# === Economy × Race ===
mk("HBP19","Business Loan Approval Rates by Race of Applicant","Controlling for credit score and revenue Black owners still get denied more","XREF","US-national","Bar chart","Economy|Race|Finance","Fed: Small Business Credit Survey (fedsmallbusiness.org); SBA: Lending Data (sba.gov)",85,72,72,80,82,65,75,78),
mk("HBP20","Wealth Mobility by Race","Starting poor and ending rich happens at very different rates by race","CHART","US-national","Bar chart","Economy|Race|Inequality","Opportunity Insights: Race and Mobility (opportunityinsights.org)",88,75,72,82,85,65,75,80),
# === Environment × Housing ===
mk("HBP21","Toxic Release Inventory Sites Near Schools","EPA-tracked polluters within 1 mile of public schools","MAP","US-national","Dot map","Environment|Housing|Children|Health","EPA: TRI Data (epa.gov/tri); NCES: School Locations (nces.ed.gov)",82,78,68,78,82,82,72,85),
mk("HBP22","Flood Damage Costs by County vs. Flood Insurance Adoption","Most flood damage happens where people dont have flood insurance","XREF","US-county","Bivariate choropleth","Environment|Housing|Finance","FEMA: NFIP Claims (fema.gov); NOAA: Storm Events (ncdc.noaa.gov)",75,72,72,78,75,78,70,85),
# === International × Demographics ===
mk("HBP23","Countries That Are Shrinking","Negative population growth mapped — its more than just Japan","MAP","World","World choropleth","International|Demographics|Economy","UN: World Population Prospects (population.un.org)",68,62,78,78,68,78,68,90),
mk("HBP24","The Youth Bulge Map","Countries where over 50% of the population is under 25","MAP","World","World choropleth","International|Demographics","UN: Population Data (population.un.org); World Bank: Demographics (worldbank.org)",65,60,78,75,65,78,68,90),
mk("HBP25","Median Age by Country","From Nigers 15 to Japans 49 — the map of demographic destiny","MAP","World","World choropleth","International|Demographics|Economy","CIA: World Factbook (cia.gov); UN: Population Data (population.un.org)",62,60,80,75,60,78,65,92),
# === Last round of unique combos ===
mk("HBP26","The Teacher Pay Penalty","How much less teachers earn than comparably educated workers by state","MAP","US-state","State choropleth","Education|Labor|Economy","EPI: Teacher Pay Gap (epi.org); BLS: OES (bls.gov); Census: ACS Education (census.gov)",82,82,78,78,78,78,68,85),
mk("HBP27","States Where Its Cheaper to Go to Prison Than College","Annual incarceration cost vs. annual in-state tuition","XREF","US-state","Bar chart","Crime|Education|Economy","Vera: Price of Prisons (vera.org); College Board: Tuition Trends (collegeboard.org)",80,78,80,85,78,65,78,85),
mk("HBP28","Americas Shrinking Attention Span Measured by Entertainment","Song intros movie runtimes and news segment lengths over decades","CHART","US-national","Line chart","Entertainment|Psychology|Technology","Kaggle: Spotify Audio Features; Nielsen: TV Ratings (nielsen.com); PEJ: News Studies",62,78,72,75,58,65,78,68),
mk("HBP29","The Noise Pollution Map of America","Where ambient decibel levels exceed healthy thresholds","MAP","US-national","County choropleth","Environment|Health|Geography","NPS: Sound Map (nps.gov/subjects/sound); EPA: Noise Data (epa.gov)",65,65,72,72,62,82,72,78),
mk("HBP30","Pet Ownership Rate vs. Happiness Score by Country","Countries with more pets report higher wellbeing","XREF","World","Scatter plot","Psychology|International|Health","Euromonitor: Pet Ownership (euromonitor.com); World Happiness Report (worldhappiness.report)",55,68,72,78,50,65,75,72),
mk("HBP31","The Geography of American Conspiracy Belief","Which conspiracy theories are most popular in which states","MAP","US-state","State choropleth","Psychology|Politics|Media","PRRI: American Conspiracy Survey (prri.org); Pew: Conspiracy Beliefs (pewresearch.org)",68,72,68,78,68,78,78,68),
mk("HBP32","Americas Disappearing Diners Drive-Ins and Independent Restaurants","Chain restaurants replacing independent ones decade by decade","CHART","US-national","Area chart","Food|Economy|History","Census: County Business Patterns (census.gov); NRA: Restaurant Data (restaurant.org)",72,78,75,72,68,68,72,82),
mk("HBP33","Every Countries Flag Mapped by Dominant Color","A world map colored by the primary color of each national flag","MAP","World","World choropleth","International|Geography|History","Flag data: Vexillology databases; Natural Earth: Country Boundaries (naturalearthdata.com)",50,55,72,72,42,85,72,85),
mk("HBP34","Americas Most Overworked Professions","Hours worked per week by occupation — some professions average 60+","RANK","US-national","Bar chart","Labor|Health|Economy","BLS: American Time Use Survey (bls.gov); AMA: Physician Work Hours (ama-assn.org)",72,82,78,72,68,65,65,85),
mk("HBP35","The Map of Every County Named After a Person","Who were the people that Americas geography was named after","MAP","US-county","County choropleth","History|Geography|Demographics","Census: County Names (census.gov); GNIS: Geographic Names (usgs.gov)",52,58,75,75,45,82,78,82),
]

# --- inject ---
with open(DATA, 'r', encoding='utf-8') as f:
    txt = f.read()
ids = set(re.findall(r'id:"([^"]+)"', txt))
new = [i for i in IDEAS if re.search(r'id:"([^"]+)"', i).group(1) not in ids]
if not new:
    print("All HBP ideas already present"); exit()
tail = "]; // end D"
txt = txt.replace(tail, ",\n".join(new) + ",\n" + tail)
with open(DATA, 'w', encoding='utf-8') as f:
    f.write(txt)
print(f"Injected {len(new)} new ideas (HBP batch)")
