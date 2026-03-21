"""
decode_and_write_batches.py
Run once from D:\projects\mapzimus-board:
    python decode_and_write_batches.py

This decodes the embedded data and writes all EL-FZ batch files.
"""
import base64, gzip, os, subprocess, sys

print("Decoding embedded batch data...")
here = os.path.dirname(os.path.abspath(__file__))

B64 = (
    "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"
)

