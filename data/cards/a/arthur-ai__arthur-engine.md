# arthur-ai/arthur-engine

⭐ 93 · Python · MIT · 推送 2026-10-28 · [GitHub](https://github.com/arthur-ai/arthur-engine) · [官网](https://arthur.ai) · 组织维护

**AI/ML 工作负载的开发、监控与治理服务：护栏、评测与追踪**

Arthur Engine 提供面向 LLM 应用与生成式 AI 工作流的完整服务：在应用中强制执行护栏（PII/敏感数据泄露、幻觉、提示注入、毒性语言等可配置指标的实时检测）；采集并分析来自任意 agent 工作流或 LLM 应用的 OpenInference OpenTelemetry 追踪，对线上追踪运行持续评测；支持提示词的版本管理与迭代、提示变体实验对比、RAG 流水线端到端评测与监控。传统 ML 模型监控与基准测试需配合 Arthur Platform 使用。安装方式为 Mac/Windows 一键安装脚本，另提供 Claude Code 与 Codex 的引导技能包。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- LLM 应用护栏：PII/敏感数据、幻觉、提示注入、毒性语言等实时检测指标
- 采集 OpenInference OpenTelemetry 追踪并对线上追踪运行持续评测
- 提示词版本管理、变体实验对比与 RAG 流水线端到端评测
- 传统 ML 模型监控（漂移、准确率等指标）需配合 Arthur Platform

## 适用场景

- 为生产环境的 LLM 应用与 agent 工作流加护栏并检测敏感内容
- 对线上 agent 追踪持续评测，自动发现质量回归
- 管理和对比不同提示词变体对质量指标的影响

## 场景标签

`LLM 可观测性` `模型评测` `提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L12: The Arthur Engine provides a **complete service** for developing, monitoring, and governing your AI/ML workloads us
> L14: - **Enforcing Guardrails in your LLM Applications and Generative AI Workflows**
> L18:  - Run continuous evaluations on live traces to catch regressions and quality issues automatically

## 星数曲线

```mermaid
xychart-beta
    title "arthur-ai/arthur-engine 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-26", "2026-10-29"]
    y-axis "stars" 91 --> 94
    line [92, 93, 93]
```

2026-10-18 92 → 2026-10-29 93（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `f20d5d165452` · [字段定义](../../DATASET.md)*
