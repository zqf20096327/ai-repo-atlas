# pinecone-io/pinecone-claude-code-plugin

⭐ — · [GitHub]() · 组织维护

**Pinecone 官方的 Claude Code 插件：语义搜索与 RAG 工作流**

由 Pinecone 维护的 Claude Code 插件，把 Pinecone 向量数据库能力接入 Claude Code：内嵌完整 Pinecone MCP Server（索引创建/列表/搜索/记录 upsert/重排等 7 个工具）、Pinecone Assistant 文档问答（带引用、增量同步）、以及 /pinecone:query、quickstart、full-text-search 等斜杠命令技能。通过 Claude Code 插件目录或 Pinecone marketplace 安装，需设置 PINECONE_API_KEY；Assistant 命令依赖 uv，MCP Server 经 npx 运行需 Node.js。查询命令仅支持使用 Pinecone 托管嵌入的 integrated 索引。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 内嵌完整 Pinecone MCP Server（7 个工具：索引管理、记录搜索/写入、重排）
- Pinecone Assistant 文档问答技能：创建、上传、同步、上下文检索，支持自然语言调用
- 斜杠命令覆盖 quickstart、语义查询、全文检索预览 API（BM25/稠密/稀疏混合）
- FTS 技能附带批量 upsert 脚本（分批错误检查与就绪轮询）

## 适用场景

- 在 Claude Code 中直接管理 Pinecone 索引并做语义搜索
- 基于自有文档创建带引用的问答助手
- 构建混合词法+语义检索的 RAG 工作流

## 场景标签

`文档问答` `RAG` `语义搜索` · 领域:知识与检索

## 证据(README 行号)

> L3: A lightweight plugin that integrates Pinecone vector database capabilities directly into Claude Code, enabling seman
> L8: - **Pinecone MCP Server** – Full integration with the Pinecone Model Context Protocol server for index creation, lis
> L145: The plugin includes the full Pinecone MCP Server with the following tools:

## 星数曲线

```mermaid
xychart-beta
    title "pinecone-io/pinecone-claude-code-plugin 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 68 --> 70
    line [69, 69]
```

2026-10-18 69 → 2026-10-27 69（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `e4c5856111e1` · [字段定义](../../DATASET.md)*
