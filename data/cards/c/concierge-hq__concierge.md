# concierge-hq/concierge

⭐ 528 · Python · NOASSERTION · 推送 2026-06-09 · [GitHub](https://github.com/concierge-hq/concierge) · [官网](https://platform.getconcierge.app) · 组织维护

**构建 MCP 服务器的 SDK：按工作流渐进披露工具**

面向开发者的 Python SDK（concierge-sdk），用于构建与包装 MCP 服务器。工作在 MCP 协议层：将工具分组为 stages 并定义 transitions，agent 在每一步只看到当前步骤的相关工具；支持步骤间服务端共享会话状态（可跨分布式副本）、大 API 场景下用语义搜索把全部工具收敛为 search_tools/call_tool 两个元工具。可包装任何现有 FastMCP 服务器而不改动原代码，支持 stdio、streamable HTTP、SSE 传输，并提供 concierge init 脚手架 CLI。要求 Python 3.9+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- stages/transitions 渐进披露工具并强制调用顺序
- 会话级共享状态，步骤间传数据不经 LLM
- 语义搜索将 100+ 工具收敛为两个元工具
- 两行代码包装现有 FastMCP 服务器，支持 stdio/HTTP/SSE 传输

## 适用场景

- 我有一个大 API，想让 agent 每步只看到相关工具以降低成本
- 我要给电商等流程强制工具调用顺序
- 我想包装现有 MCP 服务器获得渐进披露能力

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L12: The Model Context Protocol (MCP) is a standardized way to connect AI agents to tools. Instead of exposing a flat li
> L20: pip install concierge-sdk

## 星数曲线

```mermaid
xychart-beta
    title "concierge-hq/concierge 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 527 --> 529
    line [528, 528]
```

2026-10-18 528 → 2026-10-26 528（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `e35727bfe518` · [字段定义](../../DATASET.md)*
