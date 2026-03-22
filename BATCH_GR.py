"""BATCH_GR: More viral standalone ideas from underexplored angles.
Reddit-bait titles, Instagram-friendly topics, surprising data stories.
"""
import re, sys
DATA_JS = r"D:\projects\mapzimus-board\data.js"

def mk(id,title,sub,typ,geo,fmt,sect,tbl,e,r,c,s,t,v,o,dr):
    raw=e*2+r*2+c*1.25+s*1.5+t*1.5+v*2.0+o*1.5
    vs=int((raw/11.75)*(1-0.5*(1-dr/100)))
    return ('{id:"'+id+'",title:"'+title+'",sub:"'+sub+'",type:"'+typ+'",'
            'geo:"'+geo+'",fmt:"'+fmt+'",section:"'+sect+'",tbl:"'+tbl+'",'
            'sc:{emotional:'+str(e)+',relatability:'+str(r)+',clarity:'+str(c)
            +',surprise:'+str(s)+',tension:'+str(t)+',visual:'+str(v)
            +',originality:'+str(o)+',data_ready:'+str(dr)+'}'
            ',vs:'+str(vs)+',topics:[],ext:[],status:"idea",notes:""}')

ideas = []

# === REDDIT r/dataisbeautiful VIRAL BAIT ===
ideas.append(mk("gr001","Every Country the British Empire Ever Invaded","The 22 countries Britain hasnt invaded are harder to list","MAP","World","World choropleth","History","historical invasion data",78,72,72,85,72,82,78,82))
ideas.append(mk("gr002","Countries That Drive on the Left vs Right","Legacy of British colonialism in global driving standards","MAP","World","World choropleth","Transportation","driving side data",58,72,82,72,42,82,65,92))
ideas.append(mk("gr003","The Worlds Most Spoken Languages Mapped to Where Theyre Spoken","Top 20 languages overlaid on the countries where theyre official or primary","MAP","World","World choropleth","International Statistics","language data",65,78,78,65,48,82,62,88))
ideas.append(mk("gr004","Time Zones Are Absolutely Insane: A Visual Explainer","The chaos of global time zones including half-hour and 45-min offsets","MAP","World","World choropleth","Geography & Environment","time zone data",62,78,78,82,48,88,78,90))
ideas.append(mk("gr005","Countries Older Than the United States","Every nation with a founding date before 1776","MAP","World","World choropleth","History","founding dates data",68,72,75,78,55,80,72,85))
ideas.append(mk("gr006","The World Map of Internet Speeds","Average download speeds by country - the digital divide in Mbps","MAP","World","World choropleth","Science & Technology","speedtest data",70,82,78,68,58,80,58,85))
ideas.append(mk("gr007","Every Country Where Its Illegal to Be Gay","Criminal penalties for homosexuality mapped worldwide","MAP","World","World choropleth","International Statistics","ILGA data + OWID LGBT rights",88,78,72,72,90,82,68,85))
ideas.append(mk("gr008","The Most Visited Countries in the World","International tourist arrivals by country - France leads by a mile","MAP","World","World choropleth","International Statistics","UNWTO tourism data",65,78,78,65,48,82,55,85))
ideas.append(mk("gr009","Countries Where Weed Is Legal, Decriminalized, or Banned","The global patchwork of marijuana legality","MAP","World","World choropleth","International Statistics","marijuana legality data",70,82,72,68,62,80,62,88))
ideas.append(mk("gr010","The World Map of Average Height by Country","Tallest to shortest populations mapped globally","MAP","World","World choropleth","Health","NCD-RisC height data",62,82,78,72,42,80,65,85))
ideas.append(mk("gr011","Every Countries Favorite Sport by Popularity","The dominant sport in each country: football, cricket, baseball, hockey","MAP","World","World choropleth","Sports & Recreation","sports popularity data",65,82,78,68,48,82,62,82))
ideas.append(mk("gr012","The World Map of Beer vs Wine vs Spirits","Which type of alcohol each country prefers","MAP","World","World choropleth","Food & Nutrition","fivethirtyeight drinks",65,80,78,70,48,82,62,92))
ideas.append(mk("gr013","Countries That Use the Metric System (All of Them Except Three)","The U.S., Myanmar, and Liberia still holdout on metric","MAP","World","World choropleth","International Statistics","metric system data",62,78,82,78,45,80,72,92))
ideas.append(mk("gr014","Nuclear Weapons by Country: Who Has the Bomb?","Estimated nuclear warhead counts by nation","MAP","World","World choropleth","International Statistics","SIPRI nuclear data",82,72,72,72,88,80,65,85))
ideas.append(mk("gr015","The Longest Land Borders in the World","Top 20 international borders by length","MAP","World","Line map","Geography & Environment","border length data",55,65,78,68,42,85,68,88))

# === INSTAGRAM-FRIENDLY U.S. MAPS ===
ideas.append(mk("gr016","Most Googled Thing in Each State","Top unique Google search term by state for the past year","MAP","US-State","State choropleth","Science & Technology","Google Trends data",68,88,72,82,55,78,78,78))
ideas.append(mk("gr017","Americas Favorite Fast Food Chain by State","The #1 fast food restaurant in each state by number of locations","MAP","US-State","State choropleth","Food & Nutrition","restaurant location data",62,90,78,72,45,78,62,82))
ideas.append(mk("gr018","The Most Common Last Name in Every State","Dominant surnames mapped across America","MAP","US-State","State choropleth","Demographics","Census surname data",60,85,78,72,42,78,68,85))
ideas.append(mk("gr019","Each States Highest Paid Public Employee (Its Usually a Coach)","The top-earning state employee in all 50 states","MAP","US-State","State choropleth","Economy","public salary data",72,85,78,82,62,78,72,82))
ideas.append(mk("gr020","Americas Most Dangerous Animals by State","The animal that kills the most people in each state","MAP","US-State","State choropleth","Geography & Environment","CDC/wildlife fatality data",72,82,75,80,65,78,78,78))
ideas.append(mk("gr021","Daylight Hours by State on the Longest and Shortest Days","Hours of sunlight on solstices visualized by latitude","MAP","US-State","State choropleth","Geography & Environment","astronomical data",55,72,78,62,42,82,65,92))
ideas.append(mk("gr022","Americas Most Common Street Names Mapped","Main Street, Second Street, Oak Street - which wins?","MAP","US","Dot map","Geography & Environment","Census TIGER road data",55,78,75,68,42,78,68,85))
ideas.append(mk("gr023","Average Commute Time by State: Who Sits in Traffic Longest","Mean travel time to work by state","MAP","US-State","State choropleth","Transportation","Census commuting data",68,92,80,62,58,78,55,88))
ideas.append(mk("gr024","States That Give the Most to Charity vs States That Take the Most","Charitable giving per capita vs federal aid received per capita","XREF","US-State","Bivariate choropleth","Economy","IRS data + federal spending",78,82,72,80,72,80,75,82))
ideas.append(mk("gr025","The Most Common Cause of Death in Each State (Besides Heart Disease)","After removing #1 and #2, what kills people in your state?","MAP","US-State","State choropleth","Health","CDC WONDER data",78,85,72,82,75,78,72,82))

# === GLOBAL COMPARISONS & RANKINGS ===
ideas.append(mk("gr026","Countries by Number of UNESCO World Heritage Sites","Cultural and natural heritage site counts mapped globally","MAP","World","World choropleth","International Statistics","UNESCO data",62,72,78,62,48,82,60,90))
ideas.append(mk("gr027","The Worlds Busiest Airports Mapped","Top 100 airports by passenger volume with connections","MAP","World","Dot map","Transportation","ACI airport data",62,75,78,62,48,85,58,85))
ideas.append(mk("gr028","The Happiest Countries in the World","World Happiness Report scores mapped globally","MAP","World","World choropleth","International Statistics","WHR data",75,82,78,65,58,82,58,88))
ideas.append(mk("gr029","Countries by Press Freedom Index","Where journalism is free, partly free, or not free at all","MAP","World","World choropleth","International Statistics","RSF press freedom data",78,72,72,68,80,80,65,88))
ideas.append(mk("gr030","The Worlds Most Expensive Cities to Live In","Cost of living index mapped for major world cities","MAP","World","Dot map","Economy","Mercer/EIU cost of living",72,85,78,68,62,80,58,85))

# === NATURE / GEOGRAPHY ===
ideas.append(mk("gr031","Earthquake Risk: Where the Ground Shakes Most","Seismic hazard zones mapped globally","MAP","World","World choropleth","Geography & Environment","USGS seismic hazard data",78,78,72,68,78,85,62,85))
ideas.append(mk("gr032","The World Map of Average Annual Rainfall","Precipitation patterns from desert to rainforest","MAP","World","World choropleth","Geography & Environment","WorldClim precipitation data",58,68,78,62,48,88,58,88))
ideas.append(mk("gr033","Light Pollution: Where You Can Still See the Stars","Satellite light pollution data mapped globally","MAP","World","Dot map","Geography & Environment","VIIRS nighttime lights",72,80,72,72,58,90,72,85))
ideas.append(mk("gr034","The Deepest Points in Every Ocean","Bathymetric map of ocean trenches and deep sea features","MAP","World","Special map","Geography & Environment","GEBCO bathymetry",62,68,75,72,55,90,75,82))
ideas.append(mk("gr035","Americas National Parks: Size Comparison","All 63 national parks scaled to show relative size","MAP","US","Special map","Geography & Environment","NPS area data",65,78,78,65,48,88,65,90))

# === HISTORY / INTERESTING ===
ideas.append(mk("gr036","The Age of Every Democracy on Earth","Years since each countrys current democratic constitution was adopted","MAP","World","World choropleth","History","democracy founding dates",68,68,72,72,62,80,72,82))
ideas.append(mk("gr037","Countries That Have Sent Humans to Space","Only 3 countries have independently launched humans into orbit","MAP","World","World choropleth","Science & Technology","space agency data",65,68,75,72,58,80,68,88))
ideas.append(mk("gr038","The Silk Road: Ancient Trade Routes Overlaid on Modern Borders","Historical trade network mapped onto contemporary political geography","MAP","World","Line map","History","historical trade route data",68,68,72,78,58,88,82,72))
ideas.append(mk("gr039","Every Empire at Its Largest Extent","Overlay of historical empires at peak territory on modern world map","MAP","World","Special map","History","historical empire data",72,72,70,78,65,88,78,72))
ideas.append(mk("gr040","The Worlds Oldest Companies Still Operating","Companies founded before 1700 that are still in business","MAP","World","Dot map","History","oldest companies data",65,72,72,82,55,78,82,78))

# === ECONOMICS / PERSONAL FINANCE ===
ideas.append(mk("gr041","How Long You Have to Work to Buy a Big Mac in Every Country","The Big Mac Index expressed as minutes of minimum wage labor","MAP","World","World choropleth","Economy","Big Mac Index + minimum wage",82,92,82,78,68,80,78,82))
ideas.append(mk("gr042","The Rent Is Too Damn High: Rent as % of Income by Metro","Rent burden mapped for Americas 100 largest metro areas","MAP","US-Metro","Dot map","Housing","Census rent + income data",82,92,78,68,78,80,58,85))
ideas.append(mk("gr043","Americas Dollar Store Desert: Where Discount Chains Dominate","Dollar General/Dollar Tree locations per capita by county","MAP","US-County","County choropleth","Economy","business location data",72,82,72,72,65,80,72,78))
ideas.append(mk("gr044","What $100 Buys You in Each State","Purchasing power adjusted for regional price parities","MAP","US-State","State choropleth","Economy","BEA regional price parities",72,92,82,68,58,78,62,90))
ideas.append(mk("gr045","The Tipping Point: Where $15/hr Minimum Wage Is Actually Livable","$15/hr vs cost of living by metro area - where its enough vs where its not","MAP","US-Metro","Dot map","Economy","BLS wage + cost of living data",80,92,78,72,72,78,68,82))

# === SOCIAL MEDIA / CULTURE DATA ===
ideas.append(mk("gr046","Most Popular Social Media Platform by Country","Facebook vs Instagram vs TikTok vs WeChat dominance map","MAP","World","World choropleth","Science & Technology","social media usage data",68,82,78,68,55,80,62,82))
ideas.append(mk("gr047","Netflix vs Disney+ vs Amazon Prime: Streaming Wars by Country","Market share of major streaming platforms mapped globally","MAP","World","World choropleth","Entertainment","streaming market data",65,82,75,68,58,78,62,78))
ideas.append(mk("gr048","The Video Game Map: Most Popular Game Genre by Country","FPS, RPG, MOBA, Sports - gaming preferences by nation","MAP","World","World choropleth","Entertainment","gaming market data",62,78,72,68,48,78,68,75))

# === CLIMATE SPECIFICS ===
ideas.append(mk("gr049","The 100-Degree Day Map: Heat Extremes Across America","Number of days per year exceeding 100F by county","MAP","US-County","County choropleth","Climate","NOAA temperature data",72,82,78,68,72,82,62,85))
ideas.append(mk("gr050","Americas Tornado Alley vs Tornado Reality","Traditional Tornado Alley boundaries vs actual tornado frequency by county","MAP","US-County","County choropleth","Climate","NOAA storm data",72,78,78,78,72,82,72,88))

print(f"BATCH_GR: {len(ideas)} ideas generated")

# === INJECTION LOGIC ===
with open(DATA_JS, encoding="utf-8") as f:
    raw = f.read()
existing_ids = set(re.findall(r'id:"([^"]+)"', raw))
new_ideas = []
skipped = 0
for idea in ideas:
    m = re.search(r'id:"([^"]+)"', idea)
    if m and m.group(1) not in existing_ids:
        new_ideas.append(idea)
    else:
        skipped += 1
tail = "]; // end D"
if tail not in raw:
    print("[BATCH_GR] ERROR: tail marker not found"); sys.exit(1)
raw = raw.replace(tail, "")
for idea in new_ideas:
    raw += idea + ",\n"
raw += tail + "\n"
with open(DATA_JS, "w", encoding="utf-8") as f:
    f.write(raw)
print(f"[BATCH_GR] Injected {len(new_ideas)} new ideas (skipped {skipped} dupes)")
