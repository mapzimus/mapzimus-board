"""BATCH HAR: Cross-references using Kaggle datasets specifically.
Combines Kaggle data with government/OWID data for novel correlations.
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

# ── Kaggle Steam x other domains ──
ideas.append(mk("har001","Countries Where Steam Gamers Spend the Most vs Average Work Hours","Steam game spending per user by country vs OECD average annual hours worked","XREF","World","Scatter plot","Entertainment","Kaggle: Steam Games Dataset 2026 (kaggle.com/datasets/steam-games-2026) + OECD: Hours worked (oecd.org)",65,75,65,80,55,65,85,75))
ideas.append(mk("har002","States With the Most Steam Users vs Lowest Physical Activity","Steam user density vs adults meeting exercise guidelines by state","XREF","US States","Bivariate choropleth","Entertainment","Kaggle: Steam Games Dataset 2026 (kaggle.com/datasets/steam-games-2026) + CDC: BRFSS physical activity (cdc.gov)",60,70,60,80,55,75,85,60))
ideas.append(mk("har003","The Most Expensive Steam Games vs Their Metacritic Scores","Price vs Metacritic score for top 500 Steam titles","CHART","World","Scatter plot","Entertainment","Kaggle: Steam Games Dataset 2026 (kaggle.com/datasets/steam-games-2026)",55,65,70,70,45,65,70,90))

# ── Kaggle Spotify x other domains ──
ideas.append(mk("har004","Do Sad Songs Chart Higher During Recessions?","Average valence of Billboard #1 hits vs GDP growth rate by year","XREF","US","Line chart","Entertainment","Kaggle: Spotify Top Songs & Artists 2025 (kaggle.com/datasets/spotify-wrapped-2025) + BEA: GDP (bea.gov)",70,80,60,85,60,70,90,75))
ideas.append(mk("har005","Countries That Listen to the Fastest Music vs Their Driving Speed","Average BPM of top charting songs vs average highway speed","XREF","World","Scatter plot","Entertainment","Kaggle: Spotify Top Songs & Artists 2025 (kaggle.com/datasets/spotify-wrapped-2025) + WHO: Road safety (who.int)",50,65,55,90,40,55,95,55))
ideas.append(mk("har006","The Song Length Collapse: How the Average Hit Got 90 Seconds Shorter","Average duration of Spotify top 100 songs by year 2000-2025","CHART","World","Line chart","Entertainment","Kaggle: Spotify Top Songs & Artists 2025 (kaggle.com/datasets/spotify-wrapped-2025)",70,80,75,75,60,70,75,90))

# ── Kaggle Football Results x other domains ──
ideas.append(mk("har007","Countries That Win the Most International Matches Are Also the Richest","International football win rate vs GDP per capita","XREF","World","Scatter plot","Sports & Recreation","Kaggle: International Football Results 1872-2026 (kaggle.com/datasets/martj42/international-football-results-from-1872-to-2017) + World Bank: GDP (worldbank.org)",60,70,70,75,50,65,75,90))
ideas.append(mk("har008","Home Advantage Is Disappearing in International Football","Home win percentage by decade 1900s-2020s across all international matches","CHART","World","Line chart","Sports & Recreation","Kaggle: International Football Results 1872-2026 (kaggle.com/datasets/martj42/international-football-results-from-1872-to-2017)",65,70,70,80,55,70,80,90))
ideas.append(mk("har009","Countries With the Largest Goal Differentials vs Military Spending","Average goal differential in football vs military spending % GDP","XREF","World","Scatter plot","Sports & Recreation","Kaggle: International Football Results 1872-2026 (kaggle.com/datasets/martj42/international-football-results-from-1872-to-2017) + SIPRI: Military expenditure (sipri.org)",45,50,55,90,45,55,95,85))


# ── Kaggle Iran War dataset x other domains ──
ideas.append(mk("har010","How Oil Prices Spiked With Every Iran Conflict Escalation","Oil price daily movement overlaid with Iran-US conflict incident timeline","XREF","World","Line chart","Economy","Kaggle: Iran-US Conflict Incidents 2026 (kaggle.com/datasets/iran-war-dataset) + EIA: Daily oil prices (eia.gov)",80,75,75,70,80,80,70,90))
ideas.append(mk("har011","Gas Prices by State During the Iran Crisis vs Distance From the Gulf","State gas price spike magnitude vs geographic distance from Strait of Hormuz","XREF","US States","State choropleth","Economy","Kaggle: Iran War Gas Prices by State 2026 (kaggle.com/datasets/iran-war-gas-prices) + Geographic distance calc",75,80,70,80,75,80,85,85))
ideas.append(mk("har012","How Iran Conflict Incidents Map Onto Global Shipping Chokepoints","Iran-US conflict locations overlaid with major maritime chokepoints","MAP","World","Special map","International Statistics","Kaggle: Iran-US Conflict Incidents 2026 (kaggle.com/datasets/iran-war-dataset) + UNCTAD: Maritime chokepoints (unctad.org)",70,60,65,75,80,85,80,85))

# ── Kaggle AI Index x other domains ──
ideas.append(mk("har013","Countries Leading in AI Research vs Their Press Freedom Score","AI publications per capita vs RSF Press Freedom Index","XREF","World","Scatter plot","Science & Technology","Kaggle: AI Index Dataset 2024 (kaggle.com/datasets/ai-index) + RSF: Press Freedom Index (rsf.org)",65,60,65,85,70,65,90,80))
ideas.append(mk("har014","AI Investment vs Teacher Salary by Country","Private AI investment per capita vs average teacher salary","XREF","World","Scatter plot","Science & Technology","Kaggle: AI Index Dataset 2024 (kaggle.com/datasets/ai-index) + OECD: Education at a Glance (oecd.org)",70,70,65,85,75,65,90,75))
ideas.append(mk("har015","States With the Most AI Job Postings vs Highest Housing Costs","AI job posting concentration vs median rent by state","XREF","US States","Bivariate choropleth","Science & Technology","Kaggle: AI Job Market Trends 2026 (kaggle.com/datasets/ai-job-market-2026) + ACS: Median rent (census.gov)",75,80,70,70,70,80,75,85))

# ── Kaggle Student Burnout x other domains ──
ideas.append(mk("har016","Student Burnout Correlates With Screen Time Not Study Hours","Burnout score vs daily screen time vs daily study hours","XREF","World","Scatter plot","Education","Kaggle: Student Mental Health & Burnout Survey (kaggle.com/datasets/student-mental-health-burnout)",75,85,70,80,70,65,80,90))
ideas.append(mk("har017","Financial Stress Is the Top Predictor of Student Mental Health Crisis","Burnout severity by primary stressor type across 100k+ student responses","CHART","World","Bar chart","Education","Kaggle: Student Mental Health & Burnout Survey (kaggle.com/datasets/student-mental-health-burnout)",80,85,75,70,75,70,75,90))
ideas.append(mk("har018","The Sleep-GPA Connection: Students Sleeping Under 6 Hours Score a Full Grade Lower","Average GPA by sleep duration bucket from student survey","CHART","World","Bar chart","Education","Kaggle: Student Mental Health & Burnout Survey (kaggle.com/datasets/student-mental-health-burnout)",75,85,75,75,65,70,70,90))

# ── Kaggle Asteroid dataset x other domains ──
ideas.append(mk("har019","Near-Earth Asteroids Discovered Per Year vs NASA Budget","Annual NEO discoveries overlaid with NASA annual budget adjusted for inflation","XREF","World","Line chart","Science & Technology","Kaggle: Asteroid Dataset Oct 2025 (kaggle.com/datasets/asteroid-dataset-2025) + NASA: Budget history (nasa.gov)",60,55,65,75,60,70,80,90))
ideas.append(mk("har020","The Size Distribution of Known Asteroids Follows a Power Law","Asteroid count by diameter bin showing power law distribution","CHART","World","Bar chart","Science & Technology","Kaggle: Asteroid Dataset Oct 2025 (kaggle.com/datasets/asteroid-dataset-2025)",50,45,65,70,55,70,75,90))


# ── Kaggle Bitcoin + Gold + NVIDIA x Economy ──
ideas.append(mk("har021","Bitcoin vs Gold vs S&P 500: Which Actually Hedges Inflation?","Cumulative returns of BTC, Gold, SPX overlaid with CPI 2015-2026","XREF","World","Line chart","Economy","Kaggle: Bitcoin Price History (kaggle.com/datasets/bitcoin-prices) + Kaggle: Gold Price History (kaggle.com/datasets/gold-prices) + BLS: CPI (bls.gov)",80,80,75,75,65,80,75,90))
ideas.append(mk("har022","NVIDIA Stock Price Tracks AI Hype Cycle Almost Perfectly","NVDA stock price vs Google Trends AI search interest 2019-2026","XREF","World","Line chart","Economy","Kaggle: NVIDIA (NVDA) Stock Data (kaggle.com/datasets/nvidia-stock-data) + Google Trends: AI (trends.google.com)",70,70,70,75,60,75,75,85))
ideas.append(mk("har023","Bitcoin Crashes Predict Crypto Job Layoffs by 3 Months","BTC price drops vs crypto industry layoffs with time lag","XREF","World","Line chart","Economy","Kaggle: Bitcoin Price History (kaggle.com/datasets/bitcoin-prices) + Layoffs.fyi: Tech layoffs (layoffs.fyi)",70,70,65,80,70,70,80,80))

# ── Kaggle Breakfast Basket x other domains ──
ideas.append(mk("har024","Breakfast Costs More in Countries With Higher Minimum Wages","Average breakfast basket price vs minimum wage purchasing power","XREF","World","Scatter plot","Food & Nutrition","Kaggle: Global Breakfast Basket Prices (kaggle.com/datasets/breakfast-basket) + OECD: Minimum wage (oecd.org)",65,80,70,70,55,60,75,85))
ideas.append(mk("har025","The Egg Premium: Countries Where Eggs Cost the Most Relative to Income","Egg price as share of daily minimum wage across 100+ countries","RANK","World","Bar chart","Food & Nutrition","Kaggle: Global Breakfast Basket Prices (kaggle.com/datasets/breakfast-basket) + ILO: Minimum wages (ilo.org)",70,80,70,75,65,65,80,80))

# ── Kaggle UAP/UFO x other domains ──
ideas.append(mk("har026","UFO Sightings Cluster Near Military Bases","UAP report locations vs proximity to US military installations","MAP","US","Dot map","Science & Technology","Kaggle: UAP/UFO Sighting Reports (kaggle.com/datasets/uap-reports) + DoD: Military installations (defense.gov)",65,70,60,85,60,80,85,85))
ideas.append(mk("har027","States With the Most UFO Sightings Per Capita vs Light Pollution","UAP reports per 100k vs Bortle scale light pollution rating","XREF","US States","Bivariate choropleth","Science & Technology","Kaggle: UAP/UFO Sighting Reports (kaggle.com/datasets/uap-reports) + NOAA: VIIRS nighttime lights (noaa.gov)",60,65,60,85,55,75,90,80))
ideas.append(mk("har028","UFO Sighting Reports Spike After Sci-Fi Movie Releases","Monthly UAP report count vs major sci-fi film release dates","XREF","US","Line chart","Entertainment","Kaggle: UAP/UFO Sighting Reports (kaggle.com/datasets/uap-reports) + Box Office Mojo: Sci-fi releases (boxofficemojo.com)",55,65,60,90,45,65,90,75))

# ── Kaggle HistorySaid Global Economic x other domains ──
ideas.append(mk("har029","Countries That Grew Fastest After Independence vs Democracy Level","GDP growth first 20 years post-independence vs current V-Dem democracy index","XREF","World","Scatter plot","Economy","Kaggle: HistorySaid Global Economic Dataset - World Bank/IMF/BIS (kaggle.com/datasets/historysaid/global-economic-dataset) + V-Dem (v-dem.net)",70,60,65,80,70,70,85,85))
ideas.append(mk("har030","The BIS Credit Gap Predicted Every Major Financial Crisis","BIS credit-to-GDP gap overlaid with crisis dates for 40 countries","CHART","World","Line chart","Economy","Kaggle: HistorySaid Global Economic Dataset - World Bank/IMF/BIS (kaggle.com/datasets/historysaid/global-economic-dataset)",75,65,70,80,75,75,85,90))

# ── Kaggle ICE Detention x Immigration ──
ideas.append(mk("har031","Average ICE Detention Stay Length by Nationality","Mean detention days by country of origin, sorted longest to shortest","RANK","US","Bar chart","Demographics","Kaggle: ICE Detention Stays (kaggle.com/datasets/ice-detention-stays)",75,70,70,75,80,65,75,90))
ideas.append(mk("har032","ICE Detention Facilities Are Concentrated in the South and Southwest","Geographic distribution of ICE detention centers by capacity","MAP","US","Dot map","Demographics","Kaggle: ICE Detention Stays (kaggle.com/datasets/ice-detention-stays) + ICE: Facility locations (ice.gov)",75,70,70,70,80,80,70,85))
ideas.append(mk("har033","Longer ICE Detention Stays Correlate With Countries Under Travel Bans","Average detention length vs travel ban/restriction status of origin country","XREF","US","Bar chart","Demographics","Kaggle: ICE Detention Stays (kaggle.com/datasets/ice-detention-stays) + State Dept: Travel advisories (state.gov)",70,65,65,80,80,65,85,80))

# ── Kaggle Richest People x other domains ──
ideas.append(mk("har034","The Billionaire Belt: Where the Worlds Richest Actually Live","Geographic clustering of top 500 billionaires by metro area","MAP","World","Dot map","Economy","Kaggle: Richest People Dataset (kaggle.com/datasets/richest-people) + Forbes: Billionaire list (forbes.com)",65,70,70,70,55,80,70,90))
ideas.append(mk("har035","Self-Made vs Inherited Wealth by Country","Share of billionaire wealth that is self-made vs inherited by nation","CHART","World","Bar chart","Economy","Kaggle: Richest People Dataset (kaggle.com/datasets/richest-people)",70,75,70,80,65,70,80,85))

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
    print(f"Injected {len(new_ideas)} new ideas (HAR batch)")
