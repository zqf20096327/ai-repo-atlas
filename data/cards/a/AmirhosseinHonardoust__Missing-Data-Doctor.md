# AmirhosseinHonardoust/Missing-Data-Doctor

⭐ 19 · Python · MIT · 推送 2025-11-15 · [GitHub](https://github.com/AmirhosseinHonardoust/Missing-Data-Doctor) · 个人维护

**表格数据缺失值诊断与填补评估工具，输出 HTML 报告**

面向表格机器学习数据集的缺失值诊断与处理工具：统计各列缺失比例、生成柱状图与缺失矩阵热图、运行 simple/KNN/iterative 三种填补策略，并对每种策略训练随机森林模型（分类或回归任务）在留出集上评估指标，量化填补选择对模型表现的影响。结果以自包含目录输出（缺失摘要 CSV、impact.json、图片与 HTML 报告），可打包分享。以 Python 源码 + CLI 形式提供，需手动安装 pandas/numpy/scikit-learn 等依赖，自带 10 行合成示例数据集用于演示。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 按列统计缺失比例并生成柱状图与缺失矩阵热图
- simple/KNN/iterative 三种填补策略对比评估
- 每种策略训练 RandomForest 并输出指标到 impact.json
- 自包含运行目录：CSV+JSON+图片+HTML 报告，可直接分享

## 适用场景

- 建模前诊断数据集缺失模式并选择填补策略
- 对比不同填补方法对模型指标的影响
- 生成可分享的缺失值分析 HTML 报告

## 场景标签

`MLOps` · 领域:训练与推理

## 证据(README 行号)

> L3: A diagnostic & treatment suite for **missing values in tabular machine learning datasets**.
> L195: Beyond visualization, Missing Data Doctor evaluates **how different imputations affect model performance**.

## 星数曲线

```mermaid
xychart-beta
    title "AmirhosseinHonardoust/Missing-Data-Doctor 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-30 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `1a1dead23886` · [字段定义](../../DATASET.md)*
