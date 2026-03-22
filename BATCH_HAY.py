"""BATCH HAY: Niche/underserved topics + Reddit-bait correlation maps.
Targeting sections with the fewest ideas to fill gaps.
All sc values on 0-100 scale."""
import re, os

DATA = os.path.join(os.path.dirname(__file__), 'data.js')

def mk(id,title,sub,typ,geo,fmt,sect,tbl,e,r,c,s,t,v,o,dr):
    raw=e*2+r*2+c*1.25+s*1.5+t*1.5+v*2.0+o*1.5
    vs=int((raw/11.75)*(1-0.5*(1-dr/100)))
    return ('{id:"'+id+'",title:"'+title+'",sub:"'+sub+'",type:"'+typ+'",'
            'geo:"'+geo+'",fmt:"'+fmt+'",section:"'+sect+'",tbl:"'+tbl+'",'
            'sc:{emotional:'+str(e)+',relatability:'+str(r)+',clarity:'+str(c)
            +',surprise:'+str(s)+',tension:'+str(t)+',visual:'+str(v)
            +',originality:'+str(o)+',data_ready:'+str(dr)+'}'
            ',vs:'+str(vs)+',topics:[],ext:[],status:"idea",notes:""}')

MAP="MAP"; CHART="CHART"; XREF="XREF"; RANK="RANK"
ideas = []

# ── Reddit r/dataisbeautiful bait ──
ideas.append(mk("hay001","Every Country Redrawn With Straight Line Borders","What if colonial borders followed latitudes and longitudes","MAP","World","Special map","Geography & Environment","Natural Earth + hypothetical boundary calculation (naturalearthdata.com)",40,50,50,90,35,95,95,85))
ideas.append(mk("hay002","The Most Common Street Name in Every State","#1 street name (Main, Oak, Elm, etc) by state","MAP","US States","State choropleth","Geography & Environment","Census: TIGER/Line road files (census.gov/geo)",45,65,60,80,30,80,85,90))
ideas.append(mk("hay003","How Many People Share Your Birthday in the US","Daily birth frequency heat calendar for the US","CHART","US","Heatmap calendar","Demographics","CDC NCHS: Birth data by day of year (cdc.gov)",50,80,65,70,30,80,75,90))
ideas.append(mk("hay004","The Most Photographed Places on Earth From Geotagged Photos","Density of geotagged Flickr/Instagram photos worldwide","MAP","World","Dot map","Entertainment","Flickr API + academic: Geotagged photo density (flickr.com)",50,60,55,75,35,90,80,75))
ideas.append(mk("hay005","Your States Shape Rotated to Look Like Something Else","Each US state rotated to reveal pareidolia shapes","MAP","US States","Special map","Geography & Environment","Census: TIGER/Line + creative rotation (census.gov/geo)",35,65,40,90,25,90,95,85))

# ── Water and Oceans ──
ideas.append(mk("hay006","Every River in the US Colored by the Ocean It Flows Into","Atlantic vs Pacific vs Gulf watershed map","MAP","US","Special map","Geography & Environment","USGS: NHDPlus watershed boundaries (usgs.gov)",50,55,60,80,40,95,80,90))
ideas.append(mk("hay007","The Deepest Lakes in Every Continent","Maximum depth of top 3 deepest lakes per continent","CHART","World","Bar chart","Geography & Environment","ILEC: World Lake Database (ilec.or.jp)",40,45,60,75,35,75,75,85))
ideas.append(mk("hay008","Countries Drawing Down Their Groundwater Faster Than Rain Can Refill It","Water stress: groundwater withdrawal vs recharge rate by country","MAP","World","World choropleth","Geography & Environment","WRI: Aqueduct Water Risk Atlas (wri.org)",75,60,65,80,80,80,80,85))
ideas.append(mk("hay009","The Shipping Routes That Move 80% of Global Trade","Major shipping lane volume visualized as glowing flow lines","MAP","World","Line map","Economy","UNCTAD: Maritime transport review (unctad.org)",60,55,65,75,55,90,75,80))
ideas.append(mk("hay010","How Much of Each Country Is Desert vs Forest vs Farmland","Land use breakdown as stacked bars for every country","CHART","World","Bar chart","Geography & Environment","FAO: Land use statistics (fao.org)",50,55,65,70,40,75,70,90))

# ── Language and Culture ──
ideas.append(mk("hay011","The Most Spoken Language in Every US County That Isnt English or Spanish","Third most spoken language by county","MAP","US Counties","County choropleth","Demographics","ACS: Language spoken at home by county (census.gov)",60,70,65,85,45,85,85,90))
ideas.append(mk("hay012","How Many Languages Are Dying: Endangered Languages by Region","Number of endangered languages by UN region","MAP","World","World choropleth","International Statistics","UNESCO: Atlas of the Worlds Languages in Danger (unesco.org)",65,55,60,80,70,75,80,80))
ideas.append(mk("hay013","The Countries Where English Isnt Official but Everyone Speaks It","English proficiency index vs official language status","MAP","World","World choropleth","International Statistics","EF: English Proficiency Index (ef.com/epi)",55,65,65,80,40,75,80,85))

# ── Borders and Geopolitics ──
ideas.append(mk("hay014","Every Border Dispute in the World Right Now","Active territorial disputes mapped by parties and status","MAP","World","Special map","International Statistics","CIA World Factbook: Disputes + academic sources (cia.gov)",65,55,60,80,75,85,75,80))
ideas.append(mk("hay015","Countries That Dont Recognize Each Other","Non-recognition relationships mapped as network graph","CHART","World","Special map","International Statistics","UN voting records + diplomatic databases (un.org)",55,50,55,90,65,80,90,75))
ideas.append(mk("hay016","The Worlds Shortest and Longest International Borders","Top and bottom 20 international borders by length","RANK","World","Bar chart","Geography & Environment","CIA World Factbook: Land boundaries (cia.gov)",40,45,60,80,30,65,80,90))

# ── Animals and Nature ──
ideas.append(mk("hay017","The Migration Paths of Every Whale Species","Combined whale migration routes by species overlaid on ocean map","MAP","World","Line map","Geography & Environment","NOAA: Marine mammal tracking data (fisheries.noaa.gov)",50,50,55,75,45,90,80,70))
ideas.append(mk("hay018","The Most Biodiverse Square Mile on Every Continent","Location of highest species density per continent","MAP","World","Dot map","Geography & Environment","GBIF: Species occurrence data (gbif.org)",50,45,55,80,45,80,80,75))
ideas.append(mk("hay019","Invasive Species Are Costing the US $20 Billion Per Year","Economic cost of top 20 invasive species in the US","CHART","US","Bar chart","Geography & Environment","USDA APHIS: Invasive species economic impact (aphis.usda.gov)",60,55,65,75,65,65,75,75))

# ── Time Zones and Daylight ──
ideas.append(mk("hay020","Countries Where the Sun Sets Before 4PM in Winter","Latest sunset time on December 21 for every country capital","MAP","World","World choropleth","Geography & Environment","Astronomical calculation + capital coordinates (timeanddate.com)",50,65,55,80,40,80,80,90))
ideas.append(mk("hay021","The Daylight Savings Divide: Countries That Still Do It vs Those That Quit","Current DST status for every country with recent changes highlighted","MAP","World","World choropleth","International Statistics","TimeAndDate: DST rules (timeanddate.com)",45,65,60,75,40,80,75,90))
ideas.append(mk("hay022","The Ideal Time Zone: Places Where Solar Noon Is Actually Noon","Offset between solar noon and clock noon for every major city","MAP","World","Dot map","Geography & Environment","Astronomical calculation + time zone data (timeanddate.com)",40,50,55,85,30,75,90,85))

# ── Obscure but Fascinating ──
ideas.append(mk("hay023","Countries Where You Drive on the Left vs Right Overlaid With Former Colonial Power","Driving side colored by which empire imposed it","MAP","World","World choropleth","History","Various: Driving side + colonial history (general)",45,55,55,85,35,80,85,90))
ideas.append(mk("hay024","The Most Remote Inhabited Place in Every Country","Settlement furthest from any city over 50k population, per country","MAP","World","Dot map","Geography & Environment","GeoNames + population data (geonames.org)",45,50,50,85,35,80,90,75))
ideas.append(mk("hay025","Every Countries National Dish Mapped","National dish or most iconic food by country","MAP","World","World choropleth","Food & Nutrition","TasteAtlas + cultural food databases (tasteatlas.com)",50,70,55,70,30,80,75,70))
ideas.append(mk("hay026","The Most Cluttered Orbit: Space Debris Density by Altitude","Known space debris objects by orbital altitude band","CHART","World","Bar chart","Science & Technology","ESA: Space Debris Office (esa.int/spacedebris)",55,45,60,80,55,75,80,85))
ideas.append(mk("hay027","How Many Time Zones Does Each Country Have?","Countries ranked by number of time zones, France #1 with 12","RANK","World","Bar chart","Geography & Environment","IANA: Time zone database (iana.org)",40,50,60,85,30,65,80,90))
ideas.append(mk("hay028","The Worlds Busiest Air Routes You Never Heard Of","Top 20 passenger routes globally, mostly intra-Asia","RANK","World","Bar chart","Transportation","OAG: Aviation analytics (oag.com)",50,55,60,80,40,65,80,80))

# ── Cross-refs nobody thought of ──
ideas.append(mk("hay029","Countries Where People Drink the Most Tea Also Have the Longest Life Expectancy","Per capita tea consumption vs life expectancy","XREF","World","Scatter plot","Health","FAO: Tea consumption + World Bank: Life expectancy (fao.org + worldbank.org)",50,65,55,85,40,55,85,85))
ideas.append(mk("hay030","The Taller the Country the Richer It Is","Average adult male height vs GDP per capita by country","XREF","World","Scatter plot","Health","NCD-RisC: Height data + World Bank: GDP per capita (ncdrisc.org + worldbank.org)",45,55,55,85,35,55,85,85))
ideas.append(mk("hay031","Countries With the Most Nobel Prizes Per Capita Are Also the Happiest","Nobel laureates per million vs World Happiness Score","XREF","World","Scatter plot","Science & Technology","Nobel Foundation + WHR: Happiness score (nobelprize.org + worldhappiness.report)",45,50,55,85,35,55,85,85))
ideas.append(mk("hay032","Forest Cover Predicts Happiness Better Than GDP","Forest area % vs happiness score controlling for income","XREF","World","Scatter plot","Geography & Environment","World Bank: Forest area + WHR: Happiness (worldbank.org + worldhappiness.report)",50,55,50,90,45,55,90,80))
ideas.append(mk("hay033","The Wider the Streets the Fatter the City","Average road width vs obesity rate for 100 largest US cities","XREF","US Metro","Scatter plot","Health","DOT: Highway Performance + CDC: BRFSS obesity (fhwa.dot.gov + cdc.gov)",45,55,50,95,40,55,95,60))
ideas.append(mk("hay034","States With the Most Tornadoes Have the Cheapest Housing","Annual tornado count vs median home price by state","XREF","US States","Scatter plot","Housing","NOAA SPC: Tornado count + Zillow: ZHVI (spc.noaa.gov + zillow.com)",55,65,60,85,55,60,85,90))
ideas.append(mk("hay035","Countries Where People Walk the Most Weigh the Least","Average daily steps vs obesity rate by country","XREF","World","Scatter plot","Health","Stanford: Smartphone step data + WHO: Obesity (nature.com + who.int)",60,70,60,80,50,55,80,75))

# Injection
with open(DATA, 'r', encoding='utf-8') as f:
    text = f.read()
existing_ids = set(re.findall(r'id:"([^"]*)"', text))
new_ideas = [idea for idea in ideas if re.search(r'id:"([^"]*)"', idea).group(1) not in existing_ids]
if not new_ideas:
    print("All ideas already exist.")
else:
    tail = ']; // end D'
    pos = text.rfind(tail)
    inject = '\n,'.join(new_ideas)
    text = text[:pos] + ',\n' + inject + '\n' + tail
    with open(DATA, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f"Injected {len(new_ideas)} new ideas (HAY batch)")
