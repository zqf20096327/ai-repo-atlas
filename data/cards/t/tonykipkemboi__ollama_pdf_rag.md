# tonykipkemboi/ollama_pdf_rag

⭐ 550 · TypeScript · MIT · 推送 2026-04-16 · [GitHub](https://github.com/tonykipkemboi/ollama_pdf_rag) · [官网](https://tonykipkemboi.github.io/ollama_pdf_rag/) · 个人维护

**本地 PDF 问答 RAG 全栈演示：用 Ollama 与 LangChain 对话文档**

展示本地 RAG 流程的全栈演示项目：上传多个 PDF，切分并用 nomic-embed-text 生成嵌入，存入 ChromaDB，经多查询检索后由本地 Ollama 模型生成带来源引用的回答。提供三种界面：Next.js 网页应用（主要）、Streamlit 界面与 Jupyter notebook，后端为 FastAPI REST API。全部处理在本机完成，不外发数据。面向想搭建或学习本地 RAG 流程的开发者；需自行安装 Ollama 并拉取模型，CPU-only 环境需调小 chunk size。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 100% 本地处理，PDF 问答数据不离开本机
- 多查询 RAG 检索并附来源引用与推理步骤
- Next.js / Streamlit / Jupyter 三种界面与 FastAPI REST API
- 支持多 PDF 上传与本地 Ollama 模型选择

## 适用场景

- 在本机对多个 PDF 文档做问答，数据不出本地
- 通过 REST API 程序化调用 RAG 查询
- 在 Jupyter notebook 中学习/实验 RAG 流程

## 场景标签

`RAG` `文档问答` · 领域:知识与检索

## 证据(README 行号)

> L3: A powerful local RAG (Retrieval Augmented Generation) application that lets you chat with your PDF documents using O
> L11: - 🧠 **Multi-Query RAG** - Intelligent retrieval with source citations
> L118: 4. **Ask Questions** - Type your question and get answers with source citations

## 星数曲线

```mermaid
xychart-beta
    title "tonykipkemboi/ollama_pdf_rag 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-22", "2026-10-25"]
    y-axis "stars" 545 --> 551
    line [546, 548, 549, 550]
```

2026-10-18 546 → 2026-10-25 550（+4）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `f97c40d6beb1` · [字段定义](../../DATASET.md)*
