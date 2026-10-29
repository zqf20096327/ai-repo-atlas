# devdotbo/perplexity-web-mcp

⭐ 20 · Python · MIT · 推送 2026-05-01 · [GitHub](https://github.com/devdotbo/perplexity-web-mcp) · 个人维护

**通过订阅访问 Perplexity 网页接口的 MCP 服务器/CLI/API 网关**

为 Perplexity AI 网页接口提供三种访问形态：终端 CLI（ask/research/council 等命令）、22 个工具的 MCP 服务器、以及 Anthropic Messages 与 OpenAI Chat Completions 兼容的本地 API 服务器，供 Claude Code、Cursor 等 MCP 客户端或任意兼容客户端调用 8 种模型并附引用。依赖 Perplexity Pro/Max 订阅，经非官方未公开接口交互，README 声明可能随时失效且与 Perplexity 无关，自述为学习项目仅供研究与教育用途。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- CLI 覆盖问答、Deep Research、多模型 Council 并行与配额查询
- 22 个 MCP 工具，支持来源聚焦、thinking 模式与配额感知路由
- 本地 API 服务器兼容 Anthropic Messages 与 OpenAI Chat Completions 端点
- 自动配置 Claude Code、Cursor 等 7 个客户端的 MCP 并跨 9 平台安装技能

## 适用场景

- 在终端用 Perplexity 订阅查询并附带引用来源
- 给 Claude Code 或 Cursor 挂载 Perplexity 搜索/研究工具
- 让依赖 Anthropic/OpenAI API 的工具改走本地 Perplexity 通道

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L11: MCP server, CLI, and API-compatible interface for Perplexity AI's web interface.
> L18: - **MCP Server**: 22 MCP tools for AI agents with citations, source discovery, and rate limit checking
> L19: - **API Server**: Drop-in Anthropic Messages API and OpenAI Chat Completions API

## 星数曲线

```mermaid
xychart-beta
    title "devdotbo/perplexity-web-mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-29 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `01afac6cac82` · [字段定义](../../DATASET.md)*
