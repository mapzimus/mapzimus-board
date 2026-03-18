import re

with open('data.js','r',encoding='utf-8') as f:
    c = f.read()

# Fix: remove the leading comma before first idea
# Pattern: const D =[\n\n,{id:  ->  const D =[\n{id:
before = c[:200]
c = re.sub(r'(const D\s*=\s*\[[\s\n]*),(\{id:)', r'\1\2', c, count=1)
after = c[:200]

if before != after:
    print('Fixed leading comma')
else:
    print('No leading comma found - checking differently')
    # Try another approach
    idx = c.find('[')
    segment = c[idx:idx+20]
    print('After [:', repr(segment))

with open('data.js','w',encoding='utf-8') as f:
    f.write(c)

# Verify
ids = re.findall(r'\{id:"([^"]+)"', c)
print(f'Ideas: {len(ids)}')
print('First 120:', repr(c[:120]))
