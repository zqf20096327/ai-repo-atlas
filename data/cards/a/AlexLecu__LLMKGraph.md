# AlexLecu/LLMKGraph

⭐ 37 · Python · MIT · 推送 2026-10-23 · [GitHub](https://github.com/AlexLecu/LLMKGraph) · [官网](https://llmkgraph.utcluj.ro) · 个人维护

**AMD 医学文献知识图谱构建与 Graph-RAG 问答系统（论文官方代码）**

IEEE Access 2025 论文的官方实现：用 LLM（GPT-3.5/GPT-4o-mini/Mistral/DeepSeek）从 5,000 篇 AMD 摘要与 100 项临床试验中抽取 12 类实体、8 类关系，存入 GraphDB（RDF，CausalAMD 本体，HermiT 推理），再经 Weaviate BM25 检索子图供 LLM 生成带出处的回答。含 Vue 3 前端（图谱浏览、聊天、LLM 对比）、Flask API 与 3,000 题评测（RAGAS/Giskard）。Docker Compose 部署，聊天默认本地 Ollama 或任意 OpenAI 兼容 API。限制：完整 5,000 篇语料不再分发，仅含 100 篇样例。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- LLM 抽取 12 实体类型/8 关系类型，每条关系经 prov:wasDerivedFrom 链接来源文献
- Graph-RAG 聊天：spaCy 分析问题 + Weaviate BM25 实体检索子图作为生成上下文
- 3,000 题评测基准（含/无图谱上下文对照），RAGAS 忠实度 0.85–0.97
- 不同 LLM 构建的图谱可做结构对比（规模、度分布、三元组一致性）

## 适用场景

- 眼科/AMD 研究者查询有文献出处的医学知识问答
- 复现论文中知识图谱增强降低幻觉的评测结果
- 作为生物医学 Graph-RAG 系统的实现参考进行二次开发

## 场景标签

`知识图谱` `RAG` `科研工具` · 领域:知识与检索

## 证据(README 行号)

> L13: **Official code for the paper** "Reducing Hallucinations in Medical AI: A Knowledge Graph-Augmented Retrieval Syste
> L23: LLMKGraph turns the biomedical literature on **Age-related Macular Degeneration (AMD)** into a causal knowledge gra
> L64: |💬 **Graph-RAG Chatbot**|spaCy query analysis, Weaviate BM25 entity search, pairwise and per-entity relation retrie

## 星数曲线

```mermaid
xychart-beta
    title "AlexLecu/LLMKGraph 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 36 --> 38
    line [37, 37]
```

2026-10-18 37 → 2026-10-29 37（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `abdea0f0357b` · [字段定义](../../DATASET.md)*
