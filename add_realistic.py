import json, os

base = r"C:\Users\guopi\GitHub\courses\future-media-internet\labs\kaggle-demos"

# ===== DEMO 6: Add realistic frame section =====
path = os.path.join(base, "demo6-hd-video-impairments.ipynb")
with open(path, "r", encoding="utf-8") as f:
    nb = json.load(f)

# Add cell 7: realistic scene
nb["cells"].append({
    "cell_type": "code", "execution_count": None, "metadata": {}, "outputs": [],
    "source": [
        "# 模拟真实视频场景：自然风景 + 文字叠加（类新闻画面）\n"
        "def create_realistic_scene():\n"
        "    H, W = 360, 640\n"
        "    frame = np.zeros((H, W, 3), dtype=np.float32)\n"
        "    # 天空渐变\n"
        "    for y in range(H//2):\n"
        "        t = y / (H//2)\n"
        "        frame[y, :] = (0.3+0.4*t, 0.4+0.3*t, 0.6+0.3*t)\n"
        "    # 远山轮廓\n"
        "    import random; random.seed(42)\n"
        "    for x in range(W):\n"
        "        h = int(H*0.35 + np.sin(x*0.01)*20 + np.sin(x*0.03)*15)\n"
        "        frame[h:H//2+30, x] = (0.15, 0.35, 0.15)\n"
        "    # 地面纹理\n"
        "    for y in range(H//2+30, H):\n"
        "        v = 0.2 + 0.15 * np.sin(y*0.05) * np.sin(y*0.02)\n"
        "        frame[y, :] = (v, 0.25+v*0.3, v*0.5)\n"
        "    # 建筑群\n"
        "    buildings = [(50,80,120,0.6),(180,50,200,0.5),(320,100,150,0.45),(450,70,170,0.55)]\n"
        "    for bx, bw, bh, c in buildings:\n"
        "        top = H//2+30 - bh\n"
        "        frame[top:H//2+30, bx:bx+bw] = (c*0.7, c*0.6, c*0.5)\n"
        "        # 窗户\n"
        "        for wy in range(top+5, top+bh-5, 15):\n"
        "            for wx in range(bx+5, bx+bw-5, 12):\n"
        "                frame[wy:wy+8, wx:wx+6] = (0.8, 0.85, 0.7) if (wx+wy)%30<15 else (0.3, 0.3, 0.2)\n"
        "    # 文字叠加（模拟新闻标题栏）\n"
        "    frame[H-40:H-10, 20:W-20] = (0.05, 0.05, 0.1)\n"
        "    frame[H-35:H-15, 30:W-30] = (0.9, 0.9, 0.9)\n"
        "    return frame\n\n"
        "scene = create_realistic_scene()\n"
        "fig, ax = plt.subplots(figsize=(12, 7))\n"
        "ax.imshow(np.clip(scene, 0, 1))\n"
        "ax.set_title('Simulated Video Scene (Landscape + Buildings + Text Overlay)')\n"
        "ax.axis('off')\n"
        "plt.show()\n"
    ]
})

# Add cell 8: impairments on realistic scene
nb["cells"].append({
    "cell_type": "code", "execution_count": None, "metadata": {}, "outputs": [],
    "source": [
        "# 在真实感场景上应用网络损伤\n"
        "np.random.seed(123)\n"
        "impairments_real = [\n"
        "    ('Original', lambda f: f),\n"
        "    ('Loss 10%', lambda f: packet_loss(f, 0.10)),\n"
        "    ('Jitter 6px', lambda f: jitter(f, 6)),\n"
        "    ('BW Drop 30%', lambda f: bw_drop(f, 0.30)),\n"
        "]\n\n"
        "fig, axes = plt.subplots(1, 4, figsize=(18, 5))\n"
        "for j, (label, func) in enumerate(impairments_real):\n"
        "    imp = func(scene)\n"
        "    axes[j].imshow(np.clip(imp, 0, 1))\n"
        "    axes[j].set_title(label, fontsize=12, fontweight='bold')\n"
        "    axes[j].axis('off')\n"
        "plt.suptitle('Realistic Scene: Network Impairment Comparison', fontsize=14, fontweight='bold')\n"
        "plt.tight_layout()\n"
        "plt.show()\n\n"
        'print("\\n在实际视频传输中，网络损伤的影响体现在：")\n'
        'print("1. 丢包 -> 画面中出现灰色方块（错误隐藏后的残留）")\n'
        'print("2. 抖动 -> 画面行错位，在快速运动场景中最明显")\n'
        'print("3. 带宽下降 -> 整体清晰度降低，细节丢失")\n'
        'print("4. 真实系统中三种损伤往往同时发生，互相叠加")\n'
    ]
})

with open(path, "w", encoding="utf-8") as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)
print("Demo 6 enhanced with realistic scene")

# ===== DEMO 7: Add realistic VR scene =====
path = os.path.join(base, "demo7-vr-video-impairments.ipynb")
with open(path, "r", encoding="utf-8") as f:
    nb = json.load(f)

# Add realistic VR scene cell
nb["cells"].append({
    "cell_type": "code", "execution_count": None, "metadata": {}, "outputs": [],
    "source": [
        "# 模拟更真实的 VR 全景场景\n"
        "def create_realistic_vr():\n"
        "    EH, EW = 480, 960\n"
        "    frame = np.zeros((EH, EW, 3), dtype=np.float32)\n"
        "    # 天空\n"
        "    for y in range(EH//2):\n"
        "        t = y/(EH//2)\n"
        "        frame[y, :] = (0.2+0.5*t, 0.3+0.4*t, 0.5+0.4*t)\n"
        "    # 远山（起伏轮廓）\n"
        "    for x in range(EW):\n"
        "        h = int(EH*0.35 + np.sin(x*0.008)*30 + np.sin(x*0.02)*20 + np.sin(x*0.05)*10)\n"
        "        frame[h:EH//2+20, x] = (0.12, 0.28, 0.12)\n"
        "    # 地面\n"
        "    for y in range(EH//2+20, EH):\n"
        "        v = 0.18 + 0.1*np.sin(y*0.04)\n"
        "        frame[y, :] = (v, 0.22+v*0.4, v*0.4)\n"
        "    # 建筑物散布在 360 空间中\n"
        "    import random; random.seed(7)\n"
        "    for _ in range(12):\n"
        "        bx = random.randint(20, EW-100)\n"
        "        bw = random.randint(40, 90)\n"
        "        bh = random.randint(50, 130)\n"
        "        by = int(EH*0.35 - bh + random.randint(-20, 30))\n"
        "        c = random.uniform(0.3, 0.7)\n"
        "        by = max(0, by)\n"
        "        top = min(by, EH//2+20)\n"
        "        bot = min(top+bh, EH//2+20)\n"
        "        frame[top:bot, bx:bx+bw] = (c*0.6, c*0.5, c*0.4)\n"
        "    # 中心区域标注（用户注视热点）\n"
        "    cx, cy = EW//2, EH//2\n"
        "    rr = 100\n"
        "    for y in range(cy-rr, cy+rr):\n"
        "        for x in range(cx-rr, cx+rr):\n"
        "            if (x-cx)**2 + (y-cy)**2 < rr**2:\n"
        "                if 0 <= y < EH and 0 <= x < EW:\n"
        "                    frame[y, x] *= 1.2\n"
        "    return np.clip(frame, 0, 1)\n\n"
        "real_vr = create_realistic_vr()\n"
        "fig, ax = plt.subplots(figsize=(14, 7))\n"
        "ax.imshow(real_vr)\n"
        "ax.set_title('Realistic VR Equirectangular Scene')\n"
        "ax.axis('off')\n"
        "plt.show()\n"
        'print("全景场景包含：天空、远山、地面、散布的建筑群、中心注视热点")\n'
    ]
})

# Add impairments on realistic VR
nb["cells"].append({
    "cell_type": "code", "execution_count": None, "metadata": {}, "outputs": [],
    "source": [
        "# 在真实感 VR 场景上对比不同网络损伤\n"
        "np.random.seed(99)\n"
        "# 裁切视场角区域\n"
        "cy, cx = EH//2, EW//2\n"
        "fov = real_vr[cy-135:cy+135, cx-240:cx+240]\n\n"
        "fig, axes = plt.subplots(1, 4, figsize=(18, 5))\n"
        "scenarios = [\n"
        "    ('Ideal VR', fov),\n"
        "    ('Loss 5%', packet_loss(fov, 0.05)),\n"
        "    ('Jitter 3px', jitter(fov, 3)),\n"
        "    ('BW 50% + Loss 5%', packet_loss(bw_drop(fov, 0.5), 0.05)),\n"
        "]\n"
        "for j, (label, img) in enumerate(scenarios):\n"
        "    axes[j].imshow(np.clip(img, 0, 1))\n"
        "    axes[j].set_title(label, fontsize=12, fontweight='bold')\n"
        "    axes[j].axis('off')\n"
        "plt.suptitle('VR Viewport: Network Impairment Impact', fontsize=14, fontweight='bold')\n"
        "plt.tight_layout()\n"
        "plt.show()\n\n"
        'print("\\nVR 体验对网络的严苛要求总结：")\n'
        'print("1. 5% 丢包在 HD 中可接受，在 VR 中已明显破坏体验")\n'
        'print("2. 3px 抖动对 480px 宽视场角影响显著（占比 0.6%）")\n'
        'print("3. 带宽下降 50% 叠加丢包时，VR 画面已不可用")\n'
        'print("4. 这解释了为什么 VR 需要 5G/WiFi 6E 级别的网络支撑")\n'
    ]
})

with open(path, "w", encoding="utf-8") as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)
print("Demo 7 enhanced with realistic scene")
