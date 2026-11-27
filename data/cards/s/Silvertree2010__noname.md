# Silvertree2010/noname

⭐ 4 · Rust · AGPL-3.0 · 推送 2026-11-26 · [GitHub](https://github.com/Silvertree2010/noname) · 个人维护

**为 Claude Code 提供 Rust 编写的终端 TUI 界面**

用 Rust 与 ratatui 编写的 Claude Code 终端界面，替换其界面而不替换引擎：claude 在底层继续运行，订阅、插件、技能、MCP 服务器与 hooks 保持可用。提供流式文本/思考/工具调用展示、内联权限询问、esc esc 回退、上下文与用量条、主题与动画背景、图片粘贴、后台任务与会话恢复。支持 Linux/macOS/Windows，可选用 Codex、opencode、Antigravity 作为引擎。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 替换 Claude Code 界面而非引擎，订阅/插件/技能/MCP/hooks 保持工作
- 流式输出、内联权限询问、esc esc 回退、/btw 侧问题
- 多主题（dracula、tokyo-night、catppuccin mocha 等）与动画背景
- 可选 --codex/--opencode/--agy 切换引擎

## 适用场景

- 在终端中获得更完整的 Claude Code 界面与用量信息
- 用同一 TUI 通过 Codex/opencode/Antigravity 引擎会话
- 恢复和继续此前的编码会话

## 场景标签

 · 领域:开发者工具/AI 编程

## 证据(README 行号)

> L19: noname is a terminal UI (TUI) for Claude Code, built in Rust with ratatui. It replaces the interface of Claude Code
> L26: - Linux, macOS and Windows; optional Codex engine with `--codex`, opencode engine with `--opencode` and Antigravity

## 星数曲线

```mermaid
xychart-beta
    title "Silvertree2010/noname 星数(近 3 点)"
    x-axis ["2026-11-13", "2026-11-21", "2026-11-27"]
    y-axis "stars" 2 --> 5
    line [3, 4, 4]
```

2026-11-13 3 → 2026-11-27 4（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `581006ec4810` · [字段定义](../../DATASET.md)*
