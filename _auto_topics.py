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
    ("economy", [r'\b(gdp|econom|recession|fiscal|monetary|inflation|deflation|CPI|trade deficit|trade surplus|tariff|import quota|export quota|WTO|NAFTA|supply chain disruption|gig economy|labor market|unemploy rate|job market|manufacturing output|market crash|austerity|stimulus package|purchasing power)\b']),
    ("health", [r'\b(health care|healthcare|hospital|physician|nurse|pharma|vaccin|disease|cancer|diabet|obesity|life expectan|maternal mortal|infant mortal|heart disease|lung disease|asthma|dementia|alzheim|covid|pandemic|telehealth|medicaid|medicare|uninsured|epidem|public health|clinic|diagnos|patient|chronic illness|organ donor|blood supply|surgical|opioid crisis|overdose death|fentanyl|insulin)\b']),
    ("education", [r'\b(education|school|college|university|student|teacher|tuition|degree|graduat|dropout|literacy|math|reading|NAEP|PISA|GPA|campus|professor|academic|STEM|enroll|scholarship|loan|FAFSA|charter|homeschool|kindergarten)\b']),
    ("crime", [r'\b(crime|murder|homicide|assault|robbery|theft|burglary|arson|shoot|gun|firearm|violen|incarcerat|prison|jail|arrest|police|officer|law enforcement|FBI|felon|recidiv|gang|fraud|cybercrime|hate crime)\b']),
    ("housing", [r'\b(hous|home|rent|mortgag|evict|homeless|shelter|apartment|tenant|landlord|zoning|vacant|foreclos|airbnb|gentrific|affordable|section 8|HUD|real estate|property value|ZHVI)\b']),
    ("climate", [r'\b(climate|warming|carbon|CO2|emission|greenhouse|sea level|glacier|wildfire|drought|flood|hurricane|tornado|extreme weather|temperature|heat wave|NOAA)\b']),
    ("environment", [r'\b(environment|pollution|toxic|superfund|waste|recycl|plastic|deforest|biodiversity|endangered|species|water quality|air quality|EPA|conservation|ecosystem|wetland|aquifer)\b']),
    ("food", [r'\b(food|nutrition|hunger|diet|calori|grocer|restaurant|fast food|farm|agriculture|crop|livestock|beef|poultry|dairy|egg|organic|GMO|pesticide|SNAP|breakfast|meal|eat)\b']),
    ("technology", [r'\b(tech|AI|artificial intellig|robot|automat|internet|broadband|digital|cyber|software|app|silicon|startup|patent|innovat|satellite|quantum|5G|blockchain|algorithm|machine learn)\b']),
    ("population", [r'\b(population growth|population decline|population density|depopulat|overpopulat|birth rate|death rate|fertil rate|median age|aging population|youth bulge|baby boom|demographic shift|demographic transition|census population|ethnic composition|racial composition|age distribution|dependency ratio|sex ratio|population pyramid|centenarian|multigenerational|childfree|urbaniz|suburbaniz|population count|headcount|inhabitants)\b']),
    ("politics", [r'\b(politic|elect|voter|democrat|republican|partisan|congress|senat|governor|president|campaign|ballot|gerrymandr|lobby|legislat|supreme court|autocra|authoritarian|dictator|constitution|press freedom|censorship|regime|V-Dem|bipartisan|filibuster|caucus|primary election|PAC|dark money|party affiliation|red state|blue state|swing state|ranked choice)\b']),
    ("inequality", [r'\b(inequal|gap|disparit|segregat|redlin|gini|percentile|quintile|top 1%|bottom|poorest|richest|wealth gap|wage gap|gender pay|racial|discriminat|privilege|mobil)\b']),
    ("labor", [r'\b(labor|worker|union|strike|minimum wage|overtime|gig work|remote work|telework|commut|unemploy|job|occupation|career|workforce|layoff|hiring|retirement|pension|burnout)\b']),
    ("international", [r'\b(international|cross.border|bilateral|multilateral|UN |NATO|IMF|World Bank|OECD|EU |G7|G20|BRICS|treaty|diplomat|embassy|foreign aid|foreign policy|geopolitic|transnational)\b']),
    ("military", [r'\b(militar|army|navy|air force|marine|defense|weapon|war|conflict|veteran|troop|deploy|nuclear|missile|drone|Pentagon|NATO|arms|combat|battle|invasion|ceasefire|bombing|siege|casualties|peacekeep|armistice)\b']),
    ("transportation", [r'\b(transport|transit|highway|road|bridge|rail|train|subway|bus|airport|flight|airline|commut|traffic|driver|car|vehicle|EV|electric vehicle|bike|pedestrian|port|shipping)\b']),
    ("energy", [r'\b(energy|oil|gas|coal|nuclear|solar|wind|renewable|electricity|grid|power plant|fracking|pipeline|OPEC|EIA|utility|blackout|battery|lithium)\b']),
    ("geography", [r'\b(geograph|topograph|terrain|coastal|mountain|river|lake|island|peninsula|volcano|canyon|desert|tundra|plateau|archipelago|elevation|continent|ocean|glacier|fjord|delta|basin|watershed|landform|erosion|sediment|reef|cave|geyser|wetland|marsh|strait|cape|isthmus)\b']),
    ("immigration", [r'\b(immigra|emigra|refugee|asylum|border|ICE|detention|deportat|undocument|visa|citizen|naturaliz|DACA|dreamers|sanctuary|migrant)\b']),
    ("race", [r'\b(race|racial|Black|White|Hispanic|Latino|Asian|Native|Indigenous|minority|ethnic|segregat|redlin|civil rights|apartheid|colonialis|slavery)\b']),
    ("gender", [r'\b(gender|women|female|male|sex|LGBT|transgender|nonbinary|paternity|maternity|feminist|misogyn|reproductive|abortion|Title IX)\b']),
    ("children", [r'\b(child|kid|youth|teen|juvenile|infant|baby|pediatric|kindergarten|daycare|childcare|foster|adoption|custody)\b']),
    ("religion", [r'\b(religion|church|mosque|temple|faith|Christian|Muslim|Jewish|Hindu|Buddhist|atheist|secular|prayer|worship|congregation)\b']),
    ("agriculture", [r'\b(agricultur|farm|crop|harvest|livestock|cattle|poultry|dairy|irrigation|fertiliz|pesticide|USDA|ranch|arable|yield|subsid)\b']),
    ("sports", [r'\b(sport|athlet|football|soccer|basketball|baseball|hockey|tennis|golf|olympic|FIFA|NFL|NBA|MLB|NCAA|marathon|stadium|team|league|coach|player)\b']),
    ("entertainment", [r'\b(entertain|movie|film|TV|television|music|song|album|artist|Netflix|Spotify|gaming|video game|Steam|streaming|podcast|celebrity|Hollywood|Broadway|concert|box office)\b']),
    ("drugs", [r'\b(drug|opioid|fentanyl|heroin|cocaine|marijuana|cannabis|meth|overdose|addiction|substance|naloxone|DEA|cartel|trafficking)\b']),

    ("history", [r'\b(histor|ancient|century|colonial|empire|World War|Civil War|revolution|independence|medieval|reconstruction|antebellum|prohibition|postwar|prewar|founding fathers|archaeological|heritage site)\b']),
    ("finance", [r'\b(financ|banking|Wall Street|stock market|bond market|invest|portfolio|hedge fund|venture capital|IPO|interest rate|Federal Reserve|SEC|insurance industry|credit score|credit rating|derivatives|forex|pension fund|401k|mutual fund|bankruptcy|debt)\b']),
    ("infrastructure", [r'\b(infrastruct|bridge|dam|road|highway|transit|broadband|grid|sewage|water system|telecom|5G|airport|port|railway)\b']),

    ("space", [r'\b(space|NASA|asteroid|satellite|orbit|Mars|moon|rocket|SpaceX|ISS|telescope|JWST|cosmic|galaxy|exoplanet|Artemis|launch)\b']),
    ("media", [r'\b(media|news|journalist|press|newspaper|social media|Facebook|Twitter|TikTok|Instagram|YouTube|misinformation|disinformation|fake news|censor)\b']),
    ("humor", [r'\b(weird|strange|bizarre|fun |funny|quirky|absurd|oddly|unusual|surprising|ridiculous|ironic|paradox)\b']),
    ("rural", [r'\b(rural|small town|Appalachia|heartland|farm country|outskirts|isolated|remote area|county seat)\b']),
    ("science", [r'\b(scientific|laboratory|experiment|physics|chemistry|biology|genetic|DNA|CRISPR|Nobel|geology|astronomy|ecology|botany|zoology|neuroscience|paleontology|seismolog|meteorolog|oceanograph|microbiology|virology|particle|quantum|isotope|species|evolution|fossil)\b']),
    ("manufacturing", [r'\b(manufactur|factory|industrial|assembly|production|supply chain|automation|reshoring|offshoring|rust belt)\b']),

    ("guns", [r'\b(gun|firearm|shooting|mass shooting|second amendment|NRA|concealed carry|assault weapon|AR.15|ammunition)\b']),
    ("middle_east", [r'\b(Middle East|Iran|Iraq|Syria|Yemen|Saudi|Israel|Palestine|Gaza|Lebanon|Jordan|UAE|Qatar|Oman|Bahrain|Kuwait|Houthi|Strait of Hormuz)\b']),

    ("psychology", [r'\b(psychology|cognitive|behavioral|mental health|therapy|counseling|anxiety|depression|PTSD|trauma|resilience|wellbeing|loneliness|isolation)\b']),
    ("law", [r'\b(law|legal|court|judge|jury|attorney|lawyer|prosecutor|defendant|plaintiff|lawsuit|litigation|statute|sentenc|parole|probation|bail|incarcerat|prison|exonerat|wrongful convict|civil asset|qualified immunit|public defender|plea|warrant|injunction|ordinance|tort|conviction|inmate|solitary|death row)\b']),

    ("poverty", [r'\b(poverty|poor|impoverish|destitut|food insecur|hunger|homeless|low.income|welfare|SNAP|WIC|free lunch|food stamp|food bank|section 8|public assist|safety net|deprivation|disadvantaged)\b']),

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
            # Core tag-name sections (lowercase)
            'economy': ['economy'], 'health': ['health'], 'education': ['education'],
            'crime': ['crime'], 'housing': ['housing'], 'climate': ['climate'],
            'environment': ['environment'], 'food': ['food'], 'technology': ['technology'],
            'population': ['population'], 'politics': ['politics'], 'inequality': ['inequality'],
            'labor': ['labor'], 'international': ['international'], 'military': ['military'],
            'transportation': ['transportation'], 'energy': ['energy'], 'geography': ['geography'],
            'immigration': ['immigration'], 'race': ['race'], 'gender': ['gender'],
            'children': ['children'], 'religion': ['religion'], 'agriculture': ['agriculture'],
            'sports': ['sports'], 'entertainment': ['entertainment'], 'drugs': ['drugs'],
            'history': ['history'], 'finance': ['finance'], 'infrastructure': ['infrastructure'],
            'space': ['space'], 'media': ['media'], 'humor': ['humor'], 'rural': ['rural'],
            'science': ['science'], 'manufacturing': ['manufacturing'], 'guns': ['guns'],
            'middle_east': ['middle_east'], 'psychology': ['psychology'], 'law': ['law'],
            'poverty': ['poverty'],
            # Merged/legacy tag aliases
            'demographics': ['population'], 'democracy': ['politics'],
            'prices': ['economy'], 'trade': ['economy','international'],
            'war': ['military'], 'data': ['technology'],
            # Styled section names
            'Economy': ['economy'], 'Economy & Trade': ['economy'],
            'Demographics': ['population'], 'Health': ['health'],
            'Health & Medicine': ['health'], 'Science & Technology': ['technology','science'],
            'History': ['history'], 'Crime and Law Enforcement': ['crime','law'],
            'Law & Justice': ['crime','law'], 'Food & Nutrition': ['food'],
            'Education': ['education'], 'Sports & Recreation': ['sports'],
            'Sports & Athletics': ['sports'], 'Entertainment': ['entertainment'],
            'Entertainment & Media': ['entertainment','media'],
            'Transportation': ['transportation'], 'International Statistics': ['international'],
            'Geography & Environment': ['geography','environment'],
            'Climate': ['climate'], 'Environment & Climate': ['environment','climate'],
            'Labor': ['labor'], 'Labor & Employment': ['labor'],
            'Housing': ['housing'], 'Housing & Real Estate': ['housing'],
            'Environment': ['environment'], 'Elections': ['politics'],
            'Democracy & Voting': ['politics'], 'Population': ['population'],
            'Energy': ['energy'], 'Energy & Resources': ['energy'],
            'Finance': ['finance'], 'Agriculture': ['agriculture'],
            'Agriculture & Food Systems': ['agriculture','food'],
            'Conflict & Security': ['military'], 'Culture & Religion': ['religion'],
            'Guns & Weapons': ['guns','crime'], 'Drugs & Substance Use': ['drugs'],
            'Children & Youth': ['children'], 'Psychology & Behavior': ['psychology'],
            'Space & Exploration': ['space','science'], 'Rural America': ['rural'],
            'Humor & Weird Data': ['humor'], 'Manufacturing & Industry': ['manufacturing'],
            'Immigration & Migration': ['immigration'], 'Politics & Governance': ['politics'],
            'Infrastructure & Systems': ['infrastructure'],
            'Migration & Borders': ['immigration'], 'Technology & Data': ['technology'],
            'Public Safety': ['crime'], 'Geography': ['geography'], 'Multiple': ['inequality'],
            # Census / Statistical Abstract sections
            'Income': ['economy'], 'Income Expenditures': ['economy'],
            'Arts Recreation': ['entertainment','sports'],
            'Arts Recreation & Travel': ['entertainment','sports'],
            'Business Enterprise': ['economy'],
            'State Government': ['politics'], 'State Govt': ['politics'],
            'State & Local Govt': ['politics'],
            'Federal Government': ['politics','finance'],
            'Federal Government Finances': ['finance'],
            'Federal Govt': ['politics','finance'],
            'Foreign Commerce': ['economy','international'],
            'Foreign Commerce & Aid': ['economy','international'],
            'Social Insurance': ['economy','inequality'],
            'Wholesale Retail': ['economy'], 'Wholesale & Retail Trade': ['economy'],
            'Wholesale and Retail Trade': ['economy'],
            'National Security': ['military'], 'National Security & Veterans': ['military'],
            'Births Deaths Marriages': ['population'],
            'Construction': ['housing'], 'Manufactures': ['manufacturing'],
            'Forestry Fishing': ['agriculture','environment'],
            'Information': ['technology','media'], 'Internal Migration': ['immigration'],
            # Compound dash sections
            'Business  -  Income': ['economy'],
            'Social Insurance  -  Elections': ['economy','politics'],
            'Construction  -  Population': ['housing','population'],
            'Manufactures  -  Income': ['manufacturing','economy'],
            'Income  -  Elections': ['economy','politics'],
            'Construction  -  Income': ['housing','economy'],
            'Income  -  Population': ['economy','population'],
            'Federal Govt  -  Income': ['finance','economy'],
            'State Govt  -  Income': ['politics','economy'],
            'Transportation  -  Income': ['transportation','economy'],
            'Business Enterprise  -  Foreign Commerce': ['economy','international'],
            'Transportation &tic': ['transportation'],
        }
        matched = section_defaults.get(section, [])
    # If still empty, try parsing compound section (pipe/slash delimited)
    if not matched:
        _aliases = {'demographics':'population','democracy':'politics',
                    'prices':'economy','trade':'economy','war':'military'}
        _valid = {t for t,_ in TOPIC_RULES}
        parts = []
        if '|' in section:
            parts = [p.strip().lower().replace(' ','_') for p in section.split('|')]
        elif '/' in section:
            parts = [p.strip().lower().replace(' ','_') for p in section.split('/')]
        for p in parts:
            p = _aliases.get(p, p)
            if p in _valid and p not in matched:
                matched.append(p)
    
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
