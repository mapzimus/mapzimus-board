"""BATCH HEU — 35 ideas targeting: science, humor, guns, space, history, media, religion, gender"""
import re

def mk(id,title,sub,typ,geo,fmt,sect,tbl,e,r,c,s,t,v,o,dr):
    raw=v*3.0+e*2.5+s*2.0+o*1.75+t*1.75+r*2.0+c*1.5
    base=raw/14.5
    fl=0.85 if min(e,r,c,s,t,v,o)<35 else 1.0
    pen=1.0-0.35*(1.0-dr/100.0)
    vs=int(base*fl*pen)
    return ('{id:"'+id+'",title:"'+title+'",sub:"'+sub+'",type:"'+typ+'",'
            'geo:"'+geo+'",fmt:"'+fmt+'",section:"'+sect+'",tbl:"'+tbl+'",'
            'sc:{emotional:'+str(e)+',relatability:'+str(r)+',clarity:'+str(c)
            +',surprise:'+str(s)+',tension:'+str(t)+',visual:'+str(v)
            +',originality:'+str(o)+',data_ready:'+str(dr)+'}'
            ',vs:'+str(vs)+',topics:[],ext:[],status:"idea",notes:""}')

IDEAS = [
# ── science (5) ──
mk("heu01","Nobel Prize Deserts: Countries That Have Never Won a Nobel","190+ nations exist but Nobels cluster in 20 countries — map every laureate origin vs. global population share","country","world","World choropleth","Science & Technology","Nobel Foundation: All Laureates (nobelprize.org/prizes/lists/all-nobel-prizes)",55,50,75,70,45,80,72,90),
mk("heu02","Retracted Science: The Most-Cited Papers Later Pulled From Journals","Some retracted papers get cited hundreds of times after retraction — timeline of the biggest retractions and their citation afterlife","topic","world","Scatter plot","Science & Technology","Retraction Watch: Retraction Database (retractionwatch.com)",50,40,70,82,55,65,80,88),
mk("heu03","The Half-Life of Scientific Knowledge: How Fast Fields Become Obsolete","Computer science textbooks become outdated in 5 years, physics in 15, math lasts centuries — plot knowledge decay curves by field","topic","world","Line chart","Science & Technology","Semantic Scholar: Citation Decay Data (semanticscholar.org)",45,55,72,78,40,60,85,80),
mk("heu04","Lab Animals Per Paper: Which Scientific Fields Use the Most Mice","Biomedical research uses ~100M lab mice per year globally — treemap of animal use by research field and country","topic","world","Treemap","Science & Technology","Speaking of Research: Animal Use Statistics (speakingofresearch.com)",60,45,68,72,55,70,75,82),
mk("heu05","Women in STEM PhDs: Fields Where the Gender Gap Reversed","Women now earn majority of PhDs in biology and psychology but <20% in physics and CS — slope chart showing 50-year trend","compare","usa","Line chart","Science & Technology","NSF: Survey of Earned Doctorates (ncses.nsf.gov/surveys/earned-doctorates)",55,65,75,68,50,60,65,92),
# ── humor (5) ──
mk("heu06","Americas Most Complained-About Sounds: 311 Noise Complaints Mapped","Dogs barking vs. construction vs. ice cream trucks — what your city hates hearing most by neighborhood","city","usa","Dot map","Humor & Weird Data","NYC Open Data: 311 Noise Complaints (data.cityofnewyork.us)",70,80,75,65,40,78,70,92),
mk("heu07","Bigfoot Sighting Density vs. Bar Density by County","Counties with the most Bigfoot sightings also tend to have the most bars per capita — scatter plot with county dots","compare","usa","Scatter plot","Humor & Weird Data","BFRO: Bigfoot Sighting Database (bfro.net/gdb)",65,72,70,82,30,75,88,85),
mk("heu08","The Wikipedia Edit Wars: Most Contested Articles by Edit Count","Some Wikipedia pages have 50,000+ edits — from Jesus to Israel to GamerGate — bar chart of the most fought-over pages","ranking","world","Bar chart","Humor & Weird Data","Wikipedia: List of Most-Edited Pages (en.wikipedia.org/wiki/Wikipedia:Most-edited)",55,68,72,75,50,55,78,95),
mk("heu09","Pumpkin Spice Season Creep: When PSL Launches by Year Since 2003","Starbucks has pushed Pumpkin Spice Latte launch date earlier every year — from October to August — timeline chart","change","usa","Line chart","Humor & Weird Data","Starbucks: Press Releases (stories.starbucks.com)",60,82,80,62,30,55,72,88),
mk("heu10","Americas Least-Visited National Parks vs. Most Instagrammed","The most Instagrammed parks get 10M+ visitors while some parks get under 15,000 — scatter plot comparing social media fame vs. actual visits","compare","usa","Scatter plot","Humor & Weird Data","NPS: Visitor Use Statistics (irma.nps.gov/stats)",62,75,78,70,35,72,74,90),
# ── guns (4) ──
mk("heu11","Ghost Guns Seized by Police: The Rise of Untraceable Firearms by City","Unserialized ghost guns seized by law enforcement grew 1,000% in 5 years — bar chart by metro area","change","usa","Bar chart","Guns & Weapons","ATF: Ghost Gun Seizure Reports (atf.gov)",65,60,72,78,75,62,72,85),
mk("heu12","Stand Your Ground vs. Duty to Retreat: Homicide Rates by State Law Type","States with Stand Your Ground laws vs. Duty to Retreat — do self-defense laws correlate with homicide rates?","compare","usa","Bivariate choropleth","Guns & Weapons","RAND: Stand Your Ground Policy Effects (rand.org/gun-policy)",60,65,75,72,78,80,70,88),
mk("heu13","School Shooting Drills: How Often K-12 Students Practice Active Shooter Scenarios","95% of US schools now run lockdown drills — map showing drill frequency and whether schools use simulated gunfire","topic","usa","State choropleth","Guns & Weapons","Everytown: School Shooting Prevention (everytownresearch.org)",72,78,70,65,80,65,62,85),
mk("heu14","Guns Per Capita vs. Gun Deaths: Every Country Plotted","The US is a massive outlier with 120 guns per 100 people — where every nation falls on ownership vs. mortality","compare","world","Scatter plot","Guns & Weapons","Small Arms Survey: Global Firearms Holdings (smallarmssurvey.org)",58,65,80,60,72,70,55,92),
# ── space (4) ──
mk("heu15","Satellite Graveyard: Every Decommissioned Satellite Still in Orbit","Thousands of dead satellites circle Earth alongside active ones — dot map of orbital debris by altitude and origin country","topic","world","Dot map","Space & Exploration","ESA: Space Debris Statistics (esa.int/Space_Safety/Space_Debris)",50,42,68,75,55,85,78,88),
mk("heu16","Light Pollution Atlas: Where You Can Still See the Milky Way","80% of Americans cant see the Milky Way from home — map the Bortle scale darkness rating for every county","topic","usa","County choropleth","Space & Exploration","Globe at Night: Light Pollution Data (globeatnight.org)",65,72,75,68,40,90,70,90),
mk("heu17","Every Mars Mission: Success Rate by Country and Decade","Mars missions have a 50% failure rate overall but recent missions do much better — timeline of every attempt color-coded by outcome","topic","world","Line chart","Space & Exploration","NASA: Mars Exploration Program (mars.nasa.gov)",48,45,72,65,50,70,68,95),
mk("heu18","Space Junk Near-Misses: Close Calls in Low Earth Orbit Per Year","ISS has to dodge debris multiple times per year and near-misses between satellites are accelerating — line chart of conjunction events","change","world","Line chart","Space & Exploration","NASA: Conjunction Reports (celestrak.com)",55,45,70,72,68,65,75,85),
# ── history (5) ──
mk("heu19","Redlined Then and Now: 1930s HOLC Maps vs. Modern Income by Neighborhood","The red lines banks drew 90 years ago still predict neighborhood wealth today — bivariate choropleth layering HOLC grades over current median income","change","usa","Bivariate choropleth","History","Mapping Inequality: HOLC Maps (dsl.richmond.edu/panorama/redlining)",78,72,75,68,70,88,72,92),
mk("heu20","Empires by Area Over Time: Animated Rise and Fall of Territorial Control","From Rome to the British Empire — animated map showing which empires controlled the most land at each century","change","world","Animated choropleth","History","Turchin: Seshat Global History Databank (seshatdatabank.info)",55,52,65,70,45,90,72,82),
mk("heu21","Pandemics by Death Toll: Every Major Outbreak in Human History Compared","The Black Death killed 50M, 1918 flu killed 50M, COVID killed 7M — area chart stacking all major pandemics on a timeline","ranking","world","Area chart","History","Our World in Data: Pandemics (ourworldindata.org/pandemics)",65,60,72,68,58,75,60,90),
mk("heu22","The Great Migration Mapped: Black Population Shift From South 1910-1970","6 million Black Americans left the South in two waves — animated flow map showing origin and destination cities","change","usa","Line map","History","Schomburg Center: In Motion (inmotionaame.org)",72,68,70,65,62,85,70,88),
mk("heu23","US Territorial Expansion: Every Land Acquisition and Its Cost Per Acre","Louisiana Purchase cost 3 cents per acre, Alaska 2 cents — map each acquisition with inflation-adjusted price","topic","usa","Special map","History","National Archives: Territorial Acquisitions (archives.gov)",55,60,78,72,45,82,68,92),
# ── media (4) ──
mk("heu24","Local News Deserts: Counties With Zero Newspaper Coverage","Over 200 US counties have no local newspaper at all — choropleth of news deserts vs. civic engagement metrics","topic","usa","County choropleth","Entertainment & Media","UNC: News Deserts Project (usnewsdeserts.com)",68,72,78,70,65,80,68,90),
mk("heu25","Misinformation Superspreaders: The 12 Accounts Behind 65% of Anti-Vax Content","A tiny number of accounts generate the majority of health misinformation — network graph of share chains","topic","world","Special map","Entertainment & Media","CCDH: Disinformation Dozen (counterhate.com)",62,58,70,78,72,65,75,82),
mk("heu26","Podcast Market Share: Who Owns the Audio Landscape","Spotify, Apple, iHeart, and Amazon control most podcast distribution — treemap of shows and listeners by platform","ranking","usa","Treemap","Entertainment & Media","Edison Research: Podcast Consumer Tracker (edisonresearch.com)",48,62,75,60,42,60,58,88),
mk("heu27","Cable News Viewership Age: Median Viewer Age by Network Over Time","The median Fox News viewer is 68, CNN is 64, MSNBC is 65 — line chart showing all three aging together since 2000","change","usa","Line chart","Entertainment & Media","Nielsen: TV Ratings Data (nielsen.com)",55,70,78,72,48,55,65,85),
# ── religion (4) ──
mk("heu28","The Nones Map: Where Americans Report No Religious Affiliation","The religiously unaffiliated grew from 5% to 30% in 30 years — county choropleth of the none zone","change","usa","County choropleth","Culture & Religion","PRRI: American Values Atlas (atavisual.prri.org)",58,68,75,70,55,78,65,90),
mk("heu29","Megachurch Geography: Every Church Over 2,000 Weekly Attendance","The US has 1,750+ megachurches concentrated in the Sunbelt — dot map sized by weekly attendance","topic","usa","Dot map","Culture & Religion","Hartford Institute: Megachurch Database (hirr.hartsem.edu/megachurch)",52,60,72,68,42,80,70,88),
mk("heu30","Ramadan by Latitude: How Fasting Hours Vary From Iceland to Indonesia","Muslims in Reykjavik fast 21+ hours in summer while those in Jakarta fast 13 — world map of fasting duration by location","topic","world","World choropleth","Culture & Religion","IslamicFinder: Prayer Times (islamicfinder.org)",50,55,78,75,38,82,80,85),
mk("heu31","Religious Switching: Which Faiths Americans Leave and Where They Go","25% of Americans have switched religions — Sankey diagram showing flows between denominations and to/from none","change","usa","Special map","Culture & Religion","Pew: Religious Landscape Study (pewresearch.org/religion)",58,65,70,72,50,68,72,90),
# ── gender (4) ──
mk("heu32","The Motherhood Penalty: Earnings Trajectory After First Child by Gender","Mens earnings are unaffected by having children while womens drop 30% and never fully recover — line chart of parallel trajectories","compare","usa","Line chart","Gender","Census Bureau: SIPP Earnings Data (census.gov/sipp)",75,78,80,68,65,60,62,88),
mk("heu33","Unpaid Care Work: Hours Per Day by Gender and Country","Women globally do 3x more unpaid domestic work than men — bar chart of the care gap across 50+ countries","compare","world","Bar chart","Gender","OECD: Time Use Survey (oecd.org/gender/data)",70,75,78,65,60,58,55,90),
mk("heu34","Women in National Legislatures: Every Country Ranked","Rwanda leads at 61% women in parliament while 20+ countries are under 10% — world choropleth with trendline","ranking","world","World choropleth","Gender","IPU: Women in Parliament (ipu.org/women-in-parliament)",55,58,78,62,50,80,52,95),
mk("heu35","Femicide Rates: Countries Where Women Are Most Likely to Be Killed by Partners","Intimate partner violence kills 47,000 women per year globally — choropleth of femicide rates per 100k women","topic","world","World choropleth","Gender","UNODC: Gender-Related Killings (dataunodc.un.org)",78,55,72,68,82,75,60,82),
]

# ── Inject into data.js ──

f = open('data.js', 'r', encoding='utf-8')
text = f.read()
f.close()

tail = ']; // end D'
if tail not in text:
    print("ERROR: tail marker not found"); exit(1)

text = text.replace(tail, '')
for idea in IDEAS:
    text += ',\n' + idea
text += '\n' + tail

f = open('data.js', 'w', encoding='utf-8')
f.write(text)
f.close()
print(f"Injected {len(IDEAS)} ideas into data.js")
