# alp82/goodwatch-monorepo

⭐ 41 · TypeScript · MIT · 推送 2026-10-25 · [GitHub](https://github.com/alp82/goodwatch-monorepo) · [官网](https://goodwatch.app/) · 个人维护

**影视发现与个性化推荐的 Web 应用（goodwatch.app）**

面向影迷的影视发现网站，在线运行于 goodwatch.app。功能包括基于用户评分与观看历史的个性化推荐、按数百个类别（情绪、剧情、子类型、视觉风格等）为影片和剧集分类的 Fingerprint 体系、查询各流媒体平台片源可用性、聚合 IMDb/Metacritic/烂番茄评分。仓库为 monorepo：Remix Web 应用、Windmill 数据管道、Qdrant 向量库（相似检索与推荐）、CrateDB、MongoDB、Redis/Valkey 缓存、Prometheus/Grafana 监控与 Ansible 部署。本地运行指南已声明过时，需 TMDB API Key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于用户评分与观看历史的个性化推荐
- Fingerprint：数百个类别为影视分类
- 聚合 Netflix/Hulu/Prime 等流媒体片源可用性
- Qdrant 向量库支撑相似检索，Windmill 数据管道处理 ETL

## 适用场景

- 根据我看过的片子和评分找下一部想看的影视
- 在一个页面比较各平台评分和片源可用性
- 按情绪、视觉风格等维度探索影视作品

## 场景标签

`推荐系统` · 领域:学习与行业

## 证据(README 行号)

> L13: 1. Personalized Recommendations based on your ratings and watched movies & shows
> L14: 2. Fingerprint: Classify movies and TV shows by hundreds of meaningful categories (e.g. Emotions, Plot, Subgenres, 
> L27: |`goodwatch-qdrant/`|Qdrant vector database for similarity search and recommendations|

## 星数曲线

```mermaid
xychart-beta
    title "alp82/goodwatch-monorepo 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 40 --> 42
    line [41, 41]
```

2026-10-18 41 → 2026-10-25 41（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 low · 依据 README sha `6b52467518cd` · [字段定义](../../DATASET.md)*
