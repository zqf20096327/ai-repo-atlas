# mlr-org/mlr3mbo

⭐ 27 · R · 推送 2026-10-06 · [GitHub](https://github.com/mlr-org/mlr3mbo) · [官网](https://mlr3mbo.mlr-org.com) · 组织维护

**R 语言单/多目标贝叶斯优化模块化实现**

mlr3 生态中的 R6 实现库，提供单目标与多目标贝叶斯优化：由 Surrogate（代理模型）、AcqFunction（采集函数）、AcqOptimizer（采集函数优化器）三个模块类组合成 BO 循环（如 bayesopt_ego）。同时提供 OptimizerMbo（对接 bbotk 包）与 TunerMbo（对接 mlr3tuning 包）类，用于黑盒优化与超参数调优，并为各模块设有默认配置。面向使用 mlr3 生态的 R 开发者与机器学习从业者，配有论文（Patterns 期刊）。

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

- Surrogate/AcqFunction/AcqOptimizer 三模块化 R6 架构
- 支持单目标与多目标贝叶斯优化（如 bayesopt_ego）
- OptimizerMbo 与 TunerMbo 对接 bbotk 与 mlr3tuning
- 提供模块默认配置（mbo_defaults）

## 适用场景

- 对机器学习模型做超参数调优
- 优化昂贵黑盒目标函数
- 在 mlr3 生态中构建自定义贝叶斯优化流程

## 场景标签

 · 领域:机器学习/优化

## 证据(README 行号)

> L12: A new R6 and much more modular implementation for single- and
> L13: multi-objective Bayesian Optimization.
> L34: `mlr3mbo` also provides an `OptimizerMbo` class behaving like any other
> L37: from the mlr3tuning

## 星数曲线

```mermaid
xychart-beta
    title "mlr-org/mlr3mbo 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-26 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `65ed6b88c831` · [字段定义](../../DATASET.md)*
