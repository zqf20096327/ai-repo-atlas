# haroldadmin/fastify-mcp

⭐ 27 · TypeScript · Apache-2.0 · 推送 2026-05-12 · [GitHub](https://github.com/haroldadmin/fastify-mcp) · [官网](https://www.npmjs.com/package/fastify-mcp) · 个人维护

**Fastify 插件：在 Fastify 应用中运行 MCP 服务器**

Node.js 库，以 Fastify 插件形式将 Model Context Protocol 服务器集成到 Fastify 应用，支持 Streamable HTTP 传输与旧版 HTTP+SSE 传输。由于 MCP TypeScript SDK 官方不内置多会话管理，包内通过内存中 session ID 到会话的映射管理多个活动会话，并提供 Sessions 类发出 connected/terminated/error 事件。面向使用 Fastify 构建 MCP 服务器的开发者，通过 npm/yarn 安装。

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

- 以 Fastify 插件注册 MCP 服务器
- 支持 Streamable HTTP 与旧版 HTTP+SSE 传输
- 内存 session ID 映射管理多会话，Sessions 类提供 connected/terminated/error 事件

## 适用场景

- 在现有 Fastify 应用中挂载 MCP 服务器
- 需要多会话管理的 MCP HTTP 服务部署
- 从旧版 HTTP+SSE 迁移到 Streamable HTTP 传输

## 场景标签

 · 领域:AI 基础设施/MCP 服务器

## 证据(README 行号)

> L3: Integrate Model Context Protocol servers with your Fastify app.
> L5: Supports the Streamable HTTP transport as well as the legacy HTTP+SSE transport.

## 星数曲线

```mermaid
xychart-beta
    title "haroldadmin/fastify-mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-29 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `d03c6ac2b816` · [字段定义](../../DATASET.md)*
