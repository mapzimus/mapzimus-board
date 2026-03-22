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
# === "Follow the Money" series ===
mk("HBI01","Where US Foreign Aid Actually Goes","Top 25 recipient countries and what categories the money funds","MAP","World","World choropleth","Politics|International|Economy","USAID: Foreign Aid Explorer (explorer.usaid.gov); State Dept: Greenbook (state.gov)",72,68,78,78,72,80,68,92),
mk("HBI02","Lobbying Dollars by Industry Since 1998","Pharma and insurance dwarf every other sector combined","CHART","US-national","Area chart","Politics|Economy|Finance","OpenSecrets: Lobbying Database (opensecrets.org)",78,72,78,78,78,68,68,90),
mk("HBI03","Where Your College Tuition Dollar Goes","Instruction is a shrinking share as admin costs balloon","CHART","US-national","Treemap","Education|Economy|Finance","NCES: IPEDS Finance (nces.ed.gov); Delta Cost Project (deltacostproject.org)",80,85,80,78,75,72,70,85),
mk("HBI04","Police Budget as Percent of City Budget","Some cities spend 40%+ of their general fund on policing","RANK","US-city","Bar chart","Crime|Economy|Politics","Vera Institute: Police Spending (vera.org); Census: Annual Survey of Governments (census.gov)",78,75,78,75,78,65,70,85),
mk("HBI05","How Much Each Country Spends on Education vs. Military","Priorities revealed in a single scatter plot","XREF","World","Scatter plot","Education|Military|International","World Bank: Government Expenditure (worldbank.org); SIPRI: Military Spending (sipri.org)",72,65,80,78,72,68,72,90),
# === Health × Labor ===
mk("HBI06","Workers Without Health Insurance by Occupation","Farmworkers construction and food service are the most exposed","CHART","US-national","Bar chart","Health|Labor|Inequality","Census: ACS Health Insurance by Occupation (census.gov); BLS: OES (bls.gov)",80,82,78,72,78,65,68,88),
mk("HBI07","Workplace Injury Rate by Industry","Logging fishing and roofing top the list every year","RANK","US-national","Bar chart","Health|Labor","BLS: Census of Fatal Occupational Injuries (bls.gov); OSHA: Injury Data (osha.gov)",72,75,80,72,68,65,65,92),
mk("HBI08","Nurse Staffing Ratios by State vs. Patient Outcomes","States that mandate nurse ratios have fewer patient deaths","XREF","US-state","Scatter plot","Health|Labor|Law","CMS: Hospital Compare (data.cms.gov); ANA: Safe Staffing (nursingworld.org)",78,72,72,78,75,65,72,78),
# === Economy × Geography — regional identity ===
mk("HBI09","The Economic Map of Rural vs. Urban America","GDP per capita difference between metro and non-metro counties","MAP","US-county","Bivariate choropleth","Economy|Geography|Rural","BEA: GDP by County (bea.gov); Census: Urban-Rural Classification (census.gov)",75,72,78,72,72,80,68,90),
mk("HBI10","The Most Economically Isolated Counties in America","Counties farthest from any metro area with lowest GDP","MAP","US-county","County choropleth","Economy|Geography|Rural|Infrastructure","BEA: GDP by County (bea.gov); Census: Distance to Metro (census.gov)",72,68,72,78,72,82,75,82),
mk("HBI11","Which States Economies Depend Most on a Single Industry","West Virginia on coal Alaska on oil Nevada on tourism","MAP","US-state","State choropleth","Economy|Geography|Labor","BEA: GDP by Industry by State (bea.gov)",68,72,78,75,65,78,68,88),
# === Demographics × History ===
mk("HBI12","The Great Migration Animated","African American population shift from South to North 1910-1970","MAP","US-state","Animated choropleth","Demographics|History|Race","Census: Historical Census Data (census.gov); Schomburg Center: Migration Data",85,72,72,78,78,82,72,85),
mk("HBI13","White Flight in Real Time","Suburban racial composition change in 20 major metros 1950-2000","MAP","US-metro","Animated choropleth","Demographics|History|Race|Housing","Census: Decennial Census by Tract (census.gov)",82,72,68,78,80,82,72,82),
mk("HBI14","Baby Boom to Baby Bust","US birth rate by year from 1909 to present with major events annotated","CHART","US-national","Area chart","Demographics|History","CDC: Natality Data (cdc.gov); Census: Historical Statistics (census.gov)",72,75,80,72,68,68,65,92),
# === Infrastructure × Health ===
mk("HBI15","Hospital Closures Since 2010 Mapped","Over 130 rural hospitals have closed leaving millions without nearby care","MAP","US-county","Dot map","Infrastructure|Health|Rural","UNC: Cecil Sheps Center (shepscenter.unc.edu); CMS: Provider Data (data.cms.gov)",85,78,72,78,82,82,72,88),
mk("HBI16","Ambulance Response Time by County","Some rural areas wait 45+ minutes for an ambulance","MAP","US-county","County choropleth","Infrastructure|Health|Rural","NEMSIS: EMS Data (nemsis.org); NHTSA: EMS Performance (ems.gov)",82,78,72,78,82,82,72,72),
mk("HBI17","Mental Health Provider Shortage by County","Over 160 million Americans live in mental health professional shortage areas","MAP","US-county","County choropleth","Health|Infrastructure|Psychology","HRSA: HPSA Mental Health (data.hrsa.gov); SAMHSA: Treatment Locator (samhsa.gov)",82,78,75,72,78,80,68,88),
# === Trade × Technology ===
mk("HBI18","Semiconductor Supply Chain Map","Where chips are designed fabricated assembled and consumed globally","MAP","World","Line map","Trade|Technology|International","SIA: Semiconductor Industry Data (semiconductors.org); USITC: Trade Data (usitc.gov)",68,60,72,75,72,85,72,78),
mk("HBI19","Rare Earth Element Mining: Who Controls What","Chinas dominance over the minerals that power modern tech","MAP","World","World choropleth","Trade|Technology|International","USGS: Mineral Commodity Summaries (usgs.gov); IEA: Critical Minerals (iea.org)",72,60,75,80,78,80,72,88),
mk("HBI20","The Global Data Center Map","Where the internet physically lives and who owns it","MAP","World","Dot map","Technology|Infrastructure|International","DataCenterMap: Global Locations (datacentermap.com); Synergy Research (srgresearch.com)",62,58,72,75,60,82,72,82),
# === Gender × Health ===
mk("HBI21","Maternal Mortality Rate by State and Race","Black women die in childbirth at 3x the rate of white women","XREF","US-state","Bar chart","Gender|Health|Race|Inequality","CDC: Pregnancy Mortality Surveillance (cdc.gov); Census: ACS Demographics (census.gov)",90,78,78,80,88,65,72,88),
mk("HBI22","Countries Where Women Cannot Get an Abortion","The global map of reproductive rights restrictions","MAP","World","World choropleth","Gender|Health|International|Law","Center for Reproductive Rights: World Map (reproductiverights.org)",82,72,75,72,80,78,65,88),
mk("HBI23","Heart Attack Misdiagnosis Rate by Gender","Women are 50% more likely to be initially misdiagnosed","CHART","US-national","Bar chart","Gender|Health|Science","AHA: Heart Attack Data (heart.org); JAMA: Sex Differences in Cardiac Care (jamanetwork.com)",82,78,75,82,78,65,78,72),
# === Economy × Education ===
mk("HBI24","Return on Investment by College Major","Lifetime earnings difference between top and bottom majors is 3.4 million","RANK","US-national","Bar chart","Economy|Education|Labor","Georgetown CEW: ROI of College Majors (cew.georgetown.edu); Census: ACS Earnings (census.gov)",78,88,82,75,72,65,68,88),
mk("HBI25","States Where a High School Diploma Still Earns a Living Wage","The map has been shrinking every decade","MAP","US-state","State choropleth","Economy|Education|Labor","BLS: Education and Earnings (bls.gov); MIT: Living Wage Calculator (livingwage.mit.edu)",82,85,78,78,78,78,72,85),
# === Unique multi-dataset combos ===
mk("HBI26","Counties Where Dogs Outnumber Children","Pet ownership rates vs. birth rates by county","XREF","US-county","Bivariate choropleth","Demographics|Children|Geography","AVMA: Pet Ownership Data (avma.org); Census: ACS Under 18 (census.gov)",58,72,75,82,52,78,82,65),
mk("HBI27","The Correlation Between Craft Breweries and Education Level","College-educated metros have 5x more breweries per capita","XREF","US-metro","Scatter plot","Food|Education|Economy","Brewers Association: Brewery Data (brewersassociation.org); Census: ACS Education (census.gov)",55,72,75,80,50,65,78,78),
mk("HBI28","Electric Vehicle Ownership by County vs. Political Lean","EVs cluster in blue counties but the gap is narrowing","XREF","US-county","Bivariate choropleth","Technology|Politics|Energy","IHS Markit: EV Registrations; MIT: Election Lab (electionlab.mit.edu)",68,72,72,78,65,78,75,72),
mk("HBI29","Farmers Market Density vs. Obesity Rate by County","Access to fresh local food maps onto health outcomes","XREF","US-county","Scatter plot","Food|Health|Agriculture","USDA: Farmers Market Directory (ams.usda.gov); CDC: BRFSS Obesity (cdc.gov/brfss)",72,72,72,72,65,68,70,82),
mk("HBI30","Library Visits Per Capita vs. Social Mobility Score","Communities with strong libraries have more upward mobility","XREF","US-county","Scatter plot","Education|Inequality|Infrastructure","IMLS: Public Library Survey (imls.gov); Opportunity Insights: Social Mobility (opportunityinsights.org)",72,68,70,78,68,65,78,75),
# === Remaining gap-fillers ===
mk("HBI31","Daylight Hours by Latitude Animated Through the Year","How sunrise and sunset times create the seasons","MAP","World","Animated choropleth","Science|Geography","NOAA: Solar Calculator (esrl.noaa.gov); US Naval Observatory: Sun Data (aa.usno.navy.mil)",55,58,78,68,48,85,68,92),
mk("HBI32","The Wildfire Risk Map of America","Every property rated for fire danger","MAP","US-county","County choropleth","Climate|Environment|Housing","USFS: Wildfire Risk to Communities (wildfirerisk.org); First Street: Fire Factor (firststreet.org)",75,72,75,72,75,82,68,88),
mk("HBI33","Americas Busiest Truck Routes","Freight volume on every interstate highway","MAP","US-national","Line map","Transportation|Economy|Infrastructure","FHWA: Freight Analysis Framework (fhwa.dot.gov)",58,55,72,68,52,88,65,90),
mk("HBI34","Average Wedding Cost by State","From 15K in Kansas to 95K in Manhattan","MAP","US-state","State choropleth","Economy|Demographics|Geography","The Knot: Real Weddings Survey (theknot.com); Census: ACS (census.gov)",62,78,78,72,55,78,68,72),
mk("HBI35","Dog Breed Popularity by State","The map of which states prefer labs vs. French bulldogs vs. German shepherds","MAP","US-state","State choropleth","Entertainment|Geography|Demographics","AKC: Registration Statistics (akc.org); Google Trends: Pet Searches (trends.google.com)",52,72,75,68,45,78,72,62),
]

# --- inject ---
with open(DATA, 'r', encoding='utf-8') as f:
    txt = f.read()
ids = set(re.findall(r'id:"([^"]+)"', txt))
new = [i for i in IDEAS if re.search(r'id:"([^"]+)"', i).group(1) not in ids]
if not new:
    print("All HBI ideas already present"); exit()
tail = "]; // end D"
txt = txt.replace(tail, ",\n".join(new) + ",\n" + tail)
with open(DATA, 'w', encoding='utf-8') as f:
    f.write(txt)
print(f"Injected {len(new)} new ideas (HBI batch)")
