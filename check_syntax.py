import subprocess
result = subprocess.run(
    ['node', '--check', 'app.js'],
    capture_output=True, text=True,
    cwd=r'D:\projects\mapzimus-board'
)
print('STDOUT:', result.stdout)
print('STDERR:', result.stderr)
print('RC:', result.returncode)
