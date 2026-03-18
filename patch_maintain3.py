"""
patch_maintain3.py - Upgrades maintain.py with:
  1. Comprehensive fix_chars (strips ALL non-ASCII, fixes = in sc:{} blocks)
  2. validate_js step using Node to confirm file parses as valid JS

Run once: python patch_maintain3.py
"""
with open('maintain.py', 'r', encoding='utf-8') as f:
    m = f.read()

# ── Replace fix_chars function ────────────────────────────────────────────────
old_fix = '''def fix_chars():
    """Replace non-ASCII chars that cause browser rendering issues."""
    changed = 0
    for filename in ['data.js', 'app.js']:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        new = content.replace('\\u00b7', ' - ').replace('\\u00b2', '2')
        new = new.replace('\\u2014', '-').replace('\\u2013', '-')
        if new != content:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(new)
            changed += 1
    if changed:
        print(f'  [fix_chars] Fixed in {changed} file(s)')'''

new_fix = '''def fix_chars():
    """Strip all non-ASCII and fix JS syntax issues that break the browser."""
    import re as _re
    for filename in ['data.js', 'app.js']:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        new = content
        # Named replacements first (preserve meaning)
        for bad, good in [
            ('\\u2014', '-'),   # em dash
            ('\\u2013', '-'),   # en dash
            ('\\u2019', "'"),   # right single quote
            ('\\u2018', "'"),   # left single quote
            ('\\u201c', ''),    # left double quote -> remove (breaks JS strings)
            ('\\u201d', ''),    # right double quote -> remove
            ('\\u2026', '...'), # ellipsis
            ('\\u2192', '->'),  # right arrow
            ('\\u00b7', ' - '), # middot
            ('\\u00b2', '2'),   # superscript 2
            ('\\u00b0', ' degrees'), # degree symbol
            ('\\u00a0', ' '),   # non-breaking space
            ('\\u00d7', 'x'),   # multiplication sign
        ]:
            new = new.replace(bad, good)
        # Nuclear option: strip any remaining non-ASCII
        new = _re.sub(r'[^\\x00-\\x7F]', '', new)
        # Fix = signs inside sc:{} blocks (should always be :)
        new = _re.sub(
            r'(emotional|relatability|surprise|tension|visual|data_ready|originality)=(\\d+)',
            r'\\1:\\2', new
        )
        if new != content:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(new)
    # Count remaining non-ASCII (should be 0)
    with open('data.js', 'r', encoding='utf-8') as f:
        final = f.read()
    bad_count = len([c for c in final if ord(c) > 127])
    if bad_count:
        print(f'  [fix_chars] WARNING: {bad_count} non-ASCII chars remain!')
    else:
        print(f'  [fix_chars] Clean (0 non-ASCII chars)')'''

# ── Add validate_js function before MAIN block ────────────────────────────────
new_validate_js = '''
def validate_js():
    """Run Node.js to confirm data.js is syntactically valid JavaScript."""
    import subprocess
    script = (
        "try{"
        "eval(require('fs').readFileSync('data.js','utf8').replace('const D','var D'));"
        "console.log('ok:'+D.length);"
        "}catch(e){console.log('err:'+e.message.substring(0,120));}"
    )
    try:
        r = subprocess.run(['node', '-e', script],
                           capture_output=True, text=True, timeout=30)
        out = r.stdout.strip()
        if out.startswith('ok:'):
            print(f'  [js_check] Valid JS - {out[3:]} ideas parseable in browser')
        else:
            print(f'  [js_check] JS PARSE ERROR: {out}')
            print('  Fix the error above before pushing!')
            sys.exit(1)
    except FileNotFoundError:
        print('  [js_check] Node.js not found - skipping JS validation')
    except subprocess.TimeoutExpired:
        print('  [js_check] Node.js timed out - skipping')

'''

if old_fix in m:
    m = m.replace(old_fix, new_fix)
    print('fix_chars replaced.')
else:
    print('ERROR: Could not find old fix_chars to replace.')

if 'validate_js' not in m:
    m = m.replace("# ── MAIN", new_validate_js + "# ── MAIN")
    m = m.replace("    validate()\n    print(", "    validate()\n    validate_js()\n    print(")
    print('validate_js added.')
else:
    print('validate_js already present.')

with open('maintain.py', 'w', encoding='utf-8') as f:
    f.write(m)

print('maintain.py patched. Test with: python maintain.py')
