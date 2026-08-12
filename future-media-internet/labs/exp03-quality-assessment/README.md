# 实验三：AI 驱动的视频质量评估

## 实验目标

对比传统指标（PSNR）和 AI 感知指标（SSIM）在评判图像质量时的差异，理解为什么现代流媒体服务使用 AI 模型评估编码质量。

## 环境准备

```bash
pip install numpy matplotlib pillow torch torchvision jupyter
```

备选：直接使用 [Kaggle Demo Notebook](../kaggle-demos/demo3-quality-assessment.ipynb)。

## 实验步骤

### Step 1：准备测试图像（5 min）

使用提供的 `prepare_images.py` 生成不同压缩程度的测试图像，或自行用手机拍摄同一场景在不同 WhatsApp/微信压缩下的效果。

```python
import numpy as np
from PIL import Image

# 读取原始图和压缩图
original = np.array(Image.open('original.png').convert('L')) / 255.0
versions = []
for q in [90, 50, 20, 5]:  # JPEG 质量因子
    # TODO: 用 PIL 保存并重新读取，模拟压缩效果
    pass
```

### Step 2：计算传统指标 PSNR（5 min）

> 📝 **TODO**：实现 PSNR 计算公式。

```python
def psnr(original, degraded):
    """PSNR = 20 * log10(MAX / sqrt(MSE))"""
    # TODO: 计算 MSE 和 PSNR
    pass
```

### Step 3：计算感知指标 SSIM（15 min）

> 📝 **TODO**：补全 SSIM 的关键步骤。

```python
import torch
import torch.nn.functional as F

def ssim(original, degraded):
    """简化版 SSIM"""
    orig_t = torch.tensor(original).unsqueeze(0).unsqueeze(0).float()
    deg_t = torch.tensor(degraded).unsqueeze(0).unsqueeze(0).float()

    # 1. 计算局部均值（11x11 窗口）
    # TODO: 用 F.avg_pool2d 计算 mu_x 和 mu_y

    # 2. 计算局部方差和协方差
    # TODO: 用公式 VAR(X) = E(X²) - E(X)²

    # 3. 计算 SSIM
    # TODO: 用 SSIM 公式组合亮度、对比度、结构三项

    return ssim_value
```

### Step 4：对比分析（10 min）

```python
# TODO: 对每个压缩版本，计算 PSNR 和 SSIM
# TODO: 绘制"压缩程度 vs PSNR vs SSIM"双轴图
# TODO: 找出"PSNR 高但 SSIM 低"和"PSNR 低但 SSIM 还行"的例子
```

## 数据分析要求

1. **数值对比表**：列出每个版本的 PSNR 和 SSIM
2. **指标差异分析**：选一个"PSNR 和 SSIM 结论相反"的例子，截图对比并解释原因
3. **原理讨论**：为什么 SSIM 比 PSNR 更接近人眼感受？（提示：关注结构信息）

## 评分细则（20 分）

| 评分项 | 分值 | 判定标准 |
|---|---|---|
| PSNR 与 SSIM 实现 | 6 | 代码正确，计算结果合理 |
| 可视化对比 | 5 | 并排展示原图和各压缩版本，标注指标 |
| 指标差异分析 | 6 | 用具体截图解释 PSNR 和 SSIM 差异的根源 |
| 原理讨论 | 3 | 简述 AI 感知模型（如 LPIPS）的基本思路 |

## 常见错误速查

| 现象 | 原因 | 解决 |
|---|---|---|
| SSIM 计算结果为负数 | 方差计算错误 | 检查 `mu_x**2` 的位置 |
| PSNR 全为 inf | 原图和压缩图一样 | 确认压缩有实际效果 |
| torch 导入慢 | 首次加载 | 等待 10-15 秒 |

## 自检清单

- [ ] 至少对比 4 个压缩级别
- [ ] PSNR 随压缩增大而下降
- [ ] SSIM 和 PSNR 的变化趋势不完全一致
- [ ] 报告中包含"PSNR 高 SSIM 低"的具体截图分析
