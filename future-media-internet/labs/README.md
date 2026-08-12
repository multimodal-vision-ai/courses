# Wireshark 实验指南

## 实验目标

通过 Wireshark 捕获并分析真实网络流量，理解 TCP/IP 协议栈各层的工作原理。

## 环境准备

- 安装 [Wireshark](https://www.wireshark.org/download.html)（推荐 4.x 版本）
- 实验手册：[wireshark实验手册(2024版).docx](https://github.com/multimodal-vision-ai/courses/raw/main/future-media-internet/labs/wireshark%E5%AE%9E%E9%AA%8C%E6%89%8B%E5%86%8C(2024%E7%89%88).docx)
- 报告模板：[未来媒体互联网课程实验报告(2024版).docx](https://github.com/multimodal-vision-ai/courses/raw/main/future-media-internet/labs/%E6%9C%AA%E6%9D%A5%E5%AA%92%E4%BD%93%E4%BA%92%E8%81%94%E7%BD%91%E8%AF%BE%E7%A8%8B%E5%AE%9E%E9%AA%8C%E6%8A%A5%E5%91%8A(2024%E7%89%88).docx)

## 实验内容

实验按协议栈层次递进，共四个实验。如果自行抓包有困难，可直接使用 `captures/` 目录中的预捕获数据进行分析。

### 实验一：IP 协议与网络层

分析 IP 数据报结构、分片机制和路由过程。

| 捕获文件 | 内容 |
|---|---|
| [实验一_IP.pcapng](https://github.com/multimodal-vision-ai/courses/raw/main/future-media-internet/labs/captures/%E5%AE%9E%E9%AA%8C%E4%B8%80_IP.pcapng) | IP 数据报示例 |
| [实验一_ping.pcapng](https://github.com/multimodal-vision-ai/courses/raw/main/future-media-internet/labs/captures/%E5%AE%9E%E9%AA%8C%E4%B8%80_ping.pcapng) | ICMP Ping 请求与应答 |
| [实验一_tracert.pcapng](https://github.com/multimodal-vision-ai/courses/raw/main/future-media-internet/labs/captures/%E5%AE%9E%E9%AA%8C%E4%B8%80_tracert.pcapng) | Traceroute 路径探测 |

### 实验二：TCP 与 UDP 传输层

分析 TCP 三次握手、流量控制和 UDP 的无连接通信。

| 捕获文件 | 内容 |
|---|---|
| [实验二_TCP.pcapng](https://github.com/multimodal-vision-ai/courses/raw/main/future-media-internet/labs/captures/%E5%AE%9E%E9%AA%8C%E4%BA%8C_TCP.pcapng) | TCP 连接建立与数据传输 |
| [实验二_UDP_DNS.pcapng](https://github.com/multimodal-vision-ai/courses/raw/main/future-media-internet/labs/captures/%E5%AE%9E%E9%AA%8C%E4%BA%8C_UDP_DNS.pcapng) | UDP 承载的 DNS 查询 |

### 实验三：HTTP 应用层

分析 HTTP 请求/响应报文结构和 Web 通信流程。

| 捕获文件 | 内容 |
|---|---|
| [实验三_HTTP.pcapng](https://github.com/multimodal-vision-ai/courses/raw/main/future-media-internet/labs/captures/%E5%AE%9E%E9%AA%8C%E4%B8%89_HTTP.pcapng) | HTTP GET/POST 请求与响应 |

### 实验四：RTP/RTCP 多媒体传输

分析实时音视频流的 RTP 打包和 RTCP 控制。

| 捕获文件 | 内容 |
|---|---|
| [实验四_RTP_RTCP.pcapng](https://github.com/multimodal-vision-ai/courses/raw/main/future-media-internet/labs/captures/%E5%AE%9E%E9%AA%8C%E5%9B%9B_RTP_RTCP.pcapng) | RTP 媒体流与 RTCP 控制报文 |

## 实验步骤

1. 用 Wireshark 打开 `.pcapng` 文件（`File → Open`）
2. 参照实验手册中各实验的分析要求，使用过滤器（如 `tcp`、`http`、`rtp`）筛选目标流量
3. 观察协议字段，记录关键信息（端口号、序列号、标志位等）
4. 使用 `Statistics → Flow Graph` 查看通信时序
5. 按报告模板撰写实验报告

## 参考

- [Wireshark 官方文档](https://www.wireshark.org/docs/)
- [TCP/IP 协议详解](https://datatracker.ietf.org/)
