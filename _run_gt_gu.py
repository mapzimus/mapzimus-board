"""Run BATCH_GT and BATCH_GU, then maintain.py."""
import subprocess, sys, os
py = r"C:\Users\mhowe\AppData\Local\Python\pythoncore-3.14-64\python.exe"
proj = r"D:\projects\mapzimus-board"
for b in ["BATCH_GT.py", "BATCH_GU.py"]:
    print(f"\n{'='*60}\nRunning {b}...\n{'='*60}")
    r = subprocess.run([py, os.path.join(proj, b)], capture_output=True, text=True, cwd=proj)
    print(r.stdout)
    if r.stderr: print(f"STDERR: {r.stderr[:500]}")
    if r.returncode != 0: print(f"[ERROR] {b} failed"); sys.exit(1)
print(f"\n{'='*60}\nRunning maintain.py...\n{'='*60}")
r = subprocess.run([py, os.path.join(proj, "maintain.py")], capture_output=True, text=True, cwd=proj)
print(r.stdout)
if r.stderr: print(f"STDERR: {r.stderr[:500]}")
print(f"Return code: {r.returncode}")
