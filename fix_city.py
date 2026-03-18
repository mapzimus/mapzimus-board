import re
with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()
content = re.sub(r'fmt:"City map[^"]+"', 'fmt:"City map"', content)
with open('data.js', 'w', encoding='utf-8') as f:
    f.write(content)
from collections import Counter
matches = re.findall(r'fmt:"([^"]+)"', content)
dist = Counter(matches)
for k,n in sorted(dist.items(), key=lambda x:-x[1]):
    print(n, k)
print('Total unique:', len(dist))
