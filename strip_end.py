with open('data.js','r',encoding='utf-8') as f:
    c = f.read()
# Strip closing bracket
c = c[:c.rfind('\n]; // end D')]
with open('data.js','w',encoding='utf-8') as f:
    f.write(c)
print('Ready, ends:', repr(c[-50:]))
