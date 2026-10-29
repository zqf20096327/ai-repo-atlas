# ranasl62/ehr-risk-framework

⭐ 24 · Python · MIT · 推送 2026-10-19 · [GitHub](https://github.com/ranasl62/ehr-risk-framework) · [官网](https://ehr.larucare.com/) · 个人维护

**面向科研教学的 EHR 临床风险建模工作台，含泄露审计与校准**

用于纵向 EHR 风格数据的临床机器学习工作台：数据摄取→训练→泄露审计→校准→SHAP 解释→FastAPI 服务的研究闭环。支持逻辑回归、随机森林、XGBoost 多模型比较，时间切分与索引/视界截断防泄露，Isotonic 校准附 Brier/ECE，Angular 前端，Docker 一键部署，可导入自有 CSV（含列映射），可选 SQL/OMOP·FHIR 适配器。声明仅限科研与教学用途，输出非临床建议。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 时间切分 + 索引/视界截断的泄露审计流程
- Isotonic 校准与 Brier/ECE 报告
- SHAP 解释集成于 API 与 UI
- Docker Compose 一键部署 FastAPI + Angular 工作台

## 适用场景

- 在课程或实验室中做可复现的 EHR 风险建模教学演示
- 对自己的纵向数据训练并审计二分类风险模型
- 导出含校准曲线、SHAP 的方法报告与结果 ZIP

## 场景标签

`科研工具` `教程课程` · 领域:学习与行业

## 证据(README 行号)

> L10: **An open-source framework for leakage-safe, calibrated, and explainable EHR risk prediction.**
> L12: Leakage-aware **clinical machine learning** workbench for research and education: temporal splits, leakage audits, 
> L120: - Train logistic regression, random forest, or XGBoost on longitudinal or tabular demo data

## 星数曲线

```mermaid
xychart-beta
    title "ranasl62/ehr-risk-framework 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-29 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `efd6cc208416` · [字段定义](../../DATASET.md)*
