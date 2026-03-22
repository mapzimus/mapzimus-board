"""BATCH HAT: Fun/shareable cross-refs - the maps people share with friends
because they're surprising, funny, or 'wow I never thought about that'.
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

# ── Geographic Weirdness ──
ideas.append(mk("hat001","States Where More People Are Killed by Cows Than Sharks","Cow-related fatalities vs shark fatalities by coastal state","CHART","US States","Bar chart","Geography & Environment","CDC WONDER: Animal-related fatalities + ISAF: Shark attack file (wonder.cdc.gov + floridamuseum.ufl.edu)",60,75,65,95,50,65,95,75))
ideas.append(mk("hat002","The Farthest You Can Get From a McDonalds in Every State","Maximum distance to nearest McDonalds by state in miles","MAP","US States","State choropleth","Food & Nutrition","McDonalds: Store locator + Geographic calculation (mcdonalds.com)",55,75,65,85,40,80,90,80))
ideas.append(mk("hat003","Countries Shaped Most Like Other Countries","Hausdorff distance similarity matrix for 193 country outlines","CHART","World","Scatter plot","Geography & Environment","Natural Earth: Country boundaries (naturalearthdata.com)",40,50,55,90,30,80,95,90))
ideas.append(mk("hat004","US Counties Named After Presidents vs Their Current Political Leaning","County named after which president vs 2024 vote margin","MAP","US Counties","Dot map","Elections","USGS GNIS: Place names + MIT Election Lab: 2024 results (gnis.usgs.gov + electionlab.mit.edu)",50,60,60,90,50,80,95,85))
ideas.append(mk("hat005","The Longest Straight-Line Drive You Can Take in Every State","Maximum straight-line distance within each state boundary","MAP","US States","State choropleth","Geography & Environment","Census: TIGER/Line state boundaries (census.gov/geo)",40,55,60,85,30,85,90,90))

# ── Food Fun ──
ideas.append(mk("hat006","States That Prefer Coke vs Pepsi vs Dr Pepper","Dominant soft drink brand by state from purchasing data","MAP","US States","State choropleth","Food & Nutrition","IRI/Nielsen: Beverage market share by DMA (iri.com)",60,85,70,75,45,80,80,65))
ideas.append(mk("hat007","The Real Pizza Belt: Counties Where Pizza Restaurants Outnumber All Other Types","Pizza shop share of total restaurants by county","MAP","US Counties","County choropleth","Food & Nutrition","Census: County Business Patterns NAICS 722513 (census.gov)",60,80,65,80,40,80,85,85))
ideas.append(mk("hat008","Countries Where People Spend More on Alcohol Than Education","Alcohol expenditure vs education expenditure as % of household spending","XREF","World","Bar chart","Food & Nutrition","OECD: Household expenditure by category (oecd.org)",70,75,70,85,65,65,85,85))
ideas.append(mk("hat009","The Pumpkin Spice Line: The Latitude Where Pumpkin Spice Lattes Sell Best","Starbucks PSL relative sales volume by latitude band","CHART","US","Line chart","Food & Nutrition","Market research: Seasonal beverage sales by region (general)",55,80,60,85,35,70,95,50))
ideas.append(mk("hat010","How Far Your States Signature Dish Travels to Reach You","Average food miles for each states iconic dish ingredients","MAP","US States","State choropleth","Food & Nutrition","USDA: Food supply chain + state food associations (usda.gov)",55,75,60,80,50,75,90,55))


# ── Sports Surprises ──
ideas.append(mk("hat011","NFL Teams With the Worst Records Draw Bigger Crowds Than Winning NBA Teams","Average attendance of bottom 10 NFL teams vs top 10 NBA teams","CHART","US","Bar chart","Sports & Recreation","ESPN: Attendance data NFL + NBA (espn.com)",55,70,70,85,45,65,85,80))
ideas.append(mk("hat012","The Country That Invented Each Sport vs Who Dominates It Now","Sport origin country vs current #1 ranked country for 30 major sports","CHART","World","Bar chart","Sports & Recreation","World federation rankings + historical records (various)",55,65,65,85,45,70,90,75))
ideas.append(mk("hat013","States Where High School Football Attendance Rivals College","Average HS football game attendance vs college game attendance by state","XREF","US States","State choropleth","Sports & Recreation","NFHS: HS participation + NCAA: Attendance (nfhs.org + ncaa.org)",55,70,65,80,45,70,85,70))

# ── Money Weirdness ──
ideas.append(mk("hat014","The States Where a Dollar Goes the Farthest vs Where It Barely Buys Lunch","Regional Price Parities - $100 purchasing power by state","MAP","US States","State choropleth","Economy","BEA: Regional Price Parities (bea.gov)",75,90,80,70,65,80,70,95))
ideas.append(mk("hat015","Countries Where the Average Worker Earns Less Than an American Teenager","GDP per capita vs US teen median wage for 100+ countries","CHART","World","Bar chart","Economy","World Bank: GDP per capita + BLS: Youth wage data (worldbank.org + bls.gov)",70,70,70,85,75,65,85,85))
ideas.append(mk("hat016","How Many Big Macs Could Ancient Currency Buy?","Purchasing power of historical wages translated to Big Mac equivalents","CHART","World","Bar chart","Economy","Economist: Big Mac Index + historical wage data (economist.com)",55,70,60,90,40,60,95,60))
ideas.append(mk("hat017","Every US State as a Country: GDP Comparison","Each US state matched to the country with the closest GDP","MAP","US States","State choropleth","Economy","BEA: State GDP + World Bank: Country GDP (bea.gov + worldbank.org)",65,80,75,80,50,85,75,90))

# ── Nature and Animals ──
ideas.append(mk("hat018","The Most Dangerous Animal in Every State","Animal causing most human fatalities by state","MAP","US States","State choropleth","Geography & Environment","CDC WONDER: Animal-related fatalities by state (wonder.cdc.gov)",65,75,65,80,60,80,80,75))
ideas.append(mk("hat019","Countries Where Stray Dogs Outnumber Registered Pets","Estimated stray dog population vs registered pet dogs by country","CHART","World","Bar chart","Geography & Environment","WSPA: Stray animal census + Euromonitor: Pet ownership (icam-coalition.org)",55,60,55,85,50,60,90,60))
ideas.append(mk("hat020","The Bear-Human Encounter Line: Counties Where Bear Sightings Are Increasing Fastest","Year-over-year change in bear encounter reports by county","MAP","US Counties","County choropleth","Geography & Environment","State wildlife agencies: Bear report data (various state DNR)",60,65,55,80,60,80,85,55))

# ── Time and Patterns ──
ideas.append(mk("hat021","The Best Day of the Week to Be Born for Lifetime Earnings","Average lifetime earnings by day of week of birth","CHART","US","Bar chart","Demographics","SSA: Birth data + Census: Lifetime earnings (ssa.gov + census.gov)",50,70,55,95,40,55,95,55))
ideas.append(mk("hat022","States Where People Go to Bed the Earliest vs Latest","Average bedtime by state from fitness tracker data","MAP","US States","State choropleth","Health","Fitbit/CDC: Sleep data by state (cdc.gov/sleep)",60,80,65,75,40,75,80,65))
ideas.append(mk("hat023","The Monday Effect: Stock Markets Drop More on Mondays in Every Country","Average daily return by day of week for 40 stock exchanges","CHART","World","Bar chart","Economy","Yahoo Finance: Historical daily returns by exchange (finance.yahoo.com)",55,65,65,80,50,65,80,85))


# ── Unexpected Correlations (conversation starters) ──
ideas.append(mk("hat024","States With More Craft Breweries Per Capita Vote More Democratic","Craft brewery density vs Democratic vote share by state","XREF","US States","Scatter plot","Elections","Brewers Association: Craft brewery count + MIT Election Lab (brewersassociation.org + electionlab.mit.edu)",55,70,60,90,55,65,90,85))
ideas.append(mk("hat025","Countries That Consume the Most Cheese Also Win the Most Nobel Prizes","Per capita cheese consumption vs Nobel laureates per capita","XREF","World","Scatter plot","Science & Technology","FAO: Cheese consumption + Nobel Foundation (fao.org + nobelprize.org)",40,55,50,95,30,55,95,85))
ideas.append(mk("hat026","The Divorce Rate Correlates With Margarine Consumption","US divorce rate vs per capita margarine consumption 1999-2024","CHART","US","Line chart","Demographics","CDC: Marriage/divorce + USDA: Margarine consumption (cdc.gov + usda.gov)",40,60,50,95,30,60,95,80))
ideas.append(mk("hat027","States Where People Google Why Is My vs Why Does My","Google search interest for existential vs practical questions by state","MAP","US States","State choropleth","Science & Technology","Google Trends: Relative search volume (trends.google.com)",50,70,55,90,40,70,95,75))
ideas.append(mk("hat028","Countries Where Internet Speed Predicts Life Satisfaction","Average download speed vs life satisfaction score","XREF","World","Scatter plot","Science & Technology","Speedtest: Global Index + Gallup: World Poll life satisfaction (speedtest.net + gallup.com)",55,65,60,80,45,60,85,85))

# ── Map Porn Favorites (high visual, highly shareable) ──
ideas.append(mk("hat029","Every Country Scaled by Population Instead of Land Area","Cartogram where each country is sized by population","MAP","World","Special map","Demographics","UN DESA: World Population Prospects (population.un.org)",70,65,70,80,50,95,75,90))
ideas.append(mk("hat030","What America Looks Like if Every County Was the Same Population","Equal-population county cartogram of the US","MAP","US Counties","Special map","Demographics","ACS: County population (census.gov)",60,65,65,85,45,95,85,90))
ideas.append(mk("hat031","The True Size of Africa: Countries That Fit Inside It","Africa overlay showing US, China, India, Europe, Japan fitting inside","MAP","World","Special map","Geography & Environment","Natural Earth: Country boundaries + area calculations (naturalearthdata.com)",65,60,70,85,50,95,80,90))
ideas.append(mk("hat032","Drive Time From the Geographic Center of Every State to the Nearest Costco","Isochrone map from each states centroid to nearest Costco","MAP","US States","Special map","Economy","Costco: Store locator + OSRM: Drive time routing (costco.com + router.project-osrm.org)",50,70,60,85,35,90,90,80))
ideas.append(mk("hat033","The World Split in Half by Population","Line dividing the world where 50% of humanity lives on each side","MAP","World","Special map","Demographics","GPW: Gridded Population of the World (sedac.ciesin.columbia.edu)",65,65,65,90,45,95,85,90))
ideas.append(mk("hat034","Every US Highway With More Fatalities Per Mile Than a War Zone","Highway segments where fatality rate exceeds active conflict zones","MAP","US","Line map","Transportation","NHTSA: FARS + Armed Conflict Location Data (nhtsa.gov + acleddata.com)",75,75,65,90,80,85,90,75))
ideas.append(mk("hat035","The World at Night: Light Pollution From Space Colored by GDP","VIIRS nighttime lights with GDP per capita color overlay","MAP","World","Special map","Geography & Environment","NASA: VIIRS + World Bank: GDP (earthobservatory.nasa.gov + worldbank.org)",60,55,60,80,50,95,80,85))

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
    print(f"Injected {len(new_ideas)} new ideas (HAT batch)")
