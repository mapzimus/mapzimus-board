import re
from collections import Counter

with open('data.js', encoding='utf-8') as f:
    content = f.read()

# Extract all topics arrays
all_topics_raw = re.findall(r'topics:\[([^\]]*)\]', content)
empty = sum(1 for t in all_topics_raw if t.strip() == '')
single = sum(1 for t in all_topics_raw if t.strip() and len(t.split(',')) == 1)
print(f"Total ideas: {len(all_topics_raw)}")
print(f"Empty topics []: {empty}")
print(f"Single topic: {single}")
print(f"2+ topics: {len(all_topics_raw) - empty - single}")

# Topic frequency
all_topics = []
for t in all_topics_raw:
    for x in re.findall(r'"([^"]+)"', t):
        all_topics.append(x)
print(f"\nTotal topic assignments: {len(all_topics)}")
print(f"\nTopic frequency:")
for k,n in Counter(all_topics).most_common():
    print(f"  {n:5d}  {k}")
