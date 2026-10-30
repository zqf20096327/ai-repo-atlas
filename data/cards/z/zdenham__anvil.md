# zdenham/anvil

⭐ 89 · TypeScript · MIT · 推送 2026-03-31 · [GitHub](https://github.com/zdenham/anvil) · [官网](https://www.anvil.fm) · 个人维护

**管理多个编码 agent 并行工作的桌面 IDE**

面向并行运行多个编码 agent 的桌面 IDE：以隔离的 git worktree 实现并行开发避免分支冲突，内置终端、文件编辑器与 diff 查看器，提供 agent 生命周期管理、spec 阶段跟踪与计划执行、子 agent 活动可视化，以及让 Claude 以编程方式调用其他 Claude 的 REPL 编排能力；agent 可按最多 4×3 网格排列。作者因管理多个终端中的 Claude Code 会话的痛点而开发，以桌面应用形式下载，MIT 许可。

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

- 隔离 git worktree 支持多 agent 并行无合并冲突
- agent 生命周期、阶段跟踪与计划执行内置于工作流
- REPL 编排：可让 Claude 以编程方式调用其他 Claude
- 子 agent 与孙 agent 活动可视化，支持 4×3 面板网格布局

## 适用场景

- 并行运行多个编码 agent 处理不同任务
- 在统一窗口中查看各 agent 的终端、文件与 diff
- 跨 agent 共享计划并跟踪执行阶段

## 场景标签

`多智能体` `编码 Agent` · 领域:Agent 开发

## 证据(README 行号)

> L7:  A desktop IDE for parallel agent work.
> L31: |**REPL & orchestration**|Let Claude call other Claudes programmatically. Flexible building blocks, not rigid workf

## 星数曲线

```mermaid
xychart-beta
    title "zdenham/anvil 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 88 --> 90
    line [89, 89]
```

2026-10-18 89 → 2026-10-30 89（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `12c1ea3db0ba` · [字段定义](../../DATASET.md)*
