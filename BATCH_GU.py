"""BATCH_GU: Final mega cross-reference round + remaining viral ideas.
Exhaustive combination mining across all discovered datasets.
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

# === FINAL CROSS-REFERENCES: DEEP COMBOS ===
ideas.append(mk("gu001","Walkability vs Obesity vs Car Ownership: The American Triangle","Three variables that perfectly predict each other by metro area","XREF","US-Metro","Scatter plot","Health","WalkabilityIndex + CDC obesity + Sage vehicles",80,85,75,78,68,78,75,78))
ideas.append(mk("gu002","The Bible Belt Paradox: Religion vs Sin Statistics","Church density vs gambling revenue, divorce, teen pregnancy, and drinking by state","XREF","US-State","State choropleth","Demographics","Sage religion + CDC/Census indicators",82,82,72,88,72,78,85,78))
ideas.append(mk("gu003","Red States vs Blue States on Every Metric","Healthcare, education, income, crime, obesity, life expectancy split by political lean","XREF","US-State","Bar chart","Elections","election data + 20+ metrics",80,88,72,78,82,78,68,82))
ideas.append(mk("gu004","Immigration and Innovation: Patents Filed by Foreign-Born Inventors","Share of patents filed by immigrants vs immigration rate by state","XREF","US-State","Bivariate choropleth","Science & Technology","USPTO patent + Census immigration",72,72,72,78,62,80,78,78))
ideas.append(mk("gu005","Heat Waves and Emergency Rooms: Climate Change Hits Healthcare","Extreme heat days vs ER visits by region showing climate-health nexus","XREF","US-State","Bivariate choropleth","Health","NOAA heat + CMS ER data",82,78,70,75,82,80,75,75))
ideas.append(mk("gu006","The Rural Hospital Crisis: Closures vs Population Age","Hospital closures since 2010 mapped against aging population rates","XREF","US-County","Dot map","Health","rural hospital data + Census age",88,82,72,72,88,82,72,78))
ideas.append(mk("gu007","Fracking Wells vs Earthquake Frequency by State","The correlation between injection wells and induced seismicity","XREF","US-State","Bivariate choropleth","Climate","USGS earthquake + EIA well data",78,72,68,82,78,82,78,78))
ideas.append(mk("gu008","Amazon Warehouse Locations vs Median Income by County","Where Amazon builds fulfillment centers and what it says about local wages","XREF","US-County","Dot map","Economy","Amazon locations + Census income",72,82,72,72,65,82,72,78))
ideas.append(mk("gu009","Student Debt vs Home Ownership: The Millennial Trap","States with highest student debt also have lowest young homeownership","XREF","US-State","Bivariate choropleth","Economy","Fed student loans + Census homeownership",85,92,72,78,82,78,72,78))
ideas.append(mk("gu010","Police Funding vs Crime Rates: The Defund Debate in Data","Per-capita police spending vs crime rates by major city","XREF","US-City","Scatter plot","Crime and Law Enforcement","Census gov finance + FBI UCR",82,82,72,78,85,75,72,78))

# === WORLD BIVARIATE MAPS ===
ideas.append(mk("gu011","Corruption vs Press Freedom: Where Power Hides","TI corruption scores vs RSF press freedom by country","XREF","World","Bivariate choropleth","International Statistics","TI CPI + RSF press freedom",78,72,72,72,80,82,72,85))
ideas.append(mk("gu012","Carbon Emissions vs Climate Vulnerability by Country","Who pollutes most vs who suffers most from climate change","XREF","World","Bivariate choropleth","Climate","OWID co2 + ND-GAIN vulnerability",88,78,68,80,88,82,78,82))
ideas.append(mk("gu013","Refugee Hosting vs GDP: Who Carries the Burden?","Refugees hosted per capita vs national wealth by country","XREF","World","Bivariate choropleth","International Statistics","UNHCR + world_bank GDP",82,75,72,78,82,82,72,82))
ideas.append(mk("gu014","Gender Gap vs Economic Development by Country","WEF gender scores vs GDP showing equality isnt just a rich-country thing","XREF","World","Scatter plot","International Statistics","WEF gender gap + GDP",72,72,72,75,72,78,72,82))
ideas.append(mk("gu015","Death Penalty vs Democracy Score: Execution and Authoritarianism","Which regimes still execute and what their democracy scores look like","XREF","World","Bivariate choropleth","International Statistics","Amnesty execution + OWID democracy",78,72,70,75,82,82,72,82))

# === MORE STANDALONE VIRAL ===
ideas.append(mk("gu016","The U.S. County That Contains More People Than 30 Countries","Los Angeles Countys 10M population compared to entire nations","MAP","World","Special map","Demographics","Census + world_bank population",72,80,78,85,62,80,82,90))
ideas.append(mk("gu017","Americas Youngest County vs Oldest County: Two Different Worlds","Side-by-side comparison of the youngest and oldest counties on every metric","CHART","US-County","Bar chart","Demographics","Census ACS data",75,82,75,72,68,78,72,85))
ideas.append(mk("gu018","Every U.S. County Colored by Largest Employer","Government, healthcare, retail, manufacturing - who employs your county?","MAP","US-County","County choropleth","Economy","BLS QCEW data",68,82,78,68,58,82,65,82))
ideas.append(mk("gu019","The Disappearing Middle Class: Median Income vs Cost of Living by State","Where middle-class income actually affords a middle-class life","MAP","US-State","Bivariate choropleth","Economy","Census income + BEA price parities",82,92,78,72,78,80,62,85))
ideas.append(mk("gu020","Americas Hospital Deserts: Counties With No Hospital","Rural counties without a single hospital mapped","MAP","US-County","County choropleth","Health","CMS hospital data",85,82,72,72,85,82,65,82))
ideas.append(mk("gu021","The Flood Risk Map: FEMA Zones vs Actual Flood History","Where FEMA says floods happen vs where they actually do","MAP","US","Dot map","Climate","FEMA flood zones + NWS flood data",78,82,72,78,78,85,72,82))
ideas.append(mk("gu022","Every Nuclear Power Plant in the World","Location, capacity, and age of all 440 operating nuclear reactors","MAP","World","Dot map","Climate","IAEA PRIS data",68,68,75,68,72,85,68,88))
ideas.append(mk("gu023","The World Map of Minimum Wage","Minimum wages in USD PPP-adjusted mapped by country","MAP","World","World choropleth","Economy","ILO minimum wage data",72,85,78,68,65,80,58,82))
ideas.append(mk("gu024","Americas Pharmacy Deserts: Where the Nearest Drugstore Is Miles Away","Mapping access to pharmacies at the census tract level","MAP","US","Dot map","Health","NACDS pharmacy + Census geography",78,82,72,68,72,82,68,78))
ideas.append(mk("gu025","The Insulin Price Map: What Americans Pay vs the World","U.S. insulin costs compared to every other developed nation","MAP","World","Bar chart","Health","insulin pricing data",90,88,75,78,88,75,65,82))

# === HISTORY / GEOGRAPHY FUN ===
ideas.append(mk("gu026","Countries That No Longer Exist: A Map of Dissolved Nations","Every country that has been absorbed, split, or dissolved since 1900","MAP","World","Special map","History","historical border data",68,68,72,78,62,85,80,78))
ideas.append(mk("gu027","The World Map of Landlocked Countries","44 countries with no coastline and how it affects their economy","MAP","World","World choropleth","Geography & Environment","geographic + trade data",58,65,78,72,48,82,68,88))
ideas.append(mk("gu028","Americas Ghost Towns: Abandoned Places Mapped","Locations of ghost towns and abandoned settlements across the U.S.","MAP","US","Dot map","History","ghost town registry data",72,72,68,72,62,85,78,75))
ideas.append(mk("gu029","The Trans-Atlantic Slave Trade Routes Visualized","Estimated 12.5 million people transported: routes, volumes, and destinations","MAP","World","Flow map","History","SlaveVoyages.org data",92,78,68,72,92,88,78,82))
ideas.append(mk("gu030","Every Country Flag Mapped to Its Country","Flags pinned to their countries showing regional design patterns","MAP","World","Special map","International Statistics","flag + country data",50,65,78,58,38,88,62,92))

# === SPORTS DEEP DIVES ===
ideas.append(mk("gu031","Americas Football vs Soccer: Where Each Sport Dominates","NFL viewership vs MLS attendance per capita by metro area","XREF","US-Metro","Bivariate choropleth","Sports & Recreation","Nielsen + MLS data",65,82,72,68,55,78,68,75))
ideas.append(mk("gu032","Olympic Medal Count vs Population: The Overachievers","Which countries win the most medals relative to their population","MAP","World","World choropleth","Sports & Recreation","IOC medal + population data",68,78,78,78,58,80,72,88))
ideas.append(mk("gu033","The Marathon Map: Average Finish Times by City","How fast runners complete marathons in different cities","MAP","World","Dot map","Sports & Recreation","marathon results data",58,72,72,65,48,78,68,78))

# === TECH / DIGITAL ===
ideas.append(mk("gu034","Americas Data Center Map: Where the Internet Lives","Physical locations of major data centers across the U.S.","MAP","US","Dot map","Science & Technology","data center location data",65,72,75,72,58,85,72,82))
ideas.append(mk("gu035","The Electric Vehicle Map: EV Registration by State","Share of new vehicles that are electric by state","MAP","US-State","State choropleth","Transportation","DOE AFDC EV data",68,82,78,65,58,78,58,85))
ideas.append(mk("gu036","Cell Tower Density by County: The Connectivity Map","Where America has the most and fewest cell towers per area","MAP","US-County","County choropleth","Science & Technology","FCC cell tower data",62,78,75,65,52,82,62,82))

# === HOUSING DEEP DIVES ===
ideas.append(mk("gu037","Americas Rental vs Ownership Map by County","Renter-occupied vs owner-occupied housing at the county level","MAP","US-County","County choropleth","Housing","Census ACS tenure data",68,85,78,62,58,82,55,88))
ideas.append(mk("gu038","The Vacant Housing Map: Empty Homes Across America","Vacancy rates by county - some places have more empty homes than occupied","MAP","US-County","County choropleth","Housing","Census ACS vacancy data",72,78,72,72,68,82,68,85))
ideas.append(mk("gu039","Mobile Home America: Where Manufactured Housing Dominates","Share of housing that is mobile/manufactured homes by county","MAP","US-County","County choropleth","Housing","Census ACS housing type",65,78,75,68,58,82,65,85))
ideas.append(mk("gu040","The McMansion Belt: Median Home Size by Region","Average square footage of new homes by state and metro area","MAP","US-State","State choropleth","Housing","Census new construction data",62,82,75,68,52,78,62,82))

print(f"BATCH_GU: {len(ideas)} ideas generated")

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
    print("[BATCH_GU] ERROR: tail marker not found"); sys.exit(1)
raw = raw.replace(tail, "")
for idea in new_ideas:
    raw += idea + ",\n"
raw += tail + "\n"
with open(DATA_JS, "w", encoding="utf-8") as f:
    f.write(raw)
print(f"[BATCH_GU] Injected {len(new_ideas)} new ideas (skipped {skipped} dupes)")
