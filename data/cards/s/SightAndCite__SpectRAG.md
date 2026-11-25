# SightAndCite/SpectRAG

⭐ 51 · Python · MIT · 推送 2026-11-04 · [GitHub](https://github.com/SightAndCite/SpectRAG) · [官网](https://sightandcite.github.io/SpectRAG/) · 组织维护

**给 RAG 开发者：谱图增强的检索框架，提升多跳问答上下文选择**

研究状态（status: research）的检索框架，官方实现于密集向量检索之上叠加加权块图与拉普拉斯谱结构：离线索引构建块图，查询时经图扩展、谱扩散与簇感知选择，在 token 预算内选出相关、非冗余且结构连通的上下文集，再由 LLM 生成回答。栈含 Ollama 本地嵌入、FAISS、BM25 混合检索、Neo4j 图存储、FastAPI 后端与 React+D3 前端。默认索引用 OpenAI gpt-4o-mini，可切换为全本地（NER + Ollama）。提供 CLI 索引与查询，需 Python 3.11、本地 Ollama、Docker 与 Node.js 18+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 加权块图 + 拉普拉斯谱结构的离线索引
- 查询时图扩展、谱扩散（½spectral+½PPR）与 token 预算内的簇感知选择（默认 12000）
- 密集（FAISS）与 BM25 词法混合检索，RRF 融合
- 支持全本地模式（spaCy NER + Ollama），无需 API key

## 适用场景

- 多跳问答场景下选出相关且非冗余的上下文集
- 为 RAG 系统替换 top-k 相似度检索为图增强检索
- 本地（无 API key）搭建带前端界面的检索问答系统

## 场景标签

`RAG` · 领域:知识与检索

## 证据(README 行号)

> L9: Official implementation of **SpectRAG**, a retrieval framework that improves context selection in RAG systems by aug
> L11: Instead of retrieving only the top-ranked chunks by semantic similarity, SpectRAG selects a context set that is joi

## 星数曲线

```mermaid
xychart-beta
    title "SightAndCite/SpectRAG 星数(近 3 点)"
    x-axis ["2026-11-08", "2026-11-10", "2026-11-25"]
    y-axis "stars" 49 --> 52
    line [50, 51, 51]
```

2026-11-08 50 → 2026-11-25 51（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-18 · 置信度 mid · 依据 README sha `1b74fbe8edc3` · [字段定义](../../DATASET.md)*
