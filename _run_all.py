"""Master runner — executes all batches with maintain.py after each."""
import subprocess, sys, os

PY = r"C:\Users\mhowe\AppData\Local\Python\pythoncore-3.14-64\python.exe"
CWD = r"D:\projects\mapzimus-board"
os.chdir(CWD)

def run(script, label):
    print(f"\n{'='*60}")
    print(f"  [{label}] Running {script}...")
    print(f"{'='*60}")
    r = subprocess.run([PY, script], capture_output=True, text=True, cwd=CWD)
    print(r.stdout)
    if r.stderr:
        print("STDERR:", r.stderr)
    if r.returncode != 0:
        print(f"[ERROR] {script} failed with exit code {r.returncode}")
        sys.exit(1)
    return r.returncode

# Pre-flight
run("maintain.py", "PRE-FLIGHT")

batches = [
    ("BATCH_GE.py", "OWID deep dive + HSUS historical (70 ideas)"),
    ("BATCH_GF.py", "US deep dive + gap-fill (79 ideas)"),
    ("BATCH_GG.py", "High-virality + controversy (53 ideas)"),
    ("BATCH_GH.py", "Europe/Oceania/bivariate/dot map (38 ideas)"),
    ("BATCH_GI.py", "Cross-reference mega-batch (60 ideas)"),
]

for script, desc in batches:
    run(script, desc)
    run("maintain.py", f"VALIDATE after {script}")

print("\n" + "="*60)
print("  ALL BATCHES COMPLETE")
print("="*60)

# Count final ideas
import re
with open("data.js", encoding="utf-8") as f:
    raw = f.read()
count = len(re.findall(r'id:"[^"]+"', raw))
print(f"\nFinal idea count: {count}")
print("Done!")
