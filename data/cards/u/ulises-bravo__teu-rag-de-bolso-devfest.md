# ulises-bravo/teu-rag-de-bolso-devfest

⭐ 3 · JavaScript · 推送 2026-10-31 · [GitHub](https://github.com/ulises-bravo/teu-rag-de-bolso-devfest) · [官网](https://ulisesbravo.labsapp.com.br/materiais) · 个人维护

**DevFest workshop: build a local RAG in pure Node.js with no database**

Portuguese-language workshop material (DevFest Porto Alegre) teaching attendees to build a minimal HTTP server in Node.js that performs semantic retrieval over an FAQ, with v2 delivering the retrieved document to an LLM that answers as a salesperson persona. Uses pure Node without database, paid API, or framework: embedding runs locally on CPU via transformers.js (Xenova/multilingual-e5-small, 4-bit quantized). README is primarily prerequisite setup (Node.js 18+, Ollama pre-install, ~3.5 GB downloads) plus v1 running instructions, test questions, troubleshooting, and exercises.

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- ~100-line HTTP server, no database, no framework, embeddings on local CPU
- v1 semantic retrieval / v2 generation via local Ollama (qwen2.5:3b)
- Embedding model pre-download script with curl resumable download
- Exercises covering indexing, ranking, normalization, and threshold rejection

## 适用场景

- Workshop hands-on learning to build a minimal RAG from scratch
- Understanding semantic retrieval and embedding vectors with local resources
- Creating a local CPU-based FAQ search service without any paid API

## 场景标签

`RAG` `教程课程` · 领域:知识与检索

## 证据(README 行号)

> L1: # Teu RAG de bolso — DevFest
> L7: RAG = *Retrieval-Augmented Generation*. São duas metades, e o workshop

## 星数曲线

```mermaid
xychart-beta
    title "ulises-bravo/teu-rag-de-bolso-devfest 星数(近 2 点)"
    x-axis ["2026-11-21", "2026-11-24"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-11-21 3 → 2026-11-24 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `f0195de2cc04` · [字段定义](../../DATASET.md)*
