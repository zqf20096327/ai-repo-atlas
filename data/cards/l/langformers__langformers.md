# langformers/langformers

⭐ 20 · Python · Apache-2.0 · 推送 2026-02-27 · [GitHub](https://github.com/langformers/langformers) · [官网](https://langformers.com) · 组织维护

**统一 LLM 与 MLM 的 NLP 任务流水线 Python 库**

面向开发者的 Python 库，将 Hugging Face Transformers、Ollama、FAISS、ChromaDB、Pinecone 等组件纳入统一 API（tasks.create_<something> 模式）。覆盖三类任务：生成式 LLM 的对话、API 推理、数据标注、分块；掩码语言模型（如 RoBERTa）的分类器训练、从头预训练与继续预训练；以及句嵌入、语义搜索、重排和知识蒸馏。通过 pip 安装核心包，FAISS/ChromaDB/Pinecone 以可选依赖形式提供。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 统一 API 覆盖 LLM 与 MLM 两类模型的 NLP 任务
- 集成 Transformers、Ollama、FAISS、ChromaDB、Pinecone
- 支持 MLM 从头预训练与自定义数据继续预训练
- 内置数据标注、语义搜索、重排与知识蒸馏任务

## 适用场景

- 用一致接口在 LLM 与 MLM 之间切换完成各类 NLP 任务
- 用 LLM 自动标注训练数据
- 搭建语义搜索与句嵌入索引
- 对预训练模型做知识蒸馏

## 场景标签

`语义搜索` `模型训练` `微调` · 领域:知识与检索

## 证据(README 行号)

> L5: Langformers is a flexible and user-friendly library that unifies NLP pipelines for both Large Language Models (LLMs)
> L17: No need to juggle different frameworks — Langformers brings Hugging Face Transformers, Ollama, FAISS, ChromaDB, Pin

## 星数曲线

```mermaid
xychart-beta
    title "langformers/langformers 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-28 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `9226fcdecbc9` · [字段定义](../../DATASET.md)*
