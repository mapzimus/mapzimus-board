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
mk("her01","Veterinarian Desert Map","Rural counties with zero large-animal veterinarians mapped with livestock population","MAP","usa","bivariate-choropleth","Rural America","AVMA: Veterinary Workforce (avma.org)",58,55,72,72,60,70,68,82),
mk("her02","Rural Gas Station as Last Lifeline","Towns where the gas station is the only remaining commercial establishment mapped with population","MAP","usa","dot-density","Rural America","Census CBP + Google Places (census.gov)",62,72,68,74,58,70,74,78),
mk("her03","Wind Farm Lease Payment Geography","Annual payments to rural landowners from wind farm leases per county vs. farm income","MAP","usa","choropleth","Rural America","AWEA + USDA ERS (cleanpower.org)",52,60,72,72,48,70,68,82),
mk("her04","Rural School Consolidation Map","School districts that merged or consolidated over 20 years mapped with student travel distance increases","MAP","usa","dot-density","Rural America","NCES: School District Changes (nces.ed.gov)",62,68,70,68,60,68,65,85),
mk("her05","Septic System Failure Zones","Areas relying on aging septic systems mapped with contamination reports and sewer connection distance","MAP","usa","choropleth","Rural America","EPA: Septic Systems (epa.gov/septic)",55,58,68,68,62,68,62,82),
mk("her06","Rural Suicide Rate Crisis Belt","Rural counties with suicide rates 3x the national average mapped with mental health provider access","MAP","usa","bivariate-choropleth","Rural America","CDC WONDER + SAMHSA (wonder.cdc.gov)",80,62,72,68,78,68,60,88),
mk("her07","Dollar Store vs. Local Grocery Survival","Rural towns where dollar stores opened and local grocery stores subsequently closed within 3 years","MAP","usa","dot-density","Rural America","ILSR: Dollar Store Research (ilsr.org)",62,72,70,74,62,68,70,78),
mk("her08","Rural Public Transit Nonexistence","Counties with zero public transit options mapped with elderly and car-free population","MAP","usa","bivariate-choropleth","Rural America","NTD: Rural Transit (transit.dot.gov)",62,65,72,68,60,68,62,85),
mk("her09","Agricultural Chemical Exposure Clusters","Rural communities with elevated cancer rates near agricultural chemical application zones","MAP","usa","dot-density","Rural America","NCI: Cancer Atlas + EPA TRI (cancer.gov)",72,55,68,72,76,70,65,80),
mk("her10","Anchoring Effect in Real Estate","How listing price anchoring affects final sale prices by market showing buyer psychology patterns","CHART","usa","scatter","Psychology & Behavior","Zillow + MLS Data (zillow.com)",48,68,68,72,42,60,72,82),
mk("her11","Social Media Envy Index","Self-reported social comparison and envy from social media use by platform and country","CHART","world","bar-chart","Psychology & Behavior","Royal Society for Public Health (rsph.org.uk)",58,75,65,68,55,58,68,75),
mk("her12","Bystander Effect by City Density","Good Samaritan intervention rates in public emergencies by city population density","CHART","usa","scatter","Psychology & Behavior","Journal of Personality and Social Psychology + 911 Data (apa.org)",55,62,65,74,58,58,74,72),
mk("her13","Burnout Rate by Profession Map","Self-reported burnout rates by occupation mapped with average weekly hours and industry","CHART","usa","bar-chart","Psychology & Behavior","Gallup: State of the Workplace (gallup.com)",62,80,70,68,62,58,60,82),
mk("her14","Childhood Trauma ACE Score Geography","Average Adverse Childhood Experience scores by state mapped with adult health outcomes","MAP","usa","bivariate-choropleth","Psychology & Behavior","CDC: BRFSS ACE Module (cdc.gov/violenceprevention)",72,62,68,68,72,68,62,85),
mk("her15","Peak Creativity Hour by Profession","Self-reported most productive creative hours by profession showing chronotype patterns","CHART","world","bar-chart","Psychology & Behavior","AutoSleep + RescueTime Research (rescuetime.com)",40,72,68,70,38,58,72,70),
mk("her16","Grief Leave Policy Map","Bereavement leave policies by country and US state mapped with cultural attitudes toward grief","MAP","world","choropleth","Psychology & Behavior","SHRM: Leave Benefits (shrm.org)",62,65,70,68,55,64,65,82),
mk("her17","Road Rage Incident Geography","Road rage incidents involving weapons or confrontation by metro area mapped with commute stress indicators","MAP","usa","choropleth","Psychology & Behavior","AAA Foundation + NHTSA (aaafoundation.org)",58,72,70,68,65,66,62,82),
mk("her18","Shooting Range Lead Contamination","Outdoor shooting ranges with documented soil and groundwater lead contamination mapped with cleanup status","MAP","usa","dot-density","Guns & Weapons","EPA: Superfund + State DEQ (epa.gov)",58,48,70,72,68,68,68,80),
mk("her19","Gun Show Frequency Map","Number of gun shows held per year by state mapped with show size and vendor counts","MAP","usa","choropleth","Guns & Weapons","Gun Show Trader + ATF (gunshowtrader.com)",45,52,72,65,52,66,60,85),
mk("her20","Teacher Gun Training Programs","States allowing armed teachers mapped with training program requirements and participation rates","MAP","usa","choropleth","Guns & Weapons","Giffords + State DOE (giffords.org)",62,58,70,72,72,64,68,85),
mk("her21","Firearm Suicide vs. Homicide Ratio","States where gun suicides outnumber gun homicides mapped with ratio showing hidden epidemic","MAP","usa","choropleth","Guns & Weapons","CDC WONDER: Firearm Deaths (wonder.cdc.gov)",72,55,72,74,72,66,68,92),
mk("her22","3D Printed Gun Seizure Timeline","Law enforcement seizures of 3D-printed firearms by year and jurisdiction","CHART","usa","line","Guns & Weapons","ATF + State Police Reports (atf.gov)",55,42,68,78,68,62,74,72),
mk("her23","Mandatory Waiting Period Effectiveness","States with firearm waiting periods mapped with impulsive gun violence rate changes after implementation","MAP","usa","choropleth","Guns & Weapons","RAND: Gun Policy (rand.org/gun-policy)",62,55,70,68,68,64,65,85),
mk("her24","Military Surplus Equipment to Police","Military equipment transferred to police departments through 1033 program by department and item type","MAP","usa","dot-density","Guns & Weapons","DLA: LESO 1033 Program (dla.mil)",58,48,68,76,72,70,68,88),
mk("her25","Gun Violence Restraining Order Usage","Emergency gun violence restraining order filings per capita by state mapped with petitioner type","MAP","usa","choropleth","Guns & Weapons","UC Davis: GVRO Study (health.ucdavis.edu)",58,50,70,68,68,64,65,82),
mk("her26","High School Football Brain Injury Belt","High school football participation rates by state mapped with reported concussion protocols and CTE research findings","MAP","usa","choropleth","Sports & Athletics","NFHS + BU CTE Center (nfhs.org)",72,65,68,72,74,66,62,82),
mk("her27","Pay Gap in Womens Professional Sports","Average salary in womens vs. mens professional leagues by sport showing the multiplier gap","CHART","world","grouped-bar","Sports & Athletics","ESPN + League CBAs (espn.com)",68,62,72,68,68,60,62,82),
mk("her28","Olympic Medal Efficiency","Olympic medals per GDP dollar and per capita by country showing most efficient medal producers","CHART","world","scatter","Sports & Athletics","Olympics.com + World Bank (olympics.com)",45,42,72,76,42,62,72,90),
mk("her29","Youth Football Participation Exodus","Youth tackle football registration decline by state over 10 years mapped with flag football growth","CHART","usa","line","Sports & Athletics","USA Football (usafootball.com)",62,65,72,70,62,58,65,82),
mk("her30","Athlete Activism Timeline","Professional athletes taking public political stances by sport and decade showing evolution","CHART","world","timeline","Sports & Athletics","Wikipedia: Athlete Activism + ESPN (espn.com)",55,55,65,68,55,60,72,75),
mk("her31","College Athletic Scholarship Geography","Where D1 athletic scholarships go by sport and recruiting region showing talent pipelines","MAP","usa","flow-map","Sports & Athletics","NCAA: Demographics Database (ncaa.org)",55,62,70,68,48,72,65,85),
mk("her32","Drone Racing League Growth","Drone racing events and participants worldwide mapped with prize pool growth","MAP","world","dot-density","Sports & Athletics","DRL + MultiGP (thedroneracingleague.com)",38,38,68,72,35,68,74,72),
mk("her33","Marathon Finish Time Distribution","Marathon finish time distributions by age and gender showing how they differ across major races","CHART","world","line","Sports & Athletics","Marathon Guide (marathonguide.com)",42,58,72,62,38,60,62,88),
mk("her34","Sports Gambling Addiction Hotline Calls","Problem gambling hotline call volume by state mapped with sports betting legalization dates","MAP","usa","choropleth","Sports & Athletics","NCPG: Helpline Data (ncpgambling.org)",65,62,70,72,68,64,68,85),
mk("her35","Esports Earnings Geography","Top esports player earnings by country of origin mapped with gaming culture investment","MAP","world","choropleth","Sports & Athletics","Esports Earnings (esportsearnings.com)",42,45,72,68,42,68,65,85),
]

raw = open(DATA, 'r', encoding='utf-8').read()
existing = set(re.findall(r'id:"(her\d+)"', raw))
new_ideas = [i for i in IDEAS if re.search(r'id:"(her\d+)"', i).group(1) not in existing]
print(f"Injecting {len(new_ideas)} new ideas (skipping {len(IDEAS)-len(new_ideas)} dupes)")
if new_ideas:
    tail = ']; // end D'
    assert tail in raw, "Cannot find tail marker"
    raw = raw.replace(tail, ',\n'.join(new_ideas) + ',\n' + tail)
    open(DATA, 'w', encoding='utf-8').write(raw)
    print("Done")
else:
    print("Nothing to inject")
