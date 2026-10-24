# wmaslonek/guardian-db

⭐ 215 · Rust · Apache-2.0 · 推送 2026-08-04 · [GitHub](https://github.com/wmaslonek/guardian-db) · [官网](https://www.willsearch.com.br) · 个人维护

**基于 Rust 与 Iroh 的本地优先 P2P 去中心化数据库**

用 Rust 编写的本地优先、点对点同步的数据库库：每个节点持有完整本地副本，读写不经服务器，通过 Iroh（QUIC、Willow 差量同步、gossip）在节点间自动收敛。提供 KeyValue/文档/事件日志三种存储，支持 PostgreSQL 线协议兼容层（psql、TypeORM、DBeaver 可直连）、Supabase 兼容网关、pgvector 兼容向量检索与 RAG、WebAssembly 计算委托（含 Edge AI 与 LLM 推理）及可选 TypeORM/Mongoose 风格 ODM。面向需要在离线优先与 P2P 场景下存储和处理数据的开发者，通过 cargo 以 crate 或源码方式集成。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 本地优先 P2P：全量本地副本、读写本地化、Iroh Willow 差量同步
- PostgreSQL 线协议兼容层，psql/TypeORM/DBeaver 直连
- pgvector 兼容 HNSW 向量检索、自动嵌入与 RAG
- Guardian Compute 将 WebAssembly 任务（含 Edge AI、LLM 推理）委托给节点

## 适用场景

- 构建离线优先、无服务器依赖的多端数据同步应用
- 用现有 PostgreSQL 客户端连接去中心化数据库运行 SQL
- 在数据所在位置就近做向量检索与 RAG

## 场景标签

 · 领域:分布式数据库/边缘计算

## 证据(README 行号)

> L16: GuardianDB is a decentralized, local-first database for apps that need peer-to-peer
> L28: - **Vector search & RAG:** pgvector-compatible HNSW index, auto-embedding, and retrieve-augment-generate right besi
> L29: - **Guardian Compute:** delegate WebAssembly tasks to the most capable peer: capacity-aware scheduling, Edge AI, an

## 星数曲线

```mermaid
xychart-beta
    title "wmaslonek/guardian-db 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-24"]
    y-axis "stars" 213 --> 216
    line [214, 215, 215]
```

2026-10-18 214 → 2026-10-24 215（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `da7bb20e3e38` · [字段定义](../../DATASET.md)*
