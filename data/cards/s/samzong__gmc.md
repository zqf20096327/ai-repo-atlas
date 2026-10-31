# samzong/gmc

⭐ 28 · Go · MIT · 推送 2026-10-30 · [GitHub](https://github.com/samzong/gmc) · [官网](https://gmc.samzong.me) · 个人维护

**面向 AI 编码时代的 Git worktree 工作流 CLI，支持并行 agent 与 AI 提交信息**

Go 编写的 Git 工作流命令行工具：以 `.bare/` + worktree 布局管理仓库，为多个并行 AI agent 各自分配 worktree，可跨 worktree 共享 `.env`/`node_modules`/venv，支持从 GitHub PR 拉起 worktree；提交阶段由 LLM 根据暂存 diff 生成 Conventional Commits 提交信息，可自定义 prompt 模板与模型/角色配置。还包含 `gmc task` 本地任务账本（tmux 中启动 agent、记录运行与日志）、Rust 依赖缓存（Kache）与 shell 补全。通过 Homebrew 或 go install 安装，MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 每 agent 一个 worktree，`wt dup` 可批量创建并行分支
- LLM 从暂存 diff 生成 Conventional Commits 提交信息，支持自定义 prompt 模板
- 跨 worktree 共享 `.env`/`node_modules`/venv 与 Rust 依赖缓存（Kache）
- `gmc task` 以 plan→code→review→ship 工作流在 tmux 中管理 agent 任务并记录日志

## 适用场景

- 同时运行多个 AI coding agent 互不干扰地改同一仓库
- 让 LLM 自动写规范的提交信息与分支名
- 审查 GitHub PR 时在独立 worktree 中拉取代码

## 场景标签

 · 领域:开发者工具/Git 工作流

## 证据(README 行号)

> L5:  Parallel worktrees for parallel AI agents — plus AI-generated commits. A Git workflow CLI built for the AI coding e
> L39: |`gmc`|Generate Conventional Commits message from staged diff|

## 星数曲线

```mermaid
xychart-beta
    title "samzong/gmc 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 27 --> 29
    line [28, 28]
```

2026-10-18 28 → 2026-10-31 28（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `12686ce298e6` · [字段定义](../../DATASET.md)*
