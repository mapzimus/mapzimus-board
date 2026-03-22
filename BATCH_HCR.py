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
mk("HCR01","The Factory Floor Moved: US Manufacturing Employment 1970 vs. Now","County-level manufacturing jobs as percent of total employment, then and now — the deindustrialization map","MAP","US","Bivariate choropleth","manufacturing","BLS: Quarterly Census of Employment and Wages (bls.gov/cew)",82,78,78,75,80,85,72,85),
mk("HCR02","Every Car Plant in America: Who Builds What Where","Map of every auto assembly plant — Big Three, Toyota, Hyundai, Tesla — showing the new geography of American cars","MAP","US","Dot map","manufacturing","Auto Alliance: Manufacturing Map (autosinnovate.org)",68,72,78,72,62,85,68,82),
mk("HCR03","The Reshoring Scoreboard: Manufacturing Jobs Coming Back vs. Still Leaving","Net manufacturing job gains and losses by state since 2020, the reshoring vs. offshoring tug-of-war","MAP","US","State choropleth","manufacturing","Reshoring Initiative: Data Reports (reshorenow.org/data)",72,72,75,78,72,78,75,72),
mk("HCR04","What America Still Makes: Top Manufacturing Products by State","Each states highest-value manufactured product — from aircraft in Washington to chemicals in Texas","MAP","US","State choropleth","manufacturing","Census: Annual Survey of Manufactures (census.gov/programs-surveys/asm)",68,72,80,75,62,82,68,85),
mk("HCR05","The Steel Belt to Rust Belt: Steel Production Tonnage 1950 vs. Today","Steel mill capacity and output by county, showing the collapse of the industrial Midwest","MAP","US","Bivariate choropleth","manufacturing","USGS: Mineral Commodity Summaries Iron and Steel (usgs.gov/centers/national-minerals)",78,72,75,72,78,82,70,78),
mk("HCR06","CHIPS Act Money Map: Where the Semiconductor Investment Is Going","Every CHIPS Act funded facility and expansion, mapped with dollar amounts and projected jobs","MAP","US","Dot map","manufacturing","Commerce: CHIPS for America (commerce.gov/chips)",68,65,78,75,68,82,72,75),
mk("HCR07","The Rural Hospital Death Spiral: Closures Since 2010","Every rural hospital that has closed since 2010, mapped against the nearest remaining facility","MAP","US","Dot map","rural","UNC: Cecil G. Sheps Center Rural Hospital Closures (ruralhealthresearch.org)",88,78,75,72,88,82,70,82),
mk("HCR08","The Dollar General Invasion: Where Dollar Stores Outnumber Grocery Stores","Counties where dollar store locations exceed full-service grocery stores — rural food access crisis","MAP","US","County choropleth","rural","ILSR: Dollar Store Database (ilsr.org/rule/dollar-stores)",80,82,72,82,78,82,78,72),
mk("HCR09","No Bars: Cell Phone Dead Zones Mapped Against Population","Areas with no cellular coverage overlaid with population, showing who is digitally stranded","MAP","US","Bivariate choropleth","rural","FCC: Broadband Deployment Report Coverage Maps (broadbandmap.fcc.gov)",72,75,75,72,70,85,70,78),
mk("HCR10","The Meatpacking Map: Where Americas Meat Is Processed","Every major meatpacking plant mapped with capacity, workforce nationality, and OSHA violation history","MAP","US","Dot map","manufacturing","USDA: Meat Packing Plants Directory (fsis.usda.gov/inspection/establishments)",72,68,72,75,72,82,72,78),
mk("HCR11","Americas Last Textile Mills: Where Clothing Is Still Made in the US","Remaining textile and apparel manufacturing facilities, down 95% from 1990 peak","MAP","US","Dot map","manufacturing","BLS: QCEW Textile Mills Employment (bls.gov/cew)",70,65,72,78,72,78,75,72),
mk("HCR12","The Pharmacy Desert: Rural Counties With Zero Pharmacies","Counties with no pharmacy at all, overlaid with elderly population percentage","MAP","US","County choropleth","rural","RUPRI: Rural Pharmacy Closures (rupri.org)",82,78,72,78,82,82,70,75),
mk("HCR13","Farm Size Bimodal Split: The Disappearing Mid-Size Farm","Distribution of US farms by acreage showing the hollowing out of mid-size operations — tiny hobby farms and mega-operations dominate","CHART","US","Bar chart","rural","USDA: Census of Agriculture Farm Size (nass.usda.gov/AgCensus)",75,72,78,78,75,70,75,85),
mk("HCR14","Where the Factories Went: Top Destinations for Offshored US Manufacturing","Countries that absorbed the most US manufacturing jobs since NAFTA, by sector","MAP","World","World choropleth","manufacturing","BLS: Extended Mass Layoffs (bls.gov/mls)",78,72,75,72,78,78,72,72),
mk("HCR15","The EV Battery Belt: Every Electric Vehicle Battery Plant in America","Map of every EV battery gigafactory built, under construction, or announced — the new industrial geography","MAP","US","Dot map","manufacturing","DOE: Battery Manufacturing Map (energy.gov/eere/vehicles)",68,65,78,78,70,85,72,75),
mk("HCR16","Rural Brain Drain: Net Migration of 18-24 Year Olds Out of Rural Counties","Which rural counties lose the highest percentage of their young adults, and where they go","MAP","US","County choropleth","rural","Census: County-to-County Migration (census.gov/data/tables/2020/demo/geographic-mobility)",78,75,75,72,78,82,70,80),
mk("HCR17","The Broadband Divide Is a Rural Divide: Internet Speeds by County","Median download speeds by county showing the massive urban-rural digital gap","MAP","US","County choropleth","rural","FCC: Fixed Broadband Deployment (broadbandmap.fcc.gov)",72,78,78,68,72,82,65,82),
mk("HCR18","Defense Industrial Base: Where Military Equipment Gets Made","Every major defense contractor facility mapped — Lockheed, Raytheon, Boeing, Northrop — by product type","MAP","US","Dot map","manufacturing","DOD: Defense Industrial Base Reports (acq.osd.mil)",68,58,75,72,68,85,68,72),
mk("HCR19","The Veterinarian Desert: Rural Counties With No Large-Animal Vet","Counties with no veterinarian capable of treating livestock, threatening agricultural operations","MAP","US","County choropleth","rural","AVMA: Veterinarian Workforce Study (avma.org/resources-tools/reports-statistics)",70,65,70,80,70,80,78,68),
mk("HCR20","One-Employer Towns: Communities Where a Single Company Is 40%+ of Jobs","Towns economically dependent on one employer — a coal mine, a prison, a factory, a military base","MAP","US","Dot map","rural","BLS: QCEW Establishment Level Data (bls.gov/cew)",78,75,72,78,80,78,75,68),
mk("HCR21","Americas Paper Trail: Where Paper Is Still Made","Remaining paper and pulp mills in the US, an industry that has shrunk 60% since the internet age","MAP","US","Dot map","manufacturing","AF&PA: Paper Industry Statistics (afandpa.org/statistics-resources)",65,60,72,75,65,80,72,72),
mk("HCR22","The Apprenticeship Gap: Registered Apprenticeships Per Capita by State","States with robust apprenticeship systems vs. those relying entirely on four-year college pipeline","MAP","US","State choropleth","manufacturing","DOL: Registered Apprenticeship Data (apprenticeship.gov/data-and-statistics)",68,72,75,72,68,78,72,78),
mk("HCR23","Ghost Schools: Rural Districts That Have Consolidated Out of Existence","School districts eliminated through consolidation since 2000, mapped against student travel time","MAP","US","Dot map","rural","NCES: School District Boundary Changes (nces.ed.gov)",75,72,70,75,72,80,72,72),
mk("HCR24","The Supply Chain Revealed: Where Everyday Products Get Assembled","Tracing a smartphone, a car, and a Big Mac — mapping every component origin and assembly step","MAP","World","Line map","manufacturing","MIT Observatory of Economic Complexity (oec.world)",68,78,72,78,65,82,78,65),
mk("HCR25","The Craft Brewery Boom vs. Factory Brewery Bust","Map of craft brewery openings vs. macro-brewery closures, showing the decentralization of American beer","MAP","US","Dot map","manufacturing","Brewers Association: Industry Statistics (brewersassociation.org/statistics)",62,72,72,72,58,80,72,78),
mk("HCR26","Where Walmart Is the Biggest Employer: Counties Dominated by Retail","Counties where the largest private employer is Walmart, Amazon, or another retailer — post-manufacturing economy","MAP","US","County choropleth","rural","BLS: QCEW Top Employers (bls.gov/cew)",72,78,75,72,72,82,68,75),
mk("HCR27","Americas Furniture Belt: North Carolina Manufacturing Then and Now","The rise and fall of furniture manufacturing in the Piedmont region, mapped by plant closures and imports","MAP","US","Dot map","manufacturing","BIFMA: Furniture Industry Statistics (bifma.org)",70,65,72,72,72,78,70,68),
mk("HCR28","The Right-to-Work Map Meets the Union Map: How Labor Law Shapes Manufacturing","Right-to-work states vs. union density, overlaid with new factory investment locations","MAP","US","Bivariate choropleth","manufacturing","BLS: Union Membership by State (bls.gov/news.release/union2.nr0.htm)",72,68,78,72,72,82,72,80),
mk("HCR29","The Childcare Desert and the Labor Force Gap: Where Moms Cant Work Because Theres No Daycare","Counties with fewer than 1 childcare slot per 3 children, overlaid with female labor force participation","XREF","US","Bivariate choropleth","rural","Center for American Progress: Childcare Deserts (childcaredeserts.org)",85,82,72,78,82,82,72,75),
mk("HCR30","EMS Response Times: Rural Areas Where an Ambulance Takes 30+ Minutes","Average EMS response times by county, showing where distance kills","MAP","US","County choropleth","rural","NHTSA: EMS Response Time Data (ems.gov)",85,78,78,72,85,82,68,72),
mk("HCR31","The Chicken Processing Map: Americas Poultry Belt","Every major poultry processing plant in the Southeast and mid-Atlantic, with labor and inspection data","MAP","US","Dot map","manufacturing","USDA: FSIS Poultry Establishments (fsis.usda.gov)",68,65,72,72,65,82,68,78),
mk("HCR32","Where Cell Towers End and Satellite Begins: The Connectivity Frontier","Map of the boundary where cellular coverage gives way to satellite-only communication in rural America","MAP","US","Special map","rural","FCC: Coverage Area Maps (broadbandmap.fcc.gov)",65,68,72,75,62,85,72,72),
mk("HCR33","Americas Export Economy: What Each State Ships Abroad","Top export product by state by dollar value — planes from Washington, soybeans from Illinois, cars from Michigan","MAP","US","State choropleth","manufacturing","Census: State Exports by NAICS (census.gov/foreign-trade/statistics/state)",65,68,80,72,60,82,65,88),
mk("HCR34","The Rail Revival: New Rail Freight Investment vs. Abandoned Lines","Active vs. abandoned rail lines mapped, showing which routes are being rebuilt for modern logistics","MAP","US","Line map","rural","STB: Surface Transportation Board Rail Maps (stb.gov/stb/rail-maps)",65,60,72,72,62,85,72,72),
mk("HCR35","Post Office Closures: The Shrinking Federal Footprint in Rural America","Post offices closed since 2000 mapped against population, showing federal retreat from rural communities","MAP","US","Dot map","rural","USPS: Facility Closure Data (about.usps.com/what/strategic-plans)",75,72,72,75,72,82,70,75),
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
print(f"Injected {len(new)} new ideas (HCR batch)")
