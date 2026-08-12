import json

path = r"C:\Users\guopi\GitHub\courses\future-media-internet\labs\kaggle-demos\demo5-semantic-communication.ipynb"
with open(path, "r", encoding="utf-8") as f:
    nb = json.load(f)

# Replace cell 5 (index 5) - the comparison cell
new_source = [
    "# Select one image for clear comparison\n"
    "model.eval()\n"
    "demo_loader = torch.utils.data.DataLoader(train_set, batch_size=10, shuffle=True)\n"
    "test_images, test_labels = next(iter(demo_loader))\n"
    "test_images = test_images.to(device)\n\n"
    "# Pick a clear digit to demonstrate\n"
    "idx = 0\n"
    "img = test_images[idx:idx+1]\n"
    "label = test_labels[idx].item()\n"
    "print(f'Selected digit: {label}')\n\n"
    "# Traditional: add noise directly to pixels\n"
    "def traditional_transmit(img, snr_db):\n"
    "    if snr_db >= 20:\n"
    "        return img.clone()\n"
    "    sig_pow = img.pow(2).mean()\n"
    "    snr_lin = 10 ** (snr_db / 10.0)\n"
    "    if snr_lin == 0:\n"
    "        return img.clone()\n"
    "    noise_pow = sig_pow / snr_lin\n"
    "    noise = torch.randn_like(img) * torch.sqrt(noise_pow)\n"
    "    return torch.clamp(img + noise, 0, 1)\n\n"
    "# Compare at different SNR levels\n"
    "snr_levels = [20, 10, 0, -5, -10]\n\n"
    "fig, axes = plt.subplots(2, len(snr_levels) + 1, figsize=(16, 7))\n\n"
    "# Original image\n"
    "axes[0, 0].imshow(img.cpu().squeeze(), cmap='gray')\n"
    "axes[0, 0].set_title(f'Original\\nDigit: {label}', fontsize=10, fontweight='bold')\n"
    "axes[0, 0].axis('off')\n"
    "axes[1, 0].axis('off')\n\n"
    "for j, snr in enumerate(snr_levels):\n"
    "    # Traditional\n"
    "    trad = traditional_transmit(img, snr)\n"
    "    axes[0, j+1].imshow(trad.cpu().squeeze(), cmap='gray')\n"
    "    axes[0, j+1].set_title(f'Traditional\\nSNR={snr}dB', fontsize=9)\n"
    "    axes[0, j+1].axis('off')\n\n"
    "    # Semantic\n"
    "    with torch.no_grad():\n"
    "        sem = model(img, snr_db=snr)\n"
    "    axes[1, j+1].imshow(sem.cpu().squeeze(), cmap='gray')\n"
    "    axes[1, j+1].set_title(f'Semantic\\nSNR={snr}dB', fontsize=9)\n"
    "    axes[1, j+1].axis('off')\n\n"
    "plt.suptitle(f'Semantic vs Traditional: Digit {label} at Different SNR\\n(Top: Traditional | Bottom: Semantic)',\n"
    "             fontsize=13, fontweight='bold', y=1.02)\n"
    "plt.tight_layout()\n"
    "plt.show()\n\n"
    "print('Key observation:')\n"
    "print(f'At SNR=-10dB, traditional is pure noise (digit {label} unrecognizable)')\n"
    "print(f'But semantic communication still preserves the shape of {label}')\n"
    "print('Semantic comm trades pixel accuracy for meaning preservation.')"
]

nb['cells'][5]['source'] = new_source

with open(path, "w", encoding="utf-8") as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)
print("Cell 5 fixed: shows one image with correct label")
