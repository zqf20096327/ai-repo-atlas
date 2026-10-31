# MAIF/eurybia

⭐ 224 · Jupyter Notebook · Apache-2.0 · 推送 2026-10-26 · [GitHub](https://github.com/MAIF/eurybia) · [官网](https://maif.github.io/eurybia/) · 组织维护

**监测机器学习模型数据漂移并生成 HTML 报告的 Python 库**

面向数据科学家与数据分析师的模型监测库：通过训练一个二分类模型（datadrift classifier）区分基线数据集与生产数据集，以 AUC 指标量化数据漂移程度，并通过可解释性定位引发漂移的关键特征。三步流程：声明 SmartDrift 对象、compile、generate_report 输出 HTML 报告，覆盖特征重要性、分布对比、AUC 演化与模型性能演化等内容。可用于部署前数据校验，支持配合 Airflow 等调度器周期性监测。基于 Shapash、Panel、Plotly、Catboost 构建，支持 Python 3.9–3.12。概念漂移与 API 模式尚在路线图中。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 以二分类模型 AUC 量化数据漂移程度
- 生成含特征重要性、分布对比、性能演化的 HTML 报告
- 支持部署前数据校验与周期性调度监测（如 Airflow）
- 基于 Shapash 提供漂移分类器的可解释性

## 适用场景

- 模型上线前校验生产数据与训练数据的一致性
- 定期监测生产环境中的数据漂移与模型性能衰减
- 与业务方共享 HTML 报告讨论模型监测结果

## 场景标签

`MLOps` · 领域:训练与推理

## 证据(README 行号)

> L35: **Eurybia** is a Python library which aims to help in :
> L39: Eurybia addresses challenges of **industrialisation** and **maintainability** of machine learning models over time.
> L141: To use Eurybia to monitor drift over time, you can use a scheduler to make computations automatically and periodic

## 星数曲线

```mermaid
xychart-beta
    title "MAIF/eurybia 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 223 --> 225
    line [224, 224]
```

2026-10-18 224 → 2026-10-31 224（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `167a953b98a4` · [字段定义](../../DATASET.md)*
