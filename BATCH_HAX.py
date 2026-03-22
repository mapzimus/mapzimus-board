"""BATCH HAX: Animated/time-series ideas + scatter plot storytelling.
Focus on ideas that show CHANGE over time - the most viral format.
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

# ── Animated Time Series (Gapminder-style) ──
ideas.append(mk("hax001","Watch Every Country Get Richer and Older Simultaneously","Animated scatter: GDP per capita vs median age by country 1960-2024","CHART","World","Animated bar chart","Demographics","World Bank: GDP per capita + median age (worldbank.org)",75,65,70,75,65,85,75,90))
ideas.append(mk("hax002","How US Political Polarization Grew County by County Since 1960","Animated map of presidential vote margin by county 1960-2024","MAP","US Counties","Animated choropleth","Elections","MIT Election Lab: County presidential results 1960-2024 (electionlab.mit.edu)",80,75,75,80,80,90,75,90))
ideas.append(mk("hax003","The Obesity Epidemic in Real Time: State by State 1990-2024","Animated choropleth of adult obesity rate by state","MAP","US States","Animated choropleth","Health","CDC: BRFSS obesity prevalence by state (cdc.gov)",85,80,80,70,75,90,65,95))
ideas.append(mk("hax004","Watch Global Democracy Retreat Year by Year","Animated world map of V-Dem democracy index 2010-2024","MAP","World","Animated choropleth","Elections","V-Dem: Liberal democracy index (v-dem.net)",75,60,70,80,85,90,75,90))
ideas.append(mk("hax005","The Incredible Shrinking Middle Class: Animated Income Distribution","Animated area chart showing income distribution shift 1970-2024","CHART","US","Animated line chart","Economy","Census: Income distribution by decile (census.gov)",85,85,75,80,80,80,75,90))

# ── "One Chart That Explains Everything" ──
ideas.append(mk("hax006","This One Chart Explains Why Young People Cant Build Wealth","Indexed growth: home prices, tuition, wages, S&P 500 since 1980","CHART","US","Line chart","Economy","FRED: Home prices + College Board: Tuition + BLS: Wages + S&P 500 (fred.stlouisfed.org)",90,95,85,75,85,80,75,95))
ideas.append(mk("hax007","Productivity Went Up - Wages Didnt: The Great Divergence","Worker productivity vs real median compensation since 1948","CHART","US","Line chart","Economy","BLS: Productivity + compensation data (bls.gov)",90,85,85,80,90,80,70,95))
ideas.append(mk("hax008","Every Line on This Chart Is a Failed Climate Promise","Global CO2 emissions vs every COP pledge target since 1992","CHART","World","Line chart","Climate","Global Carbon Project + UNFCCC: NDC targets (globalcarbonproject.org + unfccc.int)",85,65,75,85,90,80,85,90))
ideas.append(mk("hax009","The Great Decoupling: College Costs vs Graduate Earnings","College tuition indexed to 1990 vs starting salary indexed to 1990","CHART","US","Line chart","Education","College Board: Tuition + NACE: Starting salaries (collegeboard.org + naceweb.org)",85,90,80,80,80,75,75,90))
ideas.append(mk("hax010","Americas Trust in Every Institution Has Collapsed Since 2000","Gallup confidence in institutions: military, church, congress, media, banks","CHART","US","Line chart","Demographics","Gallup: Confidence in institutions (gallup.com)",80,80,75,75,80,75,70,90))

# ── Side-by-Side Comparisons ──
ideas.append(mk("hax011","What $1 Million Buys You in Every State","Size of home you can buy for $1M by state, ranked","RANK","US States","Bar chart","Housing","Zillow: ZHVI + average $/sqft by state (zillow.com)",75,90,80,70,65,75,70,85))
ideas.append(mk("hax012","A Week of Groceries in 30 Countries","Photographed grocery basket equivalents priced in local currency and USD","RANK","World","Bar chart","Food & Nutrition","Numbeo: Grocery prices + PPP conversion (numbeo.com + worldbank.org)",70,85,75,75,55,80,75,80))
ideas.append(mk("hax013","What Teachers Earn vs What They Would Earn in Other Fields","Teacher salary vs private sector equivalent with same degree by state","CHART","US States","Bar chart","Education","BLS: OEWS + EPI: Teacher pay penalty (bls.gov + epi.org)",80,85,75,75,75,70,75,90))
ideas.append(mk("hax014","Minimum Wage in 1968 vs Today Adjusted for Inflation","Federal minimum wage purchasing power by year, peak in 1968","CHART","US","Line chart","Economy","DOL: Federal minimum wage history + BLS: CPI (dol.gov + bls.gov)",85,90,80,80,80,70,70,95))
ideas.append(mk("hax015","How Far You Could Drive on an Hours Minimum Wage in 1975 vs 2025","Miles of driving affordable per hour of minimum wage work, by decade","CHART","US","Bar chart","Economy","DOL: Minimum wage + EIA: Gas prices (dol.gov + eia.gov)",80,90,75,80,70,70,80,90))


# ── "The Map Reddit Will Argue About" Series ──
ideas.append(mk("hax016","States Where Its Legal to Fire Someone for Being Gay vs Ones Where Its Not","Employment nondiscrimination law coverage by state","MAP","US States","State choropleth","Labor","Movement Advancement Project: Employment nondiscrimination (lgbtmap.org)",75,70,70,70,80,80,70,90))
ideas.append(mk("hax017","The Most and Least Religious States by Every Possible Measure","Composite religiosity index from 6 different survey measures by state","MAP","US States","State choropleth","Demographics","Gallup + Pew + ARDA: Multiple religiosity measures (gallup.com + pewresearch.org + thearda.com)",65,70,65,75,60,80,75,80))
ideas.append(mk("hax018","If You Overlay a Poverty Map and a Fast Food Map They Are the Same Map","Fast food restaurant density vs poverty rate by census tract","XREF","US Counties","Bivariate choropleth","Food & Nutrition","Census: CBP + ACS: Poverty rate by tract (census.gov)",80,85,75,75,75,85,75,85))
ideas.append(mk("hax019","The Red State Blue State Life Expectancy Gap Is Getting Wider","Life expectancy trend 2000-2024 for states grouped by partisan lean","CHART","US States","Line chart","Health","CDC: Life expectancy + MIT Election Lab: Partisan lean (cdc.gov + electionlab.mit.edu)",80,75,75,80,85,70,80,85))
ideas.append(mk("hax020","Countries Where Women Must Ask Permission to Leave the House","Gender freedom index score colored by specific restriction type","MAP","World","World choropleth","International Statistics","World Bank: Women Business and the Law (worldbank.org/wbl)",80,65,70,80,85,80,75,85))

# ── Infrastructure and Systems ──
ideas.append(mk("hax021","Americas D+ Infrastructure: How Every State Grades","ASCE infrastructure grade by state for roads, bridges, water, energy","MAP","US States","State choropleth","Transportation","ASCE: Infrastructure Report Card by state (infrastructurereportcard.org)",75,75,75,70,75,80,65,90))
ideas.append(mk("hax022","The US Power Grid Is 3 Separate Grids That Barely Talk to Each Other","Eastern, Western, and Texas interconnection mapped with transfer capacity","MAP","US","Special map","Energy","EIA: Electric grid regions + transfer capacity (eia.gov)",65,65,65,85,65,85,80,90))
ideas.append(mk("hax023","Every US Dam Rated High Hazard Potential","High-hazard dams overlaid with downstream population density","MAP","US","Dot map","Infrastructure","USACE: National Inventory of Dams (nid.sec.usace.army.mil)",70,65,65,80,80,80,80,85))
ideas.append(mk("hax024","Amtrak Routes vs Highway Deaths: The Train Would Have Saved Lives","Annual fatalities on highway corridors where Amtrak service was cut","XREF","US","Line map","Transportation","NHTSA: FARS + Amtrak: Historical route map (nhtsa.gov + amtrak.com)",75,70,65,85,80,80,85,75))
ideas.append(mk("hax025","Lead Pipes by City: The Map Flint Wanted You to See","Estimated lead service line prevalence for 100 largest US cities","MAP","US Metro","Dot map","Health","EPA: Lead service line inventories (epa.gov)",80,75,70,80,85,80,75,80))

# ── World Records and Extremes ──
ideas.append(mk("hax026","The Hottest Place on Earth Every Year Since 1900","Location of highest recorded temperature by year, showing geographic drift","MAP","World","Dot map","Climate","WMO: Global temperature extremes archive (wmo.int)",60,55,65,80,65,80,80,85))
ideas.append(mk("hax027","The Deepest Point You Can Reach in Every Ocean","Maximum ocean depth by basin visualized as an inverted bar chart","CHART","World","Bar chart","Geography & Environment","NOAA: GEBCO bathymetric data (noaa.gov)",45,45,65,75,40,80,75,90))
ideas.append(mk("hax028","Countries With the Most Uncontacted Tribes","Known locations of uncontacted indigenous groups by country","MAP","World","Dot map","Demographics","Survival International: Uncontacted tribes (survivalinternational.org)",55,50,55,90,55,80,90,65))
ideas.append(mk("hax029","The Oldest Company Still Operating in Every Country","Founding year of each countrys oldest surviving business","MAP","World","World choropleth","Economy","Various business registries + historical records (general)",55,60,60,90,40,75,90,65))
ideas.append(mk("hax030","The Tallest Building in Every Country Is Getting Taller Exponentially","Tallest building height by country with year of construction","CHART","World","Bar chart","Geography & Environment","CTBUH: Tall Buildings Database (ctbuh.org)",50,55,65,75,40,80,75,85))

# ── Personal Finance / Relatability ──
ideas.append(mk("hax031","How Long It Takes to Save a Down Payment on Minimum Wage in Every State","Years to save 20% down on median home at state minimum wage","MAP","US States","State choropleth","Housing","DOL: Minimum wage + Zillow: ZHVI + savings rate assumption (dol.gov + zillow.com)",85,95,80,75,80,80,75,85))
ideas.append(mk("hax032","The Monthly Budget of a Family Making $50K in Every State","How $50K splits across housing, food, transportation, healthcare by state","CHART","US States","Bar chart","Economy","BLS: Consumer Expenditure Survey + regional adjustments (bls.gov)",80,95,80,70,70,70,75,85))
ideas.append(mk("hax033","The True Cost of Raising a Child to 18 by State","Total child-rearing cost from birth to 18 by state, broken down by category","RANK","US States","Bar chart","Demographics","USDA: Expenditures on Children by Families + state adjustments (usda.gov)",85,90,75,70,70,70,70,80))
ideas.append(mk("hax034","How Much Your Rent Has Increased Since You Turned 18","Rent change since 2006, 2010, 2015, 2020 for each generation","CHART","US","Line chart","Housing","Zillow: ZORI rent index by year (zillow.com)",85,95,80,70,80,70,75,90))
ideas.append(mk("hax035","The Amount of Time You Must Work to Buy a Dozen Eggs in Every Country","Minutes of minimum wage work needed to buy 12 eggs by country","RANK","World","Bar chart","Food & Nutrition","ILO: Minimum wage + Numbeo: Egg prices (ilo.org + numbeo.com)",75,85,75,80,65,65,80,80))

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
    print(f"Injected {len(new_ideas)} new ideas (HAX batch)")
