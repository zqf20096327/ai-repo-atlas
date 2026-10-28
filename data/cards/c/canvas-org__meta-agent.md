# canvas-org/meta-agent

⭐ 80 · Python · MIT · 推送 2026-08-06 · [GitHub](https://github.com/canvas-org/meta-agent) · 个人维护

**研究原型：不更新权重、持续优化 agent 外围 harness 的框架**

面向研究者的 agent harness 持续优化框架：把模型周围的决策程序（提示词、工具、验证/重试逻辑、停止条件、子 agent 编排等）视为可编辑程序，通过快循环运行 harness、记录轨迹、诊断失败、生成并评估候选改动；实验性慢循环迭代改进提案者指令。基模型保持冻结，学习成果存于 harness 代码与磁盘经验库。技术报告在 tau-bench v3 单次运行上评估了快循环；慢循环与迁移能力尚未测量。需 Python 3.11+，从源码安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 快循环：运行-诊断-提案-评估-选择，可改写提示词/工具/验证逻辑/停止条件等完整 harness
- 实验性慢循环：周期性回顾迭代并版本化更新提案者指令（--evolve-skill）
- 经验库持久保存每个候选的任务、假设、代码改动与结果，支持 meta-agent list/pareto/diff 审计
- 基模型权重冻结，benchmark 适配器与 harness 边界分离，不改 benchmark 与模型

## 适用场景

- 研究者探索 agent harness 自动优化与持续学习
- 在不改模型权重的前提下改进任务求解程序（提示词、工具编排、停止条件）
- 审计与复现 harness 搜索过程（逐候选溯源）

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L35: Meta-Agent treats that harness as an editable program. It runs the current
> L36: harness, records task-level traces and outcomes, proposes a targeted change,
> L138: The benchmark adapter owns task selection, labels, and scoring. The harness
> L139: owns the decision procedure. This boundary lets Meta-Agent change agent

## 星数曲线

```mermaid
xychart-beta
    title "canvas-org/meta-agent 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-26", "2026-10-28"]
    y-axis "stars" 78 --> 81
    line [79, 80, 80]
```

2026-10-18 79 → 2026-10-28 80（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `e127ffbb4417` · [字段定义](../../DATASET.md)*
