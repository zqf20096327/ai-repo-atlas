# kamalesh404/Ai-predictive-analytics

⭐ 16 · Python · MIT · 推送 2026-08-20 · [GitHub](https://github.com/kamalesh404/Ai-predictive-analytics) · 个人维护

**表格数据预测分析平台：训练模型并通过 CLI/API/网页提供预测**

基于 scikit-learn 的端到端机器学习流水线：读取 CSV，自动清洗（去空行、去重、缺失值填补、标准化/独热编码），按目标列自动判定分类或回归任务，支持随机森林、梯度提升、逻辑回归、Ridge 等模型训练，输出准确率/ROC-AUC/R² 等评估指标与特征重要性。模型经 joblib 持久化并带时间戳版本，推理时使用与训练一致的预处理，支持单条与批量预测。面向开发者，提供 Typer CLI、FastAPI REST API（Swagger UI 与浏览器表单）、Docker 镜像、GitHub Actions CI/CD 与 Render 一键部署蓝图；模型仅限表格监督学习场景。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 分类/回归任务自动检测，支持 4 类模型（random_forest/gradient_boosting/logistic_regression/ridge）
- 同一预处理在训练与预测阶段复用，支持单条与批量预测
- 模型以 joblib 持久化并生成时间戳版本副本，存储指标等元数据
- 提供 Typer CLI、FastAPI API（Swagger/浏览器表单）与 Docker 镜像

## 适用场景

- 用自己的 CSV 数据训练客户流失、贷款违约等预测模型
- 通过 REST API 或网页表单对新记录做实时预测
- 对整个 CSV 文件批量打分并输出预测结果

## 场景标签

 · 领域:数据分析/机器学习

## 证据(README 行号)

> L3: A complete, production-shaped machine learning platform that takes raw tabular data, trains
> L41: - **6 models** across two task types, with automatic task detection from the target:
> L84: |Machine Learning|scikit-learn|

## 星数曲线

```mermaid
xychart-beta
    title "kamalesh404/Ai-predictive-analytics 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `2360ada13cc0` · [字段定义](../../DATASET.md)*
