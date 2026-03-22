"""BATCH HAZ: Hyper-specific XREF combos from existing Kaggle + gov data.
Focus on 3-way mashups and counter-intuitive correlations.
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

# ── Counter-intuitive / paradoxical ──
ideas.append(mk("haz001","Countries With the Most Doctors Per Capita Have the Sickest Populations","Physician density vs disease burden index by country","XREF","World","Scatter plot","Health","WHO: Physician density + IHME: GBD disease burden (who.int + healthdata.org)",60,55,60,95,60,55,90,85))
ideas.append(mk("haz002","The States With the Strictest DUI Laws Have the Most Drunk Driving Deaths","DUI law severity score vs alcohol-impaired driving fatalities per 100k","XREF","US States","Scatter plot","Crime and Law Enforcement","NHTSA: FARS + MADD: DUI law ratings (nhtsa.gov + madd.org)",60,65,60,95,65,60,90,85))
ideas.append(mk("haz003","Cities With the Most Parks Have the Worst Air Quality","Park acreage per capita vs AQI for 100 largest cities","XREF","US Metro","Scatter plot","Geography & Environment","Trust for Public Land: ParkScore + EPA: AQI (tpl.org + epa.gov)",50,55,55,95,45,55,95,80))
ideas.append(mk("haz004","The Countries With the Longest School Years Have the Lowest Test Scores","Instructional days per year vs PISA scores by country","XREF","World","Scatter plot","Education","OECD: Education at a Glance + PISA 2022 (oecd.org)",60,65,65,90,55,55,90,85))
ideas.append(mk("haz005","States That Spend the Most on Police Have Higher Crime Rates","Police spending per capita vs total crime rate by state","XREF","US States","Scatter plot","Crime and Law Enforcement","Census: State expenditure + FBI UCR: Total crime (census.gov + ucr.fbi.gov)",65,65,65,90,70,60,85,90))

# ── Kaggle TSMC/AAPL x Economy ──
ideas.append(mk("haz006","TSMC Stock Price Tracks Global Chip Shortage Headlines","TSMC stock price overlaid with chip shortage news event timeline","XREF","World","Line chart","Economy","Kaggle: TSMC (TSM) Stock & Financial Data (kaggle.com/datasets/tsmc-stock-financial) + News event dates",70,60,65,75,65,75,80,85))
ideas.append(mk("haz007","Apple Revenue by Product vs Time People Spend on Each Device","iPhone/iPad/Mac/Watch revenue share vs daily usage hours per device","XREF","World","Bar chart","Economy","Kaggle: Apple (AAPL) Stock & Financial Data (kaggle.com/datasets/aapl-stock-financial) + Screen Time surveys",60,70,65,80,50,65,80,70))

# ── Global Homicide x other ──
ideas.append(mk("haz008","Countries With the Highest Homicide Rates Are Also the Most Unequal","Intentional homicide rate vs Gini coefficient by country","XREF","World","Scatter plot","Crime and Law Enforcement","Kaggle: Global Homicide Rates by Country (kaggle.com/datasets/global-homicide-rates) + World Bank: Gini (worldbank.org)",75,65,70,75,80,65,75,90))
ideas.append(mk("haz009","The Murder Rate in Latin America vs GDP Growth: A Decoupling Story","Homicide rate vs GDP growth for Latin American countries 2000-2024","XREF","World","Scatter plot","Crime and Law Enforcement","Kaggle: Global Homicide Rates by Country (kaggle.com/datasets/global-homicide-rates) + World Bank: GDP (worldbank.org)",70,55,65,80,75,65,80,85))

# ── Kaggle Global Health x OWID ──
ideas.append(mk("haz010","Healthcare Spending Doesnt Buy Happiness But It Does Buy Years","Health spending per capita vs life expectancy vs happiness score","XREF","World","Scatter plot","Health","Kaggle: Global Health Dataset (kaggle.com/datasets/global-health) + OWID + WHR (ourworldindata.org + worldhappiness.report)",65,65,65,80,55,60,85,80))

# ── Kaggle Modern Slavery x other ──
ideas.append(mk("haz011","Modern Slavery Is Highest in Countries That Export the Most Chocolate","Estimated modern slavery prevalence vs cocoa export volume","XREF","World","Scatter plot","International Statistics","Kaggle: Modern Slavery Dataset (kaggle.com/datasets/modern-slavery) + FAO: Cocoa trade (fao.org)",75,60,60,90,80,60,90,75))

# ── Kaggle Asylum/UNHCR x other ──
ideas.append(mk("haz012","Countries That Accept the Most Refugees Per Capita Are Not the Richest","Refugee acceptance per 1000 population vs GDP per capita","XREF","World","Scatter plot","Demographics","Kaggle: UNHCR Asylum Open Data (kaggle.com/datasets/unhcr-asylum) + World Bank: GDP (worldbank.org)",70,60,65,85,70,60,85,85))
ideas.append(mk("haz013","Asylum Applications Spike 6 Months After Conflict Escalations","Time lag between ACLED conflict events and asylum application surges","XREF","World","Line chart","Demographics","Kaggle: UNHCR Asylum Open Data (kaggle.com/datasets/unhcr-asylum) + ACLED: Conflict events (acleddata.com)",65,55,60,85,70,65,85,80))

# ── CPI/PPI x real life ──
ideas.append(mk("haz014","The Shrinkflation Index: Which Products Lost the Most Volume Since 2019","Product size reduction vs price increase for 50 common grocery items","CHART","US","Bar chart","Economy","BLS: CPI + consumer size tracking + USDA: ERS food data (bls.gov + ers.usda.gov)",80,90,75,80,70,70,80,75))
ideas.append(mk("haz015","The Price of a Wedding Has Tripled Since 2000 - Adjusted for Inflation","Average wedding cost by year 2000-2024 with CPI adjustment","CHART","US","Line chart","Economy","The Knot: Wedding survey + BLS: CPI (theknot.com + bls.gov)",70,80,70,75,65,60,75,80))
ideas.append(mk("haz016","Healthcare CPI Has Outpaced Every Other Category Since 1980","CPI by major category indexed to 1980","CHART","US","Line chart","Health","BLS: CPI by expenditure category (bls.gov/cpi)",80,80,80,70,80,75,65,95))

# ── Kaggle Pop data x other ──
ideas.append(mk("haz017","The Countries That Will Double in Population by 2060","Projected population growth rate with doubling time for Sub-Saharan Africa and South Asia","MAP","World","World choropleth","Demographics","Kaggle: Global Population by Country 1950-2024 (kaggle.com/datasets/global-population-1950-2024) + UN DESA projections",70,55,70,75,70,80,75,85))
ideas.append(mk("haz018","Japans Population Pyramid Is Inverting Into a Coffin Shape","Animated population pyramid Japan 1960-2060 projected","CHART","World","Animated bar chart","Demographics","Kaggle: Global Population by Country 1950-2024 (kaggle.com/datasets/global-population-1950-2024) + UN DESA",80,65,75,80,80,80,75,85))

# ── Kaggle Student Burnout x Education x Economy ──
ideas.append(mk("haz019","Students With Jobs Report More Burnout Than Students Without","Burnout score by employment status from 100k+ responses","CHART","World","Bar chart","Education","Kaggle: Student Mental Health & Burnout Survey (kaggle.com/datasets/student-mental-health-burnout)",75,85,75,70,70,60,75,90))
ideas.append(mk("haz020","The Burnout-GPA Spiral: Students in the Bottom GPA Quartile Report 2x the Burnout","Burnout severity distribution by GPA quartile","XREF","World","Bar chart","Education","Kaggle: Student Mental Health & Burnout Survey (kaggle.com/datasets/student-mental-health-burnout)",75,80,75,75,70,65,75,90))

# ── Kaggle Soccer x geopolitics ──
ideas.append(mk("haz021","Countries at War With Each Other Still Play Football Against Each Other","International matches between currently conflicting nations","CHART","World","Bar chart","Sports & Recreation","Kaggle: International Football Results 1872-2026 (kaggle.com/datasets/martj42/international-football-results-from-1872-to-2017) + ACLED (acleddata.com)",55,55,55,95,55,55,95,80))
ideas.append(mk("haz022","FIFA Rankings Correlate Better With GDP Than Actual Win Rate","FIFA ranking vs GDP per capita r-squared vs FIFA ranking vs win percentage r-squared","XREF","World","Scatter plot","Sports & Recreation","Kaggle: FIFA World Cup History & Rankings (kaggle.com/datasets/fifa-world-cup-history) + World Bank: GDP (worldbank.org)",50,55,55,90,45,55,90,85))

# ── Deep 3-way mashups ──
ideas.append(mk("haz023","The Trifecta of Despair: Counties With Rising Deaths + Falling Incomes + Losing Population","All three declining simultaneously 2015-2024","XREF","US Counties","County choropleth","Health","CDC WONDER + ACS + Census: Mortality, income, population (wonder.cdc.gov + census.gov)",85,75,70,80,90,80,85,80))
ideas.append(mk("haz024","The Innovation Desert: Counties With No College + No Broadband + Declining Jobs","Triple lack of economic mobility inputs","XREF","US Counties","County choropleth","Economy","NCES + FCC + BLS: College, broadband, employment (nces.ed.gov + fcc.gov + bls.gov)",80,70,70,80,80,80,85,80))
ideas.append(mk("haz025","Countries Getting Hotter + Poorer + More Authoritarian Simultaneously","Temperature rise + GDP decline + V-Dem score decline 2010-2024","XREF","World","Scatter plot","Climate","NASA GISS + World Bank + V-Dem: Temperature, GDP, democracy (nasa.gov + worldbank.org + v-dem.net)",75,55,60,85,85,65,90,75))

# ── Viral one-liners visualized ──
ideas.append(mk("haz026","If Walmart Were a Country It Would Be the 25th Largest Employer","Top employers globally including countries and corporations","RANK","World","Bar chart","Economy","Fortune: Largest employers + World Bank: Government employment (fortune.com + worldbank.org)",60,70,70,85,55,65,80,85))
ideas.append(mk("haz027","The US Military Budget Equals the Next 10 Countries Combined","Military spending comparison: US vs next 10 largest","CHART","World","Bar chart","International Statistics","SIPRI: Military Expenditure Database (sipri.org)",75,65,80,70,75,70,65,95))
ideas.append(mk("haz028","Americans Spend More on Lottery Tickets Than on Books Movies and Games Combined","Consumer spending by entertainment category","CHART","US","Bar chart","Entertainment","BLS: Consumer Expenditure Survey (bls.gov/cex)",70,80,70,85,60,60,80,85))
ideas.append(mk("haz029","The Amazon Rainforest Produces 20% of the Worlds Oxygen but 0% of Global GDP","Amazon nations GDP contribution vs oxygen/carbon cycle contribution","CHART","World","Bar chart","Geography & Environment","World Bank: GDP + Global Carbon Project (worldbank.org + globalcarbonproject.org)",65,55,60,85,70,65,80,85))
ideas.append(mk("haz030","There Are More Public Libraries in the US Than McDonalds","Libraries vs McDonalds vs Starbucks count comparison","CHART","US","Bar chart","Education","IMLS: Library count + Corporate: Store counts (imls.gov)",55,70,65,85,40,60,80,90))

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
    print(f"Injected {len(new_ideas)} new ideas (HAZ batch)")
