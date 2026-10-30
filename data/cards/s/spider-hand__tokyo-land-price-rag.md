# spider-hand/tokyo-land-price-rag

⭐ 18 · Vue · MIT · 推送 2026-03-02 · [GitHub](https://github.com/spider-hand/tokyo-land-price-rag) · 个人维护

**用交互式地图探索东京地价的 RAG 应用**

基于检索增强生成（RAG）的东京地价查询应用：以日本国土数值信息的地价公示与行政地区数据为数据源，经 Qdrant 向量检索与 OpenAI API 生成回答，通过 Mapbox/Maplibre 交互式地图展示。技术栈包括 Vue 前端、AWS Lambda 后端、Docker 与 LocalStack 本地开发。需自备 Mapbox API key，通过 docker compose 启动本地环境。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 以国土数值信息地价公示数据为数据源的 RAG 问答
- Mapbox/Maplibre 交互式地图可视化
- Qdrant 向量检索 + OpenAI API 生成回答

## 适用场景

- 查询东京哪些区域地价最高
- 寻找涩谷附近适合居住的区域
- 在地图上交互式浏览东京地价数据

## 场景标签

`RAG` `数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L7: A Retrieval-Augmented Generation (RAG) application for exploring Tokyo land prices using an interactive map
> L39: - LLM: OpenAI API
> L53: - 国土数値情報 （地価公示データ）(Ministry of Land, Infrastructure, Transport and Tourism) https://nlftp.mlit.go.jp/ksj/gml/datali

## 星数曲线

```mermaid
xychart-beta
    title "spider-hand/tokyo-land-price-rag 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-30 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `90d97d9c29c9` · [字段定义](../../DATASET.md)*
