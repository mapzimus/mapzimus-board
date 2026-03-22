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
mk("HCY01","The Pumpkin Spice Index: How September Coffee Orders Predict Fall Consumer Spending","Pumpkin spice latte sales as a leading indicator of fall retail spending — surprisingly correlated","XREF","US","Scatter plot","humor","NCA: National Coffee Data Trends (ncausa.org)",55,85,68,82,48,68,85,55),
mk("HCY02","Americas Most Misspelled Words by State: The Typo Map","Most commonly misspelled Google search terms by state — people in every state struggle with different words","MAP","US","State choropleth","humor","Google Trends: Spelling Data (trends.google.com)",50,85,72,78,42,80,78,72),
mk("HCY03","The Florida Man Index: Bizarre Crime Reports Per Capita by State","Rate of news stories categorized as bizarre or unusual crimes per capita — Florida leads but not by as much as you think","RANK","US","Bar chart","humor","Google News: Bizarre Crime Reports Analysis (news.google.com)",52,82,65,85,45,70,82,58),
mk("HCY04","How Long Americans Wait in Line Per Year: The Queue Economy","Total hours per year the average American spends waiting in lines — DMV, grocery, traffic, phone holds — by activity","CHART","US","Bar chart","humor","IATA/ARC: Wait Time Studies (various)",62,88,72,78,55,68,75,62),
mk("HCY05","The Pothole Index: Road Quality vs. Tax Revenue by State","States with the worst road conditions plotted against their gasoline tax rates and road spending — who pays more and gets less","XREF","US","Scatter plot","humor","TRIP: Road Condition Reports (tripnet.org)",68,85,72,78,62,72,72,78),
mk("HCY06","Americas Weirdest Town Names: A Geography of Accidental Comedy","Map of Americas most absurdly named places — Boring OR, Intercourse PA, Nothing AZ, Accident MD, Why AZ","MAP","US","Dot map","humor","USGS: Geographic Names Information System (gnis.usgs.gov)",48,78,68,82,40,85,82,82),
mk("HCY07","How Many Hot Dogs Is Too Many: The Nathan Hot Dog Contest Over Time","Nathans hot dog eating contest winning totals over time — from 25 in the 1970s to 76 in 2021","CHART","US","Line chart","humor","Major League Eating: Contest Records (majorleagueeating.com)",48,72,78,72,42,68,72,82),
mk("HCY08","The Sock Mystery: Where Single Socks Go — A Statistical Investigation","Estimated number of socks lost per household per year by country, laundry frequency, and dryer ownership","CHART","World","Bar chart","humor","Samsung: Lost Socks Index (samsung.com/uk/lostocksindex)",45,82,62,85,38,68,88,52),
mk("HCY09","Americas Most Complained-About Airline by Route: The Misery Map","Which airline generates the most DOT complaints on each route — a frequent flyer survival guide","MAP","US","Line map","humor","DOT: Air Travel Consumer Reports (transportation.gov/airconsumer)",62,82,72,72,58,78,72,82),
mk("HCY10","The Pizza Ratio: Pizza Restaurants Per Capita vs. Heart Disease by State","Number of pizza places per capita plotted against cardiovascular disease rates by state","XREF","US","Scatter plot","humor","Census: County Business Patterns (census.gov/programs-surveys/cbp.html)",55,78,68,78,52,68,78,72),
mk("HCY11","Every States Official State Fossil: The Paleontology of Bureaucracy","Map of official state fossils — yes most states have one — revealing geological identity and legislative priorities","MAP","US","State choropleth","humor","State Symbols USA: State Fossils (statesymbolsusa.org)",45,62,72,82,38,82,82,82),
mk("HCY12","The Monday Effect: How Much Less Productive America Is on Mondays","Measurable productivity drop on Mondays across industries — email response time, code commits, sales calls","CHART","US","Bar chart","humor","RescueTime: Workplace Productivity Data (rescuetime.com)",58,88,72,72,52,68,72,68),
mk("HCY13","Americas Most Stolen Items from Hotels: The Towel Index","Most commonly pilfered hotel items by category and estimated annual replacement cost for the industry","RANK","US","Bar chart","humor","AHLA: Hotel Theft Survey (ahla.com/research)",48,82,68,78,42,68,78,55),
mk("HCY14","The Lefty Map: Percentage of Left-Handed People by Country","Left-handedness rates by country — influenced by cultural pressure, with some nations as low as 2%","MAP","World","World choropleth","humor","Papadatou-Pastou: Handedness Meta-Analysis (pubmed.ncbi.nlm.nih.gov)",55,72,72,82,48,80,78,72),
mk("HCY15","How Far Americans Drive to Get a Burrito: The Taco Bell Access Map","Average drive time to nearest burrito option by county — revealing the Mexican food desert","MAP","US","County choropleth","humor","Yelp: Restaurant Category Data (yelp.com/developers)",52,82,68,78,45,82,78,62),
mk("HCY16","The Cat vs. Dog Map: Pet Preference by State Based on Ownership Data","States where cat ownership exceeds dog ownership and vice versa — the eternal debate settled by data","MAP","US","State choropleth","humor","AVMA: Pet Ownership and Demographics (avma.org/resources-tools/reports-statistics)",48,85,72,68,42,82,65,78),
mk("HCY17","Toilet Paper Over or Under: The Regional Preference Map","Survey results on toilet paper orientation preference by region — the most divisive chart in America","MAP","US","State choropleth","humor","Barry Sinrod: Toilet Paper Survey (various news sources)",42,82,65,72,38,78,78,55),
mk("HCY18","Americas Jaywalking Capital: Pedestrian Citation Rates by City","Jaywalking ticket rates per capita by major city — some cities ticket thousands while others gave up entirely","RANK","US","Bar chart","humor","Various: Municipal Court Records (via FOI requests)",55,78,68,78,52,68,78,58),
mk("HCY19","The Meeting That Could Have Been an Email: Estimated Wasted Meeting Hours by Industry","Hours per week spent in meetings rated unnecessary by attendees, by industry and company size","CHART","US","Bar chart","humor","Atlassian: Meeting Productivity Survey (atlassian.com/time-wasting-at-work-infographic)",65,88,72,72,58,68,72,68),
mk("HCY20","Americas Roundabout Revolution: Traffic Circles Built Per Year","Number of roundabouts constructed per year in the US — from near zero in 1990 to 8,000+ today, mapped","MAP","US","Dot map","humor","IIHS: Roundabout Statistics (iihs.org/topics/roundabouts)",52,68,72,72,45,80,72,72),
mk("HCY21","How Far Your Dollar Goes at a Vending Machine: Snack Prices by Airport","Average vending machine and airport food prices by airport — the most expensive snack in America","RANK","US","Bar chart","humor","Wanderu: Airport Food Price Index (wanderu.com)",55,82,72,72,48,68,72,62),
mk("HCY22","The Superstition Map: Which Countries Skip the 13th Floor","Buildings that skip floor 13, room 13, or have other numerical superstitions — 4 in East Asia, 13 in the West","MAP","World","World choropleth","humor","Otis Elevator: Building Numbering Practices (various)",48,68,68,82,42,78,82,58),
mk("HCY23","Americas Garage Sale Economy: Estimated Revenue from Yard Sales by State","Total estimated annual garage sale revenue by state — billions of dollars in informal commerce","MAP","US","State choropleth","humor","Statistic Brain: Garage Sale Statistics (statisticbrain.com)",52,78,68,72,45,78,72,55),
mk("HCY24","The Autocorrect Hall of Shame: Most Common Autocorrect Fails by Phone OS","Most frequent embarrassing autocorrect substitutions by operating system and language","RANK","World","Bar chart","humor","Grammarly: Common Autocorrect Errors (grammarly.com/blog)",48,85,68,78,42,68,78,58),
mk("HCY25","Americas Speed Trap Map: Revenue Per Traffic Stop by Town","Small towns where traffic citation revenue per capita is highest — the speed trap economy","MAP","US","Dot map","humor","AAA: Speed Trap Database (autoclubmo.aaa.com/automotive/speedtrap)",62,78,72,78,58,80,72,65),
mk("HCY26","The Return of the Mullet: Hairstyle Popularity Over Time by Region","Google search trends for mullet hairstyle by state over time — the ironic-to-unironic pipeline","MAP","US","State choropleth","humor","Google Trends: Hairstyle Searches (trends.google.com/trends)",45,72,65,78,40,78,82,68),
mk("HCY27","How Many Licks Does It Take: The Actual Scientific Answer","Peer-reviewed studies attempting to answer the Tootsie Pop question — results range from 100 to 411","CHART","World","Bar chart","humor","NYU: Mathematical Modeling of Lollipop Dissolution (journals.aps.org)",42,72,68,82,38,68,85,68),
mk("HCY28","The Urinal Protocol: Mathematically Optimal Bathroom Behavior","Game theory analysis of urinal selection — the Nash equilibrium of the mens room","CHART","World","Special map","humor","XKCD: Urinal Protocol (blog.xkcd.com/2009/09/02/urinal-protocol-vulnerability)",45,72,62,88,38,72,88,58),
mk("HCY29","The IKEA Effect: Countries With IKEA Stores Per Capita vs. Average Apartment Size","IKEA store density plotted against average living space per person — small apartments need more clever storage","XREF","World","Scatter plot","humor","IKEA: Store Locations (ikea.com/ext/local-store-finder)",52,72,68,82,45,68,82,72),
mk("HCY30","Americas Bigfoot Sighting Map: Sasquatch Reports Per Square Mile","BFRO Bigfoot sighting density map — surprisingly concentrated in the Pacific Northwest and Appalachia","MAP","US","County choropleth","humor","BFRO: Geographic Database (bfro.net/GDB)",45,68,62,82,42,82,82,78),
mk("HCY31","The Snooze Button Economy: How Many Times Americans Hit Snooze by State","Average number of alarm snooze presses by state, correlated with commute time and sunrise time","MAP","US","State choropleth","humor","Sleep Number: Sleep Survey (sleepnumber.com/research)",48,85,65,72,42,78,78,55),
mk("HCY32","What Americans Name Their WiFi Networks: The Most Common SSIDs by Region","Most common WiFi network names by region — FBI Surveillance Van, Pretty Fly for a WiFi, The LAN Before Time","MAP","US","State choropleth","humor","WiGLE: WiFi Network Statistics (wigle.net/stats)",45,78,62,82,38,75,82,62),
mk("HCY33","The Curse of the Billy Goat and Other Sports Superstitions: Longest Championship Droughts","Longest professional sports championship droughts by franchise, mapped against city population","RANK","US","Bar chart","humor","ESPN: Sports Reference Championship Data (sports-reference.com)",55,72,72,72,52,68,72,82),
mk("HCY34","Americas Most Passive-Aggressive State: Yelp Review Sentiment Analysis","Average Yelp review politeness-to-actual-satisfaction ratio by state — where people are nicest about terrible experiences","MAP","US","State choropleth","humor","Yelp: Academic Dataset (yelp.com/dataset)",52,78,65,82,48,78,82,62),
mk("HCY35","The Dad Joke Index: Pun Appreciation by Country","Which countries rate puns as humor vs. verbal assault — cultural attitudes toward wordplay mapped globally","MAP","World","World choropleth","humor","Various: Cross-Cultural Humor Research (various academic sources)",45,72,62,82,42,78,85,52),
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
print(f"Injected {len(new)} new ideas (HCY batch)")
