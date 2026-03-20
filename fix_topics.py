import re

path = r'D:\projects\mapzimus-board\index.html'
with open(path, 'r', encoding='utf-8') as f:
    html = f.read()

new_block = '  <div class="filter-row" id="topic-row">\n    <span>Topic:</span>\n'
topics = [
    ("health","Health"),("economy","Economy"),("politics","Politics"),
    ("crime","Crime"),("poverty","Poverty"),("housing","Housing"),
    ("education","Education"),("labor","Labor"),("race","Race"),
    ("gender","Gender"),("immigration","Immigration"),("war","War"),
    ("military","Military"),("energy","Energy"),("climate","Climate"),
    ("environment","Environment"),("food","Food"),("agriculture","Agriculture"),
    ("drugs","Drugs"),("guns","Guns"),("finance","Finance"),("trade","Trade"),
    ("inequality","Inequality"),("transportation","Transportation"),
    ("infrastructure","Infrastructure"),("technology","Technology"),
    ("media","Media"),("population","Population"),("international","International"),
    ("democracy","Democracy"),("religion","Religion"),("history","History"),
    ("space","Space"),("data","Data"),
]
for val, label in topics:
    new_block += f'    <button class="fp topic" data-f="topics" data-v="{val}" onclick="toggleTopic(this)">{label}</button>\n'
new_block += '  </div>'

result = re.sub(r'<div class="filter-row" id="topic-row">.*?</div>', new_block, html, flags=re.DOTALL)

if result == html:
    print('ERROR: pattern not matched - checking file encoding')
    # Try latin-1 read
    with open(path, 'r', encoding='latin-1') as f:
        html2 = f.read()
    result2 = re.sub(r'<div class="filter-row" id="topic-row">.*?</div>', new_block, html2, flags=re.DOTALL)
    if result2 != html2:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(result2)
        print('Fixed via latin-1 read -', result2.count('toggleTopic'), 'topic buttons')
    else:
        print('Still no match - manual inspection needed')
else:
    with open(path, 'w', encoding='utf-8') as f:
        f.write(result)
    print('Done -', result.count('toggleTopic'), 'topic buttons written')
