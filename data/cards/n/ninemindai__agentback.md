# ninemindai/agentback

⭐ 35 · TypeScript · NOASSERTION · 推送 2026-10-18 · [GitHub](https://github.com/ninemindai/agentback) · [官网](https://agentback.dev/) · 组织维护

**单一 Zod schema 同时生成 REST API、MCP 工具与文档的 TS 框架**

面向 API 同时服务人类开发者与 AI agent 场景的 TypeScript 框架：一份 Zod schema 同时产出运行时校验、类型、OpenAPI 3.1 文档、MCP 工具定义、类型化客户端与文档，改 schema 即所有边界同步。DI 核心为 LoopBack 4 DI 的 ESM 移植，支持在 Express/Fastify/Hono/Bun/Deno/Workers 等宿主上通过一个 fetch handler 运行。附带 MCP Inspector、/llms.txt、确认令牌、幂等键、按调用计价等组件。项目自述为 alpha 阶段，API 表面仍可能变化；需 Node 22.18+、ESM-only、TypeScript 7.0。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 一份 Zod schema 生成校验/类型/OpenAPI/MCP schema/客户端/文档
- 基于 LoopBack 4 DI 核心的 ESM 移植（Context/Binding/@inject）
- 宿主可移植：一个 fetch handler 运行于 Node/Fastify/Hono/Bun/Deno/Workers
- MCP 工具表面 token 成本报告与 x402/MPP 计价挑战等安全/计费原语

## 适用场景

- 同一服务同时暴露 REST API 给开发者和 MCP 工具给 AI agent
- 避免 schema 在 OpenAPI、工具清单、客户端间的多处维护漂移
- 为面向 agent 的 API 提供机器可读错误、确认令牌与幂等重试约定

## 场景标签

 · 领域:开发框架/API 基础设施

## 证据(README 行号)

> L10: AgentBack is an **AI-native API/MCP framework for the agent era**, built with
> L11: agents, for agents. It lets REST endpoints, MCP tools, generated docs, typed
> L60: - **MCP** (Model Context Protocol) server with the same decorator style as REST

## 星数曲线

```mermaid
xychart-beta
    title "ninemindai/agentback 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 34 --> 36
    line [35, 35]
```

2026-10-18 35 → 2026-10-28 35（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `c5f41126c1b8` · [字段定义](../../DATASET.md)*
