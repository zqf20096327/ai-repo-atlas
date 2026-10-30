# EarthlyAlien/Document-Assistant

⭐ 20 · Python · MIT · 推送 2026-02-19 · [GitHub](https://github.com/EarthlyAlien/Document-Assistant) · 个人维护

**基于 RAG 的 PDF 文档问答助手（Streamlit 界面）**

个人开发的文档问答应用：上传 PDF 后解析并分块，用 Sentence Transformers 生成向量嵌入存入 FAISS 索引；提问时检索相关片段并交给 OpenAI GPT 生成带上下文的回答。提供 Streamlit 网页界面，支持调整分块大小与重叠、查看系统统计与对话历史。需自备 OpenAI API key，从源码克隆并以 pip 安装依赖后用 streamlit run 启动，技术栈基于 Python 3.12、LangChain、FAISS-CPU。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- PDF 解析、可配置分块（默认 1000/200）与文本预处理
- Sentence Transformers 嵌入 + FAISS 向量索引与持久化存储
- OpenAI GPT 基于检索上下文生成回答
- Streamlit 界面含实时统计与对话历史

## 适用场景

- 上传自己的 PDF 文档并进行问答
- 针对长文档做基于语义检索的提问
- 追踪并回顾历史问答记录

## 场景标签

`文档问答` · 领域:知识与检索

## 证据(README 行号)

> L3: A powerful document analysis tool that uses Retrieval Augmented Generation (RAG) to provide intelligent answers to q
> L114:  - LLM-powered answer generation with context

## 星数曲线

```mermaid
xychart-beta
    title "EarthlyAlien/Document-Assistant 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-30 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `ab8ddeb35095` · [字段定义](../../DATASET.md)*
