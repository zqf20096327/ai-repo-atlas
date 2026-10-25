# pancsta/secai

⭐ 91 · Go · GPL-3.0 · 推送 2026-10-23 · [GitHub](https://github.com/pancsta/secai) · [官网](https://ai-gents.work) · 个人维护

**Golang 本地优先 AI agent/工作流框架，含嵌入式开发工具**

基于 asyncmachine-go 状态机的 Golang 框架，用于构建本地优先的 AI 工作流与长生命周期 agent。核心机制包括：多提示 agent（每个状态可绑定带独立历史的 prompt）、原子状态共识与协商、基于 JSON schema 的结构化提示输入输出、嵌入式 SQLite 记忆与 prompt 历史、主动式 stories。每个 bot 附带调试器、REPL、图示、DB 浏览器等开发工具，可打包为单文件。面向希望以状态机方式精确建模 agent 行为（含中断、并发、容错）的开发者。以 git clone 源码方式开始，需 Golang 工具链；v0.3.0 起采用 GPL 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多提示 agent 架构：每个状态可绑定带独立历史与文档的 prompt
- 原子状态共识与协商，图式执行流支持中断与容错
- 嵌入式开发工具：调试器、REPL、D2 图示、DB 浏览器、OpenTelemetry/Prometheus/Loki 可观测性
- agent 可通过 aRPC 跨多服务器与浏览器分布，底层引擎不依赖 AI

## 适用场景

- 以状态机精确建模复杂、长生命周期的 AI agent 行为
- 构建需要中断、并发与容错能力的本地优先 AI 工作流
- 借助嵌入式调试器与 REPL 对 agent 执行流做细粒度调试
- 通过 DSL 层面定义 bot schema（面向非编码作者）

## 场景标签

`Agent 框架` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L3: **secai** is a Golang framework for _Local-first AI Workflows_, implemented using a special state machine which exce
> L253: **secai** differs from other AI agents / workflows frameworks in the way it treats AI prompts. Most frameworks cal

## 星数曲线

```mermaid
xychart-beta
    title "pancsta/secai 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-25"]
    y-axis "stars" 89 --> 92
    line [90, 91, 91]
```

2026-10-18 90 → 2026-10-25 91（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `22081487258c` · [字段定义](../../DATASET.md)*
