"""
RUN_ALL.py - Master runner: fix_vscores + Batches A through V

NEW BATCHES ONLY (if A-T already done on the Legion):
  python BATCH_U.py && python maintain.py && git add . && git commit -m "Batch U: conflict geography, proxy wars, arms, nuclear, democracy" && git push
  python BATCH_V.py && python maintain.py && git add . && git commit -m "Batch V: demographic collapse, AI race, supply chains, energy, water" && git push

FULL RUN from scratch:
  cd D:\\projects\\mapzimus-board
  python RUN_ALL.py
"""
import subprocess, sys

def run(cmd):
    print(f'\n>>> {cmd}')
    result = subprocess.run(cmd, shell=True)
    if result.returncode != 0:
        print(f'ERROR: code {result.returncode}')
        sys.exit(1)

batches = [
    ('fix_vscores.py', 'Fix V-scores: recompute from formula'),
    ('BATCH_A.py',  'Batch A: Sage marijuana/inmates, HSUS mortality'),
    ('BATCH_B.py',  'Batch B: ProQuest Business/Education/Labor, GSS, SNAP'),
    ('BATCH_C.py',  'Batch C: Soccer/WC2026, energy, gun-suicide'),
    ('BATCH_D.py',  'Batch D: Standalone geographic maps'),
    ('BATCH_E.py',  'Batch E: Health/Law/Education/Labor standalone'),
    ('BATCH_F.py',  'Batch F: Metro, state pensions, prisons, immigration'),
    ('BATCH_G.py',  'Batch G: International/Foreign Commerce, global maps'),
    ('BATCH_H.py',  'Batch H: Banking/Finance/Prices, GoFundMe'),
    ('BATCH_I.py',  'Batch I: Income/Poverty, missing men'),
    ('BATCH_J.py',  'Batch J: HSUS historical, transfers paradox'),
    ('BATCH_K.py',  'Batch K: 2025-2026: DOGE, Ozempic, H5N1, EV'),
    ('BATCH_L.py',  'Batch L: Sports, music, space, weather, gaming'),
    ('BATCH_M.py',  'Batch M: ProQuest/Sage tables x current events'),
    ('BATCH_N.py',  'Batch N: ProQuest/Sage/HSUS x pop culture, sports'),
    ('BATCH_O.py',  'Batch O: Geography-first: rivers, crops, energy, transport'),
    ('BATCH_P.py',  'Batch P: Geography-first: health, education, law, banking'),
    ('BATCH_Q.py',  'Batch Q: Lyme, radon, drought, flood, pharmacy deserts'),
    ('BATCH_R.py',  'Batch R: Dollar stores, transit, food geography'),
    ('BATCH_S.py',  'Batch S: International Stats T1340-T1382'),
    ('BATCH_T.py',  'Batch T: Conflict: arms, nuclear, democracy, terrorism'),
    ('BATCH_U.py',  'Batch U: Iran-Israel, proxy wars, colonial borders, nuclear'),
    ('BATCH_V.py',  'Batch V: Demographic collapse, AI race, supply chains, water'),
]

print('='*60)
print('MAPZIMUS BOARD - FULL RUNNER (fix_vscores + A-V)')
print('Starting at 691 -> targeting ~1125 ideas')
print('='*60)

for filename, msg in batches:
    print(f'\n--- {filename} ---')
    run(f'python {filename}')
    run('python maintain.py')
    run('git add .')
    run(f'git commit -m "{msg}"')
    run('git push')
    print(f'[OK] {filename}')

print('\nDONE. Site: https://mapzimus.github.io/mapzimus-board/')
print('Ctrl+Shift+R to force refresh')
