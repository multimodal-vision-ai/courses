# FMI Course · Kaggle Hands-on Lab

这里汇总课程导航页和 7 个可直接运行的 Kaggle 实验。第一次进入课程时，
请先打开导航页了解实验顺序、主题和使用方法。

## 从这里开始

- **推荐入口**：[在 Kaggle 打开课程导航页](https://www.kaggle.com/code/guopingtan/fmi-course-kaggle-hands-on-lab-start-here)
- **GitHub 版本**：[查看课程导航 Notebook](00-start-here.ipynb)

公开页面可以直接浏览；如需运行、修改或保存自己的副本，请登录 Kaggle 后点击
**Copy & Edit**，再选择 **Run All**。

## 实验导航

| 实验 | 主题 | Kaggle 在线实验 | GitHub Notebook |
|---|---|---|---|
| Demo 1 | AI Traffic Classification | [打开实验](https://www.kaggle.com/code/guopingtan/fmi-demo1-traffic-classification) | [查看源码](demo1-traffic-classification.ipynb) |
| Demo 2 | Video QoE Optimization | [打开实验](https://www.kaggle.com/code/guopingtan/fmi-demo2-qoe-optimization) | [查看源码](demo2-qoe-optimization.ipynb) |
| Demo 3 | Video Quality Assessment | [打开实验](https://www.kaggle.com/code/guopingtan/fmi-demo3-quality-assessment) | [查看源码](demo3-quality-assessment.ipynb) |
| Demo 4 | Neural Compression vs JPEG | [打开实验](https://www.kaggle.com/code/guopingtan/fmi-demo4-neural-compression) | [查看源码](demo4-neural-compression.ipynb) |
| Demo 5 | Semantic Communication | [打开实验](https://www.kaggle.com/code/guopingtan/fmi-demo5-semantic-communication) | [查看源码](demo5-semantic-communication.ipynb) |
| Demo 6 | HD Video Network Impairments | [打开实验](https://www.kaggle.com/code/guopingtan/fmi-demo-6-network-impairments-on-hd-video) | [查看源码](demo6-hd-video-impairments.ipynb) |
| Demo 7 | VR Video Network Impairments | [打开实验](https://www.kaggle.com/code/guopingtan/fmi-demo-7-network-impairments-on-vr-360-video) | [查看源码](demo7-vr-video-impairments.ipynb) |

## 使用方法

学生可以从课程导航页按顺序访问实验，也可以使用上表直接进入指定 Demo。

## 课堂建议顺序

- **Session 1**：Demo 1（10 分钟）→ Demo 2（12 分钟）
- **Session 2**：Demo 5（10 分钟）→ Demo 6（8 分钟）→ Demo 7（8 分钟）
- **简要介绍**：Demo 3、Demo 4

## 从 Kaggle 同步最新版

Kaggle 是这些展示 Notebook 的最新版本来源。运行以下命令会同时更新课程导航页和
7 个实验：

```bash
python sync_kaggle_demos.py
git diff
```

确认差异和校验结果后，再提交到 GitHub。
