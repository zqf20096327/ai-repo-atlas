# firebolt-db/mcp-server

⭐ 15 · Go · Apache-2.0 · 推送 2026-10-27 · [GitHub](https://github.com/firebolt-db/mcp-server) · [官网](https://www.firebolt.io/) · 组织维护

**把 LLM 连接到 Firebolt 数据仓库的 MCP 服务器**

Firebolt 官方维护的 Model Context Protocol 服务器，用 Go 编写，使 Claude Desktop、Cursor、VS Code Copilot Chat 等 MCP 客户端能够连接 Firebolt 数据仓库：提供 4 个工具（文档概览、建立连接、执行 SQL、文档搜索）、资源（文档文章与账户/数据库/引擎列表）和 firebolt_expert 预设提示词。支持服务账户或 Firebolt Core URL 两种认证，默认 STDIO 传输，可选 SSE 与 Streamable HTTP。提供官方 Docker 镜像与二进制发布，Cursor 需禁用 resources 方可使用。

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

- 4 个工具：文档概览/连接建立/SQL 查询/文档搜索
- 支持 Firebolt Cloud 服务账户与 Firebolt Core URL 两种接入方式
- 默认 STDIO 传输，可切换 SSE 与 Streamable HTTP
- firebolt_connect 默认要求 LLM 先出示文档阅读证明，可关闭

## 适用场景

- 在 Claude Desktop/Cursor/VS Code 中用自然语言查询 Firebolt 数仓
- 让 AI agent 自主执行 SQL 并基于 Firebolt 文档生成回答
- 通过 Docker 或二进制在自有环境部署 MCP 服务端

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L5: A Model Context Protocol implementation that connects your LLM to Firebolt Data Warehouse
> L197: 1. **Tools** - Task-specific capabilities provided to the LLM:

## 星数曲线

```mermaid
xychart-beta
    title "firebolt-db/mcp-server 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `306612ea6a3a` · [字段定义](../../DATASET.md)*
