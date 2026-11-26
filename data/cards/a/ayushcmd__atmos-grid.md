# ayushcmd/atmos-grid

⭐ 51 · Python · Apache-2.0 · 推送 2026-11-21 · [GitHub](https://github.com/ayushcmd/atmos-grid) · [官网](https://atmosgrid.streamlit.app/) · 组织维护

**面向印度的卫星空气质量分析与 HCHO 热点检测平台**

AtmosGrid 结合地面监测数据、Sentinel-5P/TROPOMI 卫星观测与机器学习，提供两个功能：用 XGBoost 回归模型基于历史 AQI 观测估算地面空气质量指数，以及用 DBSCAN 空间聚类识别 HCHO 浓度升高的热点区域。结果通过 Streamlit 交互式仪表板展示，包含全国地理总览、AQI 分析、热点浏览器与数据质量说明，支持 CSV/GeoJSON 导出。项目源自 ISRO BAH 2026 黑客松问题陈述，README 明确声明当前地面站点仅覆盖 4 个邦的 6 个站点，尚无经验证的全国性 AQI 预测模型。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- XGBoost 回归模型基于历史 AQI 观测做地面空气质量估算（测试 R² 0.794）
- DBSCAN + Haversine 距离识别 Sentinel-5P HCHO 浓度聚类（检测到 3 个簇）
- Streamlit 交互式仪表板展示站点、聚类与行政边界地图
- 支持 CSV/GeoJSON 导出与数据来源、局限性的文档化

## 适用场景

- 探索印度地面监测站与卫星观测的空气质量数据
- 查看 HCHO 浓度升高区域的空间聚类分布
- 复现基于卫星与地面数据的 AQI 建模分析流程

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L15: AtmosGrid is a satellite-assisted environmental monitoring and research platform developed to explore two interconn
> L56: - Train and evaluate an XGBoost regression model using historical AQI observations.
> L128: AtmosGrid uses an XGBoost regression model trained on historical daily AQI observations.


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `0abe92615776` · [字段定义](../../DATASET.md)*
