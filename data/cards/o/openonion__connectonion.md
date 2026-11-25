# openonion/connectonion

⭐ 1,567 · Python · Apache-2.0 · 推送 2026-11-23 · [GitHub](https://github.com/openonion/connectonion) · [官网](https://docs.connectonion.com) · 组织维护

**给 AI agent 提供统一 CLI 的 harness：一条命令行接入邮件、浏览器与工具**

一个以 `co` 命令行为核心的 agent harness：将 Gmail、Outlook、Chrome、聊天应用、文件、issue 跟踪器等工具统一为带 `--help` 的命令，agent 按需发现并调用，无需 MCP 服务器或插件；co rem 子命令将邮件与编码会话上下文整理为本地链接 Markdown 页面供 agent 复用，支持把会话交接给他人 agent；亦提供 Python 框架用于构建自有 agent。凭 pip 或 install.sh 安装，co rem 的每日调度目前仅限 macOS。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 一条 `co` 命令行统一 Gmail、Outlook、浏览器、文件与聊天应用等工具，agent 经 `--help` 按需发现
- co rem 将邮件与编码会话上下文整理为本地 Markdown 页面，支持跨任务复用
- `co audit` 按 agent 阅读方式为 CLI 帮助页评分，并接入 CI
- 提供 Python 框架供在同一 harness 上构建自有 agent

## 适用场景

- 让编码 agent（Codex/Claude Code）直接操作我的邮箱、日历和 Slack
- 把散落在邮件与编码会话里的上下文串成本地笔记供 agent 复用
- 夜间让 agent 起草待回复邮件并执行已批准的任务

## 场景标签

`编码 Agent` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L5: **The agent CLI harness. CLI is all you need.**
> L20:  CLI as your harness. No MCP servers, adapters or glue: a CLI
> L279: ConnectOnion is also a Python framework for building your own agents on the

## 星数曲线

```mermaid
xychart-beta
    title "openonion/connectonion 星数(近 16 点)"
    x-axis ["2026-10-23", "2026-10-29", "2026-10-30", "2026-11-01", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-16", "2026-11-19", "2026-11-22", "2026-11-23", "2026-11-25"]
    y-axis "stars" 1495 --> 1573
    line [1501, 1502, 1503, 1504, 1501, 1507, 1553, 1560, 1561, 1563, 1564, 1565, 1564, 1565, 1567, 1567]
```

2026-10-23 1,501 → 2026-11-25 1,567（+66）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-24 · 置信度 high · 依据 README sha `58af9fb1dced` · [字段定义](../../DATASET.md)*
