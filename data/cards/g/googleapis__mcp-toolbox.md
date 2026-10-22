# googleapis/mcp-toolbox

⭐ 16,700 · Go · Apache-2.0 · 推送 2026-10-21 · [GitHub](https://github.com/googleapis/mcp-toolbox) · [官网](https://mcp-toolbox.dev/documentation/introduction/) · 组织维护

**连接 AI agent/IDE 与企业数据库的开源 MCP 服务器**

Google 维护的 Model Context Protocol 服务器，双用途：一是开箱即用的预置通用工具（如 list_tables、execute_sql），让 Gemini CLI、Claude Code、Codex 等 MCP 客户端直接探索数据库、生成代码；二是通过 tools.yaml 定义结构化查询、语义搜索与 NL2SQL 的自定义工具框架，供生产 agent 集成。内置连接池、IAM 认证与 OpenTelemetry 可观测性。支持 AlloyDB、BigQuery、PostgreSQL、MySQL、MongoDB、Redis 等多种数据库，提供二进制、Docker、Homebrew、Go、npm 等多种安装方式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 动量与使用信号

- 维护:`active` — 距上次 push 1.4 天,年发版 31,167 位贡献者
- 涨星:近 1 天 **+5**(自 20261016 起算)
- 安装:npm 包 `@google/gemini-cli` 月下载 1,647,448
- 平台:— · 协议:MCP

## 能力要点

- 预置通用工具可直接接入 Gemini CLI、Claude Code、Codex 等 MCP 客户端
- tools.yaml 自定义工具框架：结构化查询、语义搜索、NL2SQL
- 支持 AlloyDB、BigQuery、PostgreSQL、MySQL、MongoDB、Redis 等多种数据库
- 内置连接池、IAM 集成认证与 OpenTelemetry 指标与追踪

## 适用场景

- 在 IDE 中用自然语言查询数据库、自动发现与管理 schema
- 为生产环境 agent 构建带访问限制的数据库工具
- 少于 10 行代码将数据库工具集成进 ADK、LangChain 或 LlamaIndex

## 场景标签

`Agent 框架` `数据分析` · 领域:Agent 开发

## 证据(README 行号)

> L18: MCP Toolbox for Databases is an open source Model Context Protocol (MCP) server that connects your AI agents, IDEs,
> L23: 1. **Ready-to-use MCP Server (Build-Time):** Instantly connect Gemini CLI, Google Antigravity, Claude Code, Codex, 
> L24: 2. **Custom Tools Framework (Run-Time):** A robust framework to build specialized, highly secure AI tools for your 

## 星数曲线

```mermaid
xychart-beta
    title "googleapis/mcp-toolbox 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-22"]
    y-axis "stars" 16671 --> 16702
    line [16673, 16684, 16700]
```

2026-10-18 16,673 → 2026-10-22 16,700（+27）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-18 · 置信度 high · 依据 README sha `3c5ff095aec1` · [字段定义](../../DATASET.md)*
