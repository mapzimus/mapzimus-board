with open('app.js','r',encoding='utf-8') as f: c=f.read()

old = "if (sortK === 'newest') {\n    r.sort((a, b) => D.indexOf(b) - D.indexOf(a));\n  } else {"
new = "if (sortK === 'newest') {\n    r.sort((a, b) => D.indexOf(b) - D.indexOf(a));\n  } else if (sortK === 'oldest') {\n    r.sort((a, b) => D.indexOf(a) - D.indexOf(b));\n  } else {"

if old in c:
    c = c.replace(old, new)
    with open('app.js','w',encoding='utf-8') as f: f.write(c)
    print('Patched OK')
else:
    # Try CRLF
    old2 = old.replace('\n','\r\n')
    new2 = new.replace('\n','\r\n')
    if old2 in c:
        c = c.replace(old2, new2)
        with open('app.js','w',encoding='utf-8') as f: f.write(c)
        print('Patched OK (CRLF)')
    else:
        idx = c.find("sortK === 'newest'")
        print('Not found. Context:', repr(c[idx:idx+120]))
