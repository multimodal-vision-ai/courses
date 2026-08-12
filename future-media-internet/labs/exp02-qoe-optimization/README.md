# 实验二：自适应视频流的 QoE 优化

## 实验目标

实现三种自适应码率（ABR）策略，对比其在波动网络下的 QoE 表现，理解为什么流媒体服务需要自适应算法。

## 环境准备

本实验仅需 NumPy 和 Matplotlib，无外部依赖：

```bash
pip install numpy matplotlib jupyter
```

验证：
```python
python -c "import numpy, matplotlib; print('环境OK')"
```

备选：直接使用 [Kaggle Demo Notebook](../kaggle-demos/demo2-qoe-optimization.ipynb)。

## 实验步骤

### Step 1：理解模拟环境（5 min）

阅读提供的 `simulator.py`（视频播放缓冲模拟器），理解三个核心变量：

- **bandwidth**：当前网络带宽（Mbps），随时间波动
- **buffer**：播放缓冲区（秒），< 0 表示卡顿
- **quality**：选择的视频码率，可选 [2, 5, 10] Mbps

```python
import numpy as np

# 模拟网络带宽
np.random.seed(42)
T = 200
t = np.arange(T)
bandwidth = 8 + 3 * np.sin(t * 0.05) + 2 * np.sin(t * 0.15) + np.random.normal(0, 1.5, T)
bandwidth = np.clip(bandwidth, 0.5, 15)
```

### Step 2：实现固定码率策略（5 min）

```python
def strategy_fixed(buffer, quality, bw, history):
    """始终选择最高码率"""
    # TODO: 返回固定的质量等级（0/1/2 分别对应 2/5/10 Mbps）
    pass
```

### Step 3：实现启发式策略（10 min）

> 📝 **TODO**：设计缓冲区驱动的阈值规则。提示：缓冲 < 3s 降码率避免卡顿，缓冲 > 10s 升码率利用带宽。

```python
def strategy_heuristic(buffer, quality, bw, history):
    """基于缓冲区的启发式调节"""
    # TODO: 实现你的阈值规则
    pass
```

### Step 4：实现 Q-Learning 策略（15 min）

> 📝 **TODO**：完善 Q-table 的更新逻辑。状态 = 缓冲区离散化（0-4 档），动作 = {降码率, 保持, 升码率}。

```python
Q_table = np.zeros((5, 3))  # 5个状态 × 3个动作
alpha = 0.1   # 学习率
gamma = 0.9   # 折扣因子
epsilon = 0.1 # 探索率

def strategy_qlearning(buffer, quality, bw, history):
    # TODO: 离散化 buffer 为 state
    # TODO: ε-greedy 选择动作
    # TODO: 计算奖励（质量 - 卡顿惩罚）
    # TODO: 更新 Q-table
    pass
```

### Step 5：对比分析（10 min）

```python
# 在同一带宽轨迹下运行三种策略
strategies = [
    ('固定高码率', strategy_fixed),
    ('启发式规则', strategy_heuristic),
    ('Q-Learning', strategy_qlearning)
]

# TODO: 对每种策略，记录缓冲区、码率选择、卡顿次数
# TODO: 计算 QoE = 平均质量 - 卡顿次数×3 - 码率切换×0.5
# TODO: 绘制三张时间序列对比图
```

## 数据分析要求

1. **QoE 得分对比**：用表格展示三种策略的得分
2. **时间序列图**：绘制带宽+码率+缓冲区的三合一图
3. **策略分析**：什么时候启发式优于 RL？什么时候 RL 展现出优势？
4. **工程讨论**：为什么实际 YouTube 用启发式而非纯 RL？

## 评分细则（25 分）

| 评分项 | 分值 | 判定标准 |
|---|---|---|
| 三种策略实现 | 8 | 全部正确运行，参数合理 |
| 可视化质量 | 5 | 时间序列图清晰，关键事件（卡顿）有标记 |
| QoE 对比分析 | 7 | 正确计算 QoE 得分，结合图表分析各策略适用场景 |
| 批判性思考 | 5 | 讨论 RL 在真实系统的局限（训练成本、鲁棒性、可解释性）|

## 常见错误速查

| 现象 | 原因 | 解决 |
|---|---|---|
| 缓冲区一路下降到负数 | 码率选太高 | 检查策略函数的返回值范围 |
| Q-table 全为零 | 没有更新逻辑 | 确认 reward 计算和 Q 值更新 |
| 图上有三个子图但看不清 | 未使用 twinx | 码率和缓冲用不同的 y 轴 |
| 卡顿次数为 0 但 QoE 很低 | 切换太频繁 | 检查切换惩罚系数是否合理 |

## 自检清单

- [ ] 三种策略均能跑完 200 步不出错
- [ ] 固定策略有卡顿，启发式卡顿减少，Q-Learning 切换最平稳
- [ ] QoE 得分：RL > 启发式 > 固定
- [ ] 报告解释了"为什么 RL 不一定总是最好"
