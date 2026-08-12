# 智能感知与自动驾驶技术

河海大学计算机与软件学院本科生课程。

## 课程简介

介绍智能感知与自动驾驶的基础知识与关键技术，涵盖视觉传感器原理、车道线检测、目标检测和自动驾驶决策控制等核心主题。实验部分基于 OpenCV 和主流深度学习框架，帮助学生掌握从感知到决策的基本流程。

## 基本信息

- 授课对象：计算机及相关专业本科生
- 考核方式：课堂表现 + 实验

## 章节

1. **绪论** — 智能感知与自动驾驶概述
2. **视觉传感器** — 摄像头模型、图像处理基础
3. **自动驾驶车道线检测** — 基于 OpenCV 的传统方法与深度学习方法
4. **自动驾驶目标检测** — YOLO 等检测模型原理与实践
5. **自动驾驶决策控制** — 基于 MetaDrive 的强化学习决策

## 文件结构

- [slides/` — 课件（PDF），按章节命名
- [labs/](labs/) — Jupyter Notebook 实验及环境配置说明

## 实验

| 实验 | 文件 |
|---|---|
| 车道线检测 | `notebooks/Chapter3_OpenCVLLD_Local_V1.0.ipynb` |
| 2D 目标检测 | `notebooks/Chapter4_Selfdriving2DTD_Local_V1.0.ipynb` |
| 交通标志检测 | `notebooks/Chapter4_TrafficSignsDetection_Local_V1.0.ipynb` |
| 决策控制（PPO）| `notebooks/Chapter5_Metadrive_ppo_Decision_V1.0.ipynb` |
| 车道线检测（Kaggle）| `notebooks/kaggle-advanced-lane-detection.ipynb` |
| 目标检测（Kaggle）| `notebooks/Kaggle-kitti-object-detection-yolov8.ipynb` |
| 决策控制（Kaggle）| `notebooks/kaggle-metadrive-double-dueling-dqn.ipynb` |
| 交通标志检测（Kaggle）| `notebooks/kaggle-traffic-signs-detection-using-yolov8.ipynb` |
| 交通密度估计 | `notebooks/kaggle-real-time-traffic-density-estimation-with-yolov8.ipynb` |

环境配置：参见 `labs/metadrive-install-guide.txt`
