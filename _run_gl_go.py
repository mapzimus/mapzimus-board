"""Run BATCH_GL through BATCH_GO sequentially, then maintain.py."""
import subprocess, sys, os
py = r"C:\Users\mhowe\AppData\Local\Python\pythoncore-3.14-64\python.exe"
proj = r"D:\projects\mapzimus-board"

batches = ["BATCH_GL.py", "BATCH_GM.py", "BATCH_GN.py", "BATCH_GO.py"]
for b in batches:
    path = os.path.join(proj, b)
    print(f"\n{'='*60}")
    print(f"Running {b}...")
    print('='*60)
    r = subprocess.run([py, path], capture_output=True, text=True, cwd=proj)
    print(r.stdout)
    if r.stderr:
        print(f"STDERR: {r.stderr[:500]}")
    if r.returncode != 0:
        print(f"[ERROR] {b} failed with code {r.returncode}")
        sys.exit(1)

print(f"\n{'='*60}")
print("Running maintain.py...")
print('='*60)
r = subprocess.run([py, os.path.join(proj, "maintain.py")], capture_output=True, text=True, cwd=proj)
print(r.stdout)
if r.stderr:
    print(f"STDERR: {r.stderr[:500]}")
print(f"\nAll done! Return code: {r.returncode}")
