with open(r'D:\projects\mapzimus-board\maintain.py', 'r', encoding='utf-8') as f:
    c = f.read()
# The bad line has a backslash before the closing quote on the status line
bad  = ",status:\"idea\"}\\'"
good = ",status:\"idea\"}'"
if bad in c:
    c = c.replace(bad, good)
    with open(r'D:\projects\mapzimus-board\maintain.py', 'w', encoding='utf-8') as f:
        f.write(c)
    print('Fixed')
else:
    print('Not found - checking context:')
    idx = c.find('status')
    print(repr(c[idx:idx+60]))
