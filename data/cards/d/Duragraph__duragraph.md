# Duragraph/duragraph

⭐ 162 · Go · Apache-2.0 · 推送 2026-09-30 · [GitHub](https://github.com/Duragraph/duragraph) · [官网](https://duragraph.ai) · 组织维护

**面向 AI agent 的自托管持久化工作流编排引擎（事件溯源）**

以单二进制形式交付的 agent 工作流控制平面，内嵌 PostgreSQL 与 NATS，`duragraph dev` 即可零配置启动引擎与可视化面板。核心机制：将每次状态迁移作为不可变事件与工作本身在同一事务写入 PostgreSQL，worker 崩溃后可从最后提交状态恢复，每次运行可从事件日志重放，内置 React 面板实时观测节点执行。提供 Python（PyPI）与 Go worker SDK，通过 REST + SSE API 管理 runs/threads/assistants/graphs。README 标注多项功能仍在开发中（多租户、生产 Helm charts、工作流版本化）。自称 'Temporal for AI agents'，采用 Apache 2.0 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 单二进制内嵌 PostgreSQL 与 NATS，零配置启动 dev 模式
- 事件溯源 + CQRS：每次运行可从事件日志重放，worker 崩溃不丢工作
- Python 与 Go worker SDK，REST + SSE API，无需代码生成或 DSL
- 内嵌 React 可视化面板：Playground、Threads、Traces 实时观测

## 适用场景

- 运行需要崩溃恢复与可重放的 tool-calling agent 工作流
- 在企业内自托管 agent 编排并审计每次状态变更
- 通过可视化面板调试与回放 agent 运行轨迹

## 场景标签

`工作流自动化` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L13: > **Temporal for AI agents.** Durable, replayable agent workflows — self-hosted, event-sourced, observable.
> L15: Agent workflows fail unpredictably: workers crash mid-tool-call, LLMs return junk, networks partition, runs hang fo
> L94: Workers connect via the Python or Go SDK and register graph definitions on startup — no code-generation or DSL requ

## 星数曲线

```mermaid
xychart-beta
    title "Duragraph/duragraph 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 161 --> 163
    line [162, 162]
```

2026-10-18 162 → 2026-10-24 162（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 mid · 依据 README sha `995db3c44e7c` · [字段定义](../../DATASET.md)*
