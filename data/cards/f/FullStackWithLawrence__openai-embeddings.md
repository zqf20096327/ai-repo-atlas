# FullStackWithLawrence/openai-embeddings

⭐ 19 · Python · AGPL-3.0 · 推送 2026-10-29 · [GitHub](https://github.com/FullStackWithLawrence/openai-embeddings) · [官网](https://www.youtube.com/@FullStackWithLawrence) · 个人维护

**OpenAI 嵌入 + Pinecone + LangChain 的混合检索 RAG 示例工程**

由 FullStackWithLawrence 维护的示例仓库，演示用 Python 调用 OpenAI API 生成嵌入、持久化到 Pinecone 向量数据库、由 LangChain 管理的混合检索增强生成（RAG）方案。包含命令行 PDF 加载器（提取文本、向量化并载入 Pinecone）、系统提示与模板用法，以及用 Wharton 课程讲义 PDF（21 份）对比有无嵌入时 chatGPT 回答差异的演示。另演示 Pydantic 配置管理与敏感凭据处理。运行需 OpenAI 与 Pinecone API key，通过 git clone 与 make init 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 命令行 PDF 加载器：提取文本、向量化并载入 Pinecone 索引
- 混合检索 RAG：检索相关文档并注入 OpenAI 提示
- 系统提示与模板用法演示，LangChain 作为框架层
- 提供 21 份 Wharton 课程 PDF 样例数据用于对比实验

## 适用场景

- 学习如何组合 OpenAI Embeddings、Pinecone 与 LangChain 搭建 RAG
- 验证嵌入对 chatGPT 回答质量的影响（对照实验）
- 参考 Pydantic 项目配置与 API key 安全管理实践

## 场景标签

`RAG` `教程课程` · 领域:知识与检索

## 证据(README 行号)

> L16: A Hybrid Search and Augmented Generation prompting solution using Python OpenAI API Embeddings persisted to a Pinec
> L24: - **Retrieval Augmented Generation (RAG)**. A chatGPT prompt based on a hybrid search retriever that locates releva

## 星数曲线

```mermaid
xychart-beta
    title "FullStackWithLawrence/openai-embeddings 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-30"]
    y-axis "stars" 17 --> 20
    line [18, 19, 19]
```

2026-10-18 18 → 2026-10-30 19（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 mid · 依据 README sha `3aa32257febc` · [字段定义](../../DATASET.md)*
