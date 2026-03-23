lines = open('maintain.py', 'r', encoding='utf-8').readlines()
# Find remaining v4
for i, l in enumerate(lines):
    if 'v4' in l:
        print(f"v4 at L{i+1}: {l.rstrip()}")

print("\n--- recalc_vs function ---")
in_func = False
for i, l in enumerate(lines):
    if 'def recalc_vs' in l:
        in_func = True
    if in_func:
        print(f"L{i+1}: {l.rstrip()}")
    if in_func and l.startswith('# -- 5.'):
        break
