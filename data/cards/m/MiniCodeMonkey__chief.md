# MiniCodeMonkey/chief

⭐ 472 · Go · MIT · 推送 2026-09-28 · [GitHub](https://github.com/MiniCodeMonkey/chief) · [官网](https://chiefloop.com) · 个人维护

**把项目拆成任务并循环运行 Claude Code 的 Go TUI 工具**

面向开发者的命令行/TUI 项目自动化工具：将项目描述为一系列任务，循环调用 Claude Code（默认）逐任务执行，每任务一个 commit，形成可审查的 git 历史。采用 Ralph Wiggum 循环——每次迭代重置上下文窗口、任务间持久化进度，以规避上下文长度限制。除 Claude 外可配置 Codex、OpenCode、Cursor、Gemini 等 provider，通过 .chief/config.yaml 或环境变量切换。经 brew 或安装脚本安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Ralph Wiggum 循环：每轮重置上下文、跨轮持久化进度
- 一任务一 commit，产出可审查的 git 历史
- 支持 claude/codex/opencode/cursor/gemini 五种 provider 切换

## 适用场景

- 让 Claude Code 自动完成拆解好的大型项目任务
- 在上下文长度限制下持续推进长周期编码工作
- 在不同 agent CLI 之间切换执行同一任务清单

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L5: Build big projects with Claude. Chief breaks your work into tasks and runs Claude Code in a loop until they're done.
> L45: - **Claude Code CLI**, **Codex CLI**, **OpenCode CLI**, or **Gemini CLI** installed and authenticated
> L57: Supported values for `provider` are: `claude`, `codex`, `opencode`, `cursor`, and `gemini`.

## 星数曲线

```mermaid
xychart-beta
    title "MiniCodeMonkey/chief 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-28"]
    y-axis "stars" 470 --> 474
    line [473, 472, 471]
```

2026-10-18 473 → 2026-10-28 471（-2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `b270270a9ebc` · [字段定义](../../DATASET.md)*
