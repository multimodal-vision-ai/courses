import json, re

path = r"C:\Users\guopi\GitHub\courses\future-media-internet\labs\kaggle-demos\demo3-quality-assessment.ipynb"
with open(path, "rb") as f:
    raw = f.read()

# Strategy: find any sequence of 2+ backslashes followed by Chinese chars and a quote
# and reduce to a single escaped quote
# Pattern: \\+ followed by CJK character indicates corrupted escape

text = raw.decode("utf-8")

# Fix all occurrences of \\" that appear before/after Chinese characters
# Replace any number of backslashes (2+) before a quote that's near Chinese text
# Simpler: just replace \\\\" and \\" with \" everywhere in source lines

# Actually, let's just fix the known corrupted pattern
# The corruption: \\" where \" was intended
# But we need to NOT fix legitimate \\ sequences

# Let's target: lines that have this pattern near Chinese text
lines = text.split("\n")
for i, line in enumerate(lines):
    if i >= 165 and i <= 180:  # known problematic area
        # Replace double-backslash-quote with escaped-quote
        if '\\\\"' in line:
            # But only if near Chinese text
            if re.search(r'[\u4e00-\u9fff]', line):
                old = line
                line = line.replace('\\\\"', '\\"')
                if line != old:
                    lines[i] = line
                    print(f"Fixed L{i+1}")

text = "\n".join(lines)
with open(path, "w", encoding="utf-8") as f:
    f.write(text)

try:
    with open(path, "r", encoding="utf-8") as f:
        json.load(f)
    print("OK: Valid JSON!")
except json.JSONDecodeError as e:
    print(f"Still broken at L{e.lineno}: {e.msg}")
    ln = e.lineno - 1
    if ln < len(lines):
        print(f"  Content: {lines[ln][:120]}")
