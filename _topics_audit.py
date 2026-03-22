"""Audit topics field across all entries - find empties and assess category coverage."""
import re, os
from collections import Counter

DATA = os.path.join(os.path.dirname(__file__), 'data.js')
with open(DATA, 'r', encoding='utf-8') as f:
    text = f.read()

empty_topics = []
has_topics = []
all_topics = Counter()
section_of_empty = Counter()

for line in text.split('\n'):
    line = line.strip().lstrip(',')
    if not line.startswith('{id:'):
        continue
    id_m = re.search(r'id:"([^"]*)"', line)
    eid = id_m.group(1) if id_m else '???'
    sect_m = re.search(r'section:"([^"]*)"', line)
    sect = sect_m.group(1) if sect_m else ''
    
    # Check topics
    topics_m = re.search(r'topics:\[([^\]]*)\]', line)
    if topics_m:
        content = topics_m.group(1).strip()
        if not content:
            empty_topics.append((eid, sect))
            section_of_empty[sect] += 1
        else:
            has_topics.append(eid)
            for t in re.findall(r'"([^"]*)"', content):
                all_topics[t] += 1
    else:
        empty_topics.append((eid, sect))
        section_of_empty[sect] += 1

total = len(empty_topics) + len(has_topics)
print(f"Total entries: {total}")
print(f"With topics: {len(has_topics)} ({100*len(has_topics)/total:.1f}%)")
print(f"Empty topics: {len(empty_topics)} ({100*len(empty_topics)/total:.1f}%)")

print(f"\n=== EXISTING TOPIC TAGS ({len(all_topics)} unique) ===")
for t, c in all_topics.most_common(50):
    print(f"  [{c:>4}x] {t}")

print(f"\n=== EMPTY TOPICS BY SECTION ===")
for s, c in section_of_empty.most_common():
    print(f"  [{c:>4}x] {s}")

# Show some sample empty-topic entries
print(f"\n=== SAMPLE ENTRIES WITH EMPTY TOPICS (first 20) ===")
for eid, sect in empty_topics[:20]:
    print(f"  {eid} (section: {sect})")
