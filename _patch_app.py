import re

with open('app.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
skip_until_close = False
for i, line in enumerate(lines):
    # Remove the FMT_BONUS definition block (lines 974-977)
    if 'const FMT_BONUS' in line:
        skip_until_close = True
        continue
    if skip_until_close:
        if '};' in line:
            skip_until_close = False
        continue
    
    # Remove the FMT_BONUS display from the vs rendering (line 382)
    if 'FMT_BONUS[d.fmt]' in line:
        # Replace the whole vs display to remove the bonus span
        line = re.sub(
            r"\$\{FMT_BONUS\[d\.fmt\]\?'<span class=\"fmt-bonus\">\+'\+FMT_BONUS\[d\.fmt\]\+'</span>':''\}",
            '',
            line
        )
    
    new_lines.append(line)

with open('app.js', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

# Verify
with open('app.js', 'r', encoding='utf-8') as f:
    content = f.read()
    
hits = content.count('FMT_BONUS')
print(f"FMT_BONUS references remaining: {hits}")
print(f"Total lines: {len(new_lines)} (was {len(lines)})")
