# FMI 课程实验

本目录包含两类实验材料：

## 原有实验（保留）

Wireshark 协议分析实验，涵盖 IP、TCP/UDP、HTTP、RTP/RTCP 四组抓包分析。

- 实验手册：[wireshark实验手册(2024版).docx](wireshark实验手册(2024版).docx)
- 报告模板：[未来媒体互联网课程实验报告(2024版).docx](未来媒体互联网课程实验报告(2024版).docx)
- 捕获数据：[captures/](captures/)

## 新增实验（2026 试行）

五组 AI+媒体网络实验，将机器学习、强化学习、神经压缩和语义通信引入课程。

### 实验概览

| # | 实验 | 关联章节 | 分值 | 难度 | 环境 |
|---|---|---|---|---|---|
| 一 | [AI 流量分类](exp01-traffic-classification/) | 概论 + 网络体系结构 | 25 | ⭐ | NumPy + sklearn |
| 二 | [自适应视频流 QoE](exp02-qoe-optimization/) | 多媒体传输 | 25 | ⭐ | 纯 NumPy |
| 三 | [AI 视频质量评估](exp03-quality-assessment/) | 信源编码 | 20 | ⭐⭐ | PyTorch |
| 四 | [神经压缩 vs JPEG](exp04-neural-compression/) | 信源编码 | 15 | ⭐⭐ | PyTorch |
| 五 | [语义通信](exp05-semantic-communication/) | 物理层 | 15 | ⭐⭐ | PyTorch |

实验一、二为基础档（必做），实验三至五为进阶档（三选二，至少完成 35 分）。

### 课堂演示

每组实验均有对应的 Kaggle 演示 Notebook，可在课堂上投影运行，无需学生提前配置环境。

- 演示 Notebook：[kaggle-demos/](kaggle-demos/)
- 部署说明：[kaggle-demos/README.md](kaggle-demos/README.md)

### 使用方式

1. **课前**：教师在 Kaggle 运行对应 Demo Notebook，课堂投影展示核心效果
2. **课中**：分发实验指导书（本目录各 `exp*/README.md`），讲解评分标准
3. **课后**：学生下载 Starter Notebook，在本地或 Kaggle 完成填空并撰写报告

### 评分汇总

| 实验 | 分值 | 提交物 |
|---|---|---|
| 一（必做）| 25 | Notebook + 分析报告（≤800 字）|
| 二（必做）| 25 | Notebook + 分析报告 |
| 三至五（三选二）| 20 + 15 + 15 | Notebook + 分析报告 |
| **总计** | **100** | |

各实验详细评分细则见对应 `README.md`。
