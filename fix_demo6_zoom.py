import json

path = r"C:\Users\guopi\GitHub\courses\future-media-internet\labs\kaggle-demos\demo6-hd-video-impairments.ipynb"
with open(path, "r", encoding="utf-8") as f:
    nb = json.load(f)

nb["cells"][5]["source"] = [
    "# 局部放大对比：聚焦高细节区域（纹理+边缘），加大损伤参数\n"
    "# 选择底部细条纹理区域作为观察窗\n"
    "dy, dx = slice(340, 440), slice(100, 300)  # 100x200 region with fine details\n\n"
    "fig, axes = plt.subplots(3, 3, figsize=(16, 16))\n\n"
    "scenarios = [\n"
    "    ('Original', original[dy, dx]),\n"
    "    ('Loss 20%', np.clip(packet_loss(original, 0.20)[dy, dx], 0, 1)),\n"
    "    ('Jitter 15px', np.clip(jitter(original, 15)[dy, dx], 0, 1)),\n"
    "    ('BW Drop 15%', np.clip(bw_drop(original, 0.15)[dy, dx], 0, 1)),\n"
    "    ('BW 50% + Loss 10%', np.clip(packet_loss(bw_drop(original, 0.5), 0.10)[dy, dx], 0, 1)),\n"
    "    ('Loss 10% + Jitter 10px', np.clip(jitter(packet_loss(original, 0.10), 10)[dy, dx], 0, 1)),\n"
    "]\n\n"
    "# Row 0: Zoomed images\n"
    "# Row 1: Difference from original (abs), amplified 3x\n"
    "# Row 2: Horizontal pixel intensity profile at center row\n\n"
    "for j, (label, img) in enumerate(scenarios):\n"
    "    col = j % 3\n"
    "    row = j // 3\n"
    "    col_actual = col\n"
    "    if j >= 3:\n"
    "        col_actual = col\n"
    "        row = 1\n\n"
    "for j, (label, img) in enumerate(scenarios):\n"
    "    col = j % 3\n"
    "    # Row 0: Zoomed image\n"
    "    axes[0, col].imshow(img)\n"
    "    axes[0, col].set_title(label, fontsize=11, fontweight='bold')\n"
    "    axes[0, col].axis('off')\n"
    "    # Row 1: Difference map (amplified 5x for visibility)\n"
    "    if j > 0:\n"
    "        diff = np.abs(scenarios[0][1] - img) * 5\n"
    "        axes[1, col].imshow(np.clip(diff, 0, 1), cmap='hot')\n"
    "        axes[1, col].set_title(label + ' (Diff x5)', fontsize=10)\n"
    "    else:\n"
    "        axes[1, col].text(0.5, 0.5, 'Reference', ha='center', fontsize=14)\n"
    "    axes[1, col].axis('off')\n"
    "    # Row 2: Horizontal profile at row 50\n"
    "    prof_row = 50\n"
    "    axes[2, col].plot(img[prof_row, :, 0], 'r-', alpha=0.6, linewidth=0.5, label='R')\n"
    "    axes[2, col].plot(img[prof_row, :, 1], 'g-', alpha=0.6, linewidth=0.5, label='G')\n"
    "    axes[2, col].plot(img[prof_row, :, 2], 'b-', alpha=0.6, linewidth=0.5, label='B')\n"
    "    axes[2, col].set_title(label + ' (Profile)', fontsize=10)\n"
    "    axes[2, col].set_ylim(0, 1.1)\n"
    "    if col == 0:\n"
    "        axes[2, col].set_ylabel('Intensity')\n\n"
    "plt.suptitle('Detail Zoom: Artifact Comparison\\n(Row 1: Zoom | Row 2: Error Map x5 | Row 3: Intensity Profile)',\n"
    "             fontsize=14, fontweight='bold')\n"
    "plt.tight_layout()\n"
    "plt.show()\n\n"
    'print("\\n通过三重视角对比网络损伤效果：")\n'
    'print("第一行：直接放大——丢包=灰色块，抖动=水平错位，BW下降=模糊")\n'
    'print("第二行：差异热力图（差异x5）——越亮表示损伤越严重")\n'
    'print("第三行：像素强度剖面——损伤导致信号剧烈波动或平滑化")\n'
    'print("\\n观察：丢包在高细节区最明显，抖动在边缘处最明显，BW下降使整体平滑")\n'
]

with open(path, "w", encoding="utf-8") as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)
print("Demo 6 zoom section rewritten with 3-row comparison")
