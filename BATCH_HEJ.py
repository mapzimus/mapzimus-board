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
mk("hej01","Dollar General Density vs. Grocery Deserts","Dollar General store locations mapped against USDA food desert classifications by county","MAP","usa","bivariate-choropleth","Rural America","USDA Food Access Atlas + Dollar General Locations (ers.usda.gov)",62,72,74,72,65,72,68,90),
mk("hej02","Last Remaining Town Doctor","Rural counties with only one practicing physician mapped with nearest hospital distance","MAP","usa","dot-density","Rural America","HRSA: Area Health Resource File (data.hrsa.gov)",78,72,72,74,72,70,68,85),
mk("hej03","Rural Broadband Funding vs. Actual Coverage","Federal broadband subsidies received per county vs. actual measured download speeds","MAP","usa","bivariate-choropleth","Rural America","FCC Broadband Map + USDA ReConnect (broadbandmap.fcc.gov)",62,68,70,72,68,68,68,88),
mk("hej04","Volunteer Fire Department Coverage Gaps","Areas where the nearest fire response is volunteer-only mapped with average response times","MAP","usa","choropleth","Rural America","NFPA: Fire Department Survey (nfpa.org)",70,68,70,68,70,72,65,82),
mk("hej05","Small Town Brain Drain Return Rate","Percentage of rural high school graduates who leave vs. eventually return by county","MAP","usa","choropleth","Rural America","Census: Migration Flows (census.gov)",72,78,70,68,65,66,68,78),
mk("hej06","Rural Hospital Closure Cascade Effect","Towns where rural hospital closure triggered pharmacy and clinic closures within 3 years","MAP","usa","dot-density","Rural America","Chartis Center for Rural Health (chartis.com)",78,72,72,72,74,68,68,85),
mk("hej07","One-Employer Towns","Communities where a single employer accounts for 40%+ of local jobs mapped with that employers industry","MAP","usa","dot-density","Rural America","Census: County Business Patterns (census.gov)",65,72,70,74,68,70,72,82),
mk("hej08","Rural Mailbox Distances","Average distance to nearest post office or mailbox by ZIP code mapped with USPS delivery frequency","MAP","usa","choropleth","Rural America","USPS: Facility Database (usps.com)",52,65,72,70,48,68,70,78),
mk("hej09","Farm Bankruptcy Belt","Farm bankruptcy filings per 1000 farms by federal judicial district over 10 years","MAP","usa","choropleth","Rural America","USDA ERS + US Courts Bankruptcy Data (uscourts.gov)",68,65,72,68,70,68,62,88),
mk("hej10","Therapist Desert Map","Counties with zero licensed therapists per 10k residents mapped against suicide rates","MAP","usa","bivariate-choropleth","Psychology & Behavior","SAMHSA: National Mental Health Services Survey (samhsa.gov)",78,68,72,68,76,70,62,88),
mk("hej11","Seasonal Affective Disorder Latitude Line","Depression diagnosis rates by latitude band mapped with winter daylight hours","MAP","usa","choropleth","Psychology & Behavior","CDC BRFSS + NOAA Solar Data (cdc.gov/brfss)",65,72,72,68,55,68,70,85),
mk("hej12","Screen Time and Sleep by Age","Average daily screen time vs. reported sleep duration by age group across countries","CHART","world","scatter","Psychology & Behavior","OECD Time Use + WHO Sleep Health (oecd.org)",62,78,70,62,58,62,58,80),
mk("hej13","Loneliness Epidemic by Metro Size","Self-reported loneliness rates by city population size and density","CHART","usa","bar-chart","Psychology & Behavior","Cigna Loneliness Index + Census (cigna.com)",72,82,70,68,65,58,65,80),
mk("hej14","Nostalgia Economy Map","Revenue from retro and nostalgia-marketed products by category over 10 years","CHART","usa","area-chart","Psychology & Behavior","NPD Group + Industry Reports (npd.com)",55,72,68,68,42,60,72,72),
mk("hej15","Conspiracy Theory Belief Geography","Prevalence of specific conspiracy theory beliefs by state from survey data","MAP","usa","choropleth","Psychology & Behavior","PRRI + Pew: Conspiracy Surveys (prri.org)",60,62,65,72,65,68,72,78),
mk("hej16","Decision Fatigue in Parole Hearings","Parole board approval rates by time of day showing decision fatigue pattern","CHART","usa","line","Psychology & Behavior","Danziger et al. Replication + State Parole Data (pnas.org)",68,60,68,80,68,58,78,75),
mk("hej17","Color Psychology in Fast Food Branding","Color palette analysis of top 100 fast food chains worldwide mapped with brand recognition rates","CHART","world","bar-chart","Psychology & Behavior","Interbrand + Brand Color Analysis (interbrand.com)",48,68,68,68,38,72,72,65),
mk("hej18","Anxiety Search Trends vs. Actual Diagnoses","Google Trends anxiety-related searches per state vs. clinical anxiety diagnosis rates","MAP","usa","bivariate-choropleth","Psychology & Behavior","Google Trends + CDC BRFSS (trends.google.com)",58,72,68,70,55,66,68,82),
mk("hej19","Kids Who Walk to School Extinction Map","Percentage of K-8 students who walk or bike to school by decade from 1969 to now","CHART","usa","area-chart","Children & Youth","NHTS: School Travel (nhts.ornl.gov)",65,78,72,68,58,64,62,85),
mk("hej20","Foster Care Aging Out Outcomes","Outcomes at age 25 for youth who aged out of foster care at 18 vs. general population by state","CHART","usa","grouped-bar","Children & Youth","NYTD: Foster Youth Outcomes (acf.hhs.gov)",78,65,70,68,76,58,62,85),
mk("hej21","Playground Equipment Injury Hotspots","Emergency room visits from playground injuries by equipment type and child age group","CHART","usa","bar-chart","Children & Youth","CPSC: NEISS Database (cpsc.gov)",58,72,74,65,55,62,60,90),
mk("hej22","Child Poverty Rate by Congressional District","Child poverty rates mapped at congressional district level with representatives party and voting record on child welfare","MAP","usa","choropleth","Children & Youth","Census SAIPE + GovTrack (census.gov/saipe)",72,68,72,68,72,68,62,92),
mk("hej23","Kids Without Internet for Homework","School-age children without home internet access by county mapped against school district digital assignment rates","MAP","usa","bivariate-choropleth","Children & Youth","Census ACS + NCES (nces.ed.gov)",68,74,72,68,68,68,60,90),
mk("hej24","Youth Sports Participation Collapse","Organized youth sports participation rates by sport from 2000 to present showing which sports are dying","CHART","usa","line","Children & Youth","Aspen Institute: Project Play (aspenprojectplay.org)",60,72,72,70,58,60,62,82),
mk("hej25","Childhood Lead Exposure Hotspots Still Active","Census tracts where children still test above CDC blood lead reference value mapped with housing age","MAP","usa","choropleth","Children & Youth","CDC: Lead Surveillance (cdc.gov/nceh/lead)",75,68,72,72,76,70,60,88),
mk("hej26","School Bus Ride Length Extremes","Longest average school bus commute times by rural school district","MAP","usa","choropleth","Children & Youth","NCES: School District Data (nces.ed.gov)",55,68,72,72,50,68,68,82),
mk("hej27","Starlink Ground Station Map","SpaceX Starlink ground station locations worldwide mapped with coverage gaps and latency zones","MAP","world","dot-density","Space & Exploration","FCC Filings + Starlink Coverage (fcc.gov)",55,48,70,72,48,74,68,78),
mk("hej28","Space Debris Collision Probability Zones","Orbital debris density by altitude band with predicted collision probability over next decade","CHART","world","special","Space & Exploration","ESA: Space Debris Office (esa.int)",62,42,65,74,68,78,72,75),
mk("hej29","Rocket Launch Site Geography","All active orbital launch sites worldwide mapped with launch frequency and success rates","MAP","world","dot-density","Space & Exploration","Space Launch Report (spacelaunchreport.com)",52,42,72,62,45,76,62,88),
mk("hej30","Astronaut Home State Map","Where all NASA astronauts came from mapped by hometown with selection decade","MAP","usa","dot-density","Space & Exploration","NASA: Astronaut Biographies (nasa.gov)",52,58,72,68,40,68,68,90),
mk("hej31","Light Pollution Bortle Scale Map","Light pollution intensity across the US showing where true dark skies remain","MAP","usa","choropleth","Space & Exploration","Dark Sky Atlas + VIIRS Satellite (darksitefinder.com)",58,62,72,65,45,82,62,90),
mk("hej32","Space Economy Revenue Breakdown","Global space economy revenue by sector from satellite services to launch to tourism over 10 years","CHART","world","area-chart","Space & Exploration","Space Foundation: Space Report (spacefoundation.org)",48,42,72,68,42,62,65,82),
mk("hej33","Meteorite Strike Probability Map","Recorded meteorite fall locations worldwide weighted by mass with probability density","MAP","world","dot-density","Space & Exploration","Meteoritical Bulletin Database (lpi.usra.edu)",55,48,68,74,58,76,72,88),
mk("hej34","Countries With Space Agencies","Countries that operate their own space agency mapped with annual budget and capabilities tier","MAP","world","choropleth","Space & Exploration","OECD Space Forum + Agency Reports (oecd.org)",48,40,72,62,42,72,58,88),
mk("hej35","ISS Visibility Windows","How often the International Space Station is visible from each major city per year","MAP","world","choropleth","Space & Exploration","NASA: Spot the Station (spotthestation.nasa.gov)",48,55,70,62,38,72,65,82),
]

raw = open(DATA, 'r', encoding='utf-8').read()
existing = set(re.findall(r'id:"(hej\d+)"', raw))
new_ideas = [i for i in IDEAS if re.search(r'id:"(hej\d+)"', i).group(1) not in existing]
print(f"Injecting {len(new_ideas)} new ideas (skipping {len(IDEAS)-len(new_ideas)} dupes)")
if new_ideas:
    tail = ']; // end D'
    assert tail in raw, "Cannot find tail marker"
    raw = raw.replace(tail, ',\n'.join(new_ideas) + ',\n' + tail)
    open(DATA, 'w', encoding='utf-8').write(raw)
    print("Done")
else:
    print("Nothing to inject")
