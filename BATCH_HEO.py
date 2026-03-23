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
mk("heo01","Dark Money by Congressional District","Untraceable political spending per congressional district mapped with winning candidates margin","MAP","usa","choropleth","Democracy & Voting","OpenSecrets: Dark Money (opensecrets.org)",62,55,68,74,72,68,70,85),
mk("heo02","Voter Registration Purge Rates","Voter roll purge rates by state mapped with purge method and demographics of purged voters","MAP","usa","choropleth","Democracy & Voting","Brennan Center: Voter Purge Rates (brennancenter.org)",68,58,70,72,76,68,68,85),
mk("heo03","Local Election Turnout Collapse","Turnout rates for municipal elections vs. presidential elections by city showing the gap","CHART","usa","scatter","Democracy & Voting","ICMA + Municipal Clerk Data (icma.org)",55,65,72,72,58,62,68,82),
mk("heo04","Lobbyist to Legislator Ratio","Number of registered lobbyists per state legislator by state mapped with lobby spending","MAP","usa","choropleth","Democracy & Voting","OpenSecrets + NCSL (opensecrets.org)",55,55,72,76,62,64,72,88),
mk("heo05","Election Conspiracy Lawsuit Outcomes","Post-2020 election challenge lawsuits mapped by state with outcomes and filing attorney","MAP","usa","dot-density","Democracy & Voting","Democracy Docket (democracydocket.com)",60,55,70,72,72,66,68,88),
mk("heo06","Automatic Voter Registration Impact","States with automatic voter registration mapped with registration rate changes after implementation","MAP","usa","choropleth","Democracy & Voting","Brennan Center: AVR (brennancenter.org)",52,55,72,68,48,66,62,88),
mk("heo07","Congressional Age vs. Constituent Age","Average age of congressional delegation vs. median age of constituents by state","CHART","usa","scatter","Democracy & Voting","Congressional Bio Guide + Census (bioguide.congress.gov)",55,68,74,74,58,62,68,90),
mk("heo08","Recall Election Frequency","Recall elections filed against local and state officials by state over 20 years","MAP","usa","choropleth","Democracy & Voting","Ballotpedia: Recall Elections (ballotpedia.org)",52,55,70,72,60,66,68,85),
mk("heo09","Foreign Election Interference Attempts","Documented foreign interference attempts in democratic elections worldwide by method and origin country","MAP","world","flow-map","Democracy & Voting","Stanford Internet Observatory (cyber.fsi.stanford.edu)",62,45,62,76,74,72,72,75),
mk("heo10","Fentanyl Analog Emergence Timeline","New fentanyl analogs detected in the US drug supply by year mapped with first detection location","MAP","usa","dot-density","Drugs & Substance Use","DEA: National Forensic Lab (dea.gov)",68,48,68,78,80,68,72,80),
mk("heo11","Alcohol Outlet Density vs. Violence","Bars and liquor stores per capita by census tract mapped with violent crime rates","MAP","usa","bivariate-choropleth","Drugs & Substance Use","ABC License Data + FBI UCR (fbi.gov)",60,58,70,68,68,70,62,88),
mk("heo12","Drug Court Graduation vs. Recidivism","Drug court program graduation rates by jurisdiction mapped with re-arrest rates for graduates vs. non-participants","MAP","usa","choropleth","Drugs & Substance Use","NADCP: Drug Court Data (nadcp.org)",58,55,70,68,60,64,65,82),
mk("heo13","Vape Shop Proximity to Schools","Vape and e-cigarette retail locations within 1000 feet of schools by city","MAP","usa","dot-density","Drugs & Substance Use","Stanford REACH Lab + NCES (reach.stanford.edu)",65,65,70,68,70,68,62,82),
mk("heo14","Prescription Drug Take-Back Yield","Weight of prescription drugs collected at DEA take-back events by state over 10 years","MAP","usa","choropleth","Drugs & Substance Use","DEA: Take Back Day Results (dea.gov)",48,62,72,68,48,64,62,88),
mk("heo15","Synthetic Drug Lab Busts","Clandestine synthetic drug laboratory seizures by type and state over 10 years","MAP","usa","dot-density","Drugs & Substance Use","DEA: EPIC (dea.gov)",55,42,68,72,68,68,68,82),
mk("heo16","Naloxone Access Law Map","States with naloxone standing order vs. prescription required mapped with pharmacy distribution rates","MAP","usa","choropleth","Drugs & Substance Use","PDAPS: Naloxone Laws (pdaps.org)",62,58,72,62,68,66,60,88),
mk("heo17","College Binge Drinking Geography","Binge drinking rates at colleges by region mapped with Greek life participation and alcohol-related ER visits","MAP","usa","choropleth","Drugs & Substance Use","NIAAA + ACHA-NCHA Survey (niaaa.nih.gov)",55,72,70,62,58,64,58,85),
mk("heo18","Agricultural Runoff Dead Zones","Hypoxic dead zones in coastal waters mapped with upstream fertilizer application rates by watershed","MAP","usa","bivariate-choropleth","Agriculture & Food Systems","NOAA: Hypoxia + USGS Water Quality (noaa.gov)",68,52,70,72,72,74,65,85),
mk("heo19","Organic Farm Premium Gap","Price premium for organic vs. conventional crops by state mapped with organic certification costs","CHART","usa","bar-chart","Agriculture & Food Systems","USDA ERS: Organic Prices (ers.usda.gov)",48,58,72,68,48,60,62,88),
mk("heo20","Pollinator Highway Corridors","Monarch butterfly and native bee migration corridors mapped with habitat fragmentation along the route","MAP","usa","line-map","Agriculture & Food Systems","Xerces Society + USGS (xerces.org)",62,52,68,68,62,78,72,82),
mk("heo21","Average Farm Age Crisis","Average age of principal farm operators by county showing aging farmer population with no successor identified","MAP","usa","choropleth","Agriculture & Food Systems","USDA: Census of Agriculture (nass.usda.gov)",65,62,72,72,68,68,65,92),
mk("heo22","Crop Insurance Payout Hotspots","Counties receiving the most federal crop insurance payouts per acre over 10 years mapped with claim frequency","MAP","usa","choropleth","Agriculture & Food Systems","USDA RMA: Summary of Business (rma.usda.gov)",55,52,72,68,62,68,62,92),
mk("heo23","CAFO Concentration Map","Concentrated animal feeding operations per county mapped with water contamination complaints within 5 miles","MAP","usa","bivariate-choropleth","Agriculture & Food Systems","EPA: CAFO Permits + ECHO (echo.epa.gov)",68,55,70,72,72,72,65,88),
mk("heo24","Food Miles Calculator","Average distance food travels from farm to table by food category for major US metro areas","CHART","usa","bar-chart","Agriculture & Food Systems","USDA AMS + Leopold Center (ams.usda.gov)",52,62,68,70,48,62,68,78),
mk("heo25","Farmworker Heat Death Geography","Farmworker heat-related fatalities and illness reports by county mapped with heat index trends","MAP","usa","bivariate-choropleth","Agriculture & Food Systems","BLS + CDC NIOSH (bls.gov/iif)",75,52,70,68,78,68,65,82),
mk("heo26","Cover Crop Adoption Map","Cover crop usage rates by county showing soil health practice adoption trends","MAP","usa","choropleth","Agriculture & Food Systems","USDA NASS: Cover Crop Survey (nass.usda.gov)",42,42,72,62,42,68,62,88),
mk("heo27","Satellite Mega-Constellation Congestion","Number of active satellites by orbital altitude band over 10 years showing exponential growth","CHART","world","area-chart","Space & Exploration","UCS Satellite Database (ucsusa.org)",48,38,70,74,62,72,68,88),
mk("heo28","Lunar Landing Site Map","All successful and failed lunar landing attempts mapped on the Moon surface with mission details","MAP","world","special","Space & Exploration","NASA: Lunar Exploration Timeline (nasa.gov)",48,42,72,62,40,80,62,90),
mk("heo29","Space Tourism Price History","Cost per seat to space over time from Space Shuttle to commercial flights","CHART","world","line","Space & Exploration","Space Tourism Society + Company Reports (spacetourismsociety.org)",45,48,72,72,42,62,68,80),
mk("heo30","Radio Telescope Quiet Zones","Areas on Earth designated as radio quiet zones for astronomy mapped with encroaching wireless signals","MAP","world","dot-density","Space & Exploration","ITU: Radio Regulations + NRAO (nrao.edu)",42,35,68,74,42,74,75,82),
mk("heo31","Asteroid Mining Candidate Value","Near-Earth asteroids ranked by estimated mineral value with orbital accessibility scores","CHART","world","scatter","Space & Exploration","Asterank + JPL NEO Database (asterank.com)",42,35,65,78,42,68,80,75),
mk("heo32","Mars Mission Window Calendar","Optimal Mars launch windows over the next 20 years mapped with planned missions by space agency","CHART","world","timeline","Space & Exploration","NASA Mars Exploration Program (mars.nasa.gov)",42,38,72,65,40,68,62,85),
mk("heo33","Fallen Space Debris Impact Sites","Known locations where space debris has landed on Earth mapped with object origin","MAP","world","dot-density","Space & Exploration","Aerospace Corporation: Reentry Database (aerospace.org)",50,45,70,78,55,74,74,82),
mk("heo34","GPS Satellite Constellation Health","Current GPS satellite constellation status showing aging satellites and replacement schedule","CHART","world","special","Space & Exploration","GPS.gov: Current Constellation (gps.gov)",42,38,68,65,48,70,62,88),
mk("heo35","Exoplanet Discovery Rate by Method","Confirmed exoplanets discovered per year by detection method showing technique evolution","CHART","world","area-chart","Space & Exploration","NASA Exoplanet Archive (exoplanetarchive.ipac.caltech.edu)",42,35,72,68,38,65,65,92),
]

raw = open(DATA, 'r', encoding='utf-8').read()
existing = set(re.findall(r'id:"(heo\d+)"', raw))
new_ideas = [i for i in IDEAS if re.search(r'id:"(heo\d+)"', i).group(1) not in existing]
print(f"Injecting {len(new_ideas)} new ideas (skipping {len(IDEAS)-len(new_ideas)} dupes)")
if new_ideas:
    tail = ']; // end D'
    assert tail in raw, "Cannot find tail marker"
    raw = raw.replace(tail, ',\n'.join(new_ideas) + ',\n' + tail)
    open(DATA, 'w', encoding='utf-8').write(raw)
    print("Done")
else:
    print("Nothing to inject")
