# luckeyfaraday/Athena

⭐ 33 · TypeScript · 推送 2026-10-28 · [GitHub](https://github.com/luckeyfaraday/Athena) · 个人维护

**AI 编程 agent 的本地桌面工作台：并排运行多家 agent 终端**

基于 Electron + React 与 FastAPI 后端的本地桌面应用，用于并排运行 AI 编程 agent。通过 node-pty 与 xterm.js 嵌入终端窗格，可启动 Codex、OpenCode、Claude Code、Athena Code、Grok、Hermes 及 shell 会话，发现并恢复磁盘上的原生 agent 会话，读取终端/聊天视图中的用户与助手消息。提供 MCP 服务器让 Hermes 驱动工作区，并读取 Claude/Codex 订阅配额。支持四窗格网格、工作区标签、跨机器 Tailscale 远程访问与主题系统。从源码运行需 Node.js 与 Python 3.11+，打包版自带后端运行时；agent CLI 为可选依赖。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 在嵌入 PTY 终端中并行运行 Codex/OpenCode/Claude Code/Athena Code/Grok/Hermes/shell 会话
- 发现磁盘上的原生 agent 会话并支持恢复、重命名、聚焦等操作
- MCP 服务器暴露 Athena 工具，让 Hermes 驱动桌面工作区并管理长期记忆
- 读取 Claude/Codex 签名账户的订阅配额窗口与重置倒计时

## 适用场景

- 在一个桌面应用中并排管理多个 AI 编程 agent 与终端
- 恢复之前在原生 CLI 中留下的 agent 会话继续工作
- 让 Hermes 通过 MCP 检查会话、向窗格发消息并派生可见终端
- 通过 Tailscale 在命令室中查看另一台电脑的终端

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L26: Athena is a local desktop workspace for running AI coding agents side by side. It gives developers one Electron app
> L60: |App type|Local desktop app for AI coding agent orchestration|
> L122: - Expose Athena health, Hermes memory, native sessions, transcripts, and terminal spawning through MCP.

## 星数曲线

```mermaid
xychart-beta
    title "luckeyfaraday/Athena 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 32 --> 34
    line [33, 33]
```

2026-10-18 33 → 2026-10-31 33（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `d2fee043af70` · [字段定义](../../DATASET.md)*
