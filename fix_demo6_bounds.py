import json, os

path = r"C:\Users\guopi\GitHub\courses\future-media-internet\labs\kaggle-demos\demo6-hd-video-impairments.ipynb"
with open(path, "r", encoding="utf-8") as f:
    nb = json.load(f)

# Fix cell 3: make all functions frame-size-aware
nb["cells"][3]["source"] = [
    "# Network impairment simulators (frame-size-aware)\n"
    "def packet_loss(frame, rate):\n"
    "    result = frame.copy()\n"
    "    Hf, Wf = frame.shape[:2]\n"
    "    bh, bw = 30, 40\n"
    "    nb_h, nb_w = Hf//bh, Wf//bw\n"
    "    mask = np.random.random((nb_h, nb_w)) < rate\n"
    "    for i in range(nb_h):\n"
    "        for j in range(nb_w):\n"
    "            if mask[i,j]:\n"
    "                i1, i2 = i*bh, min((i+1)*bh, Hf)\n"
    "                j1, j2 = j*bw, min((j+1)*bw, Wf)\n"
    "                result[i1:i2, j1:j2] = 0.5\n"
    "    return result\n\n"
    "def jitter(frame, px):\n"
    "    result = frame.copy()\n"
    "    Hf = frame.shape[0]\n"
    "    shifts = (np.random.randn(Hf)*px).astype(int)\n"
    "    for y in range(Hf):\n"
    "        result[y] = np.roll(result[y], shifts[y], axis=0)\n"
    "    return result\n\n"
    "def bw_drop(frame, scale):\n"
    "    Hf, Wf = frame.shape[:2]\n"
    "    h2, w2 = int(Hf*scale), int(Wf*scale)\n"
    "    low = ndimage.zoom(frame, (scale,scale,1), order=1)\n"
    "    up = ndimage.zoom(low, (1/scale,1/scale,1), order=1)\n"
    "    return np.clip(up[:Hf,:Wf], 0, 1)\n\n"
    'print("Simulators ready (frame-size-aware)")\n'
]

with open(path, "w", encoding="utf-8") as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)
print("Demo 6 functions fixed")
