with open(r'D:\projects\mapzimus-board\app.js','r',encoding='utf-8') as f: c=f.read()

# 1. Add activeTopics to state block
c = c.replace(
    "const activeFilters = { type: null, geo: null, fmt: null, status: null, notes: null };",
    "const activeFilters = { type: null, geo: null, fmt: null, status: null, notes: null };\nlet activeTopics = new Set(); // multi-select, OR logic"
)

# 2. Add toggleTopic() function after togglePill()
toggle_topic_fn = """
function toggleTopic(btn) {
  const val = btn.dataset.v;
  if (activeTopics.has(val)) {
    activeTopics.delete(val);
    btn.classList.remove('on');
  } else {
    activeTopics.add(val);
    btn.classList.add('on');
  }
  renderBrowse();
}
"""
c = c.replace(
    "function setSort(btn) {",
    toggle_topic_fn + "function setSort(btn) {"
)

# 3. Update buildFiltered() to handle topics
c = c.replace(
    "    if (activeFilters.notes === 'has'  && !d.notes) return false;\n    if (activeFilters.notes === 'none' && d.notes)  return false;",
    "    if (activeFilters.notes === 'has'  && !d.notes) return false;\n    if (activeFilters.notes === 'none' && d.notes)  return false;\n    if (activeTopics.size > 0) {\n      const dTopics = d.topics || [];\n      if (!dTopics.some(t => activeTopics.has(t))) return false;\n    }"
)

# 4. Bump app.js version comment
c = c.replace(
    "// app.js - Mapzimus board logic v5",
    "// app.js - Mapzimus board logic v6"
)

with open(r'D:\projects\mapzimus-board\app.js','w',encoding='utf-8') as f: f.write(c)
print('app.js patched')

# Verify the patches landed
checks = ['activeTopics', 'toggleTopic', 'activeTopics.size']
for ch in checks:
    print('  %s: %s' % (ch, 'OK' if ch in c else 'MISSING'))
