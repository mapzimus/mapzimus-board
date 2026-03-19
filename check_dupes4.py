import re
with open(r'D:\projects\mapzimus-board\data.js','r',encoding='utf-8') as f: content=f.read()

# Find ALL occurrences of this id pattern anywhere in file
target = 'nuclear_warheads_2025_map'
pattern = r'\{id:"%s"' % target
matches = list(re.finditer(pattern, content))
print('Pattern: %r' % pattern)
print('Occurrences: %d' % len(matches))
for m in matches:
    start = max(0, m.start()-5)
    end = min(len(content), m.end()+100)
    print('  at pos %d: %r' % (m.start(), content[start:end]))

print()
# Also check if it appears in tags
tag_matches = [i for i,c in enumerate(content) if content[i:i+len(target)] == target]
print('ALL raw occurrences of string anywhere: %d' % len(tag_matches))
for pos in tag_matches[:5]:
    print('  pos %d: %r' % (pos, content[max(0,pos-30):pos+60]))
