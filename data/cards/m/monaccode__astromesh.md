# monaccode/astromesh

⭐ 37 · Python · Apache-2.0 · 推送 2026-10-22 · [GitHub](https://github.com/monaccode/astromesh) · [官网](https://monaccode.github.io/astromesh/) · 组织维护

**多模型 AI agent 运行时：YAML 定义 agent 并按 API 部署**

开源 agent 运行时与配套生态：用 YAML 或 Python（ADK）定义 agent，运行时负责跨模型路由（按成本/延迟、带回退）、7 种编排模式、工具（MCP/A2A）、记忆、RAG、护栏、评估与 OpenTelemetry 观测，并以 REST/WebSocket API 暴露。面向将 agent 推向生产的开发者；含 Docker Compose 全栈（Ollama、Postgres/pgvector、Redis 等）。部分组件（Herald/Nexus/Cortex/Prisma）为闭源独立产品，源码不公开。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- YAML 配置文件定义 agent，无需写代码
- 跨 provider 模型路由（成本/延迟、fallback）与 7 种多 agent 编排模式
- 内置 MCP 工具、A2A、护栏、人类审批、评估（*.eval.yaml）与追踪
- Docker Compose 一键起全栈（运行时+Ollama+pgvector+Redis+监控）

## 适用场景

- 用 YAML/Python 定义并部署多模型 agent 服务
- 统一管理 agent 的路由、记忆、RAG 与护栏
- 需要人类审批写操作和评估回归的 agent 生产化场景

## 场景标签

`Agent 框架` `多智能体` `模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L3:  An open-source runtime for AI agents, and everything around it.
> L57: Most agent frameworks are libraries for writing the agent's logic. Astromesh covers that and

## 星数曲线

```mermaid
xychart-beta
    title "monaccode/astromesh 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-25"]
    y-axis "stars" 35 --> 38
    line [36, 37, 37]
```

2026-10-18 36 → 2026-10-25 37（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `466d57637fb0` · [字段定义](../../DATASET.md)*
