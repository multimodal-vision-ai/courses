import json, os

base = r"C:\Users\guopi\GitHub\courses\future-media-internet\labs\kaggle-demos"
files = [
    "demo2-qoe-optimization.ipynb",
    "demo3-quality-assessment.ipynb",
    "demo4-neural-compression.ipynb",
    "demo5-semantic-communication.ipynb",
]

for fname in files:
    path = os.path.join(base, fname)
    with open(path, "rb") as f:
        raw = f.read()

    lines = raw.decode("utf-8").split("\n")
    fixed_lines = []

    for i, line in enumerate(lines):
        stripped = line.strip()
        # Target: markdown source lines with unescaped inner quotes
        # These start with " and have more than 2 quotes total
        if stripped.startswith('"') and stripped.count('"') > 2:
            content_start = line.index('"') + 1
            if stripped.endswith('",'):
                content_end = line.rindex('",')
            elif stripped.endswith('"'):
                content_end = line.rindex('"')
            else:
                fixed_lines.append(line)
                continue

            prefix = line[:content_start]
            middle = line[content_start:content_end]
            suffix = line[content_end:]

            if '"' in middle:
                middle_fixed = middle.replace('"', '\\"')
                fixed_lines.append(prefix + middle_fixed + suffix)
            else:
                fixed_lines.append(line)
        else:
            fixed_lines.append(line)

    content = "\n".join(fixed_lines)

    try:
        json.loads(content)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"OK: {fname}")
    except json.JSONDecodeError as e:
        print(f"FAIL: {fname} at L{e.lineno}")
        if e.lineno - 1 < len(lines):
            print(f"  Content: {lines[e.lineno-1][:100]}")
