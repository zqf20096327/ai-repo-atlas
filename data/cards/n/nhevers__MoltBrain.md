# nhevers/MoltBrain

⭐ 252 · TypeScript · NOASSERTION · 推送 2026-03-25 · [GitHub](https://github.com/nhevers/MoltBrain) · 个人维护

**为 Claude Code/OpenClaw 等 agent 提供长期记忆层的插件**

面向 OpenClaw、MoltBook 与 Claude Code 的长期记忆层插件：自动学习并召回项目上下文，提供观察记录、智能搜索、Web 查看器等能力，配置存于 ~/.moltbrain/settings.json，本地 worker 暴露 localhost:37777 的 REST API，并带 CLI 命令（stats/export/search 等）。另提供 Postgres 支撑的付费存储 dapp（x402 微支付）、Virtuals Protocol GAME SDK 插件与 MoltBook MCP 集成。要求 Node.js 18+ 或 Bun 1.0+，AGPL-3.0 许可。

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

- 自动学习并召回项目上下文的长期记忆层
- CLI 命令（stats/export/tag/prune/search）与 localhost:37777 REST API
- Virtuals Protocol GAME SDK 插件（9 个函数）与 MoltBook MCP 集成
- Postgres 支撑的存储 dapp，经 x402 微支付按钱包隔离数据

## 适用场景

- 给 Claude Code / OpenClaw 助手加上跨会话项目记忆
- Virtuals Protocol 链上 agent 接入持久记忆与存储
- 导出、打标签与检索 agent 的历史观察记录

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L3:  Long-term memory layer for OpenClaw, MoltBook & Claude Code that learns and recalls your project context automatica
> L119: GAME SDK plugin that gives any Virtuals Protocol AI agent persistent memory and storage via MoltBrain.
> L177: ## 💻 Claude Code Integration

## 星数曲线

```mermaid
xychart-beta
    title "nhevers/MoltBrain 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 251 --> 253
    line [252, 252]
```

2026-10-18 252 → 2026-10-25 252（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `47e19d557e8c` · [字段定义](../../DATASET.md)*
