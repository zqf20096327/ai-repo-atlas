# FidarOrg/mcpfoundry

⭐ 15 · TypeScript · MIT · 推送 2026-09-09 · [GitHub](https://github.com/FidarOrg/mcpfoundry) · 组织维护

**从数据库或 OpenAPI 规格生成生产可用 MCP 服务器的 CLI 工具**

面向需要快速构建 MCP 服务器的开发者的脚手架工具：通过 npx 命令内省 SQLite/Postgres 数据库或解析 OpenAPI/Swagger 规格，经模板编译器生成可运行的 Node.js 或 Python MCP 服务器，每个端点/表转为带 Zod/Pydantic 参数校验的工具。SQLite 工具执行真实参数化 SQL，OpenAPI 工具发起真实 HTTP 调用；Postgres 处理器目前为脚手架桩，MySQL/MongoDB 为存根。可选 --secure 开启 JWT 守卫与欺骗金丝雀。生成的项目附 .mcp.json 供 Claude Code/Claude Desktop 接入。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 一条命令将 DB 或 OpenAPI 规格转为可运行的 MCP 服务器
- 工具执行真实参数化 SQL 或 HTTP 调用，非 TODO 桩
- 可选 ZTAI 安全层：JWT 守卫 + 欺骗金丝雀
- 支持 Node.js 与 Python 两种输出、HTTP/stdio 两种传输

## 适用场景

- 把已有 REST API 通过 OpenAPI 规格快速暴露为 MCP 工具
- 把 SQLite 数据库内省为一组 CRUD MCP 工具
- 用 --dry-run 预览将生成的工具清单

## 场景标签

`代码生成` · 领域:编码与开发

## 证据(README 行号)

> L3: ### Create **secure, production-ready MCP servers** from your database or API — in under 5 minutes. ⚒️
> L15: > **Stop hand-writing MCP servers.** Point `mcpfoundry` at a database or an OpenAPI spec and get a clean, runnable,
> L42: |🔌 **DB & OpenAPI**|Introspect SQLite/Postgres into CRUD tools, or convert any OpenAPI/Swagger spec (file **or URL*

## 星数曲线

```mermaid
xychart-beta
    title "FidarOrg/mcpfoundry 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `b525ed33d449` · [字段定义](../../DATASET.md)*
