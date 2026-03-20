"""fix_ui.py - Comprehensive UI overhaul:
  - Fix all broken emoji/chars in index.html
  - Add topic badges on each card (from d.topics[])
  - Add section filter row (clickable, colored, multi-select)
  - Add TOPIC_COLORS map to app.js
  - Fix status menu dots
  - getSectionColor helper (fuzzy match)
  - Bump cache v13 -> v14
"""
import re

BASE = r'D:\projects\mapzimus-board'

# ─── APP.JS ────────────────────────────────────────────────────────────────
with open(BASE + r'\app.js', 'r', encoding='utf-8') as f:
    app = f.read()

# 1. Add TOPIC_COLORS right after LS_KEY
TOPIC_COLORS_BLOCK = """
const TOPIC_COLORS = {
  health:'#ef4444', economy:'#22c55e', politics:'#3b82f6',
  crime:'#dc2626', poverty:'#f59e0b', housing:'#f97316',
  education:'#14b8a6', labor:'#a855f7', race:'#ec4899',
  gender:'#e879f9', immigration:'#0ea5e9', war:'#b91c1c',
  military:'#6366f1', energy:'#eab308', climate:'#10b981',
  environment:'#16a34a', food:'#84cc16', agriculture:'#65a30d',
  drugs:'#9333ea', guns:'#991b1b', finance:'#d97706',
  trade:'#0891b2', inequality:'#e11d48', transportation:'#06b6d4',
  infrastructure:'#64748b', technology:'#8b5cf6', media:'#0ea5e9',
  population:'#ec4899', international:'#8b5cf6', democracy:'#3b82f6',
  religion:'#b45309', history:'#78716c', space:'#1d4ed8', data:'#475569',
};"""
app = app.replace(
    "const LS_KEY = 'mapzimus_overrides';",
    "const LS_KEY = 'mapzimus_overrides';" + TOPIC_COLORS_BLOCK
)

# 2. Fix STATUSES - remove emoji field
app = app.replace(
    "  { val: 'idea',        color: '#6b7280', emoji: '', label: 'Idea' },",
    "  { val: 'idea',        color: '#6b7280', label: 'Idea' },"
)
app = app.replace(
    "  { val: 'in-progress', color: '#f59e0b', emoji: '', label: 'In Progress' },",
    "  { val: 'in-progress', color: '#f59e0b', label: 'In Progress' },"
)
app = app.replace(
    "  { val: 'built',       color: '#22c55e', emoji: '', label: 'Built' },",
    "  { val: 'built',       color: '#22c55e', label: 'Built' },"
)
app = app.replace(
    "  { val: 'published',   color: '#3b82f6', emoji: '', label: 'Published' },",
    "  { val: 'published',   color: '#3b82f6', label: 'Published' },"
)

# 3. Expand SECTION_COLORS with more categories
OLD_SC = """const SECTION_COLORS = {
  'Health':'#ef4444','Elections':'#3b82f6','Income':'#22c55e','Housing':'#f59e0b',
  'Labor Force':'#a855f7','Law Enforcement':'#dc2626','Education':'#14b8a6',
  'Energy':'#f97316','Agriculture':'#84cc16','Transportation':'#06b6d4',
  'Population':'#ec4899','National Security':'#6366f1','International Statistics':'#8b5cf6',
  'Geography':'#10b981','Banking':'#f59e0b','Information':'#0ea5e9',
  'State Government':'#64748b','Federal Government':'#475569',
};"""
NEW_SC = """const SECTION_COLORS = {
  'Health':'#ef4444','Elections':'#3b82f6','Income':'#22c55e','Housing':'#f59e0b',
  'Labor Force':'#a855f7','Law Enforcement':'#dc2626','Education':'#14b8a6',
  'Energy':'#f97316','Agriculture':'#84cc16','Transportation':'#06b6d4',
  'Population':'#ec4899','National Security':'#6366f1','International Statistics':'#8b5cf6',
  'Geography':'#10b981','Banking':'#f59e0b','Information':'#0ea5e9',
  'State Government':'#64748b','Federal Government':'#475569',
  'Prices':'#d97706','Births Deaths':'#ec4899','Arts Recreation':'#14b8a6',
  'Business Enterprise':'#6366f1','Foreign Commerce':'#0891b2','Social Insurance':'#84cc16',
  'Wholesale and Retail Trade':'#f97316','Accommodation Food Services':'#8b5cf6',
  'Forestry Fishing':'#16a34a','Income Expenditures':'#22c55e',
};"""
app = app.replace(OLD_SC, NEW_SC)

# 4. Add activeSections to state block
app = app.replace(
    "let activeTopics = new Set(); // multi-select, OR logic",
    "let activeTopics = new Set(); // multi-select, OR logic\nlet activeSections = new Set(); // multi-select section filter"
)

# 5. Fix status menu - swap emoji span for sdot
app = app.replace(
    '      <span style="color:${s.color}">${s.emoji}</span> ${s.label}',
    '      <span class="sdot" style="background:${s.color}"></span>${s.label}'
)

# 6. Replace secColor line and add topic badges block
OLD_SEC = "  const secColor = SECTION_COLORS[d.section] || '#6b7280';\n\n  // Status dropdown options"
NEW_SEC = """  const secColor = getSectionColor(d.section);

  // Topic badges from d.topics[]
  const topicBadges = (d.topics || []).map(t => {
    const c = TOPIC_COLORS[t] || '#6b7280';
    return `<span class="topic-badge" style="background:${c}22;color:${c};border:1px solid ${c}44">${t}</span>`;
  }).join('');

  // Status dropdown options"""
app = app.replace(OLD_SEC, NEW_SEC)

# 7. Add getSectionColor helper before cardHTML
app = app.replace(
    "//  CARD HTML \nfunction cardHTML(d, highlight = false) {",
    """//  SECTION COLOR HELPER
function getSectionColor(section) {
  if (!section) return '#6b7280';
  const entries = Object.entries(SECTION_COLORS).sort((a,b) => b[0].length - a[0].length);
  for (const [key, color] of entries) {
    if (section.includes(key)) return color;
  }
  return '#6b7280';
}

//  CARD HTML
function cardHTML(d, highlight = false) {"""
)

# 8. Replace card-header HTML to wrap badges in badge-row div
OLD_HDR = """      <div class="card-header">
        <div class="status-wrap">
          <span class="status-dot" style="background:${st.color}" data-id="${d.id}" title="Click to change status - ${st.label}"></span>
          <div class="status-menu" id="sm-${d.id}">
            ${statusOptions}
          </div>
        </div>
        <span class="sect-badge" style="background:${secColor}22;color:${secColor};border:1px solid ${secColor}44">${d.section}</span>
      </div>"""
NEW_HDR = """      <div class="card-header">
        <div class="status-wrap">
          <span class="status-dot" style="background:${st.color}" data-id="${d.id}" title="Click to change status - ${st.label}"></span>
          <div class="status-menu" id="sm-${d.id}">
            ${statusOptions}
          </div>
        </div>
        <div class="badge-row">
          <span class="sect-badge" style="background:${secColor}22;color:${secColor};border:1px solid ${secColor}44">${d.section}</span>
          ${topicBadges}
        </div>
      </div>"""
app = app.replace(OLD_HDR, NEW_HDR)

# 9. Add section filtering to buildFiltered
OLD_TOPICS_FILTER = """    if (activeTopics.size > 0) {
      const dTopics = d.topics || [];
      if (!dTopics.some(t => activeTopics.has(t))) return false;
    }"""
NEW_TOPICS_FILTER = """    if (activeTopics.size > 0) {
      const dTopics = d.topics || [];
      if (!dTopics.some(t => activeTopics.has(t))) return false;
    }
    if (activeSections.size > 0) {
      const sec = d.section || '';
      if (![...activeSections].some(s => sec.includes(s))) return false;
    }"""
app = app.replace(OLD_TOPICS_FILTER, NEW_TOPICS_FILTER)

# 10. Add toggleSection after toggleTopic
app = app.replace(
    "function setSort(btn) {",
    """function toggleSection(btn) {
  const val = btn.dataset.v;
  const c = SECTION_COLORS[val] || '#6b7280';
  if (activeSections.has(val)) {
    activeSections.delete(val);
    btn.classList.remove('on');
    btn.style.background = '';
    btn.style.color = '';
    btn.style.borderColor = '';
  } else {
    activeSections.add(val);
    btn.classList.add('on');
    btn.style.background = c + '22';
    btn.style.color = c;
    btn.style.borderColor = c + '88';
  }
  renderBrowse();
}
function setSort(btn) {"""
)

# 11. Add buildSectionRow before INIT
app = app.replace(
    "//  INIT \nrenderBrowse();",
    """//  SECTION ROW BUILD
function buildSectionRow() {
  const row = document.getElementById('section-row');
  if (!row || row.dataset.built) return;
  row.dataset.built = '1';
  Object.entries(SECTION_COLORS).forEach(([s, c]) => {
    const btn = document.createElement('button');
    btn.className = 'fp sec';
    btn.dataset.v = s;
    btn.textContent = s;
    btn.onclick = () => toggleSection(btn);
    row.appendChild(btn);
  });
}

//  INIT
renderBrowse();"""
)

# 12. Call buildSectionRow on DOMContentLoaded
app = app.replace(
    "  updateOverrideCount();\n});",
    "  updateOverrideCount();\n  buildSectionRow();\n});"
)

with open(BASE + r'\app.js', 'w', encoding='utf-8') as f:
    f.write(app)

checks = {
    'TOPIC_COLORS': 'TOPIC_COLORS' in app,
    'getSectionColor': 'getSectionColor' in app,
    'topicBadges': 'topicBadges' in app,
    'activeSections': 'activeSections' in app,
    'toggleSection': 'toggleSection' in app,
    'buildSectionRow': 'buildSectionRow' in app,
    'badge-row': 'badge-row' in app,
    'sdot in menu': 'class="sdot"' in app,
    'section filter in buildFiltered': 'activeSections.size' in app,
}
print('app.js:')
for k,v in checks.items():
    print(f'  {"OK" if v else "MISSING"} {k}')

# ─── INDEX.HTML ────────────────────────────────────────────────────────────
with open(BASE + r'\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 13. Fix broken chars - read as bytes first to see exact encoding
# Export button - broken downward arrow
html = re.sub(r'[^\x00-\x7F]+Export edits', 'Export edits', html)

# Search placeholder - broken ellipsis
html = html.replace('immigration\u00e2\u20ac\u00a6', 'immigration...')
# Catch variant
html = re.sub(r'immigration[^\x00-\x7F]+\.\.\.|immigration[^\x00-\x7F]+(?=&quot;|")', 'immigration...', html)

# Fix correlate select placeholder - broken em dashes
html = re.sub(r'[^\x00-\x7F]+ select a variable [^\x00-\x7F]+', '- select a variable -', html)

# Fix CSS data-ext content em dash
html = re.sub(r"content: '[^\x00-\x7F]+'", "content: '-'", html)

# Fix CSS comment box-drawing chars (cosmetic only)
html = re.sub(r'/\* [^\x00-\x7F]+CARDS[^\x00-\x7F]+ \*/', '/* CARDS */', html)

# 14. Fix Status filter buttons - replace broken emoji with sdot spans
html = re.sub(
    r'onclick="togglePill\(this\)">[^\x00-\x7F]+\s*Ideas</button>',
    'onclick="togglePill(this)"><span class="sdot" style="background:#6b7280"></span>Ideas</button>',
    html
)
html = re.sub(
    r'onclick="togglePill\(this\)">[^\x00-\x7F]+\s*In progress</button>',
    'onclick="togglePill(this)"><span class="sdot" style="background:#f59e0b"></span>In Progress</button>',
    html
)
html = re.sub(
    r'onclick="togglePill\(this\)">[^\x00-\x7F]+\s*Built</button>',
    'onclick="togglePill(this)"><span class="sdot" style="background:#22c55e"></span>Built</button>',
    html
)
html = re.sub(
    r'onclick="togglePill\(this\)">[^\x00-\x7F]+\s*Published</button>',
    'onclick="togglePill(this)"><span class="sdot" style="background:#3b82f6"></span>Published</button>',
    html
)

# 15. Add section filter row before topic-row
html = html.replace(
    '    <div class="filter-row" id="topic-row">',
    '    <div class="filter-row" id="section-row">\n      <span>Section:</span>\n    </div>\n    <div class="filter-row" id="topic-row">'
)

# 16. Add new CSS before </style>
NEW_CSS = """
  /* Status dot (menu + filter bar) */
  .sdot { display:inline-block; width:8px; height:8px; border-radius:50%; margin-right:5px; vertical-align:middle; flex-shrink:0; }

  /* Badge row on cards - section + topic tags */
  .badge-row { display:flex; flex-wrap:wrap; gap:4px; align-items:center; flex:1; min-width:0; }
  .topic-badge { font-size:9px; padding:1px 6px; border-radius:20px; font-weight:500; white-space:nowrap; }

  /* Section filter buttons */
  .fp.sec { font-size:10px; }

"""
html = html.replace('</style>', NEW_CSS + '</style>')

# 17. Bump cache version v13 -> v14
html = html.replace('data.js?v=13', 'data.js?v=14')
html = html.replace('app.js?v=13', 'app.js?v=14')

with open(BASE + r'\index.html', 'w', encoding='utf-8') as f:
    f.write(html)

html_checks = {
    'section-row div': 'id="section-row"' in html,
    'sdot CSS': '.sdot' in html,
    'badge-row CSS': '.badge-row' in html,
    'topic-badge CSS': '.topic-badge' in html,
    'status dot fixed': '<span class="sdot" style="background:#6b7280">' in html,
    'v14 data.js': 'data.js?v=14' in html,
    'v14 app.js': 'app.js?v=14' in html,
    'no broken status emoji': 'st-idea' in html,
}
print('index.html:')
for k,v in html_checks.items():
    print(f'  {"OK" if v else "MISSING"} {k}')

# Verify no double section-row
sec_count = html.count('id="section-row"')
print(f'  section-row count: {sec_count} (should be 1)')
print('\nDone. Run: python maintain.py then git add/commit/push')
