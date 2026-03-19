
# Read maintain.py with the correct encoding
for enc in ['utf-16', 'utf-16-le', 'utf-16-be', 'latin-1']:
    try:
        with open(r'D:\projects\mapzimus-board\maintain.py', 'r', encoding=enc) as f:
            c = f.read()
        print('Read with encoding:', enc)
        break
    except Exception as e:
        print(enc, 'failed:', e)

# Write back as clean UTF-8
with open(r'D:\projects\mapzimus-board\maintain.py', 'w', encoding='utf-8') as f:
    f.write(c)
print('Rewritten as UTF-8')

# Verify syntax
import py_compile, sys
try:
    py_compile.compile(r'D:\projects\mapzimus-board\maintain.py', doraise=True)
    print('Syntax OK')
except py_compile.PyCompileError as e:
    print('Syntax error:', e)
