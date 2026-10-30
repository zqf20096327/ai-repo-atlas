# couchbase/mcp-server-couchbase

⭐ 34 · Python · Apache-2.0 · 推送 2026-10-29 · [GitHub](https://github.com/couchbase/mcp-server-couchbase) · [官网](https://docs.couchbase.com/mcp-server/get-started/overview.html) · 组织维护

**连接 AI 客户端与 Couchbase 数据库的自托管 MCP 服务器**

Couchbase 官方维护的 Model Context Protocol 服务器，把 Claude Desktop、Cursor、Windsurf、VS Code Copilot、JetBrains AI Assistant 等 MCP 客户端连接到 Couchbase Server 或 Capella 集群。提供两个子命令服务器：operational（52 个工具，覆盖集群健康、schema 发现、KV 文档读写、SQL++、全文与向量检索、查询性能分析）与 operational-insights（13 个工具）。默认只读、写工具需显式开启；支持 STDIO 与 Streamable HTTP（OAuth 2.1）传输，通过 PyPI、Docker Hub 或源码分发。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- operational 服务器提供 52 个工具：schema 发现、KV 读写、SQL++、全文/向量检索、查询性能分析
- 默认只读模式，写工具需 CB_MCP_READ_ONLY_MODE=false 并可按工具禁用或加确认门
- 支持 STDIO 与 Streamable HTTP（可选 OAuth 2.1，兼容 Auth0/Okta/Keycloak 等 IdP）
- 向量检索工具自动用配置的 Embedding Provider 嵌入查询文本，支持 GSI 与 Search 服务两种路径

## 适用场景

- 让 Claude/Cursor 等 AI 客户端用自然语言查询和管理 Couchbase 数据
- 诊断集群健康与慢查询、获取索引建议
- 在共享部署中以 HTTP + OAuth 2.1 方式供团队访问数据库工具

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L3: Couchbase MCP Server is a self-hosted Model Context Protocol (MCP) server that connects AI agents and assistants — C
> L5: It is read-only by default, supports STDIO and Streamable HTTP (with OAuth 2.1), and is distributed on PyPI and Dock

## 星数曲线

```mermaid
xychart-beta
    title "couchbase/mcp-server-couchbase 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 33 --> 35
    line [34, 34]
```

2026-10-18 34 → 2026-10-30 34（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `f10b6e698391` · [字段定义](../../DATASET.md)*
