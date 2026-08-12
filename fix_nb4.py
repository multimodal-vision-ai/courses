import json, os, re, nbformat

base = r"C:\Users\guopi\GitHub\courses\future-media-internet\labs\kaggle-demos"
files = [
    "demo2-qoe-optimization.ipynb",
    "demo3-quality-assessment.ipynb",
    "demo4-neural-compression.ipynb",
    "demo5-semantic-communication.ipynb",
]

for fname in files:
    path = os.path.join(base, fname)
    
    # Read raw content and fix JSON structure issues
    with open(path, "r", encoding="utf-8") as f:
        raw = f.read()
    
    # Fix: find source content lines (indented 4+ spaces, start with ")
    # and escape any inner ASCII double quotes
    lines = raw.split("\n")
    fixed = []
    for line in lines:
        # Check if this is a source content line (not JSON structure)
        # Source lines: start with 4+ spaces, then a quote
        stripped = line.lstrip()
        indent = len(line) - len(stripped)
        
        if indent >= 4 and stripped.startswith('"') and '":' not in stripped[:20]:
            # This is likely a source content line
            # Find the opening and closing structural quotes
            # The line format is: <spaces>"content", or <spaces>"content"
            q1 = line.index('"', indent)
            
            # Find the last structural quote
            if stripped.endswith('",'):
                q2 = line.rindex('",')
            elif stripped.endswith('"'):
                q2 = line.rindex('"')
            else:
                fixed.append(line)
                continue
            
            prefix = line[:q1+1]
            middle = line[q1+1:q2]
            suffix = line[q2:]
            
            # Escape inner double quotes  
            if '"' in middle:
                middle = middle.replace('"', '\\"')
                line = prefix + middle + suffix
        
        fixed.append(line)
    
    raw = "\n".join(fixed)
    
    # Also fix double-backslash issues: \\" -> \"
    raw = raw.replace('\\\\"', '\\"')
    
    # Now try to parse and rewrite with nbformat
    try:
        nb = nbformat.reads(raw, as_version=4)
        nbformat.write(nb, path)
        print(f"OK: {fname}")
    except Exception as e:
        print(f"FAIL: {fname} - {e}")
