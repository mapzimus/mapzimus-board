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
mk("hen01","Nearest Grocery Store Over 30 Minutes","Rural census tracts where the nearest full-service grocery store is more than 30 minutes drive","MAP","usa","choropleth","Rural America","USDA ERS: Food Access Research Atlas (ers.usda.gov)",68,70,72,68,65,70,62,90),
mk("hen02","Rural Ambulance Response Time Crisis","Average EMS response times in rural counties mapped with cardiac arrest survival rates","MAP","usa","choropleth","Rural America","NEMSIS: EMS Data (nemsis.org)",78,68,72,72,76,68,65,85),
mk("hen03","County Fair Survival Map","Counties that still hold annual county fairs mapped with attendance trends over 20 years","MAP","usa","dot-density","Rural America","IAFE: Fair Database (fairsandexpos.com)",50,68,72,68,42,70,70,78),
mk("hen04","Rural Childcare Desert","Rural counties with zero licensed childcare providers per 100 children under 5","MAP","usa","choropleth","Rural America","Bipartisan Policy Center: Childcare (bipartisanpolicy.org)",72,72,72,70,68,68,62,85),
mk("hen05","Main Street Vacancy Rate","Commercial vacancy rates on downtown main streets in small towns mapped with revitalization grant funding","MAP","usa","dot-density","Rural America","USDA Rural Development + CoStar (rd.usda.gov)",62,70,70,68,62,70,65,78),
mk("hen06","Rural Opioid Treatment Desert","Rural counties with zero medication-assisted treatment providers mapped with overdose death rates","MAP","usa","bivariate-choropleth","Rural America","SAMHSA: Buprenorphine Provider Locator (samhsa.gov)",75,62,72,68,76,68,62,88),
mk("hen07","Cell Phone Dead Zone Map","Areas with zero cell coverage from any carrier mapped with population density","MAP","usa","choropleth","Rural America","FCC: Mobile Broadband Map (fcc.gov)",58,72,74,68,55,72,65,85),
mk("hen08","Rural Teaching Hospital Closures","Teaching hospitals in rural areas that closed mapped with residency program relocations","MAP","usa","dot-density","Rural America","AAMC + CMS Provider Data (aamc.org)",70,55,70,72,72,68,68,82),
mk("hen09","Grain Elevator Ghost Network","Abandoned grain elevators mapped with active ones showing consolidation of rural agriculture infrastructure","MAP","usa","dot-density","Rural America","USDA GIPSA + Satellite Imagery (usda.gov)",52,55,68,72,48,74,72,78),
mk("hen10","Dunbar Number in Social Media","Average active social connections on platforms vs. Dunbars 150 limit by country and age group","CHART","world","scatter","Psychology & Behavior","Oxford Internet Institute + Platform Reports (oii.ox.ac.uk)",55,68,68,72,48,60,72,72),
mk("hen11","Retail Therapy Geography","Consumer spending spikes correlated with regional stress events and sentiment indices by metro","MAP","usa","choropleth","Psychology & Behavior","BEA: Personal Consumption + Google Trends (bea.gov)",52,72,65,72,48,62,72,75),
mk("hen12","Name Popularity and Career Outcomes","Correlation between first name popularity decade and career earnings controlling for demographics","CHART","usa","scatter","Psychology & Behavior","SSA Baby Names + Census Income (ssa.gov)",48,68,62,78,42,58,78,78),
mk("hen13","Phobia Prevalence by Region","Most commonly reported phobias by US region from clinical data mapped with environmental triggers","MAP","usa","choropleth","Psychology & Behavior","NIMH: Phobia Prevalence (nimh.nih.gov)",48,68,68,72,42,64,72,75),
mk("hen14","Misinformation Susceptibility by Media Diet","Belief in false claims correlated with primary news source and social media usage patterns","CHART","usa","bar-chart","Psychology & Behavior","MIT Media Lab + NewsGuard (medialab.mit.edu)",62,62,65,74,68,60,72,75),
mk("hen15","Gratitude Journal Effect Meta-Analysis","Effect sizes from gratitude intervention studies mapped by population type and duration","CHART","world","scatter","Psychology & Behavior","PsycINFO Meta-Analysis (apa.org)",42,58,65,65,38,55,68,78),
mk("hen16","ADHD Diagnosis Rate Geography","ADHD diagnosis rates in children by state mapped with prescribing rates and school policy differences","MAP","usa","bivariate-choropleth","Psychology & Behavior","CDC: ADHD Data (cdc.gov/ncbddd)",62,72,72,68,58,68,60,90),
mk("hen17","Imposter Syndrome by Profession","Self-reported imposter syndrome prevalence by profession from survey data","CHART","world","bar-chart","Psychology & Behavior","Journal of Behavioral Science + LinkedIn Survey (apa.org)",55,78,68,70,48,58,68,72),
mk("hen18","Child Marriage Legal Loopholes","States where child marriage is still legal mapped with minimum age and parental consent requirements","MAP","usa","choropleth","Children & Youth","Unchained At Last (unchainedatlast.org)",78,55,72,74,78,66,68,85),
mk("hen19","School Lunch Debt Shaming","School districts with lunch debt collection policies mapped with free lunch eligibility rates","MAP","usa","choropleth","Children & Youth","School Nutrition Association (schoolnutrition.org)",72,72,72,72,72,64,68,80),
mk("hen20","Pediatric Mental Health ER Visits","Emergency department visits for pediatric mental health crises by state over 5 years","CHART","usa","line","Children & Youth","CDC: WISQARS + HCUP (cdc.gov)",78,65,72,72,76,60,62,88),
mk("hen21","Recess Time Erosion","Average daily recess minutes in elementary schools by state over 20 years","CHART","usa","line","Children & Youth","CDC: School Health Profiles (cdc.gov/healthyyouth)",62,78,72,68,58,58,65,82),
mk("hen22","Juvenile Life Without Parole Sentences","States still sentencing juveniles to life without parole mapped with current prisoners and reform status","MAP","usa","choropleth","Children & Youth","Campaign for Fair Sentencing of Youth (fairsentencingofyouth.org)",75,50,70,72,78,64,68,82),
mk("hen23","Head Start Waitlist Map","Children on Head Start program waitlists by state as percentage of eligible population","MAP","usa","choropleth","Children & Youth","NHSA: Head Start Data (nhsa.org)",68,68,72,68,68,66,60,88),
mk("hen24","Teen Driver Fatal Crash Hotspots","Fatal crashes involving drivers aged 16-19 per capita by county mapped with drivers ed requirements","MAP","usa","choropleth","Children & Youth","IIHS: Teen Driving (iihs.org)",72,68,74,65,72,68,58,90),
mk("hen25","Childhood Obesity Rate by School District","Childhood obesity prevalence mapped at school district level with PE requirements and lunch program quality","MAP","usa","choropleth","Children & Youth","CDC: Youth Risk Behavior Survey (cdc.gov/yrbs)",65,70,72,65,65,68,58,88),
mk("hen26","Stadium Subsidy Payback Calculator","Public subsidies for professional sports stadiums mapped with estimated years to economic payback","MAP","usa","dot-density","Sports & Athletics","Brookings + Field of Schemes (fieldofschemes.com)",58,62,72,74,65,70,70,82),
mk("hen27","Olympic Host City Debt Hangover","Olympic host cities mapped with infrastructure debt remaining years after the games","MAP","world","dot-density","Sports & Athletics","Oxford Olympics Study + IOC (olympics.com)",60,55,72,74,62,72,70,85),
mk("hen28","Youth Concussion Rate by Sport","Concussion rates per 1000 athlete exposures by sport and age group","CHART","usa","bar-chart","Sports & Athletics","NCAA ISS + High School RIO (ncaa.org)",70,68,72,68,72,60,60,88),
mk("hen29","March Madness Bracket Economics","Workplace productivity losses during March Madness mapped with bracket pool participation rates","CHART","usa","bar-chart","Sports & Athletics","Challenger Gray + AGA Survey (challengergray.com)",42,75,72,68,40,60,70,78),
mk("hen30","Professional Athlete Hometown Density","Where professional athletes grew up per capita by county showing talent pipeline geography","MAP","usa","choropleth","Sports & Athletics","Sports Reference (sports-reference.com)",52,62,72,72,45,70,72,82),
mk("hen31","College Football Revenue vs. Academic Spending","Football program revenue compared to academic spending per student at FBS schools","CHART","usa","scatter","Sports & Athletics","NCAA Finances + IPEDS (ncaa.org)",58,62,72,76,68,62,68,88),
mk("hen32","Pickleball Court Explosion","Pickleball court construction rate by city over 5 years mapped with median player age","MAP","usa","dot-density","Sports & Athletics","USA Pickleball: Places2Play (usapickleball.org)",42,65,72,72,38,68,68,82),
mk("hen33","Sports Betting Revenue Geography","Legal sports betting handle and tax revenue by state since legalization","MAP","usa","choropleth","Sports & Athletics","AGA: State of the States (americangaming.org)",52,62,74,68,55,66,62,90),
mk("hen34","FIFA World Cup Host Country GDP Bump","GDP growth rate before during and after hosting the World Cup for every host nation","CHART","world","line","Sports & Athletics","World Bank + FIFA (worldbank.org)",48,48,72,68,48,60,65,85),
mk("hen35","Title IX Compliance Gap","NCAA schools with the widest gap between female student enrollment and female athlete participation","CHART","usa","bar-chart","Sports & Athletics","DOE: Equity in Athletics (ope.ed.gov)",62,58,70,72,68,58,68,90),
]

raw = open(DATA, 'r', encoding='utf-8').read()
existing = set(re.findall(r'id:"(hen\d+)"', raw))
new_ideas = [i for i in IDEAS if re.search(r'id:"(hen\d+)"', i).group(1) not in existing]
print(f"Injecting {len(new_ideas)} new ideas (skipping {len(IDEAS)-len(new_ideas)} dupes)")
if new_ideas:
    tail = ']; // end D'
    assert tail in raw, "Cannot find tail marker"
    raw = raw.replace(tail, ',\n'.join(new_ideas) + ',\n' + tail)
    open(DATA, 'w', encoding='utf-8').write(raw)
    print("Done")
else:
    print("Nothing to inject")
