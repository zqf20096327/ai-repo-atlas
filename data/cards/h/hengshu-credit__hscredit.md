# hengshu-credit/hscredit

⭐ 21 · Python · MIT · 推送 2026-10-28 · [GitHub](https://github.com/hengshu-credit/hscredit) · [官网](https://hscredit.hengshucredit.com) · 组织维护 · 中文 README

**给信贷风控人员的全流程量化建模 Python 工具箱**

面向金融风控策略与模型人员的 Python 库，覆盖数据探索（IV/KS/PSI、Vintage、Roll Rate）、分箱与 WOE 编码、组合特征筛选、逻辑回归与评分卡（含 PMML 导出）、XGBoost/LightGBM 等集成模型、Optuna 超参搜索、SHAP 解释、规则评估与挖掘，以及多 Sheet Excel 报告生成。分箱、编码、筛选组件兼容 sklearn Pipeline 接口，分析结果以中文指标、表格和图表返回，另提供 SQL/NoSQL 数据接入。支持 Python 3.9–3.14，按需可选依赖分 extras 安装。

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

- EDA、分箱编码、筛选、评分卡、建模、规则分析与 Excel 报告贯通一套工作流
- 分箱/编码/筛选组件兼容 sklearn Pipeline，支持 fit(X, y) 或 target 指定标签列
- 支持 XGBoost/LightGBM/CatBoost/NGBoost 与 ResNet/FTTransformer/TabM 等 net 模型
- 评分卡含完整 points 表、PMML 导出；报告支持条件格式、透视表与超链接

## 适用场景

- 信贷场景下做特征分箱、WOE 编码与评分卡建模
- 评估风控规则的置入置出与策略迭代效果
- 生成变量/模型/策略的中文 Excel 评审报告
- 对模型做 SHAP 解释、原因码与反事实分析

## 场景标签

`金融量化` · 领域:学习与行业

## 证据(README 行号)

> L14: hscredit（衡枢真信）将数据探索、分箱编码、特征筛选、评分卡与机器学习、规则分析和 Excel 报告串成一套工作流。分箱、编码和筛选组件兼容 sklearn Pipeline，分析结果以中文指标、表格和图表返回。
> L38: |模型训练|RandomForest、ExtraTrees、GradientBoosting、XGBoost、LightGBM、CatBoost、NGBoost、校准、自定义损失与完整评估|模型与报告|
> L40: |模型可解释性|全局重要性、SHAP 分布与依赖、单样本贡献、原因码与反事实分析|模型解释|

## 星数曲线

```mermaid
xychart-beta
    title "hengshu-credit/hscredit 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-28 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `94dfaa38187b` · [字段定义](../../DATASET.md)*
