with open(r'D:\projects\mapzimus-board\index.html','r',encoding='utf-8') as f: c=f.read()

# 1. Add topic pill CSS after the .fp.nt.on rule
css_insert = """  .fp.nt.on             { background: var(--surface2); color: var(--text); border-color: var(--text3); }
  .fp.topic.on          { background: #1e293b; color: #7dd3fc; border-color: #38bdf8; font-weight: 600; }"""
c = c.replace(
    '  .fp.nt.on             { background: var(--surface2); color: var(--text); border-color: var(--text3); }',
    css_insert
)

# 2. Add topic filter row before the sort row, after the Notes row
topic_row = """  <div class="filter-row">
    <span>Notes:</span>
    <button class="fp nt" data-f="notes" data-v="has"  onclick="togglePill(this)">Has notes</button>
    <button class="fp nt" data-f="notes" data-v="none" onclick="togglePill(this)">No notes</button>
  </div>
  <div class="filter-row" id="topic-row">
    <span>Topic:</span>
    <button class="fp topic" data-f="topics" data-v="health"         onclick="toggleTopic(this)">🏥 Health</button>
    <button class="fp topic" data-f="topics" data-v="economy"        onclick="toggleTopic(this)">💰 Economy</button>
    <button class="fp topic" data-f="topics" data-v="politics"       onclick="toggleTopic(this)">🗳️ Politics</button>
    <button class="fp topic" data-f="topics" data-v="crime"          onclick="toggleTopic(this)">🔒 Crime</button>
    <button class="fp topic" data-f="topics" data-v="poverty"        onclick="toggleTopic(this)">📉 Poverty</button>
    <button class="fp topic" data-f="topics" data-v="housing"        onclick="toggleTopic(this)">🏠 Housing</button>
    <button class="fp topic" data-f="topics" data-v="education"      onclick="toggleTopic(this)">📚 Education</button>
    <button class="fp topic" data-f="topics" data-v="labor"          onclick="toggleTopic(this)">👷 Labor</button>
    <button class="fp topic" data-f="topics" data-v="race"           onclick="toggleTopic(this)">✊ Race</button>
    <button class="fp topic" data-f="topics" data-v="gender"         onclick="toggleTopic(this)">⚧️ Gender</button>
    <button class="fp topic" data-f="topics" data-v="immigration"    onclick="toggleTopic(this)">🌐 Immigration</button>
    <button class="fp topic" data-f="topics" data-v="war"            onclick="toggleTopic(this)">⚔️ War</button>
    <button class="fp topic" data-f="topics" data-v="military"       onclick="toggleTopic(this)">🎖️ Military</button>
    <button class="fp topic" data-f="topics" data-v="energy"         onclick="toggleTopic(this)">⚡ Energy</button>
    <button class="fp topic" data-f="topics" data-v="climate"        onclick="toggleTopic(this)">🌡️ Climate</button>
    <button class="fp topic" data-f="topics" data-v="environment"    onclick="toggleTopic(this)">🌿 Environment</button>
    <button class="fp topic" data-f="topics" data-v="food"           onclick="toggleTopic(this)">🌽 Food</button>
    <button class="fp topic" data-f="topics" data-v="agriculture"    onclick="toggleTopic(this)">🚜 Agriculture</button>
    <button class="fp topic" data-f="topics" data-v="drugs"          onclick="toggleTopic(this)">💊 Drugs</button>
    <button class="fp topic" data-f="topics" data-v="guns"           onclick="toggleTopic(this)">🔫 Guns</button>
    <button class="fp topic" data-f="topics" data-v="finance"        onclick="toggleTopic(this)">🏦 Finance</button>
    <button class="fp topic" data-f="topics" data-v="trade"          onclick="toggleTopic(this)">📦 Trade</button>
    <button class="fp topic" data-f="topics" data-v="inequality"     onclick="toggleTopic(this)">⚖️ Inequality</button>
    <button class="fp topic" data-f="topics" data-v="transportation" onclick="toggleTopic(this)">🚗 Transportation</button>
    <button class="fp topic" data-f="topics" data-v="infrastructure" onclick="toggleTopic(this)">🌉 Infrastructure</button>
    <button class="fp topic" data-f="topics" data-v="technology"     onclick="toggleTopic(this)">💻 Technology</button>
    <button class="fp topic" data-f="topics" data-v="media"          onclick="toggleTopic(this)">📺 Media</button>
    <button class="fp topic" data-f="topics" data-v="population"     onclick="toggleTopic(this)">👥 Population</button>
    <button class="fp topic" data-f="topics" data-v="international"  onclick="toggleTopic(this)">🌍 International</button>
    <button class="fp topic" data-f="topics" data-v="democracy"      onclick="toggleTopic(this)">🗽 Democracy</button>
    <button class="fp topic" data-f="topics" data-v="religion"       onclick="toggleTopic(this)">⛪ Religion</button>
    <button class="fp topic" data-f="topics" data-v="history"        onclick="toggleTopic(this)">📜 History</button>
    <button class="fp topic" data-f="topics" data-v="space"          onclick="toggleTopic(this)">🚀 Space</button>
    <button class="fp topic" data-f="topics" data-v="data"           onclick="toggleTopic(this)">📊 Data</button>
  </div>"""

c = c.replace(
    '  <div class="filter-row">\n    <span>Notes:</span>\n    <button class="fp nt" data-f="notes" data-v="has"  onclick="togglePill(this)">Has notes</button>\n    <button class="fp nt" data-f="notes" data-v="none" onclick="togglePill(this)">No notes</button>\n  </div>',
    topic_row
)

# 3. Bump cache version
c = c.replace('data.js?v=11', 'data.js?v=12')
c = c.replace('app.js?v=11', 'app.js?v=12')

with open(r'D:\projects\mapzimus-board\index.html','w',encoding='utf-8') as f: f.write(c)
print('index.html updated, length:', len(c.split('\n')), 'lines')
