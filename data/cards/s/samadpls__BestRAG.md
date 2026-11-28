# samadpls/BestRAG

⭐ 21 · Rust · MIT · 推送 2026-11-27 · [GitHub](https://github.com/samadpls/BestRAG) · [官网](https://bestrag.samadpls.com) · 个人维护

**在 Postgres/Qdrant 上做混合检索的 RAG Python 库**

Python 库（3.10+，MIT），在已有 Postgres+pgvector 或 Qdrant 上实现稠密向量与 BM25 的混合检索并融合排序，可选交叉编码器重排（默认关闭）。默认在本机运行小型嵌入模型，也可接入 OpenAI、Cohere、Gemini 等嵌入提供商；PDF 按阅读顺序解析并保留页码，同名重建索引会替换旧版本。附 BEIR SciFact 评测数字、Hugging Face Spaces 在线试用与 llms.txt 文档。

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

- 稠密向量与 BM25 混合检索并融合结果，单次查询毫秒级且默认无 API 调用
- 内置本地嵌入模型，可切换 OpenAI/Cohere/Gemini/Voyage/Mistral/Bedrock/Ollama 等提供商
- PDF 按阅读顺序解析（含 RTL 文字），结果保留页码
- 可选 cross-encoder 重排与 BEIR SciFact 评测数字

## 适用场景

- 在已运行的 Postgres/Qdrant 上搭建检索增强问答
- 检索含型号、编号等专有名词（如 XJ-9042）的文档
- 为多语言或 RTL 文档建立带页码的 PDF 索引

## 场景标签

`RAG` `文档解析` · 领域:知识与检索

## 证据(README 行号)

> L13:  BestRAG finds passages by meaning and by exact words, then merges the two lists. Use default local models or your 
> L18: - **Finds exact words too.** BM25 finds names and codes like `XJ-9042`, even when search by meaning misses them.
> L19: - **Your own embeddings, or the built-in local model.** Use OpenAI, Cohere, Gemini and more with no model download.


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 mid · 依据 README sha `856397df6aaf` · [字段定义](../../DATASET.md)*
