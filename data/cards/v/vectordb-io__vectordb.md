# vectordb-io/vectordb

⭐ 48 · Rust · MIT · 推送 2026-10-27 · [GitHub](https://github.com/vectordb-io/vectordb) · [官网](https://vectordb.io/) · 组织维护

**Rust 编写的独立向量数据库，支持语义搜索与 RAG 存储**

以 Rust 实现的独立向量数据库：提供可嵌入引擎、HTTP 服务与命令行，持久化基于嵌入式 SQLite（WAL、事务、崩溃恢复、快照备份）。支持多库/集合/分区、多种向量类型与 COSINE/IP/L2/HAMMING/JACCARD 距离、FLAT/IVF_FLAT/HNSW 索引、标量预过滤与多向量 RRF/加权融合排序。不自动生成嵌入，应用需自行提交向量。处于 0.1.0 Alpha，明确不是 Milvus 的直接替代品；另含 Python 嵌入包（未发布到 PyPI，本地构建）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- SQLite WAL 持久化：事务、崩溃恢复、快照备份、JSONL 导入导出
- FLAT/IVF_FLAT/HNSW 索引与标量预过滤、范围/分组/多向量搜索
- 可嵌入形态：Rust crate、本地构建的 Python 包（vectordb_io）、HTTP 服务
- Bearer 认证、并发队列限制、Prometheus 指标、优雅停机

## 适用场景

- 为 RAG 应用提供带元数据过滤的向量存储与检索
- 在 Python 或 Rust 进程内嵌入使用向量数据库
- 需要单机事务性与崩溃恢复的语义搜索服务

## 场景标签

`向量数据库` · 领域:知识与检索

## 证据(README 行号)

> L5: A standalone vector database reimplemented in Rust, with an embeddable engine, an HTTP service, transactional persis
> L38: Embeddings are not generated automatically; applications must generate and submit vectors. The database logic, filt


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `b408c38f1551` · [字段定义](../../DATASET.md)*
