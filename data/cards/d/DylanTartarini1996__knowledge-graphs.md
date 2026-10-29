# DylanTartarini1996/knowledge-graphs

⭐ 34 · Python · GPL-3.0 · 推送 2025-12-23 · [GitHub](https://github.com/DylanTartarini1996/knowledge-graphs) · 个人维护

**基于生成式 AI 构建与查询知识图谱的 GraphRAG 实验仓库**

个人实验性仓库，提供从文档构建知识图谱的完整管线：加载/清洗/分块/嵌入，用 LLM agent（GraphExtractor）抽取概念图，可选 OntologyExplorer 推断领域本体，上传至 Neo4j（同时作为向量库与图数据库），并更新中心性与社区划分。查询侧由 GraphAgentResponder 提供 5 种检索策略（Cypher、vanilla RAG、社区报告、社区子图、混合）。附带 Streamlit 演示应用与 Docker 构建。LLM/嵌入支持 Ollama、OpenAI/Azure、Groq、Gemini、Hugging Face。README 自述为 work in progress，Streamlit 应用仅作演示用途。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 文档→分块→嵌入→LLM 抽取图谱→Neo4j 入库的构建管线
- GraphExtractor/OntologyExplorer/GraphAgentResponder 多个 agent
- 5 种图检索策略（Cypher/上下文 RAG/社区报告/社区子图/混合）
- 提供 Docker 镜像（含 Neo4j+APOC+GDS、Ollama 容器）

## 适用场景

- 搭建 GraphRAG 原型，对比向量检索与图检索效果
- 从 PDF/DOCX/TXT/HTML 文档自动抽取知识图谱
- 以对话方式查询知识图谱并选择检索策略

## 场景标签

`知识图谱` `RAG` · 领域:知识与检索

## 证据(README 行号)

> L6: This is a work in progress repository where I collect my experiments on building software for RAG applications based

## 星数曲线

```mermaid
xychart-beta
    title "DylanTartarini1996/knowledge-graphs 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 33 --> 35
    line [34, 34]
```

2026-10-18 34 → 2026-10-29 34（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `abc93da7d469` · [字段定义](../../DATASET.md)*
