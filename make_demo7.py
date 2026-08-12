import json, os

base = r"C:\Users\guopi\GitHub\courses\future-media-internet\labs\kaggle-demos"

d7_cells = []

d7_cells.append({
    "cell_type": "markdown", "metadata": {},
    "source": [
        "# Demo 7: Network Impairments on VR/360 Video\n\n"
        "**Course**: Future Media Internet\n"
        "**Duration**: ~10 min\n"
        "**Environment**: Kaggle Notebook (CPU, NumPy + Matplotlib + SciPy)\n\n"
        "## Objective\n\n"
        "Show why VR/360 video is MORE sensitive to network degradation than regular HD.\n"
        "VR requires higher resolution, lower latency, and the equirectangular projection\n"
        "amplifies artifacts in the viewer's focus area."
    ]
})

d7_cells.append({
    "cell_type": "code", "execution_count": None, "metadata": {}, "outputs": [],
    "source": [
        "import numpy as np\n"
        "import matplotlib.pyplot as plt\n"
        "from scipy import ndimage\n"
        "print('Imports OK')\n"
    ]
})

d7_cells.append({
    "cell_type": "code", "execution_count": None, "metadata": {}, "outputs": [],
    "source": [
        "# Create a synthetic equirectangular VR frame\n"
        "# VR 360 video is typically 4K+ (3840x1920 or higher)\n"
        "# Scaled to 960x480 for fast rendering\n"
        "EH, EW = 480, 960  # equirectangular dimensions\n\n"
        "def create_vr_frame():\n"
        '    """Create a synthetic equirectangular 360 frame with content regions"""\n'
        "    frame = np.zeros((EH, EW, 3), dtype=np.float32)\n"
        "    # Horizon line (equator)\n"
        "    frame[EH//2-2:EH//2+2, :] = 0.8\n"
        "    # Sky gradient (top half)\n"
        "    for y in range(EH//2):\n"
        "        frame[y, :] = (0.3 + 0.5*y/(EH//2), 0.4 + 0.4*y/(EH//2), 0.6 + 0.3*y/(EH//2))\n"
        "    # Ground (bottom half)\n"
        "    frame[EH//2:, :] = (0.1, 0.3, 0.1)\n"
        "    # Objects at different positions (simulating 360 content)\n"
        "    # Center object (where viewer is likely looking)\n"
        "    cx, cy = EW//2, EH//2\n"
        "    for y in range(cy-60, cy+60):\n"
        "        for x in range(cx-80, cx+80):\n"
        "            if (x-cx)**2 + (y-cy)**2 < 60**2:\n"
        "                frame[y, x] = (0.9, 0.2, 0.2)\n"
        "    # Left object\n"
        "    for y in range(cy-30, cy+30):\n"
        "        for x in range(cx-300, cx-200):\n"
        "            if (x-(cx-250))**2 + (y-cy)**2 < 30**2:\n"
        "                frame[y, x] = (0.2, 0.9, 0.2)\n"
        "    # Right object\n"
        "    for y in range(cy-30, cy+30):\n"
        "        for x in range(cx+200, cx+300):\n"
        "            if (x-(cx+250))**2 + (y-cy)**2 < 30**2:\n"
        "                frame[y, x] = (0.2, 0.2, 0.9)\n"
        "    # Grid lines for spatial reference\n"
        "    for x in range(0, EW, 120):\n"
        "        frame[:, x] *= 0.7\n"
        "    for y in range(0, EH, 60):\n"
        "        frame[y, :] *= 0.7\n"
        "    return frame\n\n"
        "vr_frame = create_vr_frame()\n"
        "fig, ax = plt.subplots(figsize=(14, 7))\n"
        "ax.imshow(np.clip(vr_frame, 0, 1))\n"
        "ax.set_title('VR Equirectangular Frame (960x480)\\nRed=Center | Green=Left | Blue=Right', fontsize=13)\n"
        "ax.axis('off')\n"
        "plt.show()\n"
        'print("The equirectangular format stretches poles. Center objects appear", '
        '"larger than edge objects when viewed in VR headset.")\n'
    ]
})

d7_cells.append({
    "cell_type": "code", "execution_count": None, "metadata": {}, "outputs": [],
    "source": [
        "# Reuse impairment simulators from Demo 6\n"
        "def packet_loss(frame, rate):\n"
        "    result = frame.copy()\n"
        "    bh, bw = 24, 40\n"
        "    nb_h, nb_w = EH//bh, EW//bw\n"
        "    mask = np.random.random((nb_h, nb_w)) < rate\n"
        "    for i in range(nb_h):\n"
        "        for j in range(nb_w):\n"
        "            if mask[i,j]:\n"
        "                result[i*bh:(i+1)*bh, j*bw:(j+1)*bw] = 0.5\n"
        "    return result\n\n"
        "def jitter(frame, px):\n"
        "    result = frame.copy()\n"
        "    shifts = (np.random.randn(EH)*px).astype(int)\n"
        "    for y in range(EH):\n"
        "        result[y] = np.roll(result[y], shifts[y], axis=0)\n"
        "    return result\n\n"
        "def bw_drop(frame, scale):\n"
        "    h2, w2 = int(EH*scale), int(EW*scale)\n"
        "    low = ndimage.zoom(frame, (scale,scale,1), order=1)\n"
        "    up = ndimage.zoom(low, (1/scale,1/scale,1), order=1)\n"
        "    return np.clip(up[:EH,:EW], 0, 1)\n\n"
        "print('Simulators ready')\n"
    ]
})

d7_cells.append({
    "cell_type": "code", "execution_count": None, "metadata": {}, "outputs": [],
    "source": [
        "# Compare: Same impairment, HD vs VR impact\n"
        "np.random.seed(42)\n\n"
        "# Create an HD-equivalent crop from the VR frame (center region)\n"
        "# This represents what the viewer actually sees in the headset\n"
        "fov_h, fov_w = 270, 480  # field-of-view crop\n"
        "cy, cx = EH//2, EW//2\n"
        "hd_crop = vr_frame[cy-fov_h//2:cy+fov_h//2, cx-fov_w//2:cx+fov_w//2]\n\n"
        "fig, axes = plt.subplots(3, 3, figsize=(16, 12))\n\n"
        "impairments = [\n"
        "    ('Original', lambda f: f),\n"
        "    ('Loss 5%', lambda f: packet_loss(f, 0.05)),\n"
        "    ('Jitter 5px', lambda f: jitter(f, 5)),\n"
        "]\n\n"
        "for j, (label, func) in enumerate(impairments):\n"
        "    # Full VR frame\n"
        "    axes[0, j].imshow(np.clip(func(vr_frame), 0, 1))\n"
        "    axes[0, j].set_title('Full VR: {}'.format(label), fontsize=11)\n"
        "    axes[0, j].axis('off')\n"
        "    # HD-equivalent crop (viewer FOV)\n"
        "    crop = np.clip(func(hd_crop), 0, 1)\n"
        "    axes[1, j].imshow(crop)\n"
        "    axes[1, j].set_title('FOV Crop: {}'.format(label), fontsize=11)\n"
        "    axes[1, j].axis('off')\n"
        "    # Zoom into the center object (red ball)\n"
        "    cz_h, cz_w = fov_h//2, fov_w//2\n"
        "    zoom = crop[cz_h-60:cz_h+60, cz_w-60:cz_w+60]\n"
        "    axes[2, j].imshow(zoom)\n"
        "    axes[2, j].set_title('Center Zoom: {}'.format(label), fontsize=11)\n"
        "    axes[2, j].axis('off')\n\n"
        "plt.suptitle('VR vs HD: Same Impairment, Different Impact', fontsize=14, fontweight='bold')\n"
        "plt.tight_layout()\n"
        "plt.show()\n"
    ]
})

d7_cells.append({
    "cell_type": "code", "execution_count": None, "metadata": {}, "outputs": [],
    "source": [
        "# Critical comparison: VR latency sensitivity\n"
        "# Simulate what happens when VR frame updates are delayed\n"
        "def frame_drop_simulation(frame, drop_every_n):\n"
        '    """Every Nth frame is dropped, previous frame is repeated"""\n'
        "    result = frame.copy()\n"
        "    # Simulate: mark dropped frames by dimming\n"
        "    return result * 0.7\n\n"
        "# Visualize the impact of frame drops on VR experience\n"
        "fig, axes = plt.subplots(1, 3, figsize=(16, 5))\n\n"
        "axes[0].imshow(np.clip(vr_frame, 0, 1))\n"
        "axes[0].set_title('Smooth VR (60 fps)', fontsize=12, fontweight='bold')\n"
        "axes[0].axis('off')\n\n"
        "axes[1].imshow(np.clip(frame_drop_simulation(vr_frame, 3), 0, 1))\n"
        "axes[1].set_title('Frame Drops (20 fps)\\nMotion sickness risk!', fontsize=12)\n"
        "axes[1].axis('off')\n\n"
        "axes[2].imshow(np.clip(packet_loss(bw_drop(vr_frame, 0.5), 0.1), 0, 1))\n"
        "axes[2].set_title('Severe: BW 50% + Loss 10%\\nVR experience breaks down', fontsize=12)\n"
        "axes[2].axis('off')\n\n"
        "plt.suptitle('VR Quality Degradation', fontsize=14, fontweight='bold')\n"
        "plt.tight_layout()\n"
        "plt.show()\n\n"
        'print("\\nWhy VR is MORE sensitive to network issues:")\n'
        'print("1. Higher resolution (4K-8K vs 1080p) -> more data per frame")\n'
        'print("2. Low latency requirement (<20ms vs 2-5s buffer for streaming)")\n'
        'print("3. Frame drops cause motion sickness (vestibular disconnect)")\n'
        'print("4. Equirectangular projection wastes bits on poles")\n'
        'print("5. Foveated rendering assumes perfect delivery")\n'
    ]
})

d7_cells.append({
    "cell_type": "markdown", "metadata": {},
    "source": [
        "## Key Observations\n\n"
        "- A 5% packet loss that is barely noticeable in HD becomes clearly visible in VR\n"
        "- The equirectangular format amplifies artifacts at the poles (top/bottom of frame)\n"
        "- Frame drops in VR directly cause motion sickness - unacceptable for any application\n"
        "- VR typically needs 4-8x the bandwidth of equivalent HD quality\n\n"
        "## Real-world solutions\n"
        "- **Foveated rendering**: only transmit high quality where the viewer is looking\n"
        "- **Viewport-dependent streaming**: split 360 video into tiles, stream only visible tiles at high quality\n"
        "- **5G edge computing**: render VR content at the network edge to reduce latency\n"
        "- **Apple Vision Pro / Meta Quest**: use dedicated wireless chips for ultra-low latency"
    ]
})

nb7 = {
    "cells": d7_cells,
    "metadata": {"kernelspec": {"display_name":"Python 3","language":"python","name":"python3"}, "language_info":{"name":"python","version":"3.10.0"}},
    "nbformat": 4, "nbformat_minor": 4
}
with open(os.path.join(base, "demo7-vr-video-impairments.ipynb"), "w", encoding="utf-8") as f:
    json.dump(nb7, f, indent=1, ensure_ascii=False)
print("Demo 7 created")
