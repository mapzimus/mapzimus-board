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

IDEAS = [
mk("HDA01","The Junk Fee Economy: How Much Americans Pay in Hidden Fees Per Year","Total annual cost of resort fees, convenience fees, processing fees, and other junk fees per household by category","CHART","US","Bar chart","prices","CFPB: Junk Fees Report (consumerfinance.gov/data-research/research-reports)",78,88,78,78,72,68,72,72),
mk("HDA02","The Pink Tax Is Real: Price Difference for Identical Products Marketed to Women","Average price premium on womens vs. mens versions of identical products — razors, deodorant, shampoo, clothing","CHART","US","Bar chart","gender","NYC DCA: From Cradle to Cane Gender Pricing Study (nyc.gov/dca)",78,82,78,78,72,68,72,72),
mk("HDA03","Shrinkflation Tracker: Products That Got Smaller While Prices Stayed the Same","Major consumer products that reduced size without reducing price, quantified by percentage shrink","RANK","US","Bar chart","prices","Consumer Reports: Shrinkflation Analysis (consumerreports.org)",72,88,78,78,68,68,72,68),
mk("HDA04","The Poverty Tax: How Being Poor Costs More Per Unit for Everything","Price per unit of basic goods at dollar stores vs. bulk retailers — the poor pay more per ounce for everything","CHART","US","Bar chart","poverty","Brookings: The High Cost of Being Poor (brookings.edu/articles/the-high-cost-of-being-poor)",85,82,78,78,82,68,72,72),
mk("HDA05","The Tipping Point: How Tip Expectations Have Crept From 15% to 30%","Average expected tip percentage over time by service type — restaurants, coffee, delivery, hair, taxi","CHART","US","Line chart","prices","Bankrate: Tipping Survey (bankrate.com)",72,88,75,72,68,68,68,72),
mk("HDA06","What Your Internet Actually Costs: Advertised vs. Real Monthly Price by Provider","Advertised broadband price vs. actual monthly bill including fees, equipment, and surcharges by ISP","CHART","US","Bar chart","prices","Consumer Reports: ISP Price Study (consumerreports.org/electronics/broadband)",75,88,78,78,72,68,70,72),
mk("HDA07","The Wedding Industrial Complex: Average Wedding Cost by Metro Area","Average total wedding cost by metro area — some exceeding $50k — broken down by category","MAP","US","Dot map","prices","The Knot: Real Weddings Study (theknot.com/content/average-wedding-cost)",68,78,78,72,62,78,65,78),
mk("HDA08","The Car Insurance Zip Code Penalty: How Your Address Sets Your Rate","Auto insurance premiums by ZIP code showing how geography — not driving record — drives pricing","MAP","US","County choropleth","prices","Insurance Information Institute: Auto Insurance Data (iii.org/fact-statistic/facts-statistics-auto-insurance)",75,82,78,78,72,82,68,78),
mk("HDA09","Americas Most Expensive Ambulance Rides: Average EMS Bill by City","Average ambulance bill by city — from $400 to $2,500+ — the hidden cost of calling 911","RANK","US","Bar chart","prices","KFF: Ambulance Cost Analysis (kff.org/health-costs)",82,82,78,80,78,68,72,68),
mk("HDA10","The Streaming Stack: Total Monthly Cost If You Subscribe to Everything","Combined monthly cost of Netflix, Hulu, Disney+, Max, Peacock, Paramount+, Apple TV+, Amazon Prime, YouTube TV — now exceeds cable","CHART","US","Line chart","prices","Various: Streaming Service Pricing (justwatch.com)",72,88,78,72,68,68,65,82),
mk("HDA11","The Insulin Price Scandal: US vs. Every Other Country","Price of one vial of insulin in the US vs. 30 other countries — America is the extreme outlier","RANK","World","Bar chart","prices","RAND: International Insulin Price Comparison (rand.org/pubs/research_reports)",88,78,82,82,88,68,68,82),
mk("HDA12","The Daycare Paradox: Childcare Workers Earn Too Little While Parents Pay Too Much","Average childcare worker wage vs. average family childcare cost by state — both numbers are broken","XREF","US","Scatter plot","prices","BLS: Childcare Workers (bls.gov/ooh/personal-care-and-service/childcare-workers.htm)",82,85,78,78,80,68,72,78),
mk("HDA13","How Much Your Commute Actually Costs: True Cost of Getting to Work by Mode","Total annual cost of commuting by car, train, bus, and bike including time value, by metro area","RANK","US","Bar chart","prices","AAA: Your Driving Costs (aaa.com/autorepair/articles/true-cost-of-vehicle-ownership)",72,85,78,72,68,68,68,75),
mk("HDA14","The College Textbook Racket: Textbook Prices vs. CPI Over Time","College textbook prices have risen 1,000% since 1977 — 3x faster than medical care and 4x faster than CPI","CHART","US","Line chart","prices","BLS: College Textbook Price Index (bls.gov/opub/ted/textbook-prices)",78,82,80,82,75,68,72,82),
mk("HDA15","The Overdraft Machine: Bank Overdraft Fee Revenue Per Customer by Bank","Annual overdraft fee revenue per account holder at major banks — some collecting billions per year","RANK","US","Bar chart","prices","CFPB: Overdraft Fee Data (consumerfinance.gov/data-research)",78,82,78,78,78,68,72,78),
mk("HDA16","What a Funeral Actually Costs: End-of-Life Pricing by State","Average funeral cost by state including casket, embalming, burial, and service — the last ripoff","MAP","US","State choropleth","prices","NFDA: Member General Price List Survey (nfda.org/news/statistics)",72,75,78,72,68,78,68,78),
mk("HDA17","The HOA Tax: Average Homeowners Association Fees by Metro Area","Monthly HOA fees by metro area and what percentage of homeowners are subject to them","MAP","US","Dot map","prices","Census: ACS Housing Costs (data.census.gov)",68,78,78,72,65,78,65,75),
mk("HDA18","The Convenience Store Premium: How Much More Everything Costs at Gas Stations","Price premium for identical products at convenience stores vs. grocery stores — the desperation markup","CHART","US","Bar chart","prices","Nielsen: Convenience Store Pricing (nielseniq.com)",68,82,78,72,62,68,68,68),
mk("HDA19","Pet Ownership True Cost: Annual Spending Per Pet by Type and State","Annual spending on veterinary care, food, insurance, grooming per pet by type — dogs averaging $2,000+","CHART","US","Bar chart","prices","APPA: National Pet Owners Survey (americanpetproducts.org/research)",62,82,78,72,58,68,65,72),
mk("HDA20","The Tax Prep Tax: What Americans Pay to File Their Taxes","Average cost of tax preparation by method — CPA, H&R Block, TurboTax, free file — and why the IRS doesnt just do it for you","CHART","US","Bar chart","prices","IRS: Individual Income Tax Return Statistics (irs.gov/statistics)",72,82,78,78,72,68,72,78),
mk("HDA21","The Emergency Room Markup: What Hospitals Charge vs. What Procedures Cost","Ratio of hospital chargemaster price to actual cost for common ER procedures by hospital","RANK","US","Bar chart","prices","CMS: Hospital Charge Data (cms.gov/Research-Statistics-Data-and-Systems/Statistics-Trends-and-Reports/Medicare-Provider-Charge-Data)",82,82,78,82,80,68,72,78),
mk("HDA22","The Subscription Creep: Average American Monthly Recurring Charges","Total monthly subscription costs for the average American — streaming, apps, gym, software, boxes — most underestimate by 2x","CHART","US","Bar chart","prices","C+R Research: Consumer Subscription Survey (crresearch.com)",72,88,72,78,68,68,68,68),
mk("HDA23","The Late Fee Machine: Total Late Fee Revenue by Industry","Annual revenue from late fees — credit cards, rent, utilities, library — the $100 billion penalty economy","CHART","US","Bar chart","prices","CFPB: Late Fees Report (consumerfinance.gov)",75,82,78,78,72,68,68,72),
mk("HDA24","What Water Costs: Residential Water Rates by City","Average monthly water bill for a family of four by major city — massive variation from $15 to $150","RANK","US","Bar chart","prices","Circle of Blue: Water Pricing Survey (circleofblue.org/waterpricing)",68,82,78,72,65,68,65,82),
mk("HDA25","The Diploma Premium Is Shrinking: College Earnings Advantage Over Time","Earnings premium of bachelor degree holders over high school graduates, adjusted for student debt — the shrinking ROI","CHART","US","Line chart","prices","Federal Reserve: Economic Well-Being of US Households (federalreserve.gov/publications/report-economic-well-being-us-households)",78,82,78,78,75,68,72,82),
mk("HDA26","Americas Most Expensive ZIP Codes to Get Sick In: Healthcare Cost Variation","Average cost of an appendectomy, MRI, and childbirth by hospital market area — 10x variation for identical procedures","MAP","US","Dot map","prices","Health Care Cost Institute: Healthy Marketplace Index (healthcostinstitute.org)",82,82,78,82,78,78,72,75),
mk("HDA27","The Rent Burden Map: Where Half Your Paycheck Goes to Landlords","Counties where median renter pays more than 30% and 50% of income on rent","MAP","US","County choropleth","prices","Census: ACS Gross Rent as Percentage of Income (data.census.gov)",82,85,78,72,80,82,65,88),
mk("HDA28","How Much a Baby Costs: First-Year Expenses by State","Average first-year cost of a baby by state including hospital delivery, supplies, childcare, and lost wages","MAP","US","State choropleth","prices","USDA: Expenditures on Children by Families (fns.usda.gov/cnpp/expenditures-children-families-reports)",78,85,78,72,72,78,68,75),
mk("HDA29","The Parking Ticket Economy: Cities Where Parking Fines Are a Revenue Strategy","Annual parking ticket revenue per capita by city, showing where enforcement is about money not safety","RANK","US","Bar chart","prices","Governing: Parking Ticket Revenue (governing.com)",68,78,72,72,65,68,68,72),
mk("HDA30","The Airport Markup: Price of a Bottle of Water Inside vs. Outside Every Major Airport","Water bottle prices inside vs. outside the security checkpoint at every major US airport","RANK","US","Bar chart","prices","Various: Airport Pricing Studies (via news reports)",62,82,72,72,58,68,68,65),
mk("HDA31","Americas Property Tax Map: Effective Rate vs. Home Value by County","Effective property tax rate by county, showing that higher-value areas often have lower rates","MAP","US","County choropleth","prices","Tax Foundation: Property Tax by State (taxfoundation.org/property-taxes)",72,78,80,72,70,82,68,85),
mk("HDA32","The Delivery Fee Illusion: What You Actually Pay on DoorDash vs. Cooking at Home","True cost comparison of a meal via delivery app vs. home cooking vs. dine-in including all fees and tips","CHART","US","Bar chart","prices","Various: Delivery Fee Analysis (via consumer reports)",72,88,78,72,68,68,68,68),
mk("HDA33","The Sports Fan Tax: Total Annual Cost of Being a Fan by Team and Sport","Season tickets, merchandise, parking, concessions, streaming — total annual fan cost index by team","RANK","US","Bar chart","prices","Team Marketing Report: Fan Cost Index (teammarketing.com)",62,82,78,72,58,68,65,78),
mk("HDA34","How Much Your Data Is Worth: What Companies Pay for Your Personal Information","Market value of different types of personal data — location, health, financial, browsing, social — per person","CHART","World","Bar chart","prices","Financial Times: How Much Is Your Data Worth (ft.com/content/how-much-is-your-personal-data-worth)",72,82,72,82,72,68,78,62),
mk("HDA35","The Infrastructure of Poverty: How Much It Costs to Not Have a Bank Account","Annual cost of check cashing, money orders, prepaid cards, and payday loans for the unbanked vs. a free checking account","CHART","US","Bar chart","prices","FDIC: How America Banks Survey (fdic.gov/analysis/household-survey)",82,78,78,80,78,68,72,75),
]

# --- inject ---
with open(DATA, 'r', encoding='utf-8') as f:
    txt = f.read()
ids = set(re.findall(r'id:"([^"]+)"', txt))
new = [i for i in IDEAS if re.search(r'id:"([^"]+)"', i).group(1) not in ids]
if not new:
    print("All 35 ideas already present"); exit()
tail = "]; // end D"
txt = txt.replace(tail, ",\n".join(new) + ",\n" + tail)
with open(DATA, 'w', encoding='utf-8') as f:
    f.write(txt)
print(f"Injected {len(new)} new ideas (HDA batch)")
