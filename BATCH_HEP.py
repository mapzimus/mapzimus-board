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
mk("hep01","Chip Fab Water Consumption","Water usage per semiconductor fabrication plant mapped against local water stress levels","MAP","world","dot-density","Manufacturing & Industry","Intel + TSMC Sustainability Reports (tsmc.com)",55,42,70,74,68,70,70,80),
mk("hep02","Meatpacking Plant Injury Rates","Worker injury rates at meatpacking plants by company and location mapped with OSHA citation history","MAP","usa","dot-density","Manufacturing & Industry","OSHA: Establishment Search (osha.gov)",72,55,70,72,74,68,65,85),
mk("hep03","Made in America Label Fraud","FTC enforcement actions against false Made in USA claims by product category and company","CHART","usa","bar-chart","Manufacturing & Industry","FTC: Made in USA Cases (ftc.gov)",55,62,70,78,62,58,72,78),
mk("hep04","Shipyard Decline Map","Active shipbuilding yards in the US over 50 years showing industry contraction","MAP","usa","dot-density","Manufacturing & Industry","MarAd: Shipyard Database (maritime.dot.gov)",62,52,70,72,62,72,68,82),
mk("hep05","Supply Chain Nearshoring Wave","Manufacturing capacity moving from Asia to Mexico and Central America by industry sector","MAP","world","flow-map","Manufacturing & Industry","Kearney: Reshoring Index (kearney.com)",52,42,68,72,58,74,70,78),
mk("hep06","Industrial Chemical Spill Frequency","Reported industrial chemical releases by facility mapped with community health complaint rates","MAP","usa","dot-density","Manufacturing & Industry","EPA: TRI Explorer (epa.gov/tri)",68,58,68,68,72,70,62,88),
mk("hep07","Textile Mill to Brewery Pipeline","Former textile mills and factories converted to breweries and distilleries mapped with renovation timeline","MAP","usa","dot-density","Manufacturing & Industry","Brewers Association + Historic Preservation (brewersassociation.org)",42,58,70,74,38,72,75,78),
mk("hep08","Defense Contractor Employment Map","Top 10 defense contractor employee locations by facility showing economic dependence on military spending","MAP","usa","dot-density","Manufacturing & Industry","DoD: Contract Awards + Company Reports (usaspending.gov)",55,48,72,68,60,70,62,85),
mk("hep09","Paper Mill Closure Cascade","Paper mill closures over 20 years mapped with downstream effects on local recycling programs","MAP","usa","dot-density","Manufacturing & Industry","AF&PA: Industry Statistics (afandpa.org)",58,52,68,72,62,70,68,82),
mk("hep10","Prosperity Gospel Church Revenue","Churches preaching prosperity gospel mapped with pastor compensation and congregation median income","MAP","usa","dot-density","Culture & Religion","MinistryWatch + IRS 990s (ministrywatch.com)",62,58,65,76,65,66,74,72),
mk("hep11","Religious Exemption Vaccination Rates","States allowing religious exemptions for school vaccinations mapped with exemption usage rates by county","MAP","usa","choropleth","Culture & Religion","CDC: SchoolVaxView (cdc.gov/vaccines)",62,62,72,68,68,68,60,90),
mk("hep12","Conversion Therapy Ban Map","States and cities that have banned conversion therapy for minors mapped with remaining legal jurisdictions","MAP","usa","choropleth","Culture & Religion","Movement Advancement Project (lgbtmap.org)",68,55,72,62,72,68,62,88),
mk("hep13","Church Property Tax Exemption Value","Estimated property tax revenue lost to religious property tax exemptions by county","MAP","usa","choropleth","Culture & Religion","Lincoln Institute + County Assessor Data (lincolninst.edu)",52,55,70,76,58,66,72,78),
mk("hep14","Interfaith Marriage Rate by Religion","Rates of interfaith marriage by religious tradition over 50 years showing convergence","CHART","usa","line","Culture & Religion","Pew: Religious Landscape (pewresearch.org)",48,65,70,72,45,58,68,82),
mk("hep15","Satanic Temple Chapter Map","Satanic Temple chapters and activities mapped with First Amendment legal challenges filed","MAP","usa","dot-density","Culture & Religion","The Satanic Temple (thesatanictemple.com)",45,48,68,78,55,66,78,78),
mk("hep16","Religious Dietary Law Economic Impact","Market size of kosher, halal, and other religiously certified food products by metro area","CHART","usa","bar-chart","Culture & Religion","Lubicom + IFANCA Market Reports (lubicom.com)",42,55,70,72,38,58,72,78),
mk("hep17","Seminary Enrollment Collapse","Seminary and theological school enrollment trends by denomination over 20 years","CHART","usa","line","Culture & Religion","ATS: Annual Data Tables (ats.edu)",58,48,70,72,60,56,65,85),
mk("hep18","Vinyl Record Pressing Plant Bottleneck","Vinyl pressing plant locations worldwide mapped with wait times and new plant construction","MAP","world","dot-density","Entertainment & Media","RIAA + Discogs Market Data (riaa.com)",45,55,70,74,48,68,72,78),
mk("hep19","Book Desert Map","Communities with zero bookstores and no library within 10 miles mapped with literacy rates","MAP","usa","choropleth","Entertainment & Media","ABA: Bookstore Directory + IMLS (bookweb.org)",65,62,72,70,62,68,68,82),
mk("hep20","Streaming Service Password Crackdown Effect","Subscriber changes after major streaming services ended password sharing by country","CHART","world","line","Entertainment & Media","Company Earnings Reports (variety.com)",48,72,70,68,55,58,65,78),
mk("hep21","Independent Venue Survival Rate","Independent music venues that survived vs. closed post-2020 by city mapped with rent changes","MAP","usa","dot-density","Entertainment & Media","NIVA: Venue Database (nivassoc.org)",65,62,68,68,65,68,68,78),
mk("hep22","AI-Generated Content Flood","Percentage of new content on major platforms estimated to be AI-generated by platform and year","CHART","world","area-chart","Entertainment & Media","NewsGuard + Stanford HAI (hai.stanford.edu)",55,62,65,74,65,60,72,72),
mk("hep23","Podcast Graveyard","Percentage of podcasts that published fewer than 10 episodes mapped with genre and platform","CHART","world","bar-chart","Entertainment & Media","Listen Notes: Podcast Stats (listennotes.com)",42,65,70,72,42,58,72,82),
mk("hep24","Broadway Ticket Price vs. Show Length","Broadway show ticket prices plotted against runtime in minutes with genre overlay","CHART","usa","scatter","Entertainment & Media","Broadway League (broadwayleague.com)",42,62,72,68,40,58,68,82),
mk("hep25","Museum Free Day Economics","Museums offering free admission days mapped with attendance spikes and revenue impact","CHART","usa","bar-chart","Entertainment & Media","AAM: Museum Financial Survey (aam-us.org)",42,58,70,68,38,62,65,80),
mk("hep26","Sports Bar Density as Cultural Indicator","Sports bars per capita by metro mapped with local team performance and fandom intensity scores","MAP","usa","choropleth","Entertainment & Media","Yelp API + ESPN Fan Metrics (yelp.com)",40,68,68,70,38,66,70,78),
mk("hep27","States That Look Like Other Things","US states overlaid with the objects they most resemble based on shape analysis algorithm","MAP","usa","special","Humor & Weird Data","Custom Shape Analysis + Census TIGER (census.gov/tiger)",38,72,70,78,35,78,82,85),
mk("hep28","Feral Cat Colony Density","Estimated feral cat populations by city mapped with TNR program funding and bird mortality estimates","MAP","usa","dot-density","Humor & Weird Data","Alley Cat Allies + Audubon (alleycat.org)",42,58,70,72,42,68,72,78),
mk("hep29","Roomba Mapping Data Reveals Floor Plans","Average home floor plan size and layout patterns derived from robot vacuum mapping data by metro","MAP","usa","choropleth","Humor & Weird Data","iRobot + Academic Research (irobot.com)",40,68,65,82,42,62,82,65),
mk("hep30","Most Misspelled City Names","Cities whose names are most frequently misspelled in USPS mail sorted by error rate","CHART","usa","bar-chart","Humor & Weird Data","USPS: Address Quality Reports (usps.com)",38,72,72,74,35,58,78,82),
mk("hep31","Left-Handed Store Locations","Retail stores specifically catering to left-handed people mapped with left-handed population estimates","MAP","world","dot-density","Humor & Weird Data","Anything Left-Handed + Survey Data (anythinglefthanded.co.uk)",35,55,70,74,35,66,78,72),
mk("hep32","Roundabout Rage Index","Cities with the most traffic incidents at roundabouts per roundabout mapped with driver unfamiliarity scores","MAP","usa","dot-density","Humor & Weird Data","IIHS + DOT Crash Data (iihs.org)",42,72,70,74,48,68,76,78),
mk("hep33","Americas Most Stolen Garden Gnomes","Garden gnome theft reports per capita by state from police blotter data","MAP","usa","choropleth","Humor & Weird Data","Police Blotter Aggregation + NIBRS (fbi.gov/ucr)",35,62,68,80,38,66,82,65),
mk("hep34","Daylight Saving Time Complaint Volume","Volume of social media complaints about daylight saving time by state mapped with states that opted out","MAP","usa","choropleth","Humor & Weird Data","Twitter/X API + State Legislation (congress.gov)",42,78,72,68,45,64,68,82),
mk("hep35","WiFi Network Name Census","Most common WiFi network names by neighborhood type from wardriving data","CHART","usa","bar-chart","Humor & Weird Data","Wigle.net: WiFi Database (wigle.net)",38,68,68,78,38,58,80,75),
]

raw = open(DATA, 'r', encoding='utf-8').read()
existing = set(re.findall(r'id:"(hep\d+)"', raw))
new_ideas = [i for i in IDEAS if re.search(r'id:"(hep\d+)"', i).group(1) not in existing]
print(f"Injecting {len(new_ideas)} new ideas (skipping {len(IDEAS)-len(new_ideas)} dupes)")
if new_ideas:
    tail = ']; // end D'
    assert tail in raw, "Cannot find tail marker"
    raw = raw.replace(tail, ',\n'.join(new_ideas) + ',\n' + tail)
    open(DATA, 'w', encoding='utf-8').write(raw)
    print("Done")
else:
    print("Nothing to inject")
