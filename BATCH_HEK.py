import re, os
DATA = os.path.join(os.path.dirname(__file__), 'data.js')

def mk(id,title,sub,typ,geo,fmt,sect,tbl,e,r,c,s,t,v,o,dr):
    raw=v*3.0+e*2.5+s*2.0+o*1.75+t*1.75+r*2.0+c*1.5
    base=raw/14.5
    fl=0.85 if min(e,r,c,s,t,v,o)<35 else 1.0
    pen=1.0-0.35*(1.0-dr/100.0)
    vs=int(base*fl*pen)
    return ('{id:"'+id+'",title:"'+title+'",sub:"'+sub+'",type:"'+typ+'",'
            'geo:"'+geo+'",fmt:"'+fmt+'",section:"'+sect+'",tbl:"'+tbl+'",'
            'sc:{emotional:'+str(e)+',relatability:'+str(r)+',clarity:'+str(c)
            +',surprise:'+str(s)+',tension:'+str(t)+',visual:'+str(v)
            +',originality:'+str(o)+',data_ready:'+str(dr)+'}'
            ',vs:'+str(vs)+',topics:[],ext:[],status:"idea",notes:""}')

IDEAS = [
mk("hek01","Voter ID Law Strictness Spectrum","States ranked by voter ID requirement strictness mapped with voter turnout changes after implementation","MAP","usa","choropleth","Democracy & Voting","NCSL: Voter ID Laws + MIT Election Data (ncsl.org)",65,68,72,62,72,68,60,90),
mk("hek02","Ballot Initiative Industry","Money spent per state ballot initiative mapped with out-of-state funding sources","MAP","usa","choropleth","Democracy & Voting","FollowTheMoney + Ballotpedia (followthemoney.org)",62,58,68,74,68,66,72,82),
mk("hek03","Ranked Choice Voting Adoption Wave","Cities and states that have adopted ranked choice voting mapped with implementation timeline","MAP","usa","dot-density","Democracy & Voting","FairVote: RCV Tracker (fairvote.org)",50,52,74,68,48,68,68,88),
mk("hek04","Election Worker Threats Geography","Reported threats against election workers by state mapped with worker resignation rates","MAP","usa","choropleth","Democracy & Voting","Brennan Center: Election Worker Survey (brennancenter.org)",72,62,68,70,80,66,68,78),
mk("hek05","Gerrymandering Efficiency Gap","Congressional district compactness scores vs. partisan lean deviation from state average","MAP","usa","choropleth","Democracy & Voting","DRA + PlanScore (planscore.org)",58,55,62,68,70,72,65,88),
mk("hek06","Felony Disenfranchisement Patchwork","Voting rights restoration policies for people with felony convictions by state with affected population size","MAP","usa","choropleth","Democracy & Voting","Sentencing Project (sentencingproject.org)",68,60,70,68,72,68,62,90),
mk("hek07","Campaign Dollar Per Vote","Total campaign spending divided by votes received for every congressional race showing cost per vote won","CHART","usa","scatter","Democracy & Voting","FEC: Campaign Finance (fec.gov)",58,62,72,72,60,62,70,90),
mk("hek08","Polling Place Wait Time Inequality","Average wait times to vote by precinct mapped with racial demographics of voting district","MAP","usa","bivariate-choropleth","Democracy & Voting","MIT: Election Performance (electionlab.mit.edu)",72,68,70,70,74,68,65,82),
mk("hek09","Democracy Backsliding Index","Countries losing democratic freedoms fastest over 10 years from V-Dem mapped with trigger events","MAP","world","choropleth","Democracy & Voting","V-Dem: Democracy Report (v-dem.net)",65,48,68,72,72,72,62,88),
mk("hek10","Xylazine Tranq Dope Spread","Cities where xylazine has been detected in the drug supply mapped with wound prevalence and treatment gaps","MAP","usa","dot-density","Drugs & Substance Use","DEA: Emerging Threat Reports (dea.gov)",72,55,68,78,78,68,72,78),
mk("hek11","Cannabis Tax Revenue Allocation","How each legal cannabis state actually spends marijuana tax revenue broken down by category","CHART","usa","bar-chart","Drugs & Substance Use","State Revenue Departments (tax.gov)",55,68,74,72,52,62,68,88),
mk("hek12","Psychedelic Therapy Legalization Wave","States and cities that have decriminalized or legalized psilocybin for therapeutic use with timeline","MAP","usa","dot-density","Drugs & Substance Use","MAPS: Psychedelic Policy (maps.org)",55,52,72,72,48,68,72,82),
mk("hek13","Narco Submarine Interdiction Map","Drug submarine and semi-submersible vessel seizures mapped with estimated route corridors","MAP","world","dot-density","Drugs & Substance Use","JIATF South + USCG (southcom.mil)",58,38,65,82,72,78,78,72),
mk("hek14","Kratom Legal Status Patchwork","Kratom legality by state and county with poison control call rates and ER visits","MAP","usa","choropleth","Drugs & Substance Use","AAPCC: Kratom Reports (aapcc.org)",48,52,70,72,55,64,70,78),
mk("hek15","Opioid Settlement Money Trail","Opioid lawsuit settlement payments received by state vs. amount actually spent on addiction services","MAP","usa","bivariate-choropleth","Drugs & Substance Use","KFF: Opioid Settlement Tracker (kff.org)",68,62,70,74,72,68,68,85),
mk("hek16","Drug Price Markup Chain","Cost of common drugs from production through distribution to patient showing markup at each step","CHART","usa","bar-chart","Drugs & Substance Use","WHO: Pharmaceutical Pricing (who.int)",65,72,72,74,68,60,68,75),
mk("hek17","Meth Lab Cleanup Sites","Former methamphetamine lab locations listed on DEA cleanup registry mapped with current property values","MAP","usa","dot-density","Drugs & Substance Use","DEA: National Clandestine Lab Register (dea.gov)",55,58,72,72,62,70,70,88),
mk("hek18","Nitrous Oxide Abuse Hotspots","Cities with highest rates of nitrous oxide canister litter reports mapped with ER visits for N2O","MAP","usa","dot-density","Drugs & Substance Use","EPA Litter Data + AAPCC (epa.gov)",48,52,68,74,55,68,72,72),
mk("hek19","Aquifer Depletion Countdown","Major US aquifers mapped with estimated years until depletion at current extraction rates","MAP","usa","choropleth","Agriculture & Food Systems","USGS: Groundwater Depletion (usgs.gov)",72,62,72,74,78,74,68,85),
mk("hek20","Farm Subsidy Millionaires","Top farm subsidy recipients mapped by county showing payments exceeding 1M dollars","MAP","usa","dot-density","Agriculture & Food Systems","EWG: Farm Subsidy Database (farm.ewg.org)",62,58,72,76,68,68,72,92),
mk("hek21","Almond Water Footprint Map","Water consumed per acre for almond orchards in California mapped against drought severity","MAP","usa","bivariate-choropleth","Agriculture & Food Systems","CDFA + USDA NASS (cdfa.ca.gov)",60,58,72,72,68,72,65,88),
mk("hek22","Vertical Farm Locations vs. Food Deserts","Indoor vertical farm locations mapped against USDA food desert classifications","MAP","usa","dot-density","Agriculture & Food Systems","USDA + Indoor Agriculture Association (ers.usda.gov)",52,55,70,72,48,70,72,78),
mk("hek23","Pesticide Drift Complaints","Reported pesticide drift incidents mapped with proximity to schools and residential areas","MAP","usa","dot-density","Agriculture & Food Systems","EPA: Pesticide Incident Reports (epa.gov)",68,62,68,70,72,68,65,82),
mk("hek24","Farmland Foreign Ownership","Foreign-owned agricultural land by country of owner mapped by state with acreage totals","MAP","usa","choropleth","Agriculture & Food Systems","USDA AFIDA: Foreign Holdings (usda.gov)",58,58,72,76,68,70,68,90),
mk("hek25","Bee Colony Collapse Geography","Honeybee colony loss rates by state mapped with neonicotinoid pesticide usage rates","MAP","usa","bivariate-choropleth","Agriculture & Food Systems","USDA NASS: Honey Bee Survey (nass.usda.gov)",68,58,70,68,70,72,62,88),
mk("hek26","Soil Erosion Rate by Farming Practice","Topsoil loss rates mapped by county comparing conventional tillage vs. no-till farming areas","MAP","usa","bivariate-choropleth","Agriculture & Food Systems","USDA NRCS: Soil Survey (nrcs.usda.gov)",58,48,68,68,68,70,65,85),
mk("hek27","Asylum Case Backlog by Court","Immigration court asylum case backlog by judicial district mapped with average wait time in years","MAP","usa","choropleth","Immigration & Migration","TRAC: Immigration Court Data (trac.syr.edu)",68,60,72,72,72,68,62,90),
mk("hek28","Sanctuary Policy Spectrum","Cities and counties on the spectrum from full sanctuary to full cooperation with ICE mapped with detainer compliance","MAP","usa","choropleth","Immigration & Migration","ICE ERO + CIS Reports (ice.gov)",62,58,70,62,72,68,60,85),
mk("hek29","Remittance Corridors","Money sent home by immigrants mapped from US metros to destination countries with volume flows","MAP","world","flow-map","Immigration & Migration","World Bank: Remittance Prices (remittanceprices.worldbank.org)",58,62,70,68,52,76,68,88),
mk("hek30","H-1B Visa Employer Concentration","Companies filing the most H-1B visa petitions mapped with approval rates and median salary offered","CHART","usa","bar-chart","Immigration & Migration","DOL: H-1B Disclosure Data (dol.gov)",55,60,74,68,58,60,62,92),
mk("hek31","Unaccompanied Minor Placement Map","Where unaccompanied migrant children are placed with sponsors mapped with school enrollment surges","MAP","usa","dot-density","Immigration & Migration","ORR: Unaccompanied Children (acf.hhs.gov)",72,58,68,72,74,68,65,82),
mk("hek32","Immigration Judge Denial Rate Lottery","Asylum denial rates by individual immigration judge showing variance within same courthouse","CHART","usa","bar-chart","Immigration & Migration","TRAC: Judge-by-Judge Data (trac.syr.edu)",65,55,70,80,72,58,74,90),
mk("hek33","Visa Overstay vs. Border Crossing Numbers","Annual visa overstays compared to illegal border crossings as share of total undocumented entries","CHART","usa","area-chart","Immigration & Migration","DHS: Entry/Exit Overstay Report (dhs.gov)",55,58,72,76,62,60,68,85),
mk("hek34","Immigrant Business Formation Rate","New business formation rate by immigrant vs. native-born entrepreneurs by metro area","CHART","usa","grouped-bar","Immigration & Migration","Census: Annual Business Survey (census.gov)",55,62,72,72,48,58,68,85),
mk("hek35","Climate Refugee Projection Map","Regions projected to produce the most climate migrants by 2050 mapped with destination predictions","MAP","world","flow-map","Immigration & Migration","World Bank: Groundswell Report (worldbank.org)",68,52,65,74,72,76,72,78),
]

raw = open(DATA, 'r', encoding='utf-8').read()
existing = set(re.findall(r'id:"(hek\d+)"', raw))
new_ideas = [i for i in IDEAS if re.search(r'id:"(hek\d+)"', i).group(1) not in existing]
print(f"Injecting {len(new_ideas)} new ideas (skipping {len(IDEAS)-len(new_ideas)} dupes)")
if new_ideas:
    tail = ']; // end D'
    assert tail in raw, "Cannot find tail marker"
    raw = raw.replace(tail, ',\n'.join(new_ideas) + ',\n' + tail)
    open(DATA, 'w', encoding='utf-8').write(raw)
    print("Done")
else:
    print("Nothing to inject")
