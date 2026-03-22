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
mk("hdy01","Solitary Confinement Usage Map","Estimated prisoners in solitary confinement per 1000 incarcerated by state with duration data","MAP","usa","choropleth","Law & Justice","Solitary Watch: Exposed (solitarywatch.org)",78,58,68,72,82,64,70,75),
mk("hdy02","Police Use of Force Reporting Gaps","States with mandatory vs. voluntary police use-of-force reporting and data completeness scores","MAP","usa","choropleth","Law & Justice","FBI: Use of Force Data (fbi.gov/use-of-force)",70,62,70,68,76,66,64,78),
mk("hdy03","Eviction Filing Rates by County","Eviction cases filed per renter household by county mapped against median rent burden","MAP","usa","bivariate-choropleth","Law & Justice","Eviction Lab: National Data (evictionlab.org)",75,78,72,62,74,70,58,88),
mk("hdy04","Court Interpreter Availability","Languages available for court interpretation by federal district with unmet demand estimates","MAP","usa","choropleth","Law & Justice","DOJ: Language Access Data (justice.gov)",62,58,65,72,60,64,70,75),
mk("hdy05","Prosecutorial Declination Rates","Percentage of arrests that prosecutors decline to charge by district with racial breakdown","CHART","usa","bar-chart","Law & Justice","BJS: Prosecutors in State Courts (bjs.gov)",68,58,70,74,72,60,68,78),
mk("hdy06","Eminent Domain Abuse Hotspots","Eminent domain actions for private development since Kelo v. New London by municipality","MAP","usa","dot-density","Law & Justice","IJ: Eminent Domain Data (ij.org/eminent-domain)",65,62,68,74,72,68,72,75),
mk("hdy07","Algorithmic Bail Decisions","Jurisdictions using algorithmic risk scores for bail with false positive rates by demographic","MAP","usa","dot-density","Law & Justice","Partnership on AI: Algorithmic Risk Assessment (partnershiponai.org)",68,55,65,78,72,62,76,72),
mk("hdy08","Fertility Rate Collapse by Country","Total fertility rates by country with year they crossed below replacement level","MAP","world","choropleth","Demographics","World Bank: Fertility Rate (data.worldbank.org)",65,62,74,70,68,72,62,92),
mk("hdy09","Twin Cities Divergence","Pairs of adjacent cities that took different economic paths mapped with outcome metrics","MAP","usa","dot-density","Demographics","Census ACS + BLS (census.gov)",58,68,65,75,55,72,78,80),
mk("hdy10","Surnames as Migration Trackers","Most common surnames by county revealing historical migration and settlement patterns","MAP","usa","choropleth","Demographics","Census: Frequently Occurring Surnames (census.gov/topics/population/genealogy)",52,68,62,80,45,74,82,88),
mk("hdy11","Peak Population Cities","Cities that hit peak population decades ago mapped with current population as percentage of peak","MAP","usa","proportional-symbol","Demographics","Census: Decennial Population (census.gov)",65,68,72,70,62,74,65,90),
mk("hdy12","Last Majority-White Generation","Projected year each state becomes majority-minority based on current demographic trends","MAP","usa","choropleth","Demographics","Census: Population Projections (census.gov/projections)",62,68,70,75,72,68,70,85),
mk("hdy13","Centenarian Hotspots","Counties with the highest rates of residents aged 100+ mapped with blue zone lifestyle factors","MAP","usa","dot-density","Demographics","Census ACS: Age Data + Blue Zones (bluezones.com)",55,62,68,78,48,72,74,85),
mk("hdy14","Name Popularity Geography","Most popular baby names by state showing regional cultural clusters over decades","MAP","usa","choropleth","Demographics","SSA: Baby Names Data (ssa.gov/oact/babynames)",48,72,68,65,42,74,62,92),
mk("hdy15","Iraqi Kurdistan Autonomy Economy","GDP composition and trade flows of the Kurdistan Region of Iraq vs. federal Iraq","CHART","middle-east","bar-chart","Economy & Trade","KRG: Economic Reports (gov.krd)",52,45,68,72,62,60,70,72),
mk("hdy16","Dead Sea Shrinkage Timeline","Dead Sea surface area and water level decline over 50 years with satellite imagery dates","CHART","middle-east","area-chart","Environment & Climate","USGS + Israeli Water Authority (water.gov.il)",65,55,72,70,68,80,66,85),
mk("hdy17","Sectarian Violence Map of Iraq","Sectarian attack locations 2003-present color-coded by perpetrator group and target","MAP","middle-east","dot-density","Conflict & Security","Iraq Body Count (iraqbodycount.org)",75,50,65,60,82,74,62,78),
mk("hdy18","Gulf State Migrant Worker Demographics","Foreign-born worker population as percentage of total by Gulf country with nationality breakdown","CHART","middle-east","bar-chart","Migration & Borders","ILO: Labour Migration (ilo.org)",65,55,72,74,68,62,68,80),
mk("hdy19","Israeli Settlement Growth Timeline","Settlement population in the West Bank over 50 years mapped with Oslo Accord boundaries","MAP","middle-east","dot-density","Politics & Governance","Peace Now: Settlement Data (peacenow.org.il)",72,52,68,62,80,76,65,82),
mk("hdy20","Syrian Refugee Integration Outcomes","Syrian refugee employment, education, and language acquisition rates by host country","CHART","middle-east","grouped-bar","Migration & Borders","UNHCR + 3RP (unhcr.org)",72,58,70,65,62,60,64,78),
mk("hdy21","UAE Sovereign Wealth Investments","Abu Dhabi and Dubai sovereign wealth fund global investment portfolio mapped by sector and country","MAP","world","proportional-symbol","Economy & Trade","SWF Institute: Rankings (swfinstitute.org)",50,45,72,70,55,74,68,80),
mk("hdy22","Firearm Background Check Surge Map","NICS background checks per capita by state over time with panic-buying event markers","MAP","usa","choropleth","Public Safety","FBI: NICS Data (fbi.gov/nics)",60,65,72,68,62,66,58,92),
mk("hdy23","Ammunition Sales Tax Revenue","States that tax ammunition separately mapped with revenue collected and rate","MAP","usa","choropleth","Economy & Trade","State Revenue Departments + Giffords (giffords.org)",52,58,70,72,55,62,64,78),
mk("hdy24","Accidental Child Gun Deaths","Accidental firearm deaths among children under 14 by state per capita mapped","MAP","usa","choropleth","Public Safety","CDC WONDER: Injury Data (wonder.cdc.gov)",82,75,72,65,80,62,55,88),
mk("hdy25","Gun Show Density Map","Licensed gun shows per year per capita by state mapped with background check exemption status","MAP","usa","bivariate-choropleth","Public Safety","ATF: Gun Show Data + NCSL (atf.gov)",58,60,70,68,62,68,62,80),
mk("hdy26","Straw Purchase Prosecution Rates","Federal straw purchase prosecutions per ATF trace by district with conviction rates","CHART","usa","bar-chart","Law & Justice","ATF: Trace Data + DOJ (atf.gov/resource-center)",62,52,68,72,70,58,66,78),
mk("hdy27","Militia Group Locations","Identified militia and armed anti-government groups mapped by county with membership estimates","MAP","usa","dot-density","Public Safety","SPLC: Extremist Files (splcenter.org)",68,55,62,72,78,72,70,75),
mk("hdy28","Firearm Waiting Period Effectiveness","States with mandatory waiting periods mapped against impulse-related gun deaths per capita","MAP","usa","bivariate-choropleth","Public Safety","Gifford: Waiting Periods + CDC (giffords.org)",70,62,70,68,72,66,62,80),
mk("hdy29","Zoning Law as Segregation Tool","Single-family-only zoning percentage by municipality mapped against racial composition","MAP","usa","bivariate-choropleth","Law & Justice","Urban Institute: Zoning and Segregation (urban.org)",72,65,68,74,70,72,70,80),
mk("hdy30","Stillbirth Rate Disparities","Stillbirth rates by race and state mapped against prenatal care access","MAP","usa","bivariate-choropleth","Demographics","CDC: Fetal Death Data (cdc.gov/nchs)",78,68,72,65,75,66,62,85),
mk("hdy31","Womens Suffrage World Timeline","Year women gained voting rights by country with restrictions and conditions noted","MAP","world","choropleth","Demographics","IPU: Women in Parliament (ipu.org)",65,62,72,68,60,70,58,90),
mk("hdy32","Turkish Military Operations in Syria","Turkish military incursion zones in northern Syria mapped with civilian displacement","MAP","middle-east","special","Conflict & Security","ACLED: Turkey-Syria Data (acleddata.com)",70,48,65,62,78,76,64,75),
mk("hdy33","Gun Buyback Program Yields","Firearms collected per 1000 residents in voluntary buyback programs by city with cost per gun","CHART","usa","bar-chart","Public Safety","Police Department Records + Trace (thetrace.org)",58,62,68,70,55,60,65,72),
mk("hdy34","Marriage Age Gap by Country","Average age difference between spouses at first marriage by country with trend over time","MAP","world","choropleth","Demographics","UN: World Marriage Data (un.org/development/desa/pd)",55,62,68,72,50,66,64,88),
mk("hdy35","Bahrain Protest Suppression","Protest events and government crackdown incidents in Bahrain 2011-present mapped over time","MAP","middle-east","dot-density","Conflict & Security","ACLED: Bahrain Data (acleddata.com)",72,48,62,68,80,70,66,72),
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
print(f"Injected {len(new)} new ideas (HDY batch)")
