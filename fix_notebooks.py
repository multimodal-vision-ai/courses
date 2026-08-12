import json, os, re

base = r"C:\Users\guopi\GitHub\courses\future-media-internet\labs\kaggle-demos"

# Read each broken notebook as raw text and fix common corruption patterns
files_to_fix = [
    "demo2-qoe-optimization.ipynb",
    "demo3-quality-assessment.ipynb",
    "demo4-neural-compression.ipynb",
    "demo5-semantic-communication.ipynb",
]

for fname in files_to_fix:
    path = os.path.join(base, fname)
    with open(path, "r", encoding="utf-8") as fp:
        content = fp.read()

    # Fix 1: Replace \u201c (left Chinese quote) and \u201d (right Chinese quote) 
    # that appear inside JSON strings with escaped ASCII double quotes
    # These are valid Unicode but seem to cause issues in Kaggle's parser
    content = content.replace("\u201c", '\\"')
    content = content.replace("\u201d", '\\"')

    # Fix 2: Replace double-escaped backslashes (\\\\") that PowerShell created
    # In JSON source, \" should appear as \" not \\"
    # But we need to be careful - let's only fix the known pattern
    content = content.replace('\\\\"', '\\"')

    with open(path, "w", encoding="utf-8") as fp:
        fp.write(content)

    # Verify
    try:
        with open(path, "r", encoding="utf-8") as fp:
            json.load(fp)
        print(f"OK: {fname}")
    except json.JSONDecodeError as e:
        print(f"STILL BROKEN: {fname} - {e}")
        # Show the problematic line
        lines = content.split("\n")
        ln = e.lineno - 1
        print(f"  Line {e.lineno}: {lines[ln][:120]}")

print("\nDone")
