# DoBuDevel/discord-agent-bridge

⭐ 31 · TypeScript · MIT · 推送 2026-02-09 · [GitHub](https://github.com/DoBuDevel/discord-agent-bridge) · 个人维护

**把 AI 编程 agent CLI 桥接到 Discord 远程监控的工具**

TypeScript 编写的 CLI 桥接工具：将 Claude Code、OpenCode 等 AI 编程 agent 运行在 tmux 会话中，通过轮询架构每 30 秒捕获 tmux 面板内容，检测状态变化后流式推送到 Discord 频道，实现远程监控。每个项目对应一个独立频道，单一守护进程管理全部连接。支持自动检测已安装的 agent、可选的 YOLO 模式（跳过权限确认）与 Docker 沙箱模式（均限 Claude Code）。面向使用 AI 编程助手的开发者，需 Node.js 18+ 与 tmux 3.0+，macOS 已测试，Linux/WSL 未测试，Windows 原生不支持。

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

- 轮询捕获 tmux 输出并每 30 秒流式推送 Discord
- 支持 Claude Code 与 OpenCode，自动检测已安装 agent
- 每个项目独立 Discord 频道，单守护进程管理多项目
- 可选 YOLO 模式与 Docker 沙箱隔离（限 Claude Code），129 个单元测试

## 适用场景

- 在 Discord 上远程监控长时间运行的 AI 编程任务
- 团队共享 AI agent 的工作进度
- 同时跟踪多个项目的 agent 会话

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L14: Discord Agent Bridge connects AI coding assistants (Claude Code, OpenCode) to Discord, enabling remote monitoring a
> L16: The bridge uses a polling-based architecture that captures tmux pane content every 30 seconds, detects state change
> L252: - **Agent Registry**: Factory pattern for multi-agent support (Claude, OpenCode)

## 星数曲线

```mermaid
xychart-beta
    title "DoBuDevel/discord-agent-bridge 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 30 --> 32
    line [31, 31]
```

2026-10-18 31 → 2026-10-29 31（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `cb7e3ee89c95` · [字段定义](../../DATASET.md)*
