import re

# Fix 1: Replace middot (U+00B7) in data.js tbl/section fields with plain " - "
with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()

before = content.count('\u00b7')
# Replace middot only inside field values (between quotes)
content = content.replace('\u00b7', ' - ')
# Also replace km2 superscript
content = content.replace('\u00b2', '2')
after_b = content.count('\u00b7')

with open('data.js', 'w', encoding='utf-8') as f:
    f.write(content)
print(f'data.js: replaced {before} middot chars, {before - after_b} removed')

# Fix 2: In app.js, replace the middot join separator with plain " | "
with open('app.js', 'r', encoding='utf-8') as f:
    app = f.read()

app_before = app.count('\u00b7')
app = app.replace('\u00b7', ' | ')
with open('app.js', 'w', encoding='utf-8') as f:
    f.write(app)
print(f'app.js: replaced {app_before} middot chars')
