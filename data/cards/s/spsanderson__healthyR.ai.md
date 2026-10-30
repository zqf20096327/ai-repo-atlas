# spsanderson/healthyR.ai

⭐ 18 · R · NOASSERTION · 推送 2026-08-22 · [GitHub](https://github.com/spsanderson/healthyR.ai) · [官网](http://www.spsanderson.com/healthyR.ai/) · 个人维护

**面向医疗数据分析的 R 机器学习/AI 建模工具包**

healthyR 包的机器学习与 AI 建模扩展，为医疗数据分析提供动词式一致接口：覆盖多算法 AutoML 与超参数调优（C5.0、Cubist、Random Forest、XGBoost、SVM、GLMnet、KNN、MARS）、K-Means 自动聚类与 UMAP/PCA 降维、缩放/傅里叶/多项式等预处理变换、以及医疗指标控制图和分布分析可视化。基于 tidymodels 生态构建，与 recipes/parsnip/tune/workflows/yardstick 集成。面向医疗数据分析师与数据科学家，以 R 包形式从 CRAN 或 GitHub 安装。生命周期徽章标注为 experimental。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 多算法 AutoML 与自动超参数调优（树模型/SVM/弹性网/KNN/MARS 等）
- K-Means 自动最优聚类检测（scree plot 与肘部法）
- UMAP/PCA 降维与可视化
- 医疗统计过程控制图（SPC）与色盲友好调色板
- 与 tidymodels（recipes/parsnip/tune/workflows）集成的自定义预处理步骤

## 适用场景

- 预测住院患者住院时长
- 用多算法预测再入院率并自动调参
- 用控制图监控医疗质量指标
- 通过聚类识别患者群组并预处理医疗数据

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L15: `healthyR.ai` is a comprehensive R package designed to streamline
> L25: Automated machine learning with hyperparameter tuning for multiple

## 星数曲线

```mermaid
xychart-beta
    title "spsanderson/healthyR.ai 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-30 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `7812396371a8` · [字段定义](../../DATASET.md)*
