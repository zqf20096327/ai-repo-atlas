# jafarinia/maxsoft

⭐ 24 · Python · MIT · 推送 2026-02-09 · [GitHub](https://github.com/jafarinia/maxsoft) · 组织维护

**全切片图像分类论文官方实现：MaxSoft 灵活池化 MIL**

NeurIPS 2025 论文 Navigating the MIL Trade-Off: Flexible Pooling for Whole Slide Image Classification 的可运行实现：前向用 max pooling、反向用适度温度的 LSE 梯度（等价 Softmax）以补偿 max pooling 不可微。复现流程含下载数据集（CAMELYON16/17、TCGA-LUNG、SICAP-MIL）、切片切块、折分、SSL（DINO）训练、特征提取与 MIL 训练；提供预训练权重与 embeddings 下载。面向科研复现者。

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

- MaxSoft 池化：前向 max pooling、反向 LSE 梯度（定理 1、2）
- 完整复现管线：切块、折分、SSL 训练、特征提取、MIL 训练
- 提供 4 个数据集的 embedder 权重与 embeddings

## 适用场景

- 复现论文在全切片图像分类上的结果
- 在 CAMELYON/TCGA-LUNG/SICAP-MIL 数据集上做 MIL 实验
- 复用预训练 DINO 权重与 embeddings 做下游研究

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L7: This repository provides a complete, runnable implementation of the paper "Navigating the MIL Trade-Off: Flexible Po
> L30: Maxsoft pooling uses max pooling for the forward pass of Multiple Instance Learning (MIL) training, and the gradien

## 星数曲线

```mermaid
xychart-beta
    title "jafarinia/maxsoft 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-29 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `353a1853f48a` · [字段定义](../../DATASET.md)*
