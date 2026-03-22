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
mk("HDD01","Every Object Humans Have Launched Into Space: The Orbital Census","Complete catalog of active satellites, defunct hardware, rocket bodies, and debris by orbit altitude and country of origin","MAP","World","Special map","space","ESA: Space Debris Office (esa.int/space_safety/space_debris)",62,55,75,78,62,88,72,82),
mk("HDD02","The Space Budget: What Each Country Spends on Space Per Capita","National space agency budgets per capita, showing who invests most per person in space exploration","MAP","World","World choropleth","space","Space Foundation: Space Report (spacefoundation.org/space-report)",65,58,80,72,62,80,68,82),
mk("HDD03","Where Rockets Launch From: Every Active Spaceport on Earth","Map of every operational launch site worldwide, with annual launch count and orbital capability","MAP","World","Dot map","space","FAA: Licensed Spaceports (faa.gov/space/spaceports)",60,55,78,72,58,88,68,82),
mk("HDD04","The Starlink Constellation: How Many Satellites Elon Musk Has in Orbit","Growth of SpaceX Starlink satellite constellation over time — from 0 to 6,000+ in five years","CHART","World","Line chart","space","Jonathan McDowell: Starlink Statistics (planet4589.org/space/stats/star/starstats.html)",62,62,78,72,60,78,68,85),
mk("HDD05","Light Pollution Is Erasing the Stars: Where You Can and Cant See the Milky Way","Light pollution map of the US showing where the night sky is still dark enough to see the Milky Way","MAP","US","Special map","space","Dark Sky Association: Light Pollution Map (darksky.org/light-pollution/dark-sky-places)",68,72,72,72,65,90,72,78),
mk("HDD06","NASAs Budget as a Fraction of Federal Spending: The Incredible Shrinking Space Program","NASA budget as percentage of federal spending, 1958-2025 — peaked at 4.4% during Apollo, now under 0.5%","CHART","US","Area chart","space","NASA: Budget Documents (nasa.gov/news/budget)",68,65,80,78,68,70,70,88),
mk("HDD07","Asteroid Near-Miss Catalog: Every Close Approach to Earth in the Last Decade","Every asteroid that passed within the Moons orbit in the last 10 years, sized by diameter and colored by discovery lead time","MAP","World","Special map","space","NASA: CNEOS Close Approach Data (cneos.jpl.nasa.gov/ca)",72,62,72,82,78,85,72,82),
mk("HDD08","Where on Earth Has Been Hit by Meteorites: The Impact Map","Every verified meteorite impact location on Earth with size, date, and type classification","MAP","World","Dot map","space","Meteoritical Society: Meteorite Bulletin Database (lpi.usra.edu/meteor)",62,55,72,78,62,85,72,82),
mk("HDD09","The Moon Race 2.0: Every Planned Lunar Mission by Country Through 2030","All planned lunar missions by space agency and private company through 2030, showing the new space race","CHART","World","Line chart","space","Planetary Society: Lunar Mission Timeline (planetary.org/space-missions/every-moon-mission)",65,55,75,78,68,78,72,72),
mk("HDD10","Scientific Papers Published Per Capita: The Research Productivity Map","Peer-reviewed scientific publications per million people by country, showing where knowledge is generated","MAP","World","World choropleth","science","SCImago Journal Rankings: Country Rankings (scimagojr.com/countryrank.php)",62,55,78,72,58,80,68,88),
mk("HDD11","The Periodic Table of Scarcity: Which Elements Are Running Out","Elements at risk of depletion within 100 years based on current extraction rates and known reserves","CHART","World","Special map","science","European Chemical Society: Endangered Elements (euchems.eu/euchems-periodic-table)",68,58,72,82,72,82,78,72),
mk("HDD12","Americas National Lab Network: Where Government Science Happens","Every DOE national laboratory and federal research facility mapped with budget and specialty area","MAP","US","Dot map","science","DOE: National Laboratories (energy.gov/national-laboratories)",60,55,78,68,55,85,65,82),
mk("HDD13","The Antibiotic Resistance Clock: How Fast Superbugs Are Outpacing Drug Development","Timeline of antibiotic introduction vs. first detected resistance, showing the narrowing window of effectiveness","CHART","World","Line chart","science","CDC: Antibiotic Resistance Threats (cdc.gov/drugresistance/biggest-threats.html)",78,68,72,82,82,70,78,78),
mk("HDD14","Where CRISPR Is Legal: Gene Editing Regulation by Country","Countries that allow human germline editing, somatic editing only, or ban gene editing entirely","MAP","World","World choropleth","science","Nature: CRISPR Regulation Tracker (nature.com/articles/d41586-019-00673-1)",68,55,72,82,72,80,78,72),
mk("HDD15","The Telescope Network: Every Major Observatory on Earth","Map of every major astronomical observatory worldwide, colored by wavelength capability — optical, radio, infrared","MAP","World","Dot map","space","IAU: Observatory List (iau.org/public/themes/observatories)",58,52,75,68,55,88,68,82),
mk("HDD16","Earthquake Prediction Accuracy Over Decades: How Much Better Have We Gotten","Accuracy of earthquake predictions over time — spoiler: not much — showing the limits of seismology","CHART","World","Line chart","science","USGS: Earthquake Prediction Research (earthquake.usgs.gov/learn/topics/prediction.php)",65,62,72,82,68,68,78,72),
mk("HDD17","Americas Superfund Legacy: Every Toxic Waste Site on the National Priorities List","Every EPA Superfund site mapped with contamination type, cleanup status, and proximity to population","MAP","US","Dot map","science","EPA: Superfund National Priorities List (epa.gov/superfund/superfund-national-priorities-list-npl)",78,72,72,72,78,82,65,85),
mk("HDD18","The Speed of Science: Time from Discovery to Vaccine by Disease","How long it took to develop vaccines for each major disease — from 100+ years for typhoid to under 1 year for COVID","CHART","World","Bar chart","science","Our World in Data: Vaccine Development Timelines (ourworldindata.org/vaccination)",65,68,80,78,65,70,72,82),
mk("HDD19","Nuclear Test Sites of the World: Every Detonation on the Map","Every nuclear weapons test detonation location worldwide 1945-present, colored by country and yield","MAP","World","Dot map","science","CTBTO: Nuclear Tests Database (ctbto.org/nuclear-testing)",72,55,78,72,78,85,68,85),
mk("HDD20","The Nobel Prize Map: Laureates Per Capita by Country","Nobel Prize winners per million people by country, revealing the geography of elite scientific achievement","MAP","World","World choropleth","science","Nobel Foundation: Laureate Database (nobelprize.org/prizes/lists/all-nobel-prizes)",62,55,78,78,58,80,72,88),
mk("HDD21","Space Junk Collision Risk: The Kessler Syndrome Probability Over Time","Probability of cascading satellite collisions in low Earth orbit over the next 50 years, by altitude band","CHART","World","Line chart","space","NASA: Orbital Debris Quarterly News (orbitaldebris.jsc.nasa.gov)",68,55,68,82,78,75,78,68),
mk("HDD22","Deep-Sea Discovery Timeline: New Species Found Per Decade Since 1960","Number of new deep-sea species formally described per decade, colored by phylum and depth zone","CHART","World","Area chart","science","OBIS: Ocean Biodiversity Information System (obis.org)",62,52,65,78,58,72,74,72),
mk("HDD23","Solar Storm Damage: Estimated Cost of Geomagnetic Events by Decade","Economic damage from solar storms hitting Earth infrastructure, from Carrington Event projections to modern grid vulnerabilities","CHART","World","Bar chart","space","NOAA: Space Weather Prediction Center (swpc.noaa.gov)",58,48,62,75,72,68,70,60),
mk("HDD24","The Periodic Table of Scarcity: Elements Running Out Within 100 Years","Which chemical elements face supply exhaustion, mapped by remaining years of known reserves and primary mining country","MAP","World","Graduated symbol map","science","USGS: Mineral Commodity Summaries (usgs.gov/centers/national-minerals-information-center)",70,62,72,80,75,82,76,78),
mk("HDD25","Mars Mission Windows: Every Launch Opportunity and Who Took It","Timeline of Mars transfer windows since 1960 showing which countries launched missions, succeeded, or failed at each opportunity","CHART","World","Timeline chart","space","NASA: Mars Exploration Program (mars.nasa.gov)",65,58,70,72,60,78,72,80),
mk("HDD26","Citizen Science Surge: Observations Submitted to iNaturalist by Country","Total biodiversity observations uploaded to iNaturalist per capita, revealing which nations have the most engaged amateur scientists","MAP","World","Choropleth","science","iNaturalist: Global Observation Data (inaturalist.org)",58,65,68,62,48,70,64,82),
mk("HDD27","Rocket Launch Cadence: Orbital Launches Per Month Since 2000","Monthly orbital launch attempts worldwide showing the SpaceX-driven acceleration and new entrants like Rocket Lab","CHART","World","Line chart","space","Jonathan McDowell: Launch Log (planet4589.org/space/log)",55,50,72,65,55,70,62,88),
mk("HDD28","The Exoplanet Catalog: Confirmed Planets by Detection Method and Star Type","Breakdown of 5,000+ confirmed exoplanets by how they were discovered — transit, radial velocity, direct imaging — and host star classification","CHART","World","Stacked bar chart","space","NASA: Exoplanet Archive (exoplanetarchive.ipac.caltech.edu)",62,48,68,72,52,75,70,90),
mk("HDD29","Lab Leak vs Natural Origin: Biosafety Level 4 Labs Worldwide","Location and capacity of every BSL-4 laboratory on Earth, mapped against emerging infectious disease hotspots","MAP","World","Dot density map","science","Global Health Security Index: GHS Tracking (ghsindex.org)",72,68,65,82,85,78,80,70),
mk("HDD30","Satellite Mega-Constellations: Who Owns Low Earth Orbit","Share of active satellites in LEO by operator — Starlink dominance vs OneWeb, Amazon Kuiper, and national programs","CHART","World","Treemap","space","UCS: Satellite Database (ucsusa.org/resources/satellite-database)",60,55,70,72,65,74,68,85),
mk("HDD31","Science Funding as GDP Share: Who Invests Most in R&D","National R&D expenditure as percentage of GDP, tracked over 30 years — Israel and South Korea lead, most nations stagnate","RANK","World","Bump chart","science","World Bank: Research and Development Expenditure (data.worldbank.org)",62,60,75,65,62,68,58,88),
mk("HDD32","Volcanic Eruption Forecast: The 10 Most Dangerous Volcanoes Still Unmonitored","High-threat volcanoes with large nearby populations that lack basic seismic monitoring equipment","MAP","World","Proportional symbol map","science","Global Volcanism Program: Smithsonian (volcano.si.edu)",72,68,65,82,80,80,74,75),
mk("HDD33","Space Tourism Price Curve: Cost Per Seat From Shuttle Era to 2026","How the price of reaching space has dropped from $58M per shuttle seat to sub-$500K projections, by vehicle","CHART","World","Line chart","space","FAA: Commercial Space Transportation (faa.gov/space)",65,70,72,68,55,65,62,72),
mk("HDD34","Replication Crisis Map: Which Scientific Fields Have the Worst Reproducibility","Percentage of landmark studies that failed replication attempts, by discipline — psychology, oncology, economics compared","RANK","World","Horizontal bar chart","science","Open Science Framework: Reproducibility Projects (osf.io)",68,65,72,78,72,62,76,70),
mk("HDD35","The Final Frontier Budget: NASA Spending Per American vs Military Spending Per American","Per-capita comparison of NASA budget to defense budget over 60 years — peak Apollo spending still dwarfed by military","XREF","US","Dual-axis line chart","space","OMB: Historical Budget Tables (whitehouse.gov/omb/budget/historical-tables)",72,75,78,70,68,65,72,85),
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
print(f"Injected {len(new)} new ideas (HDD batch)")
