# simon-hirsch/ondil

⭐ 39 · Python · GPL-3.0 · 推送 2026-06-16 · [GitHub](https://github.com/simon-hirsch/ondil) · [官网](https://simon-hirsch.github.io/ondil/) · 个人维护

**Python 在线分布回归库：流式增量估计 GAMLSS 等模型**

提供分布回归与线性回归模型的在线（增量）估计的 Python 包：通过 model.update(X, y) 增量更新模型而无需全量重训，适用于大数据或流式数据。包含带 Lasso/Ridge/Elastic Net 正则的在线线性回归、GAMLSS（位置-尺度-形状广义可加模型）的在线实现及其多变量扩展。支持 Gaussian、Student's t、Johnson's SU、Gamma 等多种分布与自定义连接函数，估计器兼容 scikit-learn，用 numba 做即时编译。前身为 rolch。面向做概率预测（如风电出力、波动率建模）的研究者与开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 在线增量更新 model.update(X, y)，无需全量重训
- GAMLSS 的原生 Python 实现及多变量扩展
- 支持 Gaussian/Student's t/Johnson's SU/Gamma 等多种分布与灵活连接函数
- 与 scikit-learn 估计器/transformer 兼容，numba 加速

## 适用场景

- 流式或大数据场景下增量估计回归模型
- 对波动率、偏度、尾部行为建模的条件概率预测（如电力市场风电预测）
- 需要 Lasso/Ridge/Elastic Net 正则化的在线回归
- 用 CRPS 评分评估分布预测（可选依赖 scoringrules）

## 场景标签

 · 领域:统计学习/概率预测

## 证据(README 行号)

> L12: This package provides an online estimation of distributional regression and linear regression models in Python. We 
> L34: - 🚀 First native `Python` implementation of generalized additive models for location, shape and scale (GAMLSS).

## 星数曲线

```mermaid
xychart-beta
    title "simon-hirsch/ondil 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 38 --> 40
    line [39, 39]
```

2026-10-18 39 → 2026-10-30 39（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `ddfa6fc5a49c` · [字段定义](../../DATASET.md)*
