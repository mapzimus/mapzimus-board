import subprocess, sys
py = r"C:\Users\mhowe\AppData\Local\Python\pythoncore-3.14-64\python.exe"
r = subprocess.run([py, "validate_batches.py"], capture_output=True, text=True, cwd=r"D:\projects\mapzimus-board")
print(r.stdout)
if r.stderr:
    print("STDERR:", r.stderr)
print("EXIT CODE:", r.returncode)
