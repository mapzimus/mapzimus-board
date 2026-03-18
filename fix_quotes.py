"""
fix_quotes.py - Remove embedded double quotes that break JS string parsing.
The problem: curly double quotes (U+201C, U+201D) were replaced with straight
double quotes, which then act as string terminators inside JS field values.
Fix: replace any straight double quote inside a JS string value with nothing.
"""
import re

with open('data.js', 'r', encoding='utf-8') as f:
    c = f.read()

before_len = len(c)

# Strategy: parse field by field and strip internal double quotes from string values.
# Simpler approach: find the specific broken pattern and fix it.
# The broken ideas have a " in the middle of a sub:"..." or title:"..." value.
# We can detect this by finding ", that is preceded by a word char (not a field boundary).

# Replace all occurrences of a double quote that appears mid-string:
# Pattern: word_char + " + space  OR  space + " + word_char  (inside a JS value)
# But we must NOT touch the field delimiter quotes themselves.

# Best approach: reconstruct each idea line, scanning for broken strings
fixed_lines = []
fixes = 0
for line in c.split('\n'):
    # Each idea is one line. Find all string values and strip internal quotes.
    # JS field format: fieldname:"value" - the value is between :" and the next ",
    # We want to remove any " that appears INSIDE a value (not at start/end of value).
    
    # Walk through and fix: after a field-opening :" we are inside a string until next "
    # that's followed by , or } 
    result = []
    i = 0
    in_string = False
    while i < len(line):
        ch = line[i]
        if not in_string:
            result.append(ch)
            # Check if we're opening a JS string value: character :" 
            if ch == '"':
                in_string = True
        else:
            # Inside a string - look for the closing "
            # Closing " is followed by , or } or end of line
            if ch == '"':
                # Is this a closing delimiter or an embedded bad quote?
                next_ch = line[i+1] if i+1 < len(line) else ''
                if next_ch in (',', '}', ']', ''):
                    # This is the closing delimiter - keep it
                    result.append(ch)
                    in_string = False
                else:
                    # This is an embedded bad quote - remove it
                    fixes += 1
                    # Don't append - skip it
            else:
                result.append(ch)
        i += 1
    
    fixed_line = ''.join(result)
    fixed_lines.append(fixed_line)

c_fixed = '\n'.join(fixed_lines)

with open('data.js', 'w', encoding='utf-8') as f:
    f.write(c_fixed)

print(f'Fixed {fixes} embedded quotes.')
print(f'File size: {round(len(c_fixed)/1024, 1)} KB')
