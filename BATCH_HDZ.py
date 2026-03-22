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
mk("hdz01","Paper Mill Towns Reinvention","Former paper mill towns mapped with current economic trajectory — thriving, stable, or declining","MAP","usa","dot-density","Economy & Trade","Census ACS + BLS QCEW (census.gov)",65,68,70,65,62,72,64,82),
mk("hdz02","3D Printing Manufacturing Hubs","Additive manufacturing facilities by metro area with industry specialization and job growth","MAP","usa","proportional-symbol","Technology & Data","Wohlers Associates: AM Report (wohlersassociates.com)",52,48,72,74,55,70,72,78),
mk("hdz03","OSHA Violation Repeat Offenders","Facilities with 3+ serious OSHA violations in 5 years mapped by industry and penalty amount","MAP","usa","dot-density","Labor & Work","OSHA: Inspection Data (osha.gov)",70,62,68,72,76,66,64,88),
mk("hdz04","Rare Earth Processing Bottleneck","Global rare earth element processing capacity by country showing Chinas dominance","MAP","world","proportional-symbol","Economy & Trade","USGS: Mineral Commodity Summaries (usgs.gov/minerals)",58,48,74,78,72,70,72,85),
mk("hdz05","Union Organizing Drives by Industry","NLRB union election petitions filed by industry and metro area over 5 years","MAP","usa","dot-density","Labor & Work","NLRB: Election Data (nlrb.gov)",65,68,70,62,68,66,60,88),
mk("hdz06","Shipyard Employment Collapse","US shipbuilding employment over 60 years by shipyard location mapped with Navy vessel orders","MAP","usa","dot-density","Economy & Trade","BLS: Shipbuilding Employment + CRS (bls.gov)",62,55,70,68,65,72,64,82),
mk("hdz07","Pharmaceutical Manufacturing Origins","Where Americas prescription drugs are actually manufactured by country and drug category","MAP","world","choropleth","Health & Wellbeing","FDA: Drug Import Data (fda.gov)",68,72,72,78,74,68,65,82),
mk("hdz08","Prosperity Gospel Mega-Churches","Churches preaching prosperity theology mapped by location with annual revenue estimates","MAP","usa","proportional-symbol","Culture & Religion","Hartford Institute + IRS 990 Data (hirr.hartsem.edu)",62,60,65,74,58,70,72,70),
mk("hdz09","Religious Attendance Decline Curve","Weekly worship attendance by denomination over 40 years in the US","CHART","usa","line-chart","Culture & Religion","Gallup: Religion (gallup.com/poll/1690/religion.aspx)",65,68,72,62,60,58,55,88),
mk("hdz10","Blasphemy Law Enforcement","Countries with blasphemy laws mapped by severity and recent enforcement actions","MAP","world","choropleth","Culture & Religion","USCIRF: Blasphemy Laws (uscirf.gov)",70,50,68,72,78,66,70,82),
mk("hdz11","Missionary Presence by Country","Active Christian missionaries per million population by host country with sending country origin","MAP","world","choropleth","Culture & Religion","CSGC: World Christian Database (worldchristiandatabase.org)",55,48,68,70,55,68,66,78),
mk("hdz12","Interfaith Marriage Rates","Percentage of married couples with different religious affiliations by state over 30 years","MAP","usa","choropleth","Culture & Religion","Pew: Religious Landscape (pewresearch.org/religion)",58,68,70,65,50,62,60,85),
mk("hdz13","Religious Land Use Discrimination","RLUIPA lawsuits filed by religious institution type mapped with denial-of-zoning data","MAP","usa","dot-density","Culture & Religion","DOJ: RLUIPA Report (justice.gov/crt/rluipa)",60,52,65,72,65,64,70,75),
mk("hdz14","Hajj Pilgrim Origins","Annual Hajj attendance by country of origin mapped with quota allocations","MAP","world","flow-map","Culture & Religion","Saudi Ministry of Hajj (haj.gov.sa)",50,48,72,65,45,76,62,80),
mk("hdz15","Broadway Show Profitability","Broadway productions mapped by profit/loss with run length and genre categorization","CHART","usa","scatter","Economy & Trade","Broadway League: Grosses (broadwayleague.com)",52,62,68,70,55,60,65,78),
mk("hdz16","Video Game Revenue vs. Film","Annual global revenue of gaming industry vs. film box office vs. music by year","CHART","world","area-chart","Economy & Trade","Newzoo: Global Games Market (newzoo.com)",50,65,72,70,48,58,55,88),
mk("hdz17","Drive-In Theater Comeback","Drive-in theater locations open vs. closed mapped with reopening surge during COVID","MAP","usa","dot-density","Culture & Religion","UDITOA: Drive-In Database (driveintheater.com)",55,68,62,65,48,72,62,78),
mk("hdz18","Public Library Visits vs. Movie Attendance","Annual public library visits per capita vs. movie ticket purchases per capita by state","CHART","usa","scatter","Education","IMLS: Library Data + MPAA (imls.gov)",55,72,70,72,48,60,68,88),
mk("hdz19","Concert Ticket Price Inflation","Average concert ticket price by genre adjusted for inflation over 30 years","CHART","usa","line-chart","Economy & Trade","Pollstar: Ticket Data (pollstar.com)",60,75,72,68,62,55,58,82),
mk("hdz20","True Crime Podcast Geographic Bias","Cases covered by top 50 true crime podcasts mapped vs. actual crime distribution","MAP","usa","bivariate-choropleth","Media & Information","Apple Podcasts + FBI UCR (fbi.gov/ucr)",55,68,65,78,52,70,80,72),
mk("hdz21","Theme Park Economic Zones","Employment and wage impact within 10-mile radius of Americas largest theme parks","MAP","usa","proportional-symbol","Economy & Trade","BLS QCEW + Company Reports (bls.gov)",52,62,70,65,48,72,58,80),
mk("hdz22","Autocorrect Most Changed Words","Words most frequently changed by autocorrect by language with unintended meaning shifts","CHART","world","bar-chart","Technology & Data","SwiftKey: Typing Data (support.swiftkey.com)",45,78,60,82,40,55,85,65),
mk("hdz23","Americas Most Misspelled Words by State","Most commonly misspelled word googled by state from how to spell searches","MAP","usa","choropleth","Education","Google Trends: Spelling Searches (trends.google.com)",42,80,65,78,38,68,75,82),
mk("hdz24","Potholes Per Capita","Pothole complaints filed per capita by major city with average repair time","RANK","usa","bar-chart","Infrastructure & Systems","311 Data: Pothole Complaints (data.cityofnewyork.us)",50,82,68,65,55,60,68,80),
mk("hdz25","Most Returned Christmas Gifts","Product categories with highest return rates in January by retail category and year","CHART","usa","bar-chart","Economy & Trade","NRF: Returns Survey (nrf.com)",45,78,68,70,42,55,62,78),
mk("hdz26","HOA Fines That Made the News","Viral HOA fines and lawsuits mapped by state with average fine amount","MAP","usa","dot-density","Law & Justice","CAI: HOA Data + News Archives (caionline.org)",52,78,58,80,48,60,78,65),
mk("hdz27","Worlds Most Dangerous Selfie Spots","Locations where selfie-related deaths have occurred worldwide with cause classification","MAP","world","dot-density","Health & Wellbeing","iScience: Selfie Death Study (journals.elsevier.com)",55,62,60,82,58,72,80,72),
mk("hdz28","Airport Delay Domino Effect","How a delay at one major hub cascades to other airports over 24 hours animated","MAP","usa","animated-choropleth","Transportation &tic","BTS: On-Time Performance (transtats.bts.gov)",52,72,68,70,55,78,72,88),
mk("hdz29","Roundabout Resistance Map","Cities that rejected roundabouts despite DOT recommendations mapped with crash rate comparison","MAP","usa","dot-density","Transportation &tic","FHWA: Roundabout Data (fhwa.dot.gov)",48,68,65,72,50,66,72,72),
mk("hdz30","Cheese Factory Consolidation","Number of cheese-producing facilities by county over 30 years mapped with production volume","MAP","usa","dot-density","Agriculture & Food","USDA NASS: Dairy Products (nass.usda.gov)",50,58,68,65,48,70,64,85),
mk("hdz31","EV Battery Plant Construction Race","Announced and under-construction EV battery gigafactories by country with capacity in GWh","MAP","world","proportional-symbol","Economy & Trade","Benchmark Minerals: Gigafactory Tracker (benchmarkminerals.com)",55,52,74,70,62,76,68,82),
mk("hdz32","Conspiracy Theory Belief Geography","Survey-based conspiracy belief rates by state for common theories — flat earth, moon landing, QAnon","MAP","usa","choropleth","Culture & Religion","PRRI: American Values Survey (prri.org)",55,68,62,78,58,64,72,75),
mk("hdz33","Americas Mattress Store Oversaturation","Mattress stores per capita by metro area plotted against population with saturation trends","MAP","usa","proportional-symbol","Economy & Trade","Census: CBP + Yelp (census.gov/programs-surveys/cbp)",42,72,65,80,40,62,78,78),
mk("hdz34","Garment Factory Comeback","New cut-and-sew apparel manufacturing jobs in the US by metro area with nearshoring trend","MAP","usa","dot-density","Economy & Trade","BLS QCEW: NAICS 3152 (bls.gov/cew)",55,52,70,72,58,66,68,78),
mk("hdz35","Worlds Longest Place Names","Longest official place names by country mapped with character count and pronunciation guide","MAP","world","dot-density","Culture & Religion","GeoNames: Gazetteer (geonames.org)",38,62,58,82,35,68,80,85),
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
print(f"Injected {len(new)} new ideas (HDZ batch)")
