# FMI 课程——课堂演示 Notebook

以下 5 个 Jupyter Notebook 部署在 Kaggle 上，适合课堂投影演示。

## 链接

| Demo | 链接 |
|---|---|
| Demo 1：AI 流量分类 | https://www.kaggle.com/code/guopingtan/fmi-demo1-traffic-classification |
| Demo 2：视频 QoE 优化 | https://www.kaggle.com/code/guopingtan/fmi-demo2-qoe-optimization |
| Demo 3：视频质量评估 | https://www.kaggle.com/code/guopingtan/fmi-demo3-quality-assessment |
| Demo 4：神经压缩 vs JPEG | https://www.kaggle.com/code/guopingtan/fmi-demo4-neural-compression |
| Demo 5：语义通信 | https://www.kaggle.com/code/guopingtan/fmi-demo5-semantic-communication |

## 使用方法

### 课堂演示

1. 浏览器打开对应链接（无需登录）
2. 页面展示最后一次 Run All 的执行结果（图表、数据、打印输出）
3. 如需重新执行，点击 **Run All**（需登录 Kaggle 账号）

### 首次部署 / 更新后

上传新版本后，需要执行一次 Run All 以生成预执行结果：

1. 打开链接 → 点击 **Run All**（约 1-3 分钟）
2. 右上角 **Save Version** → 选择 **Save & Run All (Commit)**
3. 之后任何人打开链接都能看到预执行结果

### 学生课后使用

- 无需登录即可查看结果
- 如需修改代码并运行，点击 **Copy & Edit**（Fork 到自己的 Kaggle 账号）

## 推荐课堂顺序

- 第一节课：Demo 1（10 min）→ Demo 2（12 min）
- 第二节课：Demo 5（10 min）→ 简要展示 Demo 3 / 4

## 环境依赖

所有 Notebook 均使用 Kaggle 免费 CPU 环境，预装 PyTorch、scikit-learn、NumPy 等核心库。无需额外配置。

## 更新方法

本地修改 `.ipynb` 文件后，运行仓库根目录下的 `push_cli.py` 即可批量推送到 Kaggle。
