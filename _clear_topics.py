"""Clear all topics so _auto_topics.py re-tags everything."""
import re

f = open('data.js', 'r', encoding='utf-8')
text = f.read()
f.close()

# Replace all non-empty topics:[] with topics:[]
count = 0
def replacer(m):
    global count
    if m.group(1):  # has content
        count += 1
        return 'topics:[]'
    return m.group(0)

text = re.sub(r'topics:\[([^\]]*)\]', replacer, text)

f = open('data.js', 'w', encoding='utf-8')
f.write(text)
f.close()
print(f"Cleared topics on {count} ideas")
