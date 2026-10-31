# aymenhmaidiwastaken/cosmicwatch

⭐ 14 · Python · MIT · 推送 2026-05-25 · [GitHub](https://github.com/aymenhmaidiwastaken/cosmicwatch) · 个人维护

**整合 NASA 数据的地球与太空实时监测 AI 仪表盘平台**

全栈数据智能平台，从 NASA 系数据源（系外行星档案、JPL CNEOS/Sentry、FIRMS 卫星火点）抓取并缓存数据，经 ETL 流水线用机器学习处理：KMeans/DBSCAN 做系外行星可居住性聚类与异常标记、Isolation Forest 检测小行星轨迹异常、ARIMA(2,1,2) 预测 7 天野火活动并配 CUSUM 变点检测，另提供跨模块统一威胁报告。前端为 Plotly Dash 4 暗色主题仪表盘，后端 FastAPI 提供 REST API 与 Typer CLI，数据无需 API key，6 小时自动刷新。面向想一站式监测太空与野火数据的用户。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 分析 5,000+ 系外行星：ESI 向量化计算 + KMeans 聚类 + DBSCAN 异常标记
- 小行星复合风险评分（近距离/尺寸/速度/撞击概率加权）+ Isolation Forest 轨迹异常检测
- 49,000+ 卫星火点监测：ARIMA(2,1,2) 7 天预测 + CUSUM 变点检测
- 跨模块统一威胁报告与 FastAPI REST API、Typer CLI

## 适用场景

- 浏览并筛选系外行星的可居住性与相似度分析
- 追踪近地小行星的风险评分与轨迹异常
- 监测全球野火并查看未来 7 天活动预测
- 一键生成跨模块威胁简报

## 场景标签

`数据分析` `网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L15: CosmicWatch is a full-stack data intelligence platform that ingests, processes, and visualizes real-time data from 
> L113: CosmicWatch uses AI and machine learning throughout its data processing pipeline — not as an afterthought, but as 

## 星数曲线

```mermaid
xychart-beta
    title "aymenhmaidiwastaken/cosmicwatch 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `97c90a775894` · [字段定义](../../DATASET.md)*
