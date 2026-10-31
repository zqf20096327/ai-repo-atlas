# han20192019/skill-composition-benchmark

⭐ 13 · Python · Apache-2.0 · 推送 2026-01-02 · [GitHub](https://github.com/han20192019/skill-composition-benchmark) · [官网](https://computationalrobotics.seas.harvard.edu/SkillComposition/) · 个人维护

**机器人操作技能组合基准：5 组长程组合任务环境**

论文 Compose by Focus: Scene Graph-based Atomic Skills (arXiv:2509.16053) 的基准环境发布仓库。基于 ManiSkill2 构建，用于评测组合式长程多步机器人操作技能：任务以原子技能环境（*_skill_*）与组合任务环境（*_compose*）两种形式提供，组合任务要求在共享场景下顺序执行多个原子技能。包含 Cube Out and In、Sort by Color、Blocks Stacking Game、Tools Usage、Obstacle Avoidance 五组新组合任务，并附带各任务的运动规划脚本，强调对场景变化与长程组合的鲁棒性。通过脚本运行全部场景，任务细节需参考论文。面向具身智能与机器人学习研究者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于 ManiSkill2 的机器人操作基准环境
- 5 组新组合任务，覆盖原子技能与组合任务两种形式
- 提供所有任务的运动规划脚本
- 强调场景变化鲁棒性与长程技能组合

## 适用场景

- 评测机器人操作技能的组合泛化能力
- 在长程多步操作任务上对比学习方法
- 复现论文 Compose by Focus 的实验场景

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L3: This repository releases the **benchmark environments** used in
> L6: The benchmark is built on **ManiSkill2** and is designed to evaluate

## 星数曲线

```mermaid
xychart-beta
    title "han20192019/skill-composition-benchmark 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 12 --> 14
    line [13, 13]
```

2026-10-18 13 → 2026-10-31 13（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `4e9257488f5a` · [字段定义](../../DATASET.md)*
