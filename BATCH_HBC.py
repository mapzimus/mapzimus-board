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
# === Transportation × Health ===
mk("HBC01","Car Commute Length vs. Obesity Rate by Metro","Longer drive to work correlates with higher BMI","XREF","US-metro","Scatter plot","Transportation|Health","Census: ACS Commuting (census.gov); CDC: BRFSS Obesity (cdc.gov/brfss)",78,82,75,72,68,65,70,85),
mk("HBC02","Cities With the Most Bike Infrastructure vs. Heart Disease","Protected bike lanes mapped against cardiovascular mortality","XREF","US-city","Scatter plot","Transportation|Health|Infrastructure","PeopleForBikes: City Ratings (peopleforbikes.org); CDC: Heart Disease Mortality (wonder.cdc.gov)",72,75,72,75,65,70,72,72),
mk("HBC03","Traffic Deaths per 100K vs. Speed Limit by State","The states with highest speed limits and their fatal crash rates","XREF","US-state","Scatter plot","Transportation|Health|Law","NHTSA: FARS Data (nhtsa.gov); IIHS: Speed Limit Laws (iihs.org)",75,78,80,72,72,68,65,92),
# === Children × Economy ===
mk("HBC04","Cost to Raise a Child by State","From birth to 18 adjusted for local cost of living","RANK","US-state","Bar chart","Children|Economy","USDA: Expenditures on Children (usda.gov); BLS: Regional Price Parities (bls.gov)",82,88,78,72,75,65,68,82),
mk("HBC05","Child Poverty Rate vs. State GDP Per Capita","Rich states with high child poverty rates are the real scandal","XREF","US-state","Scatter plot","Children|Economy|Inequality","Census: SAIPE Child Poverty (census.gov); BEA: GDP by State (bea.gov)",85,80,78,80,82,68,72,90),
mk("HBC06","Free School Lunch Eligibility Rate by County","A map of childhood hunger that looks like a map of everything else","MAP","US-county","County choropleth","Children|Economy|Food","USDA: National School Lunch Program (fns.usda.gov); Census: SAIPE (census.gov)",82,78,80,72,78,80,68,92),
# === Trade × History ===
mk("HBC07","Americas Top Trading Partner by Decade Since 1800","Animated shift from Britain to Canada to China","CHART","US-national","Animated bar chart","Trade|History|International","Census: Historical Foreign Trade (census.gov); USITC: DataWeb (usitc.gov)",70,65,78,78,68,72,72,88),
mk("HBC08","The Silk Road vs. Modern Shipping Routes","Ancient trade paths overlaid with todays container ship GPS tracks","MAP","World","Special map","Trade|History|International|Transportation","MarineTraffic: AIS Data (marinetraffic.com); UNESCO: Silk Road Database (unesco.org)",68,58,70,82,62,88,85,72),
mk("HBC09","Goods the US Used to Export That It Now Imports","Textiles steel electronics — the manufacturing reversal timeline","CHART","US-national","Area chart","Trade|History|Manufacturing","Census: Foreign Trade Historical (census.gov); BLS: Import/Export Price Indexes (bls.gov)",72,70,78,78,72,68,72,85),
# === Drugs × Geography ===
mk("HBC10","The Fentanyl Highway","DEA seizure locations mapped to show trafficking corridors","MAP","US-national","Line map","Drugs|Geography|Crime","DEA: National Drug Threat Assessment (dea.gov); CDC: Drug Overdose Maps (cdc.gov)",82,72,70,75,82,85,72,78),
mk("HBC11","Legal Weed Sales vs. Opioid Prescriptions by State","Do legal cannabis states see lower opioid use?","XREF","US-state","Scatter plot","Drugs|Health|Economy","BDSA: Cannabis Sales (bdsa.com); CDC: Opioid Prescribing (cdc.gov)",75,78,72,80,72,65,78,75),
mk("HBC12","Meth Labs Found Per Capita by County","The geography of methamphetamine production in America","MAP","US-county","County choropleth","Drugs|Geography|Crime","DEA: Clandestine Lab Registry (dea.gov)",72,68,75,72,75,82,68,82),
# === Prices × International ===
mk("HBC13","The Big Mac Index Map","How much a Big Mac costs in every country and what it says about purchasing power","MAP","World","World choropleth","Prices|International|Economy","The Economist: Big Mac Index (economist.com/big-mac-index)",68,78,82,75,58,78,65,92),
mk("HBC14","Price of a Liter of Gasoline in Every Country","From Venezuelas pennies to Hong Kongs dollars","MAP","World","World choropleth","Prices|International|Energy","GlobalPetrolPrices: Gasoline Prices (globalpetrolprices.com)",65,75,82,72,62,80,62,92),
mk("HBC15","What a Gallon of Milk Costs by State Adjusted for Wages","The real cost of basics when you factor in local earnings","RANK","US-state","Bar chart","Prices|Economy|Food","USDA: Retail Food Prices (ers.usda.gov); BLS: Average Wages (bls.gov)",72,82,78,70,65,65,68,88),
# === Space × Science ===
mk("HBC16","Every Object Humans Have Left in Space","Mapped orbits of 30000+ pieces of space debris","MAP","World","Special map","Space|Science|Technology","ESA: Space Debris Database (esa.int); UCS: Satellite Database (ucsusa.org)",68,58,72,80,65,90,78,88),
mk("HBC17","Light Pollution Map of Earth","Where you can and cannot see the Milky Way","MAP","World","World choropleth","Space|Science|Environment","NOAA: VIIRS Nighttime Lights (ngdc.noaa.gov); Light Pollution Atlas (lightpollutionmap.info)",70,72,78,72,62,92,70,90),
mk("HBC18","Every Meteorite Impact Site on Earth","Size and age of confirmed impact craters worldwide","MAP","World","Dot map","Space|Science|Geography","NASA: Meteoritical Bulletin Database (lpi.usra.edu); Earth Impact Database (impactearth.com)",62,55,75,78,58,88,75,90),
# === Finance × Demographics ===
mk("HBC19","Average Credit Score by ZIP Code","The credit score map of America reveals the same inequality patterns","MAP","US-county","County choropleth","Finance|Demographics|Inequality","Fed: Consumer Credit Panel (newyorkfed.org); Census: ACS Demographics (census.gov)",78,82,78,72,72,80,68,78),
mk("HBC20","Bank Branch Deserts","ZIP codes with zero bank branches overlaid with poverty rate","MAP","US-county","Bivariate choropleth","Finance|Demographics|Inequality","FDIC: Summary of Deposits (fdic.gov); Census: SAIPE (census.gov)",80,75,72,78,78,80,72,88),
mk("HBC21","Student Loan Default Rate by College","Which schools leave graduates most unable to repay","RANK","US-national","Bar chart","Finance|Education","ED: College Scorecard (collegescorecard.ed.gov)",82,85,78,75,78,62,68,92),
# === Middle East × War ===
mk("HBC22","Every US Military Base in the Middle East","The footprint of American military presence since 1990","MAP","World","Dot map","Middle East|War|Military","DoD: Base Structure Report (defense.gov); CENTCOM: Area of Responsibility (centcom.mil)",72,62,75,72,75,85,68,78),
mk("HBC23","Refugee Flows From Every Middle East Conflict Since 2000","Animated flows showing displacement paths","MAP","World","Line map","Middle East|War|Immigration","UNHCR: Refugee Statistics (unhcr.org); IDMC: Displacement Data (internal-displacement.org)",82,65,68,72,80,85,72,82),
# === Humor × Data ===
mk("HBC24","The Most Florida Man Headlines Per Capita by County","Geolocating every Florida Man news story","MAP","US-county","County choropleth","Humor|Crime|Geography","Google News: Florida Man Archive (news.google.com); Census: Population (census.gov)",60,78,72,82,50,78,85,55),
mk("HBC25","US States Ranked by How Often They Appear in Country Songs","Lyric mining 50 years of country music for state name-drops","RANK","US-state","State choropleth","Humor|Entertainment|Geography","Kaggle: Country Music Lyrics (kaggle.com/datasets); Census: Geography (census.gov)",55,72,75,80,48,78,82,60),
# === Race × Housing ===
mk("HBC26","Redlining Maps vs. Current Home Values","1930s HOLC neighborhood grades overlaid with 2024 Zillow values","MAP","US-city","Bivariate choropleth","Race|Housing|History","U of Richmond: Mapping Inequality (dsl.richmond.edu); Zillow: ZHVI (zillow.com/research)",88,78,72,80,85,82,75,82),
mk("HBC27","Racial Dot Map vs. School District Boundaries","How school borders reinforce residential segregation","MAP","US-city","Dot map","Race|Education|Housing","Census: ACS Race/Ethnicity (census.gov); NCES: School District Boundaries (nces.ed.gov)",85,75,70,78,82,85,75,88),
# === Poverty × Health ===
mk("HBC28","Life Expectancy Gap Between Richest and Poorest ZIP Codes","In some metros the gap is 20+ years across a few miles","XREF","US-metro","Bar chart","Poverty|Health|Inequality","CDC: US Small-area Life Expectancy (cdc.gov/nchs); Census: ACS Income (census.gov)",90,85,78,85,88,68,75,82),
mk("HBC29","Tooth Decay Rate by County Income Level","Dental health as a perfect proxy for poverty in America","XREF","US-county","Scatter plot","Poverty|Health","CDC: Oral Health Surveillance (cdc.gov/oralhealth); Census: SAIPE (census.gov)",72,78,75,78,70,65,75,72),
# === Democracy × International ===
mk("HBC30","Countries That Became Democracies vs. Countries That Stopped Being One","A two-directional flow since 1990","CHART","World","Area chart","Democracy|International|History","V-Dem: Democracy Indices (v-dem.net); Freedom House: Freedom in the World (freedomhouse.org)",78,62,72,80,78,72,78,88),
mk("HBC31","Voter Turnout in Every Democracy on Earth","The US ranks embarrassingly low among developed nations","RANK","World","Bar chart","Democracy|International|Politics","IDEA: Voter Turnout Database (idea.int)",72,75,82,78,72,68,65,92),
mk("HBC32","Press Freedom Index Mapped Against Internet Censorship","Countries that restrict both and countries that restrict only one","XREF","World","Bivariate choropleth","Democracy|International|Media","RSF: Press Freedom Index (rsf.org); Freedom House: FOTN (freedomhouse.org)",78,65,72,78,78,80,72,88),
# === Labor × Gender ===
mk("HBC33","The Gender Pay Gap by Occupation","Some jobs are nearly equal and others have 40% gaps","CHART","US-national","Bar chart","Labor|Gender|Inequality","BLS: Median Weekly Earnings by Sex (bls.gov); Census: ACS Earnings (census.gov)",82,85,80,72,78,68,65,92),
mk("HBC34","Paternity Leave Policies vs. Female Workforce Participation","Countries with paid paternity leave have more working women","XREF","World","Scatter plot","Labor|Gender|International","OECD: Family Database (oecd.org); ILO: LFPR by Sex (ilo.org)",75,72,72,80,72,68,78,82),
mk("HBC35","Percentage of Women in Congress Over Time by Party","One party changed dramatically and one barely moved","CHART","US-national","Area chart","Gender|Politics|History","CAWP: Women in Congress (cawp.rutgers.edu)",78,72,78,72,75,68,68,92),
]

# --- inject ---
with open(DATA, 'r', encoding='utf-8') as f:
    txt = f.read()
ids = set(re.findall(r'id:"([^"]+)"', txt))
new = [i for i in IDEAS if re.search(r'id:"([^"]+)"', i).group(1) not in ids]
if not new:
    print("All HBC ideas already present"); exit()
tail = "]; // end D"
txt = txt.replace(tail, ",\n".join(new) + ",\n" + tail)
with open(DATA, 'w', encoding='utf-8') as f:
    f.write(txt)
print(f"Injected {len(new)} new ideas (HBC batch)")
