import re

# Find all replacement char contexts in both files
for filename in ['data.js', 'app.js']:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    hits = [(m.start(), content[max(0,m.start()-40):m.start()+40]) 
            for m in re.finditer(r'\ufffd', content)]
    print(f'\n{filename}: {len(hits)} replacement chars (U+FFFD)')
    for pos, ctx in hits[:12]:
        # Show char codes around it
        codes = [f'U+{ord(c):04X}' for c in ctx]
        print(f'  pos {pos}: {repr(ctx)}')
