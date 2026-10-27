# mlr-org/bbotk

⭐ 26 · R · LGPL-3.0 · 推送 2026-09-18 · [GitHub](https://github.com/mlr-org/bbotk) · [官网](https://bbotk.mlr-org.com) · 组织维护

**R 语言黑盒优化框架：优化任意用户目标函数**

mlr-org 维护的 R 黑盒优化基础包：通过 paradox 包定义搜索空间，对任意用户自定义目标函数运行优化；内置 Random Search、Grid Search、Iterated Racing，Bayesian Optimization 与 Hyperband 由 mlr3mbo/mlr3hyperband 扩展提供。它是 mlr3tuning、mlr3fselect 和 miesmuschel 的基础包，支持多目标优化，提供 bb_optimize 快速入口函数，可配合 mlr3viz 可视化优化过程。从 CRAN 安装或 GitHub 安装开发版。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | LGPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 任意用户定义目标函数的黑盒优化
- 高度可配置搜索空间（paradox，含对数变换等变换）
- 内置 Random Search/Grid Search/Iterated Racing，扩展包提供 Bayesian Optimization 与 Hyperband
- mlr3tuning/mlr3fselect/miesmuschel 的基础包

## 适用场景

- 对任意黑盒目标函数做参数优化
- 机器学习超参数调优（经 mlr3tuning）
- 多目标优化与优化过程可视化

## 场景标签

 · 领域:机器学习/优化

## 证据(README 行号)

> L12: *bbotk* is a black-box optimization framework for R. It features highly
> L20: base package of mlr3tuning,

## 星数曲线

```mermaid
xychart-beta
    title "mlr-org/bbotk 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 25 --> 27
    line [26, 26]
```

2026-10-18 26 → 2026-10-27 26（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `8ff1a84b29a7` · [字段定义](../../DATASET.md)*
