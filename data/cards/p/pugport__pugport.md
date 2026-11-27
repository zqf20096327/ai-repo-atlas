# pugport/pugport

⭐ 3 · TypeScript · Apache-2.0 · 推送 2026-11-26 · [GitHub](https://github.com/pugport/pugport) · [官网](https://pugport.com) · 个人维护 · 中文 README

**把多个 AI 订阅账号聚合在一个聊天里，自动按用量路由任务**

PugPort 是一款桌面应用（Electron），面向付费了多个 AI 订阅的用户：用户在单一聊天中描述任务，应用读取各账号的剩余用量与限额重置时间，选择账号、模型与推理力度来执行；任务中途遇到用量上限时自动移交到有余量的账号并附带交接说明。它启动用户已安装并登录的官方命令行工具（Claude Code、Codex CLI、Grok CLI、Cursor CLI），不代理或存储密码，数据保存在本地 SQLite。路由建议由一个 322M 参数的 Task Router 分类器提供，可切换为人工确认或手动指定。处于早期开发阶段（v0.0.39），支持 Windows x64 与 Apple Silicon Mac。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 按各账号真实用量与限额重置时间路由任务，限额时自动带交接说明移交
- 内置 322M 参数 Task Router 分类器提供路由建议，可覆盖为人工确认
- 代理间子任务协作：运行中的 agent 可将子任务交给其他账号（默认只读）
- 每次运行的输出、工具调用、审批与 token 用量本地留档，可恢复中断任务

## 适用场景

- 同时持有多个 Claude/Codex/Cursor 订阅时统一在一个聊天里调度
- 账号到达用量上限时自动把进行中的任务移交到有余量的账号
- 让不同 agent 互相协作，如让 Codex 审查另一个 agent 的产出

## 场景标签

`多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L3:  Your AI subscriptions and accounts in one chat. PugPort sends each task to an account with usage to spare, picks th
> L26: PugPort starts the official command-line tools you've already installed and signed in to; it never proxies or imita
> L43: ## Supported executors


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 high · 依据 README sha `aa26aecdf6d1` · [字段定义](../../DATASET.md)*
