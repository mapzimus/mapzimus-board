# RUN_MORNING.ps1 — Master overnight batch execution script
# Run this when you wake up. It executes each batch, runs maintain.py after each,
# and stops on any error. Only push to GitHub after everything passes.
#
# Usage:
#   cd D:\projects\mapzimus-board
#   .\RUN_MORNING.ps1

$py = "C:\Users\mhowe\AppData\Local\Python\pythoncore-3.14-64\python.exe"
$ErrorActionPreference = "Stop"

Set-Location "D:\projects\mapzimus-board"

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  MAPZIMUS BOARD - MORNING BATCH RUN" -ForegroundColor Cyan
Write-Host "  $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
# --- Pre-flight check ---
Write-Host "[PRE-FLIGHT] Running maintain.py to verify clean state..." -ForegroundColor Yellow
& $py maintain.py
if ($LASTEXITCODE -ne 0) {
    Write-Host "[ERROR] maintain.py failed on pre-flight check. Fix data.js first." -ForegroundColor Red
    exit 1
}
Write-Host "[PRE-FLIGHT] Clean state confirmed.`n" -ForegroundColor Green

# Helper function to run a batch + maintain
function Run-Batch {
    param([string]$Name, [string]$Desc)
    Write-Host "[$Name] $Desc" -ForegroundColor Yellow
    & $py "$Name.py"
    if ($LASTEXITCODE -ne 0) {
        Write-Host "[ERROR] $Name.py failed. Stopping." -ForegroundColor Red
        exit 1
    }
    Write-Host "[$Name] Running maintain.py..." -ForegroundColor Yellow
    & $py maintain.py
    if ($LASTEXITCODE -ne 0) {
        Write-Host "[ERROR] maintain.py failed after $Name. Check data.js." -ForegroundColor Red
        exit 1
    }
    Write-Host "[$Name] Complete and validated.`n" -ForegroundColor Green
}
# --- Execute all batches in order ---
Run-Batch "BATCH_GB" "Injecting 111 ideas from FiveThirtyEight, FBI, CPI, Sage, OWID, Schools, MBTA, F: drive..."
Run-Batch "BATCH_GD" "Injecting 34 cross-dataset XREF ideas..."
Run-Batch "BATCH_GE" "Injecting 67 ideas from OWID deep dive + HSUS historical..."
Run-Batch "BATCH_GF" "Injecting ~90 ideas: US deep dive + gap-filling..."
Run-Batch "BATCH_GG" "Injecting ~53 high-virality, controversy, and shock value ideas..."
Run-Batch "BATCH_GH" "Injecting 38 ideas: Europe, Oceania, bivariate choropleth, dot map gap-fill..."
Run-Batch "BATCH_GI" "Injecting ~60 cross-reference mega-batch ideas..."

# --- Final validation ---
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  ALL 7 BATCHES COMPLETE" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "[FINAL] Running full_audit.py..." -ForegroundColor Yellow
& $py full_audit.py 2>$null
Write-Host ""
Write-Host "[NEXT STEPS]" -ForegroundColor Green
Write-Host "  1. Review the board at: https://mapzimus.github.io/mapzimus-board" -ForegroundColor White
Write-Host "  2. If everything looks good, commit and push:" -ForegroundColor White
Write-Host "     git add ." -ForegroundColor Gray
Write-Host '     git commit -m "Add overnight batch ideas: GB-GI (~450 new ideas from multi-source deep dive)"' -ForegroundColor Gray
Write-Host "     git push" -ForegroundColor Gray
Write-Host ""
Write-Host "Done at $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')" -ForegroundColor Cyan
