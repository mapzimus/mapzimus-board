"""
update_appjs_v4.py - Update app.js for virality algorithm v4
Changes:
  1. SC_FIELDS weights updated to v4
  2. Algorithm comment block updated
  3. Score color thresholds adjusted for new distribution
  4. Format bonus indicator added to card UI
  5. Format bonus tooltip added to V-Score display
"""
import re

with open('app.js', 'r', encoding='utf-8') as f:
    content = f.read()

original = content

# ============================================================
# 1. Replace SC_FIELDS with v4 weights
# ============================================================
old_sc_fields = """const SC_FIELDS = [
  { key:'emotional',    label:'Emotional',    short:'Emo', color:'#ff6b8a', weight:2    },
  { key:'relatability', label:'Relatability', short:'Rel', color:'#38bdf8', weight:2    },
  { key:'clarity',      label:'Clarity',      short:'Cla', color:'#fb923c', weight:2    },
  { key:'surprise',     label:'Surprise',     short:'Sur', color:'#facc15', weight:1.5  },
  { key:'tension',      label:'Tension',      short:'Ten', color:'#c084fc', weight:1.0  },
  { key:'visual',       label:'Visual',       short:'Vis', color:'#34d399', weight:1.25 },
  { key:'originality',  label:'Originality',  short:'Ori', color:'#f472b6', weight:1.0  },
  { key:'data_ready',   label:'Data Ready',   short:'Dat', color:'#818cf8', weight:'penalty' },
];"""

new_sc_fields = """const SC_FIELDS = [
  { key:'emotional',    label:'Emotional',    short:'Emo', color:'#ff6b8a', weight:2    },
  { key:'relatability', label:'Relatability', short:'Rel', color:'#38bdf8', weight:2    },
  { key:'clarity',      label:'Clarity',      short:'Cla', color:'#fb923c', weight:1.25 },
  { key:'surprise',     label:'Surprise',     short:'Sur', color:'#facc15', weight:1.5  },
  { key:'tension',      label:'Tension',      short:'Ten', color:'#c084fc', weight:1.5  },
  { key:'visual',       label:'Visual',       short:'Vis', color:'#34d399', weight:2.0  },
  { key:'originality',  label:'Originality',  short:'Ori', color:'#f472b6', weight:1.5  },
  { key:'data_ready',   label:'Data Ready',   short:'Dat', color:'#818cf8', weight:'penalty' },
];"""

content = content.replace(old_sc_fields, new_sc_fields)

# ============================================================
# 2. Replace algorithm comment block
# ============================================================
old_comment = """//  SCORE FIELDS 
// Virality algorithm v3:
// - identity_signal removed (curatorial identity lives in selection, not scoring)
// - tension back to 1.0 (no longer carrying identity's weight)
// - visual bumped to 1.25 (Instagram-specific)
// - originality kept at 1.0 (genuinely distinct from surprise)
// - data_ready is soft penalty: vs *= (1 - 0.3*(1 - data_ready/100))
// - denominator 10.75"""

new_comment = """//  SCORE FIELDS 
// Virality algorithm v4:
// - visual bumped to 2.0 (highest correlation with engagement, #1 scroll-stopper)
// - tension bumped to 1.5 (controversy drives shares/comments)
// - originality bumped to 1.5 (uniqueness prevents scroll-past)
// - clarity reduced to 1.25 (low variance, barely differentiates ideas)
// - data_ready penalty steeper: vs *= (1 - 0.5*(1 - data_ready/100))
// - format bonus: choropleths +3, bivariate/dot maps +2
// - denominator 11.75
// Formula: raw = e*2 + r*2 + c*1.25 + s*1.5 + t*1.5 + v*2.0 + o*1.5
//          vs = int(raw/11.75 * penalty) + format_bonus"""

content = content.replace(old_comment, new_comment)

# ============================================================
# 3. Adjust score color thresholds for new distribution
#    v3: mean=69.4, std=7.5  |  v4: mean~68, std~8.5, wider range
#    Shift thresholds down slightly to account for wider spread
# ============================================================
old_sc_color = "const scColor = s => s >= 85 ? '#ff6b8a' : s >= 72 ? '#facc15' : s >= 58 ? '#34d399' : '#444';"

new_sc_color = "const scColor = s => s >= 82 ? '#ff6b8a' : s >= 70 ? '#facc15' : s >= 55 ? '#34d399' : '#444';"

content = content.replace(old_sc_color, new_sc_color)

# ============================================================
# 4. Add format bonus constants and update card V-Score display
#    Show a small "+3" or "+2" badge next to vs when format bonus applies
# ============================================================

# Add FMT_BONUS constant after TYPE_BORDER
old_type_border = "const TYPE_BORDER = { MAP:'#8eedc7', XREF:'#87c3ff', CHART:'#c4a3ff', RANK:'#fcd34d' };"

new_type_border = """const TYPE_BORDER = { MAP:'#8eedc7', XREF:'#87c3ff', CHART:'#c4a3ff', RANK:'#fcd34d' };

// Format bonus for v4 virality algorithm (choropleths are proven viral formats)
const FMT_BONUS = {
  'State choropleth':3, 'County choropleth':3, 'World choropleth':3,
  'Bivariate choropleth':2, 'Dot map':2
};"""

content = content.replace(old_type_border, new_type_border)

# ============================================================
# 5. Update card HTML to show format bonus indicator
#    Add a small "+N" next to the vs score when format bonus applies
# ============================================================
old_vs_display = """<div><div class="vs" style="color:${scColor(d.vs)}">${d.vs}</div><div class="vl">V-Score</div></div>"""

new_vs_display = """<div><div class="vs" style="color:${scColor(d.vs)}">${d.vs}${FMT_BONUS[d.fmt]?'<span class="fmt-bonus">+'+FMT_BONUS[d.fmt]+'</span>':''}</div><div class="vl">V-Score v4</div></div>"""

content = content.replace(old_vs_display, new_vs_display)

# ============================================================
# VERIFY CHANGES
# ============================================================
changes = 0
if 'weight:1.25 },' in content and 'weight:2.0  },' in content:
    changes += 1
    print("  [1] SC_FIELDS weights updated to v4")
else:
    print("  [1] WARNING: SC_FIELDS weights not found/updated")

if 'Virality algorithm v4:' in content:
    changes += 1
    print("  [2] Algorithm comment updated to v4")
else:
    print("  [2] WARNING: Algorithm comment not found/updated")

if '>= 82' in content:
    changes += 1
    print("  [3] Score color thresholds adjusted")
else:
    print("  [3] WARNING: Score color thresholds not found/updated")

if 'FMT_BONUS' in content and "'State choropleth':3" in content:
    changes += 1
    print("  [4] FMT_BONUS constant added")
else:
    print("  [4] WARNING: FMT_BONUS not found/added")

if 'fmt-bonus' in content:
    changes += 1
    print("  [5] Format bonus indicator added to card UI")
else:
    print("  [5] WARNING: Format bonus indicator not found/added")

if 'V-Score v4' in content:
    changes += 1
    print("  [6] V-Score label updated to v4")
else:
    print("  [6] WARNING: V-Score label not updated")

print(f"\n  Total: {changes}/6 changes applied")

if content != original:
    with open('app.js', 'w', encoding='utf-8') as f:
        f.write(content)
    print("  app.js written successfully")
else:
    print("  WARNING: No changes made to app.js!")
