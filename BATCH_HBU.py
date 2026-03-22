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
# === "Why Everything Costs More" series — inflation deep dives ===
mk("HBU01","Real Price of a Movie Ticket Over 50 Years","Adjusted for inflation tickets are barely more expensive but the experience got worse","CHART","US-national","Line chart","Prices|Entertainment|History","NATO: Box Office Data (natoonline.org); BLS: CPI (bls.gov)",62,80,78,72,58,65,70,88),
mk("HBU02","Concert Ticket Price Explosion Since Ticketmaster Merged With Live Nation","Prices doubled in a decade after the merger","CHART","US-national","Line chart","Prices|Entertainment|Economy","Billboard: Touring Data; BLS: CPI Recreation (bls.gov)",75,82,78,78,72,65,72,78),
mk("HBU03","Real Cost of a Thanksgiving Dinner Over 30 Years","USDA tracks the same basket of goods every year","CHART","US-national","Line chart","Prices|Food|History","USDA: Thanksgiving Dinner Cost Survey (usda.gov); BLS: Food CPI (bls.gov)",62,82,80,68,55,65,65,90),
mk("HBU04","Used Car Prices vs. New Car Prices Over Time","The used car market went insane during COVID and never fully recovered","CHART","US-national","Line chart","Prices|Economy|Transportation","Manheim: Used Vehicle Index (manheim.com); BLS: CPI New Vehicles (bls.gov)",72,85,78,72,68,65,68,85),
mk("HBU05","Healthcare Premium Growth vs. Wage Growth Since 2000","Insurance costs grew 4x faster than paychecks","CHART","US-national","Line chart","Prices|Health|Economy|Labor","KFF: Employer Health Benefits (kff.org); BLS: Average Hourly Earnings (bls.gov)",85,88,80,78,82,65,68,90),
# === Labor × Geography ===
mk("HBU06","Right to Work States vs. Median Wage","Do anti-union laws correlate with lower pay?","XREF","US-state","Scatter plot","Labor|Geography|Politics","NRTW: State Laws (nrtw.org); BLS: QCEW Wages (bls.gov); Census: Median Income (census.gov)",72,72,75,78,72,68,72,88),
mk("HBU07","The Work From Home Map","Percentage of workers fully remote by metro area","MAP","US-metro","Dot map","Labor|Geography|Technology","Census: ACS Work From Home (census.gov); Kastle: Back to Work (kastle.com)",72,85,78,68,62,78,68,78),
mk("HBU08","Tipped Worker Minimum Wage by State","From 2.13 per hour in 15 states to the full minimum in others","MAP","US-state","State choropleth","Labor|Economy|Inequality","DOL: Minimum Wages for Tipped Employees (dol.gov)",80,82,80,78,78,78,68,92),
# === Housing × Crime ===
mk("HBU09","Airbnb Concentration vs. Noise Complaints by Neighborhood","Short-term rentals change the character of residential areas","XREF","US-city","Scatter plot","Housing|Crime|Technology","Kaggle: Airbnb Listings (kaggle.com/datasets/airbnb); NYC: 311 Complaints (data.cityofnewyork.us)",65,72,70,72,62,68,72,68),
mk("HBU10","Foreclosure Rate by County During the 2008 Crisis vs. Today","Are we headed for a repeat?","MAP","US-county","Bivariate choropleth","Housing|Finance|History","ATTOM: Foreclosure Data (attomdata.com); Census: ACS Housing (census.gov)",78,78,72,78,78,80,68,82),
# === International × Education ===
mk("HBU11","School Days Per Year by Country","Japanese students attend 243 days while Americans attend 180","MAP","World","World choropleth","International|Education","UNESCO: Education Data (uis.unesco.org); OECD: Education at a Glance (oecd.org)",62,72,80,78,58,78,68,88),
mk("HBU12","Literacy Rate by Country: The Remaining Illiteracy Map","800 million adults still cant read","MAP","World","World choropleth","International|Education","UNESCO: Literacy Data (uis.unesco.org); World Bank: Literacy Rate (worldbank.org)",75,65,80,72,72,78,65,90),
# === Climate × Politics ===
mk("HBU13","Climate Denial vs. Climate Damage by Congressional District","Representatives who deny climate change often represent the districts hit hardest","XREF","US-state","Bivariate choropleth","Climate|Politics|Environment","NOAA: Billion-Dollar Disasters (ncei.noaa.gov); LCV: Scorecard (lcv.org)",82,72,68,82,85,78,78,78),
mk("HBU14","Carbon Tax Adoption by Country","Which nations have put a price on carbon and how much","MAP","World","World choropleth","Climate|Politics|International","World Bank: Carbon Pricing Dashboard (carbonpricingdashboard.worldbank.org)",65,58,78,72,68,78,68,88),
# === Crime × Gender ===
mk("HBU15","Domestic Violence Report Rate by State","Some states have 3x the reporting rate and its not because of more violence","MAP","US-state","State choropleth","Crime|Gender|Health","FBI: UCR Domestic Violence (fbi.gov); NCADV: State Statistics (ncadv.org)",78,72,72,72,78,78,68,78),
mk("HBU16","Sexual Assault Kit Backlog by State","Hundreds of thousands of untested rape kits mapped","MAP","US-state","State choropleth","Crime|Gender|Law","End the Backlog: Kit Counts (endthebacklog.org); NIJ: SAKI Data (nij.gov)",82,72,72,80,85,78,72,72),
# === Economy × Agriculture ===
mk("HBU17","Farmer Suicide Rate vs. Crop Price Index","When commodity prices crash farm suicides spike","XREF","US-national","Line chart","Economy|Agriculture|Health","CDC: WONDER Suicide by Occupation (wonder.cdc.gov); USDA: Crop Prices (usda.gov)",85,68,68,82,82,65,78,72),
mk("HBU18","Food Waste By Stage of Supply Chain","40% of US food is wasted — heres where in the chain it happens","CHART","US-national","Treemap","Agriculture|Food|Environment","USDA: Food Loss and Waste (ers.usda.gov); EPA: Food Recovery (epa.gov)",72,75,78,78,68,72,68,85),
# === Health × Race ===
mk("HBU19","Clinical Trial Drug Efficacy by Race","Most drugs are tested primarily on white men but prescribed to everyone","CHART","US-national","Bar chart","Health|Race|Science","FDA: Drug Trials Snapshots (fda.gov); NIH: All of Us Research (allofus.nih.gov)",78,68,72,82,78,65,80,72),
mk("HBU20","Environmental Racism Map: Toxic Sites Near Minority Communities","EPA Superfund and TRI sites cluster in majority-minority ZIP codes","MAP","US-county","Bivariate choropleth","Health|Race|Environment","EPA: EJScreen (epa.gov/ejscreen); Census: ACS Race (census.gov)",85,72,68,78,85,80,72,85),
# === Economy × Education ===
mk("HBU21","Student Loan Debt Per Graduate by State","From 20K in Utah to 40K in Connecticut","MAP","US-state","State choropleth","Economy|Education|Finance","TICAS: Student Debt by State (ticas.org); ED: College Scorecard (collegescorecard.ed.gov)",82,85,78,72,78,78,68,88),
mk("HBU22","For-Profit College Graduate Earnings vs. Traditional College","For-profit grads earn less and default more","XREF","US-national","Scatter plot","Economy|Education","ED: College Scorecard (collegescorecard.ed.gov); Census: ACS Earnings (census.gov)",78,78,78,80,78,65,72,85),
# === War × Demographics ===
mk("HBU23","The Draft Lottery Map: Who Would Serve Today","Using current demographics to visualize a hypothetical modern draft","MAP","US-county","County choropleth","War|Demographics|Military","Census: ACS Age/Sex (census.gov); DoD: Demographic Profile (militaryonesource.mil)",65,72,68,78,72,80,78,68),
mk("HBU24","Military Veteran Homelessness by City","Vets make up 8% of the population but 11% of the homeless","MAP","US-city","Dot map","War|Housing|Poverty","HUD: AHAR Veterans Data (hudexchange.info); VA: Homeless Veterans (va.gov)",82,72,72,72,80,78,68,82),
# === Remaining combos ===
mk("HBU25","The Opioid Pipeline: From Pharma Marketing to Overdose Deaths","Purdue Pharma marketing spend by region mapped against overdose rates","XREF","US-state","Bivariate choropleth","Drugs|Economy|Health","WashPost: DEA Pain Pill Database (washingtonpost.com); CDC: Overdose Maps (cdc.gov)",85,78,68,78,85,78,72,82),
mk("HBU26","Flood Insurance Costs vs. Actual Flood Risk","NFIP pricing doesnt match reality leaving taxpayers subsidizing coastal mansions","XREF","US-county","Scatter plot","Finance|Climate|Housing","FEMA: NFIP Policy Data (fema.gov); First Street: Flood Factor (firststreet.org)",72,68,72,78,72,68,75,78),
mk("HBU27","Americas Crumbling Sewer Systems","Combined sewer overflow events mapped — raw sewage in your waterways","MAP","US-city","Dot map","Infrastructure|Environment|Health","EPA: CSO Outfalls (epa.gov); ASCE: Wastewater Grade (infrastructurereportcard.org)",75,68,72,75,75,78,72,82),
mk("HBU28","The Most Segregated Cities in America by Multiple Measures","Dissimilarity index exposure index and isolation index compared","RANK","US-metro","Bar chart","Race|Housing|Demographics","Census: ACS Segregation Measures (census.gov); Brookings: Metro Segregation (brookings.edu)",82,72,72,72,80,68,68,85),
mk("HBU29","Countries Where Women Cant Legally Do What Men Can","Driving banking inheriting traveling — the restrictions that remain","MAP","World","World choropleth","Gender|International|Law","World Bank: Women Business and Law (worldbank.org)",80,72,78,78,78,78,68,85),
mk("HBU30","The Price of Water in Every US City","From Detroits crisis to Frescos near-free water","MAP","US-city","Dot map","Prices|Infrastructure|Geography","Circle of Blue: Water Pricing (circleofblue.org)",68,72,75,72,65,78,68,82),
mk("HBU31","Americas Abandoned Mines","Over 500000 abandoned mine sites that still leak toxins","MAP","US-national","Dot map","Environment|History|Health","BLM: Abandoned Mine Lands (blm.gov); EPA: Mining Sites (epa.gov)",72,62,72,78,72,82,72,82),
mk("HBU32","The Dunbar Number Test: Average Social Circle Size by Country","How many real friends does the average person have globally","MAP","World","World choropleth","Psychology|International|Demographics","Gallup: World Poll Social Support (gallup.com); Oxford: Social Brain Hypothesis",65,68,68,82,58,72,80,68),
mk("HBU33","Americas Invasive Species Map","Where kudzu fire ants zebra mussels and Asian carp have taken over","MAP","US-national","Dot map","Environment|Science|Agriculture","USGS: Nonindigenous Aquatic Species (usgs.gov); USDA: APHIS (aphis.usda.gov)",60,58,72,72,58,82,72,85),
mk("HBU34","Every Amtrak Route Colored by On-Time Performance","The map of where Americas passenger trains actually run on schedule","MAP","US-national","Line map","Transportation|Infrastructure","Amtrak: Performance Data (amtrak.com); BTS: Rail Statistics (bts.gov)",62,72,78,72,58,82,68,85),
mk("HBU35","The Child Care Desert Map","ZIP codes where demand for childcare slots exceeds supply by 3x","MAP","US-county","County choropleth","Children|Economy|Labor","CAP: Child Care Deserts (americanprogress.org); Census: ACS Children Under 5 (census.gov)",82,82,72,72,78,80,68,82),
]

# --- inject ---
with open(DATA, 'r', encoding='utf-8') as f:
    txt = f.read()
ids = set(re.findall(r'id:"([^"]+)"', txt))
new = [i for i in IDEAS if re.search(r'id:"([^"]+)"', i).group(1) not in ids]
if not new:
    print("All HBU ideas already present"); exit()
tail = "]; // end D"
txt = txt.replace(tail, ",\n".join(new) + ",\n" + tail)
with open(DATA, 'w', encoding='utf-8') as f:
    f.write(txt)
print(f"Injected {len(new)} new ideas (HBU batch)")
