import re
c = open('data.js', encoding='utf-8').read()
ids = re.findall(r'id:"([^"]+)"', c)
print(f"Current ideas: {len(ids)}")
print(f"data.js size: {round(len(c)/1024,1)} KB")
