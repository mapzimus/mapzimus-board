with open('index.html','r',encoding='utf-8') as f:
    h = f.read()

# Add Newest button after V-Score
old = 'data-k="vscore"       onclick="setSort(this)">V-Score</button>'
new = 'data-k="vscore"       onclick="setSort(this)">V-Score</button>\n    <button class="sb"    data-k="newest"       onclick="setSort(this)">Newest</button>'
h = h.replace(old, new, 1)

# Bump cache version
h = h.replace('data.js?v=5', 'data.js?v=6').replace('app.js?v=5', 'app.js?v=6')

with open('index.html','w',encoding='utf-8') as f:
    f.write(h)
print('Done -', h.count('Newest'), 'Newest button(s) added')
