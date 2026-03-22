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
# === "America in Decline?" debate series ===
mk("HBT01","Americas Global Rankings Over 50 Years","Where the US used to rank 1st and where it ranks now across 20 metrics","CHART","World","Line chart","International|History|Economy","Various: WHO OECD World Bank Rankings Over Time",82,78,78,78,80,68,72,78),
mk("HBT02","Infrastructure Grade by Category Since 2001","The ASCE report card shows mostly Cs and Ds for 20 years running","CHART","US-national","Bar chart","Infrastructure|Economy|History","ASCE: Infrastructure Report Card (infrastructurereportcard.org)",72,72,82,72,72,65,65,92),
mk("HBT03","US Math and Science Rankings Among Developed Nations Over Time","We went from top 5 to bottom third in a generation","CHART","World","Line chart","Education|International|History","OECD: PISA Results (oecd.org/pisa); TIMSS: International Results (timss.bc.edu)",78,75,78,78,78,65,68,88),
mk("HBT04","Trust in Government From 1960 to Today","From 77% trusting the government to do the right thing to 20%","CHART","US-national","Line chart","Politics|History|Psychology","Pew: Public Trust in Government (pewresearch.org); Gallup: Trust (gallup.com)",78,78,80,72,78,65,65,90),
mk("HBT05","The Declining Third Place","Libraries bowling alleys community centers and churches per capita over time","CHART","US-national","Line chart","Demographics|History|Psychology","IMLS: Library Data (imls.gov); Census: County Business Patterns (census.gov)",78,78,72,78,72,65,78,78),
# === Inequality × History ===
mk("HBT06","CEO to Worker Pay Ratio by Decade","From 20:1 in 1965 to 399:1 in 2021 animated","CHART","US-national","Animated bar chart","Inequality|History|Economy","EPI: CEO Pay (epi.org); BLS: Employment Cost Index (bls.gov)",88,85,82,78,85,72,68,92),
mk("HBT07","Top 1% Income Share by Country Over 100 Years","The U-shaped curve of inequality in the 20th century","CHART","World","Line chart","Inequality|History|International","World Inequality Database (wid.world)",78,68,75,78,78,68,72,88),
mk("HBT08","Union Membership Decline Timeline by Industry","Which sectors lost their unions first and fastest","CHART","US-national","Area chart","Inequality|History|Labor","BLS: Union Members (bls.gov); Historical: Union Density Data",75,72,78,72,72,68,68,90),
# === Children × Education ===
mk("HBT09","Kindergarten Readiness by Family Income","Rich kids arrive at school already a year ahead of poor kids","CHART","US-national","Bar chart","Children|Education|Inequality","Stanford: CEPA Achievement Gap (cepa.stanford.edu); NCES: ECLS-K (nces.ed.gov)",82,78,78,78,78,65,72,80),
mk("HBT10","After-School Program Availability by County Income","Wealthy counties have 3x more youth programs per capita","MAP","US-county","Bivariate choropleth","Children|Education|Inequality","Afterschool Alliance: America After 3PM (afterschoolalliance.org); Census: SAIPE (census.gov)",78,78,72,72,72,78,68,72),
# === Immigration × Health ===
mk("HBT11","The Immigrant Health Paradox","Foreign-born Americans live longer than native-born despite lower incomes","CHART","US-national","Bar chart","Immigration|Health|Demographics","CDC: NCHS Nativity and Mortality (cdc.gov/nchs); Census: ACS Foreign-Born (census.gov)",68,68,72,88,62,65,82,82),
mk("HBT12","Immigrant Doctor Share by State","Over 25% of US physicians are foreign-born and some states depend on them even more","MAP","US-state","State choropleth","Immigration|Health|Labor","AAMC: International Medical Graduates (aamc.org); Census: ACS Nativity by Occupation (census.gov)",68,68,78,78,62,78,72,85),
# === Sports × Health ===
mk("HBT13","CTE Diagnosis Rate by Sport","Football dominates but soccer hockey and wrestling are rising","CHART","US-national","Bar chart","Sports|Health|Science","BU: CTE Center (bu.edu/cte); CDC: Traumatic Brain Injury (cdc.gov/traumaticbraininjury)",78,72,75,78,78,65,72,72),
mk("HBT14","Youth Sports Participation Cost by Sport","Ice hockey costs families 15x more per year than track and field","RANK","US-national","Bar chart","Sports|Economy|Children","Aspen Institute: State of Play (aspenprojectplay.org); Utah State: Youth Sports Costs",72,82,78,72,65,65,68,75),
# === Energy × Health ===
mk("HBT15","Coal Plant Proximity and Childhood Asthma Hospitalization","Kids near coal plants are hospitalized for asthma at higher rates","XREF","US-county","Bivariate choropleth","Energy|Health|Children|Environment","EPA: Power Plant Locations (epa.gov); HCUP: Kids Inpatient Database (ahrq.gov)",82,72,68,78,80,78,72,75),
mk("HBT16","Power Plant Water Consumption by Type","Thermoelectric plants use 40% of all US freshwater withdrawals","CHART","US-national","Bar chart","Energy|Environment|Infrastructure","USGS: Water Use (usgs.gov); EIA: Electric Power (eia.gov)",65,58,78,82,65,65,72,90),
# === Poverty × Transportation ===
mk("HBT17","Transit Deserts and Job Access","Neighborhoods without public transit and the jobs they cant reach","MAP","US-metro","Bivariate choropleth","Poverty|Transportation|Labor","Brookings: Transit Job Access (brookings.edu); NTD: Service Area (transit.dot.gov)",80,78,72,72,78,78,72,78),
mk("HBT18","Car Ownership Rate by Income Quartile","The bottom 20% of earners are 6x less likely to own a car","CHART","US-national","Bar chart","Poverty|Transportation|Inequality","Census: ACS Vehicle Availability (census.gov); BLS: Consumer Expenditure (bls.gov)",75,78,78,72,72,65,68,88),
# === Democracy × Technology ===
mk("HBT19","Voting Machine Type by County and Error Rate","Some counties still use machines with known vulnerabilities","MAP","US-county","County choropleth","Democracy|Technology|Politics","Verified Voting: Voting Equipment (verifiedvoting.org); EAC: Election Administration (eac.gov)",72,68,72,78,78,78,75,78),
mk("HBT20","Social Media Political Ad Spending by Platform and Party","Where campaigns spend their digital dollars","CHART","US-national","Treemap","Democracy|Technology|Politics|Media","Meta: Ad Library (facebook.com/ads/library); Google: Political Ads (transparencyreport.google.com)",68,68,75,72,68,72,68,82),
# === Economy × Religion ===
mk("HBT21","Prosperity Gospel Church Revenue vs. Community Poverty Rate","Megachurches in the poorest neighborhoods","XREF","US-county","Scatter plot","Economy|Religion|Poverty","IRS: Tax-Exempt Organizations (irs.gov); Census: SAIPE (census.gov)",78,72,68,82,78,68,80,62),
mk("HBT22","Religious Tax Exemptions Total Value by State","The untaxed billions of church property","MAP","US-state","State choropleth","Economy|Religion|Politics","SEC/CREW: Religious Tax Exemption Studies; Census: Property Tax Data (census.gov)",72,68,72,80,72,78,78,65),
# === International × Health ===
mk("HBT23","Countries Where Doctors Emigrate vs. Where They Immigrate","The global brain drain of medical professionals","MAP","World","Line map","International|Health|Immigration","WHO: Health Workforce Migration (who.int); OECD: Health Migration (oecd.org)",72,62,72,78,72,82,72,80),
mk("HBT24","Childhood Stunting Rate by Country","Where malnutrition is literally making children shorter","MAP","World","World choropleth","International|Health|Children|Food","WHO: Malnutrition Data (who.int); UNICEF: Nutrition (data.unicef.org)",80,65,78,72,78,78,68,88),
mk("HBT25","Hospital Beds Per Capita by Country","The US has fewer hospital beds per person than Cuba","MAP","World","World choropleth","International|Health|Infrastructure","WHO: Hospital Bed Density (who.int); OECD: Health Resources (oecd.org)",72,68,80,82,68,78,68,90),
# === Agriculture × International ===
mk("HBT26","Countries Most Dependent on Food Imports","Island and desert nations that import 90%+ of their food","MAP","World","World choropleth","Agriculture|International|Trade","FAO: Food Balance Sheets (fao.org); WTO: Trade Statistics (wto.org)",68,62,78,78,68,78,68,85),
mk("HBT27","Arable Land Per Capita by Country Over Time","Were feeding more people with less farmland than ever before","CHART","World","Line chart","Agriculture|International|Science","FAO: Land Use Data (fao.org); World Bank: Arable Land (worldbank.org)",65,58,78,78,65,68,72,88),
# === Crime × Finance ===
mk("HBT28","Wage Theft vs. All Other Property Crime Combined","Employers steal more from workers than all robberies and burglaries combined","CHART","US-national","Bar chart","Crime|Finance|Labor|Inequality","EPI: Wage Theft (epi.org); FBI: UCR Property Crime (fbi.gov)",82,78,78,88,80,65,82,78),
mk("HBT29","White Collar Crime Prosecution Rate vs. Street Crime","Financial crimes are caught less often and punished less severely","CHART","US-national","Bar chart","Crime|Finance|Inequality","DOJ: White Collar Crime (justice.gov); FBI: UCR (fbi.gov); SEC: Enforcement (sec.gov)",78,72,75,80,78,65,78,72),
# === Remaining novel combos ===
mk("HBT30","The Most Gerrymandered Districts in America Using Compactness Score","Polsby-Popper scores reveal the most absurdly drawn districts","MAP","US-state","Special map","Politics|Democracy|Geography","Census: Congressional Districts (census.gov); Metric Geometry: Gerrymandering Group (mggg.org)",75,68,72,78,78,85,72,85),
mk("HBT31","Americas Hidden Homeless: People Living in Cars by Metro","Vehicle residency is the fastest growing form of homelessness","MAP","US-metro","Dot map","Housing|Poverty|Transportation","HUD: Point-in-Time Count (hudexchange.info); National Alliance: Homelessness (naeh.org)",82,78,68,78,80,78,78,68),
mk("HBT32","Microplastics Found in Human Blood by Country","Every person tested has plastic in their blood","MAP","World","World choropleth","Science|Health|Environment","Environment International: Microplastics Study; WHO: Microplastics Report (who.int)",78,72,68,85,78,72,78,65),
mk("HBT33","The Most Common Cause of Death by Age Group","Accidents for young people then cancer then heart disease — the crossover points","CHART","US-national","Area chart","Health|Demographics|Science","CDC: Leading Causes of Death (cdc.gov); IHME: GBD Compare (healthdata.org)",72,78,82,72,68,68,65,92),
mk("HBT34","Percentage of Income Spent on Food by Country","Americans spend 6% while Nigerians spend 56%","MAP","World","World choropleth","Food|International|Economy","USDA: Food Expenditures (ers.usda.gov); World Bank: Household Expenditure (worldbank.org)",68,72,82,80,62,78,68,88),
mk("HBT35","The Friendship Recession","Average number of close friends reported by Americans over time","CHART","US-national","Line chart","Psychology|Demographics|History","Survey Center on American Life: Friendship (americansurveycenter.org); GSS: Social Surveys (gss.norc.org)",80,82,75,78,75,65,72,78),
]

# --- inject ---
with open(DATA, 'r', encoding='utf-8') as f:
    txt = f.read()
ids = set(re.findall(r'id:"([^"]+)"', txt))
new = [i for i in IDEAS if re.search(r'id:"([^"]+)"', i).group(1) not in ids]
if not new:
    print("All HBT ideas already present"); exit()
tail = "]; // end D"
txt = txt.replace(tail, ",\n".join(new) + ",\n" + tail)
with open(DATA, 'w', encoding='utf-8') as f:
    f.write(txt)
print(f"Injected {len(new)} new ideas (HBT batch)")
