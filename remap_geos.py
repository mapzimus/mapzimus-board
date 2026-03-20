"""
remap_geos.py
Smart geo reassignment for all 2096 ideas.
Rules:
- Keep existing value unless a more specific one clearly applies
- Only remap when title/sub/tags/section strongly indicate a specific geo
- Log all changes for review
"""
import re

with open('data.js', encoding='utf-8') as f:
    content = f.read()

lines = content.split('\n')

# Keyword rules: (keywords, new_geo, only_if_current_geo)
# only_if_current_geo: if set, only remap if current geo matches one of these
RULES = [
    # ── WORLD sub-regions ────────────────────────────────────────────────
    (['europe','european union',' eu ','eurozone','nato europe',
      'western europe','eastern europe','scandinavia','nordic countries',
      'france','germany','spain','italy','uk ','united kingdom','britain',
      'poland','ukraine','hungary','greece','netherlands','belgium',
      'portugal','sweden','norway','denmark','finland','austria','switzerland'],
     'europe', ['worldwide']),

    (['latin america','south america','central america','caribbean',
      'brazil','mexico','colombia','argentina','chile','peru','venezuela',
      'cuba','haiti','dominican','guatemala','ecuador','bolivia'],
     'latin_america', ['worldwide']),

    (['sub-saharan africa','west africa','east africa','north africa',
      'nigeria','ethiopia','kenya','ghana','south africa','egypt',
      'congo','tanzania','uganda','senegal','ivory coast','cameroon',
      'africa ','african '],
     'africa', ['worldwide']),

    (['middle east','saudi arabia','iran','iraq','israel','palestine',
      'turkey','egypt','jordan','syria','lebanon','yemen','oman',
      'uae','qatar','kuwait','bahrain','gulf '],
     'middle_east', ['worldwide']),

    (['southeast asia','south asia','east asia','india ','china ',
      'japan ','south korea','north korea','indonesia','philippines',
      'vietnam','thailand','malaysia','bangladesh','pakistan',
      'myanmar','cambodia','taiwan','hong kong','singapore'],
     'asia', ['worldwide']),

    (['oceania','australia','new zealand','pacific islands',
      'papua new guinea','fiji','samoa','tonga'],
     'oceania', ['worldwide']),

    (['canada','north america','mexico ','nafta','usmca'],
     'north_america', ['worldwide']),

    # ── Global Cities ─────────────────────────────────────────────────────
    (['global cit','world cit','cities worldwide','cities across countries',
      'cities around the world','international cit','top cities globally',
      'city comparison across','city comparison world'],
     'global_city', ['worldwide']),

    # ── US Regional ──────────────────────────────────────────────────────
    (['new england','connecticut','maine ','vermont ','rhode island',
      'massachusetts','new hampshire','boston ','providence','hartford',
      'burlington vt','portland me'],
     'us_new_england', ['us_state','us_national','us_city','us_metro']),

    (['northeast ','mid-atlantic','new york ','new jersey','pennsylvania',
      'philadelphia','pittsburgh','newark ','albany'],
     'us_northeast', ['us_state','us_national','us_city','us_metro']),

    (['appalachia','appalachian','coal country','rust belt','bible belt',
      'deep south','sun belt','great plains','the south ','southern states',
      'midwest ','midwestern','great lakes'],
     None, None),  # too ambiguous — skip

    # ── US Cities list (top-N comparison) ────────────────────────────────
    (['top 10 cit','top 20 cit','top 50 cit','us cities ranked',
      'american cities ranked','cities in america','major us cities',
      'largest us cities','most expensive cities','cheapest cities',
      'best cities','worst cities','us city comparison'],
     'us_cities', ['us_national','us_city']),

    # ── MA specific ───────────────────────────────────────────────────────
    (['massachusetts ','massgis','mass. ','in massachusetts',
      'of massachusetts','ma towns','ma cities','boston neighborhoods',
      'boston commute','mbta','in boston'],
     'us_ma', ['us_state','us_city','us_metro','us_national','us_new_england','us_northeast']),

    # ── NH specific ───────────────────────────────────────────────────────
    (['new hampshire ','nhgranit','nh towns','nh cities',
      'in new hampshire','of new hampshire','nh granit'],
     'us_nh', ['us_state','us_city','us_metro','us_national','us_new_england','us_northeast']),

    # ── US Timezones nationwide ────────────────────────────────────────────
    (['time zone','timezone','daylight saving','eastern time','central time',
      'mountain time','pacific time','clock change','dst '],
     'us_tz', ['us_national','us_state']),
]

changes = []
new_lines = []

for line in lines:
    if not (line.startswith('{id:') or line.startswith(',{id:')):
        new_lines.append(line)
        continue

    id_m    = re.search(r'id:"([^"]+)"', line)
    title_m = re.search(r'title:"([^"]*)"', line)
    sub_m   = re.search(r'sub:"([^"]*)"', line)
    tags_m  = re.search(r'tags:"([^"]*)"', line)
    geo_m   = re.search(r'geo:"([^"]+)"', line)

    if not geo_m:
        new_lines.append(line)
        continue

    current_geo = geo_m.group(1)
    haystack = ' '.join([
        title_m.group(1) if title_m else '',
        sub_m.group(1)   if sub_m   else '',
        tags_m.group(1)  if tags_m  else '',
    ]).lower()

    new_geo = None
    matched_rule = None

    for keywords, target_geo, only_if in RULES:
        if target_geo is None:
            continue
        if only_if and current_geo not in only_if:
            continue
        if any(kw in haystack for kw in keywords):
            new_geo = target_geo
            matched_rule = keywords[0]
            break

    if new_geo and new_geo != current_geo:
        idea_id = id_m.group(1) if id_m else '?'
        title   = title_m.group(1)[:60] if title_m else '?'
        changes.append((idea_id, current_geo, new_geo, title, matched_rule))
        line = line.replace(f'geo:"{current_geo}"', f'geo:"{new_geo}"')

    new_lines.append(line)

print(f"Total changes: {len(changes)}")
print()
for idea_id, old, new, title, rule in changes:
    print(f"  {old:20s} -> {new:20s}  [{rule}]")
    print(f"    {title}")

new_content = '\n'.join(new_lines)
with open('data.js', 'w', encoding='utf-8') as f:
    f.write(new_content)

# Final counts
geos = re.findall(r'geo:"([^"]+)"', new_content)
from collections import Counter
print(f"\nFinal geo distribution:")
for k,n in Counter(geos).most_common():
    print(f"  {n:5d}  {k}")
