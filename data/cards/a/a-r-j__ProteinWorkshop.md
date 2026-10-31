# a-r-j/ProteinWorkshop

⭐ 279 · Python · MIT · 推送 2026-10-30 · [GitHub](https://github.com/a-r-j/ProteinWorkshop) · [官网](https://proteins.sh/) · 个人维护

**面向蛋白质结构表征学习的基准评测框架（ICLR 2024）**

对应论文 *Evaluating Representation Learning on the Protein Structure Universe*（ICLR 2024）的代码实现：提供大量特征化方案、自监督预训练数据集、下游评测数据集、预训练任务与辅助任务。可作为蛋白质表征学习研究项目的模板、可导入的组件库（数据集/模型/特征化器），或通过 CLI 快速运行预训练与评测配置。收录 GearNet、DimeNet++、GVP-GNN、ESM2 等多类结构编码器，处理后数据与预训练权重可从 Zenodo 下载。安装面向支持 NVIDIA CUDA 的 Linux 系统，Windows 与 macOS 未获官方支持。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 实现论文的蛋白质结构表征学习基准，含特征化方案、预训练/下游数据集与任务
- CLI 快速运行训练/微调/嵌入/可视化/归因（workshop train/finetune 等）
- 组件（数据集、模型、特征化器）可导入到其他项目复用
- 收录 GearNet、DimeNet++、GCPNet、GVP-GNN、ESM2 等多类编码器

## 适用场景

- 作为蛋白质表征学习研究项目的起点模板
- 在统一配置下评测与对比不同蛋白质结构编码器
- 直接复用其数据模块与模型组件构建自己的项目

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L15: This repository provides the code for the protein structure representation learning benchmark detailed in the paper
> L19: The benchmark can be used as a working template for a protein representation learning research project, a library o

## 星数曲线

```mermaid
xychart-beta
    title "a-r-j/ProteinWorkshop 星数(近 2 点)"
    x-axis ["2026-10-30", "2026-10-31"]
    y-axis "stars" 278 --> 280
    line [279, 279]
```

2026-10-30 279 → 2026-10-31 279（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `62a4f96c8344` · [字段定义](../../DATASET.md)*
