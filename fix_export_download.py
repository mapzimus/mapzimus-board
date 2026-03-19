with open(r'D:\projects\mapzimus-board\app.js','r',encoding='utf-8') as f: c=f.read()

# Replace the clipboard approach with a direct file download
old = "  // Copy to clipboard\n  navigator.clipboard.writeText(script).then(() => {"
new = "  // Download as file directly - no clipboard needed\n  const blob = new Blob([script], {type:'text/plain'});\n  const a = document.createElement('a');\n  a.href = URL.createObjectURL(blob);\n  a.download = 'patch_overrides.py';\n  a.click();\n  setTimeout(() => {\n    alert(`\u2705 patch_overrides.py downloaded!\\n\\nIn PowerShell:\\n\\n  cd D:\\\\projects\\\\mapzimus-board\\n  Move-Item $env:USERPROFILE\\\\Downloads\\\\patch_overrides.py .\\n  python patch_overrides.py\\n  python maintain.py\\n  git add .\\n  git commit -m \"Apply status updates\"\\n  git push`);\n  }, 500);\n  // unused then block below for compat\n  Promise.resolve().then(() => {"

if old in c:
    c = c.replace(old, new, 1)
    with open(r'D:\projects\mapzimus-board\app.js','w',encoding='utf-8') as f: f.write(c)
    print('Fixed: export now downloads file directly')
else:
    idx = c.find('Copy to clipboard')
    print('Not found. Context:', repr(c[max(0,idx-10):idx+100]))
