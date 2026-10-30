# zakirkun/rag-chat-bot

⭐ 15 · Go · MIT · 推送 2025-11-20 · [GitHub](https://github.com/zakirkun/rag-chat-bot) · 个人维护

**基于 Go 与 pgvector 的文档问答 RAG 聊天机器人**

用 Go 编写的检索增强生成（RAG）聊天机器人后端：通过 OpenAI API 生成 1536 维向量嵌入与回答，向量与对话历史存储在 PostgreSQL（pgvector 扩展）中，使用 HNSW 索引做相似度检索。提供 HTTP API：/api/chat 对话端点与 /api/documents 文档上传端点，支持文档元数据（JSONB）与会话上下文。运行需 Go 1.21+、PostgreSQL 15+、OpenAI API key，可用 Docker Compose 部署数据库。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- pgvector + HNSW 索引的向量相似度文档检索
- OpenAI API 生成嵌入与回答
- 对话历史与上下文存取（Conversations/Messages 表）
- 提供 /api/chat 与 /api/documents HTTP 端点

## 适用场景

- 基于自有文档搭一个可问答的聊天机器人
- 通过 API 上传文档并对其进行检索问答
- 保留会话上下文进行多轮对话

## 场景标签

 · 领域:LLM 应用/RAG

## 证据(README 行号)

> L8: A Retrieval-Augmented Generation (RAG) Chat Bot that provides accurate responses based on available documents. This 
> L15: - 🎯 Efficient RAG system for accurate responses

## 星数曲线

```mermaid
xychart-beta
    title "zakirkun/rag-chat-bot 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `1c46ca8d64da` · [字段定义](../../DATASET.md)*
