"""BATCH HAV: More deep cross-refs targeting untapped section pairs.
Elections x Economy, Labor x Housing, Energy x Health, Agriculture x Climate.
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

# ── Elections x Economy ──
ideas.append(mk("hav001","How Gas Prices on Election Day Predict the Incumbents Margin","Average gas price in October vs incumbent party vote share for every presidential election since 1976","XREF","US","Scatter plot","Elections","EIA: Gas prices + MIT Election Lab: Presidential results (eia.gov + electionlab.mit.edu)",75,80,70,85,70,65,85,90))
ideas.append(mk("hav002","The Counties That Flipped in 2024 Had the Fastest Rising Grocery Bills","CPI food-at-home change vs 2020-to-2024 vote swing by county","XREF","US Counties","Scatter plot","Elections","BLS: CPI food + MIT Election Lab: County results (bls.gov + electionlab.mit.edu)",80,85,75,80,80,70,85,80))
ideas.append(mk("hav003","States That Raised Their Minimum Wage Vote Differently Than Those That Didnt","Minimum wage ballot initiative results vs partisan lean by state","XREF","US States","State choropleth","Elections","DOL: State minimum wage + MIT Election Lab (dol.gov + electionlab.mit.edu)",70,75,70,80,70,80,80,90))
ideas.append(mk("hav004","Every County Where Median Income Fell and the Incumbent Lost","Counties where real median income declined 2020-2024 vs vote flip","XREF","US Counties","County choropleth","Elections","ACS: Median income + MIT Election Lab: County results (census.gov + electionlab.mit.edu)",80,80,75,75,80,80,80,80))
ideas.append(mk("hav005","Billionaire Campaign Donations vs Tax Policy Votes in Congress","Top 50 donor amounts vs recipients voting record on tax legislation","XREF","US","Scatter plot","Elections","FEC: Campaign finance + GovTrack: Vote records (fec.gov + govtrack.us)",75,70,65,80,85,60,85,85))

# ── Labor x Housing ──
ideas.append(mk("hav006","The Teacher Cant Afford to Live Here Map","Counties where median teacher salary is below median 1BR rent x 12","MAP","US Counties","County choropleth","Labor","BLS: OEWS teacher salary + HUD: FMR by county (bls.gov + huduser.gov)",90,90,80,75,80,85,80,90))
ideas.append(mk("hav007","States Where Service Workers Commute Furthest Because They Cant Afford to Live Near Work","Average commute for food/retail workers vs median rent in job-center zip codes","XREF","US States","State choropleth","Labor","ACS: Commute by occupation + Zillow: Rent (census.gov + zillow.com)",80,85,75,80,75,80,80,80))
ideas.append(mk("hav008","The Work-From-Home Wealth Divide: Remote Workers Own Homes at 2x the Rate","Homeownership rate for remote vs in-person workers by metro","XREF","US Metro","Bar chart","Labor","ACS: Work from home + tenure by occupation (census.gov)",80,85,75,80,70,70,80,85))
ideas.append(mk("hav009","Cities Where Amazon Warehouse Jobs Grew and Housing Got Unaffordable","Amazon fulfillment center openings vs rent change in surrounding zip codes","XREF","US Metro","Scatter plot","Housing","Amazon: Facility locations + Zillow: ZHVI (aboutamazon.com + zillow.com)",75,80,65,80,75,70,85,70))
ideas.append(mk("hav010","Union Membership Rate vs Homeownership Rate by State","Private sector union density vs homeownership rate","XREF","US States","Scatter plot","Labor","BLS: Union membership + ACS: Homeownership (bls.gov + census.gov)",70,75,70,80,65,65,80,90))


# ── Energy x Health ──
ideas.append(mk("hav011","Counties Near Power Plants Have Higher Cancer Rates","Proximity to fossil fuel power plants vs cancer incidence by county","XREF","US Counties","Bivariate choropleth","Health","EPA: Power plant locations + NCI: Cancer incidence (epa.gov + cancer.gov)",80,70,65,80,85,80,80,75))
ideas.append(mk("hav012","States With the Cheapest Electricity Have the Highest Energy Waste","Residential electricity price vs energy intensity per capita","XREF","US States","Scatter plot","Energy","EIA: Electricity prices + energy consumption per capita (eia.gov)",60,65,65,80,60,65,80,90))
ideas.append(mk("hav013","The Coal Miner Health Crisis: Black Lung Cases Rising Again","New black lung cases per year in coal mining states 1990-2024","CHART","US States","Line chart","Health","NIOSH: Coal workers pneumoconiosis + MSHA: Employment (cdc.gov/niosh + msha.gov)",80,70,75,75,85,70,75,85))
ideas.append(mk("hav014","Wind Farm Counties Have Lower Property Tax Rates","Wind energy capacity vs effective property tax rate by county","XREF","US Counties","Scatter plot","Energy","EIA: Wind capacity + Census: Property tax (eia.gov + census.gov)",55,60,60,85,50,65,85,80))
ideas.append(mk("hav015","Nuclear Plant Proximity vs Property Values: The 10 Mile Effect","Median home value by distance ring from nuclear power plants","CHART","US","Line chart","Energy","NRC: Plant locations + ACS: Median home value by tract (nrc.gov + census.gov)",60,65,60,85,65,70,85,80))

# ── Agriculture x Climate ──
ideas.append(mk("hav016","The Harvest Is Shifting North: Corn Belt Moving 100 Miles in 30 Years","Centroid of US corn production by year 1990-2024","MAP","US","Animated choropleth","Agriculture","USDA NASS: Corn production by county (nass.usda.gov)",70,60,70,85,75,85,85,90))
ideas.append(mk("hav017","Countries Where Crop Yields Are Falling as Temperatures Rise","Cereal yield trend vs temperature anomaly trend by country","XREF","World","Scatter plot","Agriculture","FAO: Crop yields + NASA GISS: Temperature (fao.org + data.giss.nasa.gov)",75,65,70,75,80,70,80,85))
ideas.append(mk("hav018","The Aquifer Countdown: Years of Groundwater Left by Agricultural Region","Depletion rate vs estimated remaining supply for major US aquifers","CHART","US","Bar chart","Agriculture","USGS: Groundwater levels + depletion estimates (usgs.gov)",85,65,70,80,90,75,80,75))
ideas.append(mk("hav019","Wine Regions Are Moving Toward the Poles","Change in suitable wine grape growing zones 1990 vs 2024","MAP","World","World choropleth","Agriculture","IPCC + academic: Wine suitability modeling (various)",60,60,60,90,65,80,90,70))
ideas.append(mk("hav020","Farmers Who Switched to Drought-Resistant Crops Earned More","Revenue comparison for farms that switched crops vs those that didnt in drought counties","XREF","US Counties","Bar chart","Agriculture","USDA NASS: Crop economics + USDM: Drought monitor (nass.usda.gov + droughtmonitor.unl.edu)",65,60,65,80,65,65,85,70))

# ── Demographics x Entertainment ──
ideas.append(mk("hav021","The Netflix Map: What Each State Watches Most","Most-streamed Netflix genre by state","MAP","US States","State choropleth","Entertainment","Nielsen: Streaming ratings by DMA (nielsen.com)",60,85,60,75,40,80,75,60))
ideas.append(mk("hav022","Countries With the Oldest Populations Listen to the Saddest Music","Median age vs average Spotify track valence by country","XREF","World","Scatter plot","Entertainment","World Bank: Median age + Spotify: Audio features (worldbank.org + spotify.com)",55,65,55,90,45,55,95,60))
ideas.append(mk("hav023","The Death of the Mall Tracks Suburban Population Decline","Enclosed mall closures vs suburban population change by metro","XREF","US Metro","Scatter plot","Demographics","Coresight: Retail closures + ACS: Suburban population (coresight.com + census.gov)",70,80,65,75,65,65,80,70))

# ── Crime x Transportation ──
ideas.append(mk("hav024","Cities With the Best Public Transit Have Lower Car Theft Rates","Transit ridership per capita vs motor vehicle theft rate","XREF","US Metro","Scatter plot","Crime and Law Enforcement","NTD: Transit ridership + FBI UCR: Vehicle theft (transit.dot.gov + ucr.fbi.gov)",60,65,60,85,55,60,85,85))
ideas.append(mk("hav025","Speed Camera Locations Correlate With Income Not Crash Risk","Speed camera density vs median income vs crash rate by zip code","XREF","US Metro","Scatter plot","Transportation","Local DOT: Camera locations + NHTSA: Crash data + ACS: Income (various + nhtsa.gov + census.gov)",70,75,65,85,75,65,90,65))

# ── Science x Geography ──
ideas.append(mk("hav026","The Earthquake Prediction Gap: Where Seismic Monitoring Is Weakest","USGS seismograph station density vs historical earthquake frequency","XREF","World","World choropleth","Science & Technology","USGS: Global seismograph network + earthquake catalog (earthquake.usgs.gov)",60,50,60,80,70,80,80,85))
ideas.append(mk("hav027","Light Pollution Is Erasing the Milky Way for 80% of Americans","Bortle scale zones overlaid with population density","MAP","US","Special map","Geography & Environment","NOAA: VIIRS nighttime lights + ACS: Population density (noaa.gov + census.gov)",70,75,65,80,70,85,80,85))
ideas.append(mk("hav028","The Deepest Caves vs the Tallest Buildings on Every Continent","Deepest known cave vs tallest building height by continent","CHART","World","Bar chart","Geography & Environment","Speleological surveys + CTBUH: Tall buildings (various + ctbuh.org)",45,50,60,85,35,75,90,85))

# ── Health x Immigration ──
ideas.append(mk("hav029","Immigrant-Dense Counties Have Lower Age-Adjusted Mortality","Foreign-born population share vs age-adjusted death rate by county","XREF","US Counties","Scatter plot","Health","ACS: Foreign-born + CDC WONDER: Mortality (census.gov + wonder.cdc.gov)",65,65,65,90,60,65,90,85))
ideas.append(mk("hav030","The Healthy Immigrant Paradox by Country of Origin","Life expectancy of immigrants vs native-born by origin country","CHART","US","Bar chart","Health","NCHS: Mortality by nativity + Census: Country of birth (cdc.gov + census.gov)",65,65,65,90,55,60,90,75))

# ── Education x Crime ──
ideas.append(mk("hav031","Every Dollar Spent on Pre-K Saves $7 in Prison Costs","Long-term cost-benefit of preschool programs vs incarceration by state","XREF","US States","Bar chart","Education","NIEER: Pre-K spending + Vera: Incarceration costs (nieer.org + vera.org)",85,80,70,80,80,70,80,80))
ideas.append(mk("hav032","School Suspension Rate Predicts Juvenile Arrest Rate by County","K-12 out-of-school suspension rate vs juvenile arrest rate","XREF","US Counties","Scatter plot","Education","OCR: School discipline + OJJDP: Juvenile arrests (ed.gov/ocr + ojjdp.gov)",75,75,70,80,80,70,85,80))
ideas.append(mk("hav033","States That Cut Education Spending the Most Had the Biggest Crime Increases 10 Years Later","Per-pupil spending change 2008-2013 vs violent crime change 2018-2023","XREF","US States","Scatter plot","Education","Census: School finance + FBI UCR: Crime (census.gov + ucr.fbi.gov)",75,70,65,85,80,65,85,80))

# ── Housing x Education ──
ideas.append(mk("hav034","School District Quality Explains 40% of Home Price Variation","GreatSchools rating vs median home price within same metro","XREF","US Metro","Scatter plot","Housing","GreatSchools: Ratings + Zillow: ZHVI by zip (greatschools.org + zillow.com)",75,85,75,70,65,65,75,80))
ideas.append(mk("hav035","College Towns Where Students Pay More Rent Than Townies Earn","Median student rent vs median non-student income in college towns","XREF","US Metro","Bar chart","Housing","ACS: Rent by enrollment status + income by education (census.gov)",75,80,70,80,70,65,85,75))

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
    print(f"Injected {len(new_ideas)} new ideas (HAV batch)")
