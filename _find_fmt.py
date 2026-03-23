lines = open('app.js', 'r', encoding='utf-8').readlines()
for i in range(973, min(990, len(lines))):
    print(f"L{i+1}: {lines[i].rstrip()}")
