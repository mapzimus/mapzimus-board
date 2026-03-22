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
mk("hdu01","Mandatory Minimum Sentencing Map","Which states still enforce mandatory minimums for nonviolent drug offenses and how sentence lengths compare","MAP","usa","choropleth","Law & Justice","USSC: Federal Sentencing Statistics (ussc.gov/research)",62,68,72,58,70,74,60,82),
mk("hdu02","Three-Strikes Law Outcomes","Life sentences triggered by three-strikes laws vs. the severity of the third offense","CHART","usa","bar-chart","Law & Justice","Stanford: Three Strikes Project (law.stanford.edu/three-strikes-project)",68,60,70,72,75,62,65,78),
mk("hdu03","Civil Asset Forfeiture by State","Total value of property seized by police without criminal conviction per capita","MAP","usa","choropleth","Law & Justice","IJ: Policing for Profit (ij.org/report/policing-for-profit)",72,65,68,74,78,70,68,80),
mk("hdu04","Wrongful Conviction Exonerations Timeline","Cumulative DNA exonerations over time mapped against conviction year","CHART","usa","timeline","Law & Justice","Innocence Project: Exoneration Data (innocenceproject.org)",78,62,70,80,72,65,75,85),
mk("hdu05","Bail Amount vs. Income Level","Median bail set for common charges compared to defendant median income by county","CHART","usa","scatter","Law & Justice","PJI: Pretrial Data (pretrial.org)",70,75,68,65,72,60,62,76),
mk("hdu06","Public Defender Caseloads","Average cases per public defender vs. ABA recommended maximum by state","MAP","usa","choropleth","Law & Justice","NLADA: Public Defense Data (nlada.org)",65,70,72,68,74,66,60,80),
mk("hdu07","Death Penalty Cost vs. Life Imprisonment","Total taxpayer cost of capital cases vs. life-without-parole sentences by state","CHART","usa","bar-chart","Law & Justice","DPIC: Cost Data (deathpenaltyinfo.org)",60,68,75,70,65,58,62,82),
mk("hdu08","Qualified Immunity Lawsuit Outcomes","Percentage of police misconduct lawsuits dismissed due to qualified immunity by circuit","MAP","usa","choropleth","Law & Justice","Reuters: Shielded (reuters.com/investigates/special-report/usa-police-immunity)",74,60,65,76,78,68,72,75),
mk("hdu09","Juvenile Life Without Parole","States still allowing JLWOP sentences and number of juveniles currently serving them","MAP","usa","dot-density","Law & Justice","Campaign for Fair Sentencing of Youth (fairsentencingofyouth.org)",76,58,68,72,80,64,70,78),
mk("hdu10","Legal Deserts in Rural America","Counties with fewer than one lawyer per 1000 residents mapped against poverty rates","MAP","usa","bivariate-choropleth","Law & Justice","ABA: Legal Desert Map (americanbar.org)",68,72,70,74,62,76,66,80),
mk("hdu11","Census Undercount by Race","Estimated net undercount rates by racial/ethnic group across decennial censuses","CHART","usa","grouped-bar","Demographics","Census Bureau: Coverage Measurement (census.gov/coverage)",62,68,74,70,65,60,64,88),
mk("hdu12","Aging Fastest Counties","Counties where median age increased the most in the last decade vs. population change","MAP","usa","bivariate-choropleth","Demographics","Census ACS: Age by County (data.census.gov)",58,65,72,68,55,76,62,90),
mk("hdu13","Disappearing Middle Class Metro Areas","Share of households earning 67-200% of metro median income over time","CHART","usa","area-chart","Demographics","Pew: Shrinking Middle Class (pewresearch.org)",72,80,70,65,68,62,60,85),
mk("hdu14","Language Diversity Hotspots","Census tracts where 5+ languages are spoken at home mapped by metro","MAP","usa","dot-density","Demographics","Census ACS: Language Spoken at Home (data.census.gov)",55,62,68,72,48,78,70,88),
mk("hdu15","Multigenerational Household Growth","Counties where 3+ generation households grew fastest and demographic drivers","MAP","usa","proportional-symbol","Demographics","Census ACS: Household Type (data.census.gov)",60,72,68,62,50,65,58,86),
mk("hdu16","Where Americans Are Moving From and To","Net domestic migration flows between states color-coded by age cohort","MAP","usa","flow-map","Demographics","Census: State-to-State Migration (census.gov/topics/population/migration)",65,78,74,60,52,82,58,90),
mk("hdu17","Single-Person Household Surge","Growth of one-person households by metro area vs. housing unit size trends","CHART","usa","dual-axis","Demographics","Census ACS: Household Size (data.census.gov)",58,72,70,65,50,62,60,88),
mk("hdu18","Yemen War Civilian Toll","Airstrike locations mapped against civilian casualty counts and infrastructure damage","MAP","middle-east","dot-density","Conflict & Security","ACLED: Yemen Data (acleddata.com)",82,55,68,65,85,78,70,75),
mk("hdu19","Water Crisis Across MENA","Per capita renewable freshwater availability by country with 2030 projections","MAP","middle-east","choropleth","Environment & Climate","FAO: AQUASTAT (fao.org/aquastat)",70,62,75,72,78,74,68,82),
mk("hdu20","Refugee Camps of the Middle East","Major refugee camps by population size with origin country breakdown","MAP","middle-east","proportional-symbol","Migration & Borders","UNHCR: Refugee Data (unhcr.org/refugee-statistics)",78,60,72,62,76,80,65,80),
mk("hdu21","Oil Revenue vs. Diversification Index","Percentage of GDP from oil vs. economic diversification score for MENA nations","CHART","middle-east","scatter","Economy & Trade","World Bank: MENA Economic Monitor (worldbank.org)",55,58,72,68,62,60,70,85),
mk("hdu22","Press Freedom in the Middle East","Press freedom index scores mapped with journalist imprisonment counts by country","MAP","middle-east","bivariate-choropleth","Media & Information","RSF: Press Freedom Index (rsf.org)",72,55,70,68,78,65,66,82),
mk("hdu23","Iran Protest Hotspots 2017-2024","Geolocated protest events in Iran color-coded by trigger — economic, political, social","MAP","middle-east","dot-density","Politics & Governance","ACLED: Iran Protest Data (acleddata.com)",75,52,65,70,82,72,68,72),
mk("hdu24","Desalination Capacity by Country","Total desalination output vs. total water demand for water-scarce MENA nations","CHART","middle-east","bar-chart","Infrastructure & Systems","GWI: Desalination Database (globalwaterintel.com)",55,50,74,68,60,62,70,80),
mk("hdu25","Gun Ownership vs. Gun Death Rate by State","Household gun ownership rate plotted against per capita firearm deaths","CHART","usa","scatter","Public Safety","CDC WONDER + RAND: Gun Ownership (rand.org/gun-policy)",68,72,78,55,70,65,50,90),
mk("hdu26","Mass Shooting Frequency Timeline","Mass shooting events per year with rolling average and major policy change markers","CHART","usa","timeline","Public Safety","Gun Violence Archive (gunviolencearchive.org)",75,70,72,60,78,62,55,92),
mk("hdu27","Concealed Carry Permit Rates","Per capita concealed carry permits by county mapped against violent crime rates","MAP","usa","bivariate-choropleth","Public Safety","Crime Prevention Research Center (crimeresearch.org)",60,65,70,68,72,74,62,78),
mk("hdu28","School Shooting Proximity","Percentage of K-12 students attending a school within 10 miles of a prior school shooting","MAP","usa","choropleth","Education","Everytown: School Shootings (everytownresearch.org)",80,78,65,72,82,70,68,80),
mk("hdu29","Gun Store Density vs. Suicide Rate","Federally licensed firearms dealers per capita by county vs. firearm suicide rate","MAP","usa","bivariate-choropleth","Health & Wellbeing","ATF: FFL Data + CDC WONDER (atf.gov)",65,60,72,74,70,68,66,85),
mk("hdu30","Stand Your Ground Homicide Impact","Change in justifiable homicide rates before and after Stand Your Ground enactment by state","CHART","usa","slope-chart","Law & Justice","FBI UCR + RAND (rand.org/gun-policy)",70,62,68,72,76,60,68,80),
mk("hdu31","Domestic Violence and Firearms","States requiring vs. not requiring firearm surrender in domestic violence restraining orders and DV homicide rates","MAP","usa","bivariate-choropleth","Law & Justice","Giffords: Gun Law Scorecard (giffords.org)",78,72,65,68,80,62,64,78),
mk("hdu32","Ghost Gun Recovery Trends","Untraceable firearms recovered by law enforcement by metro area over time","CHART","usa","area-chart","Public Safety","ATF: Ghost Gun Trace Data (atf.gov)",62,55,68,76,72,60,74,72),
mk("hdu33","Demographic Cliff Colleges","Colleges in counties projected to lose 15%+ of 18-year-olds by 2030 mapped by enrollment trend","MAP","usa","proportional-symbol","Demographics","WICHE: Knocking at the College Door (wiche.edu)",68,72,74,70,65,72,66,82),
mk("hdu34","Stateless Populations in the Middle East","Estimated stateless persons — Bidoon, Palestinians, Kurds — by host country","MAP","middle-east","proportional-symbol","Human Rights","UNHCR: Statelessness Data (unhcr.org/statelessness)",75,52,65,78,74,68,76,70),
mk("hdu35","Red Flag Law Petitions Filed","Extreme Risk Protection Order petitions filed per capita by state since enactment","MAP","usa","choropleth","Law & Justice","Everytown: Red Flag Laws (everytownresearch.org)",64,68,72,66,70,65,60,78),
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
print(f"Injected {len(new)} new ideas (HDU batch)")
