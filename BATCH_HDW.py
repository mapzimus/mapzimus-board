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
mk("hdw01","Dollar General Density Map","Dollar General store locations per capita by county mapped against poverty and grocery access","MAP","usa","dot-density","Economy & Trade","Dollar General: Store Locator + USDA Food Access (ers.usda.gov)",62,72,70,68,60,76,58,88),
mk("hdw02","Rural Hospital Closure Cascade","Closed rural hospitals mapped with drive time to nearest ER and maternal mortality change","MAP","usa","dot-density","Health & Wellbeing","UNC: Rural Hospital Closures (shepscenter.unc.edu)",78,70,72,68,80,74,65,85),
mk("hdw03","One-Stoplight Towns Losing Post Offices","Small towns that lost their post office mapped against population decline","MAP","usa","dot-density","Infrastructure & Systems","USPS: Post Office Closures + Census (usps.com)",68,72,62,70,65,72,68,82),
mk("hdw04","Volunteer Fire Department Burnout","Volunteer firefighter recruitment shortfalls by rural county mapped with response times","MAP","usa","bivariate-choropleth","Public Safety","NFPA: Fire Department Survey (nfpa.org)",70,68,65,72,74,66,64,78),
mk("hdw05","Rural Broadband Dead Zones","Census blocks with zero broadband providers mapped against income and education","MAP","usa","choropleth","Technology & Data","FCC: Broadband Map (broadbandmap.fcc.gov)",65,74,76,58,68,72,55,90),
mk("hdw06","Aging in Place Without Services","Rural counties where 25%+ of residents are 65+ with zero home health agencies","MAP","usa","bivariate-choropleth","Health & Wellbeing","CMS: Provider Data + Census ACS (data.cms.gov)",72,68,70,72,75,68,66,84),
mk("hdw07","Rural Veterinarian Shortage","Counties classified as veterinary shortage areas mapped against livestock density","MAP","usa","bivariate-choropleth","Agriculture & Food","USDA: Veterinary Shortage Areas (usda.gov)",55,58,70,72,60,68,70,82),
mk("hdw08","Loneliness Epidemic by Age Group","Self-reported loneliness rates by age cohort and living arrangement over 10 years","CHART","usa","line-chart","Health & Wellbeing","Cigna: Loneliness Index (cigna.com)",78,80,72,65,68,58,62,80),
mk("hdw09","Therapy Deserts","Counties with zero licensed psychologists or psychiatrists mapped against suicide rates","MAP","usa","bivariate-choropleth","Health & Wellbeing","HRSA: Shortage Areas (data.hrsa.gov)",75,72,70,68,78,72,64,85),
mk("hdw10","Social Media and Teen Depression","Teen depression diagnosis rates by state plotted against smartphone adoption timeline","CHART","usa","dual-axis","Health & Wellbeing","CDC YRBS + Pew: Teen Survey (cdc.gov/yrbs)",72,78,65,62,70,58,60,82),
mk("hdw11","Adverse Childhood Experiences Heat Map","ACE scores by county mapped against adult health outcomes and incarceration rates","MAP","usa","bivariate-choropleth","Health & Wellbeing","CDC: ACE Data (cdc.gov/aces)",80,72,68,65,76,70,62,80),
mk("hdw12","Burnout by Profession","Self-reported burnout rates by occupation ranked with average hours worked and autonomy scores","RANK","usa","bar-chart","Labor & Work","Gallup: Workplace Survey (gallup.com)",70,82,74,62,65,58,55,82),
mk("hdw13","Grief Leave Policies","Countries and US states offering bereavement leave by duration and relationship coverage","MAP","world","choropleth","Labor & Work","SHRM: Benefits Survey (shrm.org)",72,75,70,68,58,60,65,78),
mk("hdw14","Cognitive Behavioral Therapy Access","Wait times for CBT appointments by metro area mapped against anxiety prevalence","MAP","usa","bivariate-choropleth","Health & Wellbeing","SAMHSA: Treatment Locator (samhsa.gov)",68,72,68,62,65,66,58,80),
mk("hdw15","Child Poverty After the Child Tax Credit","Child poverty rates by county before, during, and after the expanded CTC","CHART","usa","line-chart","Poverty & Inequality","Census: SAIPE + Columbia CPSP (povertycenter.columbia.edu)",78,75,74,68,72,60,62,88),
mk("hdw16","Children Without Health Insurance","Uninsured rate for children under 18 by state mapped with Medicaid expansion status","MAP","usa","bivariate-choropleth","Health & Wellbeing","Census: SAHIE (census.gov/sahie)",74,72,72,60,70,66,55,90),
mk("hdw17","Lead Exposure Risk by ZIP Code","Estimated child lead exposure risk based on housing age and water system mapped by ZIP","MAP","usa","choropleth","Health & Wellbeing","CDC: Lead Data + Census Housing Age (cdc.gov)",80,72,68,70,82,74,65,82),
mk("hdw18","School Lunch Debt Map","Accumulated unpaid school meal debt per student by district","MAP","usa","choropleth","Education","SNA: School Meal Trends (schoolnutrition.org)",75,78,70,68,72,62,60,75),
mk("hdw19","Foster Care Hotspots","Counties with the highest foster care entry rates per 1000 children mapped with opioid rates","MAP","usa","bivariate-choropleth","Health & Wellbeing","AFCARS: Foster Care Data (acf.hhs.gov)",80,68,70,65,78,72,62,85),
mk("hdw20","Kids Who Walk to School","Percentage of children walking or biking to school by metro area over 50 years","CHART","usa","area-chart","Transportation &Tic","NHTS: Travel Survey (nhts.ornl.gov)",58,72,68,70,52,65,62,82),
mk("hdw21","Child Marriage Legal Loopholes","US states where minors can still legally marry with parental or judicial consent and ages allowed","MAP","usa","choropleth","Law & Justice","Unchained At Last: Child Marriage Data (unchainedatlast.org)",78,62,70,80,82,64,72,80),
mk("hdw22","Space Debris Density","Tracked orbital debris objects by altitude band with collision probability zones","MAP","world","special","Science & Discovery","ESA: Space Debris Office (esa.int/debris)",55,48,70,74,68,82,72,80),
mk("hdw23","Artemis vs. Apollo Cost Comparison","Inflation-adjusted mission costs per kg to the Moon across Apollo and Artemis programs","CHART","world","bar-chart","Science & Discovery","NASA: Budget Data (nasa.gov/budget)",58,55,75,72,52,62,68,85),
mk("hdw24","Satellite Megaconstellation Light Pollution","Predicted visibility of Starlink and other satellite trains by latitude and time of year","MAP","world","choropleth","Science & Discovery","IAU: Satellite Impact (iau.org)",60,52,68,76,65,78,74,75),
mk("hdw25","Private Space Launch Sites","Active and proposed commercial spaceports worldwide mapped with launch frequency","MAP","world","dot-density","Science & Discovery","FAA: Licensed Launch Sites (faa.gov)",50,45,72,68,48,78,66,82),
mk("hdw26","Exoplanet Discovery Timeline","Confirmed exoplanets by discovery method over time with habitable zone candidates highlighted","CHART","world","area-chart","Science & Discovery","NASA: Exoplanet Archive (exoplanetarchive.ipac.caltech.edu)",55,48,72,75,50,70,72,92),
mk("hdw27","ISS Research Output","Scientific papers published from ISS experiments by field and contributing country","CHART","world","treemap","Science & Discovery","NASA: ISS Research (nasa.gov/iss-science)",50,45,70,68,42,60,65,85),
mk("hdw28","Mars Mission Success Rate","All Mars missions mapped on a timeline with success, partial, and failure outcomes by agency","CHART","world","timeline","Science & Discovery","Planetary Society: Mars Missions (planetary.org)",52,50,74,65,48,68,62,90),
mk("hdw29","Rural School Consolidation","School districts that merged or closed schools mapped with student commute time increase","MAP","usa","dot-density","Education","NCES: School District Data (nces.ed.gov)",68,72,68,62,65,70,60,82),
mk("hdw30","Psychedelic Therapy Legalization Wave","States and cities that have decriminalized or legalized psilocybin for therapy with timeline","MAP","usa","choropleth","Health & Wellbeing","MAPS: Policy Tracker (maps.org)",62,58,70,72,55,62,70,78),
mk("hdw31","Rural Brain Drain","Net out-migration of 18-24 year olds from rural counties mapped with college proximity","MAP","usa","bivariate-choropleth","Demographics","Census: Migration Flows + NCES (census.gov)",70,68,72,62,68,72,60,85),
mk("hdw32","Space Economy Revenue Breakdown","Global space economy revenue by sector — satellites, launch, ground equipment, services — over time","CHART","world","area-chart","Economy & Trade","SIA: State of Satellite (sia.org)",48,45,74,65,42,62,60,85),
mk("hdw33","Screen Time by Age","Average daily screen time by age group and device type across countries","CHART","world","grouped-bar","Health & Wellbeing","Common Sense Media: Media Use Census (commonsensemedia.org)",65,80,72,60,58,55,52,82),
mk("hdw34","Playground Inequality","Public playground equipment quality score by neighborhood income level in major cities","MAP","usa","bivariate-choropleth","Poverty & Inequality","KaBOOM!: Playspace Data (kaboom.org)",72,75,65,70,62,72,68,70),
mk("hdw35","Dark Sky Preserves","Certified dark sky areas worldwide mapped against population density and light pollution growth","MAP","world","dot-density","Environment & Climate","IDA: Dark Sky Places (darksky.org)",55,52,70,72,48,82,70,82),
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
print(f"Injected {len(new)} new ideas (HDW batch)")
