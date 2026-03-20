"""fix_consolidate.py
- Remove Section filter row from index.html
- Merge topic + section into single alphabetized Category row
- Remove activeSections / toggleSection / buildSectionRow from app.js
- Remove section filter logic from buildFiltered
- Bump cache v14 -> v15
"""
import re

BASE = r'D:\projects\mapzimus-board'

# ─── INDEX.HTML ────────────────────────────────────────────────────────────
with open(BASE + r'\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Remove the section-row div (dynamically built, just an empty shell in HTML)
html = re.sub(
    r'\s*<div class="filter-row" id="section-row">.*?</div>\s*',
    '\n    ',
    html, flags=re.DOTALL
)

# Replace topic filter row with alphabetized combined Category row
TOPICS_ALPHABETIZED = [
    ("agriculture","Agriculture"), ("climate","Climate"), ("crime","Crime"),
    ("data","Data"), ("democracy","Democracy"), ("drugs","Drugs"),
    ("economy","Economy"), ("education","Education"), ("energy","Energy"),
    ("environment","Environment"), ("finance","Finance"), ("food","Food"),
    ("gender","Gender"), ("guns","Guns"), ("health","Health"),
    ("history","History"), ("housing","Housing"), ("immigration","Immigration"),
    ("inequality","Inequality"), ("infrastructure","Infrastructure"),
    ("international","International"), ("labor","Labor"), ("media","Media"),
    ("military","Military"), ("politics","Politics"), ("population","Population"),
    ("poverty","Poverty"), ("race","Race"), ("religion","Religion"),
    ("space","Space"), ("technology","Technology"), ("trade","Trade"),
    ("transportation","Transportation"), ("war","War"),
]

buttons = '\n'.join(
    f'    <button class="fp topic" data-f="topics" data-v="{val}" onclick="toggleTopic(this)">{label}</button>'
    for val, label in TOPICS_ALPHABETIZED
)

new_topic_row = f'    <div class="filter-row" id="topic-row">\n      <span>Category:</span>\n{buttons}\n    </div>'

html = re.sub(
    r'<div class="filter-row" id="topic-row">.*?</div>',
    new_topic_row,
    html, flags=re.DOTALL
)

# Bump cache
html = html.replace('data.js?v=14', 'data.js?v=15')
html = html.replace('app.js?v=14', 'app.js?v=15')

with open(BASE + r'\index.html', 'w', encoding='utf-8') as f:
    f.write(html)

# ─── APP.JS ────────────────────────────────────────────────────────────────
with open(BASE + r'\app.js', 'r', encoding='utf-8') as f:
    app = f.read()

# Remove activeSections state line
app = app.replace(
    "let activeSections = new Set(); // multi-select section filter\n",
    ""
)

# Remove section filter block from buildFiltered
app = re.sub(
    r"\s*if \(activeSections\.size > 0\) \{.*?\}\n",
    "\n",
    app, flags=re.DOTALL
)

# Remove toggleSection function
app = re.sub(
    r"function toggleSection\(btn\) \{.*?\}\n",
    "",
    app, flags=re.DOTALL
)

# Remove buildSectionRow function
app = re.sub(
    r"//  SECTION ROW BUILD\nfunction buildSectionRow\(\) \{.*?\}\n",
    "",
    app, flags=re.DOTALL
)

# Remove buildSectionRow call from DOMContentLoaded
app = app.replace("  buildSectionRow();\n", "")

with open(BASE + r'\app.js', 'w', encoding='utf-8') as f:
    f.write(app)

# Verify
checks = {
    'section-row gone from HTML': 'id="section-row"' not in html,
    'Category label': '>Category:</span>' in html,
    'Agriculture first (alpha)': html.index('"agriculture"') < html.index('"war"'),
    'activeSections gone': 'activeSections' not in app,
    'toggleSection gone': 'function toggleSection' not in app,
    'buildSectionRow gone': 'function buildSectionRow' not in app,
    'v15 data.js': 'data.js?v=15' in html,
    'v15 app.js': 'app.js?v=15' in html,
    'topic filter still present': 'id="topic-row"' in html,
    'button count': str(html.count('toggleTopic')) + ' buttons',
}
for k, v in checks.items():
    print(f'  {"OK" if v is True else "BAD" if v is False else "  "} {k}: {v if not isinstance(v, bool) else ""}')

print('\nDone.')
