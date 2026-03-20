"""
fix_topics_v2.py
- Removes non-canonical topics
- Maps near-canonical to canonical
- Fills empty/sparse arrays via keyword matching
- Caps at 6 topics per idea
- Preserves good existing topics
"""
import re
from collections import Counter

# ── CANONICAL SET ─────────────────────────────────────────────────────────────
CANONICAL = {
    'health','economy','politics','crime','poverty','housing','education',
    'labor','race','gender','immigration','war','military','energy','climate',
    'environment','food','agriculture','drugs','guns','finance','trade',
    'inequality','transportation','infrastructure','technology','media',
    'population','international','democracy','religion','history','space',
    'data','humor','science','geography','demographics','children','rural',
    'manufacturing','law',
}

# ── MAP BAD → CANONICAL ───────────────────────────────────────────────────────
REMAP = {
    'elections':      'politics',
    'prices':         'economy',
    'water':          'environment',
    'culture':        'history',
    'social insurance': 'poverty',
    'arts':           'history',
    'retail':         'economy',
    'business':       'economy',
    'national security': 'military',
    'economics':      'economy',
    'industry':       'manufacturing',
    'defense':        'military',
    'language':       'history',
    'tourism':        'geography',
    'sports':         'history',
    'alcohol':        'drugs',
    'insurance':      'finance',
}

# ── KEYWORD → TOPIC RULES ────────────────────────────────────────────────────
# Each rule: list of keywords (any match) → topic to add
# Keywords matched against: title + sub + tags + section (all lowercased)
RULES = [
    # Health
    (['cancer','mortality','disease','hospital','diabetes','obesity','opioid','overdose',
      'mental health','suicide','vaccination','vaccine','medicaid','medicare','insurance',
      'drug death','naloxone','fentanyl','epidemic','pandemic','covid','flu','h5n1',
      'birth rate','life expectancy','infant','maternal','eating disorder','depression',
      'anxiety','loneliness','therapy','prescription','pharmaceutical','glp-1','ozempic',
      'antidepressant','viagra','ed drug','nursing home','eldercare','alcohol','drinking',
      'smoking','nicotine','lead','asthma','pm2.5','pollution health'], 'health'),

    # Economy
    (['gdp','income','wage','salary','unemployment','poverty rate','inflation','cpi',
      'tariff','trade deficit','manufacturing','jobs','layoff','recession','growth',
      'productivity','wealth','corporate','profit','revenue','tax','subsidy','bail',
      'federal spending','budget','deficit','debt','interest rate','bond','dollar',
      'currency','exchange rate','purchasing power','cost of living','shrinkflation',
      'price','consumer','retail','spending','credit'], 'economy'),

    # Politics
    (['vote','election','republican','democrat','trump','biden','harris','congress',
      'senate','house','partisan','political','policy','legislation','bill','law passed',
      'regulation','executive','president','governor','mayor','campaign','ballot',
      'gerrymandering','redistricting','approval rating','polling','party','doge',
      'federal workforce','government cut','sanctuary'], 'politics'),

    # Crime
    (['crime','murder','homicide','assault','rape','robbery','theft','incarceration',
      'prison','jail','arrest','police','fbi ucr','violent crime','property crime',
      'domestic violence','trafficking','cartel','gang','recidivism','parole','probation',
      'sentencing'], 'crime'),

    # Poverty
    (['poverty','snap','food stamp','welfare','medicaid','housing assistance','eviction',
      'homeless','unhoused','low income','minimum wage','working poor','food insecurity',
      'hunger','safety net','transfer payment','payday loan','unbanked'], 'poverty'),

    # Housing
    (['housing','home price','rent','mortgage','eviction','foreclosure','vacancy',
      'zoning','affordable housing','homeownership','landlord','tenant','real estate',
      'construction','permit','housing start','homelessness','shelter','akiya',
      'one euro house','home value'], 'housing'),

    # Education
    (['school','education','college','university','student','teacher','literacy',
      'graduation','dropout','tuition','student loan','stem','degree','academic',
      'learning','curriculum','test score','sat','act','kindergarten','preschool',
      'homeschool','school funding','per pupil','counselor','extracurricular'], 'education'),

    # Labor
    (['worker','workforce','employment','labor','union','strike','wage','salary',
      'job','occupation','remote work','gig','freelance','automation','layoff',
      'workplace','h-1b','visa worker','farm worker','caregiver','direct care',
      'teacher salary','minimum wage'], 'labor'),

    # Race
    (['race','racial','black','white','hispanic','latino','asian','native american',
      'indigenous','minority','segregation','redlining','discrimination','civil rights',
      'diversity','equity','inclusion','reparations','hate crime','ethnicity',
      'white supremacy','kkk'], 'race'),

    # Gender
    (['gender','women','men','female','male','lgbtq','transgender','abortion','birth control',
      'maternal','pregnancy','fertility','wage gap','gender gap','domestic violence',
      'sexual assault','harassment','title ix','feminist'], 'gender'),

    # Immigration
    (['immigrant','immigration','migrant','undocumented','deportation','ice','border',
      'asylum','refugee','visa','green card','naturalization','daca','dreamer',
      'foreign born','h-1b','h-2a','sanctuary city'], 'immigration'),

    # War / Military
    (['war','military','combat','conflict','battle','soldier','army','navy',
      'air force','marines','veteran','weapon','missile','drone','nato','defense',
      'troops','casualties','attack','invasion','ukraine','russia','gaza','houthi',
      'wagner','coup','armed conflict'], 'war'),

    # Energy
    (['energy','oil','gas','coal','electricity','power grid','renewable','solar',
      'wind','nuclear','petroleum','fracking','pipeline','carbon','emissions',
      'fossil fuel','clean energy','data center power','ev charging','kwh','mwh',
      'utility','eia','barrel','brent','opec','lng','uranium','reactor'], 'energy'),

    # Climate
    (['climate','global warming','temperature','sea level','flood','wildfire',
      'hurricane','drought','heat','carbon','greenhouse','glacier','arctic',
      'weather','extreme weather','insurance retreat','climate migration',
      'paris agreement','1.5 degrees','deforestation climate'], 'climate'),

    # Environment
    (['environment','pollution','air quality','water quality','toxic','superfund',
      'epa','deforestation','biodiversity','species','wildlife','ocean','river',
      'aquifer','groundwater','drought','wildfire','forest','wetland','plastic',
      'waste','landfill','recycling'], 'environment'),

    # Food
    (['food','diet','nutrition','hunger','calorie','restaurant','fast food',
      'grocery','supermarket','meal','eating','obesity','diabetes food',
      'food desert','snap food','mcdonald','burger','egg price','beef','chicken',
      'produce','farm to table','processed food','ultra processed'], 'food'),

    # Agriculture
    (['farm','agriculture','crop','livestock','cattle','poultry','dairy',
      'harvest','irrigation','drought agriculture','usda','rural farm',
      'agribusiness','fertilizer','pesticide','soybean','corn','wheat',
      'grain','ogallala','aquifer farm'], 'agriculture'),

    # Drugs
    (['drug','opioid','heroin','fentanyl','meth','cocaine','marijuana','cannabis',
      'alcohol','addiction','overdose','rehab','treatment','naloxone','narcan',
      'pill mill','prescription drug','ozempic','glp-1 drug','pharmaceutical',
      'substance use','dea','cartel drug'], 'drugs'),

    # Guns
    (['gun','firearm','weapon','shooting','mass shooting','homicide gun',
      'second amendment','nra','background check','concealed carry',
      'open carry','assault rifle','handgun','pistol','atf','gun sale',
      'gun ownership','gun violence'], 'guns'),

    # Finance
    (['bank','finance','credit','debt','loan','mortgage finance','interest',
      'investment','stock','market','wall street','hedge fund','private equity',
      'pension','retirement','savings','bankruptcy','default','foreclosure',
      'payday','insurance','premium','bond','yield','treasury','federal reserve',
      'crypto','bitcoin','nft','stablecoin'], 'finance'),

    # Trade
    (['trade','export','import','tariff','wto','nafta','usmca','supply chain',
      'manufacturing trade','china trade','global trade','trade deficit',
      'trade war','protectionism','offshore','reshore','nearshore','customs',
      'freight','shipping trade','port','container'], 'trade'),

    # Inequality
    (['inequality','gini','wealth gap','income gap','disparity','rich','poor gap',
      'top 1 percent','bottom 50','wealth concentration','class','economic mobility',
      'upward mobility','social mobility','regressive','progressive tax',
      'inheritance','estate'], 'inequality'),

    # Transportation
    (['transit','transportation','highway','road','bridge','car','vehicle',
      'truck','bus','train','rail','subway','metro','airport','airline',
      'commute','traffic','ev transportation','autonomous','bike','pedestrian',
      'port transport','shipping transport'], 'transportation'),

    # Infrastructure
    (['infrastructure','bridge','road','water system','sewer','broadband',
      'internet access','power grid','electric grid','pipeline infra',
      'dam','levee','port','airport infra','transit infra','fiber','5g',
      'lead pipe','water main'], 'infrastructure'),

    # Technology
    (['technology','tech','ai','artificial intelligence','machine learning',
      'software','algorithm','data center','cloud','internet','social media',
      'platform','startup','silicon valley','computer','smartphone','app',
      'automation tech','robot','semiconductor','chip','chatgpt','llm',
      'surveillance','facial recognition'], 'technology'),

    # Media
    (['media','news','journalism','newspaper','television','radio','podcast',
      'social media','facebook','instagram','tiktok','twitter','youtube',
      'misinformation','disinformation','fake news','algorithm media',
      'press freedom','censorship','advertising','influencer'], 'media'),

    # Population
    (['population','demographic','birth rate','death rate','fertility',
      'aging','elderly','baby boomer','millennial','gen z','generation',
      'migration population','urbanization','rural urban','density',
      'census','household','family size','marriage','divorce','single'], 'population'),

    # International
    (['international','global','world','foreign','country','nation','bilateral',
      'multilateral','united nations','imf','world bank','nato','eu','g7','g20',
      'brics','diplomacy','sanctions','embassy','sovereignty','geopolitic'], 'international'),

    # Democracy
    (['democracy','autocracy','authoritarian','election integrity','voting rights',
      'gerrymandering','press freedom','judicial independence','rule of law',
      'civil liberties','human rights','freedom house','v-dem','populism',
      'coup democracy','backsliding','electoral fraud','disinformation vote'], 'democracy'),

    # Religion
    (['religion','church','mosque','synagogue','temple','faith','christian',
      'muslim','jewish','hindu','buddhist','secular','atheist','evangelical',
      'catholic','protestant','bible belt','religiosity','prayer',
      'religious freedom'], 'religion'),

    # History
    (['history','historical','1900','1800','1700','century','decade','era',
      'war history','civil war','wwii','world war','cold war','reconstruction',
      'jim crow','redlining history','gilded age','depression era','new deal',
      'great migration','colonial','slavery','segregation history'], 'history'),

    # Space
    (['space','nasa','rocket','satellite','orbit','moon','mars','planet',
      'asteroid','galaxy','telescope','astronaut','spacex','starship',
      'iss','artemis','commercial space','starlink','launch','spacecraft'], 'space'),

    # Science
    (['science','research','study','clinical trial','peer reviewed','data science',
      'physics','chemistry','biology','genetics','dna','evolution','experiment',
      'publication','journal','nature','lancet','nejm','cdc study',
      'r&d','innovation','patent','discovery','breakthrough'], 'science'),

    # Geography
    (['geography','map','geographic','spatial','location','place','region',
      'county geography','state geography','border','territory','latitude',
      'longitude','gis','cartography','topography','coast','inland',
      'urban rural','metropolitan','suburb','exurb'], 'geography'),

    # Demographics
    (['demographic','age distribution','median age','dependency ratio',
      'generational','cohort','birth cohort','boomer','millennial',
      'aging population','youth bulge','population pyramid',
      'sex ratio','gender ratio','missing men'], 'demographics'),

    # Children
    (['child','children','kid','youth','teen','adolescent','infant','baby',
      'school age','juvenile','foster care','child poverty','child welfare',
      'daycare','pediatric','early childhood','kindergarten children'], 'children'),

    # Rural
    (['rural','small town','remote','countryside','farm community','appalachian',
      'coal country','rust belt town','dying town','rural hospital','rural school',
      'rural broadband','rural poverty','rural white','rural america'], 'rural'),

    # Manufacturing
    (['manufacturing','factory','plant','industrial','reshoring','offshoring',
      'auto industry','steel','aluminum','semiconductor fab','chips act',
      'assembly line','supply chain manufacturing','union manufacturing',
      'rust belt','deindustrialization','automation factory'], 'manufacturing'),

    # Law
    (['law','legal','court','supreme court','lawsuit','litigation','criminal justice',
      'sentencing law','mandatory minimum','civil rights law','roe v wade',
      'dobbs','regulation law','compliance','attorney','lawyer','prosecution',
      'public defender','bail reform','drug law'], 'law'),

    # Humor
    (['weird','strange','ironic','paradox','irony','joke','satire','absurd',
      'funny','strip club','shrinkflation','tipping','vending machine',
      'hotdog sandwich','bizarre','unexpected','counterintuitive funny'], 'humor'),
]

# ── LOAD DATA.JS ──────────────────────────────────────────────────────────────
with open('data.js', encoding='utf-8') as f:
    content = f.read()

lines = content.split('\n')
new_lines = []
stats = Counter()

for line in lines:
    if not (line.startswith('{id:') or line.startswith(',{id:')):
        new_lines.append(line)
        continue

    # Extract fields for matching
    title_m  = re.search(r'title:"([^"]*)"', line)
    sub_m    = re.search(r'sub:"([^"]*)"', line)
    tags_m   = re.search(r'tags:"([^"]*)"', line)
    sect_m   = re.search(r'section:"([^"]*)"', line)
    topics_m = re.search(r'topics:\[([^\]]*)\]', line)

    title   = title_m.group(1).lower()  if title_m  else ''
    sub     = sub_m.group(1).lower()    if sub_m    else ''
    tags    = tags_m.group(1).lower()   if tags_m   else ''
    section = sect_m.group(1).lower()   if sect_m   else ''
    haystack = f"{title} {sub} {tags} {section}"

    # Parse existing topics
    existing_raw = re.findall(r'"([^"]+)"', topics_m.group(1)) if topics_m else []

    # Step 1: remap non-canonical
    remapped = []
    for t in existing_raw:
        if t in CANONICAL:
            remapped.append(t)
        elif t in REMAP:
            remapped.append(REMAP[t])
            stats['remapped'] += 1
        else:
            stats['dropped'] += 1
            # drop it

    existing = set(remapped)

    # Step 2: add topics from keyword rules
    for keywords, topic in RULES:
        if any(kw in haystack for kw in keywords):
            existing.add(topic)

    # Step 3: cap at 6 most relevant — preserve ones already there, then add
    # Priority: keep originally-assigned canonical topics first, then rule-matched
    original_set = set(remapped)
    new_set = existing - original_set
    final = list(original_set) + [t for t in new_set if t not in original_set]
    # Trim to 6 — keep originals, drop lowest-priority new ones
    final = final[:6]

    # Step 4: rewrite topics in line
    new_topics_str = ','.join(f'"{t}"' for t in final)
    new_line = re.sub(r'topics:\[[^\]]*\]', f'topics:[{new_topics_str}]', line)
    new_lines.append(new_line)

    if not topics_m or not re.findall(r'"([^"]+)"', topics_m.group(1)):
        stats['filled_empty'] += 1
    elif len(final) > len(original_set):
        stats['enriched'] += 1

print(f"Remapped non-canonical: {stats['remapped']}")
print(f"Dropped unknown:        {stats['dropped']}")
print(f"Empty filled:           {stats['filled_empty']}")
print(f"Enriched sparse:        {stats['enriched']}")

new_content = '\n'.join(new_lines)
with open('data.js', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Written. Running audit...")
all_topics_raw = re.findall(r'topics:\[([^\]]*)\]', new_content)
empty_after = sum(1 for t in all_topics_raw if t.strip() == '')
print(f"Empty topics after: {empty_after}")
all_topics = []
for t in all_topics_raw:
    for x in re.findall(r'"([^"]+)"', t):
        all_topics.append(x)
print(f"Total assignments: {len(all_topics)}")
bad = [t for t in all_topics if t not in CANONICAL]
if bad:
    print(f"Non-canonical remaining: {Counter(bad).most_common(10)}")
else:
    print("All topics canonical.")
