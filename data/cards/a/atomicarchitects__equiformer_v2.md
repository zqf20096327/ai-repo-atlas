# atomicarchitects/equiformer_v2

⭐ 353 · Python · MIT · 推送 2026-04-10 · [GitHub](https://github.com/atomicarchitects/equiformer_v2) · [官网](https://arxiv.org/abs/2306.12059) · 组织维护

**面向原子体系的等变 Transformer 官方 PyTorch 实现**

ICLR 2024 论文 EquiformerV2 的官方 PyTorch 实现：一种等变 Transformer 架构，用于在 OC20 S2EF-2M 与 S2EF-All+MD 数据集上训练模型，执行能量与力预测，支持 DeNS 去噪非平衡结构作为辅助任务提升预测表现。提供 31M/153M 规模的训练脚本（多节点多 GPU）及已训练的检查点下载，并给出验证集能量/力 MAE 指标。该模型已被纳入 OCP 仓库并用于 Open Catalyst demo。环境搭建与数据下载依赖外部指引。

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

- 在 OC20 S2EF-2M / All+MD 上的训练代码与脚本
- 提供 S2EF-2M、31M、153M 三组已训练检查点及指标
- 支持 DeNS 去噪辅助自监督任务
- 架构基于 PyTorch、e3nn、PyG 等实现

## 适用场景

- 我在催化剂/原子体系模拟中训练等变 GNN 做能量与力预测
- 我下载检查点直接用于 OC20 S2EF 任务的评估或弛豫计算
- 我基于该架构复现或扩展 ICLR 2024 论文实验

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L5: This repository contains the official PyTorch implementation of the work "EquiformerV2: Improved Equivariant Transfo
> L6: We provide the code for training the base model setting on the OC20 S2EF-2M and S2EF-All+MD datasets.
> L10: In our subsequent work, we find that we can generalize self-supervised learning similar to BERT, which we call **De

## 星数曲线

```mermaid
xychart-beta
    title "atomicarchitects/equiformer_v2 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 352 --> 354
    line [353, 353]
```

2026-10-18 353 → 2026-10-30 353（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `fa994103c095` · [字段定义](../../DATASET.md)*
