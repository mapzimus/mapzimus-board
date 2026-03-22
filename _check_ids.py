import re
txt = open('data.js', 'r', encoding='utf-8').read()
ids = re.findall(r'id:"([^"]+)"', txt)
print(f"Total: {len(ids)}")
print("Last 5:", ids[-5:])
