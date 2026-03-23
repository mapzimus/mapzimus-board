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
mk("heg01","Authoritarian Playbook Timeline","Common sequence of democratic erosion steps — media capture, judiciary packing, opposition jailing — across 20 countries","CHART","world","timeline","Politics & Governance","V-Dem: Autocratization Sequences (v-dem.net)",70,58,72,74,78,68,75,82),
mk("heg02","Money in Judicial Elections","Campaign spending in state supreme court races per capita by state with donor type breakdown","MAP","usa","choropleth","Politics & Governance","Brennan Center: Judicial Elections (brennancenter.org)",65,60,72,72,74,66,68,85),
mk("heg03","Voter Wait Time Inequality","Average voter wait time by precinct mapped against racial composition of precinct","MAP","usa","bivariate-choropleth","Politics & Governance","MIT: Election Performance Index (electionlab.mit.edu)",72,68,72,70,78,72,65,82),
mk("heg04","Democracy Satisfaction Gap","Gap between satisfaction with democracy among election winners vs. losers by country","CHART","world","bar-chart","Politics & Governance","ESS: European Social Survey (europeansocialsurvey.org)",58,62,70,74,62,58,72,82),
mk("heg05","Legislative Productivity Collapse","Number of substantive bills passed per congressional session over 50 years vs. naming resolutions","CHART","usa","area-chart","Politics & Governance","Congress.gov: Legislation Statistics (congress.gov)",60,68,74,68,65,58,62,90),
mk("heg06","Partisan Gerrymandering Simulator","How different redistricting methods would change seat counts in each state","MAP","usa","choropleth","Politics & Governance","Dave Redistricting App (davesredistricting.org)",62,60,70,72,70,74,72,80),
mk("heg07","Emergency Powers Abuse Index","Countries where emergency powers declared for COVID were used for unrelated political purposes","MAP","world","choropleth","Politics & Governance","ICNL: COVID-19 Civic Freedom Tracker (icnl.org)",68,55,68,74,78,66,72,78),
mk("heg08","Xylazine Tranq Dope Spread","Cities where xylazine has been detected in the drug supply mapped with wound care availability","MAP","usa","dot-density","Health & Wellbeing","DEA: Xylazine Report (dea.gov)",78,58,68,72,82,70,68,78),
mk("heg09","Drug Price Markup Chain","Price of common drugs at each step — manufacturer, distributor, pharmacy, patient — by drug type","CHART","usa","bar-chart","Health & Wellbeing","Kaiser: Prescription Drug Costs (kff.org)",68,75,72,74,70,58,62,82),
mk("heg10","Addiction Treatment Wait Times","Average wait time for publicly funded addiction treatment by state mapped with overdose rates","MAP","usa","bivariate-choropleth","Health & Wellbeing","SAMHSA: NSSATS (samhsa.gov)",75,70,72,62,76,68,58,82),
mk("heg11","Naloxone Access Laws","States with standing Naloxone orders, pharmacy access, and Good Samaritan protections mapped with reversal rates","MAP","usa","choropleth","Health & Wellbeing","PDAPS: Naloxone Laws (pdaps.org)",68,65,74,62,70,64,58,88),
mk("heg12","Drug Lab Seizures Global","Clandestine drug laboratory seizures by country and drug type over 10 years","MAP","world","dot-density","Conflict & Security","UNODC: Drug Lab Seizures (unodc.org)",60,48,68,70,68,74,62,78),
mk("heg13","College Binge Drinking Deaths","Alcohol-related deaths among college students per year mapped by campus with Greek life prevalence","MAP","usa","dot-density","Health & Wellbeing","NIAAA: College Drinking (niaaa.nih.gov)",78,72,65,62,74,66,55,78),
mk("heg14","Supervised Injection Site Outcomes","Overdose reversals at supervised consumption sites globally mapped with zero-death records","MAP","world","dot-density","Health & Wellbeing","EMCDDA: Drug Consumption Rooms (emcdda.europa.eu)",65,52,70,72,62,66,68,78),
mk("heg15","Fertilizer Runoff Dead Zones","Hypoxic dead zones in US waterways caused by agricultural fertilizer runoff mapped with upstream farm density","MAP","usa","bivariate-choropleth","Environment & Climate","NOAA: Gulf Hypoxia (noaa.gov/hypoxia)",68,55,72,70,72,78,66,85),
mk("heg16","Cattle Feedlot Concentration","Percentage of US beef cattle in feedlots with 32,000+ head mapped against water contamination","MAP","usa","dot-density","Agriculture & Food","USDA NASS: Cattle on Feed (nass.usda.gov)",62,55,72,74,68,72,66,88),
mk("heg17","Avocado Water Footprint","Water required to grow avocados by region mapped against local water stress and export destinations","MAP","world","flow-map","Agriculture & Food","Water Footprint Network (waterfootprint.org)",60,65,70,74,62,74,68,80),
mk("heg18","Regenerative Agriculture Adoption","Farms practicing regenerative agriculture by county mapped with soil carbon improvements","MAP","usa","dot-density","Agriculture & Food","Rodale Institute: Farming Systems Trial (rodaleinstitute.org)",55,52,70,68,52,72,68,72),
mk("heg19","Seed Patent Concentration","Percentage of global seed market controlled by top 4 companies over 30 years by crop type","CHART","world","area-chart","Agriculture & Food","ETC Group: Seed Industry (etcgroup.org)",62,55,72,78,72,58,74,80),
mk("heg20","PFAS Forever Chemicals in Farmland","Agricultural land contaminated with PFAS from biosolid application mapped by state","MAP","usa","choropleth","Environment & Climate","EPA: PFAS Data (epa.gov/pfas)",75,65,68,74,80,72,68,78),
mk("heg21","Coffee Growing Zone Migration","How climate change is shifting viable coffee-growing regions mapped with 2050 projections","MAP","world","choropleth","Agriculture & Food","CIAT: Climate-Smart Agriculture (ciat.cgiar.org)",62,68,70,72,65,76,68,80),
mk("heg22","NBA Player Birthplace Density","NBA players per 100,000 males by county of birth mapped with basketball infrastructure","MAP","usa","dot-density","Sports & Recreation","Basketball Reference (basketball-reference.com)",48,62,68,68,42,72,62,85),
mk("heg23","Womens Sports Viewership Surge","TV viewership for womens sports events vs. mens equivalents over 10 years by sport","CHART","world","line-chart","Sports & Recreation","Nielsen: Sports Viewership (nielsen.com)",62,68,72,72,55,58,60,82),
mk("heg24","College Football Revenue Map","Revenue generated by each FBS football program mapped with athletic department profit/loss","MAP","usa","proportional-symbol","Sports & Recreation","USA Today: NCAA Finances (usatoday.com/sports/ncaaf/finances)",55,68,74,65,58,70,55,88),
mk("heg25","Marathon Finish Time Distribution","Boston Marathon finish time distributions by age group and gender showing who actually runs 26.2 miles","CHART","usa","area-chart","Sports & Recreation","BAA: Results Database (baa.org)",48,65,72,62,42,60,55,90),
mk("heg26","Sports Gambling Addiction Hotlines","Calls to problem gambling helplines per capita by state since sports betting legalization","MAP","usa","choropleth","Health & Wellbeing","NCPG: Helpline Data (ncpgambling.org)",70,68,70,68,72,64,62,78),
mk("heg27","Athlete Activism Timeline","Professional athlete protests and political statements mapped on a timeline with public reaction polling","CHART","world","timeline","Sports & Recreation","ESPN + Gallup (espn.com)",60,62,65,68,62,58,68,75),
mk("heg28","Soccer Stadium Disasters","Major stadium disasters worldwide mapped with death toll and safety regulation changes triggered","MAP","world","dot-density","Sports & Recreation","FIFA: Safety Guidelines (fifa.com)",72,55,68,65,72,74,58,80),
mk("heg29","Political Dynasty Persistence","Countries where the same family has held power for 20+ years mapped with governance indicators","MAP","world","choropleth","Politics & Governance","V-Dem + Rulers of the World (v-dem.net)",62,55,70,74,68,68,72,82),
mk("heg30","State Legislature Salary vs. Diversity","State legislator annual salary mapped against demographic diversity of legislature","MAP","usa","bivariate-choropleth","Politics & Governance","NCSL: Legislator Compensation (ncsl.org)",58,62,72,74,60,64,70,88),
mk("heg31","Grain Export Chokepoints","Global grain trade routes through vulnerable chokepoints — Bosphorus, Suez, Panama, Malacca","MAP","world","flow-map","Agriculture & Food","USDA FAS: Grain Transport (fas.usda.gov)",62,52,72,70,72,80,68,82),
mk("heg32","Youth Sports Concussion Protocol Compliance","States with return-to-play concussion laws mapped with actual compliance rates in high school sports","MAP","usa","bivariate-choropleth","Sports & Recreation","CDC: Heads Up (cdc.gov/headsup)",68,72,70,62,65,64,58,80),
mk("heg33","Filibuster Usage Explosion","Senate filibusters and cloture votes per Congress over 100 years showing exponential growth","CHART","usa","area-chart","Politics & Governance","Senate.gov: Cloture Motions (senate.gov)",58,60,74,72,65,58,62,90),
mk("heg34","Dairy Farm Consolidation","Number of dairy farms vs. total milk production over 50 years showing fewer farms producing more","CHART","usa","dual-axis","Agriculture & Food","USDA NASS: Milk Production (nass.usda.gov)",58,58,74,70,62,62,58,90),
mk("heg35","Transgender Athlete Policies by Sport","International sports federation policies on transgender athlete participation mapped with policy timeline","MAP","world","choropleth","Sports & Recreation","Outsports: Policy Tracker (outsports.com)",65,60,65,68,78,60,68,75),
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
print(f"Injected {len(new)} new ideas (HEG batch)")
