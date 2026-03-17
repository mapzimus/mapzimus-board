# GitHub Pages Setup — Run these 3 commands

# 1. Go to https://github.com/new
#    Name: mapzimus-board
#    Visibility: Public
#    Don't initialize with README
#    Click "Create repository"

# 2. Then run these in PowerShell from D:\projects\mapzimus-board:

cd D:\projects\mapzimus-board
git remote add origin https://github.com/mapzimus/mapzimus-board.git
git branch -M main
git push -u origin main

# 3. Then enable GitHub Pages:
#    Go to: https://github.com/mapzimus/mapzimus-board/settings/pages
#    Source: Deploy from a branch
#    Branch: main / (root)
#    Click Save

# Your board will be live at:
# https://mapzimus.github.io/mapzimus-board/

# To update after changes (e.g. adding new ideas to data.js):
cd D:\projects\mapzimus-board
git add .
git commit -m "Update ideas"
git push
