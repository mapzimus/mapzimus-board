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
# === "Why Does X Predict Y" — surprising correlations with actual causal theories ===
mk("HBF01","Why Does Ice Cream Sales Predict Murder Rate","Both spike in summer — the classic confounding variable lesson","XREF","US-national","Line chart","Science|Crime|Food","USDA: Dairy Sales (ers.usda.gov); FBI: UCR Monthly Crime (fbi.gov)",65,72,82,85,58,65,78,82),
mk("HBF02","Why Does Shoe Size Predict Reading Level","Age is the lurking variable — a stats 101 visualization","XREF","US-national","Scatter plot","Science|Education","NIH: Child Development Data (nichd.nih.gov); NAEP: Reading Assessment (nces.ed.gov)",55,68,82,85,50,62,80,65),
mk("HBF03","Why Do States With More Country Music Have Higher Suicide Rates","A real published study with a wild finding and a real explanation","XREF","US-state","Scatter plot","Science|Health|Entertainment","Social Forces Journal: Stack and Gundlach 1992; CDC: WONDER Suicide (wonder.cdc.gov)",68,65,70,92,65,62,88,68),
# === Infrastructure × International ===
mk("HBF04","High Speed Rail Networks: US vs. Europe vs. China","Americas embarrassing gap in passenger rail","MAP","World","Special map","Infrastructure|International|Transportation","UIC: High Speed Rail Atlas (uic.org); FRA: US Rail Network (fra.dot.gov)",72,72,80,78,72,85,68,88),
mk("HBF05","Bridges Rated Structurally Deficient by Country","The US has more crumbling bridges than most people realize","RANK","World","Bar chart","Infrastructure|International","ASCE: Infrastructure Report Card (infrastructurereportcard.org); OECD: Infrastructure (oecd.org)",72,70,78,78,72,65,68,82),
mk("HBF06","Percentage of Roads That Are Unpaved by Country","Over half the worlds roads are still dirt","MAP","World","World choropleth","Infrastructure|International|Transportation","CIA: World Factbook (cia.gov); IRF: World Road Statistics (irf.global)",65,60,78,78,62,80,70,85),
# === Housing × Race ===
mk("HBF07","Black Homeownership Rate by Metro Then vs. Now","The gap has barely closed in 50 years in most cities","CHART","US-metro","Bar chart","Housing|Race|Inequality","Census: ACS Homeownership by Race (census.gov); National Archives: HMDA Historical (archives.gov)",85,78,75,75,82,68,72,88),
mk("HBF08","Home Appraisal Values: Same House Different Race of Owner","Controlled studies show Black-owned homes appraised lower","CHART","US-national","Bar chart","Housing|Race|Inequality","Brookings: Devaluation of Assets (brookings.edu); FHFA: Appraisal Data (fhfa.gov)",88,78,72,82,85,65,78,72),
# === Science × History ===
mk("HBF09","Scientific Papers Published Per Year Since 1665","Exponential growth of human knowledge","CHART","World","Area chart","Science|History|Technology","NSF: Science and Engineering Indicators (nsf.gov); Web of Science: Publication Counts (clarivate.com)",65,58,78,75,62,70,72,90),
mk("HBF10","The Nobel Prize Map","Countries by total Nobel laureates per capita","MAP","World","World choropleth","Science|International|History","Nobel Prize: Laureate Database (nobelprize.org); World Bank: Population (worldbank.org)",62,60,80,72,55,78,68,95),
mk("HBF11","Inventions Whose Country of Origin Surprises Everyone","Where common everyday things were actually invented","MAP","World","Dot map","Science|History|International","Smithsonian: Invention Database (si.edu); Patent Office Historical Records (uspto.gov)",60,68,75,82,55,78,80,72),
# === Economy × Gender ===
mk("HBF12","Pink Tax Map: Products That Cost More for Women","Identical products with gendered pricing differences by state","MAP","US-state","State choropleth","Economy|Gender|Prices","NYC DCA: From Cradle to Cane Study (nyc.gov); GAO: Gender Pricing (gao.gov)",80,85,78,78,75,72,72,72),
mk("HBF13","The Mommy Penalty vs. The Daddy Bonus","How having children affects earnings differently by gender","CHART","US-national","Line chart","Economy|Gender|Labor","Census: ACS Earnings (census.gov); Third Way: Parenthood Pay Gap (thirdway.org)",85,82,78,80,80,65,75,78),
mk("HBF14","Womens Workforce Participation Rate Over 100 Years","The curve from 20% to 57% and why it plateaued","CHART","US-national","Area chart","Gender|Labor|History","BLS: Historical Labor Force Data (bls.gov); Census: Historical Statistics (census.gov)",72,72,80,70,68,68,65,92),
# === "Maps That Break Your Brain" ===
mk("HBF15","Mercator vs. True Size: Countries at the Equator Are Massive","Africa is bigger than the US China India and Europe combined","MAP","World","World choropleth","Geography|International|Education","Natural Earth: Country Boundaries (naturalearthdata.com); True Size Project (thetruesize.com)",62,68,82,88,55,85,75,92),
mk("HBF16","The Map of Every Road in America and Nothing Else","Pure road network reveals population patterns without any population data","MAP","US-national","Line map","Geography|Infrastructure|Transportation","Census: TIGER Roads (census.gov)",55,60,78,78,48,92,78,95),
mk("HBF17","Earth at Night From Space","Light pollution as a proxy for development wealth and energy use","MAP","World","Special map","Geography|Energy|International","NASA: Black Marble (earthobservatory.nasa.gov); NOAA: VIIRS (ngdc.noaa.gov)",62,65,75,72,55,95,68,95),
mk("HBF18","River Basins of the United States Colored by Watershed","Every raindrop mapped to its eventual ocean destination","MAP","US-national","Special map","Geography|Environment","USGS: National Hydrography Dataset (usgs.gov); EPA: Watershed Boundaries (epa.gov)",55,58,72,72,48,95,75,95),
# === Poverty × Education ===
mk("HBF19","School District Funding vs. Child Poverty Rate","Rich districts spend 3x more per pupil than poor ones","XREF","US-county","Scatter plot","Poverty|Education|Inequality","Census: School Finance (census.gov); Census: SAIPE Child Poverty (census.gov)",85,80,78,78,82,68,70,90),
mk("HBF20","College Graduation Rate by Parents Income Bracket","Born rich? 77% graduate. Born poor? 11% do.","CHART","US-national","Bar chart","Poverty|Education|Inequality","Pell Institute: Indicators of Higher Education Equity (pellinstitute.org)",88,82,82,80,85,65,72,82),
# === Technology × Labor ===
mk("HBF21","Jobs Most Likely to Be Automated by AI","Ranked by exposure score with current employment numbers","RANK","US-national","Bar chart","Technology|Labor|Economy","OpenAI/UPenn: GPT Exposure Study (arxiv.org); BLS: OES (bls.gov)",82,85,78,78,82,68,72,80),
mk("HBF22","Average Days Spent in Office Per Week by Industry","The remote work revolution is wildly uneven across sectors","CHART","US-national","Bar chart","Technology|Labor","Kastle: Back to Work Barometer (kastle.com); BLS: American Time Use Survey (bls.gov)",72,85,80,68,65,65,68,75),
mk("HBF23","Gig Economy Workers as Percent of Workforce by Metro","Some cities are 25% gig workers and climbing","MAP","US-metro","Dot map","Technology|Labor|Economy","MBO Partners: State of Independence (mbopartners.com); Census: ACS Class of Worker (census.gov)",72,78,75,72,68,75,70,72),
# === Health × Geography — "place matters" ===
mk("HBF24","The Diabetes Belt","A continuous band across the South with 2x the national diabetes rate","MAP","US-county","County choropleth","Health|Geography|Food","CDC: Diabetes Atlas (cdc.gov/diabetes); Census: ACS (census.gov)",78,75,80,72,75,82,68,92),
mk("HBF25","Cancer Alley Louisiana","Petrochemical corridor cancer rates vs. plant locations","MAP","US-county","Dot map","Health|Geography|Environment","EPA: TRI Data (epa.gov/tri); CDC: Cancer Statistics (cdc.gov/cancer); Census: ACS (census.gov)",85,72,70,78,82,82,72,82),
mk("HBF26","Stroke Mortality Belt in the Southeast","The persistent geographic cluster that has puzzled epidemiologists","MAP","US-state","State choropleth","Health|Geography|Science","CDC: WONDER Cerebrovascular Disease (wonder.cdc.gov); NIH: Stroke Belt Research (nih.gov)",72,68,75,78,72,80,72,90),
# === Trade × Economy ===
mk("HBF27","What America Exports to Each Country","Top export category for every US trading partner","MAP","World","World choropleth","Trade|Economy|International","Census: Foreign Trade (census.gov); USITC: DataWeb (usitc.gov)",62,60,78,72,58,82,65,92),
mk("HBF28","Trade Deficit With China by Product Category","Electronics dominate but the surprises are in the details","CHART","US-national","Treemap","Trade|Economy|International","Census: USA Trade Online (census.gov); USITC: Trade DataWeb (usitc.gov)",68,65,78,72,68,72,68,90),
# === "The Last One" series — places where things are disappearing ===
mk("HBF29","The Last Blockbuster and the Last of 100 Other Chains","Map of final surviving locations of defunct retail chains","MAP","US-national","Dot map","Economy|History|Geography","ScrapeHero: Store Locations (scrapehero.com); Wikipedia: Defunct Retailers",62,78,75,78,58,80,80,62),
mk("HBF30","The Last Payphone in Every State","Where Americas abandoned communication infrastructure still stands","MAP","US-state","Dot map","Technology|History|Infrastructure","FCC: Payphone Data (fcc.gov); Payphone Project (payphone-project.com)",58,70,72,78,52,78,82,60),
mk("HBF31","Languages With Fewer Than 100 Speakers Left","Mapped locations of endangered languages about to vanish","MAP","World","Dot map","International|History|Demographics","UNESCO: Atlas of Languages in Danger (unesco.org); Ethnologue (ethnologue.com)",80,62,70,78,78,78,80,82),
# === War × Geography ===
mk("HBF32","Every Country the US Has Bombed Since 1945","The map is more extensive than most Americans realize","MAP","World","World choropleth","War|Geography|International","Congressional Research Service: Military Operations (crs.gov); Air University: Historical (au.af.mil)",78,65,75,82,78,82,70,78),
mk("HBF33","Landmine Contamination Map of the World","Countries still clearing mines from wars that ended decades ago","MAP","World","World choropleth","War|Geography|International","ICBL: Landmine Monitor (icbl.org); HALO Trust: Where We Work (halotrust.org)",78,62,72,78,78,82,72,85),
mk("HBF34","Nuclear Weapons Tests by Location","Every detonation site on Earth since 1945","MAP","World","Dot map","War|Geography|Science","CTBTO: Nuclear Test Database (ctbto.org); SIPRI: Nuclear Forces (sipri.org)",72,58,75,78,72,85,72,90),
mk("HBF35","Unexploded WWII Bombs Still Being Found in Europe","Annual discoveries mapped by city since 2000","MAP","World","Dot map","War|Geography|History","European EOD Services; BBC/Reuters: UXO Reporting Database",70,60,72,82,68,80,80,65),
]

# --- inject ---
with open(DATA, 'r', encoding='utf-8') as f:
    txt = f.read()
ids = set(re.findall(r'id:"([^"]+)"', txt))
new = [i for i in IDEAS if re.search(r'id:"([^"]+)"', i).group(1) not in ids]
if not new:
    print("All HBF ideas already present"); exit()
tail = "]; // end D"
txt = txt.replace(tail, ",\n".join(new) + ",\n" + tail)
with open(DATA, 'w', encoding='utf-8') as f:
    f.write(txt)
print(f"Injected {len(new)} new ideas (HBF batch)")
