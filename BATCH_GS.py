"""BATCH_GS: Third cross-reference round + animated/time-series ideas.
Focus on multi-dataset combos, animated visualizations, and
Reddit/Instagram viral formats.
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

# === ANIMATED / TIME-SERIES ===
ideas.append(mk("gs001","Watch the World Get Richer: GDP Per Capita 1960-2025 Animated","Every country's GDP per capita animated over 65 years on a world map","MAP","World","Animated choropleth","Economy","world_bank GDP per capita",72,78,78,65,65,88,62,88))
ideas.append(mk("gs002","Americas Political Realignment: Presidential Election Results 1960-2024","Animated state map showing the partisan shift over 16 elections","MAP","US-State","Animated choropleth","Elections","election results data",82,85,78,72,80,88,68,88))
ideas.append(mk("gs003","Watch CO2 Emissions Explode: 1900 to Present Animated","Per-capita carbon emissions animated globally over 125 years","MAP","World","Animated choropleth","Climate","OWID co2-per-capita",80,75,72,72,80,88,65,85))
ideas.append(mk("gs004","The Spread of the Internet: 1995 to 2025 Animated","Watch internet adoption sweep across the globe year by year","MAP","World","Animated choropleth","Science & Technology","OWID internet access",72,78,78,70,62,88,65,90))
ideas.append(mk("gs005","Watch Democracy Retreat: Political Regimes 2000-2025","Animated map showing democratic backsliding over 25 years","MAP","World","Animated choropleth","International Statistics","OWID political-regime",82,75,72,75,85,88,72,88))
ideas.append(mk("gs006","Americas Opioid Epidemic: Drug Deaths 1999-2024 Animated","Watch overdose mortality sweep across the country year by year","MAP","US-County","Animated choropleth","Health","CDC WONDER overdose data",90,82,72,72,92,88,65,85))
ideas.append(mk("gs007","The Fertility Collapse in Real Time: 1960-2025","Watch children-per-woman drop globally in an animated world map","MAP","World","Animated choropleth","Demographics","OWID children-born-per-woman",80,80,75,75,78,88,68,88))
ideas.append(mk("gs008","Watch Amazon Eat Retail: Store Closures vs E-Commerce 2010-2025","Animated map of retail store closures alongside e-commerce growth","MAP","US","Animated choropleth","Economy","retail closure + e-commerce data",78,85,72,72,75,85,72,78))
ideas.append(mk("gs009","The Obesity Epidemic Spreading: CDC Data 1985-2024 Animated","State-level obesity rates animated showing the wave across decades","MAP","US-State","Animated choropleth","Health","CDC obesity prevalence data",82,85,75,72,80,88,60,85))
ideas.append(mk("gs010","Global Deforestation Time-Lapse: 2000-2025","Watch forest cover shrink globally in an animated satellite-data map","MAP","World","Animated choropleth","Climate","Global Forest Watch data",85,78,72,75,85,90,70,82))

# === MORE CROSS-REFERENCES: UNEXPECTED COMBOS ===
ideas.append(mk("gs011","States With the Most Veterans Also Have the Most Gun Stores","Veteran population vs firearms retailer density by state","XREF","US-State","Bivariate choropleth","Demographics","ProQuest veterans + ATF FFL data",72,72,68,78,72,78,78,78))
ideas.append(mk("gs012","Where America Prays vs Where America Drinks","Religious adherent rate vs alcohol consumption by state","XREF","US-State","Bivariate choropleth","Demographics","Sage religion + alcohol data",72,80,72,82,62,78,82,82))
ideas.append(mk("gs013","Broadband Access vs Educational Attainment by County","Counties with slow internet also have fewer college graduates","XREF","US-County","Bivariate choropleth","Education","ProQuest broadband + Census education",75,80,72,72,72,82,68,78))
ideas.append(mk("gs014","Dollar Store Density vs Food Insecurity by County","Where dollar stores thrive often overlaps with food deserts","XREF","US-County","Bivariate choropleth","Economy","business data + USDA food desert",78,82,72,78,75,82,75,78))
ideas.append(mk("gs015","Teacher Pay vs Cost of Living: Where Educators Struggle Most","State teacher salaries adjusted for regional price parities","XREF","US-State","Bivariate choropleth","Education","ProQuest teacher pay + BEA price parities",78,88,78,72,75,78,65,82))
ideas.append(mk("gs016","Tornado Frequency vs Home Insurance Costs by State","States hit by more tornadoes pay more for homeowners insurance","XREF","US-State","Bivariate choropleth","Climate","NOAA tornadoes + insurance rate data",72,82,75,68,68,78,65,82))
ideas.append(mk("gs017","Military Base Locations vs Local Economic Growth","Towns with military installations vs surrounding area GDP growth","XREF","US","Dot map","Economy","DoD base locations + BEA GDP data",68,72,70,70,62,80,72,75))
ideas.append(mk("gs018","Church Density vs Opioid Deaths: The Despair Map","Religious congregation rates vs drug overdose mortality by county","XREF","US-County","Bivariate choropleth","Health","Sage religion + CDC overdose",85,78,68,82,85,82,80,78))
ideas.append(mk("gs019","Immigration Rate vs Startup Rate by Metro Area","Cities with more immigrants also have more new businesses","XREF","US-Metro","Scatter plot","Economy","Census immigration + Census business formation",72,75,72,78,62,75,78,78))
ideas.append(mk("gs020","National Park Visits vs Adjacent Town Economies","Tourism impact: NPS visitor numbers vs nearby employment growth","XREF","US","Dot map","Geography & Environment","NPS visitor stats + BLS employment",65,72,70,68,55,82,72,75))

# === COMPARISON / RANKING VIRAL FORMATS ===
ideas.append(mk("gs021","U.S. States Ranked by Every Possible Metric","Interactive ranking: toggle between 20+ indicators to see how states stack up","RANK","US-State","State choropleth","Demographics","multiple datasets combined",72,88,78,68,62,82,62,82))
ideas.append(mk("gs022","The 50 Richest Countries vs the 50 Poorest: Side by Side","GDP per capita extremes compared with matching indicators","RANK","World","Bar chart","Economy","world_bank GDP per capita",78,78,78,72,75,78,65,88))
ideas.append(mk("gs023","Countries the Size of U.S. States: Area Comparison","Which countries are closest in land area to each U.S. state","MAP","World","Special map","Geography & Environment","land area data",62,78,78,78,48,85,78,88))
ideas.append(mk("gs024","Citys Population at Different Times of Day","How downtowns swell and suburbs empty during work hours","CHART","US-City","Animated bar chart","Demographics","Census LEHD commuter data",68,82,72,72,55,82,78,78))
ideas.append(mk("gs025","The Worlds Largest Economies in 1900 vs 2025","How the economic power rankings have completely reshuffled","RANK","World","Bar chart","Economy","Maddison Project + world_bank GDP",72,75,78,78,68,78,72,82))

# === NICHE BUT VIRAL ===
ideas.append(mk("gs026","Every McDonalds in the World Mapped","30,000+ golden arches as a proxy for globalization","MAP","World","Dot map","Economy","McDonalds location data",65,82,78,72,48,85,68,82))
ideas.append(mk("gs027","The Global Coffee Production Map: Who Grows Your Morning Cup","Coffee-producing countries by volume and type (Arabica vs Robusta)","MAP","World","World choropleth","Food & Nutrition","ICO coffee production data",65,82,78,65,48,82,62,85))
ideas.append(mk("gs028","Submarine Internet Cables: The Invisible Infrastructure","Undersea fiber optic cables that carry 99% of international data","MAP","World","Line map","Science & Technology","TeleGeography cable data",68,72,72,78,58,90,78,82))
ideas.append(mk("gs029","The Worlds Languages Are Dying: Endangered Languages Mapped","Where the 3,000+ endangered languages are spoken","MAP","World","Dot map","International Statistics","UNESCO endangered languages",82,72,68,78,80,82,80,78))
ideas.append(mk("gs030","Left-Handed People by Country: The Sinister Map","Percentage of left-handers varies dramatically by culture","MAP","World","World choropleth","Health","handedness studies",58,78,70,82,42,78,82,72))

# === DATA-RICH DEEP DIVES ===
ideas.append(mk("gs031","The Complete U.S. Migration Flow Map","Every state-to-state migration flow visualized as lines","MAP","US-State","Flow map","Demographics","Census ACS migration data",72,85,75,68,62,88,68,85))
ideas.append(mk("gs032","Americas Food Deserts: Where Fresh Food Is Miles Away","USDA food desert classification at the census tract level","MAP","US","County choropleth","Food & Nutrition","USDA Food Access Research Atlas",82,82,75,68,78,82,62,85))
ideas.append(mk("gs033","Every Starbucks vs Every Public Library in America","Mapping corporate coffee against community knowledge","MAP","US","Dot map","Economy","business data + IMLS library data",68,82,72,78,58,85,78,82))
ideas.append(mk("gs034","The Heat Island Effect: Urban Temperatures vs Surrounding Areas","How much hotter cities are than their suburban/rural neighbors","MAP","US-City","Dot map","Climate","Landsat thermal data",75,78,72,72,68,85,72,78))
ideas.append(mk("gs035","Americas Cell Phone Dead Zones","Areas with no cellular coverage mapped","MAP","US","Dot map","Science & Technology","FCC coverage data",68,82,75,68,58,82,65,82))

# === SOCIAL / INEQUALITY ===
ideas.append(mk("gs036","Life Expectancy by Zip Code: The 30-Year Gap","Within the same city, life expectancy varies by decades between neighborhoods","MAP","US-City","Dot map","Health","CDC life expectancy by tract",90,88,72,82,88,82,72,82))
ideas.append(mk("gs037","The Eviction Map: Where America Kicks People Out","Eviction rates by county showing the geography of displacement","MAP","US-County","County choropleth","Housing","Eviction Lab data",85,85,72,72,85,82,68,82))
ideas.append(mk("gs038","Americas Two School Systems: Per-Pupil Spending Gap","The highest-spending districts spend 3x what the lowest do","MAP","US-County","Bivariate choropleth","Education","NCES per-pupil spending data",82,85,72,72,82,82,68,82))
ideas.append(mk("gs039","Maternal Mortality in America: A Map of Shame","The U.S. maternal death rate mapped by state - worst in the developed world","MAP","US-State","State choropleth","Health","CDC maternal mortality data",90,82,72,72,90,78,68,82))
ideas.append(mk("gs040","The Credit Score Map: Average FICO by State","Which states have the best and worst average credit scores","MAP","US-State","State choropleth","Economy","Experian credit data",68,88,78,65,58,78,58,82))

print(f"BATCH_GS: {len(ideas)} ideas generated")

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
    print("[BATCH_GS] ERROR: tail marker not found"); sys.exit(1)
raw = raw.replace(tail, "")
for idea in new_ideas:
    raw += idea + ",\n"
raw += tail + "\n"
with open(DATA_JS, "w", encoding="utf-8") as f:
    f.write(raw)
print(f"[BATCH_GS] Injected {len(new_ideas)} new ideas (skipped {skipped} dupes)")
