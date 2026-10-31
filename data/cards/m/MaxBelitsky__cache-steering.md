# MaxBelitsky/cache-steering

⭐ 53 · Python · 推送 2026-08-18 · [GitHub](https://github.com/MaxBelitsky/cache-steering) · [官网](https://arxiv.org/abs/2507.08799) · 组织维护

**KV Cache Steering：单次干预算子干预冻结 LLM 行为的方法实现**

论文配套研究代码库：提出通过在推理时修改语言模型的 key-value cache 注入导向向量，以单次干预改变冻结模型行为。论文中用 GPT-4o 生成的推理轨迹导出导向向量，在小模型上诱导 chain-of-thought 推理，也演示风格迁移（如类比推理）。特点：无需重训、无架构改动、无 hook、延迟开销小，兼容标准 transformer 推理管线。提供从零开始的纯 PyTorch + Transformers 实现 notebook、SLURM 实验脚本与复现说明。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 修改 KV cache 的单次干预式行为导向（post-hoc、无 hook、无重训）
- 由 GPT-4o 推理轨迹导出导向向量，在小模型上诱导 CoT 推理
- 提供纯 PyTorch + Transformers 从零实现 notebook
- 含 SLURM 实验脚本，支持在 ARC-c/GSM8K/CSQA/PIQA 上复现实验

## 适用场景

- 在不重训冻结模型的前提下诱导推理或风格行为
- 复现论文中导向向量生成与评测实验
- 将 cache steering 集成到自有推理工作流

## 场景标签

 · 领域:LLM 研究/模型行为控制

## 证据(README 行号)

> L8: **Cache Steering** is a lightweight method for steering the behavior of language models by modifying their key-value
> L39: We provide a notebook with examples on how to use our codebase and a **pure PyTorch + Transformers implementation**

## 星数曲线

```mermaid
xychart-beta
    title "MaxBelitsky/cache-steering 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-31"]
    y-axis "stars" 51 --> 54
    line [52, 53, 53]
```

2026-10-18 52 → 2026-10-31 53（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `d04a730e25f1` · [字段定义](../../DATASET.md)*
