import json, os

cells = []

# Cell 0: Title
cells.append({
    "cell_type": "markdown",
    "metadata": {},
    "source": [
        "# 实验五（课堂演示）：语义通信 vs 传统通信\n\n"
        "**适用课程**：未来媒体互联网\n"
        "**演示时长**：约 10 分钟\n"
        "**运行环境**：Kaggle Notebook（CPU，PyTorch 预装）\n\n"
        "## 演示目标\n\n"
        "对比传统方案和语义通信方案在不同信噪比下的重建效果。\n"
        "核心震撼点：极低 SNR（-10dB）下传统方案完全失效，语义方案仍能保留数字的语义信息。"
    ]
})

# Cell 1: Imports
cells.append({
    "cell_type": "code",
    "execution_count": None,
    "metadata": {},
    "outputs": [],
    "source": [
        "import torch\n"
        "import torch.nn as nn\n"
        "import torch.optim as optim\n"
        "import torchvision\n"
        "import torchvision.transforms as transforms\n"
        "import numpy as np\n"
        "import matplotlib.pyplot as plt\n\n"
        "device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')\n"
        "print(f'Device: {device}')\n"
        "print('Imports OK')"
    ]
})

# Cell 2: Load MNIST
cells.append({
    "cell_type": "code",
    "execution_count": None,
    "metadata": {},
    "outputs": [],
    "source": [
        "# Load MNIST data\n"
        "transform = transforms.ToTensor()\n"
        "train_set = torchvision.datasets.MNIST(\n"
        "    root='./mnist_data', train=True, download=True, transform=transform\n"
        ")\n"
        "train_loader = torch.utils.data.DataLoader(train_set, batch_size=128, shuffle=True)\n\n"
        "# Show samples\n"
        "samples, labels = next(iter(train_loader))\n"
        "fig, axes = plt.subplots(1, 8, figsize=(12, 2))\n"
        "for i in range(8):\n"
        "    axes[i].imshow(samples[i][0], cmap='gray')\n"
        "    axes[i].set_title(str(labels[i].item()))\n"
        "    axes[i].axis('off')\n"
        "plt.suptitle('MNIST Samples')\n"
        "plt.tight_layout()\n"
        "plt.show()\n"
        "print(f'Training set: {len(train_set)} images')"
    ]
})

# Cell 3: Define model
cells.append({
    "cell_type": "code",
    "execution_count": None,
    "metadata": {},
    "outputs": [],
    "source": [
        "LATENT_DIM = 16\n\n"
        "class SemanticAutoencoder(nn.Module):\n"
        "    def __init__(self, latent_dim=LATENT_DIM):\n"
        "        super().__init__()\n"
        "        self.encoder = nn.Sequential(\n"
        "            nn.Linear(784, 256), nn.ReLU(),\n"
        "            nn.Linear(256, 128), nn.ReLU(),\n"
        "            nn.Linear(128, latent_dim)\n"
        "        )\n"
        "        self.decoder = nn.Sequential(\n"
        "            nn.Linear(latent_dim, 128), nn.ReLU(),\n"
        "            nn.Linear(128, 256), nn.ReLU(),\n"
        "            nn.Linear(256, 784), nn.Sigmoid()\n"
        "        )\n\n"
        "    def add_channel_noise(self, z, snr_db):\n"
        "        if snr_db is None:\n"
        "            return z\n"
        "        signal_power = z.pow(2).mean(dim=1, keepdim=True)\n"
        "        snr_linear = 10 ** (snr_db / 10.0)\n"
        "        noise_power = signal_power / snr_linear\n"
        "        noise = torch.randn_like(z) * torch.sqrt(noise_power)\n"
        "        return z + noise\n\n"
        "    def forward(self, x, snr_db=10):\n"
        "        z = self.encoder(x.view(x.size(0), -1))\n"
        "        z_noisy = self.add_channel_noise(z, snr_db)\n"
        "        return self.decoder(z_noisy).view(-1, 1, 28, 28)\n\n"
        "model = SemanticAutoencoder().to(device)\n"
        "criterion = nn.MSELoss()\n"
        "optimizer = optim.Adam(model.parameters(), lr=0.001)\n"
        "print(f'Parameters: {sum(p.numel() for p in model.parameters()):,}')"
    ]
})

# Cell 4: Train
cells.append({
    "cell_type": "code",
    "execution_count": None,
    "metadata": {},
    "outputs": [],
    "source": [
        "# Train (about 2 minutes on CPU)\n"
        "EPOCHS = 5\n"
        "model.train()\n"
        "for epoch in range(EPOCHS):\n"
        "    total_loss = 0.0\n"
        "    for batch_idx, (data, _) in enumerate(train_loader):\n"
        "        data = data.to(device)\n"
        "        optimizer.zero_grad()\n"
        "        output = model(data, snr_db=10)\n"
        "        loss = criterion(output, data)\n"
        "        loss.backward()\n"
        "        optimizer.step()\n"
        "        total_loss += loss.item()\n"
        "    avg_loss = total_loss / len(train_loader)\n"
        "    print(f'Epoch {epoch+1}/{EPOCHS} | Loss: {avg_loss:.4f}')\n"
        "print('Training done')"
    ]
})

# Cell 5: Compare
cells.append({
    "cell_type": "code",
    "execution_count": None,
    "metadata": {},
    "outputs": [],
    "source": [
        "# Get test images from training set (for demo purposes)\n"
        "model.eval()\n"
        "demo_loader = torch.utils.data.DataLoader(train_set, batch_size=10, shuffle=True)\n"
        "test_images, test_labels = next(iter(demo_loader))\n"
        "test_images = test_images.to(device)\n\n"
        "# Traditional: simulate channel degradation by adding noise directly to pixels\n"
        "def traditional_transmit(img, snr_db):\n"
        "    if snr_db >= 20:\n"
        "        return img.clone()\n"
        "    sig_pow = img.pow(2).mean()\n"
        "    snr_lin = 10 ** (snr_db / 10.0)\n"
        "    noise_pow = sig_pow / snr_lin\n"
        "    noise = torch.randn_like(img) * torch.sqrt(noise_pow)\n"
        "    return torch.clamp(img + noise, 0, 1)\n\n"
        "# Compare at different SNR levels\n"
        "snr_levels = [20, 10, 0, -5, -10]\n"
        "n_show = 5  # show 5 sample images\n\n"
        "fig, axes = plt.subplots(3, len(snr_levels) + 1, figsize=(16, 9))\n\n"
        "for row_idx in range(n_show):\n"
        "    img = test_images[row_idx:row_idx+1]\n"
        "    label = test_labels[row_idx].item()\n\n"
        "    # Original\n"
        "    if row_idx == 0:\n"
        "        axes[0, 0].imshow(img.cpu().squeeze(), cmap='gray')\n"
        "        axes[0, 0].set_title('Original', fontsize=10, fontweight='bold')\n"
        "    axes[0, 0].axis('off')\n\n"
        "    for j, snr in enumerate(snr_levels):\n"
        "        # Traditional\n"
        "        trad = traditional_transmit(img, snr)\n"
        "        axes[0, j+1].imshow(trad.cpu().squeeze(), cmap='gray')\n"
        "        if row_idx == 0:\n"
        "            axes[0, j+1].set_title(f'Traditional\\nSNR={snr}dB', fontsize=9)\n"
        "        axes[0, j+1].axis('off')\n\n"
        "        # Semantic\n"
        "        with torch.no_grad():\n"
        "            sem = model(img, snr_db=snr)\n"
        "        axes[1, j+1].imshow(sem.cpu().squeeze(), cmap='gray')\n"
        "        if row_idx == 0:\n"
        "            axes[1, j+1].set_title(f'Semantic\\nSNR={snr}dB', fontsize=9)\n"
        "        axes[1, j+1].axis('off')\n\n"
        "# Row labels\n"
        "axes[0, 0].set_title(f'Label: {label}', fontsize=9)\n"
        "axes[1, 0].text(0.5, 0.5, f'Label: {label}', transform=axes[1, 0].transAxes, ha='center', fontsize=9)\n"
        "axes[1, 0].axis('off')\n"
        "axes[2, 0].axis('off')\n\n"
        "# Noise level visualization\n"
        "for j, snr in enumerate(snr_levels):\n"
        "    axes[2, j+1].text(0.5, 0.5, f'Noise\\npower', ha='center', fontsize=8, color='gray')\n"
        "    axes[2, j+1].axis('off')\n\n"
        "plt.suptitle('Semantic vs Traditional: Reconstruction at Different SNR\\n(Top: Traditional | Middle: Semantic)',\n"
        "             fontsize=13, fontweight='bold', y=1.02)\n"
        "plt.tight_layout()\n"
        "plt.show()\n\n"
        "print('Key observation:')\n"
        "print('At SNR=-10dB, traditional is just noise, but semantic still shows the digit shape.')\n"
        "print('Semantic communication trades pixel accuracy for semantic preservation.')"
    ]
})

# Cell 6: Demo flow
cells.append({
    "cell_type": "markdown",
    "metadata": {},
    "source": [
        "## 课堂演示流程（10 分钟）\n\n"
        "1. 运行 Cell 1-2：展示 MNIST 样本\n"
        "2. 运行 Cell 3-4：训练模型（约 2 分钟），期间讲解自编码器概念\n"
        "3. 运行 Cell 5：展示对比结果\n"
        "4. 重点观察 SNR=-10dB 列：传统方案全雪花，语义方案还能看出数字\n\n"
        "## 课堂互动\n\n"
        "1. 语义通信牺牲了什么，换来了什么？\n"
        "2. 为什么这种 trade-off 适合 6G 场景？\n"
        "3. 如果传输的不是 MNIST 数字而是人脸，结果会一样吗？"
    ]
})

# Build notebook
nb = {
    "cells": cells,
    "metadata": {
        "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
        "language_info": {"name": "python", "version": "3.10.0"}
    },
    "nbformat": 4,
    "nbformat_minor": 4
}

path = r"C:\Users\guopi\GitHub\courses\future-media-internet\labs\kaggle-demos\demo5-semantic-communication.ipynb"
with open(path, "w", encoding="utf-8") as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)
print("demo5 rewritten successfully")
