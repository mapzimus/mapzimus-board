import re

with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Clear all notes fields - set to empty string
original = content
content = re.sub(r',notes:"[^"]*"', ',notes:""', content)

changed = original.count(',notes:"') - content.count(',notes:""')
# Count non-empty notes that were cleared
non_empty = len(re.findall(r',notes:""', content))
print(f'Notes cleared. Total notes fields: {non_empty}')

with open('data.js', 'w', encoding='utf-8') as f:
    f.write(content)

print('Done.')
