import re

path = r'D:\projects\mapzimus-board\app.js'
with open(path, 'r', encoding='utf-8') as f:
    js = f.read()

# Remove the orphaned fragment left by toggleSection regex removal
js = js.replace('}\nfunction toggleTopic(btn) {', 'function toggleTopic(btn) {')

# Also clean up the orphaned closing lines after toggleTopic
# Pattern: the end of toggleTopic then stray "  renderBrowse();\n}\n"
js = re.sub(
    r'(  renderBrowse\(\);\n\})\n  renderBrowse\(\);\n\}\n(function setSort)',
    r'\1\n\2',
    js
)

with open(path, 'w', encoding='utf-8') as f:
    f.write(js)
print('Fixed.')
