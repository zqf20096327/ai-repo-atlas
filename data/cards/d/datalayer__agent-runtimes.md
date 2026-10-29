# datalayer/agent-runtimes

⭐ 24 · Python · NOASSERTION · 推送 2026-10-28 · [GitHub](https://github.com/datalayer/agent-runtimes) · [官网](https://agent-runtimes.datalayer.tech) · 组织维护

**多协议 AI Agent 部署与管理统一运行时库**

提供 Python 服务端与 React 组件，用于部署、管理与交互 AI agent：一次部署即可通过 ACP、Vercel AI SDK、AG-UI、MCP-UI、A2A 等多协议访问；支持用 Pydantic AI、LangChain、Jupyter AI 等框架编写 agent。包含 Agent Node 注册与隧道路由机制（依赖 Datalayer Runtimes 服务）、预置聊天 UI 组件、MCP 工具集成、OpenTelemetry 观测、DBOS 持久化执行，以及 runtime/快照/评测 CLI。示例需同时安装 Node 与 Python 依赖栈。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 一次部署多协议访问（ACP/AG-UI/MCP-UI/A2A/Vercel AI SDK）
- 支持 Pydantic AI/LangChain/Jupyter AI 框架编写 agent
- 预置 React 聊天组件与 MCP 工具集成
- runtime、快照与多 agentspec 评测 CLI

## 适用场景

- 将自己的 agent 以多协议形式同时暴露给不同客户端
- 在 Web 应用中嵌入可执行工具的聊天界面
- 对多个 agentspec 变体运行评测并生成对比报告

## 场景标签

`Agent 框架` `模型评测` · 领域:Agent 开发

## 证据(README 行号)

> L10: **Agent Runtimes** is a unified library for deploying, managing, and interacting with AI agents across multiple pro
> L16: 1. **Protocol Abstraction**: One agent, multiple protocols - deploy your agent once and access it through ACP, Verc
> L18: 2. **Framework Flexibility**: Write agents using your preferred framework (Pydantic AI, LangChain, Jupyter AI) whil

## 星数曲线

```mermaid
xychart-beta
    title "datalayer/agent-runtimes 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-25", "2026-10-29"]
    y-axis "stars" 22 --> 25
    line [23, 24, 24]
```

2026-10-18 23 → 2026-10-29 24（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `d3fa471d5f8b` · [字段定义](../../DATASET.md)*
