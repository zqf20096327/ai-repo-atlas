# brendanlong/claude-code-plays-text-games

⭐ 16 · JavaScript · MIT · 推送 2026-07-21 · [GitHub](https://github.com/brendanlong/claude-code-plays-text-games) · 个人维护

**让 Claude 通过 tmux 游玩终端文字游戏的 MCP 服务器**

一个 MCP (Model Context Protocol) 服务器，使 Claude 能够通过 tmux 与基于终端的游戏交互，游玩 Adventure、NetHack、Zork、Dwarf Fortress 等文字游戏。提供 start_game、send_line、send_keys、read_output、end_game 五个 MCP 工具，支持任意可在 PATH 中运行的终端游戏与复杂按键组合。README 明确提示 start_game 可执行任意命令的安全风险。运行需 Node.js、tmux、游戏可执行文件及支持 MCP 的 Claude Code。

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

- 提供 5 个 MCP 工具（start_game/send_line/send_keys/read_output/end_game）
- 通过 tmux 管理游戏会话，支持任意 PATH 中的终端游戏
- 支持方向键、功能键、Ctrl/Shift/Alt 修饰键等特殊按键
- 附特定游戏的说明与指南（如 Dwarf Fortress）

## 适用场景

- 让 Claude 游玩 NetHack、Zork 等经典文字游戏
- 观察 LLM 在终端交互游戏中的表现
- 通过 MCP 为 Claude 扩展终端程序控制能力

## 场景标签

 · 领域:AI 工具/游戏

## 证据(README 行号)

> L3: This project provides an MCP (Model Context Protocol) server that allows Claude to interact with terminal-based game
> L20: - **MCP Server**: Provides a clean API for Claude to interact with games

## 星数曲线

```mermaid
xychart-beta
    title "brendanlong/claude-code-plays-text-games 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `fed5105f8a92` · [字段定义](../../DATASET.md)*
