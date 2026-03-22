"""Compact tbl audit - just the key stats."""
import re, os
from collections import Counter

DATA = os.path.join(os.path.dirname(__file__), 'data.js')
with open(DATA, 'r', encoding='utf-8') as f:
    text = f.read()

tbls = []
for line in text.split('\n'):
    line = line.strip().lstrip(',')
    if not line.startswith('{id:'):
        continue
    m = re.search(r'tbl:"([^"]*)"', line)
    tbls.append(m.group(1) if m else '')

freq = Counter(tbls)
print(f"Total: {len(tbls)}, Unique tbl: {len(freq)}, Empty: {freq['']}")

# Categorize
local_path = [t for t in freq if ('/' in t or '\\' in t) and t]
url_based = [t for t in freq if t.startswith('http')]
plain_text = [t for t in freq if t and '/' not in t and '\\' not in t and not t.startswith('http')]

print(f"\nLocal paths: {len(local_path)} unique ({sum(freq[t] for t in local_path)} entries)")
print(f"URLs: {len(url_based)} unique ({sum(freq[t] for t in url_based)} entries)")
print(f"Plain text: {len(plain_text)} unique ({sum(freq[t] for t in plain_text)} entries)")

# Top 40 most common
print(f"\nTop 40 tbl values:")
for tbl, count in freq.most_common(40):
    label = tbl if len(tbl) < 100 else tbl[:97]+'...'
    print(f"  [{count:>4}x] {label}")

# Show some examples of each category
print(f"\n--- Sample local paths (first 30) ---")
for t in sorted(local_path)[:30]:
    print(f"  [{freq[t]:>3}x] {t[:120]}")

print(f"\n--- Sample plain text refs (first 30) ---")
for t in sorted(plain_text)[:30]:
    print(f"  [{freq[t]:>3}x] {t[:120]}")
