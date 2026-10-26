# deephyper/deephyper

⭐ 310 · Python · BSD-3-Clause · 推送 2026-03-27 · [GitHub](https://github.com/deephyper/deephyper) · [官网](https://deephyper.readthedocs.io) · 组织维护

**面向机器学习的可大规模并行超参数优化 Python 库**

以超参数优化（HPO）为核心的 Python 库，并在此基础上提供神经架构搜索、多保真与集成能力。用户定义黑盒函数后，通过 Evaluator 分发多次评估的计算（单机或多机分布式），再用 CBO 贝叶斯搜索等算法寻找最大化目标值的参数配置。面向机器学习从业者与数据科学家，由 Argonne 国家实验室（UChicago Argonne）维护，以 BSD 许可分发，安装方式为 pip install deephyper。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | BSD-3-Clause |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单机与多机分布式的大规模并行超参数优化
- 基于 HPO 核心的神经架构搜索、多保真与集成能力
- Evaluator 分发评估 + CBO 贝叶斯搜索的编程接口

## 适用场景

- 优化机器学习模型的超参数
- 在集群或多机上分布式运行超参数搜索
- 执行神经架构搜索任务

## 场景标签

`MLOps` · 领域:训练与推理

## 证据(README 行号)

> L7: # DeepHyper: A Python Package for Massively Parallel Hyperparameter Optimization in Machine Learning
> L9: DeepHyper is first and foremost a hyperparameter optimization (HPO) library. By leveraging this core HPO functionnal
> L71: Copyright © 2019, UChicago Argonne, LLC

## 星数曲线

```mermaid
xychart-beta
    title "deephyper/deephyper 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 309 --> 311
    line [310, 310]
```

2026-10-18 310 → 2026-10-26 310（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `276c629bd324` · [字段定义](../../DATASET.md)*
