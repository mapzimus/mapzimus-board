import subprocess, sys, os
py = r"C:\Users\mhowe\AppData\Local\Python\pythoncore-3.14-64\python.exe"
proj = r"D:\projects\mapzimus-board"
for b in ["BATCH_HAB.py", "BATCH_HAC.py"]:
    print("=" * 60)
    print(f"Running {b}...")
    print("=" * 60)
    r = subprocess.run([py, os.path.join(proj, b)], capture_output=True, text=True, cwd=proj)
    print(r.stdout)
    if r.stderr: print("STDERR:", r.stderr)
print("=" * 60)
print("Running maintain.py...")
print("=" * 60)
r = subprocess.run([py, os.path.join(proj, "maintain.py")], capture_output=True, text=True, cwd=proj)
print(r.stdout)
if r.stderr: print("STDERR:", r.stderr)
