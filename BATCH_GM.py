"""BATCH_GM: Ideas from Downloads/GIS data, US Companies, immigration data,
groundwater, NH parcels, public schools, asylum/refugee data.
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

# ============================================================
# GROUNDWATER / SEA LEVEL RISE (GeoJSON + CSV)
# ============================================================
ideas.append(mk("gm001","Where the Ground Is Rising: Modeled Groundwater Risk Areas","Groundwater rise risk zones mapped from climate projection models","MAP","US","Dot map","Climate","C:/Users/mhowe/Downloads/GIS_Data/Groundwater_Rise_Modeled_Areas.geojson",78,72,68,75,80,82,78,88))
ideas.append(mk("gm002","Saltwater Intrusion Threat Map","Coastal areas where rising seas are contaminating freshwater aquifers","MAP","US","Dot map","Climate","C:/Users/mhowe/Downloads/GIS_Data/Saltwater_Intrusion_Modeled_Areas.csv",80,70,68,78,82,82,80,85))
ideas.append(mk("gm003","1 Foot of Sea Level Rise: Who Gets Flooded?","Vulnerable areas with less than 10ft groundwater depth under 1ft SLR scenario","MAP","US","Dot map","Climate","C:/Users/mhowe/Downloads/GIS_Data/Vulnerable_areas_(%3C10_ft_GWD)_with_1_foot_of_SLR.csv",85,78,70,75,88,82,75,85))

# ============================================================
# IMMIGRATION / POPULATION DATA (HSUS zips in GIS_Data)
# ============================================================
ideas.append(mk("gm004","Alien Admissions by Program: Who Gets Into America?","Immigration admission categories over time - family, employment, diversity, refugee","CHART","US","Stacked area chart","Demographics","C:/Users/mhowe/Downloads/GIS_Data/Alien Admissions, by Program.zip",72,78,75,70,72,70,65,85))
ideas.append(mk("gm005","Americas Border Control Timeline","Historical data on border enforcement, apprehensions, and deportations","CHART","US","Line chart","Demographics","C:/Users/mhowe/Downloads/GIS_Data/Border Control.zip",75,75,70,68,80,72,65,82))
ideas.append(mk("gm006","Immigrants by Country of Origin: 200 Years of Shifting Sources","Where Americas immigrants came from, decade by decade","CHART","World","Stacked area chart","Demographics","C:/Users/mhowe/Downloads/GIS_Data/Immigrants, by Country.zip",78,80,75,72,70,78,70,82))
ideas.append(mk("gm007","The Net Migration Map: Countries People Leave vs Enter","Immigrants minus emigrants by country over time","MAP","World","World choropleth","International Statistics","C:/Users/mhowe/Downloads/GIS_Data/Immigrants, Emigrants, and Net Migration.zip",72,75,72,70,68,80,68,82))
ideas.append(mk("gm008","The Foreign-Born Population Map: Where Immigrants Settle","Characteristics and geographic distribution of Americas foreign-born population","MAP","US-State","State choropleth","Demographics","C:/Users/mhowe/Downloads/GIS_Data/Foreign-Born Population and Its Characteristics.zip",70,78,72,65,65,78,62,85))
ideas.append(mk("gm009","Americas Internal Migration: Who Moves Where?","State-to-state migration flows within the United States","MAP","US-State","Flow map","Demographics","C:/Users/mhowe/Downloads/GIS_Data/Internal Migration.zip",72,85,72,68,62,82,68,82))
ideas.append(mk("gm010","The Path to Citizenship: Naturalization Rates by Origin Country","Which immigrant groups naturalize fastest and at what rates","CHART","US","Bar chart","Demographics","C:/Users/mhowe/Downloads/GIS_Data/Naturalization.zip",68,75,72,70,62,70,68,82))
ideas.append(mk("gm011","The Hispanic Population Explosion: 1850 to Present","Growth curve and geographic spread of Hispanic Americans","MAP","US-State","Animated choropleth","Demographics","C:/Users/mhowe/Downloads/GIS_Data/Hispanic Population.zip",72,80,75,65,68,78,60,82))
ideas.append(mk("gm012","Americas Mortality Map: Life Expectancy by State","State-level mortality rates and life expectancy variations","MAP","US-State","State choropleth","Health","C:/Users/mhowe/Downloads/GIS_Data/Mortality.zip",78,82,75,65,75,78,58,85))
ideas.append(mk("gm013","The Slave State Map: Census Data 1790-1860","State-by-state slave populations from historical census data","MAP","US-State","Animated choropleth","History","C:/Users/mhowe/Downloads/GIS_Data/Slave Population.zip",90,80,72,70,92,85,75,82))

# ============================================================
# PUBLIC SCHOOLS
# ============================================================
ideas.append(mk("gm014","Every Public School in America: 100,000+ Schools Mapped","All U.S. public school locations with characteristics and demographics","MAP","US","Dot map","Education","D:/raw_data/Public_School_Characteristics_2022-23.csv",68,82,78,65,55,85,62,95))
ideas.append(mk("gm015","The School Segregation Map: Diversity Index by District","How racially diverse (or segregated) is each public school district?","MAP","US-County","County choropleth","Education","D:/raw_data/Public_School_Characteristics_2022-23.csv",82,80,70,72,85,82,72,90))
ideas.append(mk("gm016","Title I Schools: Where Poverty Meets Education","Map of schools receiving Title I funding for high-poverty areas","MAP","US","Dot map","Education","D:/raw_data/Public_School_Characteristics_2022-23.csv",78,82,72,68,78,80,65,92))

# ============================================================
# US COMPANIES
# ============================================================
ideas.append(mk("gm017","Americas Corporate Geography: Where Companies Cluster","Mapping US company headquarters and employment concentrations","MAP","US-State","Dot map","Economy","D:/raw_data/EconData/USCompanies.csv",65,78,75,68,55,80,62,88))

# ============================================================
# NEW HAMPSHIRE GIS DATA
# ============================================================
ideas.append(mk("gm018","Every Road in New Hampshire","Complete DOT road network visualization of the Granite State","MAP","US-State","Line map","Transportation","C:/Users/mhowe/Downloads/GIS_Data/NH_DOT_Roads.csv",50,60,72,58,42,85,65,90))
ideas.append(mk("gm019","New Hampshire Parcel Map: Who Owns What","Land parcel polygons across the Granite State","MAP","US-State","Polygon map","Housing","C:/Users/mhowe/Downloads/GIS_Data/NH_Parcel_Mosaic_-_Polygons.csv",55,65,70,60,48,82,62,85))

# ============================================================
# ASYLUM / REFUGEE DATA (Kaggle archive 25)
# ============================================================
ideas.append(mk("gm020","The Asylum Pipeline: From Application to Decision","How many asylum cases are filed, pending, approved, and denied each year","CHART","US","Stacked bar chart","Demographics","D:/raw_data/Kaggle/archive (25)/Annual Asylum Open Data.xlsx",78,75,70,68,80,72,68,90))
ideas.append(mk("gm021","Where Refugees Come From: Source Countries Over Time","Top refugee source countries mapped over 20 years of data","MAP","World","World choropleth","International Statistics","D:/raw_data/Kaggle/archive (25)/USCIS and EOIR Open Refugee Data.xlsx",78,75,72,70,78,80,68,88))
ideas.append(mk("gm022","The Asylum Backlog: How Long America Makes People Wait","Monthly and quarterly asylum case volumes showing growing backlogs","CHART","US","Line chart","Demographics","D:/raw_data/Kaggle/archive (25)/Calendar Monthly Open Data.xlsx",75,72,68,70,78,68,65,90))

# ============================================================
# FOOTBALL RESULTS 2026 (Kaggle FBRESULTS26)
# ============================================================
ideas.append(mk("gm023","Every International Football Match Ever Played","Complete database of international football results with goals and venues","MAP","World","World choropleth","Sports & Recreation","D:/raw_data/Kaggle/FBRESULTS26/results.csv",65,78,78,62,50,78,60,95))
ideas.append(mk("gm024","The Top International Goal Scorers of All Time","All-time leading scorers in international football history","RANK","World","Bar chart","Sports & Recreation","D:/raw_data/Kaggle/FBRESULTS26/goalscorers.csv",62,75,78,65,52,70,58,95))
ideas.append(mk("gm025","Penalty Shootout Kings: Which Countries Win When It Matters Most","World Cup and international shootout records by nation","RANK","World","Bar chart","Sports & Recreation","D:/raw_data/Kaggle/FBRESULTS26/shootouts.csv",68,78,75,72,68,70,72,92))

# ============================================================
# MODERN SLAVERY (Kaggle archive 24)
# ============================================================
ideas.append(mk("gm026","The Global Slavery Index: Modern Slavery in 2018","Estimated victims of modern slavery by country - 40 million people worldwide","MAP","World","World choropleth","International Statistics","D:/raw_data/Kaggle/archive (24)/modern_slavery_final/GIS_2018_report.csv",90,78,68,80,92,82,75,85))

# ============================================================
# DETENTION STAYS (Kaggle archive 16)
# ============================================================
ideas.append(mk("gm027","How Long Does America Detain Immigrants?","Average detention stay lengths by facility and nationality","CHART","US","Bar chart","Demographics","D:/raw_data/Kaggle/archive (16)/detention-stays-latest.csv",78,72,65,70,82,68,68,90))

print(f"BATCH_GM: {len(ideas)} ideas generated")

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
    print("[BATCH_GM] ERROR: tail marker not found in data.js")
    sys.exit(1)

raw = raw.replace(tail, "")
for idea in new_ideas:
    raw += idea + ",\n"
raw += tail + "\n"

with open(DATA_JS, "w", encoding="utf-8") as f:
    f.write(raw)

print(f"[BATCH_GM] Injected {len(new_ideas)} new ideas (skipped {skipped} dupes)")
