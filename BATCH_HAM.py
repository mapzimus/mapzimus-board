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
# --- "Imagine If" / Perspective Maps ---
mk("ham001","The World Map Sized by Population Instead of Land Area","Africa and Asia dwarf everything else when weighted by people","MAP","World","Special map","Population","D:/raw_data/Kaggle/pop/popolazione-globale-per-paese-1950-2024.csv",7,7,6,8,4,9,8,85),
mk("ham002","What If Every State Had Equal Population: Redrawn Borders","30 million people per state creates bizarre new states","MAP","US","Special map","Population","census_2020",7,8,6,8,4,8,9,55),
mk("ham003","The Upside-Down World Map: South on Top","How perspective changes what feels like the center of the world","MAP","World","Special map","Geography & Environment","manual_geo",6,7,5,8,3,8,9,50),
mk("ham004","Earth at Night: Light Pollution Satellite Map","The brightest and darkest places on Earth","MAP","World","Special map","Environment","nasa_black_marble",7,7,6,7,5,9,7,65),
mk("ham005","What If the US Interstate System Were a Subway Map?","The Beck-style transit diagram of Americas highways","MAP","US","Special map","Transportation","fhwa + manual_design",7,8,6,8,4,9,9,50),
# --- "By Generation" breakdowns ---
mk("ham006","Gen Z vs Millennial vs Boomer: Homeownership Rate by Age","Boomers owned homes at 30 at double the rate Gen Z does now","CHART","US","Bar chart","Housing","census_cps",8,9,7,7,7,7,7,60),
mk("ham007","Average Student Loan Balance by Generation","Millennials hold $40k avg, Gen Z is already at $22k","CHART","US","Bar chart","Education","fed_scf",8,9,7,7,6,6,7,55),
mk("ham008","Social Media Platform Use by Generation","TikTok dominates Gen Z, Facebook dominates Boomers","CHART","US","Bar chart","Science & Technology","pew_internet",7,8,7,6,4,6,7,55),
# --- "One Country Deep Dive" viral ---
mk("ham009","Japans Population Pyramid: 1950 vs 2000 vs 2025","From pyramid to inverted diamond in 75 years","CHART","World","Bar chart","Population","un_population",7,7,7,8,7,7,7,70),
mk("ham010","Indias GDP by State: The Internal Inequality Map","Maharashtra alone produces 15% of national GDP","MAP","World","Special map","Economy","india_cso",6,6,7,7,5,8,7,60),
mk("ham011","Chinas Ghost Cities: Population vs Built Capacity","Cities designed for 1 million that have 50,000 residents","MAP","World","Dot map","Housing","manual_china",7,7,6,8,6,8,8,50),
mk("ham012","Brazils Biomes: Deforestation Rate by Region","Amazon gets attention but Cerrado is losing forest faster","MAP","World","Special map","Environment","inpe_prodes",7,6,6,7,7,8,8,55),
# --- "Small Data, Big Impact" ---
mk("ham013","Every Nuclear Detonation Since 1945: Location and Yield","Over 2,000 nuclear tests mapped with blast radius","MAP","World","Dot map","History","ctbto_nuclear",8,7,6,8,8,9,8,65),
mk("ham014","Every Commercial Plane Crash Since 1970","The map that shows flying is actually getting safer","MAP","World","Dot map","Transportation","asn_database",7,7,6,7,6,9,7,60),
mk("ham015","Every Mass Shooting in America: 2014-2024","The density map that shocks even when you expect it","MAP","US","Dot map","Crime and Law Enforcement","gun_violence_archive",9,8,6,7,9,8,7,65),
mk("ham016","Every Tornado Touchdown in the US: 1950-2024","Tornado Alley lights up but the Southeast is deadlier","MAP","US","Dot map","Climate","noaa_spc",7,7,6,7,5,9,7,70),
mk("ham017","Every Wildfire Over 100 Acres: 2000-2025","The West is burning at unprecedented rates","MAP","US","Dot map","Climate","nifc_wildfire",7,7,6,7,7,9,7,65),
# --- Economy/Money viral ---
mk("ham018","How Long You Need to Work to Buy an iPhone by Country","7 hours in the US, 456 hours in Nigeria","MAP","World","World choropleth","Economy","numbeo_prices",8,9,7,8,5,8,8,55),
mk("ham019","Rent vs Buy: Monthly Cost Comparison by US City","In 47 of 50 metro areas, renting is now cheaper than buying","MAP","US","Dot map","Housing","zillow + redfin",8,9,7,7,6,8,7,55),
mk("ham020","Countries by Gold Reserves Held","The US holds 8,133 tons, Germany holds 3,355 tons","MAP","World","World choropleth","Economy","wgc_gold",6,6,7,7,5,8,7,65),
]

ideas2 = [
# --- US regional culture ---
mk("ham021","Accents of America: The Dialect Region Map","14 distinct dialect regions across the continental US","MAP","US","State choropleth","Demographics","dare_linguistic",7,8,5,7,3,8,8,55),
mk("ham022","High School Mascot Types by State: Eagles vs Bulldogs vs Panthers","Eagles dominate the West, Bulldogs own the South","MAP","US","State choropleth","Education","nces_schools",7,8,5,7,3,7,8,55),
mk("ham023","Americas Favorite Fast Food Chain by State","Chick-fil-A dominates the South, In-N-Out the West","MAP","US","State choropleth","Food & Nutrition","survey_data",8,9,5,7,4,7,8,50),
mk("ham024","Tipping Culture by State: Average Tip Percentage","New Yorkers tip 20%+, Westerners average 16%","MAP","US","State choropleth","Economy","square_data",7,9,6,7,4,7,7,50),
# --- Global infrastructure ---
mk("ham025","Countries Without a Railway System","46 countries have no rail infrastructure at all","MAP","World","World choropleth","Transportation","uic_rail",5,5,6,8,4,8,7,60),
mk("ham026","Tallest Building in Every Country","Most people cant name the tallest building outside their own country","MAP","World","Dot map","Economy","ctbuh_skyscraper",6,7,6,7,3,8,7,55),
mk("ham027","Countries With Nuclear Power Under Construction","14 countries are actively building new nuclear plants","MAP","World","World choropleth","Science & Technology","iaea_pris",5,5,7,7,6,8,7,65),
# --- More cross-refs with emotional pull ---
mk("ham028","Population Growth vs Carbon Emissions: The Equity Question","Poor countries grew fastest but emit the least","XREF","World","Scatter plot","Climate","D:/raw_data/Kaggle/pop/popolazione-globale-per-paese-1950-2024.csv + D:/raw_data/Our World In Data/co-emissions-per-capita.csv",7,7,7,8,7,7,8,75),
mk("ham029","GDP Growth vs Deforestation Rate: Development Costs","Rapid economic growth often comes at environmental expense","XREF","World","Scatter plot","Environment","D:/raw_data/Kaggle/archive (35)/historysaid-global-economic-dataset/data/core/world_bank.csv + gfw_tree_loss",6,6,7,8,7,7,8,65),
mk("ham030","Military Spending vs Education Spending by Country","Some countries spend 5x more on guns than schools","XREF","World","Scatter plot","International Statistics","sipri_milex + D:/raw_data/Kaggle/archive (35)/historysaid-global-economic-dataset/data/core/world_bank.csv",7,7,7,8,7,7,8,65),
mk("ham031","Internet Speed vs GDP per Capita: Bandwidth = Wealth?","Fast internet and high GDP correlate strongly","XREF","World","Scatter plot","Science & Technology","speedtest + D:/raw_data/Kaggle/archive (35)/historysaid-global-economic-dataset/data/core/world_bank.csv",6,6,7,7,5,7,7,60),
mk("ham032","Renewable Energy Share vs Carbon Emissions per Capita","The countries walking the talk on climate","XREF","World","Scatter plot","Climate","irena + D:/raw_data/Our World In Data/co-emissions-per-capita.csv",6,6,7,7,6,7,7,65),
mk("ham033","Happiness vs Freedom: Voice and Accountability vs Happiness Score","The happiest countries are the freest - almost without exception","XREF","World","Scatter plot","International Statistics","unsdsn_whr + D:/raw_data/Kaggle/archive (35)/historysaid-global-economic-dataset/data/core/world_bank_wgi.csv",7,7,7,8,5,7,8,65),
mk("ham034","AI Adoption vs Unemployment Rate by Country","AI adoption doesnt increase unemployment - yet","XREF","World","Scatter plot","Labor","D:/raw_data/Kaggle/archive (40)/ai_index_main.csv + ilo_unemployment",6,7,7,8,7,7,8,60),
mk("ham035","Spotify Streams vs Population: Music Punches Above Weight","South Korea and Sweden produce far more streams than population suggests","XREF","World","Scatter plot","Entertainment","D:/raw_data/Kaggle/spotify/spotify_alltime_top100_songs.csv + D:/raw_data/Kaggle/pop/popolazione-globale-per-paese-1950-2024.csv",6,7,6,7,4,7,8,80),
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

print(f"BATCH_HAM: {len(all_ideas)} ideas generated")
print(f"[BATCH_HAM] Injected {len(new)} new ideas (skipped {dupes} dupes)")
