import os, sys, re
sys.path.insert(0, r"D:\projects\mapzimus-board")

def mk(id,title,sub,typ,geo,fmt,sect,tbl,e,r,c,s,t,v,o,dr):
    raw=e*2+r*2+c*1.25+s*1.5+t*1.5+v*2.0+o*1.5
    vs=int((raw/11.75)*(1-0.5*(1-dr/100)))
    return ('{id:"'+id+'",title:"'+title+'",sub:"'+sub+'",type:"'+typ+'",'
            'geo:"'+geo+'",fmt:"'+fmt+'",section:"'+sect+'",tbl:"'+tbl+'",'
            'sc:{emotional:'+str(e)+',relatability:'+str(r)+',clarity:'+str(c)
            +',surprise:'+str(s)+',tension:'+str(t)+',visual:'+str(v)
            +',originality:'+str(o)+',data_ready:'+str(dr)+'}'
            ',vs:'+str(vs)+',topics:[],ext:[],status:"idea",notes:""}')

ideas = [
# --- "Maps the Internet will fight over" ---
mk("hak001","Best BBQ Region in America: A Scientific Assessment","Texas vs Carolina vs Memphis vs Kansas City - the data picks a winner","MAP","US","State choropleth","Food & Nutrition","bbq_survey",9,9,6,7,7,8,8,45),
mk("hak002","Is a Hot Dog a Sandwich? The Geographic Divide","Regional opinions mapped by survey data","MAP","US","State choropleth","Food & Nutrition","yougov_survey",8,9,5,7,4,7,9,45),
mk("hak003","Whats the Correct Way to Load a Dishwasher: Regional Preferences","A surprisingly heated debate with geographic patterns","MAP","US","State choropleth","Demographics","survey_data",7,9,5,6,3,6,8,40),
mk("hak004","Best Pizza Style by Region: New York vs Chicago vs Detroit","The great pizza war mapped by where people actually order","MAP","US","State choropleth","Food & Nutrition","pizza_survey",8,9,5,7,5,7,8,45),
mk("hak005","At What Temperature Does It Become Shorts Weather?","60 degrees in Minnesota, 75 degrees in Florida","MAP","US","State choropleth","Climate","survey_data",8,9,6,7,3,7,8,45),
# --- Data journalism pieces ---
mk("hak006","Every Hospital in America: Mapped by Number of Beds","The healthcare desert problem in one visualization","MAP","US","Dot map","Health","cms_pos",7,8,7,7,6,9,7,65),
mk("hak007","Food Deserts by County: Where Groceries Are Miles Away","23 million Americans live more than 1 mile from a grocery store","MAP","US","County choropleth","Food & Nutrition","usda_food_access",8,8,7,7,7,8,7,65),
mk("hak008","Police Officers per Capita by City","From 0.5 per 1000 in some cities to 7 per 1000 in DC","MAP","US","Dot map","Crime and Law Enforcement","fbi_leoka",7,7,7,7,6,8,7,60),
mk("hak009","Teacher Shortages by State: Unfilled Positions Map","The states struggling hardest to find educators","MAP","US","State choropleth","Education","ed_dept",7,7,7,7,6,7,7,60),
mk("hak010","Dollar Stores per Capita by County","Dollar General has more locations than Walmart and McDonalds combined","MAP","US","County choropleth","Economy","ici_dollar_stores",7,8,7,8,5,8,8,60),
# --- Oddly specific but shareable ---
mk("hak011","Countries by Number of Islands","Sweden has 267,570 islands, Indonesia has 17,508","MAP","World","World choropleth","Geography & Environment","manual_geo",6,7,6,8,3,8,7,60),
mk("hak012","Most Common Street Name in Every US State","Main Street vs First Street vs Park Avenue","MAP","US","State choropleth","Geography & Environment","census_tiger",7,8,6,7,3,7,8,65),
mk("hak013","US Zip Codes by Shape: Weirdest Geometries","Some zip codes look like gerrymandered districts","MAP","US","Special map","Geography & Environment","census_zcta",6,6,5,8,3,8,9,60),
mk("hak014","How Far You Can Drive in 3 Hours From Every US City","The road trip isochrone map","MAP","US","Special map","Transportation","here_api",7,8,6,7,4,8,8,55),
mk("hak015","The Most Common Tree Species in Every US State","Sugar maple in the NE, loblolly pine in the SE","MAP","US","State choropleth","Environment","usfs_fia",6,7,6,7,3,8,8,60),
# --- Economy/finance viral ---
mk("hak016","Average Credit Card Debt by State","Alaska residents carry $8k avg, Wisconsin carries $4k","MAP","US","State choropleth","Economy","experian_data",8,9,7,7,5,7,7,60),
mk("hak017","States by Median Household Income: 2024 Update","Maryland leads at $95k, Mississippi trails at $48k","MAP","US","State choropleth","Economy","census_acs",7,8,8,6,5,7,6,65),
mk("hak018","Tax Burden by State: Total Tax as % of Income","New York collects 12.7%, Alaska collects 5.4%","MAP","US","State choropleth","Economy","tax_foundation",8,9,8,7,6,7,7,65),
mk("hak019","Net Migration by State: Where Are Americans Moving?","Texas, Florida, and North Carolina gain; New York, California, Illinois lose","MAP","US","State choropleth","Population","census_migration",8,8,7,7,6,8,7,65),
mk("hak020","Countries by Ease of Doing Business Score","New Zealand #1, Somalia last - the regulatory burden map","MAP","World","World choropleth","Economy","world_bank_db",6,6,7,7,5,8,6,65),
]

ideas2 = [
# --- History buffs ---
mk("hak021","Every Battle of the American Civil War: Mapped","Over 10,000 engagements from Fort Sumter to Appomattox","MAP","US","Dot map","History","nps_cwsac",7,7,6,7,6,9,7,65),
mk("hak022","Countries That Were Part of the British Empire at Peak","At its height, the Empire covered 26% of Earths land","MAP","World","World choropleth","History","manual_history",7,7,6,8,5,8,7,65),
mk("hak023","The Rise and Fall of Every Empire: Territory Over Time","Roman, Mongol, British, Ottoman, Spanish - animated","CHART","World","Area chart","History","manual_history",7,7,6,8,6,8,8,55),
mk("hak024","Every Country Alexander the Great Conquered","Modern borders overlaid on his route of conquest","MAP","World","Special map","History","manual_history",7,7,5,8,5,8,8,55),
mk("hak025","US Presidential Election Results: Every County Since 1960","Watch the red-blue shift county by county over 60 years","MAP","US","Animated choropleth","Elections","mit_election_lab",8,8,7,7,8,8,7,70),
# --- Nature/science ---
mk("hak026","Animal Species Diversity by Country: The Biodiversity Hotspots","Brazil leads with 80,000+ known species","MAP","World","World choropleth","Environment","iucn_redlist",6,6,6,7,5,8,7,60),
mk("hak027","Lightning Strike Density by Country","The Congo Basin gets 160 strikes per sq km per year","MAP","World","World choropleth","Climate","nasa_lis",6,6,6,8,4,8,8,65),
mk("hak028","Tectonic Plate Boundaries: Every Plate Mapped","The 15 major and 40 minor plates that make up Earths crust","MAP","World","Line map","Science & Technology","usgs_plates",5,5,6,7,5,9,6,70),
mk("hak029","Deepest Points in Every Ocean","Mariana Trench is 36,000 feet - deeper than Everest is tall","MAP","World","Dot map","Geography & Environment","noaa_bathymetry",6,6,6,8,4,8,8,65),
mk("hak030","Coral Reef Locations and Bleaching Status","50% of the worlds reefs have experienced severe bleaching","MAP","World","Dot map","Environment","noaa_coral",7,7,6,7,7,9,7,60),
# --- Final section fillers ---
mk("hak031","Voter Turnout by Country: Who Actually Shows Up?","Belgium: 88%, US: 66%, Switzerland: 45%","MAP","World","World choropleth","Elections","idea_int",7,7,7,7,6,8,6,65),
mk("hak032","Incarceration Rate by State: The American Prison Map","Louisiana leads at 1,094 per 100k, Massachusetts at 167","MAP","US","State choropleth","Crime and Law Enforcement","bjs_prisoners",7,7,7,7,7,7,7,65),
mk("hak033","Wind Farm Locations in the US","The Great Plains are Americas wind energy powerhouse","MAP","US","Dot map","Environment","eia_wind",5,5,6,6,4,8,6,65),
mk("hak034","Solar Energy Potential by Country","The Sahara could power the entire world 50x over","MAP","World","World choropleth","Environment","solargis",6,6,6,7,5,8,7,60),
mk("hak035","Global Internet Submarine Cable Map","99% of international data travels through undersea cables","MAP","World","Line map","Science & Technology","telegeography",6,6,6,8,5,9,8,65),
]

# --- INJECTION ---
DATA = r"D:\projects\mapzimus-board\data.js"
with open(DATA, "r", encoding="utf-8") as f:
    blob = f.read()

tail = "]; // end D"
if tail not in blob:
    print("ERROR: tail marker not found"); sys.exit(1)

existing_ids = set()
for m in re.finditer(r'id:"([^"]+)"', blob):
    existing_ids.add(m.group(1))

all_ideas = ideas + ideas2
new = [i for i in all_ideas if i.split('id:"')[1].split('"')[0] not in existing_ids]
dupes = len(all_ideas) - len(new)

blob = blob.replace(tail, ",\n".join(new) + ",\n" + tail)
with open(DATA, "w", encoding="utf-8") as f:
    f.write(blob)

print(f"BATCH_HAK: {len(all_ideas)} ideas generated")
print(f"[BATCH_HAK] Injected {len(new)} new ideas (skipped {dupes} dupes)")
