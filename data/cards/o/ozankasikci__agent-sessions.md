# ozankasikci/agent-sessions

⭐ 81 · Rust · 推送 2026-04-08 · [GitHub](https://github.com/ozankasikci/agent-sessions) · [官网](https://ozankasikci.github.io/agent-sessions/) · 个人维护

**macOS 桌面应用：实时监控多个 AI 编码 agent 会话**

用 Rust（Tauri 2.x）与 React 编写的 macOS 桌面应用，用于集中查看和管理多个 AI 编码 agent 会话：支持 Claude Code 与 OpenCode 两种 agent，实时检测会话状态（Thinking/Processing/Waiting/Idle），提供全局快捷键切换可见性、点击聚焦会话终端、会话重命名与快捷 URL 等功能。仅支持 macOS，且终端限定 iTerm2 与 Terminal。通过 Homebrew cask 或 Releases 页面的 DMG 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 集中查看所有活跃编码 agent 会话并实时检测状态
- 支持 Claude Code 与 OpenCode 两种 agent
- 全局快捷键、会话重命名、点击聚焦终端
- Tauri 2.x + React + TypeScript 技术栈

## 适用场景

- 同时运行多个 AI 编码 agent 时在一处查看各自状态
- 用快捷键快速切换到某个 agent 的终端
- 为会话标注自定义名称并记录 dev server 链接

## 场景标签

`LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L8: A macOS desktop app to monitor your AI coding agents in real-time.
> L14: - **Claude Code** - Anthropic's official CLI for Claude

## 星数曲线

```mermaid
xychart-beta
    title "ozankasikci/agent-sessions 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 80 --> 82
    line [81, 81]
```

2026-10-18 81 → 2026-10-30 81（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `717877a7d8fd` · [字段定义](../../DATASET.md)*
