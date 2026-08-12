import json, os, re

base = r"C:\Users\guopi\GitHub\courses\future-media-internet\labs\kaggle-demos"

# Comprehensive replacements for ALL Chinese text in matplotlib calls
fixes = {
    "demo2-qoe-optimization.ipynb": {
        "('策略一：固定高码率', '策略二：启发式阈值调节', '策略三：Q-Learning 自适应')":
            "('Fixed Bitrate', 'Heuristic Buffer-Based', 'Q-Learning Adaptive')",
        "f'{title}  |  卡顿 {np.sum(hist[\"stall\"]):.0f} 次'":
            "f'{title} | Stalls: {np.sum(hist[\"stall\"]):.0f}'",
    },
    "demo3-quality-assessment.ipynb": {
        "['原始', '轻微压缩', '中等压缩', '严重压缩']": 
            "['Original', 'Light', 'Medium', 'Heavy']",
        "('模拟不同压缩程度的图像')":
            "('Images at Different Compression Levels')",
        "观察重点：":
            "Key observations:",
        "PSNR 是纯数学指标（像素差），SSIM 模拟人眼感知（关注结构和纹理）":
            "PSNR is pixel-based math. SSIM mimics human perception (structure and texture).",
        "当 PSNR 相近时，SSIM 可能差异很大——因为人眼对结构失真更敏感":
            "Similar PSNR can have very different SSIM - humans are more sensitive to structural distortion.",
    },
    "demo4-neural-compression.ipynb": {
        "plt.title('原始测试图像\\n（棋盘格=高频 | 渐变=低频 | 横线=边缘）')":
            "plt.title('Test Image\\nCheckerboard=High-Freq | Gradient=Low-Freq | Line=Edge')",
        # The levels dict
        "{'无损': 0, '轻度': 1, '中度': 2, '重度': 3}":
            "{'Lossless': 0, 'Light': 1, 'Medium': 2, 'Heavy': 3}",
        # The titles in the loop
        ".set_title(f'JPEG 模拟\\n{label}压缩'":
            ".set_title(f'JPEG\\n{label}'",
        ".set_title(f'神经压缩\\n{label}压缩'":
            ".set_title(f'Neural\\n{label}'",
        # Suptitle
        "('JPEG vs 神经压缩：同一图像在不同压缩程度下的对比\\n（上排：JPEG | 下排：神经压缩）'":
            "('JPEG vs Neural Compression\\n(Top: JPEG | Bottom: Neural)'",
        # Print statements
        "观察重点：":
            "Key observations:",
        "1. JPEG：中度以上出现明显方块（8x8 块边界），高频棋盘格完全丢失":
            "1. JPEG: visible blocks at medium+ compression (8x8 boundaries), checkerboard lost",
        "2. 神经压缩：压缩后保留整体结构，但细节变模糊（降采样→上采样的平滑效果）":
            "2. Neural: preserves structure but details blur (downsample-upsample smoothing)",
        "3. 真实神经压缩使用端到端训练的 CNN/Transformer，比这里的模拟效果好得多":
            "3. Real neural compression uses end-to-end trained CNN/Transformer, much better than this simulation",
    },
}

for fname, replacements in fixes.items():
    path = os.path.join(base, fname)
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    changed = False
    for old, new in replacements.items():
        if old in content:
            content = content.replace(old, new)
            changed = True
            print(f"Fixed {fname}: {old[:50]}...")
        else:
            print(f"MISS {fname}: {old[:50]}...")
    
    if changed:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)

print("\nDone")
