# HarinezumIgel/RAG-LCC

⭐ 34 · Python · MIT · 推送 2026-10-12 · [GitHub](https://github.com/HarinezumIgel/RAG-LCC) · 个人维护

**本地实验性 RAG 实验场：调试检索质量与上下文组装**

面向研究者和工程师的实验性 RAG 系统，用于研究 RAG 流水线为何失败：由 DocClassify（文档分类与元数据生成）、RAGLoad（四路并行索引：ChromaDB 向量、BM25、实体共现图、Regex 动词/名词索引）、RAGChat（多轮对话 CLI，含合规过滤、翻译、查询改写、混合检索、重排、策略门控上下文组装）与 RAGChatService（OpenAI 兼容 REST API，可接入 Open WebUI）四个应用组成。每轮输出置信度指标（C_top、C_coverage 等）供调参。作者声明其为洞察工具而非日常生产级 RAG。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 四路混合检索：向量 + BM25 + 实体图 + Regex，经加权 RRF 融合
- 多算法合规过滤链（Regex+Levenshtein、Jaccard、BM25、KeyBERT）于存储与生成前后各运行一次
- 逐句答案溯源（grounding）与每轮置信度指标输出
- OpenAI 兼容 API 与 Open WebUI 集成，检索参数暴露为 Advanced Parameters

## 适用场景

- 在小语料上试验并比较 RAG 检索与分块参数，带回自己的系统
- 调试多轮对话中的上下文组装失败与语料冲突问题
- 通过 Open WebUI 使用本地 RAG 管线并可视化答案溯源

## 场景标签

`RAG` `科研工具` · 领域:知识与检索

## 证据(README 行号)

> L16: **RAG‑LCC is an experimental Retrieval‑Augmented Generation (RAG) lab focused on understanding and controlling retr
> L40: Short: If you want to understand *why* your RAG fails, RAG-LCC gives you a playground to experiment with the parame
> L48: The system is built around four applications that form a deliberate pipeline:

## 星数曲线

```mermaid
xychart-beta
    title "HarinezumIgel/RAG-LCC 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-26"]
    y-axis "stars" 32 --> 35
    line [33, 34, 34]
```

2026-10-18 33 → 2026-10-26 34（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `9e6b2733e763` · [字段定义](../../DATASET.md)*
