# atlanhq/agent-toolkit

⭐ 42 · Python · MIT · 推送 2026-10-26 · [GitHub](https://github.com/atlanhq/agent-toolkit) · [官网](https://docs.atlan.com/product/capabilities/atlan-ai/how-tos/atlan-mcp-overview) · 组织维护

**Atlan 数据目录的 AI agent 工具集：MCP 服务与插件**

Atlan 官方维护的仓库，包含与 Atlan 服务交互的工具与协议：一个基于 pyatlan 的 MCP 服务器（提供资产搜索与检索工具）、Claude Code 官方插件（15 个 MCP 工具，覆盖语义搜索、血缘追踪、治理、数据质量与数据网格）以及 agent skills（指导性指令，通过 golden-eval 做 A/B 评测）。注意：本地 MCP 服务器已标记弃用，处于仅维护模式，官方推荐使用托管端点 mcp.atlan.com/mcp。

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

- MCP 服务器通过 pyatlan 提供资产搜索与检索工具
- Claude Code 官方插件含 15 个 MCP 工具（OAuth 接入，无需 API key）
- skills 通过 golden-eval 评测框架做有无技能的 A/B 对比

## 适用场景

- 在 Claude Code 或 Cursor 中用自然语言搜索和管理 Atlan 数据资产
- 通过 MCP 协议让 agent 查询数据血缘与治理信息
- 把 Atlan 接入 Databricks UC 等 MCP 客户端

## 场景标签

 · 领域:数据治理/AI 工具链

## 证据(README 行号)

> L14: This repository contains a collection of tools and protocols for interacting with Atlan services for AI agents. Eac
> L18: ### Model Context Protocol (MCP)
> L20: An MCP server that enables interaction with Atlan services through tool calling. Provides tools for asset search, a

## 星数曲线

```mermaid
xychart-beta
    title "atlanhq/agent-toolkit 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 40 --> 42
    line [41, 41]
```

2026-10-18 41 → 2026-10-28 41（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `8556e0a5e005` · [字段定义](../../DATASET.md)*
