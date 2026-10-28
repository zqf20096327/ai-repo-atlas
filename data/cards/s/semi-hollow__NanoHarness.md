# semi-hollow/NanoHarness

⭐ 40 · Python · MIT · 推送 2026-08-26 · [GitHub](https://github.com/semi-hollow/NanoHarness) · 个人维护 · 中文 README

**面向真实代码仓库的可治理 Coding Agent 运行时控制平面**

以 Python 3.11 实现的 Coding Agent Harness：模型提出动作，Runtime 负责持久对话（Thread/Turn/Run 三层身份）、增量上下文压缩、受控工具执行（路由、授权、Approval、Ledger）、可恢复执行与事实落盘。支持 single/ultra 两种 Agent 策略，ultra 先 Planning 再走 Single 或多 Agent 协作（Worker 在独立 Git worktree 执行，Coordinator 统一调度与集成）。提供 CLI（forge run/console/resume/ui）、嵌入式 Harness API 与只读证据 Workbench，含 SWE-bench 形态的 Mini-50 评测资产。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Thread/Turn/Run 持久身份链与同 Turn Resume 恢复
- 工具执行统一经过路由、授权、Approval、Ledger 与副作用指纹去重
- single/ultra 两种 Agent 策略，ultra 支持受治理多 Agent 协作（HARD/LIVE readiness）
- 只读 Workbench 审阅 Durable Control、Multi-Agent Runtime 与 Mini-50 冻结证据

## 适用场景

- 在真实仓库上运行带审批与副作用治理的 Coding Agent
- 需要可恢复、可审计执行的长时间编码任务
- 用 trace/patch/validation 做基于证据的 Agent 评测对比

## 场景标签

`编码 Agent` `多智能体` `模型评测` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L7: **面向真实代码仓库的可治理 Coding Agent Harness。**
> L10: 同一套工作流中。模型提出动作；Runtime 管理身份、权限、副作用、恢复和事实落盘。
> L154: `forge ui` 启动只读 Workbench。Workbench 只投影已有证据，不运行 Agent，也不拥有

## 星数曲线

```mermaid
xychart-beta
    title "semi-hollow/NanoHarness 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 39 --> 41
    line [40, 40]
```

2026-10-18 40 → 2026-10-28 40（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `3259696a83c0` · [字段定义](../../DATASET.md)*
