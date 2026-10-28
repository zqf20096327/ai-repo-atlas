# AdrianAntico/RetroFit

⭐ 27 · Python · MIT · 推送 2026-08-23 · [GitHub](https://github.com/AdrianAntico/RetroFit) · 个人维护

**Polars 原生的 ML 训练评分评估工作流库（CatBoost/XGBoost/LightGBM）**

面向快速迭代的机器学习工作流 Python 库：内部基于 Polars 做数据处理，封装 CatBoost、XGBoost、LightGBM 三种树模型算法，覆盖回归、二分类、多分类任务。提供目标变换（log/sqrt/standardize 等）、GPU 训练开关（自动调整树构建方法与参数）、统一评分引擎与完整评估指标（含 101 点阈值曲线）、校准表、ROC/PR 曲线、SHAP 可解释性与自包含 HTML Model Insights 报告；可视化由 QuickEcharts 生成。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Polars 原生建模管线，数据预处理与后处理全程向量化
- GPU 训练开关自动适配 CatBoost/XGBoost/LightGBM 参数
- 统一评分引擎输出预测、概率与逆变换回归值
- SHAP 特征级重要性与依赖图、自包含 HTML 模型洞察报告

## 适用场景

- 用 CatBoost/XGBoost/LightGBM 快速训练与评分监督学习模型
- 生成回归/分类的完整评估指标与阈值曲线
- 产出可分享的 HTML 模型洞察与 SHAP 可解释性报告

## 场景标签

`MLOps` `模型评测` · 领域:评测与运维

## 证据(README 行号)

> L17: ### High-Performance ML Training, Scoring & Evaluation (Polars + GPU-Ready)
> L23: ### ⚙️ 1. Polars-Native Modeling Pipeline
> L50: model = RetroFit(Algorithm="catboost", TargetType="regression", GPU=True)

## 星数曲线

```mermaid
xychart-beta
    title "AdrianAntico/RetroFit 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-28 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `f4b25a349536` · [字段定义](../../DATASET.md)*
