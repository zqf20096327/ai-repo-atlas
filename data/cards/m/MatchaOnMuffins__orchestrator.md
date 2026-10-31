# MatchaOnMuffins/orchestrator

⭐ 30 · TypeScript · MIT · 推送 2026-06-30 · [GitHub](https://github.com/MatchaOnMuffins/orchestrator) · 个人维护

**并行运行多个 Claude Code agent 的桌面应用**

基于 Electron/React 的桌面应用，让多个 Claude Code agent 同时在同一仓库工作：每个 agent 通过 git worktree 获得隔离副本与独立分支，最多 10 个并行；界面按 tmux 式分屏实时展示各 agent 的工具调用、文件编辑与 token 计数，可发送后续消息，会话持久化到磁盘、重开后恢复完整对话历史。运行需 Node 18+ 与已认证的 Claude Code CLI，通过 git clone 源码加 npm 构建。

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

- 每个 agent 独立 git worktree 与分支，最多 10 个并行
- tmux 式分屏实时查看各 agent 的工具调用与 token 计数
- 会话保存到磁盘，重开应用可恢复完整对话历史

## 适用场景

- 让多个 agent 同时改同一代码库的不同部分而互不冲突
- 并排监控多个 agent 的实时工作状态
- 中断后回来继续之前的 agent 会话

## 场景标签

`编码 Agent` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L3: A desktop app for running multiple Claude Code agents on the same repo at the same time.
> L15: Orchestrator solves this by giving each agent its own git worktree and branch. You can see what all of them are doi

## 星数曲线

```mermaid
xychart-beta
    title "MatchaOnMuffins/orchestrator 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 29 --> 31
    line [30, 30]
```

2026-10-18 30 → 2026-10-31 30（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `7315cf3009e0` · [字段定义](../../DATASET.md)*
