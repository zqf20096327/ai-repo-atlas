# mburaksayici/smallevals

⭐ 23 · Python · 推送 2025-12-04 · [GitHub](https://github.com/mburaksayici/smallevals) · 个人维护

**本地小模型驱动的 RAG 检索评测框架，0.6B 模型免 API**

面向 RAG 系统的离线检索评测框架：核心是自训练的 QAG-0.6B 小模型，从文档块生成问答对作为合成评测数据，再通过向量库查询验证能否检索回原块，以此计算检索质量分数。全程本地运行于 CPU/GPU/MPS，不调用外部 LLM API。支持连接 Milvus、Elasticsearch、PGVector、Chroma、Pinecone、Qdrant、Weaviate、FAISS 等向量库，自带可视化仪表盘与 QA 生成 CLI。其余评测模型（CRC/GJ/ASM）标注为 Incoming，属未来工作；模型存在偏向结构化文本、问题偏泛等已知问题。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- QAG-0.6B 模型从 chunk 生成合成问答评测数据
- 100% 本地运行于 CPU/GPU/MPS，无需外部 LLM API
- 支持 8 种向量库连接（Milvus/Chroma/Qdrant/FAISS 等）
- 提供可视化仪表盘（smallevals dash）与 QA 生成 CLI

## 适用场景

- 为已接入向量库的 RAG 系统验证检索管线是否命中正确文档
- 批量从文档生成合成问答评测数据集
- 零 API 成本地在本地跑检索质量评分并可视化

## 场景标签

`模型评测` `RAG` · 领域:评测与运维

## 证据(README 行号)

> L5: A lightweight evaluation framework powered by tiny ( really tiny logo ) 0.6B models — runs 100% locally on CPU/GPU/M
> L11: Evaluation of RAG system includes retrieval and RAG stage, logo attacks to test retrieval and RAG answers(in the ne
> L34: Connect to your favourite Vector DB (Milvus, Elastic, PGVector, Chroma, Pinecone, FAISS, Weawiate), attach your fav

## 星数曲线

```mermaid
xychart-beta
    title "mburaksayici/smallevals 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-28 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `9bdd623670ed` · [字段定义](../../DATASET.md)*
