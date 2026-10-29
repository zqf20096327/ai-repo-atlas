# bicardinal/brinicle

⭐ 102 · Python · Apache-2.0 · 推送 2026-09-30 · [GitHub](https://github.com/bicardinal/brinicle) · [官网](https://brinicle.bicardinal.com) · 组织维护

**低内存场景的 C++ 磁盘优先 HNSW 向量/混合检索引擎**

brinicle 是以磁盘优先 HNSW 索引为核心的检索引擎，提供 Python API 与三个引擎：VectorEngine（向量 ANN 检索）、ItemSearchEngine（词法/语义/混合条目检索，alpha 参数控制权重）、AutocompleteEngine（查询建议）。C++ 核心，支持流式逐条摄入、插入/更新/删除、紧凑重建与图优化，索引驻留磁盘以降低内存占用。README 给出多组公开基准（与 FAISS、hnswlib、Qdrant 等对比），经 pip 安装或源码构建。限制：autocomplete 目前对前缀对齐的建议效果最佳。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 磁盘优先 HNSW 设计，低 RAM 索引与查询
- 单一 HNSW 图同时承载词法与语义信号（alpha 可调）
- 三引擎统一生命周期：init/ingest/finalize/search
- 流式逐条摄入，全量数据无需载入内存

## 适用场景

- 在低内存容器中构建向量或混合商品检索
- 为商品目录做带结构化字段的混合搜索
- 低资源环境下的查询自动补全/建议

## 场景标签

`向量数据库` `语义搜索` · 领域:知识与检索

## 证据(README 行号)

> L12: brinicle is a disk-first HNSW retrieval engine for vector search, structured item search, hybrid search, and autoco
> L13: It gives you a simple Python API for building search over embeddings, product catalogs, structured records, and que
> L106: * Disk-first HNSW search

## 星数曲线

```mermaid
xychart-beta
    title "bicardinal/brinicle 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 101 --> 103
    line [102, 102]
```

2026-10-18 102 → 2026-10-29 102（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `a89ca8ffd9c5` · [字段定义](../../DATASET.md)*
