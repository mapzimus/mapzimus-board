with open(r'D:\projects\mapzimus-board\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Add .fmt-bonus CSS after .vl style
old_vl = '.vl{font-size:9px;color:var(--text3);text-align:right;}'
new_vl = '.vl{font-size:9px;color:var(--text3);text-align:right;}\n.fmt-bonus{font-size:11px;font-weight:600;color:#8eedc7;margin-left:2px;vertical-align:super;}'

content = content.replace(old_vl, new_vl, 1)  # Only replace first occurrence

if '.fmt-bonus' in content:
    print("SUCCESS: .fmt-bonus CSS added")
else:
    print("WARNING: CSS not added")

with open(r'D:\projects\mapzimus-board\index.html', 'w', encoding='utf-8') as f:
    f.write(content)
