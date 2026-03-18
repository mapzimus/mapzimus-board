with open('maintain.py','r',encoding='utf-8') as f:
    m = f.read()

# Add leading comma fix right before the final write in fix_encoding
old_write = "    with open('data.js', 'w', encoding='utf-8') as f:\n        f.write(text)"
new_write = "    # Fix leading comma before first element (causes sparse array hole)\n    text = re.sub(r'(const D\\s*=\\s*\\[[\\s\\n]*),(\\{id:)', r'\\1\\2', text, count=1)\n    with open('data.js', 'w', encoding='utf-8') as f:\n        f.write(text)"

if old_write in m:
    m = m.replace(old_write, new_write, 1)
    print('Patched maintain.py with leading comma fix')
else:
    print('Pattern not found, showing nearby context...')
    idx = m.find("with open('data.js', 'w'")
    print(repr(m[idx-50:idx+100]))

with open('maintain.py','w',encoding='utf-8') as f:
    f.write(m)
