# 实验一：AI 驱动的网络流量分类

## 实验目标

使用机器学习方法自动识别网络流量类型，理解"统计特征"优于"端口号分类"的原因。

## 环境准备

### 1. 安装 Python 环境

推荐 Anaconda，或直接使用 Kaggle Notebook（免安装）。

### 2. 安装依赖

```bash
pip install numpy pandas matplotlib scikit-learn scapy seaborn jupyter
```

### 3. 验证环境

在终端运行以下命令，确认无报错：

```python
python -c "import numpy, pandas, sklearn, scapy; print('环境OK')"
```

备选：直接使用 [Kaggle Demo Notebook](../kaggle-demos/demo1-traffic-classification.ipynb)（免配置）。

## 实验步骤

### Step 1：加载捕获数据（5 min）

```python
from scapy.all import rdpcap

# 加载所有 pcapng 文件
pcap_dir = "../captures/"
files = ["实验一_IP.pcapng", "实验一_ping.pcapng", "实验一_tracert.pcapng",
         "实验二_TCP.pcapng", "实验二_UDP_DNS.pcapng",
         "实验三_HTTP.pcapng", "实验四_RTP_RTCP.pcapng"]

packets = []
for f in files:
    packets.extend(rdpcap(pcap_dir + f))

print(f"加载 {len(packets)} 个数据包")
```

**预期输出**：显示加载了数百个数据包。

### Step 2：提取流量特征（15 min）

> 📝 **TODO**：补全以下特征提取函数。提示：用 `pkt.haslayer('IP')` 判断是否 IP 包，`pkt['IP'].len` 获取长度，`pkt.time` 获取时间戳。

```python
flows = {}  # 按五元组聚合流量

for pkt in packets:
    if not pkt.haslayer('IP'):
        continue

    # TODO: 提取五元组 (src_ip, dst_ip, src_port, dst_port, proto)
    five_tuple = (pkt['IP'].src, pkt['IP'].dst,
                  # TODO: 补全端口和协议
                  )

    if five_tuple not in flows:
        flows[five_tuple] = {'times': [], 'lengths': []}

    flows[five_tuple]['times'].append(pkt.time)
    flows[five_tuple]['lengths'].append(pkt['IP'].len)

# TODO: 计算每条流的特征，生成 DataFrame
# 特征应包含：pkt_len_mean, pkt_len_var, gap_mean, gap_var, bytes, port
```

**预期输出**：一个包含数百条流记录的 DataFrame。

### Step 3：训练分类器（10 min）

```python
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier

# TODO: 划分训练集和测试集 (70/30)

# TODO: 训练 KNN 和决策树两种分类器

# TODO: 分别用"仅端口号"和"统计特征"进行训练，对比准确率
```

**预期输出**：
```
仅用端口号: 准确率 ~60%
统计特征:   准确率 ~90%+
```

### Step 4：分析结果（10 min）

```python
from sklearn.metrics import confusion_matrix
import seaborn as sns

# TODO: 绘制混淆矩阵
# TODO: 分析哪两类流量最容易混淆，从协议原理角度解释
```

## 数据分析要求

报告需包含以下三项：

1. **混淆矩阵分析**：哪两类流量最容易混淆？从 TCP/UDP/端口复用等角度解释。
2. **特征重要性讨论**：哪个特征对分类贡献最大？为什么？
3. **局限性讨论**：当前方法的局限（如加密流量、样本不均衡），如何改进？

## 评分细则（25 分）

| 评分项 | 分值 | 判定标准 |
|---|---|---|
| 特征提取 | 6 | 正确提取 ≥5 种特征，代码可运行 |
| 分类实验 | 6 | 至少对比 2 种特征组合 + 2 种分类器 |
| 混淆矩阵分析 | 5 | 准确指出易混淆流量对，给出合理的协议层解释 |
| 特征重要性讨论 | 5 | 解释统计特征优于端口号的原因，结合具体协议行为 |
| 报告质量 | 3 | 结构清晰，图表规范，有独立思考 |

## 常见错误速查

| 现象 | 原因 | 解决 |
|---|---|---|
| `ImportError: No module named 'scapy'` | 未安装 | `pip install scapy` |
| `OSError: [Errno 22]` 加载 pcapng | 路径错误 | 使用绝对路径或确认文件存在 |
| scipy Windows 报错 | 缺 Npcap | 下载安装 [Npcap](https://npcap.com/) |
| 准确率始终很低 | 特征计算有误 | 打印单个流的特征值，人工检查合理性 |

## 自检清单

实验完成后，对照以下问题自查：

- [ ] 代码运行无报错，所有图表正常生成
- [ ] 特征提取正确（检查：Web 流的包长均值应该在 500-1500 范围）
- [ ] 混淆矩阵非全零，对角线数值最高
- [ ] 报告中引用了具体的协议知识来解释分类结果
- [ ] 讨论了至少一个改进方向
