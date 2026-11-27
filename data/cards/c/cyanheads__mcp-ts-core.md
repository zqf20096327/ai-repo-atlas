# cyanheads/mcp-ts-core

⭐ 155 · TypeScript · Apache-2.0 · 推送 2026-11-26 · [GitHub](https://github.com/cyanheads/mcp-ts-core) · [官网](https://www.npmjs.com/package/@cyanheads/mcp-ts-core) · 个人维护

**TypeScript 框架：给开发者构建 MCP 服务器提供运行时与 agent 技能**

面向构建 MCP（Model Context Protocol）服务器的 TypeScript 框架。提供 tool/resource/prompt/appTool 等类型化构建器，通过 createApp() 注册并运行于 Bun、Node.js 24+ 或 Cloudflare Workers；内置 JWT/OAuth 鉴权与作用域检查、租户级存储（in-memory/filesystem/Supabase/Cloudflare D1/KV/R2）、结构化日志与可选 OpenTelemetry、定义 lint 与契约/模糊测试。每个脚手架附带 Agent Skills（设计工具、写测试、安全审查、发布）与 CLAUDE.md/AGENTS.md，由 agent 按 skills 完成构建流程。可选集成（DuckDB、Supabase、OpenTelemetry SDK）为 peer dependencies。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- tool/resource/prompt/MCP Apps 类型化构建器与 createApp() 统一注册
- JWT/OAuth 鉴权、按定义作用域检查、可切换后端的租户级存储
- enrichment/errors 双契约：结果上下文与带恢复指引的声明式错误
- 定义 lint、契约测试、模糊测试，构建期检查而非启动期

## 适用场景

- 把内部 API 或数据集通过 MCP 暴露给 AI agent
- 在 Cloudflare Workers 上托管 MCP 服务
- 用 agent 按 skills 工作流构建、测试并发布 MCP 服务器
- 本地以 stdio 或 HTTP 方式运行 MCP 服务器供客户端连接

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L2:  Agent-native TypeScript framework for building MCP servers.
> L13: Connect an API, a dataset, or a workflow to an AI agent through the Model Context Protocol (MCP). Your project hold
> L59: |Give an assistant useful capabilities|Typed builders for tools, resources, prompts, and interactive MCP Apps|

## 星数曲线

```mermaid
xychart-beta
    title "cyanheads/mcp-ts-core 星数(近 7 点)"
    x-axis ["2026-10-25", "2026-10-31", "2026-11-06", "2026-11-08", "2026-11-13", "2026-11-21", "2026-11-27"]
    y-axis "stars" 151 --> 156
    line [152, 153, 152, 153, 154, 155, 155]
```

2026-10-25 152 → 2026-11-27 155（+3）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 high · 依据 README sha `7fc903133563` · [字段定义](../../DATASET.md)*
