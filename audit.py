import re
from collections import Counter
c = open('data.js', encoding='utf-8').read()
fmts = re.findall(r'fmt:"([^"]+)"', c)
geos = re.findall(r'geo:"([^"]+)"', c)
print('FMTS:')
for k,n in Counter(fmts).most_common(): print(f'  {n:4d}  {k}')
print('GEOS:')
for k,n in Counter(geos).most_common(): print(f'  {n:4d}  {k}')
