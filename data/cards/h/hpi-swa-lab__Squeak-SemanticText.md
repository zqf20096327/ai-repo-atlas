# hpi-swa-lab/Squeak-SemanticText

⭐ 18 · Smalltalk · 推送 2026-06-30 · [GitHub](https://github.com/hpi-swa-lab/Squeak-SemanticText) · 组织维护

**为 Squeak/Smalltalk 提供 OpenAI 客户端、语义搜索与 RAG 的工具包**

面向 Squeak/Smalltalk 开发者的 AI 工具包：含 OpenAI API 客户端（对话补全、嵌入、语音转写/合成，带限流、开销追踪与价格估算）、对话式 agent 框架 SemanticConversation（支持函数调用）、ChatGPT 图形界面、语义/相似搜索与 RAG 框架 SemanticCorpus（内置简易向量数据库），以及编辑器、帮助浏览器、邮件列表等实验性集成。安装通过 Metacello 从 GitHub 加载，需配置 OpenAI API key。仍声明处于开发中，实验功能可能不稳定。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- OpenAI API 客户端：对话补全、嵌入、语音转写/合成，含限流与开销追踪
- SemanticConversation 对话/自主 agent 框架，支持函数调用与少样本提示
- SemanticCorpus 提供语义搜索、相似搜索与 RAG，内置向量数据库
- 编辑器、帮助浏览器、Inspector 等实验性集成

## 适用场景

- 在 Squeak 中通过 GUI 或 API 与 ChatGPT 对话
- 为 Squeak 帮助系统/邮件列表构建语义搜索与问答
- 在 Smalltalk 代码中直接嵌入 LLM 调用与 agent 逻辑

## 场景标签

`Agent 框架` `RAG` `语义搜索` `聊天机器人` · 领域:Agent 开发

## 证据(README 行号)

> L7: - **OpenAI API client:** Currently supports chat completions, embeddings, and speech transcription/synthesis. Includ
> L10: - **SemanticCorpus:** Framework for semantic search, similarity search, and retrieval-augmented generation (RAG, ak
> L182: Different models can be registered by providers, selected, and used through the `SemanticText` interface. The main

## 星数曲线

```mermaid
xychart-beta
    title "hpi-swa-lab/Squeak-SemanticText 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-30 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `4f2ca12f04ff` · [字段定义](../../DATASET.md)*
