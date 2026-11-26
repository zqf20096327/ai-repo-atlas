# RozhakDev/AirHealthClassifier

⭐ 12 · Jupyter Notebook · MIT · 推送 2026-11-20 · [GitHub](https://github.com/RozhakDev/AirHealthClassifier) · 个人维护

**基于KNN与NCA的空气质量健康影响分类实验项目**

这是一个机器学习实验仓库，使用 Kaggle 的空气质量与健康影响数据集（5,520 行、4 个类别、6 个核心污染物特征），通过 sklearn Pipeline 构建 StandardScaler → NCA → KNN 分类流程，预测健康影响类别。项目包含数据清洗（移除随机标签尾部数据、剔除泄露风险的评分列）、5 折分层交叉验证与超参数调优，以及单次 hold-out 测试。模型产物保存为 joblib 文件，需 Python 3.13+ 并通过 notebook 执行。

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

- StandardScaler → NCA → KNN 的 sklearn Pipeline 分类流程
- 5-Fold Stratified 交叉验证 + hold-out 测试的无泄漏评估
- 模型产物保存为 knn_air_health.joblib 与 metrics.json
- 数据清洗记录与 DATASET.md 中的数据集许可归属（CC BY 4.0）

## 适用场景

- 复现空气质量健康影响多分类实验
- 学习 NCA 降维配合 KNN 的建模方法
- 参考无数据泄漏的模型评估流程

## 场景标签

 · 领域:机器学习/环境健康

## 证据(README 行号)

> L3: Klasifikasi multi-kelas untuk memprediksi kategori dampak kesehatan (`HealthImpactClass`) dari enam parameter poluta
> L9: Pipeline akhir menggunakan 6 fitur polutan inti (`AQI`, `PM10`, `PM2_5`, `NO2`, `SO2`, `O3`) melalui `StandardScaler

## 星数曲线

```mermaid
xychart-beta
    title "RozhakDev/AirHealthClassifier 星数(近 2 点)"
    x-axis ["2026-11-21", "2026-11-26"]
    y-axis "stars" 11 --> 13
    line [12, 12]
```

2026-11-21 12 → 2026-11-26 12（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `a41988dc8e28` · [字段定义](../../DATASET.md)*
