# SamridhiiiGupta/ExoHabitAI

⭐ 18 · Jupyter Notebook · MIT · 推送 2026-03-31 · [GitHub](https://github.com/SamridhiiiGupta/ExoHabitAI) · [官网](https://b13-exohabitai-samridhigupta.onrender.com/) · 个人维护

**系外行星宜居性预测系统：Flask API + 交互式仪表盘**

面向天文爱好者与开发者的全栈机器学习应用：读取 NASA Exoplanet Archive 数据（30+ 天体物理特征），经清洗、中位数插补与特征工程（含 Earth Similarity Index 计算），训练 Logistic Regression、Decision Tree、Random Forest、XGBoost 五类模型并部署调优后的 Random Forest。通过 Flask 提供预测、模型信息、宜居性 Top 10 排名等 REST 端点，配套太空主题网页仪表盘与可视化，已配置 Render 部署。限制：模型指标表格留有占位符待填。

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

- 二分类宜居性预测（返回概率 0-1 与二元判定）
- 基于半径/密度/逃逸速度/表面温度计算 Earth Similarity Index
- GET /rank 返回按宜居概率排序的 Top 10 系外行星及配套指标
- 提供健康检查、模型信息、预测、排名四个 REST 端点

## 适用场景

- 输入行星参数即时获得宜居性概率预测
- 浏览按模型评分排序的最宜居系外行星榜单
- 本地运行或部署到 Render 演示 ML 流水线与可视化仪表盘

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L14: > 🌌 A full-stack machine learning system that predicts whether a distant exoplanet could harbor life —
> L24: It ingests raw exoplanet data, processes astrophysical signals, calculates Earth Similarity Indices, and deploys a 

## 星数曲线

```mermaid
xychart-beta
    title "SamridhiiiGupta/ExoHabitAI 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-29 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `ab74a254b27c` · [字段定义](../../DATASET.md)*
