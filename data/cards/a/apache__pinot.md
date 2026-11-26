# apache/pinot

⭐ 6,177 · Java · Apache-2.0 · 推送 2026-11-25 · [GitHub](https://github.com/apache/pinot) · [官网](https://pinot.apache.org/) · 组织维护

**面向实时低延迟 SQL 分析与向量检索的分布式 OLAP 数据库**

Apache Pinot 是一个实时分布式 OLAP 数据存储，从 Kafka、Pulsar、Kinesis 等流源和 HDFS/S3 等批源摄取数据，提供毫秒级 P90 延迟的 SQL 查询与 REST API。内置多租户、可插拔索引（倒排、StarTree、JSON、地理空间等）与实时摄取 Upsert，可通过 Helm Chart 在 Kubernetes 上部署。同时支持向量相似度检索，可用于语义搜索、推荐与 RAG 场景；由 LinkedIn 与 Uber 的工程师创建，现为 Apache 项目。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 流批双源摄取，支持 Kafka/Pulsar/Kinesis 与 Hadoop/Spark/S3
- 低延迟 SQL 查询接口，内置查询编辑器与 REST API
- 向量相似度检索，覆盖语义搜索、推荐与 RAG 用例
- Helm Chart 支持 Kubernetes 云原生部署

## 适用场景

- 为面向用户的应用提供毫秒级实时分析与交互式查询
- 承载 AI 助手与自动化决策系统的低延迟数据查询
- 为语义搜索和 RAG 应用提供向量检索
- 在 Kubernetes 上部署水平扩展的实时分析集群

## 场景标签

`向量数据库` · 领域:知识与检索

## 证据(README 行号)

> L18: Apache Pinot is a real-time distributed OLAP datastore, built to deliver scalable real-time analytics with low late
> L20: Pinot also supports vector similarity search for vector database use cases such as semantic search, recommendations

## 星数曲线

```mermaid
xychart-beta
    title "apache/pinot 星数(近 6 点)"
    x-axis ["2026-11-08", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-20", "2026-11-26"]
    y-axis "stars" 6170 --> 6179
    line [6171, 6175, 6176, 6177, 6178, 6177]
```

2026-11-08 6,171 → 2026-11-26 6,177（+6）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `1e25894f2579` · [字段定义](../../DATASET.md)*
