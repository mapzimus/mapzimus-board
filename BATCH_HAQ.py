"""BATCH HAQ: Deep cross-references - surprising correlations.
Climate x Crime, Labor x Health, Agriculture x Demographics, Sports x Economy, etc.
All sc values on 0-100 scale."""
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

MAP="MAP"; CHART="CHART"; XREF="XREF"; RANK="RANK"
ideas = []

# ── Climate x Crime ──
ideas.append(mk("haq001","Hotter States Have Higher Violent Crime Rates","Average annual temperature vs violent crime rate per 100k by state","XREF","US States","Scatter plot","Crime and Law Enforcement","NOAA: Climate normals + FBI UCR: Violent crime (noaa.gov + ucr.fbi.gov)",70,70,75,80,70,70,80,90))
ideas.append(mk("haq002","The Heat-Rage Calendar: US Assault Rates by Month","Monthly aggravated assault rate showing summer spike pattern","CHART","US","Area chart","Crime and Law Enforcement","FBI UCR: Monthly crime data (ucr.fbi.gov)",75,80,75,70,70,75,75,85))
ideas.append(mk("haq003","Countries Hit Hardest by Drought vs Political Instability","Drought severity index vs Fragile States Index score","XREF","World","Scatter plot","Climate","EM-DAT: Drought events + Fund for Peace: FSI (emdat.be + fragilestatesindex.org)",70,60,65,80,80,70,85,80))

# ── Labor x Health ──
ideas.append(mk("haq004","States Where Nurses Are Quitting Fastest vs Patient Mortality","Nursing turnover rate vs hospital mortality index by state","XREF","US States","Bivariate choropleth","Health","BLS: Nursing employment change + CMS: Hospital mortality (bls.gov + cms.gov)",80,80,70,75,85,75,80,75))
ideas.append(mk("haq005","The Burnout Map: States Where Workers Report Most Stress vs Heart Disease","Gallup workplace stress rate vs heart disease mortality by state","XREF","US States","Bivariate choropleth","Labor","Gallup: Workplace wellbeing + CDC: Heart disease mortality (gallup.com + cdc.gov)",80,85,70,75,75,80,80,70))
ideas.append(mk("haq006","Countries Where Workers Get the Most Vacation vs Depression Rates","Statutory annual leave days vs depression prevalence","XREF","World","Scatter plot","Labor","ILO: Working conditions + IHME: GBD depression prevalence (ilo.org + healthdata.org)",75,85,70,80,65,65,85,80))
ideas.append(mk("haq007","Minimum Wage vs Health Insurance Coverage by State","State minimum wage vs uninsured rate","XREF","US States","Bivariate choropleth","Labor","DOL: State minimum wages + ACS: Health insurance coverage (dol.gov + census.gov)",80,85,75,70,75,80,70,90))


# ── Agriculture x Demographics ──
ideas.append(mk("haq008","Farm Counties Are Aging Twice as Fast as Urban Ones","Median age change in farming-dependent vs metro counties 2000-2024","XREF","US Counties","Bivariate choropleth","Demographics","USDA ERS: Rural-Urban + ACS: Median age (ers.usda.gov + census.gov)",75,70,70,75,70,80,80,90))
ideas.append(mk("haq009","Countries That Export the Most Food vs Their Own Malnutrition Rate","Agricultural exports value vs stunting prevalence in children under 5","XREF","World","Scatter plot","Food & Nutrition","FAO: Trade data + UNICEF: Child malnutrition (fao.org + data.unicef.org)",80,70,70,90,85,70,90,85))
ideas.append(mk("haq010","The Vanishing Farmer: Average Age of Farmers by State 1997 vs 2022","Change in average age of farm operators by state","CHART","US States","State choropleth","Agriculture","USDA NASS: Census of Agriculture 1997+2022 (nass.usda.gov)",75,70,75,75,75,80,70,90))

# ── Sports x Economy ──
ideas.append(mk("haq011","NFL Stadium Proximity vs Home Values","Median home value within 2 miles of NFL stadiums vs city median","XREF","US Metro","Bar chart","Sports & Recreation","Zillow: ZHVI + NFL: Stadium locations (zillow.com + nfl.com)",65,75,65,75,60,70,80,80))
ideas.append(mk("haq012","Countries With the Highest Soccer Spending vs Their FIFA Ranking","Club football total expenditure vs FIFA world ranking","XREF","World","Scatter plot","Sports & Recreation","Deloitte: Football Money League + FIFA: Rankings (deloitte.com + fifa.com)",65,70,70,75,55,70,75,85))
ideas.append(mk("haq013","Olympic Host City GDP Before and After the Games","GDP growth trajectory 5 years before and after hosting Olympics","CHART","World","Line chart","Economy","World Bank: GDP + IOC: Host city data (worldbank.org + olympics.com)",70,65,70,80,65,75,80,85))

# ── Transportation x Environment ──
ideas.append(mk("haq014","Cities With the Best Public Transit vs Lowest Air Pollution","Transit ridership per capita vs PM2.5 annual average","XREF","World","Scatter plot","Transportation","UITP: Mobility statistics + WHO: Air quality (uitp.org + who.int)",70,70,70,70,65,70,80,80))
ideas.append(mk("haq015","The Commute Emissions Gap: Counties Where Driving Alone Is Highest vs CO2","Drive-alone commute share vs transportation CO2 per capita","XREF","US Counties","Bivariate choropleth","Transportation","ACS: Commute mode + EPA: GHG by county (census.gov + epa.gov)",70,75,70,70,65,80,80,80))
ideas.append(mk("haq016","Countries Where Electric Trains Move the Most People vs Carbon Intensity","Electrified rail passenger-km vs carbon intensity of electricity","XREF","World","Scatter plot","Transportation","UIC: Rail statistics + IEA: Carbon intensity (uic.org + iea.org)",60,55,65,75,55,65,85,80))

# ── Education x Health ──
ideas.append(mk("haq017","States Where School Lunch Participation Is Highest vs Childhood Obesity","Free/reduced lunch participation rate vs child obesity rate","XREF","US States","Bivariate choropleth","Education","USDA: NSLP participation + CDC: Child obesity (fns.usda.gov + cdc.gov)",75,80,70,75,70,80,75,85))
ideas.append(mk("haq018","College Degree Rate vs Life Expectancy by US County","Bachelors degree attainment vs life expectancy","XREF","US Counties","Bivariate choropleth","Education","ACS: Educational attainment + IHME: Life expectancy (census.gov + healthdata.org)",75,75,75,70,70,80,70,90))
ideas.append(mk("haq019","Countries With the Most PhDs per Capita vs Suicide Rate","PhD holders per million vs suicide rate","XREF","World","Scatter plot","Education","OECD: Education at a Glance + WHO: Suicide rates (oecd.org + who.int)",65,60,60,90,75,60,90,80))
ideas.append(mk("haq020","States Where Sex Ed Is Comprehensive vs Teen Birth Rate","Sex education mandate type vs teen birth rate","XREF","US States","State choropleth","Education","Guttmacher: Sex ed policy + CDC: Teen birth rate (guttmacher.org + cdc.gov)",80,80,75,70,75,75,75,90))


# ── Wildcard: Surprising multi-domain correlations ──
ideas.append(mk("haq021","Church Attendance vs Divorce Rate by State","Weekly church attendance rate vs divorce rate per 1000","XREF","US States","Scatter plot","Demographics","Gallup: Church attendance + CDC: Marriage/divorce (gallup.com + cdc.gov)",75,80,70,85,70,65,85,80))
ideas.append(mk("haq022","Countries With the Most UNESCO Sites vs Tourism Revenue Per Capita","UNESCO World Heritage sites count vs tourism receipts per capita","XREF","World","Scatter plot","Entertainment","UNESCO: World Heritage + UNWTO: Tourism statistics (whc.unesco.org + unwto.org)",55,60,70,70,45,70,75,90))
ideas.append(mk("haq023","States Where Dogs Outnumber Kids vs Median Age","Dog ownership rate vs percent population under 18","XREF","US States","Scatter plot","Demographics","AVMA: Pet ownership + ACS: Age distribution (avma.org + census.gov)",60,80,65,80,50,65,90,75))
ideas.append(mk("haq024","The Library-Prison Pipeline: States That Spend More on Prisons Than Libraries","Per capita spending on corrections vs public libraries by state","XREF","US States","State choropleth","Crime and Law Enforcement","Census: State/local spending + IMLS: Public library survey (census.gov + imls.gov)",80,80,75,80,85,75,80,90))
ideas.append(mk("haq025","Countries Where Coffee Consumption Predicts Research Output","Coffee consumption per capita vs scientific publications per million","XREF","World","Scatter plot","Science & Technology","ICO: Coffee consumption + Scimago: Publication ranking (ico.org + scimagojr.com)",55,65,60,90,40,60,95,85))
ideas.append(mk("haq026","Tattoo Parlors Per Capita vs Median Age by US Metro","Tattoo shop density vs metro median age","XREF","US Metro","Scatter plot","Demographics","Census: CBP tattoo shops + ACS: Median age by metro (census.gov)",55,70,60,85,40,60,90,80))
ideas.append(mk("haq027","Countries That Sleep the Most vs GDP Per Capita","Average nightly sleep hours vs GDP per capita","XREF","World","Scatter plot","Economy","OECD: Time use sleep + World Bank: GDP per capita (oecd.org + worldbank.org)",70,85,65,80,55,60,85,80))
ideas.append(mk("haq028","States With the Tallest People vs Their Agricultural Output","Average adult height vs total crop production value","XREF","US States","Scatter plot","Demographics","CDC: BRFSS + USDA NASS: Crop values by state (cdc.gov + nass.usda.gov)",50,55,55,90,35,55,95,80))
ideas.append(mk("haq029","The Pizza-Subway Index: Cities Where Pizza Costs More Than a Subway Ride","Slice of pizza price vs single-ride transit fare in world cities","RANK","World","Bar chart","Economy","Numbeo: Food prices + Moovit: Transit fares (numbeo.com + moovitapp.com)",65,80,70,80,50,65,90,70))
ideas.append(mk("haq030","Light Pollution vs Firefly Population Decline by US Region","Satellite-measured nighttime light intensity vs firefly sighting reports","XREF","US States","Bivariate choropleth","Geography & Environment","NOAA/NASA: VIIRS nighttime lights + Firefly Watch: Community science (noaa.gov + massaudubon.org)",60,65,60,85,70,80,90,60))

# ── Triple-source mashups (most viral potential) ──
ideas.append(mk("haq031","States Where Fast Food Is Cheap + Diabetes Is High + Wages Are Low","Overlaying fast food affordability, diabetes rate, and median wage","XREF","US States","State choropleth","Health","Census: CBP + CDC: Diabetes + BLS: Wage (census.gov + cdc.gov + bls.gov)",85,90,75,75,80,80,80,80))
ideas.append(mk("haq032","The American Death Triangle: Counties With High Poverty + Low Education + High Opioid Deaths","Poverty rate vs bachelors rate vs opioid mortality rate","XREF","US Counties","County choropleth","Health","ACS + NCES + CDC WONDER: Poverty, education, opioid mortality (census.gov + nces.ed.gov + cdc.gov)",85,80,70,75,90,85,80,85))
ideas.append(mk("haq033","The Climate Migration Trap: Counties Getting Hotter + More Expensive + More Populated","Temperature increase vs home price increase vs population increase 2010-2024","XREF","US Counties","County choropleth","Climate","NOAA + Zillow + ACS: Temperature, ZHVI, population by county (noaa.gov + zillow.com + census.gov)",80,80,70,80,80,85,85,80))
ideas.append(mk("haq034","Countries Getting Richer + Lonelier + Less Religious Simultaneously","GDP per capita growth vs loneliness prevalence vs religious attendance decline","XREF","World","Scatter plot","Demographics","World Bank + Gallup + WIN/Gallup: GDP, loneliness, religiosity (worldbank.org + gallup.com)",80,80,65,85,75,65,90,70))
ideas.append(mk("haq035","States Where Teachers Leave + Test Scores Drop + Housing Costs Rise","Teacher attrition rate vs NAEP score change vs home price change","XREF","US States","State choropleth","Education","NEA + NAEP + FHFA: Teachers, test scores, housing (nea.org + nces.ed.gov + fhfa.gov)",85,85,70,75,80,80,80,75))

# Injection
with open(DATA, 'r', encoding='utf-8') as f:
    text = f.read()
existing_ids = set(re.findall(r'id:"([^"]*)"', text))
new_ideas = [idea for idea in ideas if re.search(r'id:"([^"]*)"', idea).group(1) not in existing_ids]
if not new_ideas:
    print("All ideas already exist.")
else:
    tail = ']; // end D'
    pos = text.rfind(tail)
    inject = '\n,'.join(new_ideas)
    text = text[:pos] + ',\n' + inject + '\n' + tail
    with open(DATA, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f"Injected {len(new_ideas)} new ideas (HAQ batch)")
