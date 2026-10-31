# ViTAE-Transformer/ViTAE-Transformer

⭐ 280 · Python · 推送 2026-04-15 · [GitHub](https://github.com/ViTAE-Transformer/ViTAE-Transformer) · 组织维护

**ViTAE/ViTAEv2 视觉 Transformer 论文官方代码库**

NeurIPS'21 与 IJCV'22 论文的官方仓库，提供 ViTAE 与 ViTAEv2 的代码、预训练模型与测试结果。核心机制：通过 reduction cell 与 normal cell 向视觉 Transformer 引入尺度不变性与局部性归纳偏置；ViTAEv2 采用无移位的窗口注意力平衡显存、速度与性能，并以多阶段堆叠支持下游任务。应用覆盖图像分类、目标检测、语义分割、动物姿态估计、抠图与遥感；声明仅限研究用途。

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

- RC/NC 结构引入局部性与尺度不变性归纳偏置
- ViTAEv2 无移位窗口注意力与多阶段堆叠设计
- 覆盖分类、检测、分割、姿态估计、抠图、遥感六类任务
- 提供预训练模型与下游任务代码

## 适用场景

- 复现 ViTAE/ViTAEv2 论文实验结果
- 将预训练模型用于检测、分割、姿态估计等下游任务
- 研究视觉 Transformer 的归纳偏置设计

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L41:  This repository contains the code, models, test results for the paper ViTAE: Vision Transformer Advanced by Explor
> L1: ViTAEv2: Vision Transformer Advanced by Exploring Inductive Bias for Image Recognition and Beyond .svg" >

## 星数曲线

```mermaid
xychart-beta
    title "ViTAE-Transformer/ViTAE-Transformer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 279 --> 281
    line [280, 280]
```

2026-10-18 280 → 2026-10-31 280（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `ddc717447a2c` · [字段定义](../../DATASET.md)*
