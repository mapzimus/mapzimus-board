"""Audit all tbl field values in data.js to understand current state."""
import re, os
from collections import Counter

DATA = os.path.join(os.path.dirname(__file__), 'data.js')

with open(DATA, 'r', encoding='utf-8') as f:
    text = f.read()

tbls = []
entries_by_tbl = {}
for line in text.split('\n'):
    line = line.strip().lstrip(',')
    if not line.startswith('{id:'):
        continue
    tbl_m = re.search(r'tbl:"([^"]*)"', line)
    id_m = re.search(r'id:"([^"]*)"', line)
    eid = id_m.group(1) if id_m else '???'
    tbl = tbl_m.group(1) if tbl_m else ''
    tbls.append(tbl)
    if tbl not in entries_by_tbl:
        entries_by_tbl[tbl] = []
    entries_by_tbl[tbl].append(eid)

print(f"Total entries: {len(tbls)}")
print(f"Unique tbl values: {len(set(tbls))}")
print(f"Empty tbl values: {tbls.count('')}")

# Group by pattern
archive_tbls = [t for t in set(tbls) if 'archive' in t.lower()]
kaggle_tbls = [t for t in set(tbls) if 'kaggle' in t.lower()]
raw_data_tbls = [t for t in set(tbls) if 'raw_data' in t.lower() or 'D:' in t or 'F:' in t]

print(f"\n--- TBL values containing 'archive': {len(archive_tbls)} ---")
for t in sorted(archive_tbls)[:50]:
    print(f"  [{len(entries_by_tbl[t])} entries] {t}")

print(f"\n--- TBL values containing 'kaggle': {len(kaggle_tbls)} ---")
for t in sorted(kaggle_tbls)[:50]:
    print(f"  [{len(entries_by_tbl[t])} entries] {t}")

print(f"\n--- TBL values with local paths (raw_data/D:/F:): {len(raw_data_tbls)} ---")
for t in sorted(raw_data_tbls)[:80]:
    print(f"  [{len(entries_by_tbl[t])} entries] {t}")


# Show ALL unique tbl values sorted by frequency
print(f"\n--- ALL UNIQUE TBL VALUES (by frequency) ---")
freq = Counter(tbls)
for tbl, count in freq.most_common():
    print(f"  [{count:>4}x] {tbl}")
