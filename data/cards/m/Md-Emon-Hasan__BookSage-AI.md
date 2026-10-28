# Md-Emon-Hasan/BookSage-AI

⭐ 21 · Python · MIT · 推送 2026-08-05 · [GitHub](https://github.com/Md-Emon-Hasan/BookSage-AI) · [官网](https://booksage-ai.onrender.com/) · 个人维护

**混合图书推荐系统：协同过滤+内容过滤加权融合**

面向书店、图书馆或阅读应用的图书推荐系统：用 scikit-learn kNN 协同过滤（SciPy 稀疏用户-物品矩阵）与 TF-IDF 余弦相似度内容模型加权融合，在 110 万条评分的 Book-Crossing 数据集上训练。前后端解耦，FastAPI JSON API 独立于 React 19 单页应用（Vite/Tailwind），带 cachetools TTL 内存缓存与 slowapi 限流，无需 Redis。推荐结果显示评分与元数据，未识别书名返回空结果；冷启动走热门书回退。提供 Docker 镜像与 docker-compose 编排，CI 要求后端 100% 覆盖率。

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

- kNN 协同过滤 + TF-IDF 内容模型的加权平均融合
- 基于 Book-Crossing 110 万条评分数据训练
- FastAPI + React 19 前后端解耦，带 TTL 缓存与限流
- 未识别书名返回空结果而非猜测，推荐附带评分展示

## 适用场景

- 读书应用或书店网站嵌入图书推荐功能
- 按书名查找相似书籍并获得带评分的排序列表
- 作为 FastAPI 服务为其他系统提供推荐 API

## 场景标签

`推荐系统` · 领域:学习与行业

## 证据(README 行号)

> L17: Under the hood, BookSage AI is a decoupled system — a **FastAPI** JSON API served independently from a **React 19**
> L38: |**Recommendation Models**|**Hybrid System**: Collaborative Filtering + Content-Based Filtering|
> L42: |**Data Sources**|Book-Crossing Dataset (`BX-Books`, `BX-Users`, `BX-Ratings`)|

## 星数曲线

```mermaid
xychart-beta
    title "Md-Emon-Hasan/BookSage-AI 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-28 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `38c22ef8ee63` · [字段定义](../../DATASET.md)*
