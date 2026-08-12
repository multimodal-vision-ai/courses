import json

path = r"C:\Users\guopi\GitHub\courses\future-media-internet\labs\kaggle-demos\demo6-hd-video-impairments.ipynb"
with open(path, "r", encoding="utf-8") as f:
    nb = json.load(f)

nb["cells"][5]["source"] = [
    "# 局部放大对比：高损伤 + 差异热力图，让效果一目了然\n"
    "# 选取底部细条纹理区域（高频细节最多的地方）\n"
    "dy, dx = slice(340, 440), slice(60, 260)\n"
    "ref = original[dy, dx]\n\n"
    "# 三组高损伤场景\n"
    "scenarios = [\n"
    "    ('Packet Loss 20%', np.clip(packet_loss(original, 0.20)[dy, dx], 0, 1)),\n"
    "    ('Jitter 20px', np.clip(jitter(original, 20)[dy, dx], 0, 1)),\n"
    "    ('BW Drop 15%', np.clip(bw_drop(original, 0.15)[dy, dx], 0, 1)),\n"
    "]\n\n"
    "fig, axes = plt.subplots(3, 4, figsize=(18, 14))\n\n"
    "# Row 0: Images\n"
    "axes[0, 0].imshow(ref)\n"
    "axes[0, 0].set_title('Original (Reference)', fontsize=12, fontweight='bold')\n"
    "for j, (label, img) in enumerate(scenarios):\n"
    "    axes[0, j+1].imshow(img)\n"
    "    axes[0, j+1].set_title(label, fontsize=12, fontweight='bold')\n\n"
    "# Row 1: Difference maps (amplified 5x, hot colormap)\n"
    "axes[1, 0].axis('off')\n"
    "for j, (label, img) in enumerate(scenarios):\n"
    "    diff = np.abs(ref - img) * 5  # amplify for visibility\n"
    "    im = axes[1, j+1].imshow(np.clip(diff, 0, 1), cmap='hot')\n"
    "    axes[1, j+1].set_title(label + ' Error x5', fontsize=11)\n"
    "    plt.colorbar(im, ax=axes[1, j+1], fraction=0.046)\n\n"
    "# Row 2: Zoom into a 40x40 patch for pixel-level detail\n"
    "px, py = 30, 120  # pick a spot with fine detail\n"
    "sz = 20\n"
    "axes[2, 0].imshow(ref[px:px+sz, py:py+sz], interpolation='nearest')\n"
    "axes[2, 0].set_title('Original (pixel-level)', fontsize=11)\n"
    "for j, (label, img) in enumerate(scenarios):\n"
    "    axes[2, j+1].imshow(img[px:px+sz, py:py+sz], interpolation='nearest')\n"
    "    axes[2, j+1].set_title(label + ' (pixel)', fontsize=11)\n\n"
    "for ax in axes.flat:\n"
    "    ax.axis('off')\n\n"
    "plt.suptitle('Network Impairments: Three-Level Detail Comparison', fontsize=14, fontweight='bold')\n"
    "plt.tight_layout()\n"
    "plt.show()\n\n"
    'print("\\n三重视角对比网络损伤：")\n'
    'print("第一行：原始图像——丢包出现灰色方块，抖动导致水平错位，BW下降导致模糊")\n'
    'print("第二行：差异热力图（差异x5）——越亮=损伤越重，可清晰定位受损区域")\n'
    'print("第三行：像素级放大——可以看到单个像素被如何破坏")\n'
]

with open(path, "w", encoding="utf-8") as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)
print("Demo 6 zoom fixed")
