lines = open('maintain.py', 'r', encoding='utf-8').readlines()
for i in range(203, 285):
    print(f"L{i+1}: {lines[i].rstrip()}")
