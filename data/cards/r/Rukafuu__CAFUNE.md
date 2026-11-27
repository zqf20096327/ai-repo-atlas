# Rukafuu/CAFUNE

⭐ 10 · Julia · Apache-2.0 · 推送 2026-09-29 · [GitHub](https://github.com/Rukafuu/CAFUNE) · 个人维护

**面向研究者的 Julia 语言模型引擎：双向掩码扩散结合 SNN 动力学**

实验性语言模型引擎，核心用 Julia 实现：双向 Transformer、RoPE、Spiking Synchrony Attention、PLIF/SFA 神经元与 11D 超立方储备池，采用双向掩码扩散；Python 侧负责数据、RLAIF 评估与可观测性。提供 sanity 训练验证、固定 split 与三 seed 多掩码比例评估报告、7.07M 参数的 CAFUNÉ-mini 实验配置及本地推理与 dashboard。项目声明处于整合阶段，CUDA/Haskell/BitNet/Flair 均为可选集成；推理需先存在训练产出的 checkpoint。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- Julia 核心实现双向掩码扩散语言模型与 SNN 组件（SSA 注意力、PLIF/SFA）
- 三 seed、五档掩码比例（0.10–0.90）的 cross-entropy/accuracy/top-5 评估报告
- ~7.07M 参数 CAFUNÉ-mini 配置，复用 tokenizer 与 split 快速验证假设
- 可选 BitNet 三值权重变体与基于 mmap 的 RLAIF 外部评估

## 适用场景

- 在本地训练并评估一个扩散式语言模型实验架构
- 用 mini 配置快速迭代训练假设而无需跑 45M 模型
- 实验三值权重（BitNet）训练流程

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L5: **Cognição Artificial Fundamentada em Neuromorfologia** — um motor de
> L6: linguagem experimental que combina difusão mascarada bidirecional e dinâmica
> L9: O núcleo atual é escrito em Julia e reúne Transformer bidirecional, RoPE,
> L16: O repositório está em consolidação. A implementação canônica vive em


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 high · 依据 README sha `1b105ff1b5c6` · [字段定义](../../DATASET.md)*
