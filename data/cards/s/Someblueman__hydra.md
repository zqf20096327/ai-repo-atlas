# Someblueman/hydra

⭐ 28 · C · MIT · 推送 2026-10-17 · [GitHub](https://github.com/Someblueman/hydra) · 个人维护

**管理并行 AI 编码代理会话的 CLI/TUI 任务控制台**

基于 POSIX shell 与 C 的本地工具，包装 tmux ≥3.0 与 git worktree，为每个任务创建独立分支、工作目录与终端会话（head），在原生 C TUI 或 CLI 中监控代理活动、检查 diff、执行验证并守卫式集成变更。支持 SSH 主机舰队协调远程 head 与工作流。用户可选用已安装的编码代理（Codex、Claude Code、Cursor Agent 等）在 head 中运行；工具本身不产出模型结果，只协调进程并记录证据。需 Git、Make、C99 编译器从源码构建，无守护进程、数据库或云账户。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- head = 独立分支 + git worktree + tmux 会话的并行隔离机制
- 原生 C TUI 任务控制中心，含舰队视图与 SSH 远程 attach
- 支持 Antigravity、Cursor Agent、OpenCode、Claude Code、Codex、Pi 等代理配置
- 工作流计划：代理提案编译为不可变 DAG 并以验收摘要执行

## 适用场景

- 在同一仓库并行运行多个 AI 编码任务互不干扰
- 跨多台 SSH 主机远程启动并监控编码代理
- 审查代理产出 diff、运行测试并守卫式合并

## 场景标签

 · 领域:开发者工具/AI 代理编排

## 证据(README 行号)

> L9: Hydra coordinates coding agents across local projects and remote SSH hosts. Give
> L42: - **Run coding agents across your fleet.** Select agent profiles and task prompts,
> L78: Headless agents: **Antigravity (`agy`), Cursor Agent, OpenCode, Claude Code,

## 星数曲线

```mermaid
xychart-beta
    title "Someblueman/hydra 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 27 --> 29
    line [28, 28]
```

2026-10-18 28 → 2026-10-30 28（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `c6dfcb910b8e` · [字段定义](../../DATASET.md)*
