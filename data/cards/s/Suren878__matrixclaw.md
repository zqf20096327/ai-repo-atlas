# Suren878/matrixclaw

⭐ 22 · Go · MIT · 推送 2026-10-28 · [GitHub](https://github.com/Suren878/matrixclaw) · [官网](https://matrixclaw.foresko.com) · 个人维护

**给开发者的常驻本地 AI 助手与编码 agent 运行时（Go）**

用 Go 编写的本地守护进程 matrixclawd 统一管理 AI 会话：上下文、工具历史、审批、模型选择、记忆、用量与定时任务均存于本地 SQLite。终端 TUI、Telegram 机器人和本地 HTTP API 客户端共享同一会话，可跨客户端接续任务。支持 OpenAI/Anthropic/Gemini/Qwen/DeepSeek/OpenRouter 等多种 LLM 供应商及自定义端点；编码 agent 具备 git 检查点、计划模式、shell 沙箱、子 agent 与 MCP 工具。Linux/macOS 提供安装脚本与预编译二进制，源码构建需 Go 1.26+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 守护进程 + 多客户端（终端 TUI、Telegram、HTTP API）共享 SQLite 持久会话
- 工具调用审批机制（allow/ask/deny 规则）与 git 检查点回滚（/undo、/rewind）
- 子 agent 与外部 agent（Codex、Claude Code）挂载到同一会话模型
- 本地语音：Piper/Supertonic TTS、Whisper.cpp STT，可选 Asterisk/SIP 电话网关

## 适用场景

- 在终端启动编码任务，用手机 Telegram 审批工具调用并接续会话
- 让 agent 按项目指令（AGENTS.md/CLAUDE.md）自主完成多步编码并自动验证
- 设置定时 AI 任务与提醒，由常驻守护进程执行并推送到客户端

## 场景标签

`编码 Agent` `AI 助手` · 领域:编码与开发

## 证据(README 行号)

> L8: **MatrixClaw is an always-on, local-first AI assistant and coding-agent runtime
> L35: - **Autonomous coding agent.** A coding run gets an operating manual and your

## 星数曲线

```mermaid
xychart-beta
    title "Suren878/matrixclaw 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-30 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `5bea9288b942` · [字段定义](../../DATASET.md)*
