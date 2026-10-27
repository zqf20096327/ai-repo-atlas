# ShimantoRahman/empulse

⭐ 33 · Python · AGPL-3.0 · 推送 2026-10-26 · [GitHub](https://github.com/ShimantoRahman/empulse) · [官网](https://empulse.readthedocs.io/en/stable/) · 个人维护

**Python 成本敏感/利润驱动机器学习库，兼容 scikit-learn**

Empulse 是面向成本敏感分类与价值驱动（利润驱动）机器学习的 Python 包：用户以成本矩阵定义各结果的实际代价，再据此评估模型、训练模型与设定决策阈值。提供利润驱动指标、成本敏感的 logistic 回归/梯度提升/树/森林等估计器、阈值调优、逐样本成本路由（scikit-learn metadata routing）、成本比例重采样与数据集。所有估计器遵循 scikit-learn 规范，可直接用于 Pipeline/GridSearchCV。要求 Python 3.11+，AGPLv3 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 成本矩阵驱动的模型评估、训练与决策阈值设定
- 成本敏感估计器：logistic 回归、梯度提升、树/森林、进化树等
- 逐样本成本经 metadata routing 自动通过 Pipeline 与交叉验证
- 成本比例重采样使任意估计器具备成本敏感性

## 适用场景

- 以利润而非准确率调优流失预测模型
- 信用评分与获客场景定义业务成本矩阵训练模型
- 选择最大化利润的分类阈值而非默认 0.5

## 场景标签

 · 领域:机器学习/数据分析

## 证据(README 行号)

> L20: Empulse is a Python package for cost-sensitive classification and value-driven (profit-driven)
> L69: |**Cost-sensitive models**|Logistic regression, gradient boosting, trees, forests, bagging, minimax probability mac

## 星数曲线

```mermaid
xychart-beta
    title "ShimantoRahman/empulse 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 32 --> 34
    line [33, 33]
```

2026-10-18 33 → 2026-10-27 33（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `9846c6f318d0` · [字段定义](../../DATASET.md)*
