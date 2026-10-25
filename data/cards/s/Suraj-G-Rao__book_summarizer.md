# Suraj-G-Rao/book_summarizer

⭐ 45 · Python · GPL-3.0 · 推送 2026-04-13 · [GitHub](https://github.com/Suraj-G-Rao/book_summarizer) · 个人维护

**上传 PDF 生成营销简介与内容摘要的 Streamlit 应用**

基于 Streamlit 的网页应用：用户上传多个 PDF，系统抽取内容并分块，用 Google Gemini embeddings 构建 FAISS 向量库，通过 LangChain 做文档处理与检索，调用 Groq 的 LLaMA3-8B/70B 模型生成营销简介或内容摘要。面向需要快速获得书籍/文档摘要与宣传文案的读者和内容创作者。运行需配置 GROQ_API_KEY 与 GOOGLE_API_KEY，通过 git clone 源码并以 streamlit run 启动。页面展示 NIE University、IVIS Labs、PULSE 标识，附演示视频与报告链接。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 上传多个 PDF 并分块处理
- Gemini embeddings + FAISS 向量检索
- Groq LLaMA3-8B/70B 生成营销简介与摘要
- Streamlit 交互界面

## 适用场景

- 为书籍或文档快速生成摘要
- 生成图书营销简介文案
- 查询已上传文档并得到摘要回答

## 场景标签

`AI 写作` `文档问答` · 领域:内容生成

## 证据(README 行号)

> L3: This is a **Streamlit-based application** that allows users to upload **PDF documents** and generate **marketing blu
> L5: The application uses **Google Gemini embeddings** to create a **FAISS vector store** for document retrieval and **Gr

## 星数曲线

```mermaid
xychart-beta
    title "Suraj-G-Rao/book_summarizer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 44 --> 46
    line [45, 45]
```

2026-10-18 45 → 2026-10-25 45（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `000a123373cb` · [字段定义](../../DATASET.md)*
