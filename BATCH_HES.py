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
mk("hes01","Mail Ballot Rejection Rate Disparities","Mail-in ballot rejection rates by county mapped with rejection reason and voter demographics","MAP","usa","choropleth","Democracy & Voting","MIT Election Data + State SOS (electionlab.mit.edu)",65,62,70,72,72,66,68,85),
mk("hes02","State Legislature Full-Time vs. Part-Time Pay","State legislator annual salary and session length mapped showing who can afford to serve","MAP","usa","choropleth","Democracy & Voting","NCSL: Legislator Compensation (ncsl.org)",55,62,72,74,58,66,68,90),
mk("hes03","Voter Suppression Lawsuit Map","Voting rights lawsuits filed by state over 10 years mapped with outcomes and demographic impact","MAP","usa","dot-density","Democracy & Voting","Brennan Center: Voting Rights Litigation (brennancenter.org)",65,52,68,70,74,66,68,85),
mk("hes04","County Clerk Election Denial Movement","Local election officials who publicly expressed doubt about election integrity mapped with subsequent policy changes","MAP","usa","dot-density","Democracy & Voting","States United Democracy Center (statesuniteddemocracy.org)",62,52,65,74,76,66,72,78),
mk("hes05","Civic Education Requirement Gaps","States with vs. without mandatory civics courses for high school graduation mapped with civic participation rates","MAP","usa","choropleth","Democracy & Voting","iCivics + CIRCLE (icivics.org)",55,58,72,68,55,66,62,88),
mk("hes06","Gubernatorial Veto Override Difficulty","How hard it is to override a gubernatorial veto by state mapped with override frequency","MAP","usa","choropleth","Democracy & Voting","NCSL: Veto Procedures (ncsl.org)",42,45,72,72,48,66,68,88),
mk("hes07","Primary Election System Chaos","States mapped by primary election type showing the patchwork of open, closed, semi-closed, jungle, and top-two systems","MAP","usa","choropleth","Democracy & Voting","FairVote: Primary Systems (fairvote.org)",48,55,72,68,48,68,65,90),
mk("hes08","PAC Money Laundering Pathways","How dark money flows through multiple PACs before reaching candidates showing obfuscation chains","CHART","usa","special","Democracy & Voting","OpenSecrets: Outside Spending (opensecrets.org)",58,48,62,78,72,68,74,78),
mk("hes09","Uncontested Election Rate","Percentage of state legislative races with only one candidate by state showing democratic deficit","MAP","usa","choropleth","Democracy & Voting","Ballotpedia: State Legislature (ballotpedia.org)",55,55,72,74,60,66,70,88),
mk("hes10","Drug Decriminalization Outcomes","States and countries that decriminalized drug possession mapped with usage rates and overdose deaths before and after","MAP","world","choropleth","Drugs & Substance Use","Transform Drug Policy + EMCDDA (transformdrugs.org)",58,48,68,72,62,68,68,82),
mk("hes11","Needle Exchange Program Coverage","Syringe services program locations mapped with HIV and Hepatitis C rates in surrounding areas","MAP","usa","bivariate-choropleth","Drugs & Substance Use","NASEN: SSP Directory (nasen.org)",62,48,70,68,65,68,62,85),
mk("hes12","Energy Drink ER Visit Surge","Emergency room visits attributed to energy drink consumption by age group and state over 10 years","CHART","usa","line","Drugs & Substance Use","SAMHSA: DAWN + FDA (samhsa.gov)",55,68,70,72,62,58,65,82),
mk("hes13","Cannabis DUI Legal Threshold Chaos","States with legal cannabis mapped with THC DUI threshold differences and enforcement challenges","MAP","usa","choropleth","Drugs & Substance Use","GHSA: Drug-Impaired Driving (ghsa.org)",52,58,68,72,62,66,68,82),
mk("hes14","Adderall Shortage Geography","Adderall and stimulant prescription fill rates vs. shortage reports by state","MAP","usa","bivariate-choropleth","Drugs & Substance Use","DEA: ARCOS + FDA Shortage List (fda.gov)",60,72,70,68,62,64,62,82),
mk("hes15","Heroin to Fentanyl Transition Timeline","When each major city's heroin supply switched to predominantly fentanyl mapped chronologically","MAP","usa","dot-density","Drugs & Substance Use","CDC: SUDORS + DEA Lab Data (cdc.gov)",68,48,68,72,78,68,68,82),
mk("hes16","Alcohol-Related Liver Disease Age Shift","Average age of alcohol-related liver disease diagnosis dropping over 20 years by state","CHART","usa","line","Drugs & Substance Use","NIAAA + HCUP (niaaa.nih.gov)",65,58,72,74,68,58,68,85),
mk("hes17","Drug Cartel Territory Control Map","Estimated territorial control of major drug cartels in Mexico and Central America","MAP","world","choropleth","Drugs & Substance Use","DEA: National Drug Threat Assessment (dea.gov)",58,35,62,74,78,74,72,72),
mk("hes18","Child Social Media Restriction Laws","States with child social media age restrictions mapped with enforcement mechanisms and compliance","MAP","usa","choropleth","Children & Youth","NCSL: Social Media + Minors (ncsl.org)",62,72,72,68,62,66,65,85),
mk("hes19","School Counselor Ratio Crisis","Student-to-school-counselor ratios by state vs. recommended maximum showing coverage gaps","MAP","usa","choropleth","Children & Youth","ASCA: School Counselor Ratios (schoolcounselor.org)",68,68,72,68,68,64,58,90),
mk("hes20","Child Influencer Labor Laws","States with laws regulating child social media influencer earnings and work hours","MAP","usa","choropleth","Children & Youth","SAG-AFTRA + State Labor Depts (sagaftra.org)",55,58,70,76,58,62,72,78),
mk("hes21","Kindergarten Readiness Inequality","Kindergarten readiness assessment scores by school district mapped with income levels","MAP","usa","bivariate-choropleth","Children & Youth","State DOE: Kindergarten Readiness (ed.gov)",65,68,70,68,65,66,58,85),
mk("hes22","Missing Children Recovery Rate","Missing children cases and recovery rates by state mapped with average time to recovery","MAP","usa","choropleth","Children & Youth","NCMEC: Missing Children Stats (missingkids.org)",78,62,72,68,78,64,62,85),
mk("hes23","Child Food Insecurity During Summer","Children losing access to school meals during summer by county mapped with summer meal program coverage","MAP","usa","bivariate-choropleth","Children & Youth","Feeding America: Map the Meal Gap (feedingamerica.org)",72,68,72,68,72,68,60,88),
mk("hes24","Youth Incarceration Rate Decline","Juvenile incarceration rates by state over 20 years showing which states reduced fastest","CHART","usa","line","Children & Youth","OJJDP: Easy Access (ojjdp.gov)",62,52,72,68,65,60,62,88),
mk("hes25","Unsafe School Building Map","Public school buildings with documented structural, lead, or asbestos hazards by district","MAP","usa","dot-density","Children & Youth","GAO: School Facilities (gao.gov)",72,68,70,72,74,68,62,80),
mk("hes26","Child Pedestrian Death Hotspots","Child pedestrian fatalities mapped by location type showing school zones, residential streets, and arterials","MAP","usa","dot-density","Children & Youth","NHTSA: FARS (nhtsa.gov)",78,68,72,68,76,70,60,90),
mk("hes27","Space Weapon Test Debris Fields","Orbital debris clouds from anti-satellite weapon tests mapped with collision risk to active satellites","MAP","world","special","Space & Exploration","18th Space Defense Squadron + ESA (space-track.org)",55,35,65,76,68,76,72,78),
mk("hes28","NASA Budget as Share of Federal Spending","NASA budget as percentage of total federal spending from Apollo to present","CHART","usa","area-chart","Space & Exploration","OMB: Historical Tables (whitehouse.gov/omb)",48,48,74,70,52,62,62,92),
mk("hes29","Planetary Protection Zones","Regions on Mars and other bodies designated off-limits to prevent contamination mapped with mission landing zones","MAP","world","special","Space & Exploration","NASA: Planetary Protection (nasa.gov)",40,32,65,78,42,74,80,72),
mk("hes30","Space Station Commercialization Race","Planned commercial space station projects mapped with funding, timeline, and capability comparison to ISS","CHART","world","bar-chart","Space & Exploration","NASA: CLD Program + Company Filings (nasa.gov)",42,35,70,72,48,68,70,78),
mk("hes31","Kessler Syndrome Probability Model","Projected debris cascade scenarios by orbital altitude showing probability of Kessler syndrome onset","CHART","world","line","Space & Exploration","NASA ODPO: Orbital Debris Quarterly (orbitaldebris.jsc.nasa.gov)",52,32,62,78,65,68,78,72),
mk("hes32","Solar Storm Satellite Vulnerability","Satellites most vulnerable to solar storm damage mapped by orbit with estimated replacement cost","CHART","world","scatter","Space & Exploration","NOAA SWPC + UCS (swpc.noaa.gov)",52,38,65,74,62,70,72,78),
mk("hes33","Space Force Base Locations","US Space Force installation locations mapped with mission type and personnel count","MAP","usa","dot-density","Space & Exploration","USSF: Installations (spaceforce.mil)",42,38,72,68,48,70,62,85),
mk("hes34","Cislunar Economy Projection","Projected cislunar economy value by sector from mining to tourism to infrastructure through 2040","CHART","world","area-chart","Space & Exploration","NSR + Morgan Stanley Space (nsr.com)",40,32,62,74,42,62,74,72),
mk("hes35","Telescope Location Dark Sky Preservation","Major telescope locations worldwide mapped with surrounding light pollution growth threatening observations","MAP","world","dot-density","Space & Exploration","IAU Dark Skies + VIIRS (iau.org)",48,35,68,70,52,76,68,85),
]

raw = open(DATA, 'r', encoding='utf-8').read()
existing = set(re.findall(r'id:"(hes\d+)"', raw))
new_ideas = [i for i in IDEAS if re.search(r'id:"(hes\d+)"', i).group(1) not in existing]
print(f"Injecting {len(new_ideas)} new ideas (skipping {len(IDEAS)-len(new_ideas)} dupes)")
if new_ideas:
    tail = ']; // end D'
    assert tail in raw, "Cannot find tail marker"
    raw = raw.replace(tail, ',\n'.join(new_ideas) + ',\n' + tail)
    open(DATA, 'w', encoding='utf-8').write(raw)
    print("Done")
else:
    print("Nothing to inject")
