import re

with open('data.js', encoding='utf-8') as f:
    content = f.read()

# Remove identity_signal from sc blocks
cleaned = re.sub(r',identity_signal:\d+', '', content)
removed = content.count('identity_signal:') - cleaned.count('identity_signal:')
print(f"Removed identity_signal from {removed} ideas")

with open('data.js', 'w', encoding='utf-8') as f:
    f.write(cleaned)

remaining = cleaned.count('identity_signal:')
print(f"Remaining identity_signal fields: {remaining}")
