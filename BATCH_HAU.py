"""BATCH HAU: Deep dataset-to-dataset correlations.
Pairing specific government datasets that have never been crossed.
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

# ── FBI UCR x Census/BLS ──
ideas.append(mk("hau001","Counties Where Poverty Rose 10% Also Saw Property Crime Rise 15%","Change in poverty rate vs change in property crime rate 2019-2024","XREF","US Counties","Scatter plot","Crime and Law Enforcement","FBI UCR: Property crime + ACS: Poverty rate by county (ucr.fbi.gov + census.gov)",80,80,75,75,80,75,80,85))
ideas.append(mk("hau002","Police Staffing per Capita vs Violent Crime Rate: The Curve Isnt Linear","Officers per 100k vs violent crime rate showing diminishing returns","XREF","US Metro","Scatter plot","Crime and Law Enforcement","FBI UCR: Law enforcement employees + violent crime by metro (ucr.fbi.gov)",75,70,70,80,70,70,85,90))
ideas.append(mk("hau003","States Where Incarceration Spending Exceeds Higher Ed Spending","Corrections spending vs public university spending per capita","XREF","US States","Bar chart","Crime and Law Enforcement","Census: State expenditure survey - corrections vs higher ed (census.gov/govs)",85,80,75,80,85,75,80,90))

# ── CDC WONDER x BLS/Census ──
ideas.append(mk("hau004","Counties Where Drug Overdose Deaths Track Unemployment Almost Exactly","Opioid overdose mortality vs unemployment rate by county, R-squared annotated","XREF","US Counties","Scatter plot","Health","CDC WONDER: Drug overdose + BLS: LAUS unemployment (wonder.cdc.gov + bls.gov)",85,80,75,75,85,75,80,85))
ideas.append(mk("hau005","The Maternal Desert: Counties With No OB-GYN vs Maternal Mortality","Maternity care desert status vs maternal death rate","XREF","US Counties","Bivariate choropleth","Health","March of Dimes: Maternity care deserts + CDC: Maternal mortality (marchofdimes.org + cdc.gov)",85,80,75,80,85,85,80,85))
ideas.append(mk("hau006","Suicide Rate vs Altitude: The Mountain West Anomaly","Age-adjusted suicide rate by county colored by mean elevation","XREF","US Counties","Scatter plot","Health","CDC WONDER: Suicide mortality + USGS: National Elevation Dataset (wonder.cdc.gov + usgs.gov)",65,60,65,90,75,75,90,85))

# ── USDA x Census x CDC ──
ideas.append(mk("hau007","The Food Desert-Health Desert-Income Desert Triple Overlap","Counties that are simultaneously food deserts, health professional shortage areas, and below poverty line","XREF","US Counties","County choropleth","Food & Nutrition","USDA: Food access + HRSA: HPSA + ACS: Poverty (ers.usda.gov + hrsa.gov + census.gov)",85,80,75,80,85,85,85,85))
ideas.append(mk("hau008","Farm Revenue Per Acre vs Topsoil Depth by County","Agricultural revenue per cropland acre vs USDA topsoil depth","XREF","US Counties","Bivariate choropleth","Agriculture","USDA NASS: Ag census + NRCS: Soil survey (nass.usda.gov + nrcs.usda.gov)",55,50,60,80,55,80,85,85))
ideas.append(mk("hau009","SNAP Enrollment vs Grocery Store Density by County","SNAP participants per 1000 vs grocery stores per 10k population","XREF","US Counties","Bivariate choropleth","Food & Nutrition","USDA FNS: SNAP + Census: CBP grocery (fns.usda.gov + census.gov)",80,80,75,75,75,80,75,90))

# ── EPA x Census/Health ──
ideas.append(mk("hau010","Superfund Sites Within 5 Miles of Schools vs Childhood Cancer Rate","Schools near NPL sites vs pediatric cancer incidence by county","XREF","US Counties","Dot map","Health","EPA: NPL sites + NCES: School locations + NCI: Cancer incidence (epa.gov + nces.ed.gov + cancer.gov)",80,75,65,85,85,80,85,70))
ideas.append(mk("hau011","Air Quality Index vs Asthma ER Visits by Metro","Annual average AQI vs asthma-related ER visit rate","XREF","US Metro","Scatter plot","Health","EPA: AQI + HCUP: ER visits by diagnosis (epa.gov + hcup-us.ahrq.gov)",75,75,75,70,70,70,75,85))
ideas.append(mk("hau012","Counties Downwind of Coal Plants vs Respiratory Disease Mortality","Coal plant locations + prevailing wind direction vs respiratory mortality","XREF","US Counties","Bivariate choropleth","Health","EPA: Power plant emissions + CDC: Respiratory mortality (epa.gov + cdc.gov)",80,70,65,85,85,80,85,75))


# ── EIA x BLS x Census ──
ideas.append(mk("hau013","States Where Energy Costs Eat Up the Most of Low-Income Budgets","Residential energy cost as % of income for bottom quintile by state","XREF","US States","State choropleth","Economy","EIA: Residential energy expenditure + ACS: Income by quintile (eia.gov + census.gov)",85,85,80,75,80,80,75,90))
ideas.append(mk("hau014","The States Most Dependent on a Single Energy Source","Dominant energy source share of total generation by state","MAP","US States","State choropleth","Energy","EIA: State electricity generation by source (eia.gov)",65,65,70,75,65,80,70,90))
ideas.append(mk("hau015","Counties Where Fracking Jobs Replaced Manufacturing Jobs","Change in mining employment vs change in manufacturing employment 2010-2024","XREF","US Counties","Bivariate choropleth","Labor","BLS: QCEW mining + manufacturing by county (bls.gov)",70,65,65,80,70,80,80,85))

# ── DOT/NHTSA x Census ──
ideas.append(mk("hau016","The Most Dangerous Intersection in Every State","Intersection with most fatalities 2019-2024 per state","MAP","US States","Dot map","Transportation","NHTSA: FARS intersection data (nhtsa.gov)",75,80,65,75,70,80,75,80))
ideas.append(mk("hau017","Counties Where Average Commute Exceeds 45 Minutes vs Median Income","Super-commuter counties vs their median household income","XREF","US Counties","Bivariate choropleth","Transportation","ACS: Commute time + income by county (census.gov)",75,85,75,70,65,80,75,90))
ideas.append(mk("hau018","Bridge Condition vs Income: Poorer Counties Have Worse Infrastructure","Structurally deficient bridge rate vs median income by county","XREF","US Counties","Scatter plot","Transportation","FHWA: NBI bridge condition + ACS: Income (fhwa.dot.gov + census.gov)",75,75,70,75,75,75,80,90))

# ── HUD x Census ──
ideas.append(mk("hau019","Section 8 Voucher Holders Live in the Highest Poverty Zip Codes","HCV concentration vs neighborhood poverty rate","XREF","US Counties","Scatter plot","Housing","HUD: Picture of Subsidized Households + ACS: Poverty by tract (huduser.gov + census.gov)",75,70,70,75,80,70,80,90))
ideas.append(mk("hau020","Cities Where Public Housing Wait Lists Exceed 5 Years","Public housing and HCV wait list time by metro area","RANK","US Metro","Bar chart","Housing","HUD: Public housing wait lists (huduser.gov)",80,80,70,75,80,65,75,80))

# ── FCC x Census x Health ──
ideas.append(mk("hau021","The Broadband Desert Is Also a Health Desert","Counties without broadband vs counties without hospitals","XREF","US Counties","Bivariate choropleth","Health","FCC: Broadband deployment + HRSA: HPSA designations (fcc.gov + hrsa.gov)",75,70,70,80,75,80,85,85))
ideas.append(mk("hau022","Telehealth Usage Surged Most in Counties With Worst Internet","Telehealth visit rate vs broadband access rate by county","XREF","US Counties","Scatter plot","Health","CMS: Telehealth utilization + FCC: Broadband (cms.gov + fcc.gov)",65,70,65,85,60,70,85,80))

# ── OWID x World Bank x WHO mashups ──
ideas.append(mk("hau023","Countries Where Deforestation Rate Predicts Malaria Resurgence","Annual forest cover loss vs malaria incidence change","XREF","World","Scatter plot","Geography & Environment","OWID: Forest cover + WHO: Malaria report (ourworldindata.org + who.int)",65,55,65,85,75,70,85,80))
ideas.append(mk("hau024","The Corruption-Infrastructure Gap: Countries Where Roads Get Worse as Corruption Rises","Transparency International CPI vs road quality index","XREF","World","Scatter plot","International Statistics","TI: Corruption Perceptions Index + WEF: Infrastructure quality (transparency.org + weforum.org)",70,65,70,80,75,70,80,85))
ideas.append(mk("hau025","Countries That Educate Women the Most Have the Fastest Declining Birth Rates","Female secondary enrollment vs total fertility rate by country","XREF","World","Scatter plot","Demographics","World Bank: Female education + UN DESA: Fertility (worldbank.org + population.un.org)",75,70,75,70,70,70,75,90))

# ── Multi-source deep dives ──
ideas.append(mk("hau026","The Opioid Pipeline: Counties Where Pill Mills Were vs Current Overdose Hotspots","DEA ARCOS opioid shipment volume 2006-2012 vs current overdose rate","XREF","US Counties","Bivariate choropleth","Health","DEA: ARCOS + CDC WONDER: Drug overdose mortality (dea.gov + wonder.cdc.gov)",85,75,70,80,90,85,85,80))
ideas.append(mk("hau027","Redlined Neighborhoods in 1935 vs Their Property Values Today","HOLC redlining grade vs current median home value for same census tracts","XREF","US Metro","Scatter plot","Housing","U of Richmond: Mapping Inequality + ACS: Median home value (dsl.richmond.edu + census.gov)",85,75,75,80,85,80,85,85))
ideas.append(mk("hau028","Former Sundown Towns vs Their Current Demographics","Historical sundown town designation vs current non-white population share","XREF","US Counties","Dot map","Demographics","Loewen: Sundown Towns database + ACS: Race by county (sundown.tougaloo.edu + census.gov)",75,65,60,90,80,80,90,70))
ideas.append(mk("hau029","Agent Orange Spraying Zones vs Cancer Clusters in Vietnam Today","Historical defoliant spraying intensity vs current cancer incidence","XREF","World","Special map","Health","NIH: Agent Orange maps + Vietnam MOH: Cancer registry (nih.gov)",75,55,60,85,80,85,90,60))
ideas.append(mk("hau030","Nuclear Test Sites vs Downwind Cancer Rates 50 Years Later","Historical nuclear test locations vs cancer incidence in downwind counties/regions","XREF","World","Dot map","Health","DOE: Nuclear testing archive + NCI/IARC: Cancer incidence (energy.gov + cancer.gov)",80,60,60,85,85,85,90,65))

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
    print(f"Injected {len(new_ideas)} new ideas (HAU batch)")
