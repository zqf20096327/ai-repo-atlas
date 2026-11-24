# datastax/jvector

⭐ 1,759 · Java · Apache-2.0 · 推送 2026-11-24 · [GitHub](https://github.com/datastax/jvector) · [官网](https://datastax.github.io/jvector/) · 组织维护

**Java 嵌入式向量近似最近邻检索库**

JVector 是一个 Java 编写的近似最近邻（ANN）向量检索库，构建结合 HNSW 层级与 Vamana 算法的图索引，支持并发与增量构建、从磁盘读取压缩向量检索。检索采用两遍设计：先用量化编码（PQ/ASH/BQ）遍历图，再用全精度或 NVQ 向量重排序。支持 DOT_PRODUCT、EUCLIDEAN、COSINE 相似度，发布于 Maven Central，提供示例程序与教程；构建需 JDK 22+ 与 Maven，运行支持 Java 11+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- HNSW 层级 + Vamana 图索引，支持并发与流式增量构建
- 多种量化器：PQ、实验性 ASH、BQ 遍历编码与 NVQ 重排序
- fused 索引将邻居编码随图存储，支持大于内存的索引服务
- 原生 SIMD 加速（Java 22+ Panama/oneDNN），可选 MKL/OpenBLAS

## 适用场景

- 在 Java 应用中嵌入向量相似度检索
- 为 RAG/推荐系统构建大规模向量索引
- 用压缩量化在有限内存中服务超大规模向量集

## 场景标签

`向量数据库` · 领域:知识与检索

## 证据(README 行号)

> L3: JVector is a Java library for approximate nearest neighbor (ANN) vector search. It builds graph
> L91: Run with these JVM options to enable SIMD acceleration (see
> L232: - **Queued, batched queries.** `QueryPreparer` and `BatchingExecutor` project many queries at once

## 星数曲线

```mermaid
xychart-beta
    title "datastax/jvector 星数(近 9 点)"
    x-axis ["2026-10-22", "2026-10-25", "2026-10-28", "2026-10-29", "2026-11-11", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-24"]
    y-axis "stars" 1754 --> 1761
    line [1755, 1757, 1756, 1757, 1758, 1759, 1760, 1759, 1759]
```

2026-10-22 1,755 → 2026-11-24 1,759（+4）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-23 · 置信度 high · 依据 README sha `0aef56c3154e` · [字段定义](../../DATASET.md)*
