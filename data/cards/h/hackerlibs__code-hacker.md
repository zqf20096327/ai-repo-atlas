# hackerlibs/code-hacker

⭐ 55 · Python · MIT · 推送 2026-07-21 · [GitHub](https://github.com/hackerlibs/code-hacker) · 个人维护

**AI 编程 Agent 工具链：6 个 MCP 服务器 + 三种前端**

将 Claude Code 式自主编程能力拆分为 6 个 MCP 服务器（文件操作、Git、代码分析、记忆、代码评审、多项目工作区），共 62+ 工具。三种前端共享同一后端：VS Code Copilot Chat 自定义 Agent、基于 deepagents 的 Web 应用（含 4 个专用子代理）、终端 TUI（TUI 需 OPENROUTER_API_KEY）。特色机制包括 AST 级结构化 diff（ydiff）、代码质量评分、跨仓库工作区、AI 改动两阶段提交（机械变更与逻辑变更分离）；各服务器有独立安全沙箱（路径检查、命令黑名单、文件白名单）。不支��图像/PDF/Notebook。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 6 个 MCP 服务器提供 62+ 工具，三前端共享同一后端
- AST 级结构化 diff 与代码质量评审工具
- 多项目工作区：跨仓库搜索、编辑与协同提交
- AI 改动两阶段提交，机械变更标记 #not-need-review

## 适用场景

- 在 VS Code 内以自定义 Agent 方式做 AI 编程
- 通过 Web 应用进行多项目自主 AI 编程与协调
- 在 SSH/无界面服务器上用终端 TUI 进行 AI 编程

## 场景标签

`编码 Agent` `代码审查` · 领域:编码与开发

## 证据(README 行号)

> L3: **6 MCP Servers** powering **62+ tools** for a complete AI programming toolchain. Three ways to use:
> L72: The web app (and TUI) is a **complete AI programming tool** built on deepagents (`create_deep_agent`):
> L111: Code Hacker's design goal: **Replicate and surpass this closed-loop capability** — usable both within VS Code Copi

## 星数曲线

```mermaid
xychart-beta
    title "hackerlibs/code-hacker 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 54 --> 56
    line [55, 55]
```

2026-10-18 55 → 2026-10-28 55（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `b3543c05ecf7` · [字段定义](../../DATASET.md)*
