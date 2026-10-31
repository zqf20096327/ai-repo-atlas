# rclement/datasette-ml

⭐ 18 · Python · Apache-2.0 · 推送 2026-10-28 · [GitHub](https://github.com/rclement/datasette-ml) · 个人维护

**Datasette 插件：用 SQL 函数训练/评估/预测机器学习模型**

为 Datasette 提供 MLOps 面板的插件，底层功能由 sqlite-ml 提供：通过 sqml_load_dataset、sqml_train、sqml_predict、sqml_predict_batch 等 SQL 函数在 SQLite 数据旁完成数据加载、模型训练（回归/分类，算法如 logistic_regression、svc）、评估与批量预测；实验内新模型得分更高时自动部署。面向使用 Datasette/SQLite 的开发者。README 声明仍处实验阶段，可能存在破坏性变更。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- SQL 函数完成训练、评估与预测（sqml_train/sqml_predict/sqml_predict_batch）
- 实验内新模型得分超越旧模型时自动部署，预测查询无需改动
- 提供 /-/ml MLOps 仪表盘页面
- 支持加载 Scikit-Learn 标准数据集（如 Iris）

## 适用场景

- 数据已在 SQLite/Datasette 中，直接用 SQL 训练和预测模型
- 在 Datasette 界面里管理机器学习实验与部署
- 对表或视图数据做分类/回归预测而无需导出数据

## 场景标签

`MLOps` · 领域:训练与推理

## 证据(README 行号)

> L5: Datasette ML is a Datasette plugin providing an MLOps
> L6: platform to train, evaluate and make predictions from machine learning models.
> L185: This plugin registers a few SQL functions to perform machine learning model training and predictions:

## 星数曲线

```mermaid
xychart-beta
    title "rclement/datasette-ml 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-31 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `84cd89f8647a` · [字段定义](../../DATASET.md)*
