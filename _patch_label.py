with open('app.js', 'r', encoding='utf-8') as f:
    content = f.read()
count = content.count('V-Score v4')
content = content.replace('V-Score v4', 'V-Score v5')
with open('app.js', 'w', encoding='utf-8') as f:
    f.write(content)
print(f"Replaced {count} 'V-Score v4' -> 'V-Score v5'")
