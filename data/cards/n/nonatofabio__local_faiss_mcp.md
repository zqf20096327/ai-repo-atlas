# nonatofabio/local_faiss_mcp

⭐ 36 · Python · MIT · 推送 2026-04-24 · [GitHub](https://github.com/nonatofabio/local_faiss_mcp) · 个人维护

**本地 FAISS 向量库 MCP 服务器，为 Claude 等 agent 提供语义检索**

基于 FAISS 的本地向量数据库，以 MCP 服务器形式向 Claude Code/Claude Desktop 等 MCP 兼容客户端提供文档摄取与语义检索两个工具，外加 extract-answer 与 summarize-documents 两个内置提示词。文档自动分块（约 500 词、50 词重叠）并用 Hugging Face sentence-transformers 模型嵌入（默认 all-MiniLM-L6-v2），索引与元数据持久化到磁盘，可选 cross-encoder 两阶段重排。原生支持 TXT/MD/PDF，DOCX 等 40+ 格式需安装 pandoc。另提供 local-faiss 命令行做独立索引与搜索。需 Python 3.10+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- MCP 工具 ingest_document / query_rag_store，可被任意 MCP 兼容客户端调用
- 文档自动分块嵌入，索引与元数据持久化到磁盘
- 可配置 Hugging Face 嵌入模型与 cross-encoder 两阶段重排
- local-faiss CLI 提供独立索引与搜索，支持增量索引与 glob/递归目录

## 适用场景

- 给 Claude Code / Claude Desktop 接一个本地文档知识库
- 对本地 PDF/Markdown 文件做语义检索问答
- 在 CLI 中批量索引并搜索项目文档

## 场景标签

`RAG` `语义搜索` · 领域:知识与检索

## 证据(README 行号)

> L8: A Model Context Protocol (MCP) server that provides local vector database functionality using FAISS for Retrieval-Au
> L19: - **MCP Compatible**: Works with any MCP-compatible AI agent or client

## 星数曲线

```mermaid
xychart-beta
    title "nonatofabio/local_faiss_mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 35 --> 37
    line [36, 36]
```

2026-10-18 36 → 2026-10-28 36（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `29fe5a1689c0` · [字段定义](../../DATASET.md)*
