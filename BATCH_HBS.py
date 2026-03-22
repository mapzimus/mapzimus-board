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
# === "The Hidden Tax" series — costs people don't realize they're paying ===
mk("HBS01","The Commute Tax: Annual Cost of Getting to Work by Metro","Gas tolls parking transit passes and vehicle depreciation combined","RANK","US-metro","Bar chart","Transportation|Economy|Labor","AAA: Driving Costs (aaa.com); Census: ACS Commuting (census.gov); APTA: Transit Costs (apta.com)",78,88,78,72,72,65,70,82),
mk("HBS02","The Obesity Tax: How Much Extra Overweight Americans Spend on Healthcare","Annual medical spending difference between healthy weight and obese adults","CHART","US-national","Bar chart","Health|Economy|Food","CDC: Obesity Cost Data (cdc.gov/obesity); Milken Institute: Obesity Costs",78,80,78,75,72,65,68,82),
mk("HBS03","The Single Tax: How Much More It Costs to Live Alone","Per-person housing utilities and food costs for singles vs. couples","CHART","US-national","Bar chart","Economy|Demographics|Housing","BLS: Consumer Expenditure Survey (bls.gov); Census: ACS Household Type (census.gov)",72,85,78,72,65,65,72,82),
mk("HBS04","The Pink Tax vs. The Bachelor Tax","Gender-based pricing disadvantages mapped side by side","CHART","US-national","Bar chart","Gender|Economy|Prices","NYC DCA: Gender Pricing Study (nyc.gov); BLS: CPI (bls.gov)",75,80,75,78,72,65,78,72),
mk("HBS05","The Rural Penalty: Extra Costs of Living Far From a City","Higher gas prices fewer shopping options more expensive insurance","MAP","US-county","County choropleth","Rural|Economy|Geography","USDA: Rural-Urban Cost Differences (ers.usda.gov); BEA: Regional Price Parities (bea.gov)",75,75,72,72,68,78,72,78),
# === Housing × International ===
mk("HBS06","Average Square Footage Per Person by Country","Americans have 3x the living space of Japanese residents","RANK","World","Bar chart","Housing|International","OECD: Housing Conditions (oecd.org); Various National Statistical Offices",62,72,80,78,55,65,68,82),
mk("HBS07","Homeless Population Per Capita by Country","The US ranks worse than most of Europe","RANK","World","Bar chart","Housing|International|Poverty","OECD: Homelessness Data (oecd.org); HUD: Annual Homeless Assessment (huduser.gov)",78,72,78,78,78,65,68,78),
mk("HBS08","Countries Where Foreign Investors Own the Most Housing","When global capital treats homes as assets not shelter","MAP","World","World choropleth","Housing|International|Finance","OECD: Foreign Investment (oecd.org); Various National Land Registries",72,72,72,78,72,78,72,70),
# === Crime × Health ===
mk("HBS09","Gun Violence as a Public Health Crisis Map","Firearm injuries and deaths visualized like a disease outbreak","MAP","US-county","County choropleth","Crime|Health|Guns","CDC: WONDER Firearm Injuries (wonder.cdc.gov); Everytown: Gun Violence (everytown.org)",82,75,72,72,82,80,70,88),
mk("HBS10","Incarceration and Life Expectancy","Counties with highest incarceration rates have lowest life expectancy","XREF","US-county","Scatter plot","Crime|Health|Inequality","BJS: Incarceration Data (bjs.gov); CDC: WONDER Life Expectancy (wonder.cdc.gov)",82,72,70,78,80,65,72,82),
mk("HBS11","ER Visits Due to Violence by City","Assault-related emergency room visits per capita mapped","MAP","US-city","Dot map","Crime|Health","HCUP: Emergency Department Data (ahrq.gov); FBI: UCR Violent Crime (fbi.gov)",75,72,72,72,75,78,68,78),
# === Trade × Climate ===
mk("HBS12","Carbon Footprint of Imported Goods by Country of Origin","Cheap products from coal-powered factories carry hidden emissions","XREF","World","World choropleth","Trade|Climate|International","Global Carbon Project: Trade Emissions; OECD: CO2 Embodied in Trade (oecd.org)",72,62,72,78,72,78,75,78),
mk("HBS13","Food Miles by Product Type","Avocados travel 2000 miles but local lettuce travels 50","CHART","US-national","Bar chart","Trade|Food|Climate","USDA: Food Miles (ers.usda.gov); Leopold Center: Local Food (leopold.iastate.edu)",62,72,78,72,55,65,68,78),
# === Education × Health ===
mk("HBS14","School Start Times vs. Teen Car Crash Rates","Later start times correlate with fewer teen driving accidents","XREF","US-state","Scatter plot","Education|Health|Children|Transportation","CDC: Teen Motor Vehicle Crashes (cdc.gov); Start School Later (startschoollater.net)",72,78,72,80,68,65,78,72),
mk("HBS15","Recess Minutes Per Day by State","Some states mandate zero minutes of recess","MAP","US-state","State choropleth","Education|Health|Children","CDC: School Health Policies (cdc.gov/healthyyouth); Playworks: Recess Data (playworks.org)",72,78,78,72,68,78,68,72),
# === Military × Economy ===
mk("HBS16","Defense Contractor Revenue by Congressional District","The military-industrial complex mapped at the district level","MAP","US-state","County choropleth","Military|Economy|Politics","USASpending: Defense Contracts (usaspending.gov); DoD: Contract Data (defense.gov)",75,68,72,78,78,80,72,85),
mk("HBS17","Economic Impact of Military Base Closures","What happened to communities that lost their base during BRAC rounds","MAP","US-national","Dot map","Military|Economy|History","GAO: BRAC Reports (gao.gov); BEA: Regional Economic Accounts (bea.gov)",72,68,72,78,72,78,72,78),
# === Environment × Crime ===
mk("HBS18","Illegal Dumping Sites Mapped Against Poverty Rate","Who bears the burden of environmental crime","MAP","US-county","Bivariate choropleth","Environment|Crime|Poverty","EPA: Illegal Dumping Data (epa.gov); Census: SAIPE (census.gov)",78,68,68,72,78,78,72,68),
mk("HBS19","Wildlife Trafficking Routes","The 23 billion dollar illegal wildlife trade mapped globally","MAP","World","Line map","Environment|Crime|International","TRAFFIC: Wildlife Trade (traffic.org); UNODC: Wildlife Crime (unodc.org)",72,55,68,78,72,82,72,75),
# === Labor × Housing ===
mk("HBS20","Average Wage Needed to Afford a 2BR Apartment by County","The gap between actual wages and housing costs mapped","MAP","US-county","County choropleth","Labor|Housing|Inequality","NLIHC: Out of Reach (nlihc.org); BLS: QCEW Wages (bls.gov)",88,90,78,75,82,80,68,88),
mk("HBS21","The Commute Sacrifice Zone","Workers who commute 90+ minutes each way because they cant afford to live closer","MAP","US-metro","Dot map","Labor|Housing|Transportation","Census: ACS Extreme Commuters (census.gov)",80,82,72,78,78,78,72,82),
# === Science × Economy ===
mk("HBS22","Federal Research Funding by University","The top 20 schools receive as much as the bottom 500 combined","RANK","US-national","Bar chart","Science|Economy|Education","NSF: Higher Education R&D (nsf.gov); NIH: Reporter (reporter.nih.gov)",68,65,78,78,68,65,68,90),
mk("HBS23","Patent Applications Per Capita by Country","Innovation hubs mapped globally","MAP","World","World choropleth","Science|Economy|Technology","WIPO: IP Statistics (wipo.int); World Bank: Population (worldbank.org)",62,58,78,72,58,78,65,90),
# === Politics × International ===
mk("HBS24","Freedom of Press Index vs. GDP Per Capita","Economic development and press freedom are linked but not perfectly","XREF","World","Scatter plot","Politics|International|Media","RSF: Press Freedom Index (rsf.org); World Bank: GDP Per Capita (worldbank.org)",68,60,75,78,68,68,68,88),
mk("HBS25","Corruption Perception Index Mapped","The global map of how corrupt governments are perceived to be","MAP","World","World choropleth","Politics|International|Economy","Transparency International: CPI (transparency.org)",68,62,78,72,68,78,62,92),
# === Demographics × Economy ===
mk("HBS26","The Two Americas: Counties Gaining Population vs. Losing It","A nation splitting into growing metros and emptying rural areas","MAP","US-county","Bivariate choropleth","Demographics|Economy|Geography","Census: Population Estimates Components of Change (census.gov)",75,72,78,72,72,82,68,92),
mk("HBS27","Where Young People Are Moving and Where They Are Leaving","Net migration of 25-34 year olds by metro","MAP","US-metro","Bivariate choropleth","Demographics|Economy|Housing","Census: ACS Migration by Age (census.gov); IRS: SOI Migration (irs.gov)",78,78,75,72,72,80,72,85),
# === Food × Economy ===
mk("HBS28","Restaurant Workers Who Cant Afford to Eat at Their Own Restaurant","Wage vs. average entree price at major chain restaurants","CHART","US-national","Bar chart","Food|Economy|Labor|Inequality","BLS: OES Food Service (bls.gov); Glassdoor: Restaurant Worker Pay (glassdoor.com)",82,85,78,80,78,65,78,72),
mk("HBS29","Grocery Store Price Disparity Between Poor and Rich Neighborhoods","The same items cost more in food deserts than in affluent areas","XREF","US-city","Bar chart","Food|Economy|Inequality|Poverty","USDA: Food Access Research (ers.usda.gov); Feeding America: Food Price Data (feedingamerica.org)",82,80,75,78,78,65,72,72),
# === History × Geography ===
mk("HBS30","Every State Capital and Why It Was Chosen","Most capitals arent the biggest city and the reasons are fascinating","MAP","US-state","Dot map","History|Geography|Politics","Various: State Capital History; Census: City Population Historical (census.gov)",55,68,78,78,48,78,72,82),
mk("HBS31","The Trail of Tears Mapped With Modern State Borders","The forced removal routes overlaid on todays geography","MAP","US-national","Line map","History|Race|Geography","NPS: Trail of Tears (nps.gov); Smithsonian: Native American History (si.edu)",85,68,72,78,82,85,72,78),
mk("HBS32","Sundown Towns in America","Communities that historically excluded Black residents mapped","MAP","US-national","Dot map","History|Race|Geography","James Loewen: Sundown Towns Database; Various Historical Sources",85,68,68,82,85,82,78,72),
# === Technology × Health ===
mk("HBS33","Average Screen Time by Country","South Koreans lead at 8+ hours per day","MAP","World","World choropleth","Technology|Health|International","DataReportal: Digital Reports (datareportal.com); WHO: Digital Health (who.int)",65,78,78,72,58,78,65,78),
mk("HBS34","Hearing Loss Rates in Young People vs. Headphone Usage","The generation growing up with earbuds is losing hearing earlier","CHART","US-national","Line chart","Technology|Health|Demographics","NIDCD: Hearing Data (nidcd.nih.gov); CDC: Hearing Loss (cdc.gov)",72,78,72,78,72,65,72,68),
mk("HBS35","Social Media Usage Hours vs. Self-Reported Depression by Age","The J-curve relationship between scrolling and sadness","XREF","US-national","Scatter plot","Technology|Health|Psychology","Pew: Social Media Use (pewresearch.org); NIH: Adolescent Mental Health (nimh.nih.gov)",80,82,72,78,78,65,72,72),
]

# --- inject ---
with open(DATA, 'r', encoding='utf-8') as f:
    txt = f.read()
ids = set(re.findall(r'id:"([^"]+)"', txt))
new = [i for i in IDEAS if re.search(r'id:"([^"]+)"', i).group(1) not in ids]
if not new:
    print("All HBS ideas already present"); exit()
tail = "]; // end D"
txt = txt.replace(tail, ",\n".join(new) + ",\n" + tail)
with open(DATA, 'w', encoding='utf-8') as f:
    f.write(txt)
print(f"Injected {len(new)} new ideas (HBS batch)")
