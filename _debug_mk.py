# Test the mk() formula from the new batches
def mk_new(e,r,c,s,t,v,o,dr):
    raw=e*2+r*2+c*1.25+s*1.5+t*1.5+v*2.0+o*1.5
    vs=int((raw/11.75)*(1-0.5*(1-dr/100)))
    return raw, vs

# Test with typical high-scoring inputs: e=8,r=9,c=8,s=7,t=5,v=8,dr=90
raw, vs = mk_new(8,9,8,7,5,8,7,90)
print(f"New mk(): raw={raw}, vs={vs}")
print(f"  Expected: raw should be ~100, vs should be ~80+")
print()

# The v4 formula from maintain.py:
# raw = e*2 + r*2 + c*1.25 + s*1.5 + t*1.5 + v*2.0 + o*1.5
# penalty = 1 - 0.5*(1-dr/100)
# vs = int((raw/11.75)*penalty) + FMT_BONUS

raw2 = 8*2 + 9*2 + 8*1.25 + 7*1.5 + 5*1.5 + 8*2.0 + 7*1.5
penalty = 1 - 0.5*(1-90/100)
vs2 = int((raw2/11.75)*penalty)
print(f"Manual calc: raw={raw2}, penalty={penalty}, vs={vs2}")
print()

# WAIT - the mk function is missing the 8th param. Let me check...
# mk(id,title,sub,typ,geo,fmt,sect,tbl,e,r,c,s,t,v,o,dr)
# That's: e=emotional, r=relatability, c=clarity, s=surprise, t=tension, v=visual, o=originality, dr=data_ready
# That looks right...

# Let me check what a working batch used:
# From BATCH_GO (which worked) - typical call:
# mk("go001","...",XREF,US,Scatter plot,...,8,8,7,8,7,7,8,75)
raw3 = 8*2+8*2+7*1.25+8*1.5+7*1.5+7*2.0+8*1.5
penalty3 = 1-0.5*(1-75/100)
vs3 = int((raw3/11.75)*penalty3)
print(f"Working batch calc: raw={raw3}, penalty={penalty3}, vs={vs3}")
print()

# The formulas are identical. So why is maintain.py overwriting them to low values?
# Let me check if maintain.py recalc_vs is doing something different...
print("The mk() formula should produce scores in the 50-80 range.")
print(f"But the data shows scores of 4-10 for the new batches.")
print()
print("HYPOTHESIS: maintain.py recalc_vs is recalculating and OVERWRITING")
print("the scores using a different formula than mk().")
print()

# Let me look at what data_ready value maintain.py sees
# Maybe the sc fields aren't being parsed correctly?
# Let me check an actual entry from the data.js file
import re
with open(r"D:\projects\mapzimus-board\data.js", "r", encoding="utf-8") as f:
    blob = f.read()

# Find gz001 entry
m = re.search(r'\{[^}]*id:"gz001"[^}]*\}', blob)
if m:
    print(f"gz001 raw entry: {m.group()[:300]}")
    print()

# Find a working older entry for comparison
m2 = re.search(r'\{[^}]*id:"go001"[^}]*\}', blob)
if m2:
    print(f"go001 raw entry: {m2.group()[:300]}")
