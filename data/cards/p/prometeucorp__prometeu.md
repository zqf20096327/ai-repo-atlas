# prometeucorp/prometeu

⭐ 63 · Rust · MIT · 推送 2026-10-27 · [GitHub](https://github.com/prometeucorp/prometeu) · [官网](https://prometeu.co) · 组织维护

**并行运行多个编码 agent 的桌面应用，配 git worktree 隔离与 diff 审查**

MIT 许可的开源桌面应用，用于在同一界面并行运行 Claude Code、Codex、Cursor CLI 和 Antigravity 四种编码 agent：每个任务自动创建独立 git worktree 隔离改动，内置可视化 diff 审查、提交与冲突处理，并附带编辑器、终端、MCP 服务器、Linear/GitHub 任务过滤等工具。自带 provider 账号，用量由 provider 计费。macOS(Apple Silicon)/Linux(x86_64) 提供安装包，Windows 为实验性且仅支持 WSL 内的 Codex；使用分析默认关闭。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 并行运行 4 种编码 agent，每个任务独立 git worktree 隔离
- 可视化 diff 审查、暂存、提交与冲突解决
- 内置编辑器、终端、浏览器预览、MCP 服务器、插件与技能
- 可恢复中断的对话并查看本地 token 与成本历史

## 适用场景

- 同时让多个 AI 编码 agent 处理不同任务且互不干扰
- 在提交合并前可视化审查 agent 的代码改动
- 从 Linear/GitHub 筛选 issue 或 PR 直接发起 agent 工作区

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L2: Run Claude Code, Codex, Cursor CLI and Antigravity agents in parallel — each in its own git worktree, with built-in 
> L20: - Create isolated worktrees automatically for separate tasks, so agents do not edit the same checkout.

## 星数曲线

```mermaid
xychart-beta
    title "prometeucorp/prometeu 星数(近 2 点)"
    x-axis ["2026-10-26", "2026-10-28"]
    y-axis "stars" 62 --> 64
    line [63, 63]
```

2026-10-26 63 → 2026-10-28 63（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `b1127c43037d` · [字段定义](../../DATASET.md)*
