# lil-lab/knotgym

⭐ 20 · Python · 推送 2026-06-09 · [GitHub](https://github.com/lil-lab/knotgym) · [官网](https://lil-lab.github.io/knotgym/) · 组织维护

**视觉空间推理（打结）研究的极简强化学习环境**

由 lil-lab 发布、入选 NeurIPS D&B 2025 的 gym 环境库，用于研究打结场景下的空间推理。基于 MuJoCo 提供可视化交互，依赖 pyknotid 的 cython 扩展（chelpers）计算 Gauss code 以加速训练。安装流程为 git clone 源码后用 uv 构建，需手动编译 cython 扩展，并在 baselines/ 目录提供基线实验入口。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 面向空间推理的 gym 环境库，配套 NeurIPS D&B 2025 论文
- MuJoCo 可视化交互（mjpython + glfw）
- pyknotid chelpers 计算 Gauss code，训练时可显著加速
- 提供 baselines 目录

## 适用场景

- 在打结任务上训练与评测强化学习/空间推理 agent
- 研究视觉空间推理的极简基准环境
- 复现论文中的基线实验

## 场景标签

`强化学习` `模型评测` · 领域:评测与运维

## 证据(README 行号)

> L5: A minimalistic environment for spatial reasoning.
> L53: @misc{chen2025knotsimpleminimalisticenvironment,
> L54:       title={Knot So Simple: A Minimalistic Environment for Spatial Reasoning},

## 星数曲线

```mermaid
xychart-beta
    title "lil-lab/knotgym 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-28"]
    y-axis "stars" 18 --> 21
    line [19, 20, 20]
```

2026-10-18 19 → 2026-10-28 20（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `e05e2c764ffe` · [字段定义](../../DATASET.md)*
