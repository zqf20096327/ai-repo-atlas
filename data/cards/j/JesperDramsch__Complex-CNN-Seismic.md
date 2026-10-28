# JesperDramsch/Complex-CNN-Seismic

⭐ 32 · Python · Apache-2.0 · 推送 2026-10-12 · [GitHub](https://github.com/JesperDramsch/Complex-CNN-Seismic) · [官网](https://www.sciencedirect.com/science/article/pii/S0098300420306208) · 个人维护

**论文复现代码：复数值 CNN 用于地震相分类**

随论文《Complex-valued neural networks for machine learning on non-stationary physical data》发布的可复现研究代码：在公开地震相分类基准数据上训练复数值卷积神经网络，流程含数据下载与校验（Zenodo，MD5）、预处理（src/data_prep.py）、GPU 集群批量训练（src/mass_train.py）、预测生成（src/save_predictions.py）与数值/定性分析（src/explore.py）。面向科研复现者，未提供安装包或容器，需自行搭建 Keras 环境。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 复数值卷积神经网络的完整训练/预测/分析流程
- 基于公开地震相分类基准数据，提供 MD5 校验
- 按脚本划分：数据预处理、批量训练、预测、分析

## 适用场景

- 复现论文实验结果
- 在地震相分类基准上复现复数值 CNN 方法
- 参考复数值网络在物理数据上的实现

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L2: This repository reproduces "Complex-valued neural networks for machine learning on non-stationary physical data".
> L15: ## Training

## 星数曲线

```mermaid
xychart-beta
    title "JesperDramsch/Complex-CNN-Seismic 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 31 --> 33
    line [32, 32]
```

2026-10-18 32 → 2026-10-28 32（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `9b7b360bea58` · [字段定义](../../DATASET.md)*
