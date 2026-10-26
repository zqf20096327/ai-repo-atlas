# bgreenwell/vip

⭐ 193 · R · 推送 2026-07-05 · [GitHub](https://github.com/bgreenwell/vip) · [官网](https://bgreenwell.github.io/vip/) · 个人维护

**R 包：量化并可视化模型预测中各特征的重要性**

面向 R 用户的变量重要性分析包：vi() 计算各特征对已拟合模型预测的贡献分数并返回整洁数据框，vip() 基于 tinyplot 绘制重要性图。支持数十种模型类（ranger、xgboost、lightgbm、glmnet、tidymodels、mlr3 等），提供模型自带重要性、置换重要性、Shapley 与方差四种方法，模型无关方法仅需用户提供预测包装函数。已从 CRAN 迁移至 r-universe，0.5.0 为破坏性版本（绘图改用 base R 图形）。

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

- vi()/vip() 支持数十种 R 模型类
- 四种重要性方法：模型自带/置换/Shapley/方差
- 模型无关方法仅需预测包装函数，可配合任意模型
- 依赖极少：仅 base R 包与 tinyplot

## 适用场景

- 解释已训练机器学习模型中哪些特征驱动预测
- 生成变量重要性图表用于分析报告
- 跨多种模型统一计算特征重要性分数

## 场景标签

 · 领域:机器学习/模型解释

## 证据(README 行号)

> L8: Variable importance plots (VIPs) for R: quantify and visualize which features
> L14: - **Model-specific and model-agnostic methods** — native importance measures

## 星数曲线

```mermaid
xychart-beta
    title "bgreenwell/vip 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 192 --> 194
    line [193, 193]
```

2026-10-18 193 → 2026-10-26 193（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `2c645bf362a3` · [字段定义](../../DATASET.md)*
