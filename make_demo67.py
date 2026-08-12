import json, os

def make_nb(cells, filename):
    nb = {
        "cells": cells,
        "metadata": {
            "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
            "language_info": {"name": "python", "version": "3.10.0"}
        },
        "nbformat": 4,
        "nbformat_minor": 4
    }
    path = os.path.join(r"C:\Users\guopi\GitHub\courses\future-media-internet\labs\kaggle-demos", filename)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(nb, f, indent=1, ensure_ascii=False)
    print(f"Created: {filename}")

def md(src):
    return {"cell_type": "markdown", "metadata": {}, "source": src}

def code(src):
    return {"cell_type": "code", "execution_count": None, "metadata": {}, "outputs": [], "source": src}

# ===== Demo 6: HD Video Network Impairments =====
make_nb([
    md([
        "# Demo 6: Network Impairments on HD Video\n\n"
        "**Course**: Future Media Internet\n"
        "**Duration**: ~10 minutes\n"
        "**Environment**: Kaggle Notebook (CPU, NumPy + Matplotlib)\n\n"
        "## Objective\n\n"
        "Simulate how network degradation (packet loss, jitter, bandwidth drop) affects HD video quality.\n"
        "Students see visually why different types of network issues cause different artifacts."
    ]),
    code([
        "import numpy as np\n"
        "import matplotlib.pyplot as plt\n"
        "from scipy import ndimage\n\n"
        'print("Imports OK")\n'
    ]),
    code([
        "# Create a synthetic HD video frame (1920x1080 test pattern)\n"
        "H, W = 540, 960  # scaled for fast rendering\n\n"
        "def create_test_frame():\n"
        '    """Create a synthetic frame with color bars, gradients, and fine details"""\n'
        "    frame = np.zeros((H, W, 3), dtype=np.float32)\n"
        "    # Color bars\n"
        "    colors = [(1,0,0), (0,1,0), (0,0,1), (1,1,0), (0,1,1), (1,0,1), (1,1,1)]\n"
        "    bar_w = W // len(colors)\n"
        "    for i, c in enumerate(colors):\n"
        "        frame[:H//3, i*bar_w:(i+1)*bar_w] = c\n"
        "    # Gradient\n"
        "    for x in range(W):\n"
        "        frame[H//3:2*H//3, x] = (x/W, 0.5, 1-x/W)\n"
        "    # Fine details: text-like patterns\n"
        "    for y in range(2*H//3, H, 20):\n"
        "        for x in range(0, W, 4):\n"
        "            if (x//4 + y//20) % 3 == 0:\n"
        "                frame[y:y+10, x:x+2] = 0.9\n"
        "            elif (x//4 + y//20) % 3 == 1:\n"
        "                frame[y:y+10, x:x+2] = 0.2\n"
        "    return frame\n\n"
        "original = create_test_frame()\n"
        "plt.figure(figsize=(12, 7))\n"
        "plt.imshow(np.clip(original, 0, 1))\n"
        "plt.title('Original HD Test Frame (540x960)')\n"
        "plt.axis('off')\n"
        "plt.show()\n"
        'print("Test frame created")\n'
    ]),
    code([
        "# Network impairment simulators\n\n"
        "def simulate_packet_loss(frame, loss_rate):\n"
        '    """Randomly drop macroblocks (simulating packet loss)"""\n'
        "    result = frame.copy()\n"
        "    block_h, block_w = 30, 40  # macroblock size\n"
        "    n_blocks_h, n_blocks_w = H//block_h, W//block_w\n"
        "    mask = np.random.random((n_blocks_h, n_blocks_w)) < loss_rate\n"
        "    for i in range(n_blocks_h):\n"
        "        for j in range(n_blocks_w):\n"
        "            if mask[i, j]:\n"
        "                # Fill lost block with gray (concealment)\n"
        "                result[i*block_h:(i+1)*block_h, j*block_w:(j+1)*block_w] = 0.5\n"
        "    return result\n\n"
        "def simulate_jitter(frame, intensity):\n"
        '    """Simulate temporal jitter: horizontal pixel shift"""\n'
        "    result = frame.copy()\n"
        "    shift_map = (np.random.randn(H) * intensity).astype(int)\n"
        "    for y in range(H):\n"
        "        shift = shift_map[y]\n"
        "        if shift > 0:\n"
        "            result[y, shift:] = result[y, :W-shift]\n"
        "            result[y, :shift] = result[y, shift:shift+1]\n"
        "        elif shift < 0:\n"
        "            result[y, :W+shift] = result[y, -shift:]\n"
        "            result[y, W+shift:] = result[y, W+shift-1:W+shift]\n"
        "    return result\n\n"
        "def simulate_bandwidth_drop(frame, scale):\n"
        '    """Simulate forced resolution downgrade from bandwidth drop"""\n'
        "    from scipy import ndimage\n"
        "    low_res = ndimage.zoom(frame, (scale, scale, 1), order=1)\n"
        "    restored = ndimage.zoom(low_res, (1/scale, 1/scale, 1), order=1)\n"
        "    return np.clip(restored[:H, :W], 0, 1)\n\n"
        'print("Impairment simulators ready")\n'
    ]),
    code([
        "# Visual comparison: different impairment types at different levels\n"
        "loss_rates = [0.01, 0.05, 0.10, 0.20]\n"
        "jitter_levels = [1, 3, 6, 10]\n"
        "bw_scales = [0.75, 0.50, 0.25, 0.10]\n\n"
        "np.random.seed(42)\n\n"
        "fig, axes = plt.subplots(3, 5, figsize=(18, 12))\n\n"
        "# Row 0: Packet Loss\n"
        "axes[0, 0].imshow(original)\n"
        "axes[0, 0].set_title('Original', fontweight='bold')\n"
        "for j, rate in enumerate(loss_rates):\n"
        "    impaired = simulate_packet_loss(original, rate)\n"
        "    axes[0, j+1].imshow(np.clip(impaired, 0, 1))\n"
        "    axes[0, j+1].set_title(f'Loss {rate:.0%}')\n\n"
        "# Row 1: Jitter\n"
        "axes[1, 0].imshow(original)\n"
        "axes[1, 0].set_title('Original', fontweight='bold')\n"
        "for j, jit in enumerate(jitter_levels):\n"
        "    impaired = simulate_jitter(original, jit)\n"
        "    axes[1, j+1].imshow(np.clip(impaired, 0, 1))\n"
        "    axes[1, j+1].set_title(f'Jitter {jit}px')\n\n"
        "# Row 2: Bandwidth Drop\n"
        "axes[2, 0].imshow(original)\n"
        "axes[2, 0].set_title('Original', fontweight='bold')\n"
        "for j, scale in enumerate(bw_scales):\n"
        "    impaired = simulate_bandwidth_drop(original, scale)\n"
        "    axes[2, j+1].imshow(np.clip(impaired, 0, 1))\n"
        "    axes[2, j+1].set_title(f'BW x{scale:.0%}')\n\n"
        "for ax in axes.flat:\n"
        "    ax.axis('off')\n\n"
        "plt.suptitle('Network Impairments on HD Video\\n'
        "             '(Row 1: Packet Loss | Row 2: Jitter | Row 3: Bandwidth Drop)',\n"
        "             fontsize=14, fontweight='bold')\n"
        "plt.tight_layout()\n"
        "plt.show()\n"
    ]),
    code([
        "# Zoom into detail region to show artifact differences\n"
        "detail_y, detail_x = slice(200, 350), slice(400, 550)\n\n"
        "fig, axes = plt.subplots(2, 3, figsize=(14, 9))\n\n"
        "# Original detail\n"
        "axes[0, 0].imshow(original[detail_y, detail_x])\n"
        "axes[0, 0].set_title('Original Detail', fontweight='bold')\n"
        "axes[0, 0].axis('off')\n\n"
        "# Packet loss - block artifacts\n"
        "pl = simulate_packet_loss(original, 0.10)\n"
        "axes[0, 1].imshow(np.clip(pl[detail_y, detail_x], 0, 1))\n"
        "axes[0, 1].set_title('Packet Loss 10%')\n"
        "axes[0, 1].axis('off')\n\n"
        "# Jitter - horizontal tearing\n"
        "jt = simulate_jitter(original, 6)\n"
        "axes[0, 2].imshow(np.clip(jt[detail_y, detail_x], 0, 1))\n"
        "axes[0, 2].set_title('Jitter 6px')\n"
        "axes[0, 2].axis('off')\n\n"
        "# Bandwidth drop - blur\n"
        "bw = simulate_bandwidth_drop(original, 0.25)\n"
        "axes[1, 0].imshow(np.clip(bw[detail_y, detail_x], 0, 1))\n"
        "axes[1, 0].set_title('BW Drop 25%')\n"
        "axes[1, 0].axis('off')\n\n"
        "# Combined: loss + bandwidth\n"
        "combined = simulate_packet_loss(simulate_bandwidth_drop(original, 0.5), 0.05)\n"
        "axes[1, 1].imshow(np.clip(combined[detail_y, detail_x], 0, 1))\n"
        "axes[1, 1].set_title('Combined: BW 50% + Loss 5%')\n"
        "axes[1, 1].axis('off')\n\n"
        "# Combined: loss + jitter\n"
        "combined2 = simulate_jitter(simulate_packet_loss(original, 0.05), 3)\n"
        "axes[1, 2].imshow(np.clip(combined2[detail_y, detail_x], 0, 1))\n"
        "axes[1, 2].set_title('Combined: Loss 5% + Jitter 3px')\n"
        "axes[1, 2].axis('off')\n\n"
        "plt.suptitle('Detail Zoom: Artifact Comparison', fontsize=14, fontweight='bold')\n"
        "plt.tight_layout()\n"
        "plt.show()\n\n"
        'print("\\nKey observations:")\n'
        'print("1. Packet loss -> missing blocks (gray squares)")\n'
        'print("2. Jitter -> horizontal tearing (lines misaligned)")\n'
        'print("3. Bandwidth drop -> overall blur (forced low resolution)")\n'
        'print("4. Combined impairments create compound artifacts")\n'
    ]),
    md([
        "## Discussion\n\n"
        "- **Packet loss**: Most visible on high-frequency content (text, edges). Error concealment helps but leaves artifacts.\n"
        "- **Jitter**: Causes temporal misalignment. Critical for live streaming where no buffering is possible.\n"
        "- **Bandwidth drop**: Forces encoder to reduce quality. Adaptive bitrate (ABR) mitigates this (see Demo 2).\n"
        "- **Real systems**: YouTube/Netflix use FEC (Forward Error Correction) + ABR + jitter buffers to handle all three simultaneously."
    ]),
], "demo6-hd-video-impairments.ipynb")

print("Demo 6 done")
