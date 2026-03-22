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
# === "Your State vs. a Country" series ===
mk("HBD01","Every US State Matched to a Country by Murder Rate","Texas matches Brazil and Vermont matches Norway","MAP","US-state","State choropleth","Crime|International|Geography","FBI: UCR Crime Data (fbi.gov); UNODC: Homicide Statistics (unodc.org)",78,75,80,82,72,78,72,88),
mk("HBD02","Every US State Matched to a Country by Life Expectancy","Mississippi matches El Salvador and Hawaii matches Japan","MAP","US-state","State choropleth","Health|International|Geography","CDC: WONDER Life Expectancy (wonder.cdc.gov); WHO: Life Tables (who.int)",82,78,80,82,78,78,72,90),
mk("HBD03","Every US State Matched to a Country by CO2 Emissions","Wyoming matches Qatar per capita","MAP","US-state","State choropleth","Climate|International|Energy","EIA: State Energy CO2 (eia.gov); Global Carbon Project: National Emissions (globalcarbonproject.org)",72,65,78,85,72,78,75,88),
mk("HBD04","Every US State Matched to a Country by Population Density","New Jersey matches India and Alaska matches Mongolia","MAP","US-state","State choropleth","Demographics|International|Geography","Census: Population Density (census.gov); World Bank: Population (worldbank.org)",60,68,82,78,55,78,70,95),
# === Infrastructure × Economy ===
mk("HBD05","Americas Most Expensive Bridge Repairs Per Driver","Cost of deferred bridge maintenance divided by registered vehicles","RANK","US-state","Bar chart","Infrastructure|Economy|Transportation","ASCE: Infrastructure Report Card (infrastructurereportcard.org); FHWA: Highway Statistics (fhwa.dot.gov)",72,78,78,72,72,65,68,88),
mk("HBD06","Water Main Break Rate by City vs. Water Bill","Crumbling pipes correlate with higher costs passed to consumers","XREF","US-city","Scatter plot","Infrastructure|Economy","AWWA: Water Utility Benchmarking (awwa.org); Circle of Blue: Water Pricing (circleofblue.org)",75,78,72,72,75,65,72,72),
mk("HBD07","Internet Speed vs. Price Paid in Every Country","Americans pay more for slower internet than most developed nations","XREF","World","Scatter plot","Infrastructure|Technology|International","Ookla: Speedtest Global Index (speedtest.net); Cable.co.uk: Broadband Pricing (cable.co.uk)",78,82,80,78,72,68,70,88),
# === "Before and After" time comparisons ===
mk("HBD08","Amazon Warehouses Then and Now","County map of Amazon fulfillment centers 2010 vs. 2024","MAP","US-county","Dot map","Economy|Technology|Labor","MWPVL: Amazon Distribution Network (mwpvl.com); Census: County Business Patterns (census.gov)",72,75,78,75,68,80,72,82),
mk("HBD09","Downtown Office Vacancy Before and After COVID","Satellite-view comparison of business district activity","CHART","US-city","Bar chart","Economy|Housing|Health","CoStar: Office Vacancy (costar.com); Kastle: Back to Work Barometer (kastle.com)",78,82,78,72,72,70,70,78),
mk("HBD10","US Manufacturing Employment 1980 vs. Today","The same map 40 years apart tells the story of deindustrialization","MAP","US-county","County choropleth","Manufacturing|History|Labor","BLS: QCEW Manufacturing (bls.gov); Census: County Business Patterns (census.gov)",78,72,78,78,78,80,70,92),
# === "The Disappearing" series ===
mk("HBD11","The Disappearing Family Farm","Number of farms under 500 acres by decade since 1950","CHART","US-national","Area chart","Agriculture|History|Economy","USDA: Census of Agriculture (nass.usda.gov)",80,72,78,75,78,70,72,92),
mk("HBD12","The Disappearing Shopping Mall","Malls closed or dying overlaid on county population growth","MAP","US-county","Dot map","Economy|Demographics|History","Deadmalls.com; Census: Population Estimates (census.gov)",72,78,75,72,68,78,72,68),
mk("HBD13","The Disappearing Public Pool","Municipal pools per capita by decade from 1970 to today","CHART","US-national","Line chart","Infrastructure|History|Race","Census of Governments: Recreation (census.gov); Jeff Wiltse Historical Data",78,75,72,78,72,68,78,62),
# === Education × International ===
mk("HBD14","Teacher Salary vs. Student Performance by Country","Some of the best-performing countries pay teachers the most — some dont","XREF","World","Scatter plot","Education|International|Labor","OECD: Education at a Glance (oecd.org); PISA: Results Database (oecd.org/pisa)",75,72,78,78,72,68,72,88),
mk("HBD15","College Degree Holders Per Capita: US States vs. Countries","US states with lowest college rates match developing nations","XREF","US-state","Bar chart","Education|International|Demographics","Census: ACS Educational Attainment (census.gov); World Bank: Education Data (worldbank.org)",70,72,78,80,68,65,72,90),
# === Crime × Housing ===
mk("HBD16","Eviction Rate by ZIP Code Overlaid With Arrest Rates","Housing instability mapped against criminal justice contact","XREF","US-county","Bivariate choropleth","Crime|Housing|Poverty","Eviction Lab: Eviction Data (evictionlab.org); FBI: UCR Crime Data (fbi.gov)",82,78,68,75,80,78,75,75),
mk("HBD17","Property Crime Rate vs. Housing Inequality Within Metros","The Gini coefficient of home values predicts property crime","XREF","US-metro","Scatter plot","Crime|Housing|Inequality","FBI: UCR Crime Data (fbi.gov); Census: ACS Home Value (census.gov)",75,70,68,78,75,65,78,78),
# === Food × History ===
mk("HBD18","Americas Diet by Decade","What the average American ate in 1900 vs 1950 vs 2000 vs today","CHART","US-national","Area chart","Food|History|Health","USDA: Loss-Adjusted Food Availability (ers.usda.gov)",72,80,78,72,62,68,70,90),
mk("HBD19","The Great American Sugar Increase","Per capita sugar consumption timeline from 1820 to present","CHART","US-national","Line chart","Food|History|Health","USDA: Sugar and Sweeteners Yearbook (ers.usda.gov)",75,78,80,72,72,65,68,92),
mk("HBD20","How Far Your Thanksgiving Dinner Traveled","Average miles each ingredient travels to reach your plate","MAP","US-national","Special map","Food|Transportation|Agriculture","USDA: Food Miles (leopold.iastate.edu); USDA: Agricultural Statistics (usda.gov)",65,78,75,72,55,82,78,70),
# === War × Economy ===
mk("HBD21","US Military Spending vs. Next 10 Countries Combined","The bar chart that puts defense spending in perspective","CHART","World","Bar chart","War|Economy|Military","SIPRI: Military Expenditure (sipri.org)",72,68,82,78,72,68,62,95),
mk("HBD22","Veterans Unemployment Rate vs. Civilian by State","Which states fail their veterans economically","XREF","US-state","Scatter plot","War|Economy|Military|Labor","BLS: Veterans Employment (bls.gov); VA: Geographic Data (va.gov)",78,75,78,70,72,65,68,88),
mk("HBD23","The Economic Boom After Every Major US War","GDP growth in the 5 years following each conflict","CHART","US-national","Bar chart","War|Economy|History","BEA: Historical GDP (bea.gov); NBER: Business Cycle Dates (nber.org)",68,62,75,78,65,65,75,88),
# === Immigration × Labor ===
mk("HBD24","Industries Most Dependent on Immigrant Labor","Share of foreign-born workers by sector from farming to tech","CHART","US-national","Bar chart","Immigration|Labor|Economy","BLS: Foreign-Born Workers (bls.gov); Census: ACS Nativity (census.gov)",75,72,80,72,72,68,68,92),
mk("HBD25","H-1B Visa Holders by Metro Area","Tech hubs vs. everywhere else — the concentration is extreme","MAP","US-metro","Dot map","Immigration|Labor|Technology","USCIS: H-1B Employer Data (uscis.gov)",68,70,78,72,65,78,68,90),
# === "Global Divide" maps ===
mk("HBD26","Countries Where Most People Have Never Flown on a Plane","Air travel is still a luxury for most of humanity","MAP","World","World choropleth","International|Inequality|Transportation","ICAO: Air Transport Statistics (icao.int); Gallup: World Poll (gallup.com)",78,72,72,82,72,78,80,68),
mk("HBD27","Countries Where the Average Person Has Never Used the Internet","The digital divide is wider than you think","MAP","World","World choropleth","International|Technology|Inequality","ITU: ICT Facts and Figures (itu.int); World Bank: Internet Users (worldbank.org)",75,70,78,80,72,78,75,88),
mk("HBD28","Access to Clean Water by Country","A basic human need that 2 billion people still lack","MAP","World","World choropleth","International|Health|Inequality","WHO/UNICEF: JMP Data (washdata.org)",82,72,80,72,78,80,65,90),
# === Environment × Politics ===
mk("HBD29","Congressional Districts That Flood vs. How Their Rep Voted on Climate Bills","Voting against climate action while your district drowns","XREF","US-state","Bivariate choropleth","Environment|Politics|Climate","FEMA: National Flood Insurance (fema.gov); GovTrack: Roll Call Votes (govtrack.us)",82,72,68,82,85,78,80,75),
mk("HBD30","EPA Superfund Sites in Republican vs. Democratic Districts","Toxic waste is bipartisan but cleanup funding isnt","XREF","US-state","Bar chart","Environment|Politics","EPA: Superfund NPL (epa.gov/superfund); Census: Congressional Districts (census.gov)",75,68,70,78,78,68,78,82),
# === Sports × Economy ===
mk("HBD31","Stadium Subsidy Per Resident by City","What your city paid for a billionaires playground","RANK","US-city","Bar chart","Sports|Economy|Infrastructure","Brookings: Sports Subsidies (brookings.edu); Census: City Population (census.gov)",78,82,78,75,78,65,72,75),
mk("HBD32","Olympic Medal Count vs. GDP","Money buys medals — the near-perfect correlation","XREF","World","Scatter plot","Sports|Economy|International","IOC: Medal Database (olympics.com); World Bank: GDP (worldbank.org)",68,65,80,72,58,68,68,92),
# === "TikTok Bait" shareable format ===
mk("HBD33","Every Country the US Has Sanctioned","The map is more red than you think","MAP","World","World choropleth","Politics|International|Trade","Treasury: OFAC Sanctions List (treasury.gov/ofac); Congressional Research Service (crs.gov)",72,62,78,80,75,82,72,88),
mk("HBD34","How Many Hours You Need to Work at Minimum Wage to Afford a 1BR Apartment","By state — not a single state is affordable at 40 hours","MAP","US-state","State choropleth","Housing|Economy|Labor|Inequality","NLIHC: Out of Reach (nlihc.org); DOL: Minimum Wage (dol.gov)",90,92,82,78,85,78,68,90),
mk("HBD35","Countries Where Being Gay Is Still a Crime","The map of legality vs. criminalization updated to 2024","MAP","World","World choropleth","International|Law|Gender","ILGA: Sexual Orientation Laws (ilga.org)",82,72,78,78,80,80,65,90),
]

# --- inject ---
with open(DATA, 'r', encoding='utf-8') as f:
    txt = f.read()
ids = set(re.findall(r'id:"([^"]+)"', txt))
new = [i for i in IDEAS if re.search(r'id:"([^"]+)"', i).group(1) not in ids]
if not new:
    print("All HBD ideas already present"); exit()
tail = "]; // end D"
txt = txt.replace(tail, ",\n".join(new) + ",\n" + tail)
with open(DATA, 'w', encoding='utf-8') as f:
    f.write(txt)
print(f"Injected {len(new)} new ideas (HBD batch)")
