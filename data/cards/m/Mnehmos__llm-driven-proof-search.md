# Mnehmos/llm-driven-proof-search

⭐ 10 · Lean · 推送 2026-07-23 · [GitHub](https://github.com/Mnehmos/llm-driven-proof-search) · 个人维护

**供外部 LLM agent 驱动的 Lean4 定理证明 RL 环境与 MCP 服务器**

以 Rust 实现的合成强化学习环境：暴露 MCP 服务器，让外部 agent 宿主（Claude Desktop、Cline、Python RL 循环等）在其中进行以 Lean 4 内核为验证器的定理证明回合。环境本身不含推理代码、SDK、API key 与模型路由，由宿主承担全部模型调用；提供问题注册与保真度审查、回合管理、推理日志 SOP、轨迹导出、7 种模式的证明档案导出及 SFT/RL/DPO 训练数据导出等约 30 个 MCP 工具。面向做形式化数学、证明搜索与 RL 训练的开发者和研究者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | — |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- MCP 服务器接口，任意 MCP 兼容宿主可驱动证明搜索回合
- Lean 4 内核验证，环境自身不含任何推理代码与模型路由
- 轨迹哈希链导出与 training_export（SFT/RL/DPO 结构化 JSON）
- 证明档案 7 种导出模式，含 paper_dossier 与 public_summary

## 适用场景

- 为定理证明任务搭建可复现的 RL/评测环境
- 在 Claude Desktop 等 MCP 宿主中进行形式化数学研究
- 从证明轨迹导出训练数据用于 SFT/DPO
- 管理 Lean 形式化开发的小型模块提交与验证

## 场景标签

`强化学习` `模型评测` · 领域:评测与运维

## 证据(README 行号)

> L7: This is a **synthetic reinforcement learning environment** where an external LLM agent attempts to prove mathematica
> L18: **Key invariant:** LLM-Driven Proof Search Environment contains **no provider SDKs, no API keys, no model routing, 

## 星数曲线

```mermaid
xychart-beta
    title "Mnehmos/llm-driven-proof-search 星数(近 2 点)"
    x-axis ["2026-11-08", "2026-11-27"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-11-08 10 → 2026-11-27 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 high · 依据 README sha `51bbbb91f437` · [字段定义](../../DATASET.md)*
