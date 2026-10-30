# zclllyybb/OpenGiraffe

⭐ 105 · Python · 推送 2026-05-08 · [GitHub](https://github.com/zclllyybb/OpenGiraffe) · 个人维护

**基于 opencode 的守护进程式多 agent 自动编码任务队列**

持久化守护进程系统，调用 opencode CLI 驱动 Planner→Coder→Reviewer 流水线，批量自动探索、规划、实现与审查代码改动。任务并行运行于独立 git worktree 分支，支持从 TODO/FIXME 注释自动发现任务、持续探索代码库的 Explorer agent、多模型多评审员投票与失败重试，状态存于 SQLite 可断点恢复。提供 Web 仪表盘（FastAPI）管理任务与运行时模型配置。需 Python 3.11+、opencode CLI 与 git 仓库。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Explorer 持续探索代码库并自主提出潜在重构/缺陷/缺失功能任务
- TODO/FIXME 扫描后由 AI 按可行性与难度评分生成优先级任务清单
- 每任务独立 git worktree 分支并行执行，互不冲突
- 多评审模型投票，全部通过才算完成；失败自动带反馈重试

## 适用场景

- 提交多个编码任务后离场，由守护进程并发完成规划、编码与审查
- 从仓库 TODO/FIXME 注释自动生成并分发待办任务
- 对补丁或 PR 提交仅评审不生成代码的 review-only 模式

## 场景标签

`多智能体` `编码 Agent` · 领域:Agent 开发

## 证据(README 行号)

> L7: A persistent, daemon-based multi-agent system that leverages opencode to **automatically explore, discover, plan, im
> L82: - opencode CLI installed and configured with at least one model provider

## 星数曲线

```mermaid
xychart-beta
    title "zclllyybb/OpenGiraffe 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 104 --> 106
    line [105, 105]
```

2026-10-18 105 → 2026-10-30 105（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `49bd8b524973` · [字段定义](../../DATASET.md)*
