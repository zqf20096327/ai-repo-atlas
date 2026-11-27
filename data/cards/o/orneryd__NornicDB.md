# orneryd/NornicDB

⭐ 935 · Go · MIT · 推送 2026-11-26 · [GitHub](https://github.com/orneryd/NornicDB) · 个人维护

**面向 AI 应用的 Neo4j 兼容图+向量数据库**

用 Go 编写的分布式图数据库，在单一存储中组合 Cypher 查询、图遍历、向量检索（HNSW）与基于 MVCC 的历史读。提供 Bolt 与 HTTP 接口，可嵌入 Go 应用；声称兼容 Neo4j Bolt/Cypher 与 qdrant gRPC，便于迁移切换。附带 schema、托管 embedding、重排序+LLM、GPU 加速等特性，并提供 MCP server 与 agent 集成。分发渠道包括 Docker 镜像（CPU/CUDA/Vulkan 变体）、Homebrew、macOS 安装包与源码构建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Cypher 查询、图遍历、向量检索与 MVCC 历史读合一
- Neo4j Bolt/Cypher 与 qdrant gRPC 兼容，可切换迁移
- 多架构支持：CPU、CUDA、Metal、Vulkan
- 提供 MCP server 与 agent 集成，支持嵌入 Go 应用

## 适用场景

- 为 GraphRAG 或 agent 记忆场景提供图+向量混合检索
- 从 Neo4j 或 qdrant 迁移而不改查询代码
- 需要读取历史状态版本的应用

## 场景标签

`向量数据库` `知识图谱` `RAG` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L65: NornicDB is a graph database that combines Cypher queries, graph traversal, vector search, and historical reads. It
> L83: - Vector search, memory policies, and agent integration.
> L6:  Neo4j-compatible • Hybrid graph + vector retrieval • Historical reads via MVCC

## 星数曲线

```mermaid
xychart-beta
    title "orneryd/NornicDB 星数(近 16 点)"
    x-axis ["2026-10-25", "2026-10-27", "2026-10-28", "2026-10-29", "2026-11-01", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-18", "2026-11-21", "2026-11-23", "2026-11-25", "2026-11-26", "2026-11-27"]
    y-axis "stars" 914 --> 938
    line [916, 918, 919, 920, 921, 916, 924, 928, 930, 931, 932, 933, 935, 936, 935, 935]
```

2026-10-25 916 → 2026-11-27 935（+19）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `56df81983c64` · [字段定义](../../DATASET.md)*
