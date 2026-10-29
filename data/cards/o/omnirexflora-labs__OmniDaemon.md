# omnirexflora-labs/OmniDaemon

⭐ 56 · Python · MIT · 推送 2025-12-15 · [GitHub](https://github.com/omnirexflora-labs/OmniDaemon) · 组织维护

**事件驱动的 AI Agent 通用运行时：进程隔离与自动恢复**

框架无关的 Python 运行时，将 AI agent（OmniCoreAgent、Google ADK、LangChain、CrewAI、AutoGen 或自定义）以每 agent 独立进程方式运行，由 Agent Supervisor 管理生命周期：故障隔离、崩溃自动重启、健康心跳监测。采用事件驱动通信（当前基于 Redis Stream 事件总线，Kafka/RabbitMQ 标注为开发中），内置重试、DLQ、指标监控、CLI 与 HTTP API，存储后端可通过环境变量切换。运行需先安装 Redis。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 每 agent 独立进程隔离与自动重启的 Agent Supervisor
- 事件驱动通信，当前支持 Redis Stream 总线，Kafka/RabbitMQ 在路线图中
- 内置重试、DLQ、指标监控、CLI 与 HTTP API
- 支持接入 Google ADK、LangChain、CrewAI、AutoGen 等框架的 agent

## 适用场景

- 让后台 AI agent 以事件触发方式长期运行并自动恢复
- 在分布式多服务器环境协调多 agent 系统
- 为生产环境的 agent 工作流提供重试、监控与可观测性

## 场景标签

`Agent 框架` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L18: > **"Kubernetes for AI Agents"** - A production-ready runtime that makes AI agents autonomous, observable, and faul
> L20: OmniDaemon runs **each agent in its own isolated process** (like containers), managed by an Agent Supervisor. This 
> L23: - 🤖 **Run any AI agent** (OmniCoreAgent, Google ADK, LangChain, CrewAI, AutoGen, custom)

## 星数曲线

```mermaid
xychart-beta
    title "omnirexflora-labs/OmniDaemon 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 55 --> 57
    line [56, 56]
```

2026-10-18 56 → 2026-10-29 56（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `01c0a607a1f0` · [字段定义](../../DATASET.md)*
