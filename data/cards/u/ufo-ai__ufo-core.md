# ufo-ai/ufo-core

⭐ 99 · Python · Apache-2.0 · 推送 2026-10-21 · [GitHub](https://github.com/ufo-ai/ufo-core) · [官网](https://ufo.ai) · 组织维护

**面向团队自托管的 AI agent 运行时与终端客户端**

开源 AI agent 运行时：团队成员在聊天中给 agent 派活，agent 可读写文件、执行命令完成任务。单进程 `ufoctl serve` 承载 agent 循环、回合队列、沙箱与后台任务；回合为 DBOS 工作流，崩溃后可恢复。仓库含服务器、终端客户端、SDK 与扩展体系（工具/连接器/子 agent/模型提供方均为扩展）。可单机用 SQLite 与本地文件运行，也可扩展为 Postgres/S3/Redis 多实例；默认本地沙箱基于 Seatbelt/Landlock，不信任场景建议 Docker 或 E2B。另提供由同一运行时支撑的托管服务。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单进程承载 agent 循环、回合队列、沙箱与后台任务，SQLite 起步可扩展到 Postgres/S3/Redis
- 每个回合是 DBOS 工作流，崩溃后存活
- 工具/连接器/子 agent/模型提供方/沙箱载体均为扩展，`ufoctl ext` 管理
- 本地沙箱用 Seatbelt/Landlock 限制写入，可选 docker/e2b 载体

## 适用场景

- 团队在自己的基础设施上运行 AI agent 处理文件与命令类工作
- 通过终端客户端或 Slack 与 agent 协作
- 以扩展机制接入自有工具、连接器与模型提供方

## 场景标签

`Agent 框架` `AI 助手` · 领域:Agent 开发

## 证据(README 行号)

> L22: UFO is an open source runtime for AI agents. Team members give agents work in chat. Agents can read
> L26: model keys. The `ufo` terminal client connects to either. This repository contains the server,
> L110: |`ufo.harness`|Product-neutral agent execution: messages, model requests, tool calls, budgets, compaction, the san

## 星数曲线

```mermaid
xychart-beta
    title "ufo-ai/ufo-core 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-27"]
    y-axis "stars" 98 --> 101
    line [99, 100, 99]
```

2026-10-18 99 → 2026-10-27 99（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 mid · 依据 README sha `24c232ce8319` · [字段定义](../../DATASET.md)*
