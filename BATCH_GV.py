"""BATCH_GV: More Reddit/Instagram viral ideas + region-specific deep dives.
Targeting underserved sections and high-virality potential formats.
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

# === "TIL" / SURPRISING FACT MAPS ===
ideas.append(mk("gv001","There Are More Tigers in Texas Than in the Wild","Exotic animal ownership in the U.S. vs wild population worldwide","MAP","World","Special map","Geography & Environment","exotic animal data",72,78,68,92,58,78,88,72))
ideas.append(mk("gv002","The Nearest Country to Every Point on Earth","Voronoi diagram showing which country is closest from any ocean point","MAP","World","Special map","Geography & Environment","geographic distance calculations",55,62,72,78,42,90,85,82))
ideas.append(mk("gv003","Americas Billion-Dollar Weather Disasters Since 1980","Every weather event costing $1B+ mapped by location and type","MAP","US","Dot map","Climate","NOAA billion-dollar disasters",82,82,75,72,80,85,65,90))
ideas.append(mk("gv004","Countries Where More People Speak English Than England","Non-native English speakers exceed the UKs population in many nations","MAP","World","World choropleth","International Statistics","English speaker data",62,72,72,85,48,80,78,82))
ideas.append(mk("gv005","Half the World Lives in This Circle","The famous population concentration circle over Asia drawn with real data","MAP","World","Special map","Population","OWID population + geographic data",72,78,75,82,58,85,78,90))
ideas.append(mk("gv006","Pangea with Modern Political Borders","If continents were still joined, what would the world map look like?","MAP","World","Special map","Geography & Environment","plate tectonics + modern borders",62,68,68,88,48,92,90,72))
ideas.append(mk("gv007","Every River That Flows Into the Mississippi","The complete Mississippi watershed drainage basin mapped","MAP","US","Line map","Geography & Environment","USGS NHD hydrography",62,68,75,72,48,92,72,88))
ideas.append(mk("gv008","Whats on the Exact Opposite Side of Earth From You?","Antipodal map: what country is directly through the Earths core","MAP","World","Special map","Geography & Environment","antipodal calculations",55,72,72,85,42,85,85,88))

# === ECONOMY VIRAL ===
ideas.append(mk("gv009","Californias Economy Is Bigger Than Most Countries","If California were a country, itd be the 5th largest economy","MAP","World","Special map","Economy","BEA state GDP + world_bank GDP",72,82,78,82,62,80,78,88))
ideas.append(mk("gv010","Americas Biggest Employer in Each State","The single largest employer in every state - Walmart dominates","MAP","US-State","State choropleth","Economy","company employment data",65,88,78,72,55,78,62,82))
ideas.append(mk("gv011","The Billionaire Map: Where the Ultra-Rich Live","Billionaire residences per capita by city","MAP","World","Dot map","Economy","Forbes billionaire list",72,78,72,72,62,82,65,85))
ideas.append(mk("gv012","Americas Union Decline: Membership Rate 1950-2025","The slow death of organized labor in one animated chart","CHART","US","Line chart","Labor","BLS union membership data",75,78,78,68,72,75,62,88))
ideas.append(mk("gv013","Gas Station Density: Where Americas Fuel Infrastructure Is","Every gas station mapped revealing transportation patterns","MAP","US","Dot map","Transportation","AFDC fuel station data",55,75,75,62,42,85,58,85))

# === HEALTH / SOCIAL ISSUES VIRAL ===
ideas.append(mk("gv014","Americas Mental Health Crisis by County","Reported mental health distress days mapped at the county level","MAP","US-County","County choropleth","Health","CDC PLACES data",85,85,72,68,82,82,62,82))
ideas.append(mk("gv015","The Suicide Rate Map: Where Despair Is Highest","Age-adjusted suicide rates by state revealing geographic clusters","MAP","US-State","State choropleth","Health","CDC WONDER suicide data",88,78,72,68,90,78,62,85))
ideas.append(mk("gv016","Americas Uninsured: Where People Lack Health Coverage","Percentage without health insurance by county","MAP","US-County","County choropleth","Health","Census ACS insurance data",82,85,75,68,80,82,58,85))
ideas.append(mk("gv017","The Life Expectancy Gap: Americas Richest vs Poorest Counties","30-year life expectancy difference between wealthiest and poorest counties","XREF","US-County","Bivariate choropleth","Health","CDC life expectancy + Census income",90,85,72,78,88,82,72,82))
ideas.append(mk("gv018","Childhood Asthma Rates by State: The Air Kids Breathe","Pediatric asthma prevalence mapped showing environmental health impacts","MAP","US-State","State choropleth","Health","CDC childhood asthma data",80,82,72,65,78,78,62,82))

# === REGION-SPECIFIC DEEP DIVES ===
ideas.append(mk("gv019","Appalachias Data Portrait: 423 Counties in 13 States","Every major indicator mapped for the Appalachian Regional Commission area","MAP","US-County","County choropleth","Demographics","ARC data + Census",78,78,72,68,72,82,72,78))
ideas.append(mk("gv020","The Deep Souths Data Dashboard","Mississippi, Alabama, Louisiana, Georgia, South Carolina compared on 15 metrics","MAP","US-State","State choropleth","Demographics","Census + CDC + FBI data",72,78,72,68,68,78,65,82))
ideas.append(mk("gv021","New Englands Six States: How Different Are They Really?","CT, MA, ME, NH, RI, VT compared on everything from lobster catches to politics","MAP","US-State","State choropleth","Demographics","Census + state data",65,80,75,65,55,78,68,82))
ideas.append(mk("gv022","Texass Megacity Triangle: Dallas-Houston-San Antonio","The economic output and demographics of the Texas Triangle megaregion","MAP","US-City","Dot map","Economy","Census + BEA metro data",65,78,75,65,55,82,65,82))
ideas.append(mk("gv023","The Great Plains Depopulation: 100 Years of Rural Decline","County population change in the Great Plains from 1920 to 2020","MAP","US-County","Animated choropleth","Demographics","Census historical county data",80,75,72,72,78,85,72,78))

# === ELECTION / POLITICS ===
ideas.append(mk("gv024","Every County That Flipped 2016 to 2020","Counties that changed party allegiance between presidential elections","MAP","US-County","County choropleth","Elections","election results data",78,82,78,72,78,82,62,90))
ideas.append(mk("gv025","The 50 Counties That Decide Presidential Elections","Swing counties with the narrowest margins that determine outcomes","MAP","US-County","Dot map","Elections","election results data",78,82,72,72,78,82,72,85))
ideas.append(mk("gv026","Congressional Gerrymandering: Most Oddly Shaped Districts","Polsby-Popper compactness scores for every congressional district","MAP","US","Special map","Elections","Census TIGER congressional districts",75,78,72,78,72,85,72,85))
ideas.append(mk("gv027","Americas Political Polarization in One Map","Margin of victory in presidential elections by county showing fewer competitive areas","MAP","US-County","County choropleth","Elections","election results data",78,82,72,72,80,82,62,88))

# === FOOD & AGRICULTURE VIRAL ===
ideas.append(mk("gv028","Americas Bread Basket: Where Each Crop Is Grown","County-level crop production maps for corn, wheat, soybeans, cotton","MAP","US-County","County choropleth","Food & Nutrition","USDA NASS crop data",62,72,78,62,48,85,62,85))
ideas.append(mk("gv029","The Meat Map: Which States Produce Which Livestock","Cattle, hogs, chickens, and turkeys by state","MAP","US-State","State choropleth","Food & Nutrition","USDA NASS livestock data",60,75,78,62,48,80,58,85))
ideas.append(mk("gv030","Americas Beer Map: Craft Breweries Per Capita by State","The craft beer explosion mapped showing where microbreweries cluster","MAP","US-State","State choropleth","Food & Nutrition","Brewers Association data",62,85,78,68,48,78,62,85))

# === ENVIRONMENT / NATURE ===
ideas.append(mk("gv031","Americas Endangered Species Hotspots","Counties with the most threatened and endangered species","MAP","US-County","County choropleth","Geography & Environment","USFWS endangered species data",78,72,72,68,75,82,68,82))
ideas.append(mk("gv032","The Worlds River Basins: All Water Flows Somewhere","Every major river basin on Earth colored by drainage area","MAP","World","Special map","Geography & Environment","HydroSHEDS river basin data",62,65,72,68,48,92,72,82))
ideas.append(mk("gv033","Americas Wind Energy Potential by County","Wind speed at hub height showing where turbines make sense","MAP","US-County","County choropleth","Climate","NREL wind resource data",65,72,78,65,58,82,62,85))
ideas.append(mk("gv034","The Permafrost Map: Whats Thawing and Why It Matters","Global permafrost extent and rates of thaw","MAP","World","World choropleth","Climate","NSIDC permafrost data",82,68,68,72,82,85,72,78))
ideas.append(mk("gv035","Ocean Plastic Pollution: Where Trash Accumulates","Concentrations of plastic debris in world oceans from satellite and survey data","MAP","World","Dot map","Climate","5 Gyres + NOAA marine debris",85,78,72,72,82,88,68,78))

# === LABOR / WORK ===
ideas.append(mk("gv036","Americas Remote Work Map: Who Works From Home by County","Share of workers who work remotely at the county level","MAP","US-County","County choropleth","Labor","Census ACS WFH data",70,90,78,68,58,82,62,85))
ideas.append(mk("gv037","The Gig Economy Map: Independent Contractor Rates by Metro","Share of workers who are self-employed or contract workers by city","MAP","US-Metro","Dot map","Labor","Census + IRS self-employment data",68,82,72,68,58,78,65,78))
ideas.append(mk("gv038","Americas Most Dangerous Jobs Ranked","Fatality rates per 100k workers by occupation","RANK","US","Bar chart","Labor","BLS Census of Fatal Occupational Injuries",75,82,78,72,72,70,58,88))
ideas.append(mk("gv039","Night Shift America: Share of Workers Not on Day Shift","Where night and rotating shift work is most common by industry and state","MAP","US-State","State choropleth","Labor","BLS work schedule data",65,78,72,68,58,75,68,78))
ideas.append(mk("gv040","The Minimum Wage Patchwork: State, County, and City Minimums","Americas complex web of local minimum wages mapped","MAP","US","Dot map","Labor","DOL + local ordinance data",72,88,72,68,68,82,62,82))

print(f"BATCH_GV: {len(ideas)} ideas generated")

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
    print("[BATCH_GV] ERROR: tail marker not found"); sys.exit(1)
raw = raw.replace(tail, "")
for idea in new_ideas:
    raw += idea + ",\n"
raw += tail + "\n"
with open(DATA_JS, "w", encoding="utf-8") as f:
    f.write(raw)
print(f"[BATCH_GV] Injected {len(new_ideas)} new ideas (skipped {skipped} dupes)")
