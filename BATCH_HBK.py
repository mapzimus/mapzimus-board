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
# === Children × International ===
mk("HBK01","Child Labor Rates by Country in 2024","160 million children still work and heres where","MAP","World","World choropleth","Children|International|Labor","ILO: Child Labour Statistics (ilo.org); UNICEF: State of Worlds Children (unicef.org)",82,68,78,78,80,78,68,85),
mk("HBK02","Child Marriage Rates by Country","Where girls under 18 are still legally married","MAP","World","World choropleth","Children|International|Gender","UNICEF: Child Marriage Data (unicef.org); Girls Not Brides (girlsnotbrides.org)",82,68,75,78,80,78,68,88),
mk("HBK03","School Lunch Quality by Country","What kids eat for lunch in Japan vs. the US vs. France vs. Brazil","RANK","World","Bar chart","Children|International|Food","WFP: School Feeding (wfp.org); USDA: School Nutrition (fns.usda.gov)",68,78,78,78,62,68,75,72),
# === Manufacturing × Economy ===
mk("HBK04","Americas Most Valuable Manufactured Exports","We still make a lot — its just not what it used to be","RANK","US-national","Treemap","Manufacturing|Economy|Trade","Census: Foreign Trade (census.gov); BEA: Industry GDP (bea.gov)",65,62,78,72,60,72,65,90),
mk("HBK05","Manufacturing Jobs Lost vs. Manufacturing Output Gained","We make more stuff with fewer people than ever","CHART","US-national","Line chart","Manufacturing|Economy|Technology","BLS: Manufacturing Employment (bls.gov); Fed: Industrial Production (federalreserve.gov)",72,70,80,82,72,68,72,92),
mk("HBK06","The Geography of American Manufacturing in 2024","Where factory jobs still exist and what they produce","MAP","US-county","County choropleth","Manufacturing|Economy|Geography","BLS: QCEW Manufacturing (bls.gov); Census: Annual Survey of Manufactures (census.gov)",65,68,78,70,62,80,65,90),
# === Psychology × Demographics ===
mk("HBK07","The Loneliness Epidemic by Age Group","Gen Z reports the highest loneliness scores","CHART","US-national","Bar chart","Psychology|Demographics|Health","Cigna: Loneliness Index (cigna.com); Harvard: Making Caring Common (gse.harvard.edu)",82,82,78,78,78,65,72,75),
mk("HBK08","Trust in Institutions by Generation","Boomers still trust banks and media — Gen Z trusts almost nothing","CHART","US-national","Line chart","Psychology|Demographics|Politics","Gallup: Confidence in Institutions (gallup.com); Pew: Generational Data (pewresearch.org)",75,78,78,78,72,68,72,85),
mk("HBK09","Happiness U-Curve: Life Satisfaction by Age","Happiness bottoms out at 47 then climbs back up everywhere on Earth","CHART","World","Line chart","Psychology|Demographics|International","Brookings: Happiness Curve (brookings.edu); World Happiness Report (worldhappiness.report)",72,78,78,82,62,65,75,82),
# === Energy × Geography ===
mk("HBK10","Americas Energy Production Map by Type","Every oil well wind turbine solar farm and coal mine","MAP","US-national","Dot map","Energy|Geography","EIA: Layer Information for Interactive Maps (eia.gov); LBNL: Wind and Solar (lbl.gov)",62,58,78,68,58,88,65,92),
mk("HBK11","The Grid Vulnerability Map","US power grid weak points and areas prone to blackouts","MAP","US-national","Special map","Energy|Infrastructure|Geography","EIA: Electric Grid Monitor (eia.gov); DOE: Grid Modernization (energy.gov)",72,72,72,75,75,82,72,78),
mk("HBK12","Coal Mine to Solar Farm Conversions","Repurposed energy sites across Appalachia and the Midwest","MAP","US-state","Dot map","Energy|Geography|Economy","MSHA: Mine Data (msha.gov); SEIA: Solar Projects (seia.org)",68,62,72,78,68,80,78,72),
# === Drugs × International ===
mk("HBK13","Cannabis Legal Status in Every Country","The global patchwork from fully legal to death penalty","MAP","World","World choropleth","Drugs|International|Law","EMCDDA: Cannabis Policy (emcdda.europa.eu); NORML: World Laws (norml.org)",65,68,78,72,62,78,62,85),
mk("HBK14","Opioid Consumption Per Capita by Country","The US consumes 80% of the worlds opioids with 4% of the population","MAP","World","World choropleth","Drugs|International|Health","INCB: Narcotic Drugs Report (incb.org); WHO: Access to Medicines (who.int)",80,72,78,85,78,78,72,85),
mk("HBK15","Global Cocaine Trafficking Routes","From production in South America to consumption in North America and Europe","MAP","World","Line map","Drugs|International|Crime","UNODC: World Drug Report (unodc.org)",70,58,72,72,72,85,68,78),
# === Finance × International ===
mk("HBK16","Tax Haven Money Flows Visualized","How trillions move through tiny island nations","MAP","World","Line map","Finance|International|Economy","Tax Justice Network: Financial Secrecy Index (taxjustice.net); IMF: Coordinated Portfolio Investment (imf.org)",75,65,68,80,78,82,75,72),
mk("HBK17","Household Debt to Income Ratio by Country","Which nations citizens are most leveraged","MAP","World","World choropleth","Finance|International|Economy","BIS: Credit to Households (bis.org); OECD: Household Debt (oecd.org)",72,72,78,72,68,78,68,88),
mk("HBK18","Cryptocurrency Adoption by Country","Some developing nations lead wealthy ones in crypto usage","MAP","World","World choropleth","Finance|Technology|International","Chainalysis: Geography of Cryptocurrency (chainalysis.com); World Bank: Financial Inclusion (worldbank.org)",65,65,72,78,62,78,75,78),
# === Poverty × Race ===
mk("HBK19","Native American Reservation Poverty Rates","The highest poverty rates in America are on reservations","MAP","US-national","Dot map","Poverty|Race|History","Census: ACS American Indian (census.gov); BIA: Indian Entities (bia.gov)",88,72,72,78,85,80,72,85),
mk("HBK20","Redlining Impact on Present-Day Poverty by Race","1930s racist housing policy still visible in todays poverty maps","XREF","US-city","Bivariate choropleth","Poverty|Race|Housing|History","U of Richmond: Mapping Inequality (dsl.richmond.edu); Census: ACS Poverty by Race (census.gov)",88,78,72,80,85,80,78,82),
# === Climate × International ===
mk("HBK21","Countries Contributing Most to Climate Change vs. Countries Most Affected","The polluters and the victims are almost entirely different","XREF","World","Bivariate choropleth","Climate|International|Inequality","Global Carbon Project (globalcarbonproject.org); ND-GAIN: Climate Vulnerability (gain.nd.edu)",82,68,72,82,82,80,75,88),
mk("HBK22","Climate Refugees: Where People Are Already Moving Due to Climate","Island nations coastal communities and drought regions losing population","MAP","World","Dot map","Climate|International|Immigration","IDMC: Internal Displacement (internal-displacement.org); World Bank: Groundswell (worldbank.org)",80,65,68,78,80,80,78,75),
mk("HBK23","Glacier Retreat Before and After Photos Mapped","Every major glacier that has visibly shrunk since 1900","MAP","World","Dot map","Climate|Science|International","NSIDC: Glacier Data (nsidc.org); WGMS: Glacier Monitoring (wgms.ch)",78,62,72,78,78,85,72,85),
# === Law × Economy ===
mk("HBK24","Cost of a Lawyer by State vs. Median Income","Legal representation is effectively unaffordable for most Americans","XREF","US-state","Scatter plot","Law|Economy|Inequality","NALP: Lawyer Salary Data (nalp.org); Census: Median Income (census.gov)",78,78,75,78,75,65,72,78),
mk("HBK25","Time From Arrest to Trial by State","Justice delayed is justice denied — some states average 2+ years","RANK","US-state","Bar chart","Law|Crime","BJS: State Court Processing (bjs.gov); NCSC: Court Statistics (ncsc.org)",75,72,75,78,78,65,72,78),
# === Middle East × Economy ===
mk("HBK26","Oil Revenue Per Citizen in Every Middle Eastern Country","From Qatars 60K per person to Yemens near zero","RANK","World","Bar chart","Middle East|Economy|Energy","OPEC: Annual Statistical Bulletin (opec.org); World Bank: Population (worldbank.org)",68,62,78,78,68,68,72,88),
mk("HBK27","Middle East Water Scarcity vs. Agricultural Output","Farming in the desert with borrowed time and desalinated water","XREF","World","Scatter plot","Middle East|Agriculture|Environment","FAO: AQUASTAT (fao.org/aquastat); World Bank: Agriculture Data (worldbank.org)",72,58,72,78,72,68,75,82),
# === Sports × International ===
mk("HBK28","Soccer Spending vs. World Cup Performance","Money doesnt always buy trophies but it helps","XREF","World","Scatter plot","Sports|International|Economy","Transfermarkt: Club Values (transfermarkt.com); FIFA: World Cup Results (fifa.com)",62,65,78,72,55,65,68,82),
mk("HBK29","Olympic Host City Spending vs. Economic Return","Most Olympics lose money — heres the data","XREF","World","Scatter plot","Sports|International|Economy","IOC: Host City Reports (olympics.com); Oxford: Olympic Cost Data (oxfordolympics.com)",68,62,75,82,68,65,78,78),
# === Rural × Economy ===
mk("HBK30","Brain Drain Map: Counties Losing Their College Graduates","Young educated people leave and dont come back","MAP","US-county","County choropleth","Rural|Economy|Education|Demographics","Census: ACS Migration (census.gov); Census: ACS Educational Attainment (census.gov)",78,72,75,75,75,80,72,85),
mk("HBK31","Dollar General and Family Dollar Locations vs. Grocery Stores","The rural retail landscape is dominated by dollar stores","MAP","US-county","Bivariate choropleth","Rural|Economy|Food","ScrapeHero: Retail Locations; USDA: Food Environment Atlas (ers.usda.gov)",75,72,72,78,72,78,75,72),
# === Immigration × Education ===
mk("HBK32","Immigrants Educational Attainment vs. Native-Born by Country","In many countries immigrants are MORE educated than locals","XREF","World","Bar chart","Immigration|Education|International","OECD: Education of Immigrants (oecd.org); Census: ACS Education by Nativity (census.gov)",68,68,75,82,65,65,78,82),
mk("HBK33","DACA Recipients by State and Their Economic Contribution","700K young people and billions in GDP","MAP","US-state","State choropleth","Immigration|Education|Economy","USCIS: DACA Data (uscis.gov); FWD.us: Economic Impact (fwd.us)",78,72,75,72,72,78,70,82),
# === Science × Environment ===
mk("HBK34","Species Extinction Rate vs. Historical Average","We are losing species 1000x faster than the natural background rate","CHART","World","Area chart","Science|Environment|History","IUCN: Red List (iucnredlist.org); Living Planet Report (livingplanetindex.org)",80,62,72,82,80,68,72,85),
mk("HBK35","Ocean Plastic Concentration Map","The five garbage patches and coastal pollution hotspots","MAP","World","Special map","Environment|International|Science","Ocean Cleanup: Plastic Tracker (theoceancleanup.com); Jambeck: Marine Debris (jambeck.engr.uga.edu)",78,65,72,75,78,85,70,82),
]

# --- inject ---
with open(DATA, 'r', encoding='utf-8') as f:
    txt = f.read()
ids = set(re.findall(r'id:"([^"]+)"', txt))
new = [i for i in IDEAS if re.search(r'id:"([^"]+)"', i).group(1) not in ids]
if not new:
    print("All HBK ideas already present"); exit()
tail = "]; // end D"
txt = txt.replace(tail, ",\n".join(new) + ",\n" + tail)
with open(DATA, 'w', encoding='utf-8') as f:
    f.write(txt)
print(f"Injected {len(new)} new ideas (HBK batch)")
