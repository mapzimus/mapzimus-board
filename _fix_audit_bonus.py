"""Remove FMT_BONUS from _full_audit.py too."""
with open('_full_audit.py', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace(
    """FMT_BONUS = {
    'State choropleth': 3, 'County choropleth': 3, 'World choropleth': 3,
    'Bivariate choropleth': 2, 'Dot map': 2,
}""",
    """FMT_BONUS = {}  # no format bonus""")

with open('_full_audit.py', 'w', encoding='utf-8') as f:
    f.write(text)
print("Done. FMT_BONUS removed from _full_audit.py")
