import json, os

base = r"C:\Users\guopi\GitHub\courses\future-media-internet\labs\kaggle-demos"

# Fix demo4
with open(os.path.join(base, "demo4-neural-compression.ipynb"), "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace(
    "('原始测试图像\\n（棋盘格=高频 | 渐变=低频 | 横线=边缘）')",
    "('Test Image\\n(Checkerboard=High-Freq | Gradient=Low-Freq | Line=Edge)')"
)
content = content.replace(
    "f'JPEG 模拟\\n{label}压缩'",
    "f'JPEG\\n{label}'"
)
content = content.replace(
    "f'神经压缩\\n{label}压缩'",
    "f'Neural\\n{label}'"
)
content = content.replace(
    "'JPEG vs 神经压缩：同一图像在不同压缩程度下的对比\\n（上排：JPEG | 下排：神经压缩）'",
    "'JPEG vs Neural Compression\\n(Top: JPEG | Bottom: Neural)'"
)

with open(os.path.join(base, "demo4-neural-compression.ipynb"), "w", encoding="utf-8") as f:
    f.write(content)
print("demo4 fixed")

# Check demo5 for any remaining Chinese in plots
with open(os.path.join(base, "demo5-semantic-communication.ipynb"), "r", encoding="utf-8") as f:
    nb = json.load(f)

for i, cell in enumerate(nb['cells']):
    src = ''.join(cell.get('source', []))
    for line in src.split('\n'):
        if any('\u4e00' <= c <= '\u9fff' for c in line):
            if any(kw in line for kw in ['title', 'label', 'xlabel', 'ylabel', 'suptitle', 'set_title', 'plt.']):
                print(f"demo5 cell {i}: {line.strip()[:120]}")

print("Done")
