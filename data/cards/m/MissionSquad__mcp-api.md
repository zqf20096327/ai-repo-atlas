# MissionSquad/mcp-api

⭐ 15 · TypeScript · 推送 2026-08-09 · [GitHub](https://github.com/MissionSquad/mcp-api) · [官网](https://missionsquad.ai) · 组织维护

**多用户 MCP 服务器 HTTP 代理网关，含加密密钥管理**

面向 MCP 生态的代理服务器：将多个 MCP 服务器（stdio 或 Streamable HTTP 传输）通过统一 REST API 暴露，支持多用户各自使用隔离的加密凭据访问同一 MCP 服务器实例。密钥以 AES-256-GCM 加密存储于 MongoDB，按需解密用于工具调用；提供 MCP 服务器包的安装、启停、升级与卸载管理，Python 包装入独立 venv。要求 Node.js 20+ 与 MongoDB，提供 Docker/Docker Compose 部署方式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 统一 HTTP API 代理多个 MCP 服务器（stdio 与 Streamable HTTP）
- 用户级凭据隔离，AES-256-GCM 加密存储于 MongoDB
- MCP 包全生命周期管理：安装/启停/升级/卸载，支持 npm 与 pip 包
- HTTP 会话跨进程重启持久化，OAuth refresh token 自动刷新

## 适用场景

- 团队多人共用同一组 MCP 服务器而各自管理凭据
- 集中部署和运维 MCP 服务器，通过 REST API 调用工具
- 以容器化方式对外提供 MCP 工具访问入口

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L3: A scalable HTTP API for Model Context Protocol (MCP) servers with secure secret management.
> L30: MCP API acts as a proxy between clients and MCP servers:
> L36: 5. **MCP Server Communication**: The API communicates with MCP servers using the Model Context Protocol

## 星数曲线

```mermaid
xychart-beta
    title "MissionSquad/mcp-api 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `c9e312c41877` · [字段定义](../../DATASET.md)*
