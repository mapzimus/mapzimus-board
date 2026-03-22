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
mk("hea01","Main Street Vacancy Tracker","Commercial vacancy rates on main streets of small towns mapped with population trend","MAP","usa","dot-density","Economy & Trade","Census: CBP + USPS Vacancy Data (census.gov)",65,72,68,62,65,72,58,82),
mk("hea02","Rural EMS Response Time Crisis","Average emergency response times in rural counties mapped against distance to nearest hospital","MAP","usa","bivariate-choropleth","Health & Wellbeing","NRHA: Rural Health Data (ruralhealth.us)",78,70,72,65,80,72,62,80),
mk("hea03","Disappearing Rural Banks","Bank branch closures in rural counties over 20 years mapped with nearest branch distance","MAP","usa","dot-density","Economy & Trade","FDIC: Summary of Deposits (fdic.gov)",65,72,70,68,62,70,60,88),
mk("hea04","County Fair Attendance Decline","Annual county fair attendance trends mapped with local agricultural employment change","MAP","usa","dot-density","Culture & Religion","IAFE: Fair Industry Statistics (fairsandexpos.com)",55,68,62,65,52,70,64,72),
mk("hea05","Rural Teacher Shortage Severity","Unfilled teaching positions as percentage of total by rural district mapped with salary comparison","MAP","usa","bivariate-choropleth","Education","NCES: Teacher Shortage Data (nces.ed.gov)",72,70,72,62,68,68,58,82),
mk("hea06","Cell Dead Zone Map","Areas with zero cellular coverage mapped against population and highway routes","MAP","usa","choropleth","Technology & Data","FCC: Mobile Coverage Map (broadbandmap.fcc.gov)",60,74,72,58,55,76,55,88),
mk("hea07","Small Town Grocery Store Survival","Independent grocery stores in towns under 5000 people mapped with nearest chain competitor distance","MAP","usa","dot-density","Economy & Trade","USDA: Food Access Research Atlas (ers.usda.gov)",68,75,68,65,62,72,60,82),
mk("hea08","Decision Fatigue in Parole Boards","Parole grant rates by time of day and day of week across state parole boards","CHART","usa","line-chart","Law & Justice","PNAS: Extraneous Factors in Judicial Decisions (pnas.org)",62,58,68,82,60,55,80,75),
mk("hea09","Dunning-Kruger in Professional Fields","Self-assessed competence vs. measured performance by profession — medicine, law, finance, tech","CHART","world","scatter","Education","APA: Metacognition Studies (apa.org)",55,72,65,80,52,58,78,70),
mk("hea10","Color Psychology in Fast Food Branding","Dominant brand colors used by fast food chains mapped against consumer behavior research","CHART","world","bar-chart","Economy & Trade","Color Research Institute + Brand Analysis (colorcom.com)",48,72,62,74,42,68,72,72),
mk("hea11","Nostalgia Cycle Length","Time lag between cultural trends and their nostalgic revival measured across decades","CHART","usa","line-chart","Culture & Religion","Google Trends: Nostalgia Peaks (trends.google.com)",50,75,60,78,45,55,82,75),
mk("hea12","Bystander Effect by City Density","Documented bystander intervention rates in emergencies correlated with population density","CHART","world","scatter","Health & Wellbeing","APA: Bystander Research (apa.org)",65,68,62,72,60,58,75,68),
mk("hea13","Imposter Syndrome Prevalence by Field","Self-reported imposter syndrome rates by professional field and career stage","CHART","world","bar-chart","Health & Wellbeing","International Journal of Behavioral Science (ijbs-online.com)",62,80,65,68,55,55,65,72),
mk("hea14","Seasonal Affective Disorder Latitude Map","SAD diagnosis rates by latitude mapped with average winter daylight hours","MAP","usa","bivariate-choropleth","Health & Wellbeing","NIMH: SAD Data (nimh.nih.gov)",65,72,74,60,55,70,58,85),
mk("hea15","Child Food Insecurity After School Ends","Summer food insecurity spike for children on free lunch programs by county","MAP","usa","choropleth","Poverty & Inequality","Feeding America: Map the Meal Gap (feedingamerica.org)",80,75,72,62,74,66,58,85),
mk("hea16","Kindergarten Readiness Gap","Percentage of children entering kindergarten below developmental benchmarks by district and income","MAP","usa","choropleth","Education","ECLS: Early Childhood Data (nces.ed.gov/ecls)",72,72,70,62,68,64,58,82),
mk("hea17","Children in Single-Parent Military Families","Military dependents in single-parent households by installation with deployment frequency","MAP","usa","proportional-symbol","Demographics","DoD: Demographics Report (militaryonesource.mil)",70,62,65,68,72,66,68,78),
mk("hea18","Youth Homelessness by School District","Students identified as homeless under McKinney-Vento by district mapped with shelter availability","MAP","usa","bivariate-choropleth","Poverty & Inequality","NCHE: Federal Data Summary (nche.ed.gov)",80,72,70,65,78,68,60,85),
mk("hea19","Childhood Asthma and Highway Proximity","Pediatric asthma rates mapped against residential proximity to major highways","MAP","usa","bivariate-choropleth","Health & Wellbeing","EPA: Air Quality + CDC (epa.gov/air-quality)",75,72,70,68,74,72,62,82),
mk("hea20","Recess Time Erosion","Average daily recess minutes for elementary students by state over 20 years","CHART","usa","line-chart","Education","CDC: School Health Profiles (cdc.gov/schoolhealth)",65,78,72,68,62,58,60,80),
mk("hea21","Juvenile Detention Racial Disparities","Juvenile detention rates by race per 100,000 youth by state","MAP","usa","choropleth","Law & Justice","OJJDP: Juvenile Justice Data (ojjdp.ojp.gov)",78,62,72,65,80,64,62,88),
mk("hea22","College Athletic Revenue Inequality","Revenue generated by mens vs. womens sports programs by NCAA division and conference","CHART","usa","grouped-bar","Gender & Equity","NCAA: Financial Reports (ncaa.org)",68,65,72,68,70,60,62,88),
mk("hea23","Head Injury Rates by Youth Sport","Concussion rates per 1000 athlete-exposures by sport for athletes under 18","CHART","usa","bar-chart","Health & Wellbeing","CDC: Youth Sports Injuries (cdc.gov)",72,75,74,62,70,58,55,85),
mk("hea24","Olympic Host City Economic Hangover","GDP growth and infrastructure utilization rates of Olympic host cities 5 years after games","CHART","world","bar-chart","Economy & Trade","Oxford: Olympic Study (eureka.sbs.ox.ac.uk)",58,60,72,74,62,62,68,82),
mk("hea25","Pickleball Court Takeover","Tennis courts converted to pickleball by city with participation demographics","MAP","usa","dot-density","Sports & Recreation","APP: Pickleball Fact Sheet (usapickleball.org)",48,72,65,68,48,68,62,78),
mk("hea26","Minor League Baseball Contraction","Minor league teams eliminated in the 2021 reorganization mapped with community impact","MAP","usa","dot-density","Sports & Recreation","MiLB: Affiliates (milb.com)",62,65,68,65,60,70,60,82),
mk("hea27","Title IX Compliance Gaps","Colleges failing to meet Title IX athletic participation proportionality by conference","CHART","usa","bar-chart","Gender & Equity","DOE: Equity in Athletics (ope.ed.gov/athletics)",68,62,72,65,72,58,62,88),
mk("hea28","Rural Pharmacy Deserts","Rural counties that lost their last pharmacy mapped with nearest pharmacy drive time","MAP","usa","dot-density","Health & Wellbeing","NCPA: Pharmacy Data (ncpa.org)",72,70,68,68,70,72,62,82),
mk("hea29","Confirmation Bias in News Consumption","Percentage of news consumed from ideologically aligned sources by political affiliation over time","CHART","usa","area-chart","Media & Information","Pew: News Consumption Survey (pewresearch.org)",58,72,68,65,60,55,62,82),
mk("hea30","Youth Sports Travel Spending","Average family annual spending on youth travel sports by sport and income quintile","CHART","usa","bar-chart","Sports & Recreation","WinterGreen Research: Youth Sports (wintergreenresearch.com)",60,78,70,68,55,55,58,78),
mk("hea31","Sleep Deprivation Geography","Average sleep duration by county mapped against shift work prevalence and commute time","MAP","usa","bivariate-choropleth","Health & Wellbeing","CDC: BRFSS Sleep Data (cdc.gov/brfss)",68,78,72,60,62,68,58,85),
mk("hea32","Pro Athlete Hometown Clusters","Birthplaces of active professional athletes per capita by county across major sports","MAP","usa","dot-density","Sports & Recreation","Sports Reference (sports-reference.com)",48,65,68,72,42,74,65,82),
mk("hea33","Rural Childcare Provider Shortage","Licensed childcare slots per child under 5 by rural county with cost as percentage of income","MAP","usa","bivariate-choropleth","Poverty & Inequality","CCAoA: Child Care Data (childcareaware.org)",74,75,70,62,72,66,58,82),
mk("hea34","Parasocial Relationship Intensity","Self-reported emotional attachment to fictional characters and influencers by age and platform","CHART","world","bar-chart","Health & Wellbeing","APA: Media Psychology (apa.org)",55,72,60,74,48,55,76,68),
mk("hea35","High School Football Participation Decline","High school football participation rates by state over 15 years with safety concern surveys","CHART","usa","line-chart","Sports & Recreation","NFHS: Participation Survey (nfhs.org)",62,70,72,62,58,58,55,88),
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
print(f"Injected {len(new)} new ideas (HEA batch)")
