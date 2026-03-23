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
mk("hem01","Qualified Immunity Shield Map","Police excessive force lawsuits dismissed due to qualified immunity by federal circuit with case outcomes","MAP","usa","choropleth","Law & Justice","Reuters: Shielded Database + PACER (reuters.com)",72,55,68,74,78,66,70,78),
mk("hem02","Mandatory Minimum Sentence Disparities","Average sentence length for identical drug charges by state mapped with racial demographics of sentenced","MAP","usa","choropleth","Law & Justice","USSC: Sourcebook + State Sentencing Commissions (ussc.gov)",72,58,70,72,76,66,62,88),
mk("hem03","Public Defender Caseload Crisis","Average cases per public defender by jurisdiction mapped against ABA recommended maximums","MAP","usa","choropleth","Law & Justice","NLADA: Defender Workload Study (nlada.org)",68,58,72,72,74,64,65,82),
mk("hem04","Civil Asset Forfeiture Revenue","Property seized by police without criminal conviction by state mapped with revenue to department budgets","MAP","usa","choropleth","Law & Justice","IJ: Policing for Profit (ij.org)",65,55,70,78,76,66,72,85),
mk("hem05","Jury Duty Compensation Map","Daily juror pay by state mapped against living wage with average trial length","MAP","usa","choropleth","Law & Justice","NCSC: Juror Compensation (ncsc.org)",52,72,74,72,52,64,68,90),
mk("hem06","Three Strikes Law Population","Prisoners serving life sentences under three strikes laws by state mapped with original third offense","MAP","usa","choropleth","Law & Justice","Stanford: Three Strikes Project (law.stanford.edu)",72,55,70,74,76,64,68,82),
mk("hem07","Algorithmic Bail Risk Scores","Jurisdictions using algorithmic risk assessment for bail decisions mapped with false positive rates by race","MAP","usa","dot-density","Law & Justice","Partnership on AI + ProPublica (propublica.org)",62,50,65,76,72,62,74,78),
mk("hem08","Witness Protection Program Geography","Approximate number of people in federal witness protection by decade with program cost per person","CHART","usa","bar-chart","Law & Justice","DOJ: WITSEC Reports (justice.gov)",55,45,62,78,68,58,75,65),
mk("hem09","Solitary Confinement Usage","Percentage of prison population in solitary confinement by state mapped with average duration","MAP","usa","choropleth","Law & Justice","Solitary Watch + BJS Census of Jails (solitarywatch.org)",75,50,70,72,78,64,65,82),
mk("hem10","Centenarian Clusters","Counties with the highest rates of residents aged 100+ mapped with lifestyle and healthcare factors","MAP","usa","dot-density","Demographics","Census ACS + CDC Mortality (census.gov)",58,58,72,74,42,70,72,88),
mk("hem11","Twin Birth Rate Geography","Twin and multiple birth rates by state over 20 years mapped with IVF clinic density","MAP","usa","bivariate-choropleth","Demographics","CDC: Natality Detail (cdc.gov/nchs)",48,58,72,76,40,68,74,92),
mk("hem12","Last Names That Map Ethnic History","Most common surnames by county revealing settlement patterns from 200 years of immigration","MAP","usa","choropleth","Demographics","Census: Frequently Occurring Surnames (census.gov)",55,68,68,78,42,72,80,90),
mk("hem13","Languages Spoken at Home Hyperlocal","Census tracts where a non-English language is dominant at home mapped by specific language","MAP","usa","choropleth","Demographics","Census ACS: Language Spoken at Home (census.gov)",55,65,72,72,45,72,68,92),
mk("hem14","Shrinking Middle Class by Metro","Percentage of households earning middle income by metro area over 30 years showing hollowing out","CHART","usa","line","Demographics","Pew: Income Tiers + Census CPS (pewresearch.org)",68,78,72,68,68,62,62,88),
mk("hem15","Pet Population Exceeds Child Population","Counties where registered pets outnumber children under 18 mapped with birth rate trends","MAP","usa","choropleth","Demographics","AVMA Pet Demographics + Census (avma.org)",42,68,72,80,38,68,78,82),
mk("hem16","Average Age at First Marriage Map","Median age at first marriage by county showing geographic and cultural variation","MAP","usa","choropleth","Demographics","Census ACS: Marital Status (census.gov)",52,72,74,68,45,68,62,92),
mk("hem17","Millennial vs. Boomer Population Crossover","The year millennials outnumbered boomers in each state mapped with economic implications","MAP","usa","choropleth","Demographics","Census: Population Estimates (census.gov)",55,72,72,68,48,68,65,90),
mk("hem18","Disability Rate Geography","Working-age disability rates by county mapped with available disability services and SSI approval rates","MAP","usa","bivariate-choropleth","Demographics","Census ACS + SSA (ssa.gov)",65,60,70,65,62,68,58,90),
mk("hem19","Water War Flashpoints","Transboundary water disputes in the Middle East mapped with dam construction and downstream impact","MAP","middle-east","special","Conflict & Security","Pacific Institute: Water Conflict Chronology (worldwater.org)",65,42,68,72,78,74,70,78),
mk("hem20","Qatars World Cup True Cost","Total infrastructure spending for 2022 World Cup by project mapped with migrant worker death estimates","MAP","middle-east","dot-density","Economy & Trade","Guardian Investigations + Qatar 2022 (theguardian.com)",72,48,68,74,78,70,72,80),
mk("hem21","Yemen Famine Severity Map","Yemen districts by IPC famine classification phase mapped with aid delivery access","MAP","middle-east","choropleth","Health & Medicine","WFP + IPC: Yemen (ipcinfo.org)",80,40,68,62,85,72,58,78),
mk("hem22","Irans Ethnic Mosaic","Ethnic and linguistic group distribution across Iran mapped with protest activity by region","MAP","middle-east","choropleth","Demographics","CIA World Factbook + Academic Sources (cia.gov)",55,38,68,70,68,74,70,75),
mk("hem23","Dubai vs. Abu Dhabi Economic Divergence","GDP composition and growth trajectory comparing Dubais tourism pivot vs. Abu Dhabis oil wealth","CHART","middle-east","grouped-bar","Economy & Trade","UAE Federal Statistics (fcsc.gov.ae)",48,40,72,68,52,62,65,85),
mk("hem24","Syrian Refugee Distribution","Syrian refugee populations by host country mapped with per capita refugee burden and aid received","MAP","middle-east","choropleth","Immigration & Migration","UNHCR: Syria Emergency (unhcr.org)",72,48,72,62,72,72,58,90),
mk("hem25","Strait of Hormuz Oil Transit Risk","Volume of oil transiting Strait of Hormuz daily mapped with military assets and incident history","MAP","middle-east","special","Energy & Resources","EIA: Hormuz Transit + IISS (eia.gov)",55,38,70,72,75,74,65,85),
mk("hem26","Israeli Settlement Growth Timeline","Israeli settlement population in the West Bank by year mapped with international recognition status","CHART","middle-east","area-chart","Politics & Governance","Peace Now: Settlement Watch (peacenow.org.il)",68,42,68,65,80,68,62,82),
mk("hem27","Gun Store to School Distance","Average distance from gun stores to the nearest school by state mapped with density of each","MAP","usa","bivariate-choropleth","Guns & Weapons","ATF FFL List + NCES School Data (atf.gov)",62,60,72,74,68,70,70,88),
mk("hem28","Hunting License Decline by Generation","Hunting license sales by age cohort over 30 years showing generational dropoff","CHART","usa","line","Guns & Weapons","USFWS: National Hunting License Report (fws.gov)",50,62,72,70,48,60,65,90),
mk("hem29","Accidental Child Shooting Geography","Accidental shootings involving children by state mapped with safe storage law status","MAP","usa","choropleth","Guns & Weapons","Everytown: #NotAnAccident (everytownresearch.org)",82,68,72,68,82,64,60,82),
mk("hem30","Police Gun Seizure Yield by City","Guns seized per 1000 traffic stops and arrests by police department with weapon type breakdown","CHART","usa","bar-chart","Guns & Weapons","Police Dept Annual Reports + BJS (bjs.gov)",55,52,70,72,65,60,68,78),
mk("hem31","Silencer Legality and Registration Map","States where suppressors are legal mapped with NFA registration counts per capita","MAP","usa","choropleth","Guns & Weapons","ATF: NFA Registration (atf.gov)",45,50,74,68,52,66,62,90),
mk("hem32","Gun Violence Research Funding Gap","Federal funding for gun violence research vs. other causes of death per fatality","CHART","usa","bar-chart","Guns & Weapons","RAND + NIH Reporter (rand.org)",62,55,72,78,68,60,72,82),
mk("hem33","Militia Group Geography","Known militia and armed anti-government groups by state mapped with recent federal investigations","MAP","usa","choropleth","Guns & Weapons","SPLC: Antigovernment Groups (splcenter.org)",62,48,65,74,76,68,70,78),
mk("hem34","Gun Range Noise Complaint Map","Shooting ranges facing noise complaints or lawsuits from encroaching residential development","MAP","usa","dot-density","Guns & Weapons","NRA Range Database + Municipal Records (nra.org)",42,58,70,70,52,66,72,75),
mk("hem35","Interstate Gun Purchase Denials","NICS background check denials for interstate purchases by state pair showing regulatory gaps","MAP","usa","flow-map","Guns & Weapons","FBI: NICS Operations Report (fbi.gov/nics)",55,48,68,72,68,72,68,85),
]

raw = open(DATA, 'r', encoding='utf-8').read()
existing = set(re.findall(r'id:"(hem\d+)"', raw))
new_ideas = [i for i in IDEAS if re.search(r'id:"(hem\d+)"', i).group(1) not in existing]
print(f"Injecting {len(new_ideas)} new ideas (skipping {len(IDEAS)-len(new_ideas)} dupes)")
if new_ideas:
    tail = ']; // end D'
    assert tail in raw, "Cannot find tail marker"
    raw = raw.replace(tail, ',\n'.join(new_ideas) + ',\n' + tail)
    open(DATA, 'w', encoding='utf-8').write(raw)
    print("Done")
else:
    print("Nothing to inject")
