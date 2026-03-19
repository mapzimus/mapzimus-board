import re
from collections import Counter
with open(r'D:\projects\mapzimus-board\data.js','r',encoding='utf-8') as f: content=f.read()
ids = re.findall(r'\{id:"([^"]+)"', content)
dupes = [(k,n) for k,n in Counter(ids).items() if n > 1]
print('Total ideas:', len(ids))
print('Actual dupes in file:', dupes if dupes else 'NONE')
