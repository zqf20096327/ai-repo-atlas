# Perpeer/lazychat

⭐ 30 · Go · NOASSERTION · 推送 2026-10-20 · [GitHub](https://github.com/Perpeer/lazychat) · [官网](https://perpeer.github.io/lazychat/) · 个人维护

**在终端并排运行 Claude Code 与 Codex 等编码 Agent 的 TUI**

Go 编写的 macOS 终端界面（TUI），用于统一管理 AI 编码 Agent 会话：在 workspace/project 层级下，每个项目可开启多个 Claude Code 或 Codex 会话，各自运行并提示哪一需要用户输入；集成 Git（stage/diff/commit）与终端（含 SSH）。仅支持 macOS 12+（Apple silicon 或 Intel），通过 Homebrew tap 或源码脚本安装，附带菜单栏应用与 doctor 自检命令。灵感来自 lazygit/lazydocker。采用 PolyForm Shield 1.0.0 许可（source-available）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 同一项目下并排运行多个 Claude Code / Codex 会话，提示哪一需要输入或已完成
- 内置 Git 与终端（含 SSH）标签页，workspace 多项目切换
- Homebrew tap 安装并附带菜单栏应用，lazychat doctor 自检 Agent 就绪状态

## 适用场景

- 同时开多个 AI 编码会话，分别处理特性与修复
- 在一个终端里切换项目、Git 操作与 shell
- 查看哪个 Agent 在等待我的回复

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L5:  One terminal for all your AI coding agents.
> L80: **3. Sessions.** Press `n` to start Claude Code or Codex in the project,

## 星数曲线

```mermaid
xychart-beta
    title "Perpeer/lazychat 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-30"]
    y-axis "stars" 28 --> 31
    line [29, 30, 30]
```

2026-10-18 29 → 2026-10-30 30（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `72490ed20c92` · [字段定义](../../DATASET.md)*
