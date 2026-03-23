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
mk("hei01","Ankle Monitor Industry Profits","Private electronic monitoring companies revenue per monitored person by state mapped with fee burden on defendants","MAP","usa","choropleth","Law & Justice","Libre by Nexus + BI Inc Reports (mediadefense.org)",68,62,68,76,74,64,72,78),
mk("hei02","Suspended License Spiral","States that suspend drivers licenses for unpaid fines mapped with job loss and re-arrest rates","MAP","usa","choropleth","Law & Justice","Free to Drive Coalition (freetodrive.org)",72,72,70,68,72,64,62,82),
mk("hei03","Police Overtime Abuse","Top-earning police officers whose overtime exceeded base salary by department with audit findings","CHART","usa","bar-chart","Law & Justice","City Payroll Data + OIG Reports (data.boston.gov)",65,68,68,78,72,58,70,80),
mk("hei04","Wrongful Conviction Compensation","States that compensate exonerees vs. those that dont, mapped with average payout per year served","MAP","usa","choropleth","Law & Justice","Innocence Project: Compensation (innocenceproject.org)",78,60,72,72,74,64,65,82),
mk("hei05","Patent Troll Lawsuit Geography","Patent infringement lawsuits filed in plaintiff-friendly districts mapped with shell company registrations","MAP","usa","dot-density","Law & Justice","Lex Machina: Patent Litigation (lexmachina.com)",55,52,68,76,68,66,72,82),
mk("hei06","Child Support Enforcement Disparities","Child support collection rates by state mapped against incarceration rates for non-payment","MAP","usa","bivariate-choropleth","Law & Justice","OCSE: Child Support Data (acf.hhs.gov/css)",70,68,70,68,72,66,62,85),
mk("hei07","Tenant Eviction Right to Counsel","Cities that guarantee lawyers for tenants facing eviction mapped with eviction outcome changes","MAP","usa","dot-density","Law & Justice","NCCRC: Right to Counsel (civilrighttocounsel.org)",68,70,70,68,65,66,64,78),
mk("hei08","Lowest Median Age Countries","Countries with median age under 20 mapped with youth bulge conflict correlation","MAP","world","choropleth","Demographics","UN: World Population Prospects (population.un.org)",58,52,72,72,68,72,65,92),
mk("hei09","Town That Doubled Overnight","Small towns that experienced sudden population surges from single events — military base, factory, refugee resettlement","MAP","usa","dot-density","Demographics","Census: Decennial + ACS (census.gov)",55,62,65,80,52,72,78,82),
mk("hei10","Americas Most Ethnically Homogeneous Counties","Counties where 95%+ of residents share one racial category mapped against political lean","MAP","usa","choropleth","Demographics","Census ACS: Race Data (census.gov)",52,58,70,74,58,70,68,92),
mk("hei11","Death Rate Exceeds Birth Rate Counties","Counties where deaths exceeded births every year for the past decade mapped with median age","MAP","usa","bivariate-choropleth","Demographics","CDC: Natality + Mortality (wonder.cdc.gov)",65,60,74,72,68,74,62,92),
mk("hei12","Gender Ratio Extreme Counties","Counties with the most skewed male-to-female ratios mapped with driving factors — prisons, military, universities","MAP","usa","choropleth","Demographics","Census ACS: Sex Ratio (census.gov)",50,58,72,78,48,70,72,92),
mk("hei13","Household Formation Collapse","Rate of new household formation among 25-34 year olds by metro area over 20 years vs. housing cost","CHART","usa","dual-axis","Demographics","Census CPS: Housing Vacancies (census.gov/housing)",65,75,72,68,68,60,58,88),
mk("hei14","Immigrant Demographic Rescue","Counties where immigration prevented population decline by replacing natural population loss","MAP","usa","choropleth","Demographics","Census: Components of Population Change (census.gov)",58,60,72,76,55,70,70,90),
mk("hei15","Gaza Tunnel Network Density","Estimated tunnel locations and density beneath Gaza mapped with above-ground infrastructure","MAP","middle-east","special","Conflict & Security","IDF + UNRWA Reports (idf.il)",68,42,60,68,85,78,72,65),
mk("hei16","Middle East Renewable Energy Paradox","Solar and wind capacity installed by oil-producing MENA countries vs. continued fossil fuel investment","CHART","middle-east","grouped-bar","Energy & Resources","IRENA: Renewable Capacity (irena.org)",55,48,72,76,62,62,72,82),
mk("hei17","Kurdish Population Without a State","Estimated Kurdish population distribution across Turkey, Iraq, Syria, and Iran mapped with autonomy status","MAP","middle-east","choropleth","Politics & Governance","KRG + Academic Sources (kurdipedia.org)",72,50,68,65,75,74,68,75),
mk("hei18","Suez Canal Chokepoint Economics","Revenue lost and supply chain delays from each major Suez Canal disruption event mapped with trade volume","CHART","middle-east","bar-chart","Economy & Trade","Suez Canal Authority (suezcanal.gov.eg)",58,55,74,70,68,68,62,85),
mk("hei19","Irans Internet Shutdowns","Complete internet shutdowns in Iran mapped with protest events and duration","CHART","middle-east","timeline","Politics & Governance","NetBlocks: Iran (netblocks.org)",70,52,68,68,80,62,68,80),
mk("hei20","Archaeological Sites Destroyed by ISIS","Cultural heritage sites deliberately destroyed by ISIS across Iraq and Syria mapped with reconstruction status","MAP","middle-east","dot-density","Culture & Religion","UNESCO: Heritage in Danger (unesco.org)",78,48,65,62,78,78,70,78),
mk("hei21","Saudi NEOM Progress vs. Promise","NEOM megaproject announced features vs. actual construction progress as of current date","CHART","middle-east","bar-chart","Economy & Trade","NEOM: Official Data + Satellite Analysis (neom.com)",52,50,70,78,65,68,74,72),
mk("hei22","Ghost Gun Seizure Surge","Unserialized ghost guns recovered by police by city over five years mapped with 3D printer ownership rates","MAP","usa","dot-density","Guns & Weapons","ATF: Privately Made Firearms (atf.gov)",62,58,72,78,72,68,74,80),
mk("hei23","School Shooting Proximity Effect","How far from a school shooting event does enrollment drop and home values decline","MAP","usa","buffer-rings","Guns & Weapons","Everytown: School Shootings (everytownresearch.org)",80,72,68,70,82,72,68,78),
mk("hei24","Guns Per Capita vs. Gun Deaths Scatterplot","State-level gun ownership rates plotted against gun death rates with political party overlay","CHART","usa","scatter","Guns & Weapons","CDC WONDER + RAND (rand.org/gun-policy)",62,68,74,55,68,68,52,92),
mk("hei25","Firearms Dealer Density","FFL-licensed firearms dealers per 10k population by county mapped with rural vs. urban classification","MAP","usa","choropleth","Guns & Weapons","ATF: FFL List (atf.gov/firearms)",52,58,72,68,55,72,62,92),
mk("hei26","Stand Your Ground Shooting Outcomes","Justified homicide rulings in Stand Your Ground states by race of shooter and victim","CHART","usa","grouped-bar","Guns & Weapons","FBI SHR + State Prosecutors (fbi.gov/ucr)",70,62,68,72,78,58,70,82),
mk("hei27","Stolen Gun Pipeline","Guns reported stolen in one state and recovered at crime scenes in another mapped with trafficking corridors","MAP","usa","flow-map","Guns & Weapons","ATF: Firearms Trace Data (atf.gov)",68,55,68,76,74,76,72,78),
mk("hei28","Ammunition Purchase Spikes","Ammunition background checks and sales volume spikes mapped against election dates and mass shooting events","CHART","usa","timeline","Guns & Weapons","NICS + Ammo Industry Reports (fbi.gov/nics)",58,62,70,74,70,64,68,82),
mk("hei29","Concealed Carry Permit Gender Gap","Concealed carry permit holders by gender over time by state mapped with women gun ownership trends","CHART","usa","line","Guns & Weapons","State CCW Records + Pew Research (pewresearch.org)",55,62,72,72,52,60,68,80),
mk("hei30","Red Flag Law Petition Outcomes","Extreme risk protection order petitions filed vs. granted by state mapped with firearm seizure counts","MAP","usa","choropleth","Guns & Weapons","State Courts + Everytown ERPO Data (everytownresearch.org)",62,58,70,68,72,62,68,82),
mk("hei31","Gun Show Loophole Map","States with no background check requirement for private sales at gun shows mapped with crime gun trace origins","MAP","usa","choropleth","Guns & Weapons","Giffords Law Center (giffords.org)",60,62,72,62,70,64,58,88),
mk("hei32","Mass Shooting Media Attention Gap","Mass shooting events by victim count vs. days of national media coverage mapped by demographics of victims","CHART","usa","scatter","Guns & Weapons","GVA + Media Cloud (mediacloud.org)",72,65,64,76,78,60,74,75),
mk("hei33","AR-15 Style Rifle State Legality Patchwork","States where AR-15 style rifles are legal vs. banned vs. restricted mapped with sales volume estimates","MAP","usa","choropleth","Guns & Weapons","Giffords + NSSF Industry Data (giffords.org)",55,60,74,58,65,68,55,88),
mk("hei34","Buyback Program Effectiveness","Gun buyback events by city mapped with weapons collected and subsequent gun violence rate changes","MAP","usa","dot-density","Guns & Weapons","Police Dept Reports + NBER Studies (nber.org)",58,60,72,68,62,66,65,82),
mk("hei35","Domestic Violence Gun Seizure Laws","States requiring firearm surrender after DV restraining orders mapped with compliance rates and homicide changes","MAP","usa","choropleth","Guns & Weapons","NCJFCJ + State DV Data (ncjfcj.org)",72,68,70,68,76,64,65,82),
]

raw = open(DATA, 'r', encoding='utf-8').read()
existing = set(re.findall(r'id:"(hei\d+)"', raw))
new_ideas = [i for i in IDEAS if re.search(r'id:"(hei\d+)"', i).group(1) not in existing]
print(f"Injecting {len(new_ideas)} new ideas (skipping {len(IDEAS)-len(new_ideas)} dupes)")
if new_ideas:
    tail = ']; // end D'
    assert tail in raw, "Cannot find tail marker"
    raw = raw.replace(tail, ',\n'.join(new_ideas) + ',\n' + tail)
    open(DATA, 'w', encoding='utf-8').write(raw)
    print("Done")
else:
    print("Nothing to inject")
