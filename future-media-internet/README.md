# 未来媒体互联网（Future Media Internet）

河海大学计算机与软件学院本科生课程。

## 课程简介

介绍多媒体通信与互联网技术的基本原理、体系结构和协议，涵盖物理层传输、媒体接入控制、多媒体传输协议等核心内容，并通过 Wireshark 实验加深对 TCP/IP 协议栈的理解。

## 基本信息

- 授课对象：计算机专业本科生
- 课时安排：32 学时（理论讲授 + 实验）
- 考核方式：课堂表现（30%）+ 实验报告（70%）

## 章节

1. **概论** — 多媒体通信发展、网络分类与体系结构、互联网标准
2. **网络体系结构** — OSI 分层模型、TCP/IP 协议栈及各层功能
3. **物理层简介** — 信号时频特性、传输损伤、信道容量
4. **多路复用与交换技术** — FDM/WDM/TDM、电路交换与分组交换
5. **传输媒介** — 导向型与非导向型传输媒介
6. **媒体接入控制技术** — ALOHA、CSMA 系列协议、受控接入
7. **多媒体传输技术** — 信源编码与压缩、RTP/RTCP 协议

## 课件

| 章节 | 课件 |
|---|---|
| 第 1 讲：概论 | [FMI_Lecture01.pdf](https://github.com/multimodal-vision-ai/courses/raw/main/future-media-internet/slides/FMI_Lecture01.pdf) |
| 第 2 讲：网络体系结构 | [FMI_Lecture02.pdf](https://github.com/multimodal-vision-ai/courses/raw/main/future-media-internet/slides/FMI_Lecture02.pdf) |
| 第 3 讲：物理层（一）| [FMI_Lecture03-1.pdf](https://github.com/multimodal-vision-ai/courses/raw/main/future-media-internet/slides/FMI_Lecture03-1.pdf) |
| 第 3 讲：物理层（二）| [FMI_Lecture03-2.pdf](https://github.com/multimodal-vision-ai/courses/raw/main/future-media-internet/slides/FMI_Lecture03-2.pdf) |
| 第 3 讲：物理层（三）| [FMI_Lecture03-3.pdf](https://github.com/multimodal-vision-ai/courses/raw/main/future-media-internet/slides/FMI_Lecture03-3.pdf) |
| 第 4 讲：多路复用与交换 | [FMI_Lecture04.pdf](https://github.com/multimodal-vision-ai/courses/raw/main/future-media-internet/slides/FMI_Lecture04.pdf) |
| 第 5 讲：传输媒介 | [FMI_Lecture05.pdf](https://github.com/multimodal-vision-ai/courses/raw/main/future-media-internet/slides/FMI_Lecture05.pdf) |
| 第 6 讲：媒体接入控制 | [FMI_Lecture06.pdf](https://github.com/multimodal-vision-ai/courses/raw/main/future-media-internet/slides/FMI_Lecture06.pdf) |


## 实验

Wireshark 抓包实验，涵盖从 IP 层到应用层的协议分析。详见 [labs/README.md](labs/README.md)。

### 课堂演示（Kaggle）

以下 Notebook 可直接在 Kaggle 上运行，适合课堂投影演示：

- [实验一：AI 流量分类](labs/kaggle-demos/demo1-traffic-classification.ipynb)
- [实验二：自适应视频流 QoE](labs/kaggle-demos/demo2-qoe-optimization.ipynb)
- [实验三：AI 视频质量评估](labs/kaggle-demos/demo3-quality-assessment.ipynb)
- [实验四：神经压缩 vs JPEG](labs/kaggle-demos/demo4-neural-compression.ipynb)
- [实验五：语义通信](labs/kaggle-demos/demo5-semantic-communication.ipynb)

Kaggle 部署说明：[kaggle-demos/README.md](labs/kaggle-demos/README.md)

Wireshark 抓包实验，涵盖从 IP 层到应用层的协议分析。详见 [labs/README.md](labs/README.md)。
