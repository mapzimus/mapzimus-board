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
mk("heb01","Private Prison Lobbying Spending","Campaign contributions from private prison companies to state legislators mapped with incarceration policy votes","MAP","usa","choropleth","Law & Justice","OpenSecrets: Private Prison Lobbying (opensecrets.org)",70,58,68,74,78,64,70,82),
mk("heb02","Debtors Prison Comeback","States and counties jailing people for unpaid fines and fees mapped with median fine amounts","MAP","usa","dot-density","Law & Justice","ACLU: Debtors Prison Data (aclu.org)",78,72,68,74,80,64,68,78),
mk("heb03","Environmental Crime Prosecution Rates","EPA criminal enforcement actions per industrial facility by region over 20 years","MAP","usa","choropleth","Law & Justice","EPA: Enforcement Data (echo.epa.gov)",65,55,70,72,68,66,68,85),
mk("heb04","Asset Forfeiture Spending","What police departments bought with civil asset forfeiture funds — vehicles, weapons, surveillance gear","CHART","usa","treemap","Law & Justice","IJ: Forfeiture Transparency (ij.org/report/policing-for-profit)",68,62,65,78,72,62,72,78),
mk("heb05","Plea Bargain Rates by Crime Type","Percentage of cases resolved through plea bargains by offense category and federal district","CHART","usa","bar-chart","Law & Justice","BJS: Federal Justice Statistics (bjs.gov)",60,55,72,70,65,58,64,85),
mk("heb06","Fines and Fees Revenue Dependency","Municipalities where court fines represent 10%+ of total revenue mapped with income data","MAP","usa","choropleth","Law & Justice","Fines and Fees Justice Center (finesandfeesjusticecenter.org)",72,68,70,74,76,66,68,82),
mk("heb07","Cash Bail Elimination Impact","Crime rates and court appearance rates before and after cash bail reform by jurisdiction","CHART","usa","grouped-bar","Law & Justice","Vera Institute: Bail Reform (vera.org)",65,62,72,68,70,58,64,80),
mk("heb08","Shrinking Cities World Map","Cities that have lost 25%+ of peak population worldwide mapped with current trajectory","MAP","world","proportional-symbol","Demographics","UN: World Urbanization Prospects (population.un.org)",65,60,72,70,65,76,65,88),
mk("heb09","Working Age Population Cliff","Countries where the 15-64 age cohort is projected to shrink 20%+ by 2050","MAP","world","choropleth","Demographics","UN: World Population Prospects (population.un.org)",62,58,74,72,70,70,68,90),
mk("heb10","Mixed-Race Population Growth","Self-identified multiracial population growth by metro area over three censuses","MAP","usa","choropleth","Demographics","Census: Race Data (census.gov)",55,65,70,68,50,66,62,90),
mk("heb11","College Town Age Distortion","Counties where college students create extreme age distribution skews mapped with actual resident median age","MAP","usa","bivariate-choropleth","Demographics","Census ACS: Age by County (data.census.gov)",50,62,70,74,45,68,72,88),
mk("heb12","Demographic Tipping Points","US counties that flipped majority race/ethnicity in the last decade mapped with economic indicators","MAP","usa","choropleth","Demographics","Census: Decennial Comparison (census.gov)",62,60,70,78,68,72,70,88),
mk("heb13","Childless by Choice Geography","Percentage of women 40-44 who have never had children by metro area with trend line","MAP","usa","choropleth","Demographics","Census CPS: Fertility Data (census.gov/cps)",58,68,70,72,55,64,65,88),
mk("heb14","Disability Rate Disparities","Disability prevalence by county mapped against healthcare access and employment accommodation rates","MAP","usa","bivariate-choropleth","Demographics","Census ACS: Disability Data (census.gov)",68,65,72,60,62,68,58,88),
mk("heb15","Lebanon Economic Collapse Dashboard","Lebanese pound black market rate, bank deposit haircuts, and emigration wave over 5 years","CHART","middle-east","dual-axis","Economy & Trade","World Bank: Lebanon Economic Monitor (worldbank.org)",75,55,70,68,80,62,68,78),
mk("heb16","Qatari Migrant Worker Death Toll","Reported migrant worker deaths during World Cup infrastructure construction by nationality","CHART","middle-east","bar-chart","Labor & Work","Guardian: Qatar Worker Deaths (theguardian.com/qatar-deaths)",80,52,65,70,85,62,68,75),
mk("heb17","Middle East Nuclear Ambitions","Countries with nuclear programs, suspected programs, and US nuclear umbrella agreements in the region","MAP","middle-east","choropleth","Conflict & Security","IAEA: Country Profiles (iaea.org)",62,45,72,70,78,68,66,80),
mk("heb18","Jordanian Refugee Burden","Refugee population as percentage of total population in Jordan by governorate with service strain","MAP","middle-east","choropleth","Migration & Borders","UNHCR: Jordan Data (unhcr.org/jordan)",72,55,70,65,72,68,62,82),
mk("heb19","Omani Diversification Progress","Omans Vision 2040 progress metrics — non-oil GDP share, tourism revenue, manufacturing output","CHART","middle-east","line-chart","Economy & Trade","Oman Vision 2040 (oman2040.om)",48,42,72,68,55,58,66,78),
mk("heb20","Saudi Arabia Entertainment Revolution","New entertainment venues, concerts, and cinema screens opened in Saudi Arabia since 2018","CHART","middle-east","area-chart","Culture & Religion","GEA: Saudi Entertainment Authority (gea.gov.sa)",52,48,68,75,58,65,72,75),
mk("heb21","Middle East Air Quality Crisis","PM2.5 levels by city in the Middle East mapped against WHO guidelines and sandstorm frequency","MAP","middle-east","proportional-symbol","Health & Wellbeing","WHO: Air Quality Database (who.int/airpollution)",68,58,72,62,65,72,60,82),
mk("heb22","Firearm Trace Time-to-Crime","Average time between gun purchase and recovery at a crime scene by state","MAP","usa","choropleth","Public Safety","ATF: Trace Data (atf.gov/resource-center)",62,55,70,74,68,64,68,85),
mk("heb23","AR-15 Style Rifle Prevalence","Estimated modern sporting rifle ownership per capita by state with mass shooting frequency overlay","MAP","usa","bivariate-choropleth","Public Safety","NSSF: Firearm Production + GVA (nssf.org)",65,58,68,65,78,66,60,78),
mk("heb24","Gun Violence Survivor Medical Costs","Average lifetime medical costs for gunshot survivors by injury type and insurance status","CHART","usa","bar-chart","Health & Wellbeing","Health Affairs: Gun Injury Costs (healthaffairs.org)",75,68,70,72,72,58,62,78),
mk("heb25","Guns Seized at Airports","TSA firearm seizures at airport checkpoints by airport with loaded/unloaded breakdown","MAP","usa","proportional-symbol","Public Safety","TSA: Year in Review (tsa.gov)",52,62,68,78,58,66,72,90),
mk("heb26","Domestic Violence Homicide and Gun Access","States where domestic abusers can still legally possess firearms mapped with DV homicide rates","MAP","usa","bivariate-choropleth","Public Safety","Everytown: DV and Firearms (everytownresearch.org)",80,68,70,65,82,64,60,80),
mk("heb27","Ghost Gun State Laws Patchwork","States requiring serial numbers on ghost guns vs. no regulation mapped with recovery trends","MAP","usa","choropleth","Public Safety","Giffords: Ghost Gun Laws (giffords.org)",60,55,70,72,68,64,66,78),
mk("heb28","Shooting Range Density","Gun ranges per capita by county mapped against urban/rural classification","MAP","usa","choropleth","Culture & Religion","NSSF: Range Data + Census (nssf.org)",48,58,68,62,48,68,55,82),
mk("heb29","Warrant Backlog by City","Outstanding arrest warrants per capita by major city with average age of oldest warrant","CHART","usa","bar-chart","Law & Justice","DOJ: Warrant Data + City Reports (justice.gov)",62,60,68,74,68,58,66,75),
mk("heb30","Voter Registration Purges","Voters removed from rolls per 1000 registered by state since 2013 with reason breakdown","MAP","usa","choropleth","Demographics","Brennan Center: Voter Purge Data (brennancenter.org)",68,65,70,72,74,66,65,85),
mk("heb31","Drone Strike Locations in Yemen","US and Saudi coalition drone and airstrike locations in Yemen with civilian casualty estimates","MAP","middle-east","dot-density","Conflict & Security","Airwars: Yemen Data (airwars.org)",75,48,65,62,82,74,66,75),
mk("heb32","Twin Deficits by Country","Countries running both fiscal and current account deficits mapped with GDP growth","MAP","world","bivariate-choropleth","Demographics","IMF: WEO Database (imf.org/weo)",50,45,72,68,58,62,64,90),
mk("heb33","Egyptian Water Stress from GERD","Projected Nile water flow reduction to Egypt from Grand Ethiopian Renaissance Dam by scenario","CHART","middle-east","area-chart","Environment & Climate","MIT: Nile Basin Study (mit.edu)",68,48,70,72,78,68,72,75),
mk("heb34","Occupational Licensing Barriers","Number of occupations requiring state license by state mapped with average licensing cost and time","MAP","usa","choropleth","Law & Justice","IJ: License to Work (ij.org/report/license-to-work)",62,68,72,70,65,64,65,85),
mk("heb35","Kuwaiti Bidoon Population","Estimated stateless Bidoon population in Kuwait by governorate with citizenship denial rates","MAP","middle-east","choropleth","Human Rights","HRW: Kuwait Bidoon (hrw.org)",72,48,62,74,72,64,74,68),
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
print(f"Injected {len(new)} new ideas (HEB batch)")
