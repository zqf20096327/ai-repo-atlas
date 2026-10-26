# mzarnecki/php-rag

⭐ 67 · PHP · MIT · 推送 2026-07-19 · [GitHub](https://github.com/mzarnecki/php-rag) · [官网](https://medium.com/@michalzarnecki88/a-guide-to-using-llm-retrieval-augmented-generation-with-php-3bff25ce6616) · 个人维护

**PHP 实现的 RAG 问答应用：多模型检索文档生成回答**

用 PHP 编写的检索增强生成（RAG）应用：用户输入经向量检索从 pgvector 数据库（1000+ 网站文档）召回相关片段，再由 LLM 生成回答，支持 GPT、Claude、DeepSeek、Gemini、Llama3.2、Mixtral、Bielik 等云 API 模型，以及经 Ollama 本地服务的模型。提供 Web 界面、API 端点与 CLI 三种访问方式，Docker Compose 部署，内置 ROUGE/BLEU 与基于 GPT-5 的多准则回答评估，可自定义嵌入模型、系统提示、reranking 与距离度量。

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

- 多模型支持：云 API（GPT/Claude/Gemini/DeepSeek）与 Ollama 本地模型
- pgvector 向量检索，支持 l2/cosine/innerProduct 距离与 reranking
- Web / API / CLI 三种访问方式，Docker Compose 一键部署
- 内置 ROUGE/BLEU 与 15 项准则的 LLM 评估器

## 适用场景

- 在自己的文本数据集上做语义搜索与上下文问答
- 本地运行 LLM 搭建无 API key 的 RAG 问答服务
- 对比不同 LLM 在同一 RAG 任务上的回答质量

## 场景标签

`RAG` `文档问答` · 领域:知识与检索

## 证据(README 行号)

> L3: A Retrieval Augmented Generation application that combines the power of Large Language Models with document retrieva
> L11: This application leverages OpenAI's GPT-5 and other LLMs to generate contextually relevant responses based on user 

## 星数曲线

```mermaid
xychart-beta
    title "mzarnecki/php-rag 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 66 --> 68
    line [67, 67]
```

2026-10-18 67 → 2026-10-26 67（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `3f45c570c95b` · [字段定义](../../DATASET.md)*
