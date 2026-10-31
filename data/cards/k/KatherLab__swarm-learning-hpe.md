# KatherLab/swarm-learning-hpe

⭐ 14 · Jupyter Notebook · MIT · 推送 2026-10-19 · [GitHub](https://github.com/KatherLab/swarm-learning-hpe) · 组织维护

**基于 HPE Swarm Learning 的医学影像分布式训练实验库**

面向 Odelia 项目的实验性仓库：在 HPE Swarm Learning 2.2.0 去中心化联邦学习平台上训练组织病理学与放射影像模型，包含 Attention MIL（marugoto_mri，适配 MRI）、3D-CNN（odelia-breast-mri）及生成病理/X光图像的扩散模型（score-based-model、swag-latent-diffusion）。节点间仅共享模型参数而非原始数据。提供自动化脚本完成环境搭建、节点（SN/SWOP/SWCI）启动与日志查看，限定 Ubuntu 20.04/22.04 与 NVIDIA GPU 环境运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 在 HPE Swarm Learning 去中心化框架上训练医学影像模型
- 包含 Attention MIL、3D-CNN 与扩散模型多种实现
- 自动化脚本覆盖环境搭建、节点启动与训练日志查看
- 节点间仅交换模型参数以保留数据隐私

## 适用场景

- 多机构协作在不共享原始数据的前提下训练医学影像模型
- 在 DUKE 乳腺癌 MRI 数据集上做分布式模型训练实验
- 复现或扩展 Odelia 项目的节点部署流程

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L9: 1. SWARM Learning For Histopathology Image Analysis and Radiology Image Analysis
> L14: 5. Working version of odelia-breast-mri for 3D-CNN model by @Gustav. Related instructions please refer to ODELIA.md
> L26: HPE Swarm Learning extends the **concept of federated learning** to **decentralized learning** by adding functional

## 星数曲线

```mermaid
xychart-beta
    title "KatherLab/swarm-learning-hpe 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `54893b84fe02` · [字段定义](../../DATASET.md)*
