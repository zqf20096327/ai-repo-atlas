# AmirhosseinHonardoust/Forecast-Factory

⭐ 25 · Python · MIT · 推送 2025-11-07 · [GitHub](https://github.com/AmirhosseinHonardoust/Forecast-Factory) · 个人维护

**基于 Prophet 的业务预测与 what-if 情景模拟平台**

用 Python、Streamlit、Prophet 和 SQLAlchemy 构建的交互式预测模拟工具：读取 SQL/CSV 数据，用 Prophet 建模趋势、节假日与季节性（移动平均作基线），通过价格弹性、媒体响应、促销效应等系数公式生成差分情景预测，并用 Streamlit/Plotly 实时可视化，支持 CSV/Markdown 导出与自动叙事摘要。面向分析师、数据科学家与业务策略人员。当前以源码方式运行，数据库默认 SQLite，README 的 XGBoost/LSTM 等为未来计划而非已实现功能。

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

- Prophet 预测 + 移动平均基线，含 MAE/RMSE/SMAPE 回测验证
- 情景引擎基于弹性公式（价格弹性/媒体响应/促销效应）生成差分预测
- Streamlit + Plotly 交互式可视化，支持 CSV/Markdown 导出
- SQLAlchemy 数据层，默认 SQLite 可扩展 PostgreSQL/Snowflake

## 适用场景

- 模拟广告预算、定价或促销调整对业务指标的影响
- 对收入预测做压力测试与敏感性分析
- 生成带置信区间的基线预测并量化情景差分

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L3: ForecastFactory is an advanced **AI-powered forecasting and simulation platform** built with **Python, Streamlit, Pr
> L23: * **AI Forecasting:** Prophet-based trend, holiday, and seasonality modeling.
> L54: * Powered by **Prophet**, modeling seasonality, trend, and holiday effects.

## 星数曲线

```mermaid
xychart-beta
    title "AmirhosseinHonardoust/Forecast-Factory 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-28 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `7a803a06d4de` · [字段定义](../../DATASET.md)*
