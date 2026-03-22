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
# === Personal finance viral ===
mk("HBQ01","The Real Cost of Being Poor","Overdraft fees check cashing late penalties and laundromat costs poor people pay that rich people dont","CHART","US-national","Bar chart","Economy|Inequality|Finance","CFPB: Overdraft Data (consumerfinance.gov); FDIC: Unbanked Survey (fdic.gov)",88,85,78,80,82,65,72,82),
mk("HBQ02","Average Daycare Cost vs. Average Rent by State","In most states childcare costs more than housing","XREF","US-state","Scatter plot","Children|Economy|Housing","DOL: Childcare Costs (dol.gov); HUD: Fair Market Rents (huduser.gov)",85,90,78,78,80,68,68,88),
mk("HBQ03","What Minimum Wage Could Buy in 1968 vs. Today","The same hours of work buys dramatically less","CHART","US-national","Bar chart","Economy|History|Prices","DOL: Minimum Wage History (dol.gov); BLS: CPI (bls.gov)",88,88,82,80,82,65,68,92),
mk("HBQ04","Hidden Fees Americans Pay Annually","Resort fees bank fees convenience fees ticket fees — the total is staggering","CHART","US-national","Treemap","Economy|Finance","CFPB: Junk Fees Report (consumerfinance.gov); NerdWallet: Fee Analysis (nerdwallet.com)",78,88,78,78,72,72,72,72),
mk("HBQ05","The Tipping Point: Service Industry Tip Expectations Over Time","From 10% to 20% to the suggested 30% on an iPad","CHART","US-national","Line chart","Economy|Labor|Food","Square: Tipping Data; Pew: Tipping Survey (pewresearch.org)",72,88,78,72,68,65,72,72),
# === International × History ===
mk("HBQ06","Countries That No Longer Exist","Every nation that disappeared in the 20th and 21st centuries mapped","MAP","World","World choropleth","International|History|Politics","CIA: World Factbook Historical; Various Historical Atlases",65,58,78,82,62,82,75,78),
mk("HBQ07","Colonial Empires at Their Greatest Extent","Peak territorial control of every European colonial power overlaid","MAP","World","Animated choropleth","International|History|War","Various: Colonial History Databases; Cambridge Historical Atlas",68,55,72,78,68,88,72,75),
mk("HBQ08","Border Changes in Europe Since 1900","Animated map showing how European borders shifted through two world wars and the Soviet collapse","MAP","World","Animated choropleth","International|History|War","GeaCron: Historical Atlas (geacron.com); Various Historical Atlases",68,58,72,78,68,88,70,78),
# === Health × Technology ===
mk("HBQ09","Telehealth Usage by State Before and After COVID","The pandemic compressed a decade of adoption into months","MAP","US-state","Bivariate choropleth","Health|Technology","CMS: Telehealth Utilization (data.cms.gov); HRSA: Telehealth Data (hrsa.gov)",68,72,78,72,62,78,68,82),
mk("HBQ10","Medical AI Diagnostic Accuracy vs. Human Doctors by Specialty","AI already outperforms in radiology and dermatology","CHART","US-national","Bar chart","Health|Technology|Science","Nature: AI Diagnostic Studies; FDA: AI Device Approvals (fda.gov)",72,68,72,82,72,65,78,65),
# === Crime × Technology ===
mk("HBQ11","Surveillance Camera Density by City","London and Beijing lead but US cities are catching up fast","MAP","World","Bar chart","Crime|Technology|International","Comparitech: Surveillance Data (comparitech.com); ACLU: Surveillance (aclu.org)",72,68,72,78,72,68,72,78),
mk("HBQ12","Cybercrime Losses by State Per Capita","IC3 reported losses mapped — some states lose billions","MAP","US-state","State choropleth","Crime|Technology|Finance","FBI: IC3 Annual Report (ic3.gov); Census: Population (census.gov)",72,72,75,72,68,78,68,85),
# === Environment × Economy ===
mk("HBQ13","The True Cost of a Gallon of Gas Including Externalities","Health climate and infrastructure damage adds 3-6 dollars per gallon","CHART","US-national","Bar chart","Environment|Economy|Energy","IMF: Fossil Fuel Subsidies (imf.org); EPA: Social Cost of Carbon (epa.gov)",72,72,78,82,72,65,78,78),
mk("HBQ14","Cities That Turned Highways Into Parks","Before and after maps of freeway removal projects","MAP","US-city","Special map","Environment|Infrastructure|Transportation","CNU: Freeways Without Futures (cnu.org); Various City Planning Departments",65,68,72,78,62,85,78,68),
# === Education × Race ===
mk("HBQ15","AP Course Availability by School Racial Composition","Majority-minority schools offer fewer Advanced Placement classes","XREF","US-national","Scatter plot","Education|Race|Inequality","ED: Civil Rights Data Collection (ed.gov/ocr); College Board: AP Data (collegeboard.org)",82,75,72,78,80,65,72,82),
mk("HBQ16","School Counselor to Student Ratio by State","Some states have one counselor per 700 students","MAP","US-state","State choropleth","Education|Health|Children","ASCA: School Counselor Data (schoolcounselor.org); NCES: School Staffing (nces.ed.gov)",75,78,78,72,72,78,68,82),
# === Agriculture × Health ===
mk("HBQ17","Antibiotic Use in Livestock vs. Antibiotic Resistance in Humans by Region","80% of antibiotics in the US are used on animals not people","XREF","US-national","Bar chart","Agriculture|Health|Science","FDA: Antimicrobial Sales (fda.gov); CDC: Antibiotic Resistance (cdc.gov/drugresistance)",78,65,72,82,78,65,78,78),
mk("HBQ18","Herbicide Application Map of the US","Where Roundup and other chemicals are sprayed heaviest","MAP","US-county","County choropleth","Agriculture|Environment|Health","USGS: Pesticide National Synthesis (usgs.gov)",72,62,72,72,72,82,68,88),
# === Labor × Race ===
mk("HBQ19","Unemployment Rate by Race in Every State","The gap persists everywhere but varies wildly by geography","XREF","US-state","Bar chart","Labor|Race|Inequality","BLS: LAUS by Race (bls.gov); Census: ACS Employment (census.gov)",80,75,78,72,78,68,68,88),
mk("HBQ20","Occupational Segregation: Which Jobs Are Most Racially Segregated","Some professions remain over 90% one race","CHART","US-national","Bar chart","Labor|Race|Inequality","BLS: CPS Race and Employment (bls.gov); Census: ACS Occupation by Race (census.gov)",78,72,75,78,78,65,72,85),
# === Inequality × Geography ===
mk("HBQ21","The Most Unequal Block in America","Census blocks where the richest and poorest ZIP codes are physically adjacent","MAP","US-city","City map","Inequality|Geography|Housing","Census: ACS Block Group Income (census.gov); Zillow: Home Values (zillow.com/research)",82,78,68,82,80,85,80,78),
mk("HBQ22","Social Mobility Score by County","Where you grow up determines your odds of moving up more than talent","MAP","US-county","County choropleth","Inequality|Geography|Economy","Opportunity Insights: Mobility Data (opportunityinsights.org)",82,78,75,78,78,80,72,85),
# === Climate × Science ===
mk("HBQ23","CO2 Concentration Over 800000 Years","Ice core data shows were in completely uncharted territory","CHART","World","Line chart","Climate|Science|History","NOAA: Ice Core Data (ncei.noaa.gov); Scripps: Keeling Curve (scripps.ucsd.edu)",78,62,78,82,78,68,68,92),
mk("HBQ24","Ocean Acidification Rate by Region","The other CO2 problem thats dissolving coral reefs","MAP","World","World choropleth","Climate|Science|Environment","NOAA: Ocean Acidification (pmel.noaa.gov); IPCC: Ocean Chapter (ipcc.ch)",72,58,72,78,75,78,72,82),
# === War × International ===
mk("HBQ25","Active Conflicts on Earth Right Now","There are more ongoing wars today than at any point since WWII","MAP","World","Dot map","War|International","UCDP: Armed Conflict Dataset (ucdp.uu.se); ACLED: Conflict Data (acleddata.com)",78,62,75,78,80,82,68,88),
mk("HBQ26","Arms Exports by Country","Who is selling weapons to whom","MAP","World","Line map","War|International|Trade","SIPRI: Arms Transfers (sipri.org); WMEAT: Arms Deliveries (state.gov)",72,60,75,78,75,82,68,88),
# === Poverty × Education ===
mk("HBQ27","Free and Reduced Lunch Rate by School vs. Test Scores","The single strongest predictor of academic performance isnt teaching quality","XREF","US-national","Scatter plot","Poverty|Education","USDA: School Lunch Data (fns.usda.gov); NAEP: School Level Results (nces.ed.gov)",82,78,78,75,78,65,68,88),
mk("HBQ28","Summer Learning Loss by Family Income","Poor kids lose 2 months of reading progress every summer while rich kids gain","CHART","US-national","Bar chart","Poverty|Education|Children|Inequality","NWEA: MAP Growth Data (nwea.org); RAND: Summer Learning Research (rand.org)",82,78,78,78,78,65,72,75),
# === Fun geography ===
mk("HBQ29","Every Starbucks vs. Every Library in America","Coffee wins in cities but libraries still dominate rural America","MAP","US-national","Dot map","Food|Education|Geography","ScrapeHero: Starbucks Locations; IMLS: Public Library Survey (imls.gov)",58,78,78,72,50,82,72,78),
mk("HBQ30","Americans Within Walking Distance of a Park","The green space equity map","MAP","US-city","City map","Environment|Geography|Health","TPL: ParkServe (tpl.org); Census: ACS (census.gov)",68,72,75,68,62,82,68,82),
mk("HBQ31","The Speed Trap Map of America","Towns where traffic ticket revenue exceeds 10% of the municipal budget","MAP","US-national","Dot map","Crime|Economy|Geography","Governing: Fine and Fee Revenue; Census: Government Finance (census.gov)",68,78,72,78,68,78,78,68),
mk("HBQ32","Counties Where The Nearest Trauma Center Is Over an Hour Away","The golden hour map of Americas healthcare gaps","MAP","US-county","County choropleth","Health|Infrastructure|Rural","ACS: Trauma Center Locations (facs.org); Census: County Geography (census.gov)",82,75,72,78,80,82,72,78),
mk("HBQ33","The Geriatric Time Bomb Map","Counties where 30%+ of the population will be over 65 by 2035","MAP","US-county","County choropleth","Demographics|Health|Economy","Census: Population Projections (census.gov); HHS: Aging Data (acl.gov)",75,72,75,78,75,80,72,82),
mk("HBQ34","Americas Cultural Divide in One Map","Counties sorted by the ratio of churches to bars","MAP","US-county","Bivariate choropleth","Religion|Geography|Demographics","Census: County Business Patterns NAICS (census.gov); ARDA: Religious Congregations (thearda.com)",58,72,72,80,58,78,80,75),
mk("HBQ35","Every Country Scaled by Population Instead of Land Area","The cartogram that reshapes your mental model of the world","MAP","World","Special map","Demographics|International|Geography","UN: World Population (population.un.org); Worldmapper (worldmapper.org)",58,60,78,85,52,85,78,90),
]

# --- inject ---
with open(DATA, 'r', encoding='utf-8') as f:
    txt = f.read()
ids = set(re.findall(r'id:"([^"]+)"', txt))
new = [i for i in IDEAS if re.search(r'id:"([^"]+)"', i).group(1) not in ids]
if not new:
    print("All HBQ ideas already present"); exit()
tail = "]; // end D"
txt = txt.replace(tail, ",\n".join(new) + ",\n" + tail)
with open(DATA, 'w', encoding='utf-8') as f:
    f.write(txt)
print(f"Injected {len(new)} new ideas (HBQ batch)")
