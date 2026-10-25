# pinecone-io/pinecone-ts-client

⭐ 279 · TypeScript · Apache-2.0 · 推送 2026-10-23 · [GitHub](https://github.com/pinecone-io/pinecone-ts-client) · [官网](https://www.pinecone.io) · 组织维护

**Pinecone 向量数据库的官方 TypeScript/Node 客户端 SDK**

Pinecone 官方维护的 TypeScript SDK，面向在服务端构建全文检索、向量检索与 RAG 应用的开发者。功能覆盖：文档与全文检索、向量 upsert/查询与元数据过滤、Serverless/Pod 索引管理、托管模型集成嵌入（Integrated Embedding）、通过 pc.inference 调用托管 embedding 与 rerank 模型，以及 Pinecone Assistant 的创建与聊天操作。要求 TypeScript >=5.2.0、Node.js >=22.0.0 与 Pinecone 账号 API key；仅限服务端使用，浏览器中使用会暴露 API key。提供完整 TypeScript 类型支持。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 文档存储与多字段全文检索（query-string 打分、字段过滤）
- 高维向量 upsert/查询与元数据过滤、命名空间组织
- 托管集成嵌入：由 Pinecone 生成 embedding，无需自行管理向量
- pc.inference 提供托管 embedding/rerank 模型；Pinecone Assistant 创建与聊天 API

## 适用场景

- 在 Node 服务端为 RAG 或语义检索应用接入 Pinecone 向量库
- 管理文档与向量索引：创建、备份、批量导入、元数据过滤
- 通过 Assistant API 构建带文件交互的 AI 助手

## 场景标签

`向量数据库` · 领域:知识与检索

## 证据(README 行号)

> L1: # Pinecone TypeScript SDK &middot; License npm npm GitHub Workflow Status (with event)
> L5: Use Pinecone to store, search, and manage documents and high-dimensional vectors. Search document text directly with

## 星数曲线

```mermaid
xychart-beta
    title "pinecone-io/pinecone-ts-client 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 278 --> 280
    line [279, 279]
```

2026-10-18 279 → 2026-10-25 279（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `3161e4d29ba0` · [字段定义](../../DATASET.md)*
