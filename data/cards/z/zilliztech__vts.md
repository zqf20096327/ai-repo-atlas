# zilliztech/vts

⭐ 134 · Java · Apache-2.0 · 推送 2026-10-26 · [GitHub](https://github.com/zilliztech/vts) · [官网](https://zilliz.com/) · 组织维护

**向量与非结构化数据迁移工具：把各类数据源接入 Milvus**

Zilliz 基于 Apache SeaTunnel 开发的开源数据迁移工具，用于在各向量数据库、Elasticsearch、Solr、关系型数据库、数据仓库、文档数据库、S3 等数据源与 Milvus 之间搬运向量与非结构化数据。提供流式与批式统一处理、schema 匹配、基本数据校验、实时监控与告警；配合 Zilliz Cloud Pipelines 可做 embedding 等转换。以 Docker 镜像分发，通过配置文件声明 source/sink 连接器运行任务。前置要求包括 Docker、Milvus 2.3.6 以上版本。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 支持 Milvus/Elasticsearch/Pinecone/Qdrant/Weaviate 等 8 类连接器
- 流批一体的实时同步与离线批量导入
- schema 匹配与基本数据校验、监控告警机制
- 基于 Apache SeaTunnel，支持分布式集群模式运行

## 适用场景

- 把 Elasticsearch、Pinecone 等既有数据迁移到 Milvus 集群
- 向向量数据库做实时数据流同步或离线批量导入
- 迁移过程中校验数据一致性与质量

## 场景标签

 · 领域:向量数据库/数据集成基础设施

## 证据(README 行号)

> L9: **VTS** (Vector Transport Service) is an open-source tool for moving vectors and unstructured data. It is developed 
> L16: 3. **Simplifying Unstructured Data Transformation:** Unlike traditional ETL, transforming unstructured data require

## 星数曲线

```mermaid
xychart-beta
    title "zilliztech/vts 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 133 --> 135
    line [134, 134]
```

2026-10-18 134 → 2026-10-27 134（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `803e355abcb9` · [字段定义](../../DATASET.md)*
