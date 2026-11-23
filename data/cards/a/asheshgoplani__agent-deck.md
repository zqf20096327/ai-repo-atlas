# asheshgoplani/agent-deck

⭐ 1,293 · Go · MIT · 推送 2026-11-22 · [GitHub](https://github.com/asheshgoplani/agent-deck) · [官网](https://discord.gg/e4xSs6NBN8) · 个人维护

**在终端里统一管理多个 AI 编码 agent 会话的 TUI 控制台**

面向同时运行多个 AI 编码 agent（Claude Code、OpenCode、Codex、Gemini 等）的开发者的 Go 语言 TUI 工具：单个终端界面展示所有会话状态，一键切换与附着，支持分组、搜索、会话分叉（继承对话历史）、git worktree、成本看板与 MCP/Skills 管理器。提供 conductor 机制，通过 Telegram/Slack/Discord 等远程通道用手机监督整个 agent 队列。支持 macOS/Linux/Windows(WSL)，经 curl 脚本、Homebrew、go install 或源码安装。

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

- 单终端集中查看与切换多个 AI agent 会话（运行/等待/完成状态）
- 会话分叉继承父对话历史，支持多级分叉探索不同方案
- MCP Manager 与 Skills Manager 免改配置文件按项目/全局挂载能力
- conductor + Telegram bot 远程监督整个 agent 队列，异常升级到手机

## 适用场景

- 同时在多个项目上跑 Claude Code/OpenCode 等 agent，想在一个界面里全部掌控
- 对同一会话分叉出多个分支尝试不同实现方案
- 离开电脑时通过 Telegram/Slack 查看和控制 agent 运行状态

## 场景标签

 · 领域:开发者工具/AI agent 管理

## 证据(README 行号)

> L17: **Agent Deck is mission control for your AI coding agents.** Running Claude Code on ten projects, OpenCode on five 
> L146: ## Quickstart: orchestrate a fleet of AI agents
> L181: ### MCP Manager

## 星数曲线

```mermaid
xychart-beta
    title "asheshgoplani/agent-deck 星数(近 28 点)"
    x-axis ["2026-10-21", "2026-10-22", "2026-10-23", "2026-10-24", "2026-10-25", "2026-10-26", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23"]
    y-axis "stars" 1108 --> 1309
    line [1124, 1133, 1139, 1148, 1154, 1157, 1162, 1171, 1175, 1181, 1188, 1191, 1192, 1154, 1232, 1243, 1248, 1253, 1255, 1258, 1263, 1267, 1273, 1276, 1279, 1283, 1288, 1293]
```

2026-10-21 1,124 → 2026-11-23 1,293（+169）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 mid · 依据 README sha `2b31715f9e7d` · [字段定义](../../DATASET.md)*
