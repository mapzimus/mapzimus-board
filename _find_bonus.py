lines = open('maintain.py').readlines()
for i, l in enumerate(lines):
    if 'FMT_BONUS' in l or 'calc_vs' in l or 'bonus' in l.lower():
        print(f"{i+1}: {l.rstrip()}")
