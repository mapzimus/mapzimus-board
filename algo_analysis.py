import pandas as pd, numpy as np, re, os, json

# Read data.js
with open(r"D:\projects\mapzimus-board\data.js", encoding='utf-8') as f:
    raw = f.read()

# Parse all fields
ids = re.findall(r'id:"([^"]+)"', raw)
titles = re.findall(r'title:"([^"]+)"', raw)
sections = re.findall(r'section:"([^"]+)"', raw)
geos = re.findall(r'geo:"([^"]+)"', raw)
fmts = re.findall(r'fmt:"([^"]+)"', raw)
vs_scores = [int(x) for x in re.findall(r',vs:(\d+),', raw)]

# Parse sc blocks flexibly
sc2 = re.findall(r'sc:\s*\{[^}]+\}', raw)
all_sc = []
for block in sc2:
    d = {}
    for field in ['emotional','relatability','clarity','surprise','tension','visual','originality','data_ready']:
        m = re.search(field + r':(\d+)', block)
        d[field] = int(m.group(1)) if m else None
    all_sc.append(d)

sc_df = pd.DataFrame(all_sc)
sc_df['vs'] = vs_scores
sc_df['id'] = ids
sc_df['title'] = titles
sc_df['section'] = sections
sc_df['geo'] = geos
sc_df['fmt'] = fmts

# --- ALGORITHM ANALYSIS ---
weights = {'emotional':2,'relatability':2,'clarity':2,'surprise':1.5,'tension':1,'visual':1.25,'originality':1}
total_w = sum(weights.values())  # 10.75

print("="*60)
print("VIRALITY ALGORITHM v3 ANALYSIS")
print("="*60)

print("\n1. EFFECTIVE WEIGHT OF EACH FIELD:")
for k,v in weights.items():
    pct = v/total_w*100
    print("   %s: weight=%.2f  (%.1f%%)" % (k.ljust(15), v, pct))
print("   %s: multiplicative penalty (0.3 coefficient)" % "data_ready".ljust(15))

print("\n2. FIELD CORRELATIONS WITH FINAL vs:")
for col in ['emotional','relatability','clarity','surprise','tension','visual','originality','data_ready']:
    r = sc_df[col].corr(sc_df.vs)
    print("   %s: r=%.3f" % (col.ljust(15), r))

print("\n3. SENSITIVITY ANALYSIS (raise each field from mean to 100):")
penalty = 1 - 0.3*(1-85/100)
mean_vals = sc_df[['emotional','relatability','clarity','surprise','tension','visual','originality']].mean()
base_raw = sum(mean_vals[k]*weights[k] for k in weights)
base_vs = int((base_raw/total_w) * penalty)
print("   Base vs (all at mean, dr=85): %d" % base_vs)
for k in weights:
    new_raw = base_raw + (100-mean_vals[k])*weights[k]
    new_vs = int((new_raw/total_w) * penalty)
    print("   %s: mean=%.0f -> raising to 100 adds +%d vs points" % (k.ljust(15), mean_vals[k], new_vs-base_vs))

print("\n4. DATA_READY PENALTY EFFECT:")
for dr in [50, 60, 70, 75, 80, 85, 90, 95, 100]:
    p = 1 - 0.3*(1-dr/100)
    print("   data_ready=%3d: penalty factor=%.3f  (a base-80 idea becomes vs=%d)" % (dr, p, int(80*p)))

print("\n5. COMPRESSION AT THE TOP:")
max_raw = sum(100*w for w in weights.values())
max_vs = int((max_raw/total_w) * (1-0.3*(1-100/100)))
print("   Theoretical max (all 100): vs=%d" % max_vs)
great_raw = sum(85*w for w in weights.values())
great_vs = int((great_raw/total_w) * (1-0.3*(1-90/100)))
print("   Great idea (all 85, dr=90): vs=%d" % great_vs)
decent_raw = sum(70*w for w in weights.values())
decent_vs = int((decent_raw/total_w) * (1-0.3*(1-80/100)))
print("   Decent idea (all 70, dr=80): vs=%d" % decent_vs)
print("   Dynamic range: %d points between decent and perfect" % (max_vs - decent_vs))
print("   Actual board range: %d points (%d-%d)" % (max(vs_scores)-min(vs_scores), min(vs_scores), max(vs_scores)))

print("\n6. KEY PROBLEMS IDENTIFIED:")
print("   a) Clarity has LOW variance (std=%.1f) but HIGH weight (18.6%%)" % sc_df.clarity.std())
print("      -> Most ideas score clarity 70-80, so it barely differentiates")
print("   b) Originality has LOW correlation with vs (%.3f)" % sc_df.originality.corr(sc_df.vs))
print("      but originality IS what makes content go viral on social media")
print("   c) Visual has HIGHEST correlation (%.3f) but only 11.6%% weight" % sc_df.visual.corr(sc_df.vs))
print("      -> Visual impact is the #1 scroll-stopper on Instagram")
print("   d) Tension has decent correlation (%.3f) but lowest weight (9.3%%)" % sc_df.tension.corr(sc_df.vs))
print("      -> Controversy drives shares/comments")
print("   e) data_ready penalty is TOO GENTLE: dr=70 only costs 9%% of score")
print("      -> Ideas with unacquired data should be penalized MORE so ready ideas surface")

print("\n7. SCATTER PLOT OVERREPRESENTATION:")
sp_count = (sc_df.fmt=='Scatter plot').sum()
print("   Scatter plots: %d / %d (%.1f%%)" % (sp_count, len(sc_df), sp_count/len(sc_df)*100))
print("   But scatter plots rarely go viral on Instagram - they need annotation")
print("   Choropleths are the proven viral format for @mapzimus")

print("\n8. SECTION NAME CLEANUP NEEDED:")
compound = [s for s in sc_df.section.unique() if '  -  ' in s or ' - ' in s]
print("   %d compound section names found (should use canonical sections)" % len(compound))

print("\n9. PROPOSED ALGORITHM v4:")
print("   Increase: visual (2.0), tension (1.5), originality (1.5)")
print("   Decrease: clarity (1.25)")
print("   Steeper data_ready penalty: 0.5 coefficient instead of 0.3")
print("   Add: format_bonus for choropleths (+3), dot/bivariate maps (+2)")
print("   raw = e*2 + r*2 + c*1.25 + s*1.5 + t*1.5 + v*2.0 + o*1.5")
new_w = {'emotional':2,'relatability':2,'clarity':1.25,'surprise':1.5,'tension':1.5,'visual':2.0,'originality':1.5}
new_tw = sum(new_w.values())
print("   total_w = %.2f" % new_tw)

vs_v4 = []
for i, row in sc_df.iterrows():
    raw_v4 = sum(row[k]*new_w[k] for k in new_w)
    dr = row['data_ready']
    p = 1 - 0.5*(1-dr/100)
    fmt_bonus = 3 if row['fmt'] in ['State choropleth','County choropleth','World choropleth'] else (2 if row['fmt'] in ['Dot map','Bivariate choropleth'] else 0)
    vs_v4.append(int((raw_v4/new_tw)*p) + fmt_bonus)

sc_df['vs_v4'] = vs_v4

print("\n10. v3 vs v4 COMPARISON:")
print("    v3 mean=%.1f std=%.1f range=%d-%d" % (sc_df.vs.mean(), sc_df.vs.std(), sc_df.vs.min(), sc_df.vs.max()))
print("    v4 mean=%.1f std=%.1f range=%d-%d" % (sc_df.vs_v4.mean(), sc_df.vs_v4.std(), sc_df.vs_v4.min(), sc_df.vs_v4.max()))

sc_df['v4_delta'] = sc_df.vs_v4 - sc_df.vs
print("\n    Biggest RISERS (undervalued in v3):")
risers = sc_df.nlargest(10, 'v4_delta')[['id','vs','vs_v4','v4_delta','visual','tension','originality','fmt']]
print(risers.to_string())
print("\n    Biggest FALLERS (overvalued in v3):")
fallers = sc_df.nsmallest(10, 'v4_delta')[['id','vs','vs_v4','v4_delta','visual','tension','originality','fmt']]
print(fallers.to_string())

print("\n" + "="*60)
print("ANALYSIS COMPLETE")
print("="*60)
