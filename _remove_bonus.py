"""Remove FMT_BONUS from maintain.py and update the formula."""
import re

with open('maintain.py', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Comment out the FMT_BONUS dict (lines 205-212)
text = text.replace(
    """# Format bonus lookup: choropleths get +3, bivariate/dot maps get +2
FMT_BONUS = {
    'State choropleth': 3,
    'County choropleth': 3,
    'World choropleth': 3,
    'Bivariate choropleth': 2,
    'Dot map': 2,
}""",
    """# FMT_BONUS removed: all formats scored equally on idea quality alone
FMT_BONUS = {}  # no format bonus""")

# 2. Update the docstring
text = text.replace(
    "      - format bonus:        NEW  (choropleths +3, bivariate/dot +2)",
    "      - format bonus:        REMOVED (all formats equal)")

text = text.replace(
    """      bonus   = FMT_BONUS.get(fmt, 0)
      vs      = int(base_vs * penalty) + bonus""",
    """      vs      = int(base_vs * penalty)""")

# 3. Update calc_vs function to remove bonus
text = text.replace(
    """        bonus = FMT_BONUS.get(fmt, 0)
        return int(base_vs * penalty) + bonus""",
    """        return int(base_vs * penalty)""")

# 4. Update the reporting line
text = text.replace(
    """        # Format bonus distribution
        bonus_count = sum(1 for line in result.split('\\n')
                         if re.search(r'fmt:"(State choropleth|County choropleth|World choropleth|Bivariate choropleth|Dot map)"', line))
        print(f'    Format bonus applied to: {bonus_count} ideas (choropleths +3, bivariate/dot +2)')""",
    """        print(f'    No format bonus (all formats scored equally)')""")

with open('maintain.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("Done. FMT_BONUS removed from maintain.py")
