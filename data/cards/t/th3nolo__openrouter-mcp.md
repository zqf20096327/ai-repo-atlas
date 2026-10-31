# th3nolo/openrouter-mcp

⭐ 14 · TypeScript · MIT · 推送 2026-09-29 · [GitHub](https://github.com/th3nolo/openrouter-mcp) · [官网](https://th3nolo.com/articles/openrouter-stateless-mcp-2026-07-28) · 个人维护

**面向 Claude Code 等 MCP 客户端的 OpenRouter 无状态 MCP 服务器与 CLI**

将 agent 接入 OpenRouter 的双入口工具：严格的仅支持 MCP 2026-07-28 的无状态 HTTP/stdio 服务器，以及共享同一操作层的 agent 优先 CLI。暴露 13 个工具（模型目录检索、供应商与端点对比、排名、额度/活动/分析、生成与多模型对比、生成元数据查询）和 1 个 usage 资源。需 Node.js 24 LTS 与 pnpm 12.0.0，从源码构建安装；推理与排名需 API key，额度/活动/分析需独立管理 key。HTTP 模式仅监听 127.0.0.1。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 13 个 MCP 工具覆盖模型目录、供应商、排名、额度、分析与生成
- 严格无状态：仅支持 MCP 2026-07-28，不做会话与旧版回退
- CLI 与 MCP 服务器共享同一操作层，管道输出自动 JSON
- API key 与管理 key 分离的凭证边界

## 适用场景

- 在 Claude Code 等 MCP 客户端中直接调用 OpenRouter 的任意模型
- 通过 CLI 检索与对比 OpenRouter 模型、供应商价格和排名
- 查询账户额度、活动与分析数据

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L1: # OpenRouter MCP server
> L3: This project connects agents to OpenRouter through two front doors: an agent-first command-line interface and a stri
> L5: Version 3.0 targets MCP `2026-07-28` only. Each HTTP POST is independent. The server does not accept `initialize`, c

## 星数曲线

```mermaid
xychart-beta
    title "th3nolo/openrouter-mcp 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-31"]
    y-axis "stars" 12 --> 15
    line [13, 14, 14]
```

2026-10-18 13 → 2026-10-31 14（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `a686aac60d62` · [字段定义](../../DATASET.md)*
