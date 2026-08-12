# 实验指南

## 实验目标

通过 Jupyter Notebook 动手实践，掌握自动驾驶感知与决策的核心技术：车道线检测、交通标志识别、目标检测和强化学习决策控制。

## 环境配置

### 基础环境

需要 Python 3.11 及以下依赖：

```
pip install opencv-python opencv-contrib-python
pip install torch torchvision
pip install ultralytics           # YOLOv8
pip install jupyter
```

### MetaDrive（实验五）

实验五需要在仿真环境中训练驾驶策略，配置步骤：

```
# 1. 创建环境
conda create -n metadrive python=3.11
conda activate metadrive

# 2. 安装 PyTorch
pip install torch torchvision torchaudio -f https://mirrors.aliyun.com/pytorch-wheels/cu128/

# 3. 安装依赖
pip install "gymnasium<0.29"
conda install -n metadrive ipykernel --update-deps --force-reinstall

# 4. 安装 MetaDrive
git clone https://github.com/metadriverse/metadrive.git
cd metadrive
pip install -e .
```

在 Kaggle 上运行则只需在 Notebook 开头执行：

```python
%pip install git+https://github.com/metadriverse/metadrive.git
```

## 实验列表

实验按感知到决策的顺序编排，建议按序号依次完成。

### 实验一：OpenCV 基础与车道线检测

[Chapter3_OpenCVLLD_Local_V1.0.ipynb](https://github.com/multimodal-vision-ai/courses/raw/main/intelligent-perception/labs/notebooks/Chapter3_OpenCVLLD_Local_V1.0.ipynb)

学习 OpenCV 图像处理基础（颜色空间转换、边缘检测、ROI 提取），实现基于霍夫变换的车道线检测。

### 实验二：车道线检测进阶

[kaggle-advanced-lane-detection.ipynb](https://github.com/multimodal-vision-ai/courses/raw/main/intelligent-perception/labs/notebooks/kaggle-advanced-lane-detection.ipynb)

使用相机标定和透视变换，实现更鲁棒的车道线检测 pipeline，适用于弯道和复杂光照场景。

### 实验三：交通标志检测

[Chapter4_TrafficSignsDetection_Local_V1.0.ipynb](https://github.com/multimodal-vision-ai/courses/raw/main/intelligent-perception/labs/notebooks/Chapter4_TrafficSignsDetection_Local_V1.0.ipynb)

基于 YOLOv8 训练交通标志检测模型，理解目标检测的数据标注、训练和评估流程。

- 补充：[kaggle-traffic-signs-detection-using-yolov8.ipynb](https://github.com/multimodal-vision-ai/courses/raw/main/intelligent-perception/labs/notebooks/kaggle-traffic-signs-detection-using-yolov8.ipynb) — Kaggle 版本

### 实验四：道路目标检测

[Chapter4_Selfdriving2DTD_Local_V1.0.ipynb](https://github.com/multimodal-vision-ai/courses/raw/main/intelligent-perception/labs/notebooks/Chapter4_Selfdriving2DTD_Local_V1.0.ipynb)

使用 YOLOv8 在自动驾驶场景数据集（KITTI）上进行车辆和行人检测。

- 补充：[Kaggle-kitti-object-detection-yolov8.ipynb](https://github.com/multimodal-vision-ai/courses/raw/main/intelligent-perception/labs/notebooks/Kaggle-kitti-object-detection-yolov8.ipynb) — Kaggle 版本
- 补充：[kaggle-real-time-traffic-density-estimation-with-yolov8.ipynb](https://github.com/multimodal-vision-ai/courses/raw/main/intelligent-perception/labs/notebooks/kaggle-real-time-traffic-density-estimation-with-yolov8.ipynb) — 实时交通密度估计

### 实验五：强化学习决策控制

[Chapter5_Metadrive_ppo_Decision_V1.0.ipynb](https://github.com/multimodal-vision-ai/courses/raw/main/intelligent-perception/labs/notebooks/Chapter5_Metadrive_ppo_Decision_V1.0.ipynb)

在 MetaDrive 仿真环境中使用 PPO 算法训练自动驾驶策略，理解状态空间、动作空间和奖励函数设计。

- 补充：[kaggle-metadrive-double-dueling-dqn.ipynb](https://github.com/multimodal-vision-ai/courses/raw/main/intelligent-perception/labs/notebooks/kaggle-metadrive-double-dueling-dqn.ipynb) — Double Dueling DQN 版本

## 数据集

部分实验需要外部数据集，请从原始来源获取：

- [KITTI Road Segmentation](https://www.cvlibs.net/datasets/kitti/eval_road.php)
- [Waymo Open Dataset](https://waymo.com/open/)
- [Traffic Signs Detection](https://www.kaggle.com/datasets/)

Kaggle 版本的 Notebook 可直接在 Kaggle 平台运行，无需本地配置数据集。

## 评分标准

- 代码运行无误，产生预期输出
- 能解释关键参数的含义和调参依据
- 实验报告包含结果截图、分析和改进思路
