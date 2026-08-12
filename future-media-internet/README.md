# 未来媒体互联网（Future Media Internet）

河海大学计算机与软件学院本科生课程。

## 课程简介

介绍多媒体通信与互联网技术的基本原理、体系结构和协议，涵盖物理层传输、媒体接入控制、多媒体传输协议等核心内容，并通过协议分析和 AI 实验加深理解。

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
| 第 1 讲：概论 | [FMI_Lecture01.pdf](slides/FMI_Lecture01.pdf) |
| 第 2 讲：网络体系结构 | [FMI_Lecture02.pdf](slides/FMI_Lecture02.pdf) |
| 第 3 讲：物理层（一）| [FMI_Lecture03-1.pdf](slides/FMI_Lecture03-1.pdf) |
| 第 3 讲：物理层（二）| [FMI_Lecture03-2.pdf](slides/FMI_Lecture03-2.pdf) |
| 第 3 讲：物理层（三）| [FMI_Lecture03-3.pdf](slides/FMI_Lecture03-3.pdf) |
| 第 4 讲：多路复用与交换 | [FMI_Lecture04.pdf](slides/FMI_Lecture04.pdf) |
| 第 5 讲：传输媒介 | [FMI_Lecture05.pdf](slides/FMI_Lecture05.pdf) |
| 第 6 讲：媒体接入控制 | [FMI_Lecture06.pdf](slides/FMI_Lecture06.pdf) |

## 实验

### 原有实验

Wireshark 协议分析实验（IP/TCP/HTTP/RTP），详见 [labs/](labs/)。

### 新增 AI 实验（2026 试行）

五组 AI+媒体网络实验，含 Kaggle 课堂演示和完整学生指导书：

| # | 实验 | 分值 | 指导书 |
|---|---|---|---|
| 一 | AI 流量分类 | 25 | [exp01](labs/exp01-traffic-classification/) |
| 二 | 自适应视频流 QoE | 25 | [exp02](labs/exp02-qoe-optimization/) |
| 三 | AI 视频质量评估 | 20 | [exp03](labs/exp03-quality-assessment/) |
| 四 | 神经压缩 vs JPEG | 15 | [exp04](labs/exp04-neural-compression/) |
| 五 | 语义通信 | 15 | [exp05](labs/exp05-semantic-communication/) |

课堂演示：[Kaggle Demo Notebooks](labs/kaggle-demos/) | 教师准备：[教师准备清单](labs/教师准备清单.md)
