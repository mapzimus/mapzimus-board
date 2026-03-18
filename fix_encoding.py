"""fix_encoding.py — fix BOM, double-encoded chars, missing closing bracket"""
import re

with open('data.js', 'rb') as f:
    raw_bytes = f.read()

# Decode — file is UTF-8 but may have BOM
if raw_bytes[:3] == b'\xef\xbb\xbf':
    raw_bytes = raw_bytes[3:]
    print('Stripped BOM')

text = raw_bytes.decode('utf-8')

# Fix double-encoded em dash: â€" -> —
text = text.replace('\u00e2\u0080\u0094', '\u2014')  # â€" -> —
text = text.replace('\u00e2\u0080\u0093', '\u2013')  # â€" -> –
text = text.replace('â€"', '\u2014')
text = text.replace('â€™', "'")
text = text.replace('Ã©', 'é')

# Fix comment headers — replace Ä garbage with plain ASCII
text = re.sub(r'//\s*[Ä─\-]+\s*([^Ä─\n]+?)\s*[Ä─\-]+', r'// \1', text)
text = re.sub(r'[Ä]+', '-', text)  # remaining Ä -> dash

# Fix corrupted table references: ú -> ·  (was em dash)
text = text.replace(' ú ', ' · ')

# Ensure closing bracket exists
trimmed = text.rstrip()
if not trimmed.endswith(']; // end D'):
    text = trimmed + '\n]; // end D\n'
    print('Added closing bracket')
else:
    print('Closing bracket already present')

# Write back as UTF-8 without BOM
with open('data.js', 'w', encoding='utf-8') as f:
    f.write(text)

lines = text.split('\n')
print(f'Done. Lines: {len(lines)}')

# Quick sanity check — count ideas
idea_count = len(re.findall(r',?\{id:', text))
print(f'Ideas found: {idea_count}')
