import re

# Fix app.js - remove the orphaned subtitle expression
with open('app.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove the commented-out line + the dangling backtick expression below it
before_len = len(content)
content = re.sub(
    r'// document\.getElementById\(.subl.\)\.textContent =\s*\n\s*`[^`]+`;',
    '',
    content
)
print(f'app.js: {before_len} -> {len(content)} chars (removed {before_len - len(content)} chars)')

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(content)
print('app.js fixed')
