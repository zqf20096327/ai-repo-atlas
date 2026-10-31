# pinecone-io/pinecone-rag-demo

⭐ 81 · HTML · MIT · 推送 2026-10-30 · [GitHub](https://github.com/pinecone-io/pinecone-rag-demo) · 组织维护

**Pinecone + Vercel 全栈 RAG 聊天机器人示例教程**

Pinecone 官方维护的 Next.js 全栈示例：以教程形式构建基于 RAG 的聊天机器人，对比无上下文与带知识库上下文两种回答模式。机制包括：网页爬虫抓取 URL 内容、分块（递归字符/Markdown 切分）、嵌入后存入 Pinecone 索引；查询时通过向量检索取回相关片段注入 system prompt，用 OpenAI API（openai-edge，edge 运行时）流式生成回答，并在 UI 中展示回答所用的上下文片段。面向希望学习 RAG 与 Pinecone 用法的开发者。

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

- 爬虫抓取 URL → 分块 → 嵌入 → Pinecone 索引的完整知识库构建流程
- 基于 Pinecone 向量检索的 getContext 上下文注入与 system prompt 更新
- Vercel AI SDK 驱动的流式聊天界面与上下文来源展示面板
- 对比无上下文与 RAG 上下文两种回答模式

## 适用场景

- 学习如何用 Pinecone 构建带知识库的聊天机器人
- 参考网页爬取、分块与嵌入的 RAG 数据管道实现
- 作为 Next.js + edge 运行时流式聊天应用的起点模板

## 场景标签

`聊天机器人` `RAG` `教程课程` · 领域:对话与助手

## 证据(README 行号)

> L1: In this example, we'll build a full-stack application that uses Retrieval Augmented Generation (RAG) powered by Pine
> L88:   apiKey: process.env.OPENAI_API_KEY,

## 星数曲线

```mermaid
xychart-beta
    title "pinecone-io/pinecone-rag-demo 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 80 --> 82
    line [81, 81]
```

2026-10-18 81 → 2026-10-31 81（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `e8d12eae9497` · [字段定义](../../DATASET.md)*
