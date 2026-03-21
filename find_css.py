import re
with open(r'D:\projects\mapzimus-board\index.html', 'r', encoding='utf-8') as f:
    content = f.read()
lines = content.split('\n')
for i, l in enumerate(lines):
    if '.vs' in l and ('{' in l or '}' in l):
        print(f"Line {i+1}: {l.strip()}")
    if '.vl' in l and ('{' in l or '}' in l):
        print(f"Line {i+1}: {l.strip()}")
print("Total lines:", len(lines))
# Find where to insert new CSS - look for .vl style
for i, l in enumerate(lines):
    if '.vl{' in l or '.vl {' in l:
        print(f"\n.vl found at line {i+1}: {l.strip()}")
        # Print surrounding context
        for j in range(max(0,i-2), min(len(lines), i+5)):
            print(f"  {j+1}: {lines[j].rstrip()}")
