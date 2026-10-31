# tobna/WhatTransformerToFavor

⭐ 33 · Python · MIT · 推送 2026-02-25 · [GitHub](https://github.com/tobna/WhatTransformerToFavor) · [官网](https://tobias.nauen-it.de/publication/wtf-benchmark/) · 个人维护

**高效视觉 Transformer 的效率基准评测代码（WACV 2025 论文）**

论文 'Which Transformer to Favor' 的官方代码：对 45+ 种（40 种架构、94 个模型变体）高效视觉 Transformer 在图像分类任务下从头训练，测量准确率、吞吐量与内存等效率指标，并基于 Pareto 前沿分析模型优劣。支持 CIFAR10、ImageNet-21k、ImageNet-1k 数据集，默认通过 slurm 集群运行（srun），可用 -local 标志在本地运行。依赖 timm 与 datadings，提供 main.py 统一入口完成预训练、微调与评测。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 覆盖 40 种架构、94 个模型变体的效率基准
- 从头训练并跟踪准确率、速度、内存等多项效率指标
- 基于 Pareto 前沿的模型效率分析
- 统一入口支持预训练/微调/评测与 slurm 集群运行

## 适用场景

- 为视觉任务选型时比较各 Transformer 的准确率-效率权衡
- 复现论文基准结果或评测自选模型
- 在标准化条件下从头训练高效视觉 Transformer

## 场景标签

`模型评测` `模型训练` · 领域:评测与运维

## 证据(README 行号)

> L12: This is the code for the paper Which Transformer to Favor: A Comparative Analysis of Efficiency in Vision Transform
> L18: To address this gap in comparability, we perform a large-scale benchmark of more than 45 models for image classific

## 星数曲线

```mermaid
xychart-beta
    title "tobna/WhatTransformerToFavor 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 32 --> 34
    line [33, 33]
```

2026-10-18 33 → 2026-10-31 33（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `32d9a7291359` · [字段定义](../../DATASET.md)*
