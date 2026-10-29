# mlr-org/mlr3hyperband

⭐ 19 · R · LGPL-3.0 · 推送 2026-09-23 · [GitHub](https://github.com/mlr-org/mlr3hyperband) · [官网](https://mlr3hyperband.mlr-org.com) · 组织维护

**R 包：为 mlr3 生态提供 Successive Halving 与 Hyperband 超参数优化算法**

mlr3 生态的 R 扩展包，实现 Successive Halving 与 Hyperband 两种多保真度优化算法，提供 mlr3tuning 的超参数调优器与 bbotk 的黑盒优化优化器。实现包含改进的调度机制，并支持配置评估的并行化。示例演示以 XGBoost 的 boosting 轮数为保真度参数，在 Sonar 数据集上调参并拟合最终模型。通过 CRAN 或 GitHub 安装，附带 mlr3book 章节与案例研究等资源。

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

- 实现 Successive Halving 与 Hyperband 算法
- 提供 mlr3tuning 调优器与 bbotk 黑盒优化器
- 改进调度并并行化配置评估
- 以 `budget` 标签定义保真度参数（如 XGBoost 的 nrounds）

## 适用场景

- 在 mlr3 流水线中对学习器做超参数调优
- 用 Hyperband 在有限预算下筛选大量超参数配置
- 结合数据子采样调优支持向量机等模型

## 场景标签

`MLOps` · 领域:训练与推理

## 证据(README 行号)

> L11: *mlr3hyperband* adds the optimization algorithms Successive Halving
> L15: evaluation of configurations. The package includes tuners for

## 星数曲线

```mermaid
xychart-beta
    title "mlr-org/mlr3hyperband 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-29 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `851e5c070999` · [字段定义](../../DATASET.md)*
