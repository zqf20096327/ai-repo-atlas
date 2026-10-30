# assembledhq/143

⭐ 20 · Go · MIT · 推送 2026-10-29 · [GitHub](https://github.com/assembledhq/143) · [官网](https://143.dev) · 组织维护

**团队共享的编码 Agent 运行平台：沙箱执行并产出 PR**

面向团队的开源编码 Agent 基础设施：连接 GitHub 仓库与 Linear、Sentry、Slack、Notion、PagerDuty 等上下文工具，从浏览器、Slack 或手机发起任务，在 Docker/gVisor 隔离沙箱中运行自选的编码 Agent（Codex、Claude Code、OpenCode、Amp、Pi），产出可评审的分支或 PR，附 diff、transcript、检查与实时预览。后端为 Go+Postgres，前端 Next.js。提供 143.dev 托管服务与自托管两条路径，自托管需自备基础设施与 LLM/Agent 凭证，本地运行需 Go 1.24+、Node.js 24+、PostgreSQL 17。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Docker/gVisor 隔离沙箱中运行团队选定的编码 Agent
- 通过适配器接入 Codex、Claude Code、OpenCode、Amp、Pi 等多种 Agent
- 集成 GitHub、Linear、Sentry、Slack、Notion、PagerDuty 等上下文源
- 输出分支/PR 及 diff、transcript、检查、实时预览

## 适用场景

- 团队在共享工作区中运行编码 Agent 完成 issue 到 PR 的流程
- 支持/产品等非工程角色在受限工作流中发起 Agent 任务
- 自托管地以沙箱基础设施运行公司内部的编码 Agent

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L5: 143 is an open-source platform where your whole team builds software together, running coding agents in the cloud an
> L23: - **Bring the agent you prefer:** 143 is built around coding-agent adapters (Codex, Claude Code, OpenCode, Amp, Pi)
> L34: 3. 143 spins up an isolated sandbox, checks out the repo, and runs your chosen agent.

## 星数曲线

```mermaid
xychart-beta
    title "assembledhq/143 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-30 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `ec485700610b` · [字段定义](../../DATASET.md)*
