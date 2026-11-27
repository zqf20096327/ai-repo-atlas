# Interactive-Active-AI/NextTransformer

⭐ 504 · Python · MIT · 推送 2026-11-26 · [GitHub](https://github.com/Interactive-Active-AI/NextTransformer) · [官网](https://interactive-active-ai.github.io/NextTransformer/) · 组织维护 · 中文 README

**面向研究者的下一代 Transformer 架构公平基准与自动研究平台**

在同一预算下训练与评估多种语言模型架构（recurrent depth、稀疏与线性注意力、残差变体、混合结构），所有模型共享同一数据（49.152B tokens）、优化器与评测点，训练算力按 ±1% 对齐并被审计记录。提供 observatory（学习曲线、排行榜、模型图谱）、模型 zoo（Hugging Face 权重）与 Arena v2：任何 LLM 可作为 agent 提交经 MCP 工具与计费算力的架构研究任务。支持单机 8 卡与多节点、Slurm 提交训练。

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

- compute-matched 协议：所有模型同数据、同算力预算（±1%）并全程审计
- 模型 zoo 覆盖 Residual/Looped/Sparse/Linear/Hybrid 等架构家族
- Arena v2 支持任意 LLM 以 agent 身份端到端开展架构研究（MCP 工具、计量算力）
- observatory 提供学习曲线、排行榜与 22 个 CORE 任务评测

## 适用场景

- 在公平算力预算下对比不同注意力与残差架构的语言模型
- 让 LLM agent 在统一协议下自动研究新 Transformer 架构
- 下载已评测模型的权重并查看训练曲线与排行榜

## 场景标签

`模型评测` `科研工具` · 领域:评测与运维

## 证据(README 行号)

> L3:  The comprehensive, cutting-edge open-source framework, benchmark and auto-research platform for next-generation Tra
> L25: result is an audited, file-backed record, and AI agents can research new architectures under the very same rules.
> L45: Agent-native research: hand the arena task to your agent; the full version, Arena v2, has been live since November 

## 星数曲线

```mermaid
xychart-beta
    title "Interactive-Active-AI/NextTransformer 星数(近 19 点)"
    x-axis ["2026-11-01", "2026-11-02", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-25", "2026-11-26", "2026-11-27"]
    y-axis "stars" 0 --> 552
    line [16, 87, 393, 402, 404, 408, 411, 412, 421, 457, 476, 481, 483, 487, 489, 492, 493, 498, 504]
```

2026-11-01 16 → 2026-11-27 504（+488）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 high · 依据 README sha `1b0b36b9da95` · [字段定义](../../DATASET.md)*
