import json, os

base = r"C:\Users\guopi\GitHub\courses\future-media-internet\labs\kaggle-demos"

# ===== Demo 6 =====
d6_cells = []

d6_cells.append({
    "cell_type": "markdown", "metadata": {},
    "source": [
        "# Demo 6: Network Impairments on HD Video\n\n"
        "**Course**: Future Media Internet\n"
        "**Duration**: ~10 min\n"
        "**Environment**: Kaggle Notebook (CPU, NumPy + Matplotlib + SciPy)\n\n"
        "## Objective\n"
        "Simulate packet loss, jitter, and bandwidth drops on a synthetic HD test frame.\n"
        "Show how each impairment type creates visually distinct artifacts."
    ]
})

d6_cells.append({
    "cell_type": "code", "execution_count": None, "metadata": {}, "outputs": [],
    "source": [
        "import numpy as np\n"
        "import matplotlib.pyplot as plt\n"
        "from scipy import ndimage\n"
        "print('Imports OK')\n"
    ]
})

d6_cells.append({
    "cell_type": "code", "execution_count": None, "metadata": {}, "outputs": [],
    "source": [
        "# Create synthetic HD test frame (scaled to 540x960)\n"
        "H, W = 540, 960\n\n"
        "def create_test_frame():\n"
        "    frame = np.zeros((H, W, 3), dtype=np.float32)\n"
        "    colors = [(1,0,0),(0,1,0),(0,0,1),(1,1,0),(0,1,1),(1,0,1),(1,1,1)]\n"
        "    bar_w = W // len(colors)\n"
        "    for i, c in enumerate(colors):\n"
        "        frame[:H//3, i*bar_w:(i+1)*bar_w] = c\n"
        "    for x in range(W):\n"
        "        frame[H//3:2*H//3, x] = (x/W, 0.5, 1-x/W)\n"
        "    for y in range(2*H//3, H, 20):\n"
        "        for x in range(0, W, 4):\n"
        "            v = 0.9 if (x//4+y//20)%2==0 else 0.2\n"
        "            frame[y:y+10, x:x+2] = v\n"
        "    return frame\n\n"
        "original = create_test_frame()\n"
        "fig, ax = plt.subplots(figsize=(12,7))\n"
        "ax.imshow(np.clip(original,0,1))\n"
        "ax.set_title('Original HD Test Frame (540x960)')\n"
        "ax.axis('off')\n"
        "plt.show()\n"
    ]
})

d6_cells.append({
    "cell_type": "code", "execution_count": None, "metadata": {}, "outputs": [],
    "source": [
        "# Network impairment simulators\n\n"
        "def packet_loss(frame, rate):\n"
        "    result = frame.copy()\n"
        "    bh, bw = 30, 40\n"
        "    nb_h, nb_w = H//bh, W//bw\n"
        "    mask = np.random.random((nb_h, nb_w)) < rate\n"
        "    for i in range(nb_h):\n"
        "        for j in range(nb_w):\n"
        "            if mask[i,j]:\n"
        "                result[i*bh:(i+1)*bh, j*bw:(j+1)*bw] = 0.5\n"
        "    return result\n\n"
        "def jitter(frame, px):\n"
        "    result = frame.copy()\n"
        "    shifts = (np.random.randn(H)*px).astype(int)\n"
        "    for y in range(H):\n"
        "        s = shifts[y]\n"
        "        result[y] = np.roll(result[y], s, axis=0)\n"
        "    return result\n\n"
        "def bw_drop(frame, scale):\n"
        "    h2, w2 = int(H*scale), int(W*scale)\n"
        "    low = ndimage.zoom(frame, (scale,scale,1), order=1)\n"
        "    up = ndimage.zoom(low, (1/scale,1/scale,1), order=1)\n"
        "    return np.clip(up[:H,:W], 0, 1)\n\n"
        "print('Simulators ready')\n"
    ]
})

d6_cells.append({
    "cell_type": "code", "execution_count": None, "metadata": {}, "outputs": [],
    "source": [
        "# Full comparison grid\n"
        "np.random.seed(42)\n"
        "loss_rates = [0.01, 0.05, 0.10, 0.20]\n"
        "jitter_px = [1, 3, 6, 10]\n"
        "bw_scales = [0.75, 0.50, 0.25, 0.10]\n\n"
        "fig, axes = plt.subplots(3, 5, figsize=(18, 12))\n\n"
        "for row, (label, levels, func) in enumerate([\n"
        "    ('Packet Loss', loss_rates, lambda f,l: packet_loss(f,l)),\n"
        "    ('Jitter', jitter_px, lambda f,l: jitter(f,l)),\n"
        "    ('BW Drop', bw_scales, lambda f,l: bw_drop(f,l)),\n"
        "]):\n"
        "    axes[row,0].imshow(original)\n"
        "    axes[row,0].set_title('Original', fontweight='bold')\n"
        "    for j, lv in enumerate(levels):\n"
        "        imp = func(original, lv)\n"
        "        axes[row,j+1].imshow(np.clip(imp,0,1))\n"
        "        axes[row,j+1].set_title('{} {}'.format(label, lv))\n"
        "for ax in axes.flat:\n"
        "    ax.axis('off')\n"
        "plt.suptitle('Network Impairments on HD Video', fontsize=14, fontweight='bold')\n"
        "plt.tight_layout()\n"
        "plt.show()\n"
    ]
})

d6_cells.append({
    "cell_type": "code", "execution_count": None, "metadata": {}, "outputs": [],
    "source": [
        "# Detail zoom comparison\n"
        "dy, dx = slice(200,350), slice(400,550)\n"
        "fig, axes = plt.subplots(2, 3, figsize=(14, 9))\n\n"
        "axes[0,0].imshow(original[dy,dx])\n"
        "axes[0,0].set_title('Original Detail', fontweight='bold')\n"
        "axes[0,0].axis('off')\n\n"
        "pl = packet_loss(original, 0.10)\n"
        "axes[0,1].imshow(np.clip(pl[dy,dx],0,1))\n"
        "axes[0,1].set_title('Packet Loss 10%')\n"
        "axes[0,1].axis('off')\n\n"
        "jt = jitter(original, 6)\n"
        "axes[0,2].imshow(np.clip(jt[dy,dx],0,1))\n"
        "axes[0,2].set_title('Jitter 6px')\n"
        "axes[0,2].axis('off')\n\n"
        "bw = bw_drop(original, 0.25)\n"
        "axes[1,0].imshow(np.clip(bw[dy,dx],0,1))\n"
        "axes[1,0].set_title('BW Drop 25%')\n"
        "axes[1,0].axis('off')\n\n"
        "cb = packet_loss(bw_drop(original, 0.5), 0.05)\n"
        "axes[1,1].imshow(np.clip(cb[dy,dx],0,1))\n"
        "axes[1,1].set_title('BW 50% + Loss 5%')\n"
        "axes[1,1].axis('off')\n\n"
        "cb2 = jitter(packet_loss(original, 0.05), 3)\n"
        "axes[1,2].imshow(np.clip(cb2[dy,dx],0,1))\n"
        "axes[1,2].set_title('Loss 5% + Jitter 3px')\n"
        "axes[1,2].axis('off')\n\n"
        "plt.suptitle('Detail Zoom: Artifact Comparison', fontsize=14, fontweight='bold')\n"
        "plt.tight_layout()\n"
        "plt.show()\n"
    ]
})

d6_cells.append({
    "cell_type": "markdown", "metadata": {},
    "source": [
        "## Key Observations\n\n"
        "- **Packet loss**: missing blocks (gray squares). Error concealment helps but leaves visible artifacts.\n"
        "- **Jitter**: horizontal tearing (lines misaligned). Critical for live streaming where no buffering is possible.\n"
        "- **Bandwidth drop**: overall blur from forced resolution downgrade.\n"
        "- **Combined**: compound artifacts are worse than any single impairment.\n\n"
        "## Real-world mitigation\n"
        "- YouTube/Netflix: ABR (Adaptive Bitrate) + FEC (Forward Error Correction) + jitter buffers\n"
        "- WebRTC/Google Meet: NACK (retransmission) + FEC + adaptive encoding\n"
        "- 5G URLLC: ultra-low latency reduces jitter sensitivity\n"
    ]
})

nb = {
    "cells": d6_cells,
    "metadata": {"kernelspec": {"display_name":"Python 3","language":"python","name":"python3"}, "language_info":{"name":"python","version":"3.10.0"}},
    "nbformat": 4, "nbformat_minor": 4
}
with open(os.path.join(base, "demo6-hd-video-impairments.ipynb"), "w", encoding="utf-8") as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)
print("Demo 6 created")
