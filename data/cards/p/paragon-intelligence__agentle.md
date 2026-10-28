# paragon-intelligence/agentle

⭐ 54 · Python · MIT · 推送 2026-07-01 · [GitHub](https://github.com/paragon-intelligence/agentle) · [官网](https://paragon-intelligence.github.io/agentle/) · 组织维护

**Python AI Agent 开发框架：少量代码构建生产级多智能体**

面向开发者的 Python 3.13+ AI Agent 框架（MIT，PyPI 发布）。提供 Agent/AgentPipeline/AgentTeam 抽象，支持工具调用、Pydantic 结构化输出、MCP 协议接入、文档缓存（InMemory/Redis）；可将 Agent 暴露为带自动文档的 BlackSheep ASGI REST API，内置 HITL 挂起/恢复流程；集成 Langfuse 可观测与自动评分，支持 Streamlit 聊天 UI，并含实验性 WhatsApp（Evolution API）机器人集成。默认示例使用 Google 生成提供器。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- Agent/管线/团队编排，支持工具调用与 Pydantic 结构化输出
- 自动生成带 Scalar 文档的 REST API（BlackSheep ASGI），内置 HITL 挂起/恢复
- Langfuse 可观测集成与四类自动评分（模型层级/工具使用/Token/成本）
- MCP 协议接入外部工具，文档缓存支持 InMemory 与 Redis

## 适用场景

- 用少量代码快速搭建生产级 AI 助手或多 Agent 系统
- 把 Agent 部署为带文档与人审流程的 REST 服务
- 为 Agent 加上追踪、评分与会话（Redis）管理

## 场景标签

`Agent 框架` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L22: agent = Agent(
> L85:  🔗 Agent Pipelines - Chain agents for complex workflows
> L103:  🔌 MCP Integration - Connect to external tools via Model Context Protocol

## 星数曲线

```mermaid
xychart-beta
    title "paragon-intelligence/agentle 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 53 --> 55
    line [54, 54]
```

2026-10-18 54 → 2026-10-28 54（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `76acf8c1f8fe` · [字段定义](../../DATASET.md)*
