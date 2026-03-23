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
mk("hel01","Reshoring Index by Industry","Manufacturing jobs moved back to the US from overseas by industry sector and destination state","MAP","usa","choropleth","Manufacturing & Industry","Reshoring Initiative: Data Report (reshorenow.org)",55,58,72,72,55,68,68,82),
mk("hel02","Semiconductor Fab Construction Race","New semiconductor fabrication plants under construction worldwide mapped with capacity and completion date","MAP","world","dot-density","Manufacturing & Industry","SEMI: World Fab Forecast (semi.org)",55,42,72,72,62,74,68,85),
mk("hel03","Auto Parts Supply Chain Vulnerability","Single points of failure in the US automotive supply chain where one factory supplies 70%+ of a critical part","MAP","world","flow-map","Manufacturing & Industry","IHS Markit: Automotive Supply (ihsmarkit.com)",58,48,65,78,72,72,74,72),
mk("hel04","Factory Floor Robot Density","Industrial robots per 10k manufacturing workers by country over 10 years","CHART","world","line","Manufacturing & Industry","IFR: World Robotics Report (ifr.org)",52,48,72,70,58,68,65,88),
mk("hel05","Steel Mill Ghost Towns","Former steel-producing cities mapped with current employment rate and median income vs. peak","MAP","usa","dot-density","Manufacturing & Industry","BLS + Census ACS (bls.gov)",72,68,68,68,68,70,62,85),
mk("hel06","3D Printing Patent Cliff","3D printing patents expiring each year mapped with new consumer product categories enabled","CHART","world","area-chart","Manufacturing & Industry","USPTO + EPO Patent Data (uspto.gov)",42,38,65,72,42,58,72,78),
mk("hel07","PFAS Forever Chemical Factory Proximity","PFAS manufacturing and processing facilities mapped with drinking water contamination detections within 10 miles","MAP","usa","dot-density","Manufacturing & Industry","EPA: PFAS Analytic Tools (epa.gov/pfas)",72,65,68,72,78,72,65,85),
mk("hel08","Rare Earth Processing Chokepoints","Global rare earth element processing capacity by country showing Chinas dominance vs. new facilities","MAP","world","choropleth","Manufacturing & Industry","USGS: Mineral Commodity Summaries (usgs.gov)",55,40,70,74,70,70,68,88),
mk("hel09","EV Battery Gigafactory Map","Electric vehicle battery manufacturing plants announced vs. under construction vs. operational worldwide","MAP","world","dot-density","Manufacturing & Industry","Benchmark Minerals: Gigafactory Tracker (benchmarkminerals.com)",52,45,74,68,58,74,65,88),
mk("hel10","Megachurch Revenue Empires","Megachurches with over 10k weekly attendance mapped with estimated annual revenue and tax-exempt property value","MAP","usa","dot-density","Culture & Religion","Hartford Institute + IRS Form 990 (hirr.hartsem.edu)",62,58,68,74,65,68,72,78),
mk("hel11","Exorcism Demand Surge","Catholic dioceses reporting increased demand for exorcism services mapped with training program locations","MAP","world","dot-density","Culture & Religion","Vatican + Diocese Reports (vatican.va)",55,48,62,82,58,62,80,65),
mk("hel12","Religious None Belt","Counties where religiously unaffiliated population exceeds 50% mapped with generational shift rates","MAP","usa","choropleth","Culture & Religion","PRRI: American Values Atlas (prri.org)",58,65,72,72,52,68,68,88),
mk("hel13","Mosque Construction Opposition Map","Proposed mosque construction projects that faced organized opposition mapped with legal outcomes","MAP","usa","dot-density","Culture & Religion","ACLU + DOJ Religious Land Use Cases (aclu.org)",68,52,68,72,74,66,70,78),
mk("hel14","Tithe as Percentage of Income by Denomination","Average charitable giving as share of household income by religious denomination","CHART","usa","bar-chart","Culture & Religion","Giving USA + Denominational Reports (givingusa.org)",52,62,70,72,48,58,68,82),
mk("hel15","Religious Switching Sankey","Flow diagram showing which religions Americans are leaving and joining by generation","CHART","usa","special","Culture & Religion","Pew: Religious Landscape Study (pewresearch.org)",62,68,68,72,58,72,72,85),
mk("hel16","Faith Healing Death Map","Child deaths attributed to faith healing exemptions by state mapped with religious exemption laws","MAP","usa","dot-density","Culture & Religion","CHILD Inc. + State Death Records (childrenshealthcare.org)",78,52,68,74,82,66,72,72),
mk("hel17","Pilgrimage Route Economics","Major global pilgrimage routes mapped with annual pilgrim counts and local economic impact","MAP","world","line-map","Culture & Religion","UNWTO: Religious Tourism (unwto.org)",52,50,70,68,42,76,68,78),
mk("hel18","Sunday School Enrollment Collapse","Sunday school enrollment decline by denomination over 30 years mapped with church closure rates","CHART","usa","line","Culture & Religion","Denominational Yearbooks + ARDA (thearda.com)",62,62,70,70,62,58,65,82),
mk("hel19","Movie Theater Deserts","Counties with zero movie theaters mapped with nearest theater distance and streaming subscription rates","MAP","usa","choropleth","Entertainment & Media","NATO: Theater Count + Census (natoonline.org)",58,68,72,68,52,68,68,82),
mk("hel20","K-Pop World Domination Timeline","K-pop artist chart performance across 40 countries over 15 years showing genre spread","MAP","world","animated-choropleth","Entertainment & Media","Spotify Charts + Billboard (spotify.com/charts)",55,55,68,68,42,72,68,80),
mk("hel21","True Crime Podcast Density","True crime podcast listeners per capita by metro area mapped with actual violent crime rates","MAP","usa","bivariate-choropleth","Entertainment & Media","Edison Research + FBI UCR (edisonresearch.com)",52,68,70,74,52,64,74,75),
mk("hel22","Theme Park Wait Time Economics","Average ride wait times at major theme parks vs. ticket price inflation over 20 years","CHART","usa","dual-axis","Entertainment & Media","Theme Park Insider + TouringPlans (touringplans.com)",52,72,72,68,55,62,65,78),
mk("hel23","Local News Desert Expansion","Counties that lost their last local newspaper mapped with year of closure and replacement coverage","MAP","usa","choropleth","Entertainment & Media","UNC: News Deserts Project (usnewsdeserts.com)",70,68,72,72,68,68,68,88),
mk("hel24","Video Game Revenue vs. Hollywood","Annual revenue of the gaming industry compared to box office plus streaming by year","CHART","world","area-chart","Entertainment & Media","Newzoo + MPAA (newzoo.com)",48,62,72,72,48,62,62,85),
mk("hel25","Concert Ticket Price Inflation","Average concert ticket prices by genre over 20 years adjusted for inflation","CHART","usa","line","Entertainment & Media","Pollstar: Boxoffice Data (pollstar.com)",55,75,72,68,62,58,60,85),
mk("hel26","Drive-In Theater Survivors","Remaining drive-in movie theaters in the US mapped with opening decade and screen count","MAP","usa","dot-density","Entertainment & Media","UDITOA: Drive-In Database (driveinmovie.com)",55,65,72,70,45,72,68,85),
mk("hel27","Americas Worst Intersection Names","Intersections with the most absurd street name combinations mapped across the US","MAP","usa","dot-density","Humor & Weird Data","OpenStreetMap + TIGER/Line (openstreetmap.org)",42,72,74,78,35,68,82,85),
mk("hel28","Most Complained About Airplane Seats","Specific seat numbers with the most passenger complaints by aircraft type","CHART","usa","bar-chart","Humor & Weird Data","SeatGuru + DOT Complaints (seatguru.com)",45,78,72,72,48,62,72,72),
mk("hel29","Town Name Doppelgangers","Pairs of identically named towns in different states mapped with how different they actually are","MAP","usa","line-map","Humor & Weird Data","Census: Place Names (census.gov)",40,65,70,72,35,72,78,90),
mk("hel30","HOA Fine Hall of Shame","Most absurd HOA fines by state compiled from court records and news reports","CHART","usa","bar-chart","Humor & Weird Data","Court Records + CAI Reports (caionline.org)",52,78,68,80,55,58,78,68),
mk("hel31","Americas Longest Traffic Lights","Intersections with the longest red light duration by city mapped with driver complaint reports","MAP","usa","dot-density","Humor & Weird Data","DOT Signal Timing + Google Traffic (transportation.gov)",42,75,72,72,45,66,74,78),
mk("hel32","Bigfoot Sighting Density vs. Bar Density","Bigfoot sighting reports per county mapped against bars and breweries per capita","MAP","usa","bivariate-choropleth","Humor & Weird Data","BFRO: Sighting Database (bfro.net)",38,62,68,78,35,70,82,88),
mk("hel33","State Bird Popularity Contest","How popular each states official state bird actually is based on eBird sighting enthusiasm scores","CHART","usa","bar-chart","Humor & Weird Data","eBird + State Legislature Records (ebird.org)",40,62,72,72,35,68,75,85),
mk("hel34","Pizza Delivery Radius as a Measure of Remoteness","Furthest delivery radius of major pizza chains as a proxy for how remote an area is","MAP","usa","choropleth","Humor & Weird Data","Chain Delivery APIs + Census (dominos.com)",42,72,70,78,38,72,82,75),
mk("hel35","Worlds Most Passive-Aggressive Yelp Reviews by City","Cities with the highest rate of one-star reviews containing the phrase 'I guess' mapped with politeness indexes","MAP","usa","choropleth","Humor & Weird Data","Yelp Academic Dataset (yelp.com/dataset)",40,72,65,78,42,58,82,72),
]

raw = open(DATA, 'r', encoding='utf-8').read()
existing = set(re.findall(r'id:"(hel\d+)"', raw))
new_ideas = [i for i in IDEAS if re.search(r'id:"(hel\d+)"', i).group(1) not in existing]
print(f"Injecting {len(new_ideas)} new ideas (skipping {len(IDEAS)-len(new_ideas)} dupes)")
if new_ideas:
    tail = ']; // end D'
    assert tail in raw, "Cannot find tail marker"
    raw = raw.replace(tail, ',\n'.join(new_ideas) + ',\n' + tail)
    open(DATA, 'w', encoding='utf-8').write(raw)
    print("Done")
else:
    print("Nothing to inject")
