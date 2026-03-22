import subprocess, sys, os
py = r"C:\Users\mhowe\AppData\Local\Python\pythoncore-3.14-64\python.exe"
proj = r"D:\projects\mapzimus-board"
for b in ["BATCH_HAV.py", "BATCH_HAW.py"]:
    print(f"\n=== Running {b} ===")
    r = subprocess.run([py, os.path.join(proj, b)], capture_output=True, text=True, cwd=proj)
    print(r.stdout)
    if r.stderr: print("ERR:", r.stderr[:500])
print("\n=== Auto-topic new entries ===")
r = subprocess.run([py, os.path.join(proj, "_auto_topics.py")], capture_output=True, text=True, cwd=proj)
print(r.stdout[:500])
print("\n=== Running maintain.py ===")
r = subprocess.run([py, os.path.join(proj, "maintain.py")], capture_output=True, text=True, cwd=proj)
print(r.stdout)
if r.stderr: print("ERR:", r.stderr[:500])
