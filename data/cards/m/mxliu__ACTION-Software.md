# mxliu/ACTION-Software

⭐ — · [GitHub]() · 组织维护

**脑科研者用的 fMRI 分析工具箱：数据增强、脑网络构建与 AI 建模**

面向功能磁共振成像（fMRI）研究者的开源 Python 软件工具箱，提供图形界面，功能覆盖 fMRI 数据增强（BOLD 信号与图增强）、脑网络构建（Pearson 相关、互信息、稀疏表示等 8 类方法）、网络特征提取、机器学习与深度学习模型构建。预训练部分包含 13 种图神经网络编码器（基于 3,806 例公开静息态 fMRI 自监督预训练），另附 5 种联邦学习方法用于多站点研究。深度学习模型通过 Pretrain_*.py / Finetune_*.py 脚本运行，要求输入形状为 (nsub, nlength, nroi) 的时间序列数据。由 UNC-CH 团队维护，学术用户免费使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 13 种图神经网络编码器在 3,806 例静息态 fMRI 上自监督预训练
- 5 种联邦学习方法（FedAvg/FedProx/MOON/pFedMe/LGFedAvg）支持多站点研究
- BOLD 信号与图数据双通道增强、8 类脑网络构建方法
- 提供图形界面与 SVM/XGBoost 等传统机器学习建模流程

## 适用场景

- 对 fMRI 数据做脑网络构建与特征提取
- 微调预训练图神经网络编码器做疾病分类等下游任务
- 跨站点 fMRI 研究中使用联邦学习训练模型

## 场景标签

`科研工具` `微调` · 领域:学习与行业

## 证据(README 行号)

> L6: The Augmentation and Computation Toolbox for braIn netwOrk aNalysis (ACTION) is an open-source Python software, desi
> L73: 1. The feature encoders of ten deep learning models are pretrained on 3,806 unlabeled fMRI scans from public cohort

## 星数曲线

```mermaid
xychart-beta
    title "mxliu/ACTION-Software 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 27 --> 29
    line [28, 28]
```

2026-10-18 28 → 2026-10-30 28（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `a0b822eb08b2` · [字段定义](../../DATASET.md)*
