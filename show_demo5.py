import json

path = r"C:\Users\guopi\GitHub\courses\future-media-internet\labs\kaggle-demos\demo5-semantic-communication.ipynb"
with open(path, "r", encoding="utf-8") as f:
    nb = json.load(f)

for i, cell in enumerate(nb['cells']):
    if cell['cell_type'] == 'code':
        print(f"\n===== CELL {i} =====")
        src = ''.join(cell.get('source', []))
        print(src[:500])
        if len(src) > 500:
            print("... (truncated)")
