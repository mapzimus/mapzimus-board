import re, pathlib

app = pathlib.Path('app.js').read_text(encoding='utf-8')

# Find the TOPICS or canonical filter list
# Look for any array of strings that looks like section/category names
# Dump lines around "section" references
lines = app.splitlines()
for i, ln in enumerate(lines):
    if 'section' in ln.lower() and ('filter' in ln.lower() or 'SECTION' in ln or 'badge' in ln.lower() or 'pill' in ln.lower()):
        print(f'{i+1}: {ln[:200]}')
