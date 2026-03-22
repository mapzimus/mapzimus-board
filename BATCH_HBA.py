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
# === Religion × Economy ===
mk("HBA01","Churches Per Capita vs. Poverty Rate by County","Do the most religious counties have the most poverty?","XREF","US-county","Scatter plot","Religion|Economy","Census: Religious Congregations (census.gov); Census: SAIPE Poverty Estimates (census.gov)",82,78,75,80,75,70,78,85),
mk("HBA02","The Prosperity Gospel Map","Counties where megachurches cluster vs. median household income","MAP","US-county","County choropleth","Religion|Economy","Kaggle: US Churches Dataset (kaggle.com/datasets/usda-church-data); Census: ACS Income (census.gov)",75,72,70,78,72,80,76,70),
mk("HBA03","Tithing vs. Tax Revenue","States where religious giving exceeds state income tax collected","XREF","US-state","Bar chart","Religion|Economy","IRS: SOI Tax Stats (irs.gov); Giving USA Foundation (givingusa.org)",70,65,72,82,70,65,80,72),
# === Manufacturing × Environment ===
mk("HBA04","Americas Toxic Inheritance","EPA Superfund sites overlaid on shuttered factory locations","MAP","US-county","Dot map","Manufacturing|Environment","EPA: Superfund NPL Sites (epa.gov/superfund); Census: Annual Survey of Manufactures (census.gov)",80,70,72,75,80,85,74,90),
mk("HBA05","The Rust Belt Breathes Again","Air quality improvement in deindustrialized cities since 1990","CHART","US-city","Line chart","Manufacturing|Environment","EPA: Air Quality System (aqs.epa.gov); BLS: QCEW Manufacturing Employment (bls.gov)",72,75,78,70,65,70,72,88),
mk("HBA06","Where Factories Closed and Cancer Rates Dropped","County-level manufacturing decline vs. cancer mortality change","XREF","US-county","Bivariate choropleth","Manufacturing|Environment|Health","CDC: Cancer Statistics (cdc.gov/cancer); Census: County Business Patterns (census.gov)",85,72,68,82,80,80,78,75),
# === Sports × Demographics ===
mk("HBA07","Your Zip Code Predicts Your Sport","Youth sport participation by household income bracket","XREF","US-national","Bar chart","Sports|Demographics","Aspen Institute: State of Play (aspenprojectplay.org); Census: ACS Income (census.gov)",78,85,80,72,68,65,70,80),
mk("HBA08","The Geography of College Football Recruiting","Where Division I football players come from per capita","MAP","US-county","County choropleth","Sports|Demographics|Education","NCAA: Recruiting Database (ncaa.org); Census: Population Estimates (census.gov)",70,75,78,72,60,82,68,78),
mk("HBA09","Baseball Is Dying Where It Was Born","MLB viewership decline mapped against its founding cities","CHART","US-city","Scatter plot","Sports|Demographics|Entertainment","Nielsen: Sports Ratings (nielsen.com); MLB: Historical Attendance (mlb.com)",75,72,70,80,72,68,82,65),
# === Agriculture × International ===
mk("HBA10","Americas Farm Output vs. Entire Countries GDP","US agricultural exports that exceed the GDP of nations","RANK","World","Bar chart","Agriculture|International|Economy","USDA: Agricultural Trade (fas.usda.gov); World Bank: GDP (worldbank.org)",68,72,80,85,65,65,75,92),
mk("HBA11","The World Map of What America Feeds","Countries most dependent on US grain exports","MAP","World","World choropleth","Agriculture|International|Trade","USDA: GATS Export Data (fas.usda.gov); FAO: Food Balance Sheets (fao.org)",72,65,75,78,75,82,70,88),
mk("HBA12","Coffee Belt vs. Coffee Consumption","Where coffee grows vs. where its consumed most per capita","XREF","World","World choropleth","Agriculture|International|Food","ICO: Coffee Trade Statistics (ico.org); Euromonitor: Per Capita Consumption (euromonitor.com)",65,78,82,72,55,80,68,85),
# === Psychology × Technology ===
mk("HBA13","Screen Time vs. Anxiety by Age Group","Hours of daily phone use correlated with self-reported anxiety","XREF","US-national","Scatter plot","Psychology|Technology|Health","Gallup: Wellbeing Index (gallup.com); Pew: Technology Use (pewresearch.org)",85,88,78,72,75,65,70,75),
mk("HBA14","The Loneliness Map of America","Social isolation index by county overlaid with broadband access","MAP","US-county","Bivariate choropleth","Psychology|Technology|Health","HRSA: Social Vulnerability (data.hrsa.gov); FCC: Broadband Map (broadbandmap.fcc.gov)",82,80,70,78,78,80,76,72),
mk("HBA15","Where People Trust AI More Than Doctors","Survey trust scores for AI healthcare vs. physician visits","XREF","World","World choropleth","Psychology|Technology|Health","Ipsos: Global AI Survey (ipsos.com); WHO: Health Workforce (who.int)",75,72,68,85,78,72,82,65),
# === Energy × International ===
mk("HBA16","Who Powers the World and Who Pays","Top energy exporters mapped against their citizens energy costs","XREF","World","World choropleth","Energy|International|Economy","EIA: International Energy (eia.gov); World Bank: Energy Prices (worldbank.org)",72,70,75,80,78,80,72,88),
mk("HBA17","The Renewable Leapfrog","Countries that skipped fossil fuel infrastructure for solar/wind","MAP","World","World choropleth","Energy|International|Technology","IRENA: Renewable Capacity (irena.org); IEA: World Energy Outlook (iea.org)",68,62,72,82,70,78,80,82),
mk("HBA18","Nuclear Power Generation vs. Public Fear of Nuclear","Countries with most nuclear energy vs. anti-nuclear sentiment","XREF","World","Scatter plot","Energy|International|Psychology","IAEA: Nuclear Power Reactors (iaea.org); Ipsos: Global Nuclear Survey (ipsos.com)",70,65,72,85,80,68,82,78),
# === Immigration × Housing ===
mk("HBA19","Where Immigrants Arrive vs. Where Rent Explodes","Immigration inflow ZIP codes overlaid with rent growth","XREF","US-metro","Bivariate choropleth","Immigration|Housing|Economy","Census: ACS Migration (census.gov); HUD: Fair Market Rents (huduser.gov)",78,75,70,72,82,78,70,82),
mk("HBA20","The Refugee Resettlement Rent Map","Cities receiving most refugees vs. their housing vacancy rates","MAP","US-city","Dot map","Immigration|Housing","State Dept: Refugee Processing (state.gov); Census: Housing Vacancies (census.gov)",72,68,72,78,75,78,76,75),
# === Education × Crime ===
mk("HBA21","Every Dollar Spent on Pre-K Saves How Much in Prison","States that invest in early education vs. incarceration cost trajectory","XREF","US-state","Scatter plot","Education|Crime|Economy","NIEER: State of Preschool (nieer.org); BJS: Justice Expenditure (bjs.gov)",85,78,75,80,82,68,78,78),
mk("HBA22","School Funding Per Pupil vs. Juvenile Arrest Rates","Districts with lowest per-pupil spending mapped against youth crime","XREF","US-county","Bivariate choropleth","Education|Crime","Census: School Finance (census.gov); FBI: UCR Juvenile Arrests (fbi.gov)",82,80,72,75,80,78,72,80),
# === Military × Demographics ===
mk("HBA23","Where Americas Soldiers Come From","Military enlistment rates per capita by county","MAP","US-county","County choropleth","Military|Demographics","DoD: Population Representation (militaryonesource.mil); Census: Population (census.gov)",72,78,80,70,65,82,68,88),
mk("HBA24","The Veteran Map of America","Veteran population percentage by county and how its changed since 2000","MAP","US-county","Bivariate choropleth","Military|Demographics|History","Census: ACS Veterans (census.gov); VA: Geographic Distribution (va.gov)",68,72,78,65,60,80,65,90),
# === Media × Politics ===
mk("HBA25","Local News Deserts and Voter Turnout","Counties that lost their local newspaper vs. election participation","XREF","US-county","Bivariate choropleth","Media|Politics|Democracy","UNC: News Desert Project (usnewsdeserts.com); MIT: Election Lab (electionlab.mit.edu)",82,75,72,80,78,78,80,82),
mk("HBA26","Cable News Viewership vs. Political Polarization","Counties with highest Fox/MSNBC viewership vs. straight-ticket voting","XREF","US-county","Scatter plot","Media|Politics","Nielsen: Local TV Ratings (nielsen.com); MIT: Election Lab (electionlab.mit.edu)",78,80,70,72,80,65,75,68),
# === Rural × Infrastructure ===
mk("HBA27","The Last Mile Problem","Rural communities farthest from a hospital ER and their mortality rates","MAP","US-county","Dot map","Rural|Infrastructure|Health","HRSA: Health Professional Shortage Areas (data.hrsa.gov); CDC: WONDER Mortality (wonder.cdc.gov)",85,78,75,72,82,82,70,85),
mk("HBA28","Bridge Conditions in Rural vs. Urban America","Structurally deficient bridges per capita: rural counties vs. metro","XREF","US-county","Bivariate choropleth","Rural|Infrastructure|Transportation","FHWA: National Bridge Inventory (fhwa.dot.gov); Census: Urban-Rural Classification (census.gov)",70,68,78,72,72,78,68,92),
# === Law × Technology ===
mk("HBA29","AI-Generated Evidence in Court Cases Over Time","Timeline of cases involving AI-generated content as evidence","CHART","US-national","Line chart","Law|Technology","Westlaw: Case Law Database (westlaw.com); Stanford: AI Index (aiindex.stanford.edu)",72,65,68,82,78,62,85,58),
mk("HBA30","Facial Recognition Bans vs. Surveillance Spending","Cities that banned facial recognition vs. their police tech budgets","XREF","US-city","Scatter plot","Law|Technology|Crime","ACLU: Community Control (aclu.org); Urban Institute: Police Spending (urban.org)",78,70,70,80,82,68,82,65),
# === Guns × Geography ===
mk("HBA31","Gun Stores Per Capita vs. Gun Deaths Per Capita","Do more gun stores mean more gun deaths? County-level scatter","XREF","US-county","Scatter plot","Guns|Geography|Crime","ATF: Federal Firearms Licensees (atf.gov); CDC: WONDER Firearm Deaths (wonder.cdc.gov)",80,75,78,72,82,68,68,90),
mk("HBA32","Distance to Nearest Gun-Free State","How far every US county is from a state with strict gun laws","MAP","US-county","County choropleth","Guns|Geography|Politics","Giffords: State Scorecard (giffords.org); Census: TIGER Boundaries (census.gov)",68,72,75,78,72,82,80,82),
# === Climate × Agriculture ===
mk("HBA33","The Crop Migration Map","How the ideal growing zones for corn wheat and soybeans have shifted north","MAP","US-state","Animated choropleth","Climate|Agriculture|Science","USDA: Crop Progress (usda.gov); NOAA: Climate Normals (ncei.noaa.gov)",72,68,75,80,78,82,78,85),
mk("HBA34","Drought Frequency vs. Farm Bankruptcy","Counties with increasing drought years overlaid with farm closure rates","XREF","US-county","Bivariate choropleth","Climate|Agriculture|Economy","USDA: Farm Bankruptcies (ers.usda.gov); US Drought Monitor (droughtmonitor.unl.edu)",80,72,70,75,80,78,72,82),
mk("HBA35","Wine Regions That Wont Exist in 2050","Climate projections threatening established wine-growing regions worldwide","MAP","World","World choropleth","Climate|Agriculture|International","Kaggle: Wine Reviews (kaggle.com/datasets/zynicide/wine-reviews); NASA: Climate Projections (climate.nasa.gov)",75,72,68,82,78,80,80,70),
]

# --- inject ---
with open(DATA, 'r', encoding='utf-8') as f:
    txt = f.read()
ids = set(re.findall(r'id:"([^"]+)"', txt))
new = [i for i in IDEAS if re.search(r'id:"([^"]+)"', i).group(1) not in ids]
if not new:
    print("All HBA ideas already present"); exit()
tail = "]; // end D"
txt = txt.replace(tail, ",\n".join(new) + ",\n" + tail)
with open(DATA, 'w', encoding='utf-8') as f:
    f.write(txt)
print(f"Injected {len(new)} new ideas (HBA batch)")
