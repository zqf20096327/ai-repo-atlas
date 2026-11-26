# vinodbavage31/ITSM-dataset-ML

⭐ 10 · Jupyter Notebook · 推送 2026-01-23 · [GitHub](https://github.com/vinodbavage31/ITSM-dataset-ML) · [官网](https://itsm-project-ui.vercel.app/) · 个人维护

**面向 ITSM 运营的事故分类与预测 ML 流水线**

基于 45K 条 ITSM 事故记录（SQL 数据源）构建的端到端数据科学项目，核心为 Jupyter Notebook：涵盖数据清洗、插补、缩放与独热编码，随后执行四个目标——高优先级票据预测、事故量时间序列预测、优先级/部门自动打标、RFC 失败概率预测；模型以 joblib 保存，另有在线 UI。需自备 MySQL 数据库连接并更新凭据后按序运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 四个预测任务：高优先级预测、事故量预测、自动打标、RFC 失败预测
- 技术栈为 Scikit-learn、XGBoost、statsmodels 与 SMOTE
- 以 Jupyter Notebook 形式按序执行预处理到建模全流程

## 适用场景

- 对 ITSM 历史工单做高优先级预测与自动分派
- 预测季度/年度事故量以辅助资源规划
- 评估变更请求（RFC）导致失败的可能性

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L6: This project delivers a robust, end-to-end data science pipeline built to analyze historical IT Service Management (
> L16: |**1. High Priority Prediction**|Forecast whether an incoming ticket will be high priority (P1/P2).|**96% Accuracy*

## 星数曲线

```mermaid
xychart-beta
    title "vinodbavage31/ITSM-dataset-ML 星数(近 2 点)"
    x-axis ["2026-10-24", "2026-11-26"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-10-24 10 → 2026-11-26 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-19 · 置信度 high · 依据 README sha `efb06c17de62` · [字段定义](../../DATASET.md)*
