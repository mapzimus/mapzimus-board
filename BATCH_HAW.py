"""BATCH HAW: High-viral potential cross-refs - the ones that make people
argue in the comments. Controversial takes backed by data.
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

# ── "Actually..." Series (conventional wisdom vs data) ──
ideas.append(mk("haw001","Immigration Doesnt Raise Crime - It Lowers It","Foreign-born population share vs violent crime rate by US metro, 2000-2024","XREF","US Metro","Scatter plot","Crime and Law Enforcement","ACS: Foreign-born + FBI UCR: Crime by metro (census.gov + ucr.fbi.gov)",75,70,75,85,80,65,80,90))
ideas.append(mk("haw002","Red States Get More Federal Dollars Than They Pay In","Net federal spending per capita (received minus paid) by state colored by 2024 vote","XREF","US States","State choropleth","Economy","Rockefeller Institute: Balance of Payments + MIT Election Lab (rockinst.org + electionlab.mit.edu)",80,80,75,85,85,80,80,90))
ideas.append(mk("haw003","Countries With Stricter Gun Laws Have Fewer Gun Deaths - No Exceptions","Gun law strength index vs firearm death rate for all 50 countries with data","XREF","World","Scatter plot","Crime and Law Enforcement","GunPolicy.org: Law strength + IHME: Firearm deaths (gunpolicy.org + healthdata.org)",80,75,75,70,85,70,75,85))
ideas.append(mk("haw004","States That Banned Abortion Saw Maternal Mortality Rise","Maternal mortality rate before vs after Dobbs by abortion ban status","XREF","US States","Bar chart","Health","CDC: Maternal mortality + Guttmacher: Abortion policy (cdc.gov + guttmacher.org)",85,80,70,75,90,70,80,75))
ideas.append(mk("haw005","The Death Penalty Doesnt Deter Murder: States With It Have Higher Rates","Murder rate in death penalty vs non-death penalty states 1990-2024","CHART","US States","Line chart","Crime and Law Enforcement","FBI UCR: Murder rate + Death Penalty Information Center (ucr.fbi.gov + deathpenaltyinfo.org)",75,70,75,80,80,65,80,90))

# ── "The System Is Broken" Series ──
ideas.append(mk("haw006","CEO Pay Has Grown 1460% Since 1978 While Worker Pay Grew 18%","CEO-to-worker compensation ratio 1978-2024","CHART","US","Line chart","Economy","EPI: CEO compensation + BLS: Worker compensation (epi.org + bls.gov)",90,85,80,75,90,75,75,90))
ideas.append(mk("haw007","The US Spends More on Healthcare Than Any Country but Ranks 37th in Outcomes","Health spending per capita vs health outcomes index for OECD nations","XREF","World","Scatter plot","Health","OECD: Health spending + Bloomberg: Health efficiency (oecd.org + bloomberg.com)",85,80,80,75,85,70,75,90))
ideas.append(mk("haw008","Congress Members Net Worth vs Their Constituents Median Income","Average congressional member net worth vs district median income","XREF","US","Scatter plot","Elections","OpenSecrets: Member wealth + ACS: District income (opensecrets.org + census.gov)",80,80,70,80,85,65,80,85))
ideas.append(mk("haw009","The US Incarcerates More People Than China and Russia Combined","Total incarcerated population: US vs rest of world","CHART","World","Bar chart","Crime and Law Enforcement","World Prison Brief: Incarceration rates (prisonstudies.org)",85,70,80,80,90,70,70,90))
ideas.append(mk("haw010","Corporate Profits Hit Record Highs While Real Wages Stay Flat","S&P 500 profits vs real median wage indexed to 2000","CHART","US","Line chart","Economy","BEA: Corporate profits + BLS: Real median wage (bea.gov + bls.gov)",85,85,80,75,85,75,75,90))


# ── "Did You Know?" Series (mind-blowing single facts visualized) ──
ideas.append(mk("haw011","Half of Americas GDP Comes From Just 25 Counties","Top 25 counties by GDP contribution overlaid on map","MAP","US Counties","County choropleth","Economy","BEA: GDP by county (bea.gov)",75,80,80,85,65,85,75,90))
ideas.append(mk("haw012","More Americans Died of Overdoses in 2024 Than in the Entire Vietnam War","Annual overdose deaths vs Vietnam War total casualties","CHART","US","Bar chart","Health","CDC WONDER: Drug overdose + DoD: Vietnam casualty count (wonder.cdc.gov + dcas.dmdc.osd.mil)",90,80,80,80,90,70,80,90))
ideas.append(mk("haw013","The 3 Richest Americans Own More Than the Bottom 50%","Wealth distribution: top 3 individuals vs bottom 165 million","CHART","US","Bar chart","Economy","Forbes: Billionaire list + Federal Reserve: SCF (forbes.com + federalreserve.gov)",90,85,80,80,85,70,75,90))
ideas.append(mk("haw014","Texas Is Bigger Than Every Country in Europe Except Ukraine","Texas area vs European country areas overlaid","MAP","World","Special map","Geography & Environment","Natural Earth: Country boundaries (naturalearthdata.com)",50,65,70,85,35,90,80,90))
ideas.append(mk("haw015","If Amazon Were a Country It Would Have the 26th Largest GDP","Corporate revenue vs national GDPs ranked","CHART","World","Bar chart","Economy","Fortune 500: Revenue + World Bank: GDP (fortune.com + worldbank.org)",65,70,75,85,60,65,80,90))

# ── "Before and After" Series ──
ideas.append(mk("haw016","What American Cities Looked Like Before Highways Destroyed Them","Urban freeway construction dates overlaid with demolished neighborhood counts","MAP","US Metro","Special map","Transportation","FHWA: Highway history + Urban Renewal records (fhwa.dot.gov)",80,70,65,80,80,85,85,70))
ideas.append(mk("haw017","Satellite Images of Shrinking Lakes: Before and After","Aral Sea, Lake Chad, Great Salt Lake, Lake Mead surface area over time","CHART","World","Area chart","Climate","NASA: Landsat imagery + USGS: Lake levels (earthobservatory.nasa.gov + usgs.gov)",85,65,75,80,85,90,75,80))
ideas.append(mk("haw018","Detroit Population Then vs Now: A City That Lost 65% of Its People","Detroit population by decade 1950-2024 with peak annotation","CHART","US Metro","Bar chart","Demographics","Census: Decennial population Detroit (census.gov)",80,75,80,75,80,70,65,95))
ideas.append(mk("haw019","The Aral Sea Was the 4th Largest Lake in the World - Now Its Gone","Aral Sea surface area by year 1960-2024","CHART","World","Area chart","Geography & Environment","NASA: Aral Sea monitoring + UNEP (earthobservatory.nasa.gov + unep.org)",85,60,75,80,85,85,75,85))
ideas.append(mk("haw020","How Redlining in 1935 Still Shows Up in Satellite Temperature Maps","HOLC redlining grades vs urban heat island intensity in 2024","XREF","US Metro","Bivariate choropleth","Housing","U of Richmond: Mapping Inequality + Landsat: Surface temperature (dsl.richmond.edu + nasa.gov)",85,75,70,85,85,90,90,80))

# ── "Why Does X Predict Y?" Series ──
ideas.append(mk("haw021","Waffle House Density Predicts Hurricane Recovery Speed","Waffle Houses per capita vs FEMA average days to restore power by county","XREF","US Counties","Scatter plot","Geography & Environment","Waffle House: Locations + FEMA: Disaster recovery metrics (wafflehouse.com + fema.gov)",55,65,55,95,50,65,95,60))
ideas.append(mk("haw022","Dollar Tree Locations Predict Poverty Better Than Census Data","Dollar store density vs poverty rate by census tract","XREF","US Counties","Scatter plot","Economy","Census: CBP dollar stores + ACS: Poverty (census.gov)",70,80,70,85,65,70,85,85))
ideas.append(mk("haw023","Cracker Barrel Locations Almost Perfectly Predict Red Counties","Cracker Barrel locations vs 2024 Republican vote share by county","XREF","US Counties","Dot map","Elections","Cracker Barrel: Locations + MIT Election Lab (crackerbarrel.com + electionlab.mit.edu)",55,70,60,95,55,75,90,80))
ideas.append(mk("haw024","The Pirate Bay Downloads Predict Economic Inequality","Software piracy rate vs Gini coefficient by country","XREF","World","Scatter plot","Economy","BSA: Software piracy + World Bank: Gini (bsa.org + worldbank.org)",50,55,55,90,50,55,95,80))
ideas.append(mk("haw025","States Where People Google Am I Depressed Have Higher Suicide Rates","Google Trends depression-related search volume vs suicide rate","XREF","US States","Scatter plot","Health","Google Trends + CDC WONDER: Suicide (trends.google.com + wonder.cdc.gov)",70,75,60,85,75,65,85,75))

# ── "The Global Divide" Series ──
ideas.append(mk("haw026","Countries North of This Line Are Rich - Countries South Are Poor","GDP per capita divided at the Brandt Line (30°N latitude)","MAP","World","World choropleth","Economy","World Bank: GDP per capita + Brandt Line (worldbank.org)",70,65,70,85,70,80,80,90))
ideas.append(mk("haw027","The Vaccine Apartheid: Doses Per Capita Rich vs Poor Countries","COVID vaccine doses administered per 100 people by income group","CHART","World","Bar chart","Health","OWID: COVID vaccinations by income group (ourworldindata.org)",80,65,75,75,85,70,75,90))
ideas.append(mk("haw028","Global Internet Freedom Is Declining Every Year","Freedom House internet freedom scores 2015-2024 showing downward trend","CHART","World","Line chart","Science & Technology","Freedom House: Freedom on the Net (freedomhouse.org)",70,65,70,80,80,70,75,90))
ideas.append(mk("haw029","Women Do 75% of the Worlds Unpaid Work","Share of unpaid domestic work by gender across 75 countries","CHART","World","Bar chart","Labor","OECD/ILO: Time use surveys (oecd.org + ilo.org)",80,80,75,75,80,65,75,85))
ideas.append(mk("haw030","The Countries Getting More Authoritarian Outnumber Those Getting More Free","Net democracy score change by country 2013-2024","MAP","World","World choropleth","Elections","V-Dem: Liberal democracy index (v-dem.net)",75,60,70,80,85,80,75,90))

# ── Data Storytelling (complex multi-variable narratives) ──
ideas.append(mk("haw031","The Anatomy of a Food Desert: Income + Distance + Race + Health in One Map","Layered bivariate showing food access, income, racial composition, and diabetes","XREF","US Counties","Bivariate choropleth","Food & Nutrition","USDA: Food access + ACS + CDC: Diabetes (ers.usda.gov + census.gov + cdc.gov)",85,80,70,75,80,85,85,80))
ideas.append(mk("haw032","The Rust Belt Recovery Myth: Only Some Cities Bounced Back","GDP change, population change, and median wage change for 20 Rust Belt metros","CHART","US Metro","Bar chart","Economy","BEA: Metro GDP + ACS: Population + BLS: Wage (bea.gov + census.gov + bls.gov)",80,75,75,80,75,75,80,85))
ideas.append(mk("haw033","The Climate Gentrification Effect: Flood-Safe Neighborhoods Are Now the Most Expensive","FEMA flood zone vs median home price change 2015-2024 in coastal metros","XREF","US Metro","Scatter plot","Housing","FEMA: Flood maps + Zillow: ZHVI by zip (fema.gov + zillow.com)",75,75,65,85,75,75,90,75))
ideas.append(mk("haw034","The Prescription Paradox: Counties With Most Doctors Have Most Opioid Prescriptions","Physician density vs opioid prescription rate per capita","XREF","US Counties","Scatter plot","Health","HRSA: Physician supply + CDC: Opioid prescribing rate (hrsa.gov + cdc.gov)",65,65,65,90,75,65,90,85))
ideas.append(mk("haw035","The Military-to-Police Pipeline: Cities With Most Veteran Officers Use Most Force","Veteran share of police force vs use-of-force incidents per arrest","XREF","US Metro","Scatter plot","Crime and Law Enforcement","DOJ: Law enforcement demographics + Police Use of Force data (bjs.gov + various PD)",65,60,55,90,80,55,90,55))

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
    print(f"Injected {len(new_ideas)} new ideas (HAW batch)")
