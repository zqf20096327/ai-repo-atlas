# ani03sha/distributed-rag-system

⭐ 21 · Python · MIT · 推送 2026-07-18 · [GitHub](https://github.com/ani03sha/distributed-rag-system) · 个人维护

**面向工程团队的生产级分布式 RAG 参考实现平台**

基于分布式系统原则构建的生产级 RAG 平台，定位为工程团队在生产环境运行 RAG 的参考实现。功能：从可插拔数据源（默认 Wikipedia）摄取文档，经 Redpanda 事件驱动管线分块、嵌入并存入 Qdrant，通过混合检索（稠密+BM25 稀疏、RRF 融合、FlashRank 重排）与本地 LLM 生成回答。采用六边形架构，各组件可替换适配器；内置两层语义缓存、JWT 认证、RAGAS 评测与完整可观测性。服务均为无状态可独立扩展，需 Docker 与 Ollama 运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 事件驱动摄取管线（Redpanda），摄取不阻塞查询服务
- 混合检索：稠密+BM25 稀疏向量、RRF 融合、FlashRank 本地重排
- 两层语义缓存：Redis 精确缓存 + Qdrant 余弦相似度语义缓存
- 六边形架构，向量库/LLM 通过适配器可替换（Qdrant↔pgvector、Ollama↔OpenAI）

## 适用场景

- 工程团队参考其架构在生产环境运行 RAG
- 学习事件驱动摄取与无状态服务水平扩展的落地方式
- 替换适配器后接入自有向量库或 LLM 提供商

## 场景标签

`RAG` · 领域:知识与检索

## 证据(README 行号)

> L3: > A production-grade Retrieval Augmented Generation (RAG) platform built on distributed systems principles.
> L4: > Designed as a reference implementation for engineering teams who want to run RAG in production.
> L13: - **No framework lock-in** — core logic sits behind interfaces; swapping Qdrant for pgvector or Ollama for OpenAI r

## 星数曲线

```mermaid
xychart-beta
    title "ani03sha/distributed-rag-system 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-28 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `9a502977d579` · [字段定义](../../DATASET.md)*
