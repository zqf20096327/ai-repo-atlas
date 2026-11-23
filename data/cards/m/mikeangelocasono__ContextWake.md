# mikeangelocasono/ContextWake

⭐ 10 · Rust · Apache-2.0 · 推送 2026-11-06 · [GitHub](https://github.com/mikeangelocasono/ContextWake) · 个人维护

**AI 编码 agent 间的项目上下文续接工具：跨工具保留工作状态**

终端工具（Rust 编写，提供 ctx TUI 与 CLI），在工作区、Git 状态、任务、决策、检查点等本地层面组织项目状态；当用户在 Codex、Claude Code、Copilot 等 AI 编码 agent 间切换时，生成可移植 handoff 使下一个 agent 获得此前的项目状态，同一 agent 则可调用其原生 resume。本身不运行模型，各 agent 需另行安装并自持认证。安装包覆盖 Windows x86_64、Linux x86_64 与 macOS Apple Silicon，可从源码构建。README 标注当前为 public alpha，部分 provider 特定能力仍在验证。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 跨 agent 切换时生成包含工作区/分支/任务/决策/检查点的 portable handoff
- 同 agent 兼容会话时使用其原生 resume 并可验证 handoff 送达标记
- 面向 Codex、Claude Code、Copilot、Cursor 等 9 个终端 agent 提供适配
- ctx doctor 检查已装 agent 与能力，ctx agent info 查看支持范围

## 适用场景

- 一个编码 agent 不可用时切换到另一个而不重新解释整个仓库
- 在同一项目的多个 agent 之间往返并继续未完成的任务
- 本地记录任务的客观目标、决策、约束与待办以备交接

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L5: ContextWake is a terminal tool that helps you move between AI coding agents
> L52: ContextWake manages coding agents; it is not a model runtime. The agents remain
> L22: ship for Codex, Claude Code, GitHub Copilot, Cursor, OpenCode, Gemini, Kiro,

## 星数曲线

```mermaid
xychart-beta
    title "mikeangelocasono/ContextWake 星数(近 2 点)"
    x-axis ["2026-10-21", "2026-11-23"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-10-21 10 → 2026-11-23 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-19 · 置信度 high · 依据 README sha `64db1015eeba` · [字段定义](../../DATASET.md)*
