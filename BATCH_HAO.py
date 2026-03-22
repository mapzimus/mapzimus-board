"""BATCH HAO: Cross-referenced ideas from uncombined section pairs.
Demographics x Economy, Health x History, Crime x Health, Food x Health, etc.
All sc values on 0-100 scale. Forward slashes in tbl paths."""
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

# ── Demographics x Economy (558 combined entries, never crossed) ──
ideas.append(mk("hao001","Countries Where Women Earn More Have Fewer Babies","Gender pay gap vs total fertility rate by country","XREF","World","Scatter plot","Demographics","World Bank: Gender pay gap + UN DESA: Fertility rates (worldbank.org + population.un.org)",75,85,70,80,70,75,80,85))
ideas.append(mk("hao002","The Richer the County the Fewer Kids Under 5","Median household income vs percent population under 5 by US county","XREF","US Counties","Scatter plot","Demographics","ACS/Census: Income + age by county (census.gov)",70,80,75,70,60,80,70,90))
ideas.append(mk("hao003","States Where Young People Are Leaving vs GDP Growth","Net migration age 18-34 vs real GDP growth rate by state","XREF","US States","Bivariate choropleth","Economy","ACS/Census: Migration + BEA: GDP by state (census.gov + bea.gov)",80,85,70,80,75,85,80,85))
ideas.append(mk("hao004","The Fertility-Unemployment Paradox","Countries with lowest unemployment often have lowest birth rates","XREF","World","Scatter plot","Demographics","World Bank: Unemployment + fertility rate by country (worldbank.org)",75,80,75,85,70,70,85,85))
ideas.append(mk("hao005","Where Median Age Is Rising Fastest vs Where Wages Are Stagnant","Change in median age vs real wage growth 2010-2024 by country","XREF","World","Scatter plot","Demographics","World Bank: Median age + ILO: Real wages (worldbank.org + ilo.org)",70,75,70,80,75,75,80,80))

# ── Health x History (528 combined entries, never crossed) ──
ideas.append(mk("hao006","Life Expectancy in 1900 vs 2024 by Country","How much each nation gained in lifespan over 124 years","XREF","World","Bar chart","Health","OWID: Life expectancy 1900-2024 (ourworldindata.org/life-expectancy)",80,75,80,75,60,80,70,90))
ideas.append(mk("hao007","The Countries That Beat Smallpox First vs Their Current Vaccination Rates","Historical smallpox eradication date vs current childhood vaccination coverage","XREF","World","Scatter plot","Health","WHO: Vaccination coverage + OWID: Smallpox history (who.int + ourworldindata.org)",65,60,65,85,60,70,90,75))
ideas.append(mk("hao008","How US States That Had Sanitariums Now Rank in Mental Health","Former TB sanitarium locations vs current depression/anxiety prevalence","XREF","US States","State choropleth","Health","SAMHSA: Mental health + Historical sanitarium registry (samhsa.gov)",60,65,60,90,65,75,95,60))
ideas.append(mk("hao009","The Countries That Suffered Most From the 1918 Flu vs COVID-19","Estimated 1918 influenza death rate vs COVID-19 death rate by country","XREF","World","Scatter plot","Health","OWID: COVID-19 + historical 1918 flu estimates (ourworldindata.org)",80,70,70,85,80,75,85,80))
ideas.append(mk("hao010","US Counties Named After Doctors vs Their Current Health Rankings","Counties named after physicians vs County Health Rankings","XREF","US Counties","Dot map","Health","USGS GNIS: Place names + County Health Rankings (countyhealthrankings.org)",50,60,60,90,40,75,95,70))


# ── Crime x Health (511 combined, never crossed) ──
ideas.append(mk("hao011","States With the Most Opioid Deaths Also Have the Highest Gun Violence","Opioid overdose rate vs firearm death rate by state","XREF","US States","Bivariate choropleth","Crime and Law Enforcement","CDC WONDER: Opioid + firearm deaths by state (wonder.cdc.gov)",85,80,75,75,85,85,75,90))
ideas.append(mk("hao012","Counties Where ER Wait Times Predict Violent Crime Rates","Average ER wait time vs violent crime rate by county","XREF","US Counties","Scatter plot","Crime and Law Enforcement","CMS: ER wait times + FBI UCR: Crime by county (cms.gov + ucr.fbi.gov)",65,70,65,85,75,70,90,75))
ideas.append(mk("hao013","Countries With Better Mental Health Care Have Lower Homicide Rates","Mental health spending per capita vs intentional homicide rate","XREF","World","Scatter plot","Health","WHO: Mental health atlas + UNODC: Homicide rates (who.int + unodc.org)",75,75,70,80,80,70,85,75))
ideas.append(mk("hao014","The Lead Paint-to-Crime Pipeline by US County","Historical lead exposure levels vs violent crime rate 20 years later","XREF","US Counties","Bivariate choropleth","Crime and Law Enforcement","CDC: Blood lead levels + FBI UCR: Crime by county (cdc.gov + ucr.fbi.gov)",80,75,70,85,80,80,90,70))
ideas.append(mk("hao015","States Where Medicaid Expansion Happened vs Change in Drug Arrests","Pre/post ACA Medicaid expansion vs drug arrest rate change by state","XREF","US States","State choropleth","Health","KFF: Medicaid expansion + FBI UCR: Drug arrests (kff.org + ucr.fbi.gov)",75,75,70,80,80,75,85,85))

# ── Food x Health (482 combined, never crossed) ──
ideas.append(mk("hao016","Countries That Eat the Most Sugar vs Diabetes Prevalence","Per capita sugar consumption vs type 2 diabetes rate by country","XREF","World","Scatter plot","Food & Nutrition","FAO: Food balance sheets + IDF: Diabetes atlas (fao.org + diabetesatlas.org)",80,85,80,70,75,75,70,90))
ideas.append(mk("hao017","States With the Most Fast Food Per Capita vs Obesity Rates","Fast food restaurants per 100k vs adult obesity rate by state","XREF","US States","Bivariate choropleth","Food & Nutrition","Census: County Business Patterns + CDC: BRFSS obesity (census.gov + cdc.gov)",80,85,80,65,70,85,65,90))
ideas.append(mk("hao018","The Breakfast Desert: Counties With No Breakfast Restaurants vs Child Hunger","Breakfast restaurant density vs child food insecurity rate","XREF","US Counties","Bivariate choropleth","Food & Nutrition","Census: CBP + Feeding America: Map the Meal Gap (census.gov + feedingamerica.org)",75,80,70,80,75,80,85,75))
ideas.append(mk("hao019","Countries Where Meat Consumption Dropped vs Heart Disease Mortality Change","Change in per capita meat consumption vs change in cardiovascular mortality 2000-2023","XREF","World","Scatter plot","Health","FAO: Food balance + WHO: Mortality database (fao.org + who.int)",70,75,70,80,70,70,85,80))
ideas.append(mk("hao020","US Counties Where Dollar Stores Outnumber Grocery Stores vs Life Expectancy","Dollar store to grocery store ratio vs life expectancy by county","XREF","US Counties","Bivariate choropleth","Food & Nutrition","Census: CBP retail + IHME: Life expectancy by county (census.gov + healthdata.org)",80,85,75,85,80,85,85,75))


# ── International Statistics x Transportation (491 combined, never crossed) ──
ideas.append(mk("hao021","Countries With the Best Trains Have the Fewest Car Crashes","Rail passenger-km per capita vs road traffic fatality rate","XREF","World","Scatter plot","Transportation","World Bank: Rail transport + WHO: Road traffic deaths (worldbank.org + who.int)",75,80,75,75,70,75,80,85))
ideas.append(mk("hao022","Air Connectivity vs GDP Per Capita by Country","International air routes per airport vs GDP per capita","XREF","World","Scatter plot","Economy","ICAO: Air transport + World Bank: GDP per capita (icao.int + worldbank.org)",65,65,70,70,55,70,75,80))
ideas.append(mk("hao023","Countries Where People Walk the Most vs Their Carbon Emissions","Walking/cycling modal share vs CO2 per capita","XREF","World","Scatter plot","Transportation","ITDP: Modal share + Global Carbon Project (itdp.org + globalcarbonproject.org)",70,75,70,80,65,70,85,75))

# ── Health x Housing (470 combined, never crossed) ──
ideas.append(mk("hao024","Counties Where Rent Takes Half Your Income vs ER Visits for Anxiety","Rent burden >50% rate vs anxiety-related ER visit rate by county","XREF","US Counties","Bivariate choropleth","Housing","ACS: Rent burden + HCUP: ER visits by diagnosis (census.gov + hcup-us.ahrq.gov)",80,85,75,80,80,80,85,70))
ideas.append(mk("hao025","States Where Homelessness Rose vs Where Mental Health Funding Was Cut","Change in PIT homeless count vs change in state mental health budget","XREF","US States","Bivariate choropleth","Housing","HUD: PIT count + SAMHSA: State mental health expenditures (huduser.gov + samhsa.gov)",80,80,75,75,85,80,80,80))
ideas.append(mk("hao026","The Mold Belt: Counties With Highest Humidity vs Asthma Hospitalization","Average relative humidity vs asthma hospitalization rate by county","XREF","US Counties","Bivariate choropleth","Health","NOAA: Climate normals + CDC: Asthma hospitalization (noaa.gov + cdc.gov)",65,70,65,80,60,80,85,80))
ideas.append(mk("hao027","Countries Where Housing Costs More Than Healthcare","Housing expenditure share vs healthcare expenditure share of GDP","XREF","World","Bar chart","Housing","OECD: Household spending by category (oecd.org)",70,80,75,75,70,70,80,85))
ideas.append(mk("hao028","Lead Pipes and Low Birth Weight by US County","Estimated lead service line prevalence vs low birth weight rate","XREF","US Counties","Bivariate choropleth","Health","EPA: Lead service lines + CDC: Low birth weight by county (epa.gov + cdc.gov)",80,75,70,80,85,80,85,70))

# ── Geography x Health (468 combined, never crossed) ──
ideas.append(mk("hao029","Elevation and Depression: US Counties Above 5000 Feet vs Suicide Rate","Mean county elevation vs age-adjusted suicide rate","XREF","US Counties","Bivariate choropleth","Health","USGS: Elevation data + CDC WONDER: Suicide mortality (usgs.gov + wonder.cdc.gov)",65,65,65,90,75,80,90,85))
ideas.append(mk("hao030","Distance to the Nearest Hospital vs Maternal Mortality by County","Drive time to nearest hospital vs maternal death rate","XREF","US Counties","Bivariate choropleth","Health","HRSA: Hospital locations + CDC: Maternal mortality (hrsa.gov + cdc.gov)",80,80,75,75,80,85,80,75))


# ── Economy x History (462 combined, never crossed) ──
ideas.append(mk("hao031","Countries That Were Colonized vs Their GDP Per Capita Today","Former colonial status vs current GDP per capita","XREF","World","World choropleth","Economy","OWID: Colonial history + World Bank: GDP per capita (ourworldindata.org + worldbank.org)",75,70,70,80,75,80,85,85))
ideas.append(mk("hao032","US States That Were Slave States vs Their Median Wage Today","Former slave/free state status vs current median wage","XREF","US States","State choropleth","Economy","Historical: Slave state status + BLS: Median wage by state (bls.gov)",80,75,70,85,85,80,85,90))
ideas.append(mk("hao033","Gold Rush Counties Then vs Their Economy Now","Historical gold rush activity 1849-1900 vs current median income","XREF","US Counties","Dot map","Economy","USGS: Historical mining + ACS: Median income by county (usgs.gov + census.gov)",55,65,60,85,55,75,90,65))
ideas.append(mk("hao034","Countries on the Silk Road vs Their Trade Volume Today","Historical Silk Road route countries vs current trade as % of GDP","XREF","World","World choropleth","Economy","UNESCO: Silk Road heritage + World Bank: Trade % GDP (worldbank.org)",60,60,65,85,55,80,90,80))
ideas.append(mk("hao035","Rust Belt Cities Then and Now: Manufacturing Employment 1970 vs 2024","Manufacturing jobs as share of total employment 1970 vs 2024 for Rust Belt MSAs","XREF","US Metro","Bar chart","Economy","BLS: CES manufacturing employment by MSA 1970 + 2024 (bls.gov)",80,80,80,70,75,75,70,90))

# ── Economy x Science & Technology (458 combined, never crossed) ──
ideas.append(mk("hao036","Countries That Spend the Most on R&D vs Their Patent Output","R&D spending as % GDP vs patents per million people","XREF","World","Scatter plot","Science & Technology","UNESCO: R&D expenditure + WIPO: Patent statistics (uis.unesco.org + wipo.int)",65,60,70,70,55,70,75,90))
ideas.append(mk("hao037","States Where AI Job Postings Grew Fastest vs Median Wage Change","AI-related job postings growth vs median wage change 2020-2024","XREF","US States","Bivariate choropleth","Science & Technology","Kaggle: AI Job Market Trends 2026 (kaggle.com/datasets/ai-job-market-2026) + BLS: OEWS median wage (bls.gov)",75,80,70,80,70,75,85,85))
ideas.append(mk("hao038","The Broadband Divide Predicts Economic Mobility","Broadband access rate vs upward economic mobility by county","XREF","US Counties","Bivariate choropleth","Economy","FCC: Broadband deployment + Opportunity Insights: Economic mobility (fcc.gov + opportunityinsights.org)",80,85,75,75,75,80,80,85))
ideas.append(mk("hao039","Countries With the Most Satellites vs Their GDP","Active satellites in orbit vs nominal GDP by country","XREF","World","Scatter plot","Science & Technology","UCS: Satellite database + World Bank: GDP (ucsusa.org + worldbank.org)",60,55,65,80,55,70,85,80))
ideas.append(mk("hao040","EV Adoption Rate vs Average Electricity Price by State","Electric vehicle registration share vs residential electricity rate","XREF","US States","Bivariate choropleth","Science & Technology","DOE AFDC: EV registrations + EIA: Electricity prices (afdc.energy.gov + eia.gov)",70,75,75,75,65,80,75,90))

# Injection
with open(DATA, 'r', encoding='utf-8') as f:
    text = f.read()
existing_ids = set(re.findall(r'id:"([^"]*)"', text))
new_ideas = [idea for idea in ideas if re.search(r'id:"([^"]*)"', idea).group(1) not in existing_ids]
if not new_ideas:
    print("All ideas already exist. Skipping.")
else:
    tail = ']; // end D'
    pos = text.rfind(tail)
    inject = '\n,'.join(new_ideas)
    text = text[:pos] + ',\n' + inject + '\n' + tail
    with open(DATA, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f"Injected {len(new_ideas)} new XREF ideas (HAO batch)")
