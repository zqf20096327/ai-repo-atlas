# enricollen/rag-conversational-agent

⭐ 49 · Python · 推送 2025-12-25 · [GitHub](https://github.com/enricollen/rag-conversational-agent) · [官网](https://medium.com/@nello.enrico/how-to-build-a-python-flask-rag-chat-with-documents-cf5de7b05399) · 个人维护

**本地 RAG 聊天机器人：基于个人 PDF 文档问答**

基于 Flask 的本地 RAG 对话应用：用户将 PDF 放入 data 目录，运行 populate_database.py 将文档索引到 Chroma 向量数据库，随后通过 Web 页面提问，检索 top-K 相关片段交给 LLM 生成回答。LLM 来源支持三种配置：本地 Ollama、OpenAI API、Anthropic API。组件包括 Chroma、Flask、Ollama 与 LangChain，安装方式为 git clone 源码后 pip 安装依赖运行。

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

- PDF 文档索引到 Chroma 向量库后检索问答
- LLM 三种可选来源：本地 Ollama、OpenAI API、Anthropic API
- Flask 提供 Web 交互界面

## 适用场景

- 把自己的 PDF 资料做成可问答的知识库
- 本地 Ollama 模型离线运行个人文档问答

## 场景标签

`文档问答` · 领域:知识与检索

## 证据(README 行号)

> L1: A simple local Retrieval-Augmented Generation (RAG) chatbot that can answer to questions by acquiring information fr
> L66: 6. **Run once the populate_database script to index the pdf files into the vector db:**

## 星数曲线

```mermaid
xychart-beta
    title "enricollen/rag-conversational-agent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 48 --> 50
    line [49, 49]
```

2026-10-18 49 → 2026-10-30 49（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `905e8958500d` · [字段定义](../../DATASET.md)*
