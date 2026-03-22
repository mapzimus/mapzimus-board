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
# === "Reddit r/dataisbeautiful top post" bait ===
mk("HBH01","Every Flight Path in the World on a Single Map","Air traffic reveals economic corridors at a glance","MAP","World","Line map","Transportation|International|Economy","OpenFlights: Route Database (openflights.org); OAG: Flight Schedules (oag.com)",58,55,72,72,50,95,70,88),
mk("HBH02","The Map of the World Drawn Only With Rivers","Hydrological networks reveal continental structure beautifully","MAP","World","Special map","Geography|Environment","HydroSHEDS: River Network (hydrosheds.org); Natural Earth: Rivers (naturalearthdata.com)",50,50,68,72,42,95,78,92),
mk("HBH03","Every Building in the Netherlands","Country-scale building footprints colored by construction year","MAP","World","Special map","Geography|History|Housing","OpenStreetMap: Building Footprints (openstreetmap.org); BAG: Dutch Building Register (bag.basisregistraties.overheid.nl)",50,52,68,75,42,95,78,88),
mk("HBH04","The Ship Traffic Map of the World","AIS vessel tracking data shows global trade arteries","MAP","World","Line map","Transportation|International|Trade","MarineTraffic: AIS Data (marinetraffic.com); UNCTAD: Maritime Transport (unctad.org)",55,52,72,72,48,95,72,88),
mk("HBH05","Population Density of Earth Rendered in 3D","Spike map where height equals people per square mile","MAP","World","Special map","Demographics|Geography|International","WorldPop: Population Density (worldpop.org); SEDAC: GPWv4 (sedac.ciesin.columbia.edu)",55,55,72,75,48,95,72,90),
# === "The $X Comparison" — putting money in perspective ===
mk("HBH06","Elon Musks Net Worth vs. Countries Entire GDP","One person is richer than most nations on earth","CHART","World","Bar chart","Economy|Inequality|International","Forbes: Real-Time Billionaires (forbes.com); World Bank: GDP (worldbank.org)",82,78,82,85,78,68,70,90),
mk("HBH07","What Americas Military Budget Could Buy Instead","Universal pre-K 4x over or free college 6x over","CHART","US-national","Bar chart","Military|Economy|Politics","SIPRI: Military Expenditure (sipri.org); CBO: Budget Options (cbo.gov)",80,78,80,78,78,68,72,88),
mk("HBH08","What Jeff Bezos Earns Per Second vs. Median Worker","He makes in 11 seconds what the median worker makes in a year","CHART","US-national","Bar chart","Economy|Inequality|Labor","Forbes: Billionaires (forbes.com); Census: Median Income (census.gov)",85,82,80,82,80,65,68,85),
mk("HBH09","The Federal Deficit Visualized as a Stack of Dollar Bills","How tall would the debt be if each dollar was a physical bill","CHART","US-national","Infographic","Economy|Politics","Treasury: Debt to the Penny (treasurydirect.gov)",65,72,78,82,62,72,78,92),
# === Health × Drugs deep dives ===
mk("HBH10","Opioid Pills Shipped Per Person by County","Some counties received 100+ pills per person per year","MAP","US-county","County choropleth","Health|Drugs|Crime","WashPost: DEA Pain Pill Database (washingtonpost.com); Census: Population (census.gov)",85,78,72,82,85,82,72,88),
mk("HBH11","Alcohol Consumption Per Capita by Country","From Kuwaits near-zero to Czechias 14 liters of pure alcohol","MAP","World","World choropleth","Drugs|Health|International","WHO: Global Status Report on Alcohol (who.int)",65,70,78,72,58,78,62,90),
mk("HBH12","States That Legalized Marijuana vs. Their Crime Rate Change","Before and after legalization comparisons","XREF","US-state","Bar chart","Drugs|Crime|Politics","FBI: UCR Crime Data (fbi.gov); NORML: State Legalization Dates (norml.org)",72,75,75,78,72,65,72,80),
# === "Personal Finance" viral angle ===
mk("HBH13","How Much You Need to Earn to Buy a Median Home by Metro","The salary needed has doubled in many cities since 2019","MAP","US-metro","Dot map","Housing|Economy|Finance","NAR: Housing Affordability (nar.realtor); Census: Median Home Price (census.gov)",85,90,82,78,82,78,68,85),
mk("HBH14","Average Student Loan Payment as Percent of Take-Home Pay by State","Some states graduates pay 20%+ of net income to loans","MAP","US-state","State choropleth","Finance|Education|Economy","Fed: Student Loan Data (newyorkfed.org); BLS: Average Weekly Earnings (bls.gov)",85,88,78,75,80,78,68,82),
mk("HBH15","Retirement Savings Needed by State to Maintain Lifestyle","From 600K in Mississippi to 2.5M in Hawaii","MAP","US-state","State choropleth","Finance|Economy|Geography","Fidelity: Retirement Planning (fidelity.com); BLS: Consumer Expenditure Survey (bls.gov)",78,85,78,72,72,78,68,78),
# === Science × Geography ===
mk("HBH16","Earthquake Risk Map of the United States","Not just California — the New Madrid zone and Cascadia are overdue","MAP","US-national","Special map","Science|Geography|Infrastructure","USGS: Seismic Hazard Maps (usgs.gov)",72,72,78,78,72,85,65,95),
mk("HBH17","Where Sinkholes Are Most Likely to Swallow Your House","Karst topography and the geology of sudden ground collapse","MAP","US-state","State choropleth","Science|Geography|Housing","USGS: Karst Map (usgs.gov); FEMA: Loss Data (fema.gov)",68,72,72,78,68,80,75,85),
mk("HBH18","Americas Radiation Hotspots","Radon risk zones mapped against average home ventilation","MAP","US-county","County choropleth","Science|Health|Geography","EPA: Radon Zones Map (epa.gov); Census: Housing Characteristics (census.gov)",70,68,72,75,68,80,72,88),
# === Democracy × Economy ===
mk("HBH19","Voter Turnout by Income Bracket","The richer you are the more likely you vote","CHART","US-national","Bar chart","Democracy|Economy|Inequality","Census: CPS Voting Supplement (census.gov)",80,78,82,75,78,65,68,90),
mk("HBH20","Campaign Donations by ZIP Code Income","The wealthiest ZIP codes fund most of American politics","MAP","US-county","County choropleth","Democracy|Economy|Inequality","OpenSecrets: Donor Demographics (opensecrets.org); Census: ACS Income (census.gov)",78,72,72,78,78,78,72,82),
# === "Animated Timeline" showcase ===
mk("HBH21","US Electoral Map Every Presidential Election Since 1856","Animated party flip map showing realignment over 170 years","MAP","US-state","Animated choropleth","Politics|History|Democracy","MIT: Election Lab Historical (electionlab.mit.edu); 270toWin: Historical Maps (270towin.com)",72,68,78,72,68,82,65,95),
mk("HBH22","Global Temperature Anomaly Year by Year Since 1880","The warming stripes rendered as an animated globe","MAP","World","Animated choropleth","Climate|Science|International","NASA: GISS Surface Temperature (data.giss.nasa.gov)",78,68,78,72,78,85,65,95),
mk("HBH23","US Immigration Flows Animated by Decade and Origin","Shifting streams from 1820 to today","CHART","US-national","Animated bar chart","Immigration|History|Demographics","DHS: Yearbook of Immigration (dhs.gov); Census: Historical Foreign-Born (census.gov)",68,65,75,72,65,78,70,90),
# === Environment × Economy ===
mk("HBH24","GDP Lost to Natural Disasters by State Per Year","The growing economic cost of climate events","MAP","US-state","State choropleth","Environment|Economy|Climate","NOAA: Billion-Dollar Disasters (ncei.noaa.gov); BEA: GDP by State (bea.gov)",75,72,78,72,75,78,68,88),
mk("HBH25","States Where Renewable Energy Is Now Cheaper Than Fossil","The crossover is accelerating faster than projections","MAP","US-state","State choropleth","Environment|Energy|Economy","Lazard: LCOE Analysis (lazard.com); EIA: State Energy Profiles (eia.gov)",72,68,78,78,72,78,72,82),
# === "Map Porn" visual-first ideas ===
mk("HBH26","The Age of Every Building in Manhattan","Color-coded block by block from 1765 to present","MAP","US-city","City map","History|Geography|Housing","NYC: PLUTO Dataset (nyc.gov/planning); OpenStreetMap: NYC Buildings",55,58,72,72,50,95,75,90),
mk("HBH27","Every Tree in New York City","875000 trees mapped by species","MAP","US-city","Dot map","Environment|Geography","NYC: Street Tree Census (data.cityofnewyork.us)",50,55,68,72,45,95,72,95),
mk("HBH28","The Commute Map: Where Americans Travel for Work","Origin-destination flows for the 50 largest metros","MAP","US-metro","Line map","Transportation|Economy|Geography","Census: LODES (lehd.ces.census.gov); Census: ACS Commuting (census.gov)",62,75,72,68,58,88,70,90),
# === Inequality deep dives ===
mk("HBH29","The Richest Person in Every State vs. That States Median Income","The ratio ranges from 10000x to over 1000000x","RANK","US-state","Bar chart","Inequality|Economy|Geography","Forbes: Richest in Every State (forbes.com); Census: Median Income (census.gov)",82,78,80,82,78,68,72,85),
mk("HBH30","The Inheritance Gap: Average Inheritance by Race","White families inherit 10x more than Black families on average","CHART","US-national","Bar chart","Inequality|Race|Economy","Fed: Survey of Consumer Finances (federalreserve.gov); Brookings: Inheritance Gap (brookings.edu)",85,78,78,82,82,65,75,80),
mk("HBH31","How Long It Takes to Save a Down Payment by City","Years of savings needed at median income for a median home","RANK","US-city","Bar chart","Inequality|Housing|Economy","Zillow: Home Values (zillow.com/research); Census: Median Income (census.gov); BEA: Personal Savings (bea.gov)",85,90,80,75,80,68,70,82),
# === Technology × International ===
mk("HBH32","Countries That Have Banned or Restricted AI Tools","The emerging global patchwork of AI regulation","MAP","World","World choropleth","Technology|International|Law","Stanford: AI Index (aiindex.stanford.edu); OECD: AI Policy Observatory (oecd.ai)",72,68,72,78,72,78,80,68),
mk("HBH33","Submarine Internet Cable Map of the World","99% of intercontinental data travels through underwater cables","MAP","World","Line map","Technology|International|Infrastructure","TeleGeography: Submarine Cable Map (submarinecablemap.com)",58,55,75,78,55,90,72,90),
mk("HBH34","Satellites Currently in Orbit by Country","Starlink alone outnumbers every other country combined","MAP","World","Dot map","Technology|International|Space","UCS: Satellite Database (ucsusa.org); UN: OOSA Registry (unoosa.org)",62,58,78,80,60,85,72,90),
mk("HBH35","EV Charging Stations Per Capita by Country","The infrastructure gap between leaders and laggards","MAP","World","World choropleth","Technology|International|Energy","IEA: Global EV Outlook (iea.org); AFDC: Station Locator (afdc.energy.gov)",65,68,78,72,62,78,68,85),
]

# --- inject ---
with open(DATA, 'r', encoding='utf-8') as f:
    txt = f.read()
ids = set(re.findall(r'id:"([^"]+)"', txt))
new = [i for i in IDEAS if re.search(r'id:"([^"]+)"', i).group(1) not in ids]
if not new:
    print("All HBH ideas already present"); exit()
tail = "]; // end D"
txt = txt.replace(tail, ",\n".join(new) + ",\n" + tail)
with open(DATA, 'w', encoding='utf-8') as f:
    f.write(txt)
print(f"Injected {len(new)} new ideas (HBH batch)")
