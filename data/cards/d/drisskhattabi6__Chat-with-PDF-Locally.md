# drisskhattabi6/Chat-with-PDF-Locally

⭐ 20 · Python · 推送 2026-11-10 · [GitHub](https://github.com/drisskhattabi6/Chat-with-PDF-Locally) · 个人维护

**本地优先的 PDF 对话 RAG 应用：上传、索引并问答 PDF**

基于 Streamlit 的本地 RAG 应用：用户上传 PDF 后选择提取引擎（PyMuPDF4LLM 快速版或 Docling 均衡版）、四种分块策略（递归字符/Markdown 标题/Token/页面感知）、嵌入来源（本地 SentenceTransformers 或 Ollama 嵌入），内容持久化存储于 ChromaDB，通过向量检索 + BM25 混合重排后由所选 LLM 生成回答，并展示检索到的来源片段。LLM 可选 Ollama（本地）或 OpenAI、Groq、OpenRouter、SambaNova（需 API key）。基于 PDF 哈希缓存已索引文档，支持对话导出 PDF。需 Python 3.10+ 环境，从源码克隆安装，Docker 尚未提供。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 五种 LLM 提供商可选（Ollama 本地 + OpenAI/Groq/OpenRouter/SambaNova 云端）
- 四种可选分块策略与双 PDF 提取引擎（PyMuPDF4LLM/Docling）
- 向量检索 + BM25 混合重排，回答附带来源片段展示
- ChromaDB 持久化索引，PDF 哈希缓存避免重复处理

## 适用场景

- 在本地对论文、报告、手册等 PDF 提问并获得带出处的回答
- 不依赖云端 API、使用本地 Ollama 模型进行文档问答
- 按文档结构选择不同分块与提取策略以优化问答效果

## 场景标签

`文档问答` · 领域:知识与检索

## 证据(README 行号)

> L5: **ChatPDF** is a local RAG (Retrieval-Augmented Generation) application that lets you upload a PDF, index its conten
> L86: - **Ollama** (local)

## 星数曲线

```mermaid
xychart-beta
    title "drisskhattabi6/Chat-with-PDF-Locally 星数(近 2 点)"
    x-axis ["2026-11-10", "2026-11-22"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-11-10 20 → 2026-11-22 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-18 · 置信度 mid · 依据 README sha `c16a91a93311` · [字段定义](../../DATASET.md)*
