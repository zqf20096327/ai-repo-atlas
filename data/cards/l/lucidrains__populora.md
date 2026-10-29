# lucidrains/populora

⭐ 19 · Python · MIT · 推送 2026-10-17 · [GitHub](https://github.com/lucidrains/populora) · 个人维护

**PopuLoRA 论文实现：共享基座上协同进化 LoRA 种群**

实现 PopuLoRA（Co-Evolving LLM Populations for Reasoning Self-Play）：在共享基座模型上维护 LoRA 适配器种群，通过选择、交叉、变异演化，并将最优个体合并回基座。支持逐权重矩阵配置算子、torchrun 分布式演化、对 gymnasium/dm_control 等环境的演化（evolve_with_env）、克隆选择（AIS）、多种群协同进化（proposer/solver/judge）与批量自回归生成。以 pip 包形式提供，标注 wip。

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

- 共享基座上的 LoRA 种群演化，最优个体合并回基座
- torchrun 多 rank 分布式演化（仅同步 LoRA 权重）
- evolve_with_env 对接 gymnasium/dm_control/isaac/maniskill 等环境
- 多种群协同进化（probe/fitness 链式依赖）与批量生成

## 适用场景

- 在 GPU 上对 LLM 做 LoRA 种群自博弈演化训练
- 强化学习环境中用演化方法训练策略并合并最优个体
- 构建 proposer/solver/judge 式协同进化训练流程

## 场景标签

`微调` `强化学习` · 领域:训练与推理

## 证据(README 行号)

> L3: Implementation of PopuLoRA: Co-Evolving LLM Populations for Reasoning Self-Play (Roger Castanyer et al., vmax.ai). M
> L52: ## Environment evolution

## 星数曲线

```mermaid
xychart-beta
    title "lucidrains/populora 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-29 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `b00797d3b995` · [字段定义](../../DATASET.md)*
