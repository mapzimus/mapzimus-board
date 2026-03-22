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
# --- Remaining original angles not yet covered ---
mk("hai001","Every National Park Visited: Annual Visitors Ranked","Great Smoky gets 13M, Gates of the Arctic gets 7,000","RANK","US","Bar chart","Geography & Environment","nps_stats",7,8,7,7,4,7,7,70),
mk("hai002","Water Stress by Country: Who Is Running Out?","25 countries face extremely high water stress right now","MAP","World","World choropleth","Environment","wri_aqueduct",8,7,7,8,8,8,7,65),
mk("hai003","Global Plastic Waste per Capita","Americans generate 5x more plastic waste than the global average","MAP","World","World choropleth","Environment","D:/raw_data/Our World In Data/plastic-pollution.csv",7,7,7,7,6,8,7,70),
mk("hai004","Renewable Energy Share by Country: The Green Transition Map","Iceland 100%, Norway 98%, US 21%","MAP","World","World choropleth","Environment","irena_statistics",7,7,7,7,6,8,7,70),
mk("hai005","Deaths from Natural Disasters by Decade","2000s saw fewer deaths than any decade since 1900","CHART","World","Bar chart","Environment","D:/raw_data/Our World In Data/natural-disasters.csv",7,7,7,8,6,7,7,75),
mk("hai006","Most Common Cause of Death by Country","Heart disease dominates the West, infectious disease dominates Africa","MAP","World","World choropleth","Health","who_gho",7,7,7,7,6,8,7,65),
mk("hai007","Internet Users as Percentage of Population: 2000 vs 2024","From 7% to 65% in 24 years","MAP","World","World choropleth","Science & Technology","itu_ict",7,7,7,7,5,8,6,65),
mk("hai008","Smartphone Penetration by Country","South Korea at 98%, Chad at 5%","MAP","World","World choropleth","Science & Technology","gsma_mobile",7,7,7,7,5,8,6,65),
mk("hai009","Global Food Waste: Kg per Person per Year","Americans waste 120kg of food per year, Japan wastes 30kg","MAP","World","World choropleth","Food & Nutrition","fao_food_waste",7,8,7,7,5,8,7,65),
mk("hai010","Obesity Rate by Country: The Global Weight Map","The Pacific Islands lead at 50%+, East Asia stays under 10%","MAP","World","World choropleth","Health","who_gho_obesity",7,8,7,7,5,8,6,65),
# --- US deep-cut maps ---
mk("hai011","Most Federally Owned Land by State","Nevada is 80% federal land, the East Coast is under 5%","MAP","US","State choropleth","Geography & Environment","blm_stats",7,7,7,8,5,8,7,70),
mk("hai012","Broadband Internet Access by County: The Digital Divide","Rural counties still lack reliable broadband in 2025","MAP","US","County choropleth","Science & Technology","fcc_broadband",7,8,7,7,6,8,7,65),
mk("hai013","Farm Subsidies by County: Where the Money Goes","The top 10% of counties get 60% of all farm subsidies","MAP","US","County choropleth","Economy","ewg_farm",7,7,7,7,6,8,7,60),
mk("hai014","Military Veterans as Percentage of Population by State","Alaska, Virginia, and Montana have the highest veteran rates","MAP","US","State choropleth","Demographics","va_stats",6,7,7,7,5,7,6,65),
mk("hai015","Craft Breweries per Capita by State","Vermont leads with 12 breweries per 100k people","MAP","US","State choropleth","Food & Nutrition","brewers_assoc",7,8,7,7,4,7,7,65),
# --- Time-series that tell a story ---
mk("hai016","China vs India GDP: The Race to #1","China pulled ahead in 1990 and never looked back - until now?","CHART","World","Line chart","Economy","D:/raw_data/Kaggle/archive (35)/historysaid-global-economic-dataset/data/core/world_bank.csv",7,7,7,8,7,7,7,85),
mk("hai017","Global Government Debt Since 2000: The Post-Crisis Explosion","World debt went from 60% to 100% of GDP in 25 years","CHART","World","Line chart","Economy","D:/raw_data/Kaggle/archive (35)/historysaid-global-economic-dataset/data/core/imf_weo.csv",7,7,7,7,7,7,7,85),
mk("hai018","Voice and Accountability: Countries Getting More vs Less Free","Democracy is retreating in more countries than its advancing","CHART","World","Line chart","International Statistics","D:/raw_data/Kaggle/archive (35)/historysaid-global-economic-dataset/data/core/world_bank_wgi.csv",7,7,7,8,8,7,7,85),
mk("hai019","US CPI Monthly: Every Inflationary Episode Annotated","From WWII to COVID - the moments that spiked prices","CHART","US","Line chart","Economy","D:/raw_data/cpi/historical-cpi-u-202602.xlsx",7,7,8,7,7,7,7,95),
mk("hai020","Regional GDP: Sub-Saharan Africa vs Southeast Asia Since 1960","Two regions that started similar but diverged dramatically","CHART","World","Line chart","Economy","D:/raw_data/Kaggle/archive (35)/historysaid-global-economic-dataset/data/aggregates/regional_aggregates.csv",6,6,7,8,6,7,8,85),
]

ideas2 = [
# --- Final remaining cross-refs ---
mk("hai021","Population Density vs Breakfast Cost by City","Dense cities charge more per calorie","XREF","World","Scatter plot","Food & Nutrition","D:/raw_data/Kaggle/archive (38)/breakfast basket.csv + un_population",6,7,6,7,5,7,7,70),
mk("hai022","Government Effectiveness Score vs CPI Level","Better-governed countries have more stable prices","XREF","World","Scatter plot","Economy","D:/raw_data/Kaggle/archive (35)/historysaid-global-economic-dataset/data/core/world_bank_wgi.csv + D:/raw_data/cpi/historical-cpi-u-202602.xlsx",5,5,7,7,5,7,7,70),
mk("hai023","AI Policy Score vs AI Adoption Rate by Country","Regulation slows adoption - or does it attract investment?","XREF","World","Scatter plot","Science & Technology","D:/raw_data/Kaggle/archive (40)/ai_index_main.csv",6,6,7,8,6,7,8,85),
mk("hai024","Population Growth Rate vs Political Stability Score","Rapidly growing countries tend to be less politically stable","XREF","World","Scatter plot","International Statistics","D:/raw_data/Kaggle/pop/popolazione-globale-per-paese-1950-2024.csv + D:/raw_data/Kaggle/archive (35)/historysaid-global-economic-dataset/data/core/world_bank_wgi.csv",6,6,7,7,6,7,7,80),
mk("hai025","Every Indicator vs Every Other: The Correlation Matrix","17 global indicators ranked by correlation strength","CHART","World","Special map","International Statistics","D:/raw_data/Kaggle/archive (35)/historysaid-global-economic-dataset/data/unified/all_indicators.csv",5,5,7,7,5,7,9,85),
# --- Fun finishers ---
mk("hai026","Countries Shaped Like Other Things: A Cartographic Pareidolia","Italy = boot, Chile = chili pepper, Japan = seahorse","MAP","World","Special map","Geography & Environment","manual_geo",7,8,5,8,3,8,9,50),
mk("hai027","The Straightest and Most Crooked Borders in the World","US-Canada is ruler-straight, India-Bangladesh is fractal","MAP","World","Special map","Geography & Environment","manual_geo",7,7,5,8,4,8,9,55),
mk("hai028","Every Country That Has a Dragon on Its Flag or Coat of Arms","Wales, Bhutan, and 4 others you probably didnt know","MAP","World","World choropleth","History","manual_flags",7,7,5,8,3,8,8,60),
mk("hai029","The Narrowest Countries in the World: Width at Thinnest Point","Chile is 40 miles wide, Gambia is 15 miles wide","MAP","World","Special map","Geography & Environment","manual_geo",6,7,5,8,3,8,8,55),
mk("hai030","Countries With More Tourists Than Residents","Aruba gets 10x its population in tourists every year","MAP","World","World choropleth","Economy","unwto_tourism",7,8,6,8,4,8,8,65),
mk("hai031","The Most Isolated Human Settlements on Earth","Tristan da Cunha is 1,750 miles from the nearest landmass","MAP","World","Dot map","Geography & Environment","manual_geo",7,7,5,9,4,8,9,50),
mk("hai032","US State Shapes: Which Ones Could You Draw from Memory?","Survey-based recognizability ranking of all 50 states","RANK","US","Bar chart","Geography & Environment","manual_survey",7,8,6,7,4,6,8,50),
mk("hai033","Countries That Changed Their Flag in the Last 25 Years","At least 15 nations redesigned since 2000","MAP","World","World choropleth","History","manual_flags",6,6,5,8,4,8,8,55),
mk("hai034","Every Country by When It Got Its First McDonald","The golden arches timeline: 1955-2025","MAP","World","World choropleth","Food & Nutrition","manual_mcdonalds",7,8,6,7,4,8,8,55),
mk("hai035","Countries Where English Is an Official Language but Few Speak It","India, Philippines, and 15 others","MAP","World","World choropleth","Demographics","ethnologue",6,7,6,8,4,8,7,60),
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

print(f"BATCH_HAI: {len(all_ideas)} ideas generated")
print(f"[BATCH_HAI] Injected {len(new)} new ideas (skipped {dupes} dupes)")
