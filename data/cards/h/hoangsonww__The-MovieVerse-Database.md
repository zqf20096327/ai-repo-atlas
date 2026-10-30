# hoangsonww/The-MovieVerse-Database

⭐ 34 · JavaScript · NOASSERTION · 推送 2026-09-27 · [GitHub](https://github.com/hoangsonww/The-MovieVerse-Database) · [官网](https://movie-verse.com) · 个人维护

**面向影迷的开源电影数据库与推荐 Web 平台**

由 Son Nguyen 维护的全栈、移动友好的电影信息平台：支持按标题/演员/导演/类型搜索，浏览详情、评分、写评论、管理观影清单，并提供 AI 驱动的推荐与 ML 统计、MovieBot 聊天机器人。后端为 Django 网关 + FastAPI 微服务，含 MLflow 模型注册、Feast 特征存储、Kafka/RabbitMQ 事件、Docker Compose/Kubernetes/AWS 部署资产。注意：本仓库非生产代码库，仅供教育展示，可在本地运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 电影搜索、详情、评分评论与观影清单
- AI 驱动推荐与 ML 统计（LightFM、SentenceTransformers + FAISS）
- 微服务架构：Django 网关 + FastAPI 服务 + Kafka/RabbitMQ
- 提供 Docker Compose、Kubernetes、AWS CloudFormation 部署资产

## 适用场景

- 查找电影信息、写评论并管理观影清单
- 获取基于个人偏好的 AI 电影推荐
- 作为参考学习微服务与 AI 平台的部署实践

## 场景标签

`聊天机器人` `推荐系统` · 领域:对话与助手

## 证据(README 行号)

> L15: The MovieVerse is an open-source, full-stack, and mobile-friendly application created with the vision of creating a
> L101: - **Movie Recommendations**: Receive suggestions based on your movie preferences and reviews with AI-powered recom
> L153: - **AI API**: inference endpoints for recommendations, similarity, ranking, sentiment, summarization, and vision.

## 星数曲线

```mermaid
xychart-beta
    title "hoangsonww/The-MovieVerse-Database 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 33 --> 35
    line [34, 34]
```

2026-10-18 34 → 2026-10-30 34（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `8d50319fd7a6` · [字段定义](../../DATASET.md)*
