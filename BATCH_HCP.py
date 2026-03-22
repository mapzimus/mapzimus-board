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
mk("HCP01","The Water Wars: Who Controls the Jordan River","Water allocation from the Jordan River basin — Israel, Jordan, Syria, Palestine — and who gets what share","MAP","Middle East","Special map","middle_east","FAO: AQUASTAT Jordan River Basin (fao.org/aquastat)",78,62,72,80,85,82,75,70),
mk("HCP02","Every Border the British Drew: Colonial Boundaries vs. Ethnic Realities","Sykes-Picot borders overlaid with actual ethnic, tribal, and religious population distributions","MAP","Middle East","Special map","middle_east","Columbia University: Gulf/2000 Ethnic Maps (gulf2000.columbia.edu)",75,60,70,82,80,88,82,72),
mk("HCP03","Sectarian Mosaic: Religion by Neighborhood in Beirut, Baghdad, and Jerusalem","Block-level religious composition maps of three of the most divided cities on earth","MAP","Middle East","City map","middle_east","Columbia University: Gulf/2000 Project (gulf2000.columbia.edu)",72,58,68,80,82,90,80,65),
mk("HCP04","The Refugee Orbit: Where 14 Million Middle Eastern Refugees Actually Live","Country-by-country refugee hosting from Syria, Iraq, Yemen, Palestine — who takes them in","MAP","Middle East","World choropleth","middle_east","UNHCR: Refugee Data Finder (unhcr.org/refugee-statistics)",85,68,78,72,80,82,70,82),
mk("HCP05","Oil Revenue Per Citizen: The Gulf State Lottery","GDP per capita from petroleum across every Middle Eastern country, showing the staggering inequality","RANK","Middle East","Bar chart","middle_east","World Bank: GDP Per Capita Middle East (data.worldbank.org)",72,68,80,75,70,68,72,85),
mk("HCP06","The Youth Bulge Bomb: Median Age Across the Middle East","Median age by country — many under 25 — overlaid with unemployment rates for under-30s","MAP","Middle East","World choropleth","middle_east","UN Population Division: World Population Prospects (population.un.org)",78,65,75,78,80,78,75,80),
mk("HCP07","Desert Megaprojects: Every $1B+ Construction Project in the Gulf","Map of NEOM, The Line, Lusail, new Saudi cities — the scale of Gulf state construction","MAP","Middle East","Special map","middle_east","MEED: Gulf Construction Projects Database (meed.com/projects)",65,58,72,80,68,90,78,72),
mk("HCP08","Where Women Could Not Drive Until 2018: Gender Rights Timeline","Timeline of womens rights milestones across Middle Eastern countries — driving, voting, working, traveling","CHART","Middle East","Line chart","middle_east","World Bank: Women Business and the Law (wbl.worldbank.org)",80,72,75,78,82,70,72,78),
mk("HCP09","Nuclear Hedging: Who in the Middle East Is Closest to the Bomb","Uranium enrichment capability, reactor programs, and delivery systems by country","MAP","Middle East","Special map","middle_east","IAEA: Country Nuclear Profiles (iaea.org/programmes/country-nuclear-profiles)",72,55,70,82,90,78,75,68),
mk("HCP10","The Expat Majority: Countries Where Foreigners Outnumber Citizens","UAE, Qatar, Kuwait, Bahrain — where migrant workers are 60-90% of the population","RANK","Middle East","Bar chart","middle_east","Gulf Labour Markets: Demographic Data (gulfmigration.grc.net)",75,65,80,85,72,68,78,80),
mk("HCP11","Every US Military Base in the Middle East","Complete map of American military installations, from massive air bases to small outposts","MAP","Middle East","Special map","middle_east","Overseas Base Realignment: Base Structure Report (acq.osd.mil/eie/bsr)",70,60,75,72,78,88,68,72),
mk("HCP12","The Desalination Dependency: Where Drinking Water Comes from the Sea","Percentage of drinking water from desalination by Middle Eastern country, showing total water dependency","MAP","Middle East","World choropleth","middle_east","IDDA: Desalination Yearbook (idadesal.org)",72,62,78,80,75,78,75,75),
mk("HCP13","Sectarian Voting: How Religion Predicts Elections in Lebanon and Iraq","Correlation between religious sect and voting patterns in confessional democracies","XREF","Middle East","Scatter plot","middle_east","Carnegie Endowment: Sectarian Politics (carnegieendowment.org/regions/middle-east)",68,55,70,75,78,68,75,65),
mk("HCP14","The Proxy War Web: Who Funds Which Militia Across the Region","Network diagram of state sponsors and their proxy forces — Iran, Saudi, Turkey, UAE connections","CHART","Middle East","Special map","middle_east","CSIS: Missile Defense Project (missilethreat.csis.org)",75,55,68,80,88,82,80,65),
mk("HCP15","Arable Land Disappearing: Fertile Crescent Then vs. Now","Satellite comparison of agricultural land in Iraq, Syria, Turkey showing desertification over 50 years","MAP","Middle East","Bivariate choropleth","middle_east","NASA: MODIS Land Cover Change (lpdaac.usgs.gov)",78,60,72,80,82,85,78,72),
mk("HCP16","The Brain Drain Express: Where Educated Middle Easterners Emigrate To","Destination countries for university-educated emigrants from Iran, Lebanon, Iraq, Egypt","MAP","World","World choropleth","middle_east","OECD: International Migration Database (oecd.org/migration)",75,65,72,75,78,78,72,70),
mk("HCP17","Press Freedom in the Middle East: Journalists Killed and Jailed","Journalists imprisoned or killed per country, overlaid with press freedom index scores","MAP","Middle East","World choropleth","middle_east","CPJ: Journalists in Prison Database (cpj.org/data/imprisoned)",85,62,75,72,88,75,70,78),
mk("HCP18","The Sovereign Wealth Scoreboard: How Much the Gulf States Have Saved","Total sovereign wealth fund assets by Gulf country, compared to their GDP","RANK","Middle East","Bar chart","middle_east","SWFI: Sovereign Wealth Fund Rankings (swfinstitute.org/fund-rankings)",65,58,80,72,62,68,70,85),
mk("HCP19","Languages of the Middle East: The Dialect Map Nobody Agrees On","Linguistic diversity map showing Arabic dialects, Kurdish varieties, Persian, Hebrew, Turkish, and minority languages","MAP","Middle East","Special map","middle_east","Ethnologue: Languages of the Middle East (ethnologue.com)",62,58,68,75,60,88,80,70),
mk("HCP20","Internet Censorship Heat Map: What You Cannot Access by Country","Websites and services blocked by country — social media, news, VPN, LGBTQ content","MAP","Middle East","World choropleth","middle_east","Freedom House: Freedom on the Net (freedomhouse.org/report/freedom-net)",78,72,75,75,80,78,72,78),
mk("HCP21","The Arms Bazaar: Top Weapons Exporters to the Middle East","Arms trade flows into the region — US, Russia, France, UK, China — by dollar value and weapon type","CHART","Middle East","Bar chart","middle_east","SIPRI: Arms Transfers Database (sipri.org/databases/armstransfers)",72,58,78,72,80,70,68,82),
mk("HCP22","Israels Expanding Footprint: Settlement Growth Timeline 1967-Present","West Bank settlement population growth mapped year by year showing territorial expansion","MAP","Middle East","Animated choropleth","middle_east","Peace Now: Settlement Data (peacenow.org.il/en/settlements-watch)",80,65,72,75,88,85,72,75),
mk("HCP23","The Strait of Hormuz Chokepoint: 20% of World Oil Passes Through Here","Daily oil tanker traffic through the strait, showing global economic vulnerability to one waterway","MAP","Middle East","Line map","middle_east","EIA: World Oil Transit Chokepoints (eia.gov/international/analysis/special-topics)",72,65,80,78,82,82,72,80),
mk("HCP24","Executions Per Capita: The Middle East Leads the World","Annual execution rates per million people by country, Middle East highlighted against global comparison","RANK","Middle East","Bar chart","middle_east","Amnesty International: Death Sentences and Executions (amnesty.org/en/what-we-do/death-penalty)",82,62,78,72,85,68,68,78),
mk("HCP25","Where Atheism Is Punishable by Death: Blasphemy Laws Worldwide","Countries where apostasy or blasphemy carry death penalty or imprisonment, concentrated in MENA region","MAP","World","World choropleth","middle_east","IHEU: Freedom of Thought Report (fot.humanists.international)",80,65,78,82,85,78,72,78),
mk("HCP26","The Kafala System: Modern Labor Control in Gulf States","Countries using kafala (employer sponsorship) system for migrant workers, with reform status","MAP","Middle East","World choropleth","middle_east","ILO: Employer-Worker Relations in Gulf (ilo.org/beirut)",82,68,72,78,82,72,75,72),
mk("HCP27","Earthquake Fault Lines vs. Population Density in Turkey and Iran","Seismic hazard zones overlaid with population density — showing who lives on the most dangerous ground","MAP","Middle East","Bivariate choropleth","middle_east","USGS: Seismic Hazard Maps (earthquake.usgs.gov/hazards)",78,65,75,72,80,85,72,78),
mk("HCP28","The Literacy Revolution: Female Education Rates 1970 vs. Today","Female literacy rate transformation across Middle Eastern countries over 50 years","CHART","Middle East","Bar chart","middle_east","UNESCO: Education Statistics (uis.unesco.org)",75,68,78,75,70,70,72,82),
mk("HCP29","The Diaspora Map: Where Middle Eastern Communities Live in America","US metro areas with largest Iraqi, Iranian, Lebanese, Yemeni, and Palestinian populations","MAP","US","Dot map","middle_east","Census: American Community Survey Ancestry (data.census.gov)",72,70,75,72,65,80,70,78),
mk("HCP30","Camp Forever: Refugee Camps That Became Permanent Cities","Long-term refugee camps in Jordan, Lebanon, Gaza — some over 70 years old — mapped with population","MAP","Middle East","Dot map","middle_east","UNRWA: Camp Profiles (unrwa.org/where-we-work)",85,68,72,78,85,82,75,75),
mk("HCP31","Solar Potential vs. Solar Investment: The Middle East Paradox","Countries with highest solar irradiance but lowest renewable energy investment per capita","XREF","Middle East","Scatter plot","middle_east","IRENA: Renewable Capacity Statistics (irena.org/Statistics)",68,58,75,82,68,72,80,75),
mk("HCP32","The Sectarian Census Nobody Will Take: Estimated Religious Breakdown","Best estimates of Sunni/Shia/Christian/Druze/other populations by country — data most governments refuse to collect","MAP","Middle East","World choropleth","middle_east","Pew: Religious Composition by Country (pewresearch.org/religion)",70,58,65,80,78,80,78,60),
mk("HCP33","Cigarette Consumption Champions: Smoking Rates Across the Middle East","Daily cigarette consumption per capita by country — Lebanon and Jordan among worlds highest","RANK","Middle East","Bar chart","middle_east","WHO: Tobacco Control Country Profiles (who.int/tobacco)",68,65,78,72,65,68,68,82),
mk("HCP34","The Tourism Paradox: Ancient History vs. Tourist Arrivals","Countries with most UNESCO World Heritage sites per capita vs. actual tourism revenue","XREF","Middle East","Scatter plot","middle_east","UNWTO: Tourism Dashboard (unwto.org/tourism-data)",65,60,72,78,62,72,75,75),
mk("HCP35","Food Import Dependency: Countries That Cannot Feed Themselves","Percentage of calories imported by Middle Eastern country — some above 80%","RANK","Middle East","Bar chart","middle_east","FAO: Food Balance Sheets (fao.org/faostat/en/#data/FBS)",78,68,80,75,78,68,72,80),
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
print(f"Injected {len(new)} new ideas (HCP batch)")
