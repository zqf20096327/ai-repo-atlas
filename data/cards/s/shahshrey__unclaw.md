# shahshrey/unclaw

⭐ 17 · Shell · MIT · 推送 2026-04-13 · [GitHub](https://github.com/shahshrey/unclaw) · [官网](https://github.com/shahshrey/unclaw) · 个人维护

**把 Claude Code 变成个人 AI agent 的配置模板**

面向 Claude Pro/Max/Team 订阅用户的个人 agent 配置模板：本体是 markdown 文件、shell 脚本和一个 Python 索引器，无自建运行时，运行在 Claude Code 内部，使用现有订阅而不产生 API 费用。通过 /setup 技能完成初始化，建立身份（SOUL.md）、hot/cold/raw 三层记忆（SQLite FTS5 检索）、会话钩子、可选 Telegram 接入与 macOS launchd 定时任务（心跳、记忆提升、夜间自我改进）。多 agent 通过重复克隆仓库实现目录级隔离，每个 agent 有独立的工具、技能、规则与记忆。

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

- 运行在 Claude Code 内，使用现有 Claude 订阅，README 称零额外 API 成本
- hot/cold/raw 三层记忆架构，SQLite FTS5 全文检索，/promote 提升信号
- 零运行时代码：markdown + shell 脚本 + Python 索引器，无 npm 依赖、无 Docker、无构建步骤
- 多 agent 目录级隔离：独立工具、技能、安全规则、记忆与 Telegram bot

## 适用场景

- 用现有 Claude 订阅搭建一个有持久记忆的个人 AI agent
- 通过 Telegram 从手机与自己的 agent 对话
- 为不同角色（写作、金融分析、开发）克隆出多个相互隔离的 agent

## 场景标签

`Agent 框架` `Agent 记忆` `AI 助手` · 领域:Agent 开发

## 证据(README 行号)

> L22: And because Claude Code already is a full agent runtime — tools, file access, shell, subagents, MCP servers — UnCla
> L86: **Zero lines of runtime code.** UnClaw is markdown files, shell scripts, and a Python indexer. There is no applicat

## 星数曲线

```mermaid
xychart-beta
    title "shahshrey/unclaw 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-29"]
    y-axis "stars" 15 --> 18
    line [16, 17, 17]
```

2026-10-18 16 → 2026-10-29 17（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 mid · 依据 README sha `e54219d1a2ec` · [字段定义](../../DATASET.md)*
