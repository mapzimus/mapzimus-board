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
mk("heq01","Statute of Limitations Patchwork","Statute of limitations for sexual assault by state showing which states have eliminated it entirely","MAP","usa","choropleth","Law & Justice","RAINN: State Law Database (rainn.org)",72,55,72,68,74,66,62,90),
mk("heq02","Police Body Camera Footage Release Policies","States ranked by how quickly and easily body camera footage can be obtained by the public","MAP","usa","choropleth","Law & Justice","Reporters Committee: Police Camera Laws (rcfp.org)",62,55,70,68,72,64,68,85),
mk("heq03","Private Prison Occupancy Guarantees","States with guaranteed minimum occupancy clauses in private prison contracts mapped with actual occupancy","MAP","usa","choropleth","Law & Justice","In the Public Interest + State Contracts (inthepublicinterest.org)",65,52,68,78,74,66,72,80),
mk("heq04","Innocence Project Exoneration Map","Wrongful convictions overturned by state mapped with years served and contributing factors","MAP","usa","dot-density","Law & Justice","National Registry of Exonerations (law.umich.edu)",78,58,72,72,76,68,65,90),
mk("heq05","Court Interpreter Shortage","Courts with critical interpreter shortages by language mapped with LEP population served","MAP","usa","dot-density","Law & Justice","NCSC: Language Access (ncsc.org)",62,55,70,72,65,64,68,78),
mk("heq06","Debtors Prison Comeback","Jurisdictions that still jail people for inability to pay fines mapped with median fine amounts","MAP","usa","dot-density","Law & Justice","ACLU: Debtors Prisons (aclu.org)",72,62,70,76,76,64,70,80),
mk("heq07","Police Misconduct Settlement Costs","Total police misconduct lawsuit settlement payouts by city over 10 years mapped per capita","MAP","usa","choropleth","Law & Justice","FiveThirtyEight + City Budget Data (fivethirtyeight.com)",65,58,72,74,72,66,68,85),
mk("heq08","Bail Bond Industry Profit Map","Bail bond company revenue by state mapped with average bail amounts and pretrial detention rates","MAP","usa","choropleth","Law & Justice","PJI: Pretrial Justice (pretrial.org)",62,55,70,74,70,66,70,82),
mk("heq09","Death Row Exoneration Rate","Percentage of death row inmates later exonerated by state mapped with time served before exoneration","MAP","usa","choropleth","Law & Justice","DPIC: Death Penalty Info (deathpenaltyinfo.org)",78,52,72,76,78,64,68,88),
mk("heq10","Single Person Household Majority Counties","Counties where single-person households are the most common household type mapped with age distribution","MAP","usa","choropleth","Demographics","Census ACS: Household Type (census.gov)",55,68,72,72,48,68,68,92),
mk("heq11","Multigenerational Household Surge","Counties with the fastest growth in three-generation households mapped with housing costs and cultural demographics","MAP","usa","choropleth","Demographics","Census ACS: Multigenerational (census.gov)",58,68,72,72,52,68,68,90),
mk("heq12","College Town Population Whiplash","Towns where population swings 30%+ between academic year and summer mapped with economic impact","MAP","usa","dot-density","Demographics","Census: Group Quarters + IPEDS (census.gov)",48,62,72,74,42,68,72,85),
mk("heq13","Citizenship by Birth Tourism Hotspots","Hospitals with highest rates of births to non-resident mothers by metro area","MAP","usa","dot-density","Demographics","CDC: Natality Detail File (cdc.gov/nchs)",52,48,65,78,65,66,74,78),
mk("heq14","Retirement Migration Corridors","Where retirees move from and to showing dominant corridors between states","MAP","usa","flow-map","Demographics","Census: State-to-State Migration (census.gov)",55,65,72,68,45,74,62,92),
mk("heq15","Working Age Population Cliff","Counties projected to lose 20%+ of working-age population by 2035 mapped with current industry dependence","MAP","usa","choropleth","Demographics","Census Population Projections (census.gov)",65,62,72,72,68,68,65,85),
mk("heq16","Uncontacted Peoples Map","Approximate locations of remaining uncontacted indigenous groups worldwide with threat levels","MAP","world","dot-density","Demographics","Survival International (survivalinternational.org)",58,42,60,80,62,74,78,68),
mk("heq17","Same-Sex Couple Household Density","Same-sex couple households per 1000 households by county showing geographic clustering","MAP","usa","choropleth","Demographics","Census ACS: Same-Sex Couples (census.gov)",48,58,72,65,42,68,60,92),
mk("heq18","Digital Nomad Visa Countries","Countries offering digital nomad visas mapped with requirements, tax implications, and uptake numbers","MAP","world","choropleth","Demographics","Nomad List + Government Sources (nomadlist.com)",48,55,72,68,42,72,68,82),
mk("heq19","Beirut Explosion Blast Radius Damage Assessment","Building damage assessment by distance from Beirut port explosion mapped with reconstruction progress","MAP","middle-east","special","Conflict & Security","World Bank: Beirut Assessment (worldbank.org)",72,45,68,68,72,76,65,80),
mk("heq20","Houthi Red Sea Shipping Disruption","Commercial shipping rerouted around Yemen due to Houthi attacks mapped with cost per voyage increase","MAP","middle-east","flow-map","Conflict & Security","IMO + Lloyd's List Intelligence (imo.org)",62,38,68,72,76,76,68,82),
mk("heq21","MENA Desalination Plant Network","Desalination plants across the Middle East mapped with capacity, energy source, and water cost per gallon","MAP","middle-east","dot-density","Energy & Resources","GWI: DesalData (desaldata.com)",48,35,72,68,55,72,68,85),
mk("heq22","Iraqs Marsh Arab Wetland Restoration","Mesopotamian marshlands destruction under Saddam vs. restoration progress mapped with satellite imagery","MAP","middle-east","special","Environment & Climate","UNEP: Iraqi Marshlands (unep.org)",62,38,65,72,58,78,72,78),
mk("heq23","Lebanese Banking Crisis Depositor Losses","Estimated depositor losses in Lebanese banking crisis by account size bracket","CHART","middle-east","bar-chart","Economy & Trade","Banque du Liban + IMF (bdl.gov.lb)",65,42,68,72,74,58,68,78),
mk("heq24","Omani Frankincense Trade Route Heritage","Historical frankincense trade routes mapped with modern UNESCO sites and remaining production areas","MAP","middle-east","line-map","Culture & Religion","UNESCO + Omani Heritage (unesco.org)",42,35,68,68,38,76,72,78),
mk("heq25","UAE Migrant Worker Kafala System","Migrant worker populations under kafala sponsorship system by UAE emirate mapped with nationality and sector","MAP","middle-east","choropleth","Labor & Employment","HRW: UAE Labor (hrw.org)",68,40,68,72,74,66,68,75),
mk("heq26","Jordans Refugee Economy","Jordans economy adjusted for refugee population showing per capita GDP with and without refugee count","CHART","middle-east","dual-axis","Economy & Trade","UNHCR + World Bank Jordan (unhcr.org)",58,42,70,72,58,60,68,82),
mk("heq27","DACA Recipient Economic Contribution","DACA recipient employment, tax contributions, and home ownership by state","MAP","usa","choropleth","Immigration & Migration","FWD.us: DACA Data (fwd.us)",62,58,72,68,62,66,62,85),
mk("heq28","Refugee Resettlement Agency Capacity","Refugee resettlement agency office locations mapped with annual placement capacity vs. arrivals","MAP","usa","dot-density","Immigration & Migration","WRAPS: Refugee Processing (state.gov)",62,52,70,68,62,68,62,85),
mk("heq29","Language Interpreter Demand Surge","Most requested languages for court and hospital interpreters by metro area over 10 years","CHART","usa","bar-chart","Immigration & Migration","NCIHC: Interpreter Data (ncihc.org)",48,58,70,72,48,58,68,82),
mk("heq30","TPS Country Designation Timeline","Temporary Protected Status designations and terminations by country of origin over 30 years","CHART","usa","timeline","Immigration & Migration","USCIS: TPS (uscis.gov)",55,48,70,68,62,62,65,90),
mk("heq31","Border Wall Construction Progress","US-Mexico border wall sections built by administration mapped with cost per mile and terrain type","MAP","usa","line-map","Immigration & Migration","CBP + GAO Reports (cbp.gov)",58,55,72,68,68,74,58,85),
mk("heq32","Immigrant Small Business Corridor","Census tracts where immigrant-owned businesses make up 50%+ of all businesses mapped by origin country","MAP","usa","choropleth","Immigration & Migration","Census: Survey of Business Owners (census.gov)",55,62,70,74,48,68,70,85),
mk("heq33","EB-5 Investor Visa Geography","EB-5 visa approvals by country of origin and investment project location showing capital flows","MAP","usa","flow-map","Immigration & Migration","USCIS: EB-5 Data (uscis.gov)",48,42,70,72,52,72,68,88),
mk("heq34","ICE Detention Facility Conditions","ICE detention facilities mapped with DHS OIG inspection findings and average detainee stay duration","MAP","usa","dot-density","Immigration & Migration","DHS OIG + FOIA Data (oig.dhs.gov)",68,48,68,72,76,68,65,82),
mk("heq35","Naturalization Ceremony Wait Times","Average wait time from green card to citizenship ceremony by USCIS field office","MAP","usa","choropleth","Immigration & Migration","USCIS: Processing Times (uscis.gov)",55,62,72,68,58,64,60,88),
]

raw = open(DATA, 'r', encoding='utf-8').read()
existing = set(re.findall(r'id:"(heq\d+)"', raw))
new_ideas = [i for i in IDEAS if re.search(r'id:"(heq\d+)"', i).group(1) not in existing]
print(f"Injecting {len(new_ideas)} new ideas (skipping {len(IDEAS)-len(new_ideas)} dupes)")
if new_ideas:
    tail = ']; // end D'
    assert tail in raw, "Cannot find tail marker"
    raw = raw.replace(tail, ',\n'.join(new_ideas) + ',\n' + tail)
    open(DATA, 'w', encoding='utf-8').write(raw)
    print("Done")
else:
    print("Nothing to inject")
