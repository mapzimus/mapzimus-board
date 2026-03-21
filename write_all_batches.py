"""
write_all_batches.py  — run once, writes all EL-FZ batch files
Usage:  cd D:\projects\mapzimus-board
        python write_all_batches.py
"""
import os, sys
dest = os.path.dirname(os.path.abspath(__file__))
written = 0
skipped = 0

