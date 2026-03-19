"""
backfill_topics.py
Assign topics[] array to every idea based on section + keyword matching.
Topics are multi-value — one idea can have several.
"""
import re, json

# ── TOPIC DEFINITIONS ─────────────────────────────────────────────────────────
# Each entry: (topic_tag, [keywords to match in title+sub+tags+section])
TOPIC_RULES = [
    # Broad life/society topics
    ('war',           ['war','conflict','combat','weapon','nuclear','warhead','bomb','drone strike','arms','proxy war','invasion','battle','military deaths','troop','nato','troops']),
    ('military',      ['military','defense','national security','pentagon','veteran','navy','army','air force','marines','reserve','national guard','base overseas']),
    ('crime',         ['crime','criminal','incarcerat','prison','jail','murder','homicide','violent crime','property crime','arrest','police','law enforcement','victim','assault','theft','fraud']),
    ('drugs',         ['drug','opioid','fentanyl','overdose','heroin','methamphetamine','addiction','substance use','naloxone','dea','dealer','rehab','treatment program']),
    ('guns',          ['gun','firearm','shooting','mass shooting','weapon','second amendment','background check','carry','handgun','rifle','ammunition']),
    ('health',        ['health','hospital','doctor','physician','nurse','medicine','disease','cancer','diabetes','obesity','mental health','mortality','life expectancy','medicaid','medicare','insurance','prescription','drug cost','clinic','patient','surgery','chronic']),
    ('poverty',       ['poverty','poor','low income','snap','food stamp','welfare','homeless','destitute','hunger','food insecur','hardship','evict','unhoused','material deprivation','safety net']),
    ('food',          ['food','farm','agriculture','crop','hunger','grocery','nutrition','calorie','diet','eat','meal','restaurant','famine','malnutrition','food desert','usda']),
    ('energy',        ['energy','electricity','power grid','solar','wind','oil','gas','coal','renewable','fossil fuel','nuclear power','utility','kilowatt','barrel','refinery','petroleum']),
    ('climate',       ['climate','temperature','global warming','carbon','co2','emission','greenhouse','drought','flood','wildfire','sea level','hurricane','storm','heat wave','glacier','deforestation','ipcc']),
    ('economy',       ['economy','gdp','economic','recession','growth','inflation','productivity','fiscal','monetary','trade deficit','surplus','gdp per capita','national income']),
    ('labor',         ['labor','worker','wage','employment','unemploy','job','workforce','union','strike','minimum wage','gig','salary','occupation','layoff','hire']),
    ('housing',       ['housing','rent','home','mortgage','evict','homelessness','affordable','zoning','landlord','tenant','real estate','apartment','vacancy','shelter','hud']),
    ('education',     ['education','school','college','university','student','teacher','tuition','literacy','dropout','graduation','campus','curriculum','classroom','degree','naep','pisa']),
    ('politics',      ['election','vote','democrat','republican','partisan','congress','senate','legislature','gerrymandering','redistrict','campaign','ballot','political','president','governor','mayor','policy','lobbyist']),
    ('immigration',   ['immigr','migrant','border','asylum','refugee','visa','deportation','undocumented','citizenship','naturalization','daca','customs','ice enforcement','h-1b','h-2']),
    ('race',          ['race','racial','racism','white','black','hispanic','latino','asian','native american','indigenous','minority','segregation','redlining','discrimination','equity','diversity','ethnic']),
    ('gender',        ['gender','women','female','male','sex','maternal','feminist','wage gap','pregnancy','abortion','birth control','reproductive','lgbtq','transgender','maternity']),
    ('technology',    ['technology','tech','software','ai','artificial intelligence','algorithm','data center','semiconductor','chip','robot','automation','cyber','internet','broadband','startup','silicon valley','patent','r&d']),
    ('media',         ['media','news','journalism','newspaper','social media','facebook','twitter','instagram','press','broadcast','television','podcast','streaming','censorship','misinformation']),
    ('religion',      ['religion','church','faith','god','christian','catholic','protestant','evangelical','muslim','islam','jewish','hindu','buddhist','secular','worship','congregation','spiritual']),
    ('population',    ['population','birth rate','fertility','death rate','aging','demographic','census','household','migration','urbanization','suburban','rural','density','baby']),
    ('transportation',['transportation','transit','highway','road','commute','traffic','rail','bus','subway','airport','airline','freight','shipping','trucking','infrastructure','bridge']),
    ('infrastructure',['infrastructure','bridge','road','highway','dam','levee','water system','sewer','grid','pipeline','port','broadband','utility','construction','repair']),
    ('environment',   ['environment','pollution','toxic','superfund','epa','air quality','water quality','wildfire','habitat','species','biodiversity','conservation','national park','forest','river','wetland']),
    ('finance',       ['finance','bank','credit','debt','loan','investment','stock','bond','interest rate','federal reserve','wall street','hedge fund','private equity','bankruptcy','401k','retirement','pension','insurance premium']),
    ('trade',         ['trade','export','import','tariff','wto','nafta','supply chain','manufacturing','offshoring','globalization','trade deficit','trade surplus','fdi','foreign direct']),
    ('inequality',    ['inequality','gini','income gap','wealth gap','disparity','haves','have-not','top 1%','bottom quintile','redistribution','progressive','regressive']),
    ('democracy',     ['democracy','voting','election','voter id','suppression','turnout','representation','autocracy','authoritarian','civil liberties','free speech','press freedom','corruption','transparency']),
    ('agriculture',   ['farm','farmer','crop','livestock','commodity','usda','corn','soybean','wheat','cattle','dairy','pesticide','irrigation','drought','harvest','agricultural']),
    ('international', ['global','world','country','nation','international','foreign','abroad','overseas','diplomatic','treaty','united nations','imf','world bank','oecd','geopolit']),
    ('history',       ['historical','1900','1800','1950','1960','1970','1980','trend since','decades','century','era','post-war','civil war','great depression','cold war','history']),
    ('space',         ['space','nasa','satellite','orbit','planet','moon','asteroid','telescope','iss','rocket','astronomy','climate from space']),
    ('data',          ['data','statistics','dataset','index','measure','metric','indicator','benchmark','survey','poll','census data','estimate']),
]

# Section → guaranteed topics
SECTION_TOPICS = {
    'National Security':         ['war','military'],
    'Law Enforcement':           ['crime'],
    'Health':                    ['health'],
    'Income':                    ['economy','inequality'],
    'Housing':                   ['housing'],
    'Labor Force':               ['labor','economy'],
    'Education':                 ['education'],
    'Energy':                    ['energy'],
    'Agriculture':               ['food','agriculture'],
    'Transportation':            ['transportation'],
    'Population':                ['population'],
    'Elections':                 ['politics','democracy'],
    'Federal Government':        ['politics'],
    'State Government':          ['politics'],
    'Banking':                   ['finance'],
    'International Statistics':  ['international'],
    'Geography':                 ['climate','environment'],
    'Information':               ['media','technology'],
    'Arts Recreation':           [],
    'Prices':                    ['economy'],
    'Wholesale Retail':          ['economy'],
    'Social Insurance':          ['poverty','economy'],
}

def assign_topics(idea_line):
    """Assign topic tags to an idea based on section + keyword matching."""
    section_m = re.search(r',section:"([^"]+)"', idea_line)
    title_m   = re.search(r',title:"([^"]+)"', idea_line)
    sub_m     = re.search(r',sub:"([^"]+)"', idea_line)
    tags_m    = re.search(r',tags:"([^"]+)"', idea_line)

    section = section_m.group(1) if section_m else ''
    text = ' '.join(filter(None, [
        title_m.group(1) if title_m else '',
        sub_m.group(1)   if sub_m   else '',
        tags_m.group(1)  if tags_m  else '',
        section,
    ])).lower()

    topics = set(SECTION_TOPICS.get(section, []))

    for topic, keywords in TOPIC_RULES:
        for kw in keywords:
            if kw.lower() in text:
                topics.add(topic)
                break

    return sorted(topics)


# ── APPLY TO DATA.JS ──────────────────────────────────────────────────────────
with open(r'D:\projects\mapzimus-board\data.js','r',encoding='utf-8') as f:
    content = f.read()

lines = content.split('\n')
new_lines = []
added = 0
already = 0

for line in lines:
    if not (line.startswith(',{id:') or line.startswith('{id:')):
        new_lines.append(line)
        continue

    # Check if topics already exists
    if ',topics:[' in line:
        already += 1
        new_lines.append(line)
        continue

    topics = assign_topics(line)
    topics_str = ',topics:[' + ','.join('"%s"' % t for t in topics) + ']'

    # Insert before ,status: or ,notes: or ,tags:
    inserted = False
    for anchor in [',status:', ',notes:', ',tags:']:
        if anchor in line:
            line = line.replace(anchor, topics_str + anchor, 1)
            inserted = True
            break

    if not inserted:
        # Append before closing }
        line = line.rstrip()
        if line.endswith('}'):
            line = line[:-1] + topics_str + '}'

    added += 1
    new_lines.append(line)

with open(r'D:\projects\mapzimus-board\data.js','w',encoding='utf-8') as f:
    f.write('\n'.join(new_lines))

print('Done.')
print('  Topics added: %d' % added)
print('  Already had topics: %d' % already)

# Show distribution
from collections import Counter
topic_counter = Counter()
for line in new_lines:
    if not (line.startswith(',{id:') or line.startswith('{id:')): continue
    m = re.search(r',topics:\[([^\]]*)\]', line)
    if m:
        for t in re.findall(r'"([^"]+)"', m.group(1)):
            topic_counter[t] += 1

print('\nTopic distribution:')
for topic, count in sorted(topic_counter.items(), key=lambda x: -x[1]):
    print('  %-20s %d' % (topic, count))
