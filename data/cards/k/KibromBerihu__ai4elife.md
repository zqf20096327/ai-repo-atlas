# KibromBerihu/ai4elife

⭐ 43 · Python · MIT · 推送 2025-12-12 · [GitHub](https://github.com/KibromBerihu/ai4elife) · 个人维护

**PET 图像淋巴瘤病灶自动分割与生物标志物计算工具**

基于 LFBNet 深度学习方法的数据驱动医学图像分割流水线：将 3D 18F-FDG PET 图像投影为冠状与矢状 MIP 图像，自动分割淋巴瘤病灶，并计算替代生物标志物 sTMTV 与 sDmax，用于 DLBCL 患者的预后预测。输入仅需 SUV 单位的 nifti 格式 PET 图像（CT 非必需），提供预训练权重推理与自数据迁移学习两种用法，支持虚拟环境（conda）与 Docker 两种运行方式，可在桌面机或集群运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- PET MIP 自动分割并计算 sTMTV/sDmax 替代生物标志物
- 仅需 PET（SUV 单位 nifti）即可运行，CT 非必需
- 支持预训练推理与自有数据迁移学习/从头训练
- 提供 conda 环境与 Docker 镜像两种可复现运行方式

## 适用场景

- 对 DLBCL 患者全 PET 图像批量自动分割肿瘤病灶
- 从分割结果自动计算 TMTV/Dmax 类预后生物标志物
- 用自有数据集做迁移学习训练自己的分割模型

## 场景标签

`目标检测` `微调` · 领域:感知与多模态

## 证据(README 行号)

> L19: Here, we developed data-driven AI to calculate surrogate biomarkers for DLBCL patients automatically. Briefly, firs
> L21: an AI algorithm to segment lymphoma regions automatically. From the segmented images, the surrogate TMTV (sTMTV) an
> L36: We adapted the deep learning-based robust medical image segmentation method LFBNet.

## 星数曲线

```mermaid
xychart-beta
    title "KibromBerihu/ai4elife 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 42 --> 44
    line [43, 43]
```

2026-10-18 43 → 2026-10-26 43（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `3b7bf33f2f2d` · [字段定义](../../DATASET.md)*
