"""
Auto-categorize all entries with empty topics[] fields.
Uses title, sub, section, and tbl to assign 2-5 relevant topic tags.
Preserves existing topics on entries that already have them.
"""
import re, os
from collections import Counter

DATA = os.path.join(os.path.dirname(__file__), 'data.js')

# ── TOPIC RULES ──
# Each rule: (topic_tag, list of keyword patterns to match against title+sub+section+tbl)
TOPIC_RULES = [
    ("economy", [r'\b(gdp|econom|wage|salary|income|wealth|debt|fiscal|monetary|recession|inflation|price|cost|spend|budget|tax|financ|bank|loan|credit|mortgage|stock|market|trade|tariff|import|export|currency|dollar|bitcoin|crypto|invest|profit|revenue|business|startup|entrepreneur|gig|freelanc|employment|unemploy|paycheck|afford)\b']),
    ("health", [r'\b(health|medic|hospital|doctor|nurse|pharma|drug|opioid|overdose|fentanyl|insulin|vaccin|disease|cancer|diabet|obesity|mental|depress|anxiety|suicide|mortal|death|die|dying|life expectan|birth|fertil|pregnan|maternal|infant|heart|lung|asthma|dementia|alzheim|covid|pandemic|telehealth|insur|medicaid|medicare|uninsured)\b']),
    ("education", [r'\b(education|school|college|university|student|teacher|tuition|degree|graduat|dropout|literacy|math|reading|NAEP|PISA|GPA|campus|professor|academic|STEM|enroll|scholarship|loan|FAFSA|charter|homeschool|kindergarten)\b']),
    ("crime", [r'\b(crime|murder|homicide|assault|robbery|theft|burglary|arson|shoot|gun|firearm|violen|incarcerat|prison|jail|arrest|police|officer|law enforcement|FBI|felon|recidiv|gang|fraud|cybercrime|hate crime)\b']),
    ("housing", [r'\b(hous|home|rent|mortgag|evict|homeless|shelter|apartment|tenant|landlord|zoning|vacant|foreclos|airbnb|gentrific|affordable|section 8|HUD|real estate|property value|ZHVI)\b']),
    ("climate", [r'\b(climate|warming|carbon|CO2|emission|greenhouse|sea level|glacier|wildfire|drought|flood|hurricane|tornado|extreme weather|temperature|heat wave|NOAA)\b']),
    ("environment", [r'\b(environment|pollution|toxic|superfund|waste|recycl|plastic|deforest|biodiversity|endangered|species|water quality|air quality|EPA|conservation|ecosystem|wetland|aquifer)\b']),
    ("food", [r'\b(food|nutrition|hunger|diet|calori|grocer|restaurant|fast food|farm|agriculture|crop|livestock|beef|poultry|dairy|egg|organic|GMO|pesticide|SNAP|breakfast|meal|eat)\b']),
    ("technology", [r'\b(tech|AI|artificial intellig|robot|automat|internet|broadband|digital|cyber|software|app|silicon|startup|patent|innovat|satellite|quantum|5G|blockchain|algorithm|machine learn)\b']),
    ("population", [r'\b(population|census|demograph|migration|immigra|emigra|refugee|asylum|birth rate|death rate|fertil|aging|median age|genera|millennial|gen z|boomer|urbaniz|rural|suburban|density)\b']),
    ("politics", [r'\b(politic|elect|vote|democrat|republican|partisan|congress|senat|governor|president|campaign|ballot|gerrymandr|lobby|legislat|law|regulation|policy|supreme court|judicial)\b']),
    ("inequality", [r'\b(inequal|gap|disparit|segregat|redlin|gini|percentile|quintile|top 1%|bottom|poorest|richest|wealth gap|wage gap|gender pay|racial|discriminat|privilege|mobil)\b']),
    ("labor", [r'\b(labor|worker|union|strike|minimum wage|overtime|gig work|remote work|telework|commut|unemploy|job|occupation|career|workforce|layoff|hiring|retirement|pension|burnout)\b']),
    ("international", [r'\b(global|world|countr|nation|international|foreign|UN |NATO|WHO|IMF|World Bank|OECD|EU |European|Asian|African|Latin America|Middle East|BRICS)\b']),
    ("military", [r'\b(militar|army|navy|air force|marine|defense|weapon|war|conflict|veteran|troop|deploy|nuclear|missile|drone|Pentagon|NATO|arms|combat)\b']),
    ("transportation", [r'\b(transport|transit|highway|road|bridge|rail|train|subway|bus|airport|flight|airline|commut|traffic|driver|car|vehicle|EV|electric vehicle|bike|pedestrian|port|shipping)\b']),
    ("energy", [r'\b(energy|oil|gas|coal|nuclear|solar|wind|renewable|electricity|grid|power plant|fracking|pipeline|OPEC|EIA|utility|blackout|battery|lithium)\b']),
    ("geography", [r'\b(geograph|map|spatial|GIS|county|state|region|urban|rural|coastal|mountain|river|lake|island|boundar|territory|elevation|latitude|longitude)\b']),
    ("immigration", [r'\b(immigra|emigra|refugee|asylum|border|ICE|detention|deportat|undocument|visa|citizen|naturaliz|DACA|dreamers|sanctuary|migrant)\b']),
    ("race", [r'\b(race|racial|Black|White|Hispanic|Latino|Asian|Native|Indigenous|minority|ethnic|segregat|redlin|civil rights|apartheid|colonialis|slavery)\b']),
    ("gender", [r'\b(gender|women|female|male|sex|LGBT|transgender|nonbinary|paternity|maternity|feminist|misogyn|reproductive|abortion|Title IX)\b']),
    ("children", [r'\b(child|kid|youth|teen|juvenile|infant|baby|pediatric|kindergarten|daycare|childcare|foster|adoption|custody)\b']),
    ("religion", [r'\b(religion|church|mosque|temple|faith|Christian|Muslim|Jewish|Hindu|Buddhist|atheist|secular|prayer|worship|congregation)\b']),
    ("agriculture", [r'\b(agricultur|farm|crop|harvest|livestock|cattle|poultry|dairy|irrigation|fertiliz|pesticide|USDA|ranch|arable|yield|subsid)\b']),
    ("sports", [r'\b(sport|athlet|football|soccer|basketball|baseball|hockey|tennis|golf|olympic|FIFA|NFL|NBA|MLB|NCAA|marathon|stadium|team|league|coach|player)\b']),
    ("entertainment", [r'\b(entertain|movie|film|TV|television|music|song|album|artist|Netflix|Spotify|gaming|video game|Steam|streaming|podcast|celebrity|Hollywood|Broadway|concert|box office)\b']),
    ("drugs", [r'\b(drug|opioid|fentanyl|heroin|cocaine|marijuana|cannabis|meth|overdose|addiction|substance|naloxone|DEA|cartel|trafficking)\b']),
    ("democracy", [r'\b(democra|autocra|authoritarian|dictator|freedom|liberty|rights|constitution|press freedom|censorship|regime|V-Dem)\b']),
    ("history", [r'\b(histor|ancient|century|colonial|empire|war |World War|Civil War|revolution|independence|legacy|former|historic|medieval|reconstruction)\b']),
    ("finance", [r'\b(financ|bank|Wall Street|stock|bond|invest|portfolio|hedge fund|venture capital|IPO|interest rate|Federal Reserve|SEC|insurance|credit)\b']),
    ("infrastructure", [r'\b(infrastruct|bridge|dam|road|highway|transit|broadband|grid|sewage|water system|telecom|5G|airport|port|railway)\b']),
    ("trade", [r'\b(trade|tariff|import|export|supply chain|shipping|freight|container|port|commerce|WTO|NAFTA|sanction)\b']),
    ("space", [r'\b(space|NASA|asteroid|satellite|orbit|Mars|moon|rocket|SpaceX|ISS|telescope|JWST|cosmic|galaxy|exoplanet|Artemis|launch)\b']),
    ("media", [r'\b(media|news|journalist|press|newspaper|social media|Facebook|Twitter|TikTok|Instagram|YouTube|misinformation|disinformation|fake news|censor)\b']),
    ("humor", [r'\b(weird|strange|bizarre|fun |funny|quirky|absurd|oddly|unusual|surprising|ridiculous|ironic|paradox)\b']),
    ("rural", [r'\b(rural|small town|Appalachia|heartland|farm country|outskirts|isolated|remote area|county seat)\b']),
    ("science", [r'\b(science|research|study|lab|experiment|discover|physics|chemistry|biology|genetic|DNA|CRISPR|Nobel|peer.review|journal|publication)\b']),
    ("manufacturing", [r'\b(manufactur|factory|industrial|assembly|production|supply chain|automation|reshoring|offshoring|rust belt)\b']),
    ("war", [r'\b(war|conflict|battle|invasion|troops|combat|ceasefire|missile|bombing|siege|casualties|peacekeep|armistice|Iran|Ukraine|Gaza|Syria|Iraq)\b']),
    ("guns", [r'\b(gun|firearm|shooting|mass shooting|second amendment|NRA|concealed carry|assault weapon|AR.15|ammunition)\b']),
    ("middle_east", [r'\b(Middle East|Iran|Iraq|Syria|Yemen|Saudi|Israel|Palestine|Gaza|Lebanon|Jordan|UAE|Qatar|Oman|Bahrain|Kuwait|Houthi|Strait of Hormuz)\b']),
    ("prices", [r'\b(price|cost|CPI|inflation|deflation|purchasing power|afford|expensive|cheap|bargain|premium|markup|sticker shock)\b']),
    ("psychology", [r'\b(psychology|cognitive|behavioral|mental health|therapy|counseling|anxiety|depression|PTSD|trauma|resilience|wellbeing|loneliness|isolation)\b']),
    ("law", [r'\b(law|legal|court|judge|jury|attorney|lawyer|prosecutor|defendant|plaintiff|lawsuit|litigation|statute|sentenc|parole|probation|bail|incarcerat|prison|exonerat|wrongful convict|civil asset|qualified immunit|public defender|plea|warrant|injunction|ordinance|tort|conviction|inmate|solitary|death row)\b']),
    ("demographics", [r'\b(demograph|median age|life expectancy|birth rate|death rate|household size|census tract|ethnic composition|racial composition|age distribution|dependency ratio|sex ratio|population pyramid|generational|centenarian|multigenerational|surname|language spoken|uncontacted|childfree|marriage rate|disability rate|nomad)\b']),
    ("poverty", [r'\b(poverty|poor|impoverish|destitut|food insecur|hunger|homeless|low.income|welfare|SNAP|WIC|free lunch|food stamp|food bank|section 8|public assist|safety net|deprivation|disadvantaged)\b']),
    ("data", [r'\b(dataset|open data|FOIA|data.gov|census data|GIS|geospatial|big data|data viz|data quality)\b']),
]


# Compile patterns
COMPILED_RULES = []
for tag, patterns in TOPIC_RULES:
    combined = '|'.join(patterns)
    COMPILED_RULES.append((tag, re.compile(combined, re.IGNORECASE)))


def assign_topics(title, sub, section, tbl):
    """Return list of 2-5 topic tags based on content."""
    searchable = f"{title} {sub} {section} {tbl}"
    matched = []
    for tag, pattern in COMPILED_RULES:
        if pattern.search(searchable):
            matched.append(tag)
    
    # Ensure at least 1 topic: fall back to section-based defaults
    if not matched:
        section_defaults = {
            'Economy': ['economy'],
            'Economy & Trade': ['economy', 'trade'],
            'Demographics': ['population', 'demographics'],
            'Health': ['health'],
            'Health & Medicine': ['health'],
            'Science & Technology': ['technology'],
            'History': ['history'],
            'Crime and Law Enforcement': ['crime'],
            'Law & Justice': ['crime', 'law'],
            'Food & Nutrition': ['food'],
            'Education': ['education'],
            'Sports & Recreation': ['sports'],
            'Sports & Athletics': ['sports'],
            'Entertainment': ['entertainment'],
            'Entertainment & Media': ['entertainment', 'media'],
            'Transportation': ['transportation'],
            'International Statistics': ['international'],
            'Geography & Environment': ['geography', 'environment'],
            'Climate': ['climate'],
            'Environment & Climate': ['environment', 'climate'],
            'Labor': ['labor'],
            'Labor & Employment': ['labor'],
            'Housing': ['housing'],
            'Housing & Real Estate': ['housing'],
            'Environment': ['environment'],
            'Elections': ['politics'],
            'Democracy & Voting': ['democracy', 'politics'],
            'Population': ['population'],
            'Energy': ['energy'],
            'Energy & Resources': ['energy'],
            'Finance': ['finance'],
            'Agriculture': ['agriculture'],
            'Agriculture & Food Systems': ['agriculture', 'food'],
            'Conflict & Security': ['war', 'military'],
            'Culture & Religion': ['religion'],
            'Guns & Weapons': ['guns', 'crime'],
            'Drugs & Substance Use': ['drugs', 'health'],
            'Children & Youth': ['children'],
            'Psychology & Behavior': ['psychology'],
            'Space & Exploration': ['space', 'science'],
            'Rural America': ['rural'],
            'Humor & Weird Data': ['humor'],
            'Manufacturing & Industry': ['manufacturing'],
            'Immigration & Migration': ['immigration'],
            'Politics & Governance': ['politics'],
        }
        matched = section_defaults.get(section, ['data'])
    
    # Cap at 5 topics
    return matched[:5]


def run():
    with open(DATA, 'r', encoding='utf-8') as f:
        text = f.read()
    
    lines = text.split('\n')
    filled = 0
    still_empty = 0
    topic_counts = Counter()
    
    for i, line in enumerate(lines):
        stripped = line.strip().lstrip(',')
        if not stripped.startswith('{id:'):
            continue
        
        # Check if topics is empty
        topics_m = re.search(r'topics:\[([^\]]*)\]', line)
        if not topics_m:
            continue
        
        existing = topics_m.group(1).strip()
        if existing:
            # Already has topics - count them
            for t in re.findall(r'"([^"]*)"', existing):
                topic_counts[t] += 1
            continue
        
        # Extract fields for categorization
        title_m = re.search(r'title:"([^"]*)"', line)
        sub_m = re.search(r'sub:"([^"]*)"', line)
        sect_m = re.search(r'section:"([^"]*)"', line)
        tbl_m = re.search(r'tbl:"([^"]*)"', line)
        
        title = title_m.group(1) if title_m else ''
        sub = sub_m.group(1) if sub_m else ''
        section = sect_m.group(1) if sect_m else ''
        tbl = tbl_m.group(1) if tbl_m else ''
        
        topics = assign_topics(title, sub, section, tbl)
        
        if topics:
            topics_str = ','.join(f'"{t}"' for t in topics)
            line = line.replace('topics:[]', f'topics:[{topics_str}]')
            lines[i] = line
            filled += 1
            for t in topics:
                topic_counts[t] += 1
        else:
            still_empty += 1
    
    with open(DATA, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))
    
    print(f"Filled topics for {filled} entries")
    print(f"Still empty: {still_empty}")
    
    print(f"\n=== FINAL TOPIC DISTRIBUTION ({len(topic_counts)} tags) ===")
    for t, c in topic_counts.most_common():
        print(f"  [{c:>5}x] {t}")


if __name__ == '__main__':
    run()
