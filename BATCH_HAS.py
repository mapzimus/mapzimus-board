"""BATCH HAS: 'Existential' viral cross-refs - the maps/charts that make people
stop scrolling because they reveal uncomfortable truths.
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

# ── The Inequality Series ──
ideas.append(mk("has001","It Takes 2.5 Lifetimes to Earn What a CEO Makes in One Year","Median worker lifetime earnings vs average CEO annual comp by industry","XREF","US","Bar chart","Economy","BLS: Median wage + AFL-CIO: Executive Paywatch (bls.gov + aflcio.org/paywatch)",90,90,80,80,85,75,80,90))
ideas.append(mk("has002","The Zip Code Lottery: Life Expectancy Varies 30 Years Within the Same City","Min vs max life expectancy by zip code within the 20 largest US metros","CHART","US Metro","Bar chart","Health","IHME: Life expectancy by census tract (healthdata.org)",90,85,80,85,90,80,80,85))
ideas.append(mk("has003","Your Grandparents Could Buy a House on One Income - Heres What Changed","Median home price to median household income ratio 1960-2024","CHART","US","Line chart","Housing","FRED: Median home price + Census: Median household income (fred.stlouisfed.org + census.gov)",90,95,85,75,85,80,70,90))
ideas.append(mk("has004","The Wealth Gap Between Black and White Families Has Barely Moved Since 1990","Median net worth by race 1989-2022 from Survey of Consumer Finances","CHART","US","Line chart","Economy","Federal Reserve: Survey of Consumer Finances (federalreserve.gov/econres/scfindex.htm)",90,80,80,75,90,75,75,90))
ideas.append(mk("has005","States Where the Rich Pay a Lower Tax Rate Than Everyone Else","Effective total state+local tax rate by income quintile","CHART","US States","Bar chart","Economy","ITEP: Who Pays? (itep.org/whopays)",85,90,80,80,85,75,75,90))

# ── Climate Dread ──
ideas.append(mk("has006","The Cities That Will Be Underwater by 2100","Projected sea level rise impact on 50 most vulnerable coastal cities","MAP","World","Special map","Climate","Climate Central: Coastal risk screening (climatecentral.org)",90,80,80,85,90,90,75,80))
ideas.append(mk("has007","This Is How Much Hotter Your City Got Since You Were Born","Temperature anomaly by decade for 100 largest US cities 1960-2024","CHART","US Metro","Line chart","Climate","NOAA: Climate normals by station (noaa.gov/ncei)",85,90,80,75,80,80,75,90))
ideas.append(mk("has008","Countries Contributing the Most CO2 vs Countries Suffering Most From Climate Change","Cumulative CO2 emissions vs Global Climate Risk Index score","XREF","World","Scatter plot","Climate","Global Carbon Project + Germanwatch: CRI (globalcarbonproject.org + germanwatch.org)",85,70,75,80,90,80,80,90))
ideas.append(mk("has009","The Wildfire Season Used to Be 4 Months Long - Now Its 7","US wildfire season length in days by decade 1980s-2020s","CHART","US","Bar chart","Climate","NIFC: Wildfire statistics (nifc.gov)",80,80,80,80,85,75,75,90))
ideas.append(mk("has010","Glacier Surface Area Lost by Country Since 1980","Percent glacier area remaining vs 1980 baseline by country with glaciers","CHART","World","Bar chart","Climate","WGMS: Global Glacier Change Bulletin (wgms.ch)",85,65,75,80,90,85,80,80))


# ── AI / Automation Displacement ──
ideas.append(mk("has011","Jobs Most Likely to Be Automated vs Their Current Median Wage","Automation probability vs median annual wage for 100 occupations","XREF","US","Scatter plot","Science & Technology","Oxford/Frey-Osborne: Automation risk + BLS: OEWS wages (bls.gov)",80,85,75,80,80,70,80,90))
ideas.append(mk("has012","Countries With the Most Robots Per Worker vs Youth Unemployment","Industrial robot density vs youth unemployment rate","XREF","World","Scatter plot","Science & Technology","IFR: World Robotics + World Bank: Youth unemployment (ifr.org + worldbank.org)",70,70,70,85,75,70,85,85))
ideas.append(mk("has013","The AI Paradox: States With the Most AI Jobs Also Have the Widest Wage Gaps","AI job density vs 90/10 wage ratio by state","XREF","US States","Bivariate choropleth","Science & Technology","Kaggle: AI Job Market Trends 2026 (kaggle.com/datasets/ai-job-market-2026) + BLS: Wage percentiles (bls.gov)",75,75,70,85,75,80,85,80))

# ── Healthcare Costs ──
ideas.append(mk("has014","The Price of a Heart Attack by State","Average cost of heart attack hospitalization by state","MAP","US States","State choropleth","Health","CMS: Medicare Provider Utilization (cms.gov)",85,85,80,75,80,80,70,90))
ideas.append(mk("has015","Insulin Costs 10x More in America Than Anywhere Else","Insulin price per unit across 30 countries","RANK","World","Bar chart","Health","RAND: International Drug Price Comparison (rand.org)",90,85,85,70,90,75,70,90))
ideas.append(mk("has016","Counties Where People Crowdfund Medical Bills the Most vs Insurance Rates","GoFundMe medical campaign density vs uninsured rate by county","XREF","US Counties","Bivariate choropleth","Health","GoFundMe: Public campaigns + ACS: Health insurance (census.gov)",85,85,70,80,85,80,85,65))

# ── Housing Crisis ──
ideas.append(mk("has017","How Many Hours of Minimum Wage Work to Afford a 1BR Apartment in Every State","Hours per week at minimum wage needed to afford median 1BR rent","MAP","US States","State choropleth","Housing","DOL: State minimum wage + HUD: Fair Market Rents (dol.gov + huduser.gov)",90,95,85,70,85,80,70,95))
ideas.append(mk("has018","The Number of Homeless People vs Empty Homes by State","Estimated homeless population vs vacant housing units","XREF","US States","Bar chart","Housing","HUD: PIT count + ACS: Vacant housing units (huduser.gov + census.gov)",85,80,80,80,90,75,80,90))
ideas.append(mk("has019","Cities Where Average Rent Exceeds Average Mortgage Payment","Monthly rent vs monthly mortgage for median home in 50 largest metros","CHART","US Metro","Bar chart","Housing","Zillow: Rent + mortgage payment index (zillow.com)",85,90,80,75,80,75,75,85))

# ── Education Debt ──
ideas.append(mk("has020","Total US Student Loan Debt Is Now Larger Than the GDP of 170 Countries","$1.77T student debt compared to national GDPs, with countries smaller highlighted","CHART","World","Bar chart","Education","Federal Reserve: Student loan balance + World Bank: GDP (newyorkfed.org + worldbank.org)",80,85,75,85,80,70,85,90))
ideas.append(mk("has021","States Where College Graduates Earn Less Than the National Median","States where BA holders median income is below national all-worker median","RANK","US States","State choropleth","Education","ACS: Earnings by educational attainment by state (census.gov)",80,85,75,85,80,80,80,90))

# ── Democracy and Rights ──
ideas.append(mk("has022","The Global Democracy Recession: Countries That Backslid Since 2010","V-Dem liberal democracy index change 2010-2024 by country","MAP","World","World choropleth","Elections","V-Dem: Liberal democracy index (v-dem.net)",80,65,70,80,85,85,75,90))
ideas.append(mk("has023","States That Passed the Most Voting Restrictions vs Voter Turnout Change","New voting restrictions enacted 2020-2024 vs change in voter turnout","XREF","US States","Bivariate choropleth","Elections","Brennan Center: Voting laws tracker + MIT Election Lab (brennancenter.org + electionlab.mit.edu)",80,75,70,80,85,80,80,85))
ideas.append(mk("has024","Countries Where Press Freedom Fell Most in 5 Years vs GDP Growth","RSF Press Freedom change vs GDP growth rate 2019-2024","XREF","World","Scatter plot","International Statistics","RSF: Press Freedom Index + World Bank: GDP growth (rsf.org + worldbank.org)",70,60,65,80,80,70,85,85))

# ── Loneliness Epidemic ──
ideas.append(mk("has025","The Friendship Recession: Americans With Zero Close Friends by Year","Share of Americans reporting zero close friends 1990-2024","CHART","US","Line chart","Demographics","GSS: Social networks + Surgeon General: Advisory on loneliness (gss.norc.org)",85,90,75,80,80,70,80,80))
ideas.append(mk("has026","States Where People Live Alone vs Suicide Rate","Single-person household rate vs age-adjusted suicide rate","XREF","US States","Bivariate choropleth","Health","ACS: Household composition + CDC WONDER: Suicide (census.gov + wonder.cdc.gov)",80,80,70,75,85,80,80,90))

# ── Food System ──
ideas.append(mk("has027","4 Companies Control 85% of US Beef Processing","Market concentration in beef, pork, poultry processing","CHART","US","Bar chart","Food & Nutrition","USDA GIPSA: Packers & Stockyards annual report (usda.gov)",80,80,80,80,80,70,75,85))
ideas.append(mk("has028","Countries That Throw Away the Most Food vs Countries With the Most Hunger","Per capita food waste vs Global Hunger Index score","XREF","World","Scatter plot","Food & Nutrition","UNEP: Food Waste Index + Global Hunger Index (unep.org + globalhungerindex.org)",85,75,75,85,85,70,85,85))

# ── Water Crisis ──
ideas.append(mk("has029","Counties Where the Aquifer Is Running Dry","Groundwater level change 2000-2024 for major US aquifers by county","MAP","US Counties","County choropleth","Geography & Environment","USGS: Groundwater levels + Ogallala aquifer monitoring (usgs.gov)",85,70,75,80,90,85,80,80))
ideas.append(mk("has030","Countries That Import the Most Water in Virtual Form","Net virtual water imports via agricultural trade by country","MAP","World","World choropleth","Geography & Environment","Water Footprint Network: Virtual water trade (waterfootprint.org)",60,55,60,90,65,75,90,75))

# ── Generational ──
ideas.append(mk("has031","Every Generation Thinks the Next One Is Lazier - The Data Says Otherwise","Labor force participation rate at age 25 for each generation","CHART","US","Bar chart","Demographics","BLS: CPS labor force participation by age cohort (bls.gov)",80,90,75,80,65,70,85,90))
ideas.append(mk("has032","Gen Z Cant Afford to Live Where the Jobs Are","Entry-level salary vs cost of living ratio for 25 largest job markets","CHART","US Metro","Bar chart","Economy","BLS: Entry-level wages + MIT Living Wage Calculator (bls.gov + livingwage.mit.edu)",90,95,80,75,80,75,80,85))
ideas.append(mk("has033","The Age You Could Afford a Home Has Risen 13 Years Since 1980","Age at which median earner can afford median home, by decade","CHART","US","Line chart","Housing","Census: Income by age + FRED: Median home price (census.gov + fred.stlouisfed.org)",90,95,85,80,85,80,80,85))
ideas.append(mk("has034","Parents Spend 3x More on Childcare Than Their Parents Spent on a Mortgage","Childcare cost as % of income vs mortgage cost as % of income by decade","CHART","US","Line chart","Demographics","BLS: Consumer Expenditure Survey historical (bls.gov/cex)",90,95,80,80,80,75,80,85))
ideas.append(mk("has035","The American Dream Probability by Birth Year","Probability of earning more than your parents by birth cohort 1940-2000","CHART","US","Line chart","Economy","Opportunity Insights: Absolute mobility (opportunityinsights.org)",90,90,80,80,85,80,80,90))

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
    print(f"Injected {len(new_ideas)} new ideas (HAS batch)")
