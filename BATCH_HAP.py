"""BATCH HAP: More cross-referenced ideas from uncombined section pairs.
Crime x Economy, Health x Sports, Demographics x Science, Food x Economy, etc.
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

# ── Crime x Economy (445 combined, never crossed) ──
ideas.append(mk("hap001","States Where Property Crime Rose as Wages Fell","Change in property crime rate vs real median wage change 2019-2024","XREF","US States","Bivariate choropleth","Crime and Law Enforcement","FBI UCR: Property crime + BLS: Median wage by state (ucr.fbi.gov + bls.gov)",80,85,75,75,80,80,75,85))
ideas.append(mk("hap002","Countries Where Income Inequality Predicts Murder Rate","Gini coefficient vs intentional homicide rate by country","XREF","World","Scatter plot","Crime and Law Enforcement","World Bank: Gini + UNODC: Homicide rate (worldbank.org + unodc.org)",80,75,75,75,85,70,80,90))
ideas.append(mk("hap003","US Counties Where Bank Deserts Overlap With Fraud Hotspots","Counties with no bank branches vs financial fraud complaint rate","XREF","US Counties","Bivariate choropleth","Crime and Law Enforcement","FDIC: Bank branch data + FTC: Consumer Sentinel fraud (fdic.gov + ftc.gov)",70,75,65,85,75,80,90,75))
ideas.append(mk("hap004","The Payday Lender-to-Police Ratio by US County","Payday lender density vs police officers per capita","XREF","US Counties","Scatter plot","Economy","Census: CBP + FBI: Law enforcement employees (census.gov + ucr.fbi.gov)",65,75,65,85,70,70,90,75))
ideas.append(mk("hap005","Countries Where Cryptocurrency Is Banned vs Financial Crime Rate","Crypto legal status vs financial crime index","XREF","World","World choropleth","Crime and Law Enforcement","Library of Congress: Crypto regulation + Basel AML Index (loc.gov + index.baselgovernance.org)",65,65,65,85,70,75,85,80))

# ── Health x Sports (460 combined, never crossed) ──
ideas.append(mk("hap006","States With the Most Gyms Per Capita vs Obesity Rate","Gym/fitness center density vs adult obesity rate","XREF","US States","Bivariate choropleth","Health","Census: CBP fitness + CDC: BRFSS obesity (census.gov + cdc.gov)",75,85,80,70,60,80,70,90))
ideas.append(mk("hap007","Countries That Win the Most Olympic Medals vs Life Expectancy","All-time Olympic medal count vs current life expectancy","XREF","World","Scatter plot","Sports & Recreation","IOC: Medal database + World Bank: Life expectancy (olympics.com + worldbank.org)",65,70,70,80,50,75,80,90))
ideas.append(mk("hap008","NFL Concussion Rates by Team vs City CTE Diagnosis Rate","Reported concussions per team vs metro area CTE-related deaths","XREF","US Metro","Bar chart","Sports & Recreation","NFL: Injury data + CDC: CTE mortality by metro (nfl.com + cdc.gov)",75,70,60,80,80,65,85,55))
ideas.append(mk("hap009","Marathon Finish Times Are Getting Slower in Hotter Cities","Average marathon finish time trend vs average race-day temperature by city","XREF","World","Scatter plot","Sports & Recreation","World Athletics: Marathon results + NOAA/Weather: Temperature (worldathletics.org + noaa.gov)",65,70,70,80,65,70,85,70))
ideas.append(mk("hap010","Youth Sports Participation vs Teen Depression by State","Youth organized sports participation rate vs teen depression rate","XREF","US States","Bivariate choropleth","Health","Aspen Institute: State of Play + CDC: YRBS teen mental health (aspenprojectplay.org + cdc.gov)",80,85,75,70,70,75,80,75))


# ── Demographics x Science & Technology (418 combined, never crossed) ──
ideas.append(mk("hap011","The Graying of Silicon Valley: Median Age in Tech Hubs 2000 vs 2024","Median age change in top 20 tech metros","XREF","US Metro","Bar chart","Science & Technology","ACS/Census: Median age by metro 2000+2024 (census.gov)",70,75,70,75,65,70,80,90))
ideas.append(mk("hap012","Countries Where the Youngest Population Meets the Fastest Internet","Median age vs average broadband speed by country","XREF","World","Scatter plot","Science & Technology","CIA Factbook: Median age + Speedtest: Global Index (cia.gov + speedtest.net)",60,65,65,75,55,70,80,85))
ideas.append(mk("hap013","Birth Rate vs Patent Applications by Country","Crude birth rate vs patent applications per million","XREF","World","Scatter plot","Demographics","World Bank: Birth rate + WIPO: Patents (worldbank.org + wipo.int)",55,55,65,85,60,65,90,90))
ideas.append(mk("hap014","Counties Where Population Is Shrinking But STEM Jobs Are Growing","Population change vs STEM employment change 2018-2024","XREF","US Counties","Bivariate choropleth","Demographics","ACS: Population + BLS: OEWS STEM employment (census.gov + bls.gov)",70,75,65,85,70,80,85,80))
ideas.append(mk("hap015","The Countries Sending the Most STEM Students Abroad vs Brain Drain","Outbound STEM students vs net skilled migration rate","XREF","World","Scatter plot","Demographics","UNESCO: Student mobility + World Bank: Net migration (uis.unesco.org + worldbank.org)",65,60,65,80,70,65,85,75))

# ── Economy x Food & Nutrition (416 combined, never crossed) ──
ideas.append(mk("hap016","How Much of Your Paycheck Goes to Groceries in Every State","Grocery spending as % of median household income by state","XREF","US States","State choropleth","Food & Nutrition","BLS: Consumer Expenditure Survey + ACS: Median income (bls.gov + census.gov)",80,90,80,70,75,80,65,90))
ideas.append(mk("hap017","Countries Where Food Is Cheapest vs Where People Are Hungriest","Food CPI vs Global Hunger Index score","XREF","World","Scatter plot","Food & Nutrition","World Bank: Food CPI + Global Hunger Index (worldbank.org + globalhungerindex.org)",80,75,75,75,80,70,80,85))
ideas.append(mk("hap018","The Avocado Toast Index: Brunch Prices vs Median Rent by City","Average brunch restaurant meal price vs median studio rent in top 50 US cities","XREF","US Metro","Scatter plot","Food & Nutrition","Yelp: Restaurant pricing + Zillow: Rent index (yelp.com + zillow.com)",70,85,70,75,65,70,85,70))
ideas.append(mk("hap019","Farm Subsidies per Acre vs Food Desert Rate by County","USDA farm subsidy dollars per cropland acre vs food desert population %","XREF","US Counties","Bivariate choropleth","Food & Nutrition","EWG: Farm subsidies + USDA: Food access atlas (ewg.org + ers.usda.gov)",75,75,70,85,80,80,85,80))
ideas.append(mk("hap020","Countries Where People Spend the Most Time Eating vs GDP","Minutes per day eating and drinking vs GDP per capita","XREF","World","Scatter plot","Economy","OECD: Time use survey + World Bank: GDP per capita (oecd.org + worldbank.org)",65,80,70,80,50,65,85,85))

# ── Housing x International (421 combined, never crossed) ──
ideas.append(mk("hap021","The Price of a Home in Every Capital City Relative to Local Salary","Median home price to median annual salary ratio in world capitals","XREF","World","World choropleth","Housing","Numbeo: Cost of living + World Bank: GNI per capita (numbeo.com + worldbank.org)",80,85,80,75,75,80,75,80))
ideas.append(mk("hap022","Countries Where Homeownership Is Highest vs Happiest","Homeownership rate vs World Happiness Index score","XREF","World","Scatter plot","Housing","Eurostat/World Bank: Homeownership + WHR: Happiness score (worldbank.org + worldhappiness.report)",70,75,70,80,60,65,85,80))
ideas.append(mk("hap023","Rent as % of Income: How OECD Countries Compare","Housing cost overburden rate across 38 OECD nations","RANK","World","Bar chart","Housing","OECD: Housing affordability indicators (oecd.org)",80,85,80,70,75,75,70,90))


# ── Economy x Housing (404 combined, never crossed) ──
ideas.append(mk("hap024","States Where Home Prices Rose Fastest vs Where Wages Didn't Keep Up","Home price growth vs median wage growth 2019-2024 by state","XREF","US States","Bivariate choropleth","Economy","FHFA: House Price Index + BLS: Median wage (fhfa.gov + bls.gov)",85,90,80,70,80,80,70,90))
ideas.append(mk("hap025","The Airbnb Effect: Cities Where Tourist Rentals Predict Rent Hikes","Airbnb listing density vs year-over-year rent increase","XREF","US Metro","Scatter plot","Housing","Inside Airbnb: Listing data + Zillow: Rent index (insideairbnb.com + zillow.com)",75,80,70,80,80,70,80,75))
ideas.append(mk("hap026","Counties Where Remote Work Grew Most vs Home Price Surge","Remote work rate increase vs median home price increase 2019-2024","XREF","US Counties","Bivariate choropleth","Housing","ACS: Work from home + Zillow: ZHVI by county (census.gov + zillow.com)",80,85,75,75,70,80,80,85))

# ── Entertainment x International (408 combined, never crossed) ──
ideas.append(mk("hap027","Countries That Produce the Most Movies vs Box Office Revenue Per Capita","Annual film production vs domestic box office per capita","XREF","World","Scatter plot","Entertainment","UNESCO: Film production + Box Office Mojo (uis.unesco.org + boxofficemojo.com)",60,65,65,75,50,65,80,75))
ideas.append(mk("hap028","The Netflix Paradox: Countries With Most Subscribers vs Least Local Content","Netflix subscribers per capita vs share of local-language titles","XREF","World","Scatter plot","Entertainment","Netflix: Global subscriber data + JustWatch: Catalog analysis (netflix.com + justwatch.com)",65,70,65,80,60,65,85,65))
ideas.append(mk("hap029","Gaming Revenue Per Capita by Country vs Average Internet Speed","Video game market revenue per capita vs median download speed","XREF","World","Scatter plot","Entertainment","Newzoo: Global Games Market + Speedtest: Global Index (newzoo.com + speedtest.net)",60,70,65,70,50,65,80,80))
ideas.append(mk("hap030","Countries Where Spotify Listening Hours Predict Happiness Scores","Average daily Spotify listening hours vs World Happiness Score","XREF","World","Scatter plot","Entertainment","Kaggle: Spotify Top Songs & Artists 2025 (kaggle.com/datasets/spotify-wrapped-2025) + WHR (worldhappiness.report)",60,70,60,80,50,60,90,70))

# ── Education x Economy (never crossed) ──
ideas.append(mk("hap031","States Where Teacher Pay Is Lowest vs Student Loan Debt Is Highest","Average teacher salary vs average student loan balance","XREF","US States","Bivariate choropleth","Education","NEA: Teacher salary + Federal Reserve: Student loans by state (nea.org + newyorkfed.org)",80,85,75,75,80,80,75,85))
ideas.append(mk("hap032","Countries That Spend the Most on Education vs PISA Scores","Education spending as % GDP vs average PISA math score","XREF","World","Scatter plot","Education","UNESCO: Education spending + OECD: PISA 2022 (uis.unesco.org + oecd.org/pisa)",70,70,75,80,65,70,75,90))
ideas.append(mk("hap033","The Community College Pipeline: Enrollment vs Local Unemployment","Community college enrollment change vs local unemployment rate by metro","XREF","US Metro","Scatter plot","Education","IPEDS: CC enrollment + BLS: LAUS metro unemployment (nces.ed.gov + bls.gov)",65,75,70,70,65,65,75,85))
ideas.append(mk("hap034","Counties Where Kids Cant Read vs Median Income","4th grade reading proficiency vs median household income by county","XREF","US Counties","Bivariate choropleth","Education","NAEP: Trial Urban District + ACS: Income (nces.ed.gov + census.gov)",80,80,75,70,80,80,70,75))
ideas.append(mk("hap035","Student Debt Per Capita vs Home Ownership Rate by State for Under-35s","Average student loan balance for 25-34 vs homeownership rate same age","XREF","US States","Bivariate choropleth","Education","Federal Reserve: Student loans + ACS: Homeownership by age (newyorkfed.org + census.gov)",85,90,75,75,80,80,80,85))

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
    print(f"Injected {len(new_ideas)} new ideas (HAP batch)")
