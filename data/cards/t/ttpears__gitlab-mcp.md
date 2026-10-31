# ttpears/gitlab-mcp

⭐ 13 · TypeScript · MIT · 推送 2026-10-04 · [GitHub](https://github.com/ttpears/gitlab-mcp) · [官网](https://www.npmjs.com/package/@ttpears/gitlab-mcp-server) · 个人维护

**社区版 GitLab MCP Server：让 MCP 客户端操作任意 GitLab 版本**

面向 GitLab 的社区 MCP 服务器，支持 Free/Premium/Ultimate 各版本，无需 GitLab Duo。以 PAT 认证，提供 stdio 与 streamable HTTP 两种传输；支持 Claude Code、Claude Desktop、LibreChat 等客户端接入。提供约 40 个工具：项目/Issue/MR 搜索与读写、CI/CD 流水线管理、GraphQL schema 内省与自定义查询、仓库浏览、时间跟踪、成就管理等。部署形式包括 npx、npm 全局安装、MCPB 安装包与 Docker 容器；多用户场景支持服务账号只读、严格按用户 PAT、以及代理式 OAuth 2.1（RFC 9728/8414/7591，dual-PKCE）。

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

- 支持 Free/Premium/Ultimate 全部 GitLab 版本，无需 Duo
- GraphQL schema 内省与自定义查询（execute_custom_query）
- stdio + streamable HTTP 传输，PAT/服务账号/逐用户 PAT/代理 OAuth 2.1 多种认证模式
- 覆盖搜索、Issue/MR 读写、CI/CD、时间跟踪、成就管理等约 40 个工具

## 适用场景

- 在 Claude Code 等 IDE 中用 AI 操作 GitLab 仓库与 Issue/MR
- LibreChat 团队部署：服务账号只读 + 用户自带 PAT 写入
- 公开托管实例下让用户以自身 GitLab 身份经 OAuth 免配置 token 接入

## 场景标签

 · 领域:开发者工具/MCP 服务器

## 证据(README 行号)

> L11: A community MCP server for GitLab — works with **any GitLab tier** (Free, Premium, Ultimate), no GitLab Duo require
> L21: |You're running|Go to|

## 星数曲线

```mermaid
xychart-beta
    title "ttpears/gitlab-mcp 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-30", "2026-10-31"]
    y-axis "stars" 11 --> 14
    line [12, 13, 13]
```

2026-10-18 12 → 2026-10-31 13（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `f25a48b453f3` · [字段定义](../../DATASET.md)*
