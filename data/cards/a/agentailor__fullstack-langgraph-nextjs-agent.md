# agentailor/fullstack-langgraph-nextjs-agent

⭐ 134 · TypeScript · MIT · 推送 2026-09-04 · [GitHub](https://github.com/agentailor/fullstack-langgraph-nextjs-agent) · 个人维护

**基于 Next.js 与 LangGraph.js 的全栈 AI Agent 开发模板**

面向开发者的生产就绪 Next.js 模板，用于构建 LangGraph.js AI Agent 应用。提供 MCP 动态工具加载（stdio/HTTP 两种传输）、人工审批工具调用（允许/拒绝/修改）、基于 PostgreSQL 的持久会话记忆、多模态文件上传（S3/MinIO 存储）、SSE 实时流式响应，以及 Langfuse 可观测性集成。技术栈为 TypeScript、React 19、Prisma、Tailwind CSS，支持 OpenAI/Google/Anthropic 模型。运行需 Node.js 18+、pnpm、Docker（启动 PostgreSQL 与 MinIO）及至少一家模型 API key。

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

- MCP 集成：通过 Web UI 添加工具服务器，支持 stdio 与 HTTP 传输
- 人工在环工具审批（允许/拒绝/修改参数），可暂停流式执行
- LangGraph checkpointer + PostgreSQL 持久会话记忆，跨会话恢复
- Langfuse 端到端追踪（agent 运行/LLM 调用/工具/token 用量）

## 适用场景

- 快速搭建带人工审批机制的全栈 AI Agent 应用
- 需要持久记忆与多模态文件上传的对话式 Agent 项目
- 通过 MCP 动态接入外部工具而无需改代码

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L3: > **A production-ready Next.js template for building AI agents with LangGraph.js, featuring Model Context Protocol (
> L32: ## Features

## 星数曲线

```mermaid
xychart-beta
    title "agentailor/fullstack-langgraph-nextjs-agent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 133 --> 135
    line [134, 134]
```

2026-10-18 134 → 2026-10-28 134（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `2e5030f27ee1` · [字段定义](../../DATASET.md)*
