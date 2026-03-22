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
# === "The Debate Starter" — polarizing data that forces discussion ===
mk("HBL01","Does the Death Penalty Deter Murder","States with vs. without capital punishment and their murder rates","XREF","US-state","Bar chart","Crime|Law|Politics","FBI: UCR Murder Rates (fbi.gov); Death Penalty Information Center (deathpenaltyinfo.org)",78,72,78,78,82,65,72,88),
mk("HBL02","Universal Healthcare Countries vs. US on Every Health Metric","Life expectancy infant mortality preventable deaths — the US loses on all","XREF","World","Bar chart","Health|International|Politics","WHO: World Health Statistics (who.int); OECD: Health Data (oecd.org)",85,78,82,78,82,68,68,92),
mk("HBL03","States With More Guns vs. States With More Gun Deaths","The correlation is stronger than the debate suggests","XREF","US-state","Scatter plot","Guns|Health|Politics","ATF: Firearms in Commerce (atf.gov); CDC: WONDER Firearm Deaths (wonder.cdc.gov)",80,75,78,72,82,65,68,90),
mk("HBL04","Immigration Rate vs. GDP Growth in Developed Countries","Countries with more immigration tend to grow faster","XREF","World","Scatter plot","Immigration|Economy|International","OECD: International Migration (oecd.org); World Bank: GDP Growth (worldbank.org)",72,68,78,82,72,68,78,85),
mk("HBL05","Union Membership Rate vs. Middle Class Income Share by Decade","They track each other almost perfectly since 1950","XREF","US-national","Line chart","Labor|Economy|Inequality|History","BLS: Union Membership (bls.gov); Census: Income Distribution (census.gov)",80,78,78,82,78,68,72,90),
# === Poverty × International ===
mk("HBL06","Child Poverty Rate: US vs. Peer Nations","The richest country has among the highest child poverty in the developed world","RANK","World","Bar chart","Poverty|International|Children","UNICEF: Innocenti Report Card (unicef.org); OECD: Income Distribution (oecd.org)",85,78,80,82,82,65,70,88),
mk("HBL07","The Map of Global Extreme Poverty Over Time","From 90% in 1820 to under 10% today — humanitys greatest achievement","CHART","World","Animated choropleth","Poverty|International|History","World Bank: PovcalNet (worldbank.org); OWID: Global Extreme Poverty (ourworldindata.org)",78,62,78,78,72,82,68,90),
mk("HBL08","Poverty Rate by Family Structure in America","Single-parent households face poverty at 5x the rate of married couples","CHART","US-national","Bar chart","Poverty|Demographics|Gender","Census: ACS Poverty by Household Type (census.gov)",78,80,80,72,75,65,65,90),
# === Crime × International ===
mk("HBL09","Recidivism Rate by Country: Who Actually Rehabilitates","Norways 20% vs. Americas 76% tells you everything","RANK","World","Bar chart","Crime|International|Law","World Prison Brief (prisonstudies.org); BJS: Recidivism Data (bjs.gov)",78,72,78,82,78,65,72,82),
mk("HBL10","Police Officers Per Capita by Country vs. Crime Rate","More police doesnt always mean less crime","XREF","World","Scatter plot","Crime|International","UNODC: Criminal Justice Data (unodc.org); Interpol: Statistics (interpol.int)",68,62,75,80,68,65,78,82),
# === Housing × History ===
mk("HBL11","Average Home Size in America by Decade","From 983 sq ft in 1950 to 2480 sq ft today as family size shrank","CHART","US-national","Area chart","Housing|History|Demographics","Census: Characteristics of New Housing (census.gov)",68,78,80,78,62,68,68,90),
mk("HBL12","Homeownership Rate by Generation at Same Age","Each generation owns less at every comparable age","CHART","US-national","Line chart","Housing|History|Demographics|Inequality","Census: CPS Housing Vacancies (census.gov); Urban Institute: Generational Housing (urban.org)",85,85,78,78,82,68,72,82),
# === "The Timeline" — long-range historical data ===
mk("HBL13","World Population Growth Animated From Year 1 to 2024","From 200 million to 8 billion in one visualization","CHART","World","Area chart","Demographics|History|International","UN: World Population Prospects (population.un.org); OWID: World Population (ourworldindata.org)",68,62,80,75,65,72,65,92),
mk("HBL14","Global GDP Distribution Shift: 1500 to Today","China and India dominated for centuries then Europe and the US took over then Asia is returning","CHART","World","Area chart","Economy|History|International","Maddison Project: Historical GDP (rug.nl/ggdc/historicaldevelopment); World Bank: GDP (worldbank.org)",70,60,75,80,68,72,72,85),
mk("HBL15","The Rise and Fall of Every World Empire Animated","Territory controlled by major empires from 3000 BC to present","MAP","World","Animated choropleth","History|International|War","Historical Atlas of World Empires; GeaCron (geacron.com)",72,58,68,78,68,88,72,72),
# === Economy × Psychology ===
mk("HBL16","Consumer Confidence vs. Actual Economic Performance","People feel the economy is bad even when numbers say otherwise","XREF","US-national","Line chart","Economy|Psychology","Conference Board: Consumer Confidence (conference-board.org); BEA: GDP (bea.gov)",75,80,78,78,72,65,72,90),
mk("HBL17","Stock Market Returns by Which Party Controls the White House","Democrats vs. Republicans and the S&P 500 — the data surprises both sides","CHART","US-national","Bar chart","Economy|Politics|Finance","S&P Dow Jones: Historical Data (spglobal.com); White House: Administration Timeline",68,72,78,82,72,65,72,88),
# === Health × International deep dives ===
mk("HBL18","Antibiotic Resistance Rates by Country","The superbugs are winning and the map shows where","MAP","World","World choropleth","Health|International|Science","WHO: GLASS Report (who.int); CDC: AR Threats (cdc.gov/drugresistance)",78,65,72,78,78,78,72,80),
mk("HBL19","Mental Health Spending Per Capita by Country","Most nations spend less than 2% of health budgets on mental health","MAP","World","World choropleth","Health|International|Psychology","WHO: Mental Health Atlas (who.int); OECD: Mental Health Data (oecd.org)",78,72,75,78,75,78,70,85),
mk("HBL20","COVID Death Rate by Country vs. Healthcare Spending","Rich countries didnt always do better","XREF","World","Scatter plot","Health|International|Economy","WHO: COVID Dashboard (who.int); OECD: Health Expenditure (oecd.org)",72,68,75,80,72,68,72,90),
# === "The Most X in Every State" series ===
mk("HBL21","The Most Dangerous Intersection in Every State","Crash data reveals Americas deadliest crossroads","MAP","US-state","Dot map","Transportation|Geography|Health","NHTSA: FARS Data (nhtsa.gov); State DOT: Crash Records",72,78,72,72,68,82,72,78),
mk("HBL22","The Oldest Business Still Operating in Every State","Some have been running for 300+ years","MAP","US-state","Dot map","Economy|History|Geography","SBA: Historical Business Data; Various State Historical Records",60,72,78,82,52,78,78,68),
mk("HBL23","The Most Common Job in Every State Over Time","From farmer to truck driver to registered nurse — the animated shift","MAP","US-state","Animated choropleth","Labor|Geography|History","Census: Decennial Census (census.gov); BLS: OES (bls.gov)",68,78,78,78,65,82,72,88),
# === Health × Race ===
mk("HBL24","COVID Vaccination Rate by Race and County","The vaccination gap mapped nationwide","MAP","US-county","Bivariate choropleth","Health|Race|Inequality","CDC: COVID Vaccination Data (cdc.gov); Census: ACS Race (census.gov)",75,68,72,68,72,78,65,85),
mk("HBL25","Infant Mortality Rate by Race in Every State","In some states Black infant mortality is 3x the white rate","XREF","US-state","Bar chart","Health|Race|Children|Inequality","CDC: WONDER Infant Mortality (wonder.cdc.gov); Census: ACS Demographics (census.gov)",88,72,75,80,85,65,72,85),
# === Economy × Immigration ===
mk("HBL26","GDP Contribution of Immigrants vs. Their Share of Population","Immigrants punch above their weight economically","CHART","US-national","Bar chart","Economy|Immigration","CBO: Impact of Immigration (cbo.gov); Census: ACS Foreign-Born (census.gov)",72,68,78,80,68,65,72,85),
mk("HBL27","Immigrant-Founded Fortune 500 Companies","Over 40% of Fortune 500 companies were founded by immigrants or their children","RANK","US-national","Bar chart","Economy|Immigration|Technology","New American Economy: Fortune 500 (newamericaneconomy.org)",72,70,78,82,68,65,75,82),
# === Education × Health ===
mk("HBL28","Years of Education vs. Life Expectancy in America","Each additional year of school adds measurable years of life","XREF","US-national","Scatter plot","Education|Health","CDC: NCHS Education and Mortality (cdc.gov/nchs); Census: ACS Education (census.gov)",78,75,78,78,72,65,70,85),
mk("HBL29","School Nurse to Student Ratio by State","Some states have one nurse for 5000+ students","MAP","US-state","State choropleth","Education|Health|Children","NASN: School Nurse Survey (nasn.org); NCES: School Staffing (nces.ed.gov)",75,78,78,72,72,78,68,78),
# === Energy × Health ===
mk("HBL30","Proximity to Fracking Wells vs. Childhood Asthma","Families near fracking operations report more respiratory illness","XREF","US-county","Bivariate choropleth","Energy|Health|Children|Environment","EPA: FracFocus (fracfocus.org); CDC: Asthma Data (cdc.gov/asthma)",80,72,68,78,80,78,75,68),
# === Economy × Demographics ===
mk("HBL31","Median Age of First-Time Mothers by Country","From 19 in Niger to 32 in South Korea","MAP","World","World choropleth","Demographics|International|Gender|Health","UN: World Fertility Data (un.org/en/development); World Bank: Fertility Rate (worldbank.org)",65,68,78,78,62,78,68,88),
mk("HBL32","Single-Person Households by Country","In Sweden its 40% and climbing everywhere","MAP","World","World choropleth","Demographics|International|Psychology","UN: Household Size (population.un.org); Census: ACS Households (census.gov)",65,70,78,78,62,78,72,85),
# === Unique visual format ideas ===
mk("HBL33","The Topographic Map of US Income","3D terrain where height represents median household income","MAP","US-county","Special map","Economy|Geography|Inequality","Census: ACS Median Income (census.gov)",72,72,72,78,68,92,78,90),
mk("HBL34","Americas Electric Grid Visualized","Every power plant transmission line and distribution network","MAP","US-national","Line map","Energy|Infrastructure","EIA: Electric Grid Map (eia.gov); HIFLD: Electric Infrastructure (hifld-geoplatform.opendata.arcgis.com)",58,55,72,68,55,92,68,90),
mk("HBL35","The Commute Isochrone Map of Every Major City","How far can you get in 30 minutes from downtown by car vs. transit","MAP","US-metro","Special map","Transportation|Geography|Infrastructure","Google Maps: Travel Time API; Census: LODES Commute Data (lehd.ces.census.gov)",62,78,72,72,58,88,75,75),
]

# --- inject ---
with open(DATA, 'r', encoding='utf-8') as f:
    txt = f.read()
ids = set(re.findall(r'id:"([^"]+)"', txt))
new = [i for i in IDEAS if re.search(r'id:"([^"]+)"', i).group(1) not in ids]
if not new:
    print("All HBL ideas already present"); exit()
tail = "]; // end D"
txt = txt.replace(tail, ",\n".join(new) + ",\n" + tail)
with open(DATA, 'w', encoding='utf-8') as f:
    f.write(txt)
print(f"Injected {len(new)} new ideas (HBL batch)")
