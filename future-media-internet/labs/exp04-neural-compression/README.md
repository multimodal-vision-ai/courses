# 实验四：神经图像压缩 vs JPEG

## 实验目标

对比传统 JPEG 编码和神经压缩（自编码器）在相近压缩比下的重建质量差异，直观感受"学习的威力"。

## 环境准备

```bash
pip install numpy matplotlib pillow torch torchvision jupyter
```

备选：直接使用 [Kaggle Demo Notebook](../kaggle-demos/demo4-neural-compression.ipynb)。

## 实验步骤

### Step 1：构建测试图像集（5 min）

准备 8-10 张包含不同纹理特征的图像（自己拍摄或使用标准测试图如 Lena、Barbara、Peppers）。

```python
test_images = ['img1.png', 'img2.png', ...]
# 确保图像尺寸统一（如 256×256）
```

### Step 2：实现 JPEG 编码器（10 min）

> 📝 **TODO**：用 PIL 实现多级别 JPEG 压缩。

```python
from PIL import Image
import io

def jpeg_compress(img_array, quality):
    """用指定 quality 做 JPEG 压缩，返回重建图和实际比特数"""
    # TODO: PIL 保存为 JPEG buffer，再读回
    # TODO: 计算 bpp = buffer_size * 8 / pixels
    pass
```

### Step 3：实现神经压缩（20 min）

> 📝 **TODO**：构建卷积自编码器并训练。

```python
import torch
import torch.nn as nn

class ConvAutoencoder(nn.Module):
    def __init__(self, latent_channels=8):
        super().__init__()
        # TODO: 编码器（3 层 Conv2d，逐步降采样）
        # TODO: 解码器（3 层 ConvTranspose2d，逐步上采样）

    def forward(self, x):
        # TODO: encode → decode
        pass

# TODO: 训练自编码器（MSE loss，Adam optimizer）
# TODO: 通过改变 latent_channels 控制压缩比
```

### Step 4：率失真对比（10 min）

```python
# TODO: 对每张测试图，计算
#   - JPEG 在 quality=[5,20,50,90] 下的 bpp 和 PSNR
#   - 神经压缩在 latent=[2,4,8,16] 下的 bpp 和 PSNR
# TODO: 绘制率失真曲线（横轴 bpp，纵轴 PSNR）
# TODO: 放大展示高频区域（如图像边缘）的局部差异
```

## 数据分析要求

1. **率失真曲线**：散点图，两条曲线分别标注 JPEG 和 Neural
2. **局部放大对比**：选取高频纹理区域，并排展示两种方法的差异
3. **分析**：神经压缩在什么类型的图像上优势最大？什么情况下 JPEG 仍然更好？

## 评分细则（15 分）

| 评分项 | 分值 | 判定标准 |
|---|---|---|
| 压缩实验完整性 | 4 | ≥3 个 JPEG 质量级 + ≥3 个神经压缩级 |
| 率失真曲线 | 4 | 图表规范，轴标注清晰，对比明显 |
| 视觉对比 | 4 | 用局部放大截图指出块效应 vs 模糊失真的具体差异 |
| 技术理解 | 3 | 简述自编码器和 DCT 的核心区别 |

## 常见错误速查

| 现象 | 原因 | 解决 |
|---|---|---|
| bpp 计算差异巨大 | 未统一图像尺寸 | 所有图 resize 到相同尺寸 |
| 自编码器 loss 不下降 | 学习率过大 | 调小 lr 到 0.0001 |
| 神经压缩 PSNR 不如 JPEG | latent 太小 | 增大 latent_channels |
| CUDA out of memory | 图太大 | 统一 resize 到 128×128 |

## 自检清单

- [ ] 率失真曲线中神经压缩和 JPEG 各有优势区间
- [ ] 局部放大图能清晰展示方块效应 vs 平滑模糊的差异
- [ ] 报告中讨论了"为什么神经压缩还没完全取代 JPEG"
- [ ] 代码包含自编码器结构图示或文字说明
