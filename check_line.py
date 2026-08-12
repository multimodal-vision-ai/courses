path = r"C:\Users\guopi\GitHub\courses\future-media-internet\labs\kaggle-demos\demo3-quality-assessment.ipynb"
with open(path, "rb") as f:
    raw = f.read()

# Find line 169 (0-indexed: 168) and show its bytes
lines = raw.split(b"\n")
line = lines[168]
print(f"Line 169 bytes ({len(line)} bytes):")
print(line[:200])

# The issue: \\" in the raw file appears as two backslash bytes (0x5C 0x5C) then quote (0x22)
# Count occurrences
cnt = line.count(b'\\\\')
print(f"\nFound {cnt} double-backslash sequences")
