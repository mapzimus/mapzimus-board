import re
with open('data.js','r',encoding='utf-8') as f:
    c = f.read()
ids = re.findall(r'\{id:"([^"]+)"', c)
from collections import Counter
dupes = [k for k,n in Counter(ids).items() if n>1]
print('Total ideas:', len(ids), '| Dupes:', dupes or 'none')

# Check for double commas (sparse holes)
doubles = re.findall(r',\s*,', c)
print('Double commas:', len(doubles))

# Verify end marker
end_markers = len(re.findall(r'\];\s*//\s*end D', c))
print('End markers:', end_markers)

# Check file ends cleanly
print('Last 60 chars:', repr(c[-60:]))
