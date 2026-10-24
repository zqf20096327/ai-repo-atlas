# chadingTV/claudecode-discord

⭐ 63 · TypeScript · MIT · 推送 2026-05-01 · [GitHub](https://github.com/chadingTV/claudecode-discord) · 个人维护

**通过 Discord 远程控制 Claude Code 的多机 agent 中枢**

以 Node.js/TypeScript 编写的 Discord 机器人，通过 @anthropic-ai/claude-agent-sdk 将 Claude Code 以子进程方式运行，复用用户现有 Claude Pro/Max 订阅登录，无需 API key。每个 Discord 频道映射一个项目目录、维护独立会话；支持手机端发起新会话、按钮式工具调用审批、文件附件、消息队列、用量面板（5 小时/周/周 Sonnet）。通过出站 WebSocket 连接 Discord，不开放任何入站端口；提供用户白名单、速率限制与路径安全防护。多台机器可各跑一个 bot 汇聚到同一服务器，形成多机管理面板；macOS/Linux/Windows 均提供后台守护与系统托盘/菜单栏 GUI。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 复用 Claude Pro/Max 订阅运行 Claude Code 子进程，无需 API key
- 频道即工作区：每频道映射一个项目目录、独立会话与审批流
- 零入站端口：仅出站 WebSocket 连接 Discord，自托管于本机
- 多机 hub：一服务器多 bot 管理 Mac/PC/云服务器上的会话
- 三平台托盘/菜单栏控制面板与用量仪表盘

## 适用场景

- 在手机上随时启动或接管家中/公司电脑上的 Claude Code 会话
- 用 Discord 频道侧栏同时监控多台机器的编码任务状态
- 团队成员在服务器内围观、审批工具调用或排队派发任务

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L7: Control Claude Code from your phone — a multi-machine agent hub via Discord.
> L56: - 💰 **No API key** — runs on Claude Code CLI with your Pro or Max subscription
> L74: |AI|@anthropic-ai/claude-agent-sdk|
> L147: - Claude Agent SDK runs Claude Code as subprocess (shares existing auth)

## 星数曲线

```mermaid
xychart-beta
    title "chadingTV/claudecode-discord 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 62 --> 64
    line [63, 63]
```

2026-10-18 63 → 2026-10-24 63（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `cf8b784a5d99` · [字段定义](../../DATASET.md)*
