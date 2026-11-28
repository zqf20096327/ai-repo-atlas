# qwwiwi/codex-cli-telegram-plugin

⭐ 6 · TypeScript · Apache-2.0 · 推送 2026-11-27 · [GitHub](https://github.com/qwwiwi/codex-cli-telegram-plugin) · 个人维护

**把 OpenAI Codex CLI 接入私人 Telegram 聊天的桥接服务**

Bun/TypeScript 编写的 Telegram bot 与 Codex CLI 之间的桥：以子进程启动 `codex app-server`（JSON-RPC 接口），把用户消息转发给 Codex 会话并将回答回传聊天。面向个人用户在自己服务器上自建私有 agent，单主人单私聊。支持文本、语音（经 Groq 转录）、照片、文档输入，长任务 `/goal`、并行侧会话、审批卡片（never/standard/risky 三种模式）、固定 HUD、消息与线程落盘重启恢复。安装脚本面向 Linux systemd，macOS 需手动配置；要求 ChatGPT 账号登录 Codex。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 以子进程运行 codex app-server，转发消息并回传结果
- 审批卡片三种模式（never/standard/risky），支持专用系统用户的全自主运行
- 语音消息经 Groq whisper-large-v3-turbo 转录（默认语言 ru，≤25MB）
- 消息、Codex 线程与投递进度持久化，重启不丢失

## 适用场景

- 在手机 Telegram 上远程操控自己服务器上的 Codex agent
- 给 agent 下发带完成标准的长时间任务并查看进度
- 以审批卡片确认沙箱外的命令与文件改动

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L19: **A small Bun/TypeScript bridge between a Telegram bot and OpenAI Codex CLI.** It starts `codex app-server` (the JS
> L74: - Linux with systemd user services for `install.sh` and `update.sh`; `loginctl enable-linger` so the bot keeps runn
> L76: - A ChatGPT account with Codex access. The bridge checks at start that Codex is signed in through ChatGPT.


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `6f4d9a97f8f9` · [字段定义](../../DATASET.md)*
