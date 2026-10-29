# KenisLabs/arka-mcp-gateway

⭐ 50 · Python · Apache-2.0 · 推送 2025-12-07 · [GitHub](https://github.com/KenisLabs/arka-mcp-gateway) · [官网](https://kenislabs.com/) · 组织维护

**企业 MCP 服务器网关：集中管理接入与用户授权**

面向组织的 MCP（Model Context Protocol）服务器集中网关，社区版提供 GitHub OAuth 登录、管理面板、MCP 服务器目录与配置（GitHub/Gmail/Google Tasks/Slack 等）、集中式 OAuth 凭据管理、按用户会话隔离与工具级启停，通过 Docker Compose 一条命令部署；另设付费企业版（Azure AD/SAML SSO、团队权限、AI Guardrails、审计日志等，见 COMMERCIAL.md）。技术栈为 FastAPI + React + PostgreSQL + Nginx。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 集中管理多个 MCP 服务器的接入与 OAuth 凭据
- 按用户会话隔离与组织级工具启停
- Docker Compose 单命令部署，提供 OpenAPI 文档
- 社区版之外提供含 SSO/AI Guardrails/审计的企业版

## 适用场景

- 组织内统一管控多个 MCP 服务器的访问授权
- 为成员提供自助连接 MCP 服务器的用户面板
- 集中保管各 MCP 服务器的 OAuth 凭据

## 场景标签

 · 领域:AI 基础设施/MCP 网关

## 证据(README 行号)

> L3: A centralized gateway for managing and connecting to multiple MCP (Model Context Protocol) servers. Provides secure,
> L16: - 🎯 **MCP Server Management** - Configure GitHub, Gmail, Google Tasks, Slack, and more

## 星数曲线

```mermaid
xychart-beta
    title "KenisLabs/arka-mcp-gateway 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 49 --> 51
    line [50, 50]
```

2026-10-18 50 → 2026-10-29 50（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `9a756e175816` · [字段定义](../../DATASET.md)*
