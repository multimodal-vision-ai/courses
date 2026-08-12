import json, os

base = r"C:\Users\guopi\GitHub\courses\future-media-internet\labs\kaggle-demos"

# ===== FIX DEMO 7 =====
path = os.path.join(base, "demo7-vr-video-impairments.ipynb")
with open(path, "r", encoding="utf-8") as f:
    nb = json.load(f)

# Fix cell 3: packet_loss and jitter use frame.shape instead of global EH/EW
nb["cells"][3]["source"] = [
    "# Network impairment simulators (frame-size-aware)\n"
    "def packet_loss(frame, rate):\n"
    "    result = frame.copy()\n"
    "    H, W = frame.shape[:2]\n"
    "    bh, bw = 24, 40\n"
    "    nb_h, nb_w = H//bh, W//bw\n"
    "    mask = np.random.random((nb_h, nb_w)) < rate\n"
    "    for i in range(nb_h):\n"
    "        for j in range(nb_w):\n"
    "            if mask[i,j]:\n"
    "                i1, i2 = i*bh, min((i+1)*bh, H)\n"
    "                j1, j2 = j*bw, min((j+1)*bw, W)\n"
    "                result[i1:i2, j1:j2] = 0.5\n"
    "    return result\n\n"
    "def jitter(frame, px):\n"
    "    result = frame.copy()\n"
    "    H = frame.shape[0]\n"
    "    shifts = (np.random.randn(H)*px).astype(int)\n"
    "    for y in range(H):\n"
    "        result[y] = np.roll(result[y], shifts[y], axis=0)\n"
    "    return result\n\n"
    "def bw_drop(frame, scale):\n"
    "    H, W = frame.shape[:2]\n"
    "    h2, w2 = int(H*scale), int(W*scale)\n"
    "    low = ndimage.zoom(frame, (scale,scale,1), order=1)\n"
    "    up = ndimage.zoom(low, (1/scale,1/scale,1), order=1)\n"
    "    return np.clip(up[:H,:W], 0, 1)\n\n"
    'print("Simulators ready (frame-size-aware)")\n'
]

# Fix cell 4: replace comparison with cleaner version + Chinese
nb["cells"][4]["source"] = [
    "# 对比：相同网络损伤对 VR 和 HD 的不同影响\n"
    "np.random.seed(42)\n\n"
    "# 从 VR 全景帧中裁切视场角区域（模拟头显中实际看到的画面）\n"
    "fov_h, fov_w = 270, 480\n"
    "cy, cx = EH//2, EW//2\n"
    "hd_crop = vr_frame[cy-fov_h//2:cy+fov_h//2, cx-fov_w//2:cx+fov_w//2]\n\n"
    "fig, axes = plt.subplots(3, 3, figsize=(16, 12))\n\n"
    "impairments = [\n"
    "    ('Original', lambda f: f),\n"
    "    ('Loss 5%', lambda f: packet_loss(f, 0.05)),\n"
    "    ('Jitter 5px', lambda f: jitter(f, 5)),\n"
    "]\n\n"
    "for j, (label, func) in enumerate(impairments):\n"
    "    # 完整 VR 帧\n"
    "    axes[0, j].imshow(np.clip(func(vr_frame), 0, 1))\n"
    "    axes[0, j].set_title('Full VR: {}'.format(label), fontsize=11)\n"
    "    axes[0, j].axis('off')\n"
    "    # 视场角裁切（用户实际看到的部分）\n"
    "    crop = np.clip(func(hd_crop), 0, 1)\n"
    "    axes[1, j].imshow(crop)\n"
    "    axes[1, j].set_title('FOV Crop: {}'.format(label), fontsize=11)\n"
    "    axes[1, j].axis('off')\n"
    "    # 中心物体放大\n"
    "    ch, cw = crop.shape[0]//2, crop.shape[1]//2\n"
    "    r = 60\n"
    "    z = crop[max(0,ch-r):min(crop.shape[0],ch+r), max(0,cw-r):min(crop.shape[1],cw+r)]\n"
    "    axes[2, j].imshow(z)\n"
    "    axes[2, j].set_title('Center Zoom: {}'.format(label), fontsize=11)\n"
    "    axes[2, j].axis('off')\n\n"
    "plt.suptitle('VR vs HD: Same Impairment, Different Impact', fontsize=14, fontweight='bold')\n"
    "plt.tight_layout()\n"
    "plt.show()\n\n"
    'print("观察要点：")\n'
    'print("1. VR 全景帧中，损伤在画面各处可见")\n'
    'print("2. 在视场角裁切（用户实际观看区域）中，损伤更加集中和明显")\n'
    'print("3. 中心物体放大后，即使 5% 的丢包也会破坏关键视觉信息")\n'
    'print("4. VR 需要比 HD 高 4-8 倍的带宽才能达到同等感知质量")\n'
]

# Fix cell 5
nb["cells"][5]["source"] = [
    "# VR 时延敏感性对比\n"
    "def frame_drop_sim(frame, drop_ratio):\n"
    "    return frame * (1.0 - drop_ratio * 0.3)\n\n"
    "fig, axes = plt.subplots(1, 3, figsize=(16, 5))\n\n"
    "axes[0].imshow(np.clip(vr_frame, 0, 1))\n"
    "axes[0].set_title('Smooth VR (60 fps)', fontsize=12, fontweight='bold')\n"
    "axes[0].axis('off')\n\n"
    "axes[1].imshow(np.clip(frame_drop_sim(vr_frame, 0.5), 0, 1))\n"
    "axes[1].set_title('Frame Drops 50%\\nMotion sickness risk!', fontsize=12)\n"
    "axes[1].axis('off')\n\n"
    "axes[2].imshow(np.clip(packet_loss(bw_drop(vr_frame, 0.5), 0.1), 0, 1))\n"
    "axes[2].set_title('Severe: BW 50% + Loss 10%\\nVR experience broken', fontsize=12)\n"
    "axes[2].axis('off')\n\n"
    "plt.suptitle('VR Quality Degradation', fontsize=14, fontweight='bold')\n"
    "plt.tight_layout()\n"
    "plt.show()\n\n"
    'print("\\n为什么 VR 对网络损伤更敏感：")\n'
    'print("1. 更高分辨率（4K-8K vs 1080p）-> 每帧数据量更大")\n'
    'print("2. 超低时延要求（<20ms vs 流媒体 2-5s 缓冲）")\n'
    'print("3. 帧丢失直接导致运动眩晕（前庭-视觉冲突）")\n'
    'print("4. 等距矩形投影在两极浪费大量码率")\n'
    'print("5. 注视点渲染假设传输完美无缺")\n'
]

# Fix cell 6 - markdown explanations
nb["cells"][6]["source"] = [
    "## 关键结论\n\n"
    "- 5% 丢包在 HD 中几乎不可察觉，在 VR 中却明显可见\n"
    "- 等距矩形投影在画面顶部/底部（极点）放大了压缩伪影\n"
    "- VR 中的帧丢失直接导致运动眩晕——任何应用场景都无法接受\n"
    "- VR 通常需要 HD 的 4-8 倍带宽才能达到同等感知质量\n\n"
    "## 实际解决方案\n"
    "- **注视点渲染**：只对用户注视区域传输高质量画面\n"
    "- **视口依赖流式传输**：将 360 视频切分为瓦片，仅高质量传输可见瓦片\n"
    "- **5G 边缘计算**：在网络边缘渲染 VR 内容，降低时延\n"
    "- **Apple Vision Pro / Meta Quest**：使用专用无线芯片实现超低时延\n"
]

with open(path, "w", encoding="utf-8") as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)
print("Demo 7 fixed: dimension bug + Chinese text")
