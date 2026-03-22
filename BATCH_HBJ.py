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
# === "Counterintuitive Truth" — the hook is the surprise ===
mk("HBJ01","The Safest Countries Are Not the Richest","Some middle-income nations outperform wealthy ones on safety indexes","XREF","World","Scatter plot","Crime|International|Economy","UNODC: Crime Statistics (unodc.org); World Bank: GNI Per Capita (worldbank.org)",68,65,75,82,68,68,78,85),
mk("HBJ02","More Americans Die From Cows Than Sharks","Annual death counts from surprising animal encounters","RANK","US-national","Bar chart","Health|Science|Humor","CDC: WONDER Mortality (wonder.cdc.gov); ISAF: Shark Attack File (floridamuseum.ufl.edu)",55,72,82,90,50,62,82,82),
mk("HBJ03","Countries With the Longest Work Hours Have Lower Productivity","Working harder doesnt mean working smarter","XREF","World","Scatter plot","Labor|International|Economy","OECD: Hours Worked (oecd.org); OECD: GDP per Hour Worked (oecd.org)",72,72,80,85,68,65,78,90),
mk("HBJ04","US States With Strictest Drug Laws vs. Drug Usage Rates","Enforcement intensity doesnt correlate with lower usage","XREF","US-state","Scatter plot","Drugs|Crime|Law","SAMHSA: NSDUH State Data (samhsa.gov); NCSL: Drug Policy (ncsl.org)",72,68,72,82,75,65,80,78),
mk("HBJ05","The Happiest Countries Tax Their Citizens the Most","Scandinavian paradox: high taxes correlate with high satisfaction","XREF","World","Scatter plot","International|Economy|Psychology","World Happiness Report (worldhappiness.report); OECD: Tax Revenue (oecd.org)",75,72,78,85,68,68,78,88),
# === Education × Race ===
mk("HBJ06","Segregation in Schools Is Worse Now Than in 1968","After peaking in the 1980s integration has reversed","CHART","US-national","Line chart","Education|Race|History","UCLA: Civil Rights Project (civilrightsproject.ucla.edu); NCES: School Composition (nces.ed.gov)",85,75,72,82,82,68,72,85),
mk("HBJ07","School Suspension Rate by Race Within the Same District","Black students suspended at 4x the rate for same offenses","XREF","US-national","Bar chart","Education|Race|Crime|Inequality","ED: Civil Rights Data Collection (ed.gov/ocr); Census: ACS Demographics (census.gov)",85,75,75,78,82,65,72,85),
# === Economy × Health ===
mk("HBJ08","Medical Bankruptcy as a Percentage of All Bankruptcies","Two-thirds of US bankruptcies are linked to medical debt","CHART","US-national","Area chart","Economy|Health|Finance","American Journal of Public Health: Medical Bankruptcy Study; Census: SIPP (census.gov)",88,85,78,78,82,65,70,78),
mk("HBJ09","Healthcare Spending Per Capita vs. Health Outcomes by Country","America spends the most and gets some of the worst results","XREF","World","Scatter plot","Economy|Health|International","OECD: Health Expenditure (oecd.org); WHO: Health Statistics (who.int)",85,78,80,82,82,68,68,92),
mk("HBJ10","Counties Where Life Expectancy Decreased Since 2000","Its not supposed to go backwards in a developed nation","MAP","US-county","County choropleth","Health|Economy|Demographics","CDC: US Small-area Life Expectancy (cdc.gov/nchs); Census: ACS (census.gov)",85,78,78,82,85,80,72,85),
# === Housing × Education ===
mk("HBJ11","School District Boundaries Are Americas Most Powerful Segregation Tool","Home values jump at district lines","MAP","US-metro","Special map","Housing|Education|Race|Inequality","Zillow: Home Values by ZIP (zillow.com/research); NCES: District Boundaries (nces.ed.gov)",82,78,68,78,82,82,78,78),
mk("HBJ12","Property Tax Funding Creates a Cycle of Inequality","Rich districts get more money from higher home values perpetuating the gap","XREF","US-county","Bivariate choropleth","Housing|Education|Inequality","Census: School Finance (census.gov); Census: ACS Home Values (census.gov)",82,78,75,75,80,78,72,85),
# === Crime × Race ===
mk("HBJ13","Police Stops Per Capita by Race in Every State","The magnitude of the disparity varies wildly by geography","XREF","US-state","Bar chart","Crime|Race|Law","Stanford: Open Policing Project (openpolicing.stanford.edu)",82,75,75,78,82,65,72,82),
mk("HBJ14","Cash Bail Amount for Same Offense by Defendant Race","Identical charges result in different bail amounts","CHART","US-national","Bar chart","Crime|Race|Inequality|Law","Measures for Justice: County Data (measuresforjustice.org); Vera: Bail Data (vera.org)",85,72,72,80,85,65,78,72),
# === Environment × Agriculture ===
mk("HBJ15","Fertilizer Runoff and the Dead Zone in the Gulf of Mexico","Farm chemicals flow down the Mississippi and kill the ocean","MAP","US-national","Special map","Environment|Agriculture|Health","NOAA: Gulf Hypoxia (gulfhypoxia.net); USGS: Nutrient Loads (usgs.gov)",78,65,72,78,78,85,72,85),
mk("HBJ16","Pesticide Use by County Overlaid With Cancer Clusters","Agricultural chemical exposure mapped against health outcomes","XREF","US-county","Bivariate choropleth","Environment|Agriculture|Health","USGS: Pesticide National Synthesis (usgs.gov); CDC: Cancer Statistics (cdc.gov/cancer)",82,68,68,78,82,78,75,75),
# === Economy × International — "America vs. the World" ===
mk("HBJ17","US Healthcare Spending vs. Every Other Developed Nation on One Chart","Were the outlier on the scatter plot and not in a good way","XREF","World","Scatter plot","Economy|Health|International","OECD: Health Expenditure (oecd.org); WHO: UHC Service Coverage (who.int)",85,78,82,78,82,68,65,92),
mk("HBJ18","Paid Maternity Leave: US vs. Literally Every Other Country","Americas zero federally mandated weeks mapped against the world","MAP","World","World choropleth","Labor|Gender|International","ILO: Maternity Protection (ilo.org); OECD: Family Database (oecd.org)",85,82,82,80,78,78,68,90),
mk("HBJ19","Mass Shootings Per Capita: US vs. Other Developed Nations","The chart that needs no explanation","CHART","World","Bar chart","Guns|International|Crime","Gun Violence Archive (gunviolencearchive.org); Small Arms Survey (smallarmssurvey.org)",82,75,80,72,82,65,62,85),
mk("HBJ20","Incarceration Rate: US vs. Every Other Country","America has 4% of the worlds people and 20% of its prisoners","RANK","World","Bar chart","Crime|International|Law","World Prison Brief (prisonstudies.org); Census: Population (census.gov)",82,72,82,80,82,65,65,92),
# === Technology × Demographics ===
mk("HBJ21","The Age Digital Divide in America","Internet usage skills and device ownership by age bracket","CHART","US-national","Bar chart","Technology|Demographics","Pew: Internet and Technology (pewresearch.org); Census: Computer and Internet Use (census.gov)",72,78,80,68,65,65,65,85),
mk("HBJ22","Smart Speaker Ownership by Income Bracket","Whos letting Amazon and Google listen in their homes","CHART","US-national","Bar chart","Technology|Demographics|Economy","Pew: Smart Speaker Survey (pewresearch.org); NPR/Edison: Smart Audio Report (nationalpublicmedia.com)",62,75,78,72,58,65,72,72),
# === "Historical What If" counterfactual data viz ===
mk("HBJ23","If Minimum Wage Kept Up With Productivity Since 1968","It would be over 24 per hour today","CHART","US-national","Line chart","Economy|Labor|History|Inequality","EPI: Minimum Wage (epi.org); BLS: Productivity Data (bls.gov)",88,85,82,82,82,68,72,90),
mk("HBJ24","If Black Family Wealth Grew at White Family Rates Since 1968","The compounding cost of the racial wealth gap","CHART","US-national","Line chart","Race|Economy|History|Inequality","Fed: Survey of Consumer Finances (federalreserve.gov); Brookings: Racial Wealth Gap (brookings.edu)",88,75,72,82,85,68,78,78),
mk("HBJ25","If CO2 Emissions Had Peaked in 2000","Projected vs. actual temperature trajectory divergence","CHART","World","Line chart","Climate|Science|History","IPCC: Emissions Scenarios (ipcc.ch); Global Carbon Project (globalcarbonproject.org)",78,65,72,78,78,68,78,82),
# === "The Infrastructure Countdown" ===
mk("HBJ26","Average Age of Americas Bridges by State","Some states are driving on 60+ year old bridges daily","MAP","US-state","State choropleth","Infrastructure|Transportation","FHWA: National Bridge Inventory (fhwa.dot.gov)",72,75,78,72,72,78,65,92),
mk("HBJ27","Americas Water Pipe System Is Older Than You Think","Average age of water mains by city — many exceed 100 years","RANK","US-city","Bar chart","Infrastructure|Health","AWWA: Buried Infrastructure (awwa.org); EPA: Drinking Water Infrastructure Needs (epa.gov)",75,72,75,78,75,65,72,78),
mk("HBJ28","The Dam Safety Crisis Map","High-hazard dams rated in poor or unsatisfactory condition","MAP","US-national","Dot map","Infrastructure|Environment","ASCE: Dam Safety (infrastructurereportcard.org); USACE: National Inventory of Dams (nid.sec.usace.army.mil)",72,65,72,78,78,82,72,88),
# === Remaining novel combos ===
mk("HBJ29","Countries Where Teachers Are Paid More Than Doctors","The nations that truly value education","RANK","World","Bar chart","Education|International|Labor","OECD: Teachers Salaries (oecd.org); OECD: Health Workforce Remuneration (oecd.org)",68,65,78,88,65,65,82,78),
mk("HBJ30","The Loneliest Counties in America","Social isolation index based on single-person households living alone rate and social org density","MAP","US-county","County choropleth","Psychology|Demographics|Health","Census: ACS Households (census.gov); HRSA: Social Vulnerability (data.hrsa.gov)",78,78,72,75,72,80,75,78),
mk("HBJ31","Every US County Colored by Its Largest Employer","Government dominates rural America while tech dominates coastal metros","MAP","US-county","County choropleth","Economy|Labor|Geography","Census: County Business Patterns (census.gov); BLS: QCEW (bls.gov)",65,72,78,72,60,82,70,88),
mk("HBJ32","Commute Time vs. Happiness Score by Metro","After 30 minutes each additional minute of commute measurably reduces life satisfaction","XREF","US-metro","Scatter plot","Transportation|Psychology|Economy","Census: ACS Commuting (census.gov); Gallup: Wellbeing Index (gallup.com)",75,82,75,78,68,65,72,78),
mk("HBJ33","The Most and Least Trusted Professions Over Time","Nurses at the top and Congress at the bottom for 20 straight years","CHART","US-national","Line chart","Labor|Politics|Health","Gallup: Honesty and Ethics Poll (gallup.com)",68,78,80,72,62,65,65,88),
mk("HBJ34","Americas Crumbling School Buildings","Average age of K-12 school buildings by state","MAP","US-state","State choropleth","Education|Infrastructure","NCES: Condition of Public School Facilities (nces.ed.gov); GAO: School Facilities (gao.gov)",78,78,75,72,75,78,68,80),
mk("HBJ35","State Pension Funding Ratio Map","How underfunded your states retirement promises are","MAP","US-state","State choropleth","Finance|Politics|Economy","Pew: State Pension Funding (pewtrusts.org); Equable: State of Pensions (equable.org)",72,70,78,75,75,78,70,88),
]

# --- inject ---
with open(DATA, 'r', encoding='utf-8') as f:
    txt = f.read()
ids = set(re.findall(r'id:"([^"]+)"', txt))
new = [i for i in IDEAS if re.search(r'id:"([^"]+)"', i).group(1) not in ids]
if not new:
    print("All HBJ ideas already present"); exit()
tail = "]; // end D"
txt = txt.replace(tail, ",\n".join(new) + ",\n" + tail)
with open(DATA, 'w', encoding='utf-8') as f:
    f.write(txt)
print(f"Injected {len(new)} new ideas (HBJ batch)")
