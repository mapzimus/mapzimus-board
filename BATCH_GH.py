"""
BATCH_GH.py — Regional gap-fill (Europe, Oceania) + GIS spatial + bivariate choropleth
Gap targets: europe (181), oceania (2!), bivariate choropleth (83), dot map (38)
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
# EUROPE-FOCUSED
# ============================================================
ideas.append(mk("eu_languages_map","Europes Linguistic Map","Most widely spoken language by country and region","MAP","europe","Special map","Demographics","Eurobarometer + Ethnologue https://ec.europa.eu/eurobarometer/",50,55,80,55,30,85,55,90))
ideas.append(mk("eu_youth_unemployment","Youth Unemployment Across Europe","Under-25 unemployment rate ranges from 6% to 30% across EU","MAP","europe","Special map","Labor","Eurostat https://ec.europa.eu/eurostat",70,65,80,55,60,80,45,95))
ideas.append(mk("eu_population_decline_map","Europe Is Shrinking","Countries with declining populations across the continent","MAP","europe","Special map","Demographics","Eurostat + OWID https://ec.europa.eu/eurostat",65,60,80,65,55,80,50,95))
ideas.append(mk("eu_housing_prices_map","European Housing Prices Have Doubled Since 2010","House price index changes across European countries","MAP","europe","Special map","Economy","Eurostat House Price Index https://ec.europa.eu/eurostat",70,75,80,55,60,80,50,95))
ideas.append(mk("eu_rail_network_density","Europes Rail Networks Vary Enormously","Railway line density by country in Europe","MAP","europe","Special map","Transportation","Eurostat + UIC Railway Statistics https://uic.org",45,50,80,55,30,80,55,90))
ideas.append(mk("eu_renewable_energy_share","Europes Renewable Energy Leaders","Share of energy from renewables by European country","MAP","europe","Special map","Environment","Eurostat Energy Statistics https://ec.europa.eu/eurostat",55,55,80,55,45,80,45,95))
ideas.append(mk("eu_immigration_origin_map","Where Europes Immigrants Come From","Top country of origin for foreign-born residents in each EU nation","MAP","europe","Special map","Demographics","Eurostat Migration Statistics https://ec.europa.eu/eurostat",60,60,80,65,65,80,55,90))
ideas.append(mk("eu_beer_wine_divide","Europes Beer-Wine Divide","Per capita consumption of beer vs wine shows a clear geographic split","MAP","europe","Bivariate choropleth","Food & Nutrition","WHO + Eurostat + OWID alcohol data https://www.who.int",50,65,80,65,30,85,60,90))

# ============================================================
# OCEANIA gap-fill (only 2 ideas!!!)
# ============================================================
ideas.append(mk("oceania_indigenous_population","Indigenous Population Share Across Oceania","Aboriginal and Torres Strait Islander and Maori population shares","MAP","oceania","Special map","Demographics","ABS + Stats NZ https://www.abs.gov.au + https://www.stats.govt.nz",65,50,80,55,55,80,60,85))
ideas.append(mk("oceania_remoteness_map","The Most Remote Inhabited Places on Earth","Distance to nearest city of 50000 for Pacific Island nations","MAP","oceania","Special map","Geography & Environment","UNDP + geographic calculations https://www.undp.org",45,40,75,80,30,80,80,80))
ideas.append(mk("oceania_sea_level_threat","Pacific Islands That Will Disappear","Island nations most threatened by sea level rise","MAP","oceania","Special map","Climate","Pacific Climate Change Portal + IPCC https://www.pacificclimatechangescience.org",80,50,80,70,80,80,65,85))
ideas.append(mk("oceania_australia_population_density","Australias Population Clings to the Coast","97% of Australians live on 3% of the land","MAP","oceania","Dot map","Demographics","ABS Census https://www.abs.gov.au",55,55,80,70,30,85,60,90))
ideas.append(mk("oceania_coral_reef_bleaching","The Great Barrier Reef Is Dying","Mass coral bleaching events by year 1998-2025","CHART","oceania","Bar chart","Environment","GBRMPA + NOAA Coral Reef Watch https://www.gbrmpa.gov.au",80,55,80,60,80,60,55,90))
ideas.append(mk("oceania_nz_vs_aus_comparison","New Zealand vs Australia by the Numbers","Side-by-side comparison of key indicators for the two neighbors","CHART","oceania","Bar chart","Economy","World Bank + ABS + Stats NZ https://data.worldbank.org",45,55,80,55,30,60,55,90))

# ============================================================
# BIVARIATE CHOROPLETH gap-fill (high visual impact, +2 format bonus)
# ============================================================
ideas.append(mk("biv_income_vs_education","Income vs Education Level by County","Median income vs college degree rate reveals Americas class geography","XREF","us_county","Bivariate choropleth","Economy","Census ACS https://data.census.gov",65,75,80,55,50,85,55,95))
ideas.append(mk("biv_age_vs_income","Age vs Income by County","Median age vs median income shows retirement vs working communities","XREF","us_county","Bivariate choropleth","Demographics","Census ACS https://data.census.gov",55,65,80,55,35,85,55,95))
ideas.append(mk("biv_obesity_vs_poverty","Obesity vs Poverty by State","Obesity rate vs poverty rate shows a troubling correlation","XREF","us_state","Bivariate choropleth","Health","CDC BRFSS + Census ACS https://www.cdc.gov/brfss/ + https://data.census.gov",70,80,80,55,55,85,55,95))
ideas.append(mk("biv_internet_vs_income_county","Internet Access vs Income by County","Broadband access vs household income - digital divide mapped","XREF","us_county","Bivariate choropleth","Science & Technology","FCC + Census ACS https://broadbandmap.fcc.gov + https://data.census.gov",65,75,80,55,50,85,55,95))
ideas.append(mk("biv_election_vs_education","Trump Vote vs College Education by County","2024 vote share vs bachelors degree rate","XREF","us_county","Bivariate choropleth","Elections","MIT Election Lab + Census ACS https://electionlab.mit.edu + https://data.census.gov",70,75,80,60,80,85,55,95))
ideas.append(mk("biv_crime_vs_unemployment","Crime vs Unemployment by County","Violent crime rate vs unemployment rate","XREF","us_county","Bivariate choropleth","Crime and Law Enforcement","FBI UCR + BLS LAUS https://cde.ucr.cjis.gov + https://www.bls.gov/lau/",65,65,80,60,60,85,55,90))
ideas.append(mk("biv_population_change_vs_housing","Population Growth vs Housing Cost by County","Counties growing fastest also have skyrocketing housing costs","XREF","us_county","Bivariate choropleth","Housing","Census ACS + Zillow ZHVI https://data.census.gov + https://www.zillow.com/research/",65,75,80,55,50,85,55,85))
ideas.append(mk("biv_life_expectancy_vs_income","Life Expectancy vs Income by County","The rich live a decade longer than the poor by county","XREF","us_county","Bivariate choropleth","Health","CDC USALEEP + Census ACS https://www.cdc.gov/nchs/nvss/usaleep/ + https://data.census.gov",80,80,80,60,70,85,55,90))
ideas.append(mk("biv_electric_vs_gas_cars","Electric vs Gas Car Registration by State","EV adoption rate vs average gas price by state","XREF","us_state","Bivariate choropleth","Transportation","DOE AFDC + EIA Gas Prices https://afdc.energy.gov + https://www.eia.gov",55,70,80,60,40,85,60,85))
ideas.append(mk("biv_farm_income_vs_farm_size","Farm Income vs Farm Size by County","Average farm revenue vs average acreage shows industrialization pattern","XREF","us_county","Bivariate choropleth","Food & Nutrition","USDA Census of Agriculture https://www.nass.usda.gov/",45,50,75,60,35,85,60,85))
ideas.append(mk("biv_military_vs_civilian_jobs","Military vs Civilian Employment by County","Military employment share vs civilian unemployment rate","XREF","us_county","Bivariate choropleth","Labor","BLS QCEW + DOD https://www.bls.gov/cew/ + https://www.defense.gov",50,55,75,60,45,85,60,85))
ideas.append(mk("biv_immigrant_share_vs_gdp_world","Immigration vs GDP by Country","Immigrant share of population vs GDP per capita worldwide","XREF","worldwide","Scatter plot","Demographics","UN DESA Migration Stock + World Bank GDP https://www.un.org/development/desa/pd/ + https://data.worldbank.org",55,55,75,65,50,60,60,90))

# ============================================================
# DOT MAP gap-fill (high visual, +2 format bonus)
# ============================================================
ideas.append(mk("dot_every_fire_station","Every Fire Station in America","17000+ fire stations plotted on the map","MAP","us_national","Dot map","Geography & Environment","HIFLD Fire Stations https://hifld-geoplatform.opendata.arcgis.com",40,55,80,45,25,90,50,95))
ideas.append(mk("dot_every_hospital","Every Hospital in America","6000+ hospitals mapped by type and bed count","MAP","us_national","Dot map","Health","HIFLD Hospitals https://hifld-geoplatform.opendata.arcgis.com",55,70,80,45,35,90,45,95))
ideas.append(mk("dot_every_military_base","Every US Military Installation Worldwide","800+ military bases across the globe","MAP","worldwide","Dot map","History","DOD Base Structure Report https://www.acq.osd.mil/eie/bsr.html",55,50,80,65,55,90,60,90))
ideas.append(mk("dot_every_brewery","Every Brewery in America","9000+ craft breweries mapped","MAP","us_national","Dot map","Food & Nutrition","Brewers Association https://www.brewersassociation.org",45,70,80,45,25,90,50,90))
ideas.append(mk("dot_every_national_park","Every National Park Unit in the US","423 National Park Service units mapped by type","MAP","us_national","Dot map","Environment","NPS https://www.nps.gov",50,65,85,45,25,90,45,95))
ideas.append(mk("dot_every_earthquake","Every Earthquake Above 5.0 in the Last 50 Years","Seismic activity mapped worldwide","MAP","worldwide","Dot map","Geography & Environment","USGS Earthquake Catalog https://earthquake.usgs.gov/earthquakes/search/",55,50,80,55,40,90,55,95))
ideas.append(mk("dot_every_active_volcano","Every Active Volcano on Earth","Mapping the Ring of Fire and beyond","MAP","worldwide","Dot map","Geography & Environment","Smithsonian GVP https://volcano.si.edu",50,45,80,55,40,90,60,95))
ideas.append(mk("dot_every_airport","Every Airport in the World","40000+ airports mapped by traffic volume","MAP","worldwide","Dot map","Transportation","OurAirports + ICAO data https://ourairports.com",40,50,80,45,25,90,50,95))
ideas.append(mk("dot_every_mass_shooting","Every Mass Shooting in America Since 2013","Gun Violence Archive mass shooting incidents mapped","MAP","us_national","Dot map","Crime and Law Enforcement","Gun Violence Archive https://www.gunviolencearchive.org",90,80,80,50,90,90,45,95))
ideas.append(mk("dot_every_superfund_site","Every Superfund Toxic Waste Site in America","1300+ EPA Superfund sites mapped","MAP","us_national","Dot map","Environment","EPA Superfund https://www.epa.gov/superfund/search-superfund-sites",70,65,80,55,65,90,55,95))
ideas.append(mk("dot_every_mcdonalds_worldwide","Every McDonalds on Earth","40000 locations in 100+ countries","MAP","worldwide","Dot map","Food & Nutrition","McDonalds store locator data https://www.mcdonalds.com",40,70,80,55,25,90,55,85))
ideas.append(mk("dot_lightning_strikes_map","Where Lightning Strikes Most Often","Lightning flash density worldwide","MAP","worldwide","Dot map","Climate","NASA LIS/OTD + NOAA NLDN https://lightning.nsstc.nasa.gov",45,45,80,65,30,90,60,90))


# ============================================================
# INJECTION LOGIC
# ============================================================
print(f"[BATCH_GH] {len(ideas)} ideas ready")

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
    print("[BATCH_GH] ERROR: tail marker not found in data.js")
    sys.exit(1)

raw = raw.replace(tail, "")
for idea in new_ideas:
    raw += idea + ",\n"
raw += tail + "\n"

with open(DATA_JS, "w", encoding="utf-8") as f:
    f.write(raw)

print(f"[BATCH_GH] Injected {len(new_ideas)} new ideas ({skipped} dupes skipped)")
