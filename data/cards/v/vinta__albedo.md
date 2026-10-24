# vinta/albedo

⭐ 190 · Scala · MIT · 推送 2025-12-18 · [GitHub](https://github.com/vinta/albedo) · 个人维护 · 中文 README

**用 Apache Spark 构建的 GitHub 仓库推荐系统**

个人项目，基于 Apache Spark（Scala）与 Elasticsearch 实现 GitHub 仓库发现推荐系统。流程包括：用 GitHub Personal Token 采集数据，构建用户与仓库画像做特征工程，训练 ALS 模型与基于 Elasticsearch More Like This 的内容推荐做候选生成，Word2Vec 做文本向量化，逻辑回归做排序，并以 NDCG@30 报告各模型效果。通过 git clone 与 make 命令配合 Docker 容器运行本地 Spark Standalone 集群，也支持在 Google Cloud Dataproc 上建集群。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- ALS 与基于 Elasticsearch 的内容推荐双路候选生成
- 用户/仓库画像特征工程与 Word2Vec 文本向量化
- 逻辑回归排序，各阶段以 NDCG@30 报告指标
- make 命令驱动容器化环境与本地 Spark Standalone 集群

## 适用场景

- 学习如何用 Spark 搭建多路召回加排序的推荐系统
- 获取 GitHub 仓库个性化发现/推荐的参考实现
- 复现 ALS、内容推荐、逻辑回归排序的离线评测流程

## 场景标签

 · 领域:机器学习/推荐系统

## 证据(README 行号)

> L3: A recommender system for discovering GitHub repos, built with Apache Spark.
> L72: ## Train an ALS Model for Candidate Generation
> L116: ## Train a Logistic Regression Model for Ranking

## 星数曲线

```mermaid
xychart-beta
    title "vinta/albedo 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 189 --> 191
    line [190, 190]
```

2026-10-18 190 → 2026-10-24 190（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `532d401bf0f7` · [字段定义](../../DATASET.md)*
