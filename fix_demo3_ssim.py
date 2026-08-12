import json

path = r"C:\Users\guopi\GitHub\courses\future-media-internet\labs\kaggle-demos\demo3-quality-assessment.ipynb"
with open(path, "r", encoding="utf-8") as f:
    nb = json.load(f)

# Replace cell 3 with robust SSIM
nb["cells"][3]["source"] = [
    "# Calculate quality metrics\n",
    "def psnr(original, degraded):\n",
    "    mse = np.mean((original - degraded) ** 2)\n",
    "    if mse < 1e-10:\n",
    "        return 100.0\n",
    "    return float(20 * np.log10(1.0 / np.sqrt(mse)))\n",
    "\n",
    "def ssim_torch(original, degraded):\n",
    '    """Robust SSIM with numerical safeguards"""\n',
    "    orig_t = torch.tensor(original).unsqueeze(0).unsqueeze(0).float()\n",
    "    deg_t = torch.tensor(degraded).unsqueeze(0).unsqueeze(0).float()\n",
    "    \n",
    "    # Local means via 11x11 box filter\n",
    "    mu_x = F.avg_pool2d(orig_t, 11, 1, 5)\n",
    "    mu_y = F.avg_pool2d(deg_t, 11, 1, 5)\n",
    "    \n",
    "    # Local variances (clamp to prevent negative from FP errors)\n",
    "    sigma_x = torch.clamp(F.avg_pool2d(orig_t ** 2, 11, 1, 5) - mu_x ** 2, min=0.0)\n",
    "    sigma_y = torch.clamp(F.avg_pool2d(deg_t ** 2, 11, 1, 5) - mu_y ** 2, min=0.0)\n",
    "    sigma_xy = F.avg_pool2d(orig_t * deg_t, 11, 1, 5) - mu_x * mu_y\n",
    "    \n",
    "    C1 = 0.01 ** 2\n",
    "    C2 = 0.03 ** 2\n",
    "    num = (2 * mu_x * mu_y + C1) * (2 * sigma_xy + C2)\n",
    "    den = (mu_x ** 2 + mu_y ** 2 + C1) * (sigma_x + sigma_y + C2)\n",
    "    ssim_map = num / den\n",
    "    return ssim_map.mean().item()\n",
    "\n",
    "# Compute all versions\n",
    "results = []\n",
    "for i, (ver, name) in enumerate(zip(versions, titles)):\n",
    "    p = psnr(original, ver)\n",
    "    s = ssim_torch(original, ver)\n",
    "    results.append(dict(name=name, PSNR=p, SSIM=s))\n",
    "    print(f\"{name:8s} | PSNR: {p:5.1f} dB | SSIM: {s:.3f}\")\n",
    "\n",
    'print("\\nKey observation:")\n',
    'print("PSNR is pixel-based. SSIM mimics human perception (structure and texture).")\n',
    'print("When PSNR values are similar, SSIM can differ greatly - humans notice structural distortion more.")\n',
]

with open(path, "w", encoding="utf-8") as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)
print("demo3 SSIM fixed")
