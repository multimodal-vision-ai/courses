import json

path = r"C:\Users\guopi\GitHub\courses\future-media-internet\labs\kaggle-demos\demo5-semantic-communication.ipynb"
with open(path, "r", encoding="utf-8") as f:
    nb = json.load(f)

print(f"Total cells: {len(nb['cells'])}")
for i, cell in enumerate(nb['cells']):
    src = cell.get("source", [])
    first = src[0][:80] if src else "(empty)"
    print(f"  [{i}] {cell['cell_type']:8s} | {first}...")
