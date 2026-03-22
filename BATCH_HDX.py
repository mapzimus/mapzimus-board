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
mk("hdx01","Gerrymandering Efficiency Gap","Partisan efficiency gap scores by congressional district with compactness overlay","MAP","usa","choropleth","Politics & Governance","Princeton Gerrymandering Project (gerrymander.princeton.edu)",65,62,72,68,74,78,66,85),
mk("hdx02","Voter ID Law Strictness Map","Voter ID requirements by state ranked by strictness with turnout change after enactment","MAP","usa","choropleth","Politics & Governance","NCSL: Voter ID Laws (ncsl.org)",68,72,74,60,72,68,58,88),
mk("hdx03","Democracy Backsliding Index","Countries ranked by democratic erosion metrics — press freedom, judicial independence, election integrity","MAP","world","choropleth","Politics & Governance","V-Dem: Democracy Indices (v-dem.net)",72,58,70,68,78,74,68,85),
mk("hdx04","Ranked Choice Voting Adoption","Cities and states using ranked choice voting mapped with voter satisfaction surveys","MAP","usa","dot-density","Politics & Governance","FairVote: RCV Data (fairvote.org)",58,62,74,68,55,66,70,82),
mk("hdx05","Dark Money in State Elections","Untraceable political spending per capita in state-level races by state","MAP","usa","choropleth","Politics & Governance","OpenSecrets: Dark Money (opensecrets.org)",68,62,68,74,76,64,70,80),
mk("hdx06","Election Denial Candidates","Candidates who denied 2020 election results mapped by district with win/loss outcomes","MAP","usa","dot-density","Politics & Governance","States United: Candidates (statesuniteddemocracy.org)",72,65,68,70,78,72,65,82),
mk("hdx07","Polling Place Closures Since Shelby","Polling locations closed since Shelby County v. Holder by county with demographic data","MAP","usa","dot-density","Politics & Governance","Leadership Conference: Polling Place Report (civilrights.org)",74,62,70,72,80,74,68,82),
mk("hdx08","Fentanyl Seizure Hot Zones","DEA fentanyl seizure locations by weight mapped with overdose death clusters","MAP","usa","dot-density","Health & Wellbeing","DEA: Drug Seizure Data (dea.gov)",78,68,70,65,82,74,62,82),
mk("hdx09","Opioid Prescribing Rate by County","Opioid prescriptions per 100 persons by county mapped with addiction treatment facility access","MAP","usa","bivariate-choropleth","Health & Wellbeing","CDC: Opioid Prescribing Maps (cdc.gov/opioids)",75,72,74,60,76,70,55,90),
mk("hdx10","Cannabis Tax Revenue vs. Promises","Marijuana tax revenue collected vs. amount promised during legalization campaigns by state","CHART","usa","grouped-bar","Economy & Trade","MJBizDaily: Tax Revenue (mjbizdaily.com)",58,68,74,72,62,58,66,85),
mk("hdx11","Meth Lab Cleanup Sites","Former methamphetamine production sites on the National Clandestine Lab Register by county","MAP","usa","dot-density","Public Safety","DEA: Clandestine Lab Register (dea.gov)",65,58,68,72,70,74,60,88),
mk("hdx12","Drug Court Success Rates","Drug court program completion rates vs. recidivism mapped by judicial district","MAP","usa","bivariate-choropleth","Law & Justice","NADCP: Drug Court Data (nadcp.org)",68,62,70,65,60,62,64,80),
mk("hdx13","Kratom Legal Status Patchwork","States and municipalities where kratom is banned, regulated, or unregulated","MAP","usa","choropleth","Health & Wellbeing","AKA: Kratom Legality Map (americankratom.org)",52,55,68,72,58,62,68,78),
mk("hdx14","Cocaine Trafficking Routes","Major cocaine flow paths from source countries to US markets with seizure volumes","MAP","world","flow-map","Conflict & Security","UNODC: World Drug Report (unodc.org/wdr)",62,50,68,65,72,78,64,75),
mk("hdx15","Farm Bankruptcies by Region","Chapter 12 farm bankruptcy filings per 1000 farms by agricultural district over 20 years","MAP","usa","choropleth","Agriculture & Food","USDA ERS: Farm Finance (ers.usda.gov)",70,65,72,62,72,68,58,85),
mk("hdx16","Pollinator Decline and Crop Yields","Bee colony losses by state mapped against pollinator-dependent crop production trends","MAP","usa","bivariate-choropleth","Agriculture & Food","USDA NASS: Honey Bee Survey (nass.usda.gov)",68,62,70,74,72,72,70,82),
mk("hdx17","Aquifer Depletion Rates","Major aquifer water level decline rates mapped with irrigation dependency percentages","MAP","usa","choropleth","Environment & Climate","USGS: Groundwater Data (waterdata.usgs.gov)",72,60,74,70,78,76,68,88),
mk("hdx18","SNAP Benefits vs. Fresh Food Access","SNAP participation rates by county overlaid with USDA food desert classifications","MAP","usa","bivariate-choropleth","Poverty & Inequality","USDA: SNAP Data + Food Access (fns.usda.gov)",72,75,70,62,68,70,58,90),
mk("hdx19","Farmworker Heat Deaths","Agricultural worker heat-related deaths by county mapped with average summer temperatures","MAP","usa","dot-density","Labor & Work","BLS: CFOI (bls.gov/iif/oshcfoi1.htm)",80,65,68,72,82,70,68,75),
mk("hdx20","Soil Erosion Severity","Topsoil loss rates by county in tons per acre per year mapped against tillage practices","MAP","usa","choropleth","Agriculture & Food","USDA NRCS: NRI Data (nrcs.usda.gov)",60,52,72,68,65,74,66,85),
mk("hdx21","Foreign Ownership of US Farmland","Acres of US farmland owned by foreign entities by state with country-of-origin breakdown","MAP","usa","choropleth","Agriculture & Food","USDA: AFIDA Report (usda.gov/afida)",62,68,72,78,72,70,68,85),
mk("hdx22","Asylum Backlog by Immigration Court","Pending asylum cases per judge mapped by immigration court location with wait times","MAP","usa","proportional-symbol","Migration & Borders","TRAC: Immigration Court Data (trac.syr.edu)",72,62,70,68,76,70,62,85),
mk("hdx23","Deportation Flight Routes","ICE Air Operations deportation flight paths by frequency with destination country","MAP","world","flow-map","Migration & Borders","ICE: ERO Data + Flight Records (ice.gov)",68,55,65,72,78,76,70,72),
mk("hdx24","Immigrant Entrepreneurship Rates","Business ownership rates by nativity status and country of origin by metro area","MAP","usa","choropleth","Economy & Trade","Census: SBO + ACS (census.gov/programs-surveys/sbo)",58,62,72,70,52,64,68,85),
mk("hdx25","Sanctuary City Policy Map","Cities and counties with sanctuary policies mapped against ICE detainer compliance rates","MAP","usa","choropleth","Migration & Borders","CIS: Sanctuary Jurisdictions (cis.org)",65,62,70,60,72,68,58,85),
mk("hdx26","Unaccompanied Minor Releases","Counties where unaccompanied migrant children were released to sponsors mapped with school enrollment","MAP","usa","dot-density","Migration & Borders","ORR: UC Program Data (acf.hhs.gov)",72,60,65,68,74,70,64,78),
mk("hdx27","Remittance Flows from the US","Total remittances sent from the US to recipient countries with per capita impact on receiving end","MAP","world","flow-map","Economy & Trade","World Bank: Remittance Data (worldbank.org/remittances)",58,62,72,65,50,74,62,88),
mk("hdx28","H-1B Visa Employer Concentration","Top H-1B sponsoring employers by metro area with median wage offered vs. local median","MAP","usa","proportional-symbol","Labor & Work","DOL: H-1B Disclosure Data (dol.gov/agencies/eta)",60,65,74,68,62,66,60,90),
mk("hdx29","Voter Turnout in Midterms vs. Presidential","Voter turnout gap between midterm and presidential elections by county over 20 years","CHART","usa","line-chart","Politics & Governance","EAC: Election Administration Survey (eac.gov)",60,68,72,58,55,60,62,88),
mk("hdx30","Lobbyist-to-Lawmaker Ratio","Registered lobbyists per elected official at state and federal level over time","CHART","usa","bar-chart","Politics & Governance","OpenSecrets: Lobbying Data (opensecrets.org)",62,65,70,74,68,58,70,85),
mk("hdx31","Crop Insurance Payouts and Climate","Federal crop insurance indemnity payments by county over 20 years mapped against drought severity","MAP","usa","bivariate-choropleth","Agriculture & Food","USDA RMA: Summary of Business (rma.usda.gov)",62,58,72,68,65,72,62,88),
mk("hdx32","Refugee Resettlement Capacity Collapse","Annual refugee admissions by resettlement city vs. federal ceiling over 20 years","CHART","usa","area-chart","Migration & Borders","State Dept: Refugee Admissions (state.gov/refugee-admissions)",74,62,70,65,72,60,62,85),
mk("hdx33","Coca Cultivation Satellite Tracking","Coca-growing regions in Colombia, Peru, and Bolivia tracked by satellite over 15 years","MAP","south-america","choropleth","Conflict & Security","UNODC: Coca Monitoring (unodc.org)",58,48,70,68,72,78,66,80),
mk("hdx34","Local News Deserts and Voter Turnout","Counties that lost their last local newspaper mapped against changes in voter participation","MAP","usa","bivariate-choropleth","Media & Information","Northwestern: News Desert Project (localnewsinitiative.northwestern.edu)",72,68,70,74,68,70,72,82),
mk("hdx35","DACA Recipient Geography","Estimated DACA-eligible and active DACA recipients by metro area with economic contribution","MAP","usa","proportional-symbol","Migration & Borders","MPI: DACA Data (migrationpolicy.org)",70,65,72,62,68,68,60,85),
]

# --- inject ---
with open(DATA, 'r', encoding='utf-8') as f:
    txt = f.read()
ids = set(re.findall(r'id:"([^"]+)"', txt))
new = [i for i in IDEAS if re.search(r'id:"([^"]+)"', i).group(1) not in ids]
if not new:
    print("All 35 ideas already present"); exit()
tail = "]; // end D"
txt = txt.replace(tail, ",\n".join(new) + ",\n" + tail)
with open(DATA, 'w', encoding='utf-8') as f:
    f.write(txt)
print(f"Injected {len(new)} new ideas (HDX batch)")
