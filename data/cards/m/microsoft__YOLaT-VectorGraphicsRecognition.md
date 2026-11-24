# microsoft/YOLaT-VectorGraphicsRecognition

⭐ 109 · Python · MIT · 推送 2026-11-23 · [GitHub](https://github.com/microsoft/YOLaT-VectorGraphicsRecognition) · 组织维护

**面向研究者的矢量图形识别模型（YOLaT/YOLaT++）PyTorch 实现**

NeurIPS 2021 与 T-PAMI 2024 论文的官方 PyTorch 实现：将矢量图形的文本表示直接作为输入进行识别，避免栅格化带来的内存开销与结构信息丢失。模型基于图神经网络，YOLaT++ 采用 Primitive/Curve/Point 三层层次结构与位置感知增强策略。README 提供环境搭建（conda + 安装脚本）、Floorplans 与 Diagrams 两个数据集的准备脚本，以及训练与推理命令。面向复现论文结果的研究者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 直接以矢量图形文本为输入，无需栅格化
- YOLaT++ 层次结构：Primitive/Curve/Point 三级
- 提供 Floorplans 与 Diagrams 数据集准备与训练脚本
- 附 NeurIPS21 与 T-PAMI24 论文及引用信息

## 适用场景

- 复现矢量图形识别论文的实验结果
- 在 Floorplans/Diagrams 数据集上训练检测模型
- 研究图神经网络在矢量图形任务上的应用

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L5: This repository is the official PyTorch implementation of our two powerful vector graphics recognition models.
> L13: To summarize, we propose You Only Look at Text series (YOLaT & YOLaT++) which addresses issues with raster graphics
> L58: YOLaT++ is introduced, characterized by a hierarchical structure designed for VGs, spanning three levels: **Primiti


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-24 · 置信度 high · 依据 README sha `094e522e87d3` · [字段定义](../../DATASET.md)*
