# Kaggle 演示 Notebook 使用指南

## 上传到 Kaggle

1. 登录 [Kaggle](https://www.kaggle.com/)，点击右上角 **Create → New Notebook**
2. 在 Notebook 编辑器中，点击 **File → Upload Notebook**，选择本目录中的 `.ipynb` 文件
3. 上传后，**File → Save Version** 保存
4. 将 Notebook 设为 **Public**（Settings → Sharing → Public）

## 五个演示 Notebook

| Notebook | 内容 | 运行时间 | 适合场景 |
|---|---|---|---|
| `demo1-traffic-classification.ipynb` | AI 流量分类 | ~1 min | 课堂开门红 |
| `demo2-qoe-optimization.ipynb` | 自适应视频流 QoE | ~1 min | 课堂核心演示 |
| `demo3-quality-assessment.ipynb` | AI 视频质量评估 | ~2 min | 概念引入 |
| `demo4-neural-compression.ipynb` | 神经压缩 vs JPEG | ~1 min | 视觉对比 |
| `demo5-semantic-communication.ipynb` | 语义通信 | ~3 min | 前沿收尾 |

## 推荐课堂使用顺序

- **第一节课**：demo1（10 min）→ demo2（12 min）
- **第二节课**：demo5（10 min）→ 简要展示 demo3/demo4

## 依赖说明

- demo1：无外部依赖（NumPy/Matplotlib/Pandas 预装）
- demo2：无外部依赖（纯 NumPy）
- demo3：PyTorch（Kaggle 预装）
- demo4：PyTorch（Kaggle 预装）
- demo5：PyTorch + torchvision（Kaggle 预装）

所有 Notebook 均可在 Kaggle 免费 CPU 环境运行，无需 GPU。

## 教师准备清单

1. 提前将所有 Notebook 上传到 Kaggle 并设为 Public
2. 课前在 Kaggle 中打开对应 Notebook，确认可以正常运行
3. 课堂上直接点击 **Run All** 展示结果
4. 将 Notebook 链接分享给学生，供课后自行运行和修改
