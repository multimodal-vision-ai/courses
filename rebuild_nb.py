import json, os

def make_notebook(cells, filename):
    """Create a valid Jupyter notebook from a list of cells."""
    nb = {
        "cells": cells,
        "metadata": {
            "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
            "language_info": {"name": "python", "version": "3.10.0"}
        },
        "nbformat": 4,
        "nbformat_minor": 4
    }
    path = os.path.join(r"C:\Users\guopi\GitHub\courses\future-media-internet\labs\kaggle-demos", filename)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(nb, f, indent=1, ensure_ascii=False)
    print(f"Created: {filename}")

def md(src):
    return {"cell_type": "markdown", "metadata": {}, "source": src}

def code(src):
    return {"cell_type": "code", "execution_count": None, "metadata": {}, "outputs": [], "source": src}

# ===== Demo 2: QoE Optimization =====
make_notebook([
    md([
        "# 实验二（课堂演示）：自适应视频流的 QoE 优化\n\n"
        "**适用课程**：未来媒体互联网\n"
        "**演示时长**：约 12 分钟\n"
        "**运行环境**：Kaggle Notebook（CPU，无外部依赖）\n\n"
        "## 演示目标\n\n"
        "模拟视频播放器面对波动网络带宽时，三种策略的表现对比：\n"
        "- 固定码率（不调节）→ 频繁卡顿\n"
        "- 启发式规则（缓冲区低就降码率）→ 勉强可用\n"
        "- Q-learning 强化学习 → 平稳适应\n\n"
        "让学生直观感受为什么 YouTube/Netflix 需要自适应码率算法。"
    ]),
    code([
        "import numpy as np\n"
        "import matplotlib.pyplot as plt\n"
        "from collections import defaultdict\n\n"
        'print("无外部依赖，纯 NumPy 实现 ✅")'
    ]),
    code([
        "# 模拟网络带宽轨迹（Mbps）：模拟 WiFi 信号波动\n"
        "np.random.seed(42)\n"
        "T = 200  # 200 个时间步（每步 0.5 秒，共 100 秒）\n"
        "t = np.arange(T)\n\n"
        "# 生成波动带宽：均值 8 Mbps，有周期性波动和随机噪声\n"
        "bandwidth = 8 + 3 * np.sin(t * 0.05) + 2 * np.sin(t * 0.15) + np.random.normal(0, 1.5, T)\n"
        "bandwidth = np.clip(bandwidth, 0.5, 15)\n\n"
        "plt.figure(figsize=(14, 4))\n"
        "plt.plot(t * 0.5, bandwidth, 'b-', alpha=0.7, linewidth=1)\n"
        "plt.fill_between(t * 0.5, 0, bandwidth, alpha=0.1, color='blue')\n"
        "plt.axhline(y=2, color='red', linestyle='--', alpha=0.5, label='低码率视频 (2 Mbps)')\n"
        "plt.axhline(y=5, color='orange', linestyle='--', alpha=0.5, label='中码率视频 (5 Mbps)')\n"
        "plt.axhline(y=10, color='green', linestyle='--', alpha=0.5, label='高码率视频 (10 Mbps)')\n"
        "plt.xlabel('时间 (秒)')\n"
        "plt.ylabel('带宽 (Mbps)')\n"
        "plt.title('模拟网络带宽波动（100 秒）')\n"
        "plt.legend()\n"
        "plt.grid(True, alpha=0.3)\n"
        "plt.show()\n"
        'print("三条虚线代表三种可选视频码率。")'
    ]),
], "demo2-qoe-optimization.ipynb")

print("Demo 2 done")
