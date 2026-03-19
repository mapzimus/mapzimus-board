with open(r'D:\projects\mapzimus-board\app.js','r',encoding='utf-16') as f:
    content = f.read()
with open(r'D:\projects\mapzimus-board\app.js','w',encoding='utf-8') as f:
    f.write(content)
print('app.js rewritten as UTF-8, length:', len(content))
# verify first chars
print('First 50 chars:', repr(content[:50]))
