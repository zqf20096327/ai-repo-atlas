# flamehaven01/Flamehaven-Filesearch

⭐ 109 · Python · MIT · 推送 2026-05-19 · [GitHub](https://github.com/flamehaven01/Flamehaven-Filesearch) · [官网](https://flamehaven.space/work/flamehaven-filesearch/) · 个人维护

**自托管的 RAG 文档搜索引擎：34 种格式混合检索**

基于 FastAPI 的自托管 RAG 搜索引擎：解析 34 种文件格式（PDF/DOCX/XLSX/PPTX/Markdown/Obsidian vault 等），提供关键词、语义与 BM25+RRF 混合检索，含 PASS/FORGE/INHIBIT 质量门控与自适应 BM25 池。支持 Gemini（默认）、OpenAI、Claude、Ollama 及 OpenAI 兼容端点作为 LLM 后端，单个环境变量切换；嵌入可用自研 DSP（无 ML 依赖）或 Ollama。提供 Docker 部署、Python SDK、REST API，出处的溯源指向源文档与分块；附 LangChain/LlamaIndex/Haystack/CrewAI 适配器、OAuth2/OIDC 认证与管理面板。

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

- 34 种文件格式解析与结构感知分块、KnowledgeAtom 两级索引
- 关键词/语义/BM25+RRF 混合检索，带 PASS/FORGE/INHIBIT 置信度质量门控
- 四种 LLM 后端（Gemini/OpenAI/Claude/Ollama）环境变量切换
- LangChain/LlamaIndex/Haystack/CrewAI 框架适配器与 API key/OAuth2/OIDC 认证

## 适用场景

- 把敏感文档留在本机做私有 RAG 搜索，不依赖第三方服务
- 给已有应用通过 Python SDK 或 REST API 接入文档问答检索
- 对 Obsidian Markdown 库做保留结构（wikilink/frontmatter）的检索

## 场景标签

`RAG` `文档解析` `语义搜索` · 领域:知识与检索

## 证据(README 行号)

> L5: ### Self-hosted RAG search engine. Production-ready in 3 minutes.
> L20: Stop sending your sensitive documents to third-party services. FLAMEHAVEN FileSearch is a production-grade RAG sear
> L50: |**Search Modes**|Keyword, semantic, and hybrid (BM25+RRF) with automatic typo correction|

## 星数曲线

```mermaid
xychart-beta
    title "flamehaven01/Flamehaven-Filesearch 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 108 --> 110
    line [109, 109]
```

2026-10-18 109 → 2026-10-23 109（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `b4aaa4207a69` · [字段定义](../../DATASET.md)*
