with open(r'D:\projects\mapzimus-board\maintain.py', 'r', encoding='utf-8') as f:
    c = f.read()

bad  = "if line.endswith('}'): line = line[:-1] + ',status:\"idea\"}\\'"
good = "if line.endswith('}'): line = line[:-1] + ',status:\"idea\"}'"

if bad in c:
    c = c.replace(bad, good)
    with open(r'D:\projects\mapzimus-board\maintain.py', 'w', encoding='utf-8') as f:
        f.write(c)
    print('Fixed')
else:
    print('Pattern not found, showing line 258-263:')
    lines = c.split('\n')
    for i, l in enumerate(lines[257:263], 258):
        print(i, repr(l))
