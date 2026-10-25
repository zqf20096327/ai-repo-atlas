# tianyu0207/CCD

⭐ 48 · Python · 推送 2025-10-29 · [GitHub](https://github.com/tianyu0207/CCD) · 个人维护

**MICCAI 2021 论文官方实现：医学图像无监督异常检测**

论文《Constrained Contrastive Distribution Learning for Unsupervised Anomaly Detection and Localisation in Medical Images》（MICCAI 2021）的 PyTorch 官方代码库，作者来自阿德莱德大学等机构。代码基于 SCAN 框架构建，在 Hyper-Kvasir 数据集上训练，用户需自行下载数据集并按需修改 dataloader 后通过 python simclr.py 命令运行。README 仅包含数据集说明、训练命令与引用信息，无安装依赖清单与预训练模型。

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

- PyTorch 实现论文提出的约束对比分布学习方法
- 无监督医学图像异常检测与定位
- 基于 SCAN 代码构建，可修改 dataloader 适配自有医学影像

## 适用场景

- 复现 MICCAI 2021 论文的异常检测实验
- 在自有医学影像数据上做无监督异常检测研究
- 作为异常检测研究的对比基线引用

## 场景标签

 · 领域:医学影像/深度学习

## 证据(README 行号)

> L2: This repo contains the Pytorch implementation of our paper:
> L3: > **Constrained Contrastive Distribution Learning for Unsupervised Anomaly Detection and Localisation in Medical Ima
> L16: Modify the dataloader (data/lag_loader.py) code for your own medical images, then simply run the following command:

## 星数曲线

```mermaid
xychart-beta
    title "tianyu0207/CCD 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 47 --> 49
    line [48, 48]
```

2026-10-18 48 → 2026-10-25 48（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `00dafb38464a` · [字段定义](../../DATASET.md)*
