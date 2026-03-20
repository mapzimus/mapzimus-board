import re
from collections import Counter

with open('data.js', encoding='utf-8') as f:
    content = f.read()

ideas = []
for m in re.finditer(r'\{id:"([^"]+)".*?vs:(\d+).*?data_ready:(\d+)', content):
    ideas.append({'id': m.group(1), 'vs': int(m.group(2)), 'dr': int(m.group(3))})

ideas.sort(key=lambda x: -x['vs'])
print(f"Total ideas: {len(ideas)}")
print(f"\nTop 15:")
for i in ideas[:15]:
    print(f"  vs={i['vs']}  dr={i['dr']}  {i['id']}")

print(f"\nVS distribution:")
buckets = Counter(i['vs']//10*10 for i in ideas)
for k in sorted(buckets.keys(), reverse=True):
    print(f"  {k}-{k+9}: {buckets[k]}")
