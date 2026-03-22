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
mk("HCT01","Guns Per Capita vs. Gun Deaths Per Capita: The Scatter Plot Nobody Wants to See","State-level gun ownership rates plotted against gun death rates, showing the uncomfortable correlation","XREF","US","Scatter plot","guns","CDC: WISQARS Fatal Injury Data (wisqars.cdc.gov)",85,72,80,72,88,70,68,82),
mk("HCT02","The Gun Store Desert and the Gun Store Oasis: FFL Dealers Per Capita","Federal firearms license holders per capita by county, showing where guns are most commercially available","MAP","US","County choropleth","guns","ATF: Federal Firearms Licensee List (atf.gov/firearms/listing-federal-firearms-licensees)",68,65,75,75,72,82,68,85),
mk("HCT03","School Shooting Geography: Every K-12 Incident Since Columbine","Map of every school shooting incident 1999-present, with casualties and weapon type","MAP","US","Dot map","guns","Everytown: School Shootings Database (everytownresearch.org/maps/gunfire-on-school-grounds)",92,75,78,68,92,80,62,82),
mk("HCT04","Americas Gun Age: Average Age of Firearms in Circulation","Estimated age distribution of the 400+ million civilian firearms in the US — many are decades old","CHART","US","Bar chart","guns","ATF: Firearms Commerce Report (atf.gov/firearms/docs/report/firearms-commerce)",65,65,70,80,68,68,78,68),
mk("HCT05","The Concealed Carry Patchwork: Who Can Carry Where","Concealed carry permit requirements by state — constitutional carry vs. shall-issue vs. may-issue vs. no-issue","MAP","US","State choropleth","guns","USCCA: Concealed Carry Reciprocity Map (usconcealedcarry.com/resources/ccw_reciprocity_map)",68,72,80,68,72,82,62,85),
mk("HCT06","Ghost Guns: Unserialized Firearms Recovered by Police by City","Privately made firearms recovered at crime scenes by city, the fastest-growing category of crime guns","RANK","US","Bar chart","guns","ATF: National Firearms Commerce and Trafficking Assessment (atf.gov/firearms/national-firearms-commerce-and-trafficking-assessment)",78,65,72,82,80,68,78,72),
mk("HCT07","The Background Check Surge: NICS Checks Per Month 2000-2025","Monthly FBI background checks for firearm purchases, showing spikes after mass shootings and elections","CHART","US","Line chart","guns","FBI: NICS Firearm Background Checks (fbi.gov/services/cjis/nics)",72,72,80,75,72,70,68,88),
mk("HCT08","Where Guns Cross State Lines: Interstate Firearms Trafficking Flows","ATF trace data showing which states are net exporters and importers of crime guns","MAP","US","Line map","guns","ATF: Firearms Trace Data (atf.gov/resource-center/firearms-trace-data)",78,65,75,82,80,82,75,78),
mk("HCT09","The Overdose Atlas: Drug Death Rates by County and Substance","County-level overdose death rates, colored by primary substance — opioid, fentanyl, meth, cocaine","MAP","US","County choropleth","drugs","CDC: WONDER Multiple Cause of Death (wonder.cdc.gov)",88,78,78,72,85,82,68,85),
mk("HCT10","Fentanyl Seizure Map: Where Customs Intercepts the Supply","Border crossing points and mail facilities where fentanyl is seized, with volume data","MAP","US","Dot map","drugs","CBP: Drug Seizure Statistics (cbp.gov/newsroom/stats/drug-seizure-statistics)",78,65,75,78,82,82,72,78),
mk("HCT11","The Marijuana Patchwork: Legal Status by State Over Time","Animated map of marijuana legalization spreading across states, year by year from 1996 to present","MAP","US","Animated choropleth","drugs","NORML: State Marijuana Laws (norml.org/laws)",68,78,78,68,65,82,62,88),
mk("HCT12","Narcan Nation: Naloxone Administrations Per Capita by County","Rate of naloxone (Narcan) administration by emergency services per capita, a proxy for overdose crisis severity","MAP","US","County choropleth","drugs","NEMSIS: National EMS Database (nemsis.org)",82,72,75,72,82,80,70,72),
mk("HCT13","The Democracy Index Map: How Free Is Each Country Really","Economist Intelligence Unit democracy scores mapped globally — full democracy, flawed democracy, hybrid, authoritarian","MAP","World","World choropleth","democracy","EIU: Democracy Index (eiu.com/topic/democracy-index)",68,62,80,68,72,82,62,88),
mk("HCT14","Voter Suppression or Voter Integrity: Restrictive Voting Laws by State Since 2020","New voting restrictions passed since 2020 by state — ID requirements, drop box limits, polling place closures","MAP","US","State choropleth","democracy","Brennan Center: Voting Laws Roundup (brennancenter.org/our-work/research-reports/voting-laws-roundup)",80,72,75,72,82,78,68,78),
mk("HCT15","The Gerrymandering Gallery: Most Absurdly Shaped Congressional Districts","Congressional districts ranked by geometric compactness score, showing the worst gerrymandering offenders","RANK","US","Special map","democracy","FiveThirtyEight: Redistricting Tracker (projects.fivethirtyeight.com/redistricting-maps)",75,72,78,78,75,85,72,82),
mk("HCT16","Where Your Vote Counts Most: Electoral College Weight Per Voter","Effective voting power per person by state in presidential elections — Wyoming voters have 3.6x the power of Californians","MAP","US","State choropleth","democracy","Census: Apportionment Data (census.gov/topics/public-sector/voting)",72,75,80,82,75,78,72,88),
mk("HCT17","The Pharma Pipeline: Where Prescription Opioids Were Shipped 2006-2014","DEA ARCOS database showing opioid pill shipments to every pharmacy in America — the supply-side flood","MAP","US","County choropleth","drugs","DEA: ARCOS Retail Drug Summary (deadiversion.usdoj.gov/arcos)",85,72,75,78,88,82,72,82),
mk("HCT18","Americas Meth Belt: Methamphetamine Lab Seizures by County","Clandestine meth lab discoveries mapped by county, showing the shift from domestic production to cartel supply","MAP","US","County choropleth","drugs","DEA: National Clandestine Laboratory Register (dea.gov/clan-lab)",78,65,72,72,78,82,68,78),
mk("HCT19","Dark Money in Elections: Outside Spending by Undisclosed Donors","Total dark money spent in federal elections by cycle, broken down by type and transparency level","CHART","US","Area chart","democracy","OpenSecrets: Dark Money Database (opensecrets.org/dark-money)",78,68,72,78,80,68,72,80),
mk("HCT20","The Lobbying Landscape: Top Industries by Spending Per Congressperson","Lobby spending per member of relevant committee, showing which industries invest most in which legislators","RANK","US","Bar chart","democracy","OpenSecrets: Lobbying Database (opensecrets.org/federal-lobbying)",75,68,75,78,78,68,72,82),
mk("HCT21","Gun Buyback ROI: Firearms Collected vs. Gun Violence Reduction by City","Effectiveness of gun buyback programs — guns collected per dollar spent and any measurable violence reduction","XREF","US","Scatter plot","guns","National Police Foundation: Gun Buyback Studies (policefoundation.org)",72,65,70,78,72,68,78,58),
mk("HCT22","The Ballot Measure Boom: Direct Democracy Usage by State","Number of ballot measures per decade by state, showing where citizens bypass legislatures most","MAP","US","State choropleth","democracy","Ballotpedia: Ballot Measures Database (ballotpedia.org/Ballot_measures)",65,62,75,72,65,78,70,82),
mk("HCT23","How Many Guns Were Made This Year: US Firearms Manufacturing by Type","Annual domestic firearms production by type — pistols, rifles, shotguns, revolvers — 1986-2025","CHART","US","Area chart","guns","ATF: Annual Firearms Manufacturing and Export Report (atf.gov/firearms/docs/report)",65,62,78,72,68,68,65,88),
mk("HCT24","Drug Decriminalization Experiment: Oregon vs. Portugal Outcomes","Comparing drug decriminalization outcomes — overdose deaths, arrests, treatment uptake — in Oregon vs. Portugal","XREF","World","Bar chart","drugs","Oregon Health Authority: Drug Decriminalization Data (oregon.gov/oha)",75,68,72,78,72,68,78,68),
mk("HCT25","The Filibuster Effect: Bills That Passed the House But Died in the Senate","Major legislation that had majority Senate support but failed to overcome the filibuster, by topic area","CHART","US","Bar chart","democracy","GovTrack: Congressional Bills Database (govtrack.us)",72,65,75,78,75,68,72,78),
mk("HCT26","Domestic Violence and Gun Access: The Lethal Intersection","States that do and dont prohibit firearm possession for domestic violence misdemeanor convictions","MAP","US","State choropleth","guns","Giffords Law Center: Domestic Violence and Firearms (giffords.org/lawcenter)",85,72,75,72,88,78,68,78),
mk("HCT27","The Kratom-to-Fentanyl Pipeline: How Drug Trends Spread Geographically","Geographic spread patterns of drug trends over time — how new substances diffuse across the country","MAP","US","Animated choropleth","drugs","NIDA: Drug Trend Reports (nida.nih.gov/research-topics/trends-statistics)",72,62,68,80,75,78,78,62),
mk("HCT28","Voter Turnout in Non-Presidential Elections: Who Actually Shows Up","Voter turnout for midterm, state, and local elections by state — some under 20% for local races","MAP","US","State choropleth","democracy","EAVS: Election Administration and Voting Survey (eac.gov/research-and-data/datasets-codebooks-and-surveys)",72,75,78,72,70,78,68,82),
mk("HCT29","The NRA Scoreboard: Congressional Ratings vs. Gun Vote Record","NRA letter grades for every member of Congress plotted against their actual voting record on gun bills","XREF","US","Scatter plot","guns","NRA-PVF: Grades and Endorsements (nrapvf.org/grades)",72,65,75,72,78,68,68,78),
mk("HCT30","Treatment Deserts: Counties With No Substance Abuse Facility","Counties with zero licensed drug treatment facilities, overlaid with overdose death rates","MAP","US","Bivariate choropleth","drugs","SAMHSA: Treatment Locator (findtreatment.gov)",85,72,75,78,85,82,70,78),
mk("HCT31","Ranked Choice Voting Adoption: Where Alternative Voting Has Spread","Cities and states using ranked choice voting, instant runoff, or other alternative voting methods","MAP","US","Dot map","democracy","FairVote: Ranked Choice Voting Map (fairvote.org/rcv)",65,60,78,72,62,80,72,78),
mk("HCT32","The AR-15 Economy: How One Gun Platform Drives an Entire Industry","Market share, accessories market, and economic footprint of AR-15 style rifles in American gun industry","CHART","US","Bar chart","guns","NSSF: Firearms Industry Economic Impact (nssf.org)",68,62,72,78,72,68,75,68),
mk("HCT33","Cannabis Tax Revenue by State: The Green Gold Rush","Annual marijuana tax revenue by state since legalization, compared to original projections","RANK","US","Bar chart","drugs","Tax Foundation: Marijuana Tax Revenue (taxfoundation.org/marijuana-taxes-state)",68,72,80,72,62,70,68,82),
mk("HCT34","The Revolving Door: Former Congress Members Now Lobbying","Percentage of departed Congress members who became registered lobbyists by decade","CHART","US","Line chart","democracy","OpenSecrets: Revolving Door Database (opensecrets.org/revolving)",72,68,72,78,75,68,72,78),
mk("HCT35","Suicide by Firearm: The Gun Death Nobody Talks About","Firearm suicides as percentage of all gun deaths by state — typically 60%+ but rarely in the headlines","MAP","US","State choropleth","guns","CDC: WISQARS Fatal Injury Data (wisqars.cdc.gov)",88,72,78,80,85,78,72,82),
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
print(f"Injected {len(new)} new ideas (HCT batch)")
