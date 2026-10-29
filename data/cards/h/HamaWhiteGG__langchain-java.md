# HamaWhiteGG/langchain-java

⭐ 565 · Java · Apache-2.0 · 推送 2025-11-20 · [GitHub](https://github.com/HamaWhiteGG/langchain-java) · 个人维护 · 中文 README

**LangChain 的 Java 实现，面向大数据场景开发 LLM 应用**

用 Java 语言重新实现 LangChain 框架，供 Java 技术栈开发者构建 LLM 应用，并面向大数据域（含 Spark SQL Agent、Flink SQL Agent）。提供 LLM/聊天模型抽象、链（LLMChain、SQL Chain、API Chain）、Agent 与工具机制；集成 OpenAI（含流式）、Azure OpenAI、ChatGLM2、Ollama，以及 Pinecone、Milvus 向量存储。以 Maven 依赖（langchain-core 0.2.1）分发，要求 Java 17+ 与 Maven 3.5.4+，支持多语言输出环境变量。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Java 实现的 LangChain：LLM/Chat 模型、Chain、Agent 抽象
- SQL Chain 支持自然语言查询 MySQL 等数据库
- 面向大数据：Spark SQL Agent 与 Flink SQL Agent 示例
- 集成 OpenAI/Azure OpenAI/ChatGLM2/Ollama 与 Pinecone/Milvus

## 适用场景

- 在 Java 工程中以 Maven 依赖接入 LLM 构建应用
- 用自然语言对 SQL 数据库做查询（SQL Chain）
- 在 Spark/Flink 大数据环境中接入 LLM Agent

## 场景标签

`Agent 框架` `RAG` `数据分析` · 领域:Agent 开发

## 证据(README 行号)

> L12: This is the Java language implementation of LangChain, which makes it as easy as possible to develop LLM-powered ap
> L5: It serves as a bridge to the realm of LLM within the Big Data domain, primarily in the Java stack.

## 星数曲线

```mermaid
xychart-beta
    title "HamaWhiteGG/langchain-java 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 564 --> 566
    line [565, 565]
```

2026-10-18 565 → 2026-10-29 565（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `2ae55d08ab56` · [字段定义](../../DATASET.md)*
