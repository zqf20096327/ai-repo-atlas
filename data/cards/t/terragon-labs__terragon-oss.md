# terragon-labs/terragon-oss

⭐ 261 · TypeScript · Apache-2.0 · 推送 2026-02-10 · [GitHub](https://github.com/terragon-labs/terragon-oss) · [官网](https://www.terragonlabs.com/) · 组织维护

**云端编码代理编排器：在云端沙箱运行 Claude Code 等编码 CLI**

Terragon 的开源停服快照：将开发任务委派给云端编码代理（Claude Code、OpenAI Codex、Amp、Gemini 等），每个代理在隔离沙箱容器中运行并拥有仓库独立副本；任务自动分配分支，提交 AI 生成的 commit 与 Pull Request；提供 terry CLI 做本地接管、MCP server 管理任务，支持 BYO 订阅或自有 API key、定时/事件触发自动化及 Slack/GitHub 集成。声明为 as-is 快照，不保证维护。本地开发需 Node.js v20+、pnpm、Docker（PostgreSQL/Redis）、Stripe CLI 及多项外部服务凭据。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多编码代理支持（Claude Code、Codex、Amp、Gemini）
- 每代理独立沙箱容器隔离运行
- 自动分支分配、AI 生成 commit 与 PR 的 Git 工作流
- terry CLI 本地接管与 MCP server 任务管理

## 适用场景

- 把编码任务委派给云端代理并行处理
- 通过 Slack/GitHub @提及直接发起代理任务
- 配置 issue/PR 触发的自动化开发流程

## 场景标签

`编码 Agent` `工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L13: - **Multi-Agent Support**: Use multiple coding agents, including Claude Code, OpenAI Codex, Amp, and Gemini. Easily
> L16: - **Local Handoff & MCP**: The `terry` CLI tool enables easy local task takeover and continuation. It also includes

## 星数曲线

```mermaid
xychart-beta
    title "terragon-labs/terragon-oss 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 260 --> 262
    line [261, 261]
```

2026-10-18 261 → 2026-10-29 261（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `52f9144e1e60` · [字段定义](../../DATASET.md)*
