# 实验五：语义通信原型系统

## 实验目标

实现一个简单的语义通信系统（自编码器+信道噪声模拟），对比传统方案和语义方案在不同信噪比下的重建效果，理解 6G 语义通信的基本思想。

## 环境准备

```bash
pip install numpy matplotlib torch torchvision jupyter
```

备选：直接使用 [Kaggle Demo Notebook](../kaggle-demos/demo5-semantic-communication.ipynb)。

## 实验步骤

### Step 1：加载 MNIST 数据集（2 min）

```python
import torchvision
import torchvision.transforms as transforms

transform = transforms.ToTensor()
train_set = torchvision.datasets.MNIST(
    root='./data', train=True, download=True, transform=transform
)
```

### Step 2：构建语义通信自编码器（15 min）

> 📝 **TODO**：搭建编码器→信道→解码器的完整流水线。

```python
import torch.nn as nn

class SemanticAutoencoder(nn.Module):
    def __init__(self, latent_dim=16):
        super().__init__()
        # TODO: 编码器（784 → 256 → 128 → latent_dim）
        # TODO: 解码器（latent_dim → 128 → 256 → 784）

    def add_channel_noise(self, z, snr_db):
        """模拟高斯信道噪声"""
        # TODO: 根据 SNR 计算噪声功率，加入高斯噪声
        # 提示：noise_power = signal_power / 10^(snr_db/10)
        pass

    def forward(self, x, snr_db):
        z = self.encoder(x.view(-1, 784))
        z_noisy = self.add_channel_noise(z, snr_db)
        return self.decoder(z_noisy).view(-1, 1, 28, 28)
```

### Step 3：训练模型（10 min）

```python
model = SemanticAutoencoder(latent_dim=16)
criterion = nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

# TODO: 训练循环（5 epochs）
# 注意：训练时加入 SNR=10dB 噪声，让模型学会抗噪
```

**预期**：训练 loss 从 ~0.1 下降到 ~0.01。

### Step 4：传统方案基线（5 min）

```python
def traditional_transmission(img, snr_db):
    """传统方案：直接传输像素 + 信道噪声"""
    # TODO: 根据 SNR 加噪
    pass
```

### Step 5：对比实验（10 min）

```python
snr_levels = [20, 10, 0, -5, -10]  # dB

# TODO: 对每个 SNR 级别
#   - 用传统方案传输 10 张测试图
#   - 用语义通信传输同一批图
#   - 计算两种方案的重建 PSNR
#   - 绘制对比图矩阵

# TODO: 回答：SNR=-10dB 时，传统方案完全失效，语义方案仍能辨识数字吗？
```

## 数据分析要求

1. **重建 PSNR vs SNR 曲线**：两条线（传统 vs 语义），标注关键 SNR 点
2. **可视化对比矩阵**：5 张图 × 5 个 SNR × 两种方案，共 50 张子图
3. **核心分析**：语义通信"牺牲了什么，换来了什么"？为什么适合 6G？

## 评分细则（15 分）

| 评分项 | 分值 | 判定标准 |
|---|---|---|
| 模型实现 | 5 | 自编码器 + 信道噪声完整实现，训练收敛 |
| 对比实验 | 5 | 5 个 SNR 级别的对比完整，PSNR 曲线合理 |
| 可视化 | 3 | 对比矩阵清晰展示 SNR=-10 时的显著差异 |
| 概念论述 | 2 | 阐述语义通信 trade-off 及 6G 适用场景 |

## 常见错误速查

| 现象 | 原因 | 解决 |
|---|---|---|
| 训练 loss 不下降 | 未加噪声训练 | 在训练循环中加入 SNR=10dB 噪声 |
| 低 SNR 下语义方案也失效 | latent_dim 太小 | 增大到 32 |
| PSNR 曲线两条几乎重合 | 噪声加得太轻 | 检查 SNR 到噪声功率的换算 |
| MNIST 下载失败 | 网络问题 | 用 `download=True` 第一次会缓存 |

## 自检清单

- [ ] 自编码器在无噪声 SNR=20 时完美重建数字
- [ ] SNR=-10dB 时，传统方案 PSNR < 10dB（几乎不可辨识）
- [ ] SNR=-10dB 时，语义方案 PSNR > 15dB（数字可辨识）
- [ ] 报告中用"保存语义 vs 保存像素"的核心概念解释差异
