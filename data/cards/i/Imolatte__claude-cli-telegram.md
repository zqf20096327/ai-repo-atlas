# Imolatte/claude-cli-telegram

⭐ 36 · JavaScript · MIT · 推送 2026-09-25 · [GitHub](https://github.com/Imolatte/claude-cli-telegram) · [官网](https://github.com/Imolatte/tg-claude#readme) · 个人维护

**把 Mac/Linux 变成 Telegram 远程 Claude Code 终端的 bot**

Node.js 编写的 Telegram bot，在用户本机或服务器上启动真实的 Claude Code CLI 进程，把消息转发给 CLI 并流式返回工具活动与结果，非 API 封装。面向已安装 Claude Code CLI 的开发者，提供会话管理、危险操作审批（tmux 注入原生提示）、语音输入（Groq Whisper STT）、git 面板、30+ 命令、Mac 远程控制，以及 Mac/服务器双机角色切换（primary/standby 经 ssh 心跳交接）。需 Node.js 20+、Telegram bot token 与 Groq API key，可选 FFmpeg、tmux、Puppeteer。

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

- 启动真实 Claude Code CLI，流式展示工具活动与内联 diff
- 双通道危险操作审批，tmux 下经 send-keys 应答原生提示
- Mac(primary/standby) 与服务器经 ssh 心跳自动交接运行位置
- 语音输入走 Groq Whisper STT，支持照片/文件/转发的多类型输入

## 适用场景

- 离开电脑时用手机继续操控 Claude Code 编码任务
- 在手机上审批 git push、rm -rf 等危险操作
- 远程管理服务器与 Mac 上的 Claude 会话和 git 仓库

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L12: Send a message from Telegram → bot spawns real Claude Code CLI → streams progress → sends response back. Not an API
> L15: You (Telegram) → Bot (Node.js) → Claude Code CLI → tools → response → You

## 星数曲线

```mermaid
xychart-beta
    title "Imolatte/claude-cli-telegram 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 35 --> 37
    line [36, 36]
```

2026-10-18 36 → 2026-10-29 36（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `3133b740f773` · [字段定义](../../DATASET.md)*
