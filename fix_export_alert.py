with open(r'D:\projects\mapzimus-board\app.js','r',encoding='utf-8') as f: c=f.read()

old = """  // Copy to clipboard
  navigator.clipboard.writeText(script).then(() => {
    alert(` ${n} overrides copied as Python patch script.\\n\\nPaste into D:\\\\projects\\\\mapzimus-board\\\\patch_overrides.py and run:\\n  python patch_overrides.py\\n  python maintain.py\\n  git add . && git commit -m "Apply browser edits" && git push`);
  }).catch(() => {
    // Fallback: show in textarea
    const win = window.open('', '_blank', 'width=700,height=500');
    win.document.write('<textarea style="width:100%;height:100%;font-family:monospace;font-size:12px">' + script.replace(/</g,'&lt;') + '</textarea>');
  });
}"""

new = """  // Copy to clipboard
  navigator.clipboard.writeText(script).then(() => {
    alert(`\u2705 ${n} overrides copied!\\n\\nIn PowerShell:\\n\\n  cd D:\\\\projects\\\\mapzimus-board\\n  # paste into patch_overrides.py, then:\\n  python patch_overrides.py\\n  python maintain.py\\n  git add .\\n  git commit -m "Apply status updates"\\n  git push\\n\\n(PowerShell uses separate lines, not &&)`);
  }).catch(() => {
    const win = window.open('', '_blank', 'width=700,height=560');
    win.document.write('<pre style="background:#111;color:#eee;padding:16px;font-size:12px;white-space:pre-wrap">SAVE AS: D:\\\\projects\\\\mapzimus-board\\\\patch_overrides.py\\n\\nTHEN RUN IN POWERSHELL:\\n  cd D:\\\\projects\\\\mapzimus-board\\n  python patch_overrides.py\\n  python maintain.py\\n  git add .\\n  git commit -m \\"Apply status updates\\"\\n  git push\\n\\n---\\n\\n' + script.replace(/</g,'&lt;') + '</pre>');
  });
}"""

if old in c:
    c = c.replace(old, new)
    with open(r'D:\projects\mapzimus-board\app.js','w',encoding='utf-8') as f: f.write(c)
    print('Fixed export alert')
else:
    # Try to find and show what's around the alert
    idx = c.find('overrides copied')
    print('Not found. Context:', repr(c[max(0,idx-50):idx+200]))
