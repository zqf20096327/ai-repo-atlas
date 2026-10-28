# strands-labs/harness-optimizer

⭐ 59 · Python · Apache-2.0 · 推送 2026-10-19 · [GitHub](https://github.com/strands-labs/harness-optimizer) · [官网](https://strandsagents.com) · 组织维护

**面向 LLM agent 的 harness 优化框架，用可调 Formula 与轨迹驱动优化器**

基于 Strands Agents 构建的 Python 框架，用于定义、挂载和优化 LLM agent 的上下文单元（如 system prompt）。核心机制：Trainer.fit() 循环中由 DataLoader 产出任务样本，AgentRolloutEngine 以当前 Formula 参数执行 agent 生成 rollout，RewardFunction 打分，FormulaOptimizer 依据累积的 rollout 与奖励更新参数。提供 Formula 抽象基类、Strands adapter、CandidateSearchOptimizer（在留出数据上对候选 Formula 做门控选择）等接口。注意：ContextUnitProcessor (CUP) 已更名为 Formula，旧名经 compat 模块带弃用警告提供。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Formula 定义可调上下文单元，经 Trainer 循环用 rollout 轨迹优化参数
- CandidateSearchOptimizer 在留出样本上对候选 Formula 做门控比较与选择
- 通过 hook 回调将 Formula 挂载到 Strands agent
- 核心依赖仅 strands-agents 系列、jinja2、botocore，无 PyTorch 依赖

## 适用场景

- 自动优化 agent 的 system prompt 等上下文配置
- 基于任务轨迹与奖励信号迭代 agent harness 参数
- 在留出数据上比较并选择更优的候选 Formula

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L18: A framework for optimizing LLM agent harness through Formulas.
> L22: Harness Optimizer provides a framework for defining, attaching, and optimizing context units (e.g., system prompts)
> L16:  Built on Strands Agents

## 星数曲线

```mermaid
xychart-beta
    title "strands-labs/harness-optimizer 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-22", "2026-10-28"]
    y-axis "stars" 54 --> 60
    line [55, 56, 59, 59]
```

2026-10-18 55 → 2026-10-28 59（+4）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `c7390690c8a6` · [字段定义](../../DATASET.md)*
