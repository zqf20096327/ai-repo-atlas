# ModelOriented/treeshap

⭐ 106 · R · GPL-3.0 · 推送 2026-05-13 · [GitHub](https://github.com/ModelOriented/treeshap) · [官网](https://modeloriented.github.io/treeshap/) · 组织维护

**R 包：用 TreeSHAP 算法为树集成模型计算 SHAP 值**

R 语言包，实现 TreeSHAP 算法为树集成模型计算 SHAP 值与交互值，复杂度为多项式级 O(TLD²)。支持 xgboost、lightgbm、gpboost、gbm、ranger、randomForest 包训练的模型，catboost 支持仅在单独分支提供；通过 unify() 将各类模型转为统一表示后计算。附带 4 种绘图函数（特征贡献、重要性、依赖、交互）及 predict()。可从 CRAN 或 GitHub 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- TreeSHAP 算法多项式时间计算 SHAP 值与交互值
- 支持 xgboost/lightgbm/gpboost/gbm/ranger/randomForest 六类模型
- unify() 统一模型表示，附 4 种可视化函数
- catboost 支持在独立分支维护（主分支因 CRAN 不可用已移除）

## 适用场景

- 解释 xgboost/lightgbm 等树模型的单条预测归因
- 分析特征重要性与特征间交互影响
- 可视化 SHAP 结果用于模型解释报告

## 场景标签

 · 领域:机器学习可解释性（XAI）

## 证据(README 行号)

> L12: `treeshap` is an efficient answer for this question. Due to implementing
> L13: an optimized algorithm for tree ensemble models (called TreeSHAP), it
> L14: calculates the SHAP values in polynomial (instead of exponential) time.

## 星数曲线

```mermaid
xychart-beta
    title "ModelOriented/treeshap 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-25"]
    y-axis "stars" 104 --> 107
    line [105, 106, 106]
```

2026-10-18 105 → 2026-10-25 106（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `3794a3550cf2` · [字段定义](../../DATASET.md)*
