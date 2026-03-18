with open('data.js','r',encoding='utf-8') as f:
    c = f.read()
end_idx = c.rfind('\n]; // end D')
c = c[:end_idx]
with open('data.js','w',encoding='utf-8') as f:
    f.write(c)
print('Ready, ends:', repr(c[-40:]))
