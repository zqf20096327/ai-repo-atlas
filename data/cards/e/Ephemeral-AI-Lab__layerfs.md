# Ephemeral-AI-Lab/layerfs

⭐ 2,034 · Rust · MIT · 推送 2026-10-24 · [GitHub](https://github.com/Ephemeral-AI-Lab/layerfs) · [官网](https://layerfs.ai/) · 组织维护

**面向 AI agent 的写时复制共享文件系统，支持分支/提交/合并**

LayerFS 为每个 agent 提供挂载于共享提交历史之上的完整可写 Workspace，无需复制基础数据；agent 工作结束后将变更以去重 checkpoint 形式提交，支持分支、回退与合并。底层为单一 SQLite 文件承载 Branch、Commit 与内容对象，无数据库服务器；通过 FUSE 提供挂载视图，文件操作直入 Store 成为 Commit。当前通过 dsh-layerfs 插件与 DeepSeek Harness 配合运行，Store 的 Disposable 配置不提供崩溃/断电持久性，官方声明不应用于不可重建数据的唯一副本。1.0.0 以源码形式发布。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- Workspace 写时复制挂载，写入进入自身 overlay，提交后去重存储
- 单一 SQLite 文件承载全部 Branch/Commit/内容对象，无数据库服务器
- 支持递归 fork 分支、自动 checkpoint、合并发布与 Conflict 冲突拒绝
- 157 个快照（4.94 GB 树）存为 100.1 MB 可挂载 Commit

## 适用场景

- 多 agent 并行开发时共享同一提交历史并各自持有可写工作区
- agent 实验分支的打分、回退与最佳分支保留（配合 MCTS 式探索）
- 频繁快照的项目历史去重存储与即时恢复依赖环境

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L7:  LayerFS is the substrate under your agents. Each one mounts a complete, writable
> L8:  Workspace over shared committed history, does its work, commits what it changed,
> L47:  fs calls go straight into the Store as Commits; each Bash call mounts a Workspace, runs, commits and unmounts

## 星数曲线

```mermaid
xychart-beta
    title "Ephemeral-AI-Lab/layerfs 星数(近 3 点)"
    x-axis ["2026-10-23", "2026-10-24", "2026-10-25"]
    y-axis "stars" 1896 --> 2046
    line [1908, 1992, 2034]
```

2026-10-23 1,908 → 2026-10-25 2,034（+126）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `9a0ed66a3b23` · [字段定义](../../DATASET.md)*
