import subprocess, sys, re

PY = r"C:\Users\mhowe\AppData\Local\Python\pythoncore-3.14-64\python.exe"
CWD = r"D:\projects\mapzimus-board"

def run(script):
    print(f"\n{'='*60}")
    print(f"  Running {script}...")
    print(f"{'='*60}")
    r = subprocess.run([PY, script], capture_output=True, text=True, cwd=CWD)
    print(r.stdout)
    if r.stderr:
        print("STDERR:", r.stderr)
    if r.returncode != 0:
        print(f"FAILED: {script}")
        sys.exit(1)

run("BATCH_GJ.py")
run("maintain.py")
run("BATCH_GK.py")
run("maintain.py")

# Final count
with open(r"D:\projects\mapzimus-board\data.js", encoding="utf-8") as f:
    raw = f.read()
count = len(re.findall(r'id:"[^"]+"', raw))
print(f"\nFinal idea count: {count}")
print("ALL DONE!")
