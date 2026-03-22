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
mk("hef01","Statute of Limitations Loopholes","Crimes with expired statutes of limitations by type and state — how many serious offenses go unprosecutable","MAP","usa","choropleth","Law & Justice","NCSL: Statute of Limitations (ncsl.org)",68,60,70,74,72,64,68,82),
mk("hef02","Non-Compete Agreement Enforceability","States by non-compete enforcement level mapped with startup formation rates and worker mobility","MAP","usa","choropleth","Law & Justice","EPI: Non-Compete Data (epi.org)",60,68,72,68,62,64,62,85),
mk("hef03","Incarceration Cost Per Prisoner","Annual cost to incarcerate one person by state mapped against per-pupil education spending","MAP","usa","bivariate-choropleth","Law & Justice","Vera Institute: Price of Prisons (vera.org)",72,68,74,72,70,66,62,88),
mk("hef04","Sovereign Immunity Abuse","Government entities invoking sovereign immunity to avoid liability in wrongful death and injury cases by state","MAP","usa","choropleth","Law & Justice","Legal Scholarship + Court Records (westlaw.com)",68,58,65,76,74,62,72,72),
mk("hef05","Police Body Camera Footage FOIA Denials","Percentage of body camera footage FOIA requests denied by department with reason breakdown","CHART","usa","bar-chart","Law & Justice","Reporters Committee: FOIA Data (rcfp.org)",68,62,68,72,76,58,68,75),
mk("hef06","Criminalization of Homelessness","Cities that have enacted anti-camping, anti-panhandling, or sit-lie ordinances mapped with homeless count","MAP","usa","dot-density","Law & Justice","NLCHP: Housing Not Handcuffs (nlchp.org)",75,68,68,70,76,68,65,82),
mk("hef07","Judicial Vacancy Crisis","Federal court vacancies by circuit and district mapped with average case wait time","MAP","usa","choropleth","Law & Justice","USCOURTS: Judicial Vacancies (uscourts.gov/judges-judgeships/judicial-vacancies)",62,55,72,68,70,64,62,88),
mk("hef08","Depopulation Speed Record","Fastest-depopulating counties in the US over 10 years mapped with cause — aging, migration, industry loss","MAP","usa","choropleth","Demographics","Census: Population Estimates (census.gov)",65,62,72,70,68,74,62,90),
mk("hef09","Where Twins Are Born Most","Twin birth rates by country mapped with IVF usage rates and maternal age trends","MAP","world","bivariate-choropleth","Demographics","CDC: Natality Data + WHO (cdc.gov/nchs)",48,55,70,78,42,66,72,88),
mk("hef10","Last Speakers of Endangered Languages","Locations of languages with fewer than 100 speakers worldwide mapped with speaker age","MAP","world","dot-density","Demographics","Endangered Languages Project (endangeredlanguages.com)",72,55,65,78,70,72,80,75),
mk("hef11","Age of First Marriage Gap","Average age at first marriage for men vs. women by country showing cultural variation","MAP","world","bivariate-choropleth","Demographics","UN: World Marriage Data (un.org/development/desa/pd)",55,65,70,68,52,66,58,90),
mk("hef12","Pet Population Exceeding Child Population","Metro areas where registered pets outnumber children under 18 with trend since 2000","MAP","usa","choropleth","Demographics","APPA + Census: Pet vs. Child Count (americanpetproducts.org)",45,75,68,80,42,65,72,80),
mk("hef13","Life Expectancy by Congressional District","Life expectancy at birth mapped by congressional district showing 20+ year gaps","MAP","usa","choropleth","Demographics","IHME: Life Expectancy Data (healthdata.org)",78,72,74,70,72,70,62,88),
mk("hef14","Grandparents Raising Grandchildren","Counties where grandparents are primary caregivers for grandchildren mapped with contributing factors","MAP","usa","choropleth","Demographics","Census ACS: Grandparents Data (census.gov)",72,68,70,65,68,66,60,88),
mk("hef15","Iranian Brain Drain Destinations","Top destination countries for Iranian emigrants by education level and profession","MAP","world","flow-map","Migration & Borders","UNDESA: International Migration (un.org/migration)",65,52,70,68,62,74,66,78),
mk("hef16","Euphrates River Drying","Euphrates River flow volume decline over 30 years by measurement station with Turkish dam impact","CHART","middle-east","line-chart","Environment & Climate","FAO: AQUASTAT Euphrates (fao.org/aquastat)",68,50,72,72,76,74,70,80),
mk("hef17","Palestinian Olive Tree Destruction","Documented olive tree destruction events in the West Bank mapped with economic impact to farmers","MAP","middle-east","dot-density","Agriculture & Food","OCHA: Protection of Civilians (ochaopt.org)",78,48,62,68,82,72,70,72),
mk("hef18","Irans Proxy Network Map","Iranian-backed militia and political organizations across the Middle East with estimated funding","MAP","middle-east","special","Conflict & Security","CSIS: Iran Proxy Map (csis.org)",60,45,68,72,78,76,68,78),
mk("hef19","Dubai Construction Worker Conditions","Construction worker fatality and injury rates in Dubai vs. international benchmarks by year","CHART","middle-east","bar-chart","Labor & Work","HRW: UAE Labor Rights (hrw.org)",75,50,68,70,78,62,66,72),
mk("hef20","Middle East Female Labor Participation","Female labor force participation rates by MENA country over 20 years with policy change markers","CHART","middle-east","line-chart","Gender & Equity","ILO: Labour Statistics (ilo.org)",62,55,72,68,60,60,62,85),
mk("hef21","Yemeni Cultural Heritage Destruction","UNESCO sites and cultural landmarks damaged or destroyed in Yemen conflict mapped","MAP","middle-east","dot-density","Conflict & Security","UNESCO: Damage Assessment (unesco.org)",75,48,62,68,80,76,72,72),
mk("hef22","Gun Dealer Inspection Rates","Percentage of federal firearms licensees inspected by ATF per year by state","MAP","usa","choropleth","Public Safety","ATF: FFL Inspection Data (atf.gov)",58,55,72,74,68,64,66,85),
mk("hef23","Guns Stolen From Cars","Firearms reported stolen from vehicles by city mapped with car break-in rates","MAP","usa","dot-density","Public Safety","Everytown: Stolen Guns (everytownresearch.org)",65,62,68,72,70,68,62,80),
mk("hef24","Military-Grade Weapons in Civilian Hands","Legal civilian ownership of .50 caliber rifles and other military-grade weapons by state","MAP","usa","choropleth","Public Safety","ATF: Firearms Trace Data (atf.gov)",60,52,68,74,72,66,68,78),
mk("hef25","Gun Violence Near Schools and Churches","Shootings occurring within 500 feet of schools and houses of worship by city","MAP","usa","dot-density","Public Safety","GVA: Incident Data (gunviolencearchive.org)",80,68,65,62,82,72,58,82),
mk("hef26","Interstate Gun Trafficking Flows","Source states for firearms recovered in crimes in other states — the gun pipeline","MAP","usa","flow-map","Public Safety","ATF: Interstate Trace Data (atf.gov)",68,58,72,70,74,78,65,85),
mk("hef27","Hunting License Decline","Hunting licenses sold per capita by state over 30 years with wildlife management budget impact","CHART","usa","line-chart","Environment & Climate","USFWS: Hunting License Data (fws.gov)",55,62,72,65,55,62,58,90),
mk("hef28","Silencer Ownership Growth","Registered suppressors per capita by state over 10 years with hearing protection argument data","MAP","usa","choropleth","Public Safety","ATF: NFA Registry (atf.gov)",48,52,70,72,55,62,62,82),
mk("hef29","Jury Trial Disappearance","Percentage of federal cases going to jury trial over 50 years — the vanishing trial phenomenon","CHART","usa","line-chart","Law & Justice","Federal Judicial Center: Caseload Statistics (fjc.gov)",60,58,72,78,62,55,72,88),
mk("hef30","Death Row Exoneration Rate by State","Exonerations per 100 death sentences imposed by state with average years served","MAP","usa","choropleth","Law & Justice","DPIC: Exoneration Data (deathpenaltyinfo.org)",78,62,72,76,78,64,68,85),
mk("hef31","MENA Youth Unemployment Bomb","Youth unemployment rates (15-24) across Middle East and North Africa with protest correlation","MAP","middle-east","choropleth","Economy & Trade","World Bank: Youth Unemployment (data.worldbank.org)",70,55,72,68,75,68,65,88),
mk("hef32","Intergenerational Income Mobility by County","Probability of a child born in the bottom quintile reaching the top quintile by county","MAP","usa","choropleth","Demographics","Opportunity Atlas: Chetty et al. (opportunityatlas.org)",72,72,74,68,65,72,65,90),
mk("hef33","Teacher Carrying Guns in Schools","States allowing armed teachers mapped with school shooting proximity and public opinion","MAP","usa","choropleth","Education","Giffords: Guns in Schools (giffords.org)",72,68,68,70,78,66,62,82),
mk("hef34","Execution Methods Still Legal","Legal execution methods by state — lethal injection, electric chair, firing squad, gas chamber, hanging","MAP","usa","choropleth","Law & Justice","DPIC: State Methods (deathpenaltyinfo.org)",65,58,72,72,70,65,62,88),
mk("hef35","Kuwaiti Investment Authority Global Portfolio","KIA sovereign wealth fund investment locations worldwide by sector and estimated value","MAP","world","proportional-symbol","Economy & Trade","SWF Institute: KIA Profile (swfinstitute.org)",45,40,72,68,50,72,62,78),
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
print(f"Injected {len(new)} new ideas (HEF batch)")
