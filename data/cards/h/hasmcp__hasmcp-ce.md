# hasmcp/hasmcp-ce

⭐ 62 · Go · AGPL-3.0 · 推送 2026-06-06 · [GitHub](https://github.com/hasmcp/hasmcp-ce) · [官网](https://hasmcp.com) · 组织维护

**免代码把 API 端点转成 MCP Server 的网关工具**

面向开发者与 SaaS 提供者的 MCP 服务器构建与网关：读取 OpenAPI Spec v3+/Swagger 自动生成 MCP Server，也支持手动从 API 端点定义 MCP；提供 OAuth2 认证、按服务器切换端点、可选代理头转发、长短期令牌、实时调用日志与分析、Let's Encrypt 自动 SSL。本仓库为社区版（AGPL-3.0，前后端 monorepo，Go+前端），另有闭源的 Pro 与 Enterprise 版及托管云服务，云版含负载优化、用户团队管理、审计日志等附加功能。默认使用 SQLite，可切换 Postgres，推荐以 Docker 运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于 OpenAPI Spec v3+/Swagger 免代码自动生成 MCP Server
- OAuth2 认证与长短期令牌、代理头转发
- 实时 MCP 方法/工具调用日志与服务器分析
- 默认 SQLite、可切换 Postgres，推荐 Docker 部署

## 适用场景

- 把现有 REST API 快速接入 MCP 生态供 AI agent 调用
- 为 SaaS 产品提供 MCP 端点而不自行维护 MCP 规范实现
- 集中管理多个 MCP Server 的端点开关、认证与调用日志

## 场景标签

 · 领域:MCP 基础设施/API 集成

## 证据(README 行号)

> L3: HasMCP is a tool that converts API endpoints into MCP Server without writing a single line of code. It is practical 
> L13: - Automated MCP server creation using OpenAPI Spec v3+ and Swagger

## 星数曲线

```mermaid
xychart-beta
    title "hasmcp/hasmcp-ce 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 61 --> 63
    line [62, 62]
```

2026-10-18 62 → 2026-10-24 62（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `fc0c851edf2d` · [字段定义](../../DATASET.md)*
