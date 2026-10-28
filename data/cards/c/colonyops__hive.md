# colonyops/hive

⭐ 39 · Go · MIT · 推送 2026-10-28 · [GitHub](https://github.com/colonyops/hive) · [官网](https://colonyops.github.io/hive/) · 组织维护

**管理多个 AI agent 隔离 git 会话的 CLI/TUI 工具**

用 Go 编写的终端工具（另含 Hive Desktop 桌面程序），在隔离的 git clone 目录中并行运行 AI agent（如 Claude、Aider、Codex）：自动处理克隆、回收与终端会话创建，会话按 active→recycled→deleted 生命周期管理并可复用。提供 tmux 实时状态监控、多 agent 任务跟踪（epics/tasks）、会话间 pub/sub 消息、共享上下文存储与操作员 todo。需 Git 与 tmux；可经 brew、go install 或预编译二进制安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 隔离 git clone 会话的创建/回收/修剪与生命周期跟踪
- tmux 中实时监控 agent 状态（工作中/待批准/就绪等指示器）
- 多 agent 任务跟踪与会话间 pub/sub 消息
- 每仓库共享上下文存储（.hive 符号链接）

## 适用场景

- 并行运行多个 AI agent 各自处理独立任务
- 统一监控各 agent 会话状态并按需介入
- 为多个 agent 安排任务并让它们之间通信

## 场景标签

`多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L38: Hive manages isolated git sessions for running AI agents in parallel. Instead of manually managing git worktrees or
> L45: - **Terminal Integration** — Real-time status monitoring of AI agents in tmux (works out of the box)

## 星数曲线

```mermaid
xychart-beta
    title "colonyops/hive 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-28"]
    y-axis "stars" 37 --> 40
    line [38, 39, 39]
```

2026-10-18 38 → 2026-10-28 39（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `740f9ca9aad0` · [字段定义](../../DATASET.md)*
