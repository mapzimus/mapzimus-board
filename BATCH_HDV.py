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
mk("hdv01","Factory Closure Ripple Effects","Job losses in surrounding businesses after a major factory closes mapped over 5 years","MAP","usa","dot-density","Economy & Trade","BLS: QCEW (bls.gov/cew)",72,70,68,65,74,72,62,80),
mk("hdv02","Reshoring vs. Offshoring Tracker","Manufacturing jobs moved back to the US vs. moved overseas by industry per year","CHART","usa","bar-chart","Economy & Trade","Reshoring Initiative (reshoringnow.org)",60,65,72,70,68,58,66,78),
mk("hdv03","Semiconductor Fab Locations","Current and planned chip fabrication facilities mapped with investment amounts","MAP","world","proportional-symbol","Technology & Data","SIA: Semiconductor Data (semiconductors.org)",55,52,74,72,60,78,70,82),
mk("hdv04","Auto Plant Employment Shift","EV assembly plants vs. closing ICE plants mapped with job count changes","MAP","usa","dot-density","Economy & Trade","BLS + Company Filings (bls.gov)",68,72,70,74,72,76,68,78),
mk("hdv05","Steel Mill Towns Then and Now","Population and median income change in steel-producing counties from 1970 to today","MAP","usa","bivariate-choropleth","Economy & Trade","Census: Longitudinal Data (census.gov)",75,72,68,62,70,74,60,85),
mk("hdv06","Defense Manufacturing Dependency","Counties where defense contracts represent 20%+ of manufacturing employment","MAP","usa","choropleth","Economy & Trade","USAspending: Contract Data (usaspending.gov)",58,55,72,70,65,68,66,85),
mk("hdv07","Meatpacking Plant Injury Rates","OSHA-reported injury rates at meatpacking facilities mapped by location and company","MAP","usa","dot-density","Labor & Work","OSHA: Inspection Data (osha.gov)",72,65,68,70,76,66,64,80),
mk("hdv08","Religious Switching in America","Net gains and losses between denominations over 20 years as a Sankey diagram","CHART","usa","flow-map","Culture & Religion","Pew: Religious Landscape (pewresearch.org/religion)",62,68,70,72,55,65,68,85),
mk("hdv09","Megachurch Growth Map","Congregations with 2000+ weekly attendance mapped by metro area with growth rate","MAP","usa","proportional-symbol","Culture & Religion","Hartford Institute: Megachurch Database (hirr.hartsem.edu)",58,62,68,70,52,72,64,82),
mk("hdv10","Religious Exemption Laws","States with religious exemptions for vaccination, medical care, and anti-discrimination laws","MAP","usa","choropleth","Culture & Religion","NCSL: Religious Exemption Statutes (ncsl.org)",65,60,72,68,70,62,66,85),
mk("hdv11","Mosque Construction Controversies","Proposed mosque sites that faced organized opposition mapped with outcome","MAP","usa","dot-density","Culture & Religion","ACLU: Mosque Opposition Data (aclu.org)",72,55,62,68,76,70,72,70),
mk("hdv12","Seminary Enrollment Decline","Total seminary students by denomination over 30 years vs. clergy retirement projections","CHART","usa","area-chart","Culture & Religion","ATS: Enrollment Data (ats.edu)",55,52,70,72,60,58,68,85),
mk("hdv13","Exorcism Demand by Country","Countries where the Catholic Church has expanded exorcism training programs with demand data","MAP","world","choropleth","Culture & Religion","IAEA: International Association of Exorcists (vaticannews.va)",50,48,58,82,55,60,85,55),
mk("hdv14","Streaming Platform Content Wars","Total original titles released per year by streaming service vs. subscriber growth","CHART","world","area-chart","Media & Information","Ampere Analysis: Streaming Data (ampereanalysis.com)",55,72,70,62,58,60,55,80),
mk("hdv15","Movie Theater Closures","Permanent theater closures since 2019 mapped against population density and streaming adoption","MAP","usa","dot-density","Media & Information","NATO: Theater Count Data (natoonline.org)",62,68,70,65,60,72,58,78),
mk("hdv16","Music Festival Economic Impact","Revenue generated and local economic impact per major music festival mapped by location","MAP","usa","proportional-symbol","Economy & Trade","Pollstar: Festival Data (pollstar.com)",52,65,68,58,45,74,55,75),
mk("hdv17","K-Pop Global Fan Map","Google search interest in K-pop by country over time with album sales overlay","MAP","world","choropleth","Culture & Religion","Google Trends + IFPI (ifpi.org)",48,60,65,62,40,68,58,80),
mk("hdv18","Stand-Up Comedy Boom Cities","Per capita comedy club count and open mic nights by metro area with growth trend","MAP","usa","proportional-symbol","Culture & Religion","Comedy Bureau + Yelp Data (yelp.com/dataset)",50,65,62,60,42,68,64,70),
mk("hdv19","Late Night TV Political Lean","Sentiment analysis of political jokes by late night host over election cycles","CHART","usa","line-chart","Media & Information","GDELT: Television Data (gdeltproject.org)",58,68,65,70,62,55,72,72),
mk("hdv20","Satirical News Trust Problem","Percentage of adults who mistook satirical headlines for real news by age and education","CHART","usa","grouped-bar","Media & Information","Pew: News Knowledge Survey (pewresearch.org)",62,72,68,74,55,58,70,78),
mk("hdv21","Meme Stock Geographic Clusters","ZIP codes with highest retail trading volume during meme stock events mapped","MAP","usa","dot-density","Economy & Trade","SEC: Retail Trading Data (sec.gov)",55,65,62,74,58,68,76,68),
mk("hdv22","Olympic Medal Efficiency","Medals per million population and per billion GDP by country across Summer Olympics","RANK","world","scatter","Sports & Recreation","IOC: Medal Database (olympics.com)",52,60,74,72,48,62,70,90),
mk("hdv23","Youth Sports Participation Decline","Percentage of teens playing organized sports by sport over 20 years","CHART","usa","line-chart","Sports & Recreation","Aspen Institute: State of Play (aspenprojectplay.org)",65,75,72,62,60,58,55,85),
mk("hdv24","Stadium Subsidy Scorecard","Public dollars spent on professional sports stadiums vs. promised economic returns by city","CHART","usa","bar-chart","Economy & Trade","Brookings: Stadium Finance (brookings.edu)",68,72,74,70,72,65,62,82),
mk("hdv25","CTE Diagnosis Map","Posthumous CTE diagnoses in former athletes by sport mapped against career length","MAP","usa","dot-density","Health & Wellbeing","BU CTE Center: Brain Bank Data (bu.edu/cte)",75,65,68,72,70,66,68,78),
mk("hdv26","Sports Betting Revenue by State","Legal sports betting handle and tax revenue per capita since legalization","MAP","usa","choropleth","Economy & Trade","AGA: State Gaming Data (americangaming.org)",55,68,74,62,58,66,58,88),
mk("hdv27","Equal Pay in Professional Sports","Prize money and salary ratios between mens and womens equivalents by sport","CHART","world","grouped-bar","Gender & Equity","Forbes: Sports Salary Data (forbes.com)",72,68,70,65,68,58,60,80),
mk("hdv28","Humor Style Map of America","Most popular comedy genres — stand-up, improv, sketch — by metro area ticket sales","MAP","usa","choropleth","Culture & Religion","Eventbrite: Comedy Events (eventbrite.com)",48,62,58,65,40,66,68,65),
mk("hdv29","Florida Man Index","Bizarre crime report frequency per capita by Florida county with headline samples","MAP","usa","choropleth","Public Safety","FDLE: Uniform Crime Reports (fdle.state.fl.us)",45,72,60,80,42,62,82,70),
mk("hdv30","Most Complained About Sounds","Top noise complaints by city — leaf blowers, car alarms, roosters, construction — mapped","MAP","usa","dot-density","Culture & Religion","311 Data: Noise Complaints (data.cityofnewyork.us)",48,75,62,68,40,64,72,78),
mk("hdv31","Americas Pettiest Lawsuits","Viral frivolous lawsuits mapped by state with outcome and amount sought","MAP","usa","dot-density","Law & Justice","PACER: Court Records (pacer.uscourts.gov)",50,72,58,80,45,60,78,65),
mk("hdv32","Worlds Deadliest Animals Misconception","Actual deaths caused by animal type vs. public fear ranking by country","CHART","world","bar-chart","Health & Wellbeing","WHO: Animal-Related Mortality (who.int)",55,68,72,82,48,65,78,80),
mk("hdv33","Robot Density in Manufacturing","Industrial robots per 10,000 manufacturing workers by country with 5-year trend","MAP","world","choropleth","Technology & Data","IFR: World Robotics (ifr.org)",52,55,74,70,62,72,68,88),
mk("hdv34","Textile Mill to Brewery Pipeline","Former textile and manufacturing towns that now have craft breweries mapped","MAP","usa","dot-density","Economy & Trade","Brewers Association + Census (brewersassociation.org)",50,65,62,72,42,70,74,75),
mk("hdv35","Esports Earnings by Country","Total competitive gaming prize money earned per capita by country","MAP","world","choropleth","Technology & Data","Esports Earnings (esportsearnings.com)",48,58,70,68,45,64,66,82),
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
print(f"Injected {len(new)} new ideas (HDV batch)")
