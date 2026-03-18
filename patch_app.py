with open('app.js','r',encoding='utf-8') as f:
    app = f.read()

# Replace the sort comparator to handle 'newest'
old = """  }).sort((a, b) => {
    const av = sortK === 'vscore' ? a.vs : (a.sc[sortK] || 0);
    const bv = sortK === 'vscore' ? b.vs : (b.sc[sortK] || 0);
    return bv - av;
  });"""

new = """  });
  // Sort
  if (sortK === 'newest') {
    r.sort((a, b) => D.indexOf(b) - D.indexOf(a));
  } else {
    r.sort((a, b) => {
      const av = sortK === 'vscore' ? a.vs : (a.sc[sortK] || 0);
      const bv = sortK === 'vscore' ? b.vs : (b.sc[sortK] || 0);
      return bv - av;
    });
  }"""

if old in app:
    app = app.replace(old, new, 1)
    print('Sort logic patched')
else:
    print('ERROR: old string not found - check spacing')

with open('app.js','w',encoding='utf-8') as f:
    f.write(app)
