import re

with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the sparse hole: ,\n\n, -> single comma between the two ideas
before = len(re.findall(r',\s*,', content))
content = re.sub(r',(\s*),', r',\1', content)
after = len(re.findall(r',\s*,', content))
print(f'Double commas: {before} -> {after}')

with open('data.js', 'w', encoding='utf-8') as f:
    f.write(content)
print('data.js fixed')
