with open('index.html','r',encoding='utf-8') as f: c=f.read()
needle = '>Newest</button>'
replacement = '>Newest</button>\n    <button class="sb"    data-k="oldest"       onclick="setSort(this)">Oldest</button>'
if needle in c:
    c = c.replace(needle, replacement, 1)
    with open('index.html','w',encoding='utf-8') as f: f.write(c)
    print('index.html patched OK')
else:
    print('needle not found')
