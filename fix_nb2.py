import json, os

base = r"C:\Users\guopi\GitHub\courses\future-media-internet\labs\kaggle-demos"

# The core problem: ASCII double quotes inside JSON string values
# We need to find and escape them. Let's do it by reading each file,
# finding lines that are part of JSON string arrays, and escaping inner quotes.

for fname in ["demo2-qoe-optimization.ipynb", "demo3-quality-assessment.ipynb", "demo5-semantic-communication.ipynb"]:
    path = os.path.join(base, fname)
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    fixed = False
    for i, line in enumerate(lines):
        stripped = line.strip()
        # Look for lines that start with a JSON string value and contain unescaped inner quotes
        # Pattern: starts with " and ends with ",\n or "\n or just "
        if stripped.startswith('"') and ('"' in stripped[1:-2] or stripped.count('"') > 2):
            # This line has inner quotes that need escaping
            # Strategy: keep the first and last " as delimiters, escape all others
            first_q = line.index('"')
            # Find the last quote that's part of the JSON structure
            # Usually the line ends with ",\n  or  "\n  or  "
            if stripped.endswith('",'):
                last_q = line.rindex('",')
            elif stripped.endswith('"'):
                last_q = line.rindex('"')
            else:
                continue
            
            prefix = line[:first_q+1]  # include first "
            middle = line[first_q+1:last_q]
            suffix = line[last_q:]
            
            # Escape inner quotes
            middle_fixed = middle.replace('"', '\\"')
            if middle != middle_fixed:
                lines[i] = prefix + middle_fixed + suffix
                fixed = True
                print(f"Fixed {fname} L{i+1}: {lines[i][:100].rstrip()}...")

    if fixed:
        content = "".join(lines)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        
        try:
            with open(path, "r", encoding="utf-8") as f:
                json.load(f)
            print(f"  -> {fname}: Valid JSON!")
        except json.JSONDecodeError as e:
            print(f"  -> {fname}: Still broken at L{e.lineno}")
    else:
        print(f"{fname}: No fixes applied")
