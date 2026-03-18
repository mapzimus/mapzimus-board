with open('maintain.py','r',encoding='utf-8') as f:
    m = f.read()

# Add fix_chars step after fix_encoding call
old = '    fix_encoding()\n    add_ext()'
new = '    fix_encoding()\n    fix_chars()\n    add_ext()'

# Add the fix_chars function before the add_ext function
func = '''
# ── FIX ENCODING ARTIFACTS ───────────────────────────────────────────────────

def fix_chars():
    """Replace middot and other non-ASCII chars that cause browser rendering issues."""
    changes = 0
    for filename in ['data.js', 'app.js']:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        before = len(content)
        content = content.replace('\\u00b7', ' - ')   # middot -> plain dash
        content = content.replace('\\u00b2', '2')      # superscript 2 -> plain 2
        content = content.replace('\\u2014', '-')      # em dash -> hyphen
        content = content.replace('\\u2013', '-')      # en dash -> hyphen
        if len(content) != before:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
            changes += 1
    if changes:
        print(f'  [fix_chars] Fixed encoding artifacts in {changes} file(s)')

'''

insertion_point = m.find('\n# ── 2. ADD EXT')
m = m[:insertion_point] + func + m[insertion_point:]
m = m.replace(old, new, 1)

with open('maintain.py','w',encoding='utf-8') as f:
    f.write(m)
print('maintain.py updated')
