# last9/last9-mcp-server

⭐ 63 · Go · Apache-2.0 · 推送 2026-10-25 · [GitHub](https://github.com/last9/last9-mcp-server) · [官网](https://last9.io/mcp) · 组织维护

**把生产可观测数据接入 AI 助手的 MCP 服务器**

Last9 出品的 MCP 服务器，将 Claude、Cursor、Windsurf、VS Code 等 MCP 客户端连接到 Last9 生产可观测数据：日志、指标、链路追踪、异常、数据库查询、告警与部署。提供 Hosted HTTP（OAuth）与自托管 STDIO 两种接入方式，后者可经 Homebrew、npm 或 GitHub Releases 二进制安装。暴露大量工具：服务健康、数据库可观测（PostgreSQL/MySQL/MongoDB/Redis 等）、PromQL 查询、日志与追踪查询。支持 --read-only 模式限制写操作，仅管理员可创建 Refresh Token。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Hosted HTTP OAuth 与自托管 STDIO 两种接入模式
- 覆盖服务健康、数据库可观测、PromQL、日志、追踪的工具集
- --read-only 模式可隐藏全部写工具并按白名单放行
- Node.js 版本要求带安全说明（eMudhra 中间证书问题）

## 适用场景

- 让 AI 编码助手在排查线上问题时直接读取日志、追踪与告警
- 通过对话查询服务性能回归与慢查询
- 在只读模式下安全地把生产监控暴露给 agent

## 场景标签

 · 领域:可观测性/AI Agent 基础设施

## 证据(README 行号)

> L7: Last9 MCP Server connects Claude, Cursor, Windsurf, and any other MCP-capable AI assistant directly to your producti
> L199: ## What It Can Do

## 星数曲线

```mermaid
xychart-beta
    title "last9/last9-mcp-server 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-26"]
    y-axis "stars" 61 --> 64
    line [62, 63, 63]
```

2026-10-18 62 → 2026-10-26 63（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `ca8e664887a3` · [字段定义](../../DATASET.md)*
