# SoluDevTech/mcp-raganything

⭐ 15 · Python · 推送 2026-07-27 · [GitHub](https://github.com/SoluDevTech/mcp-raganything) · 组织维护

**面向 RAGAnything/LightRAG 的多模态 RAG 服务，提供 REST API 与 MCP 服务器**

将 RAGAnything 和 LightRAG 封装为 FastAPI 服务：支持图式 LightRAG 与经典 RAG（多查询生成+LLM 评分）两条检索路径；文件从 MinIO 拉取、索引到 PostgreSQL 知识图谱，按 working_dir 做项目隔离。同时提供 MCP 服务器注册表，可从 OpenAPI 文档动态生成 MCP server。安全模型为双重认证（Logto JWT 或 per-user API key）、行级安全与 per-user LLM 凭据/RAG 隔离，需搭配 soludev-compose-apps 部署栈；旧 master API_KEY 与 OPEN_ROUTER_API_KEY（chat/embeddings）已标记废弃。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 图式 LightRAG 与经典 RAG 双管线检索
- MCP 服务器注册表：注册外部/由 OpenAPI 文档动态生成 MCP server
- JWT/Logto + per-user API key 双重认证与 per-user RAG 隔离
- 自动识别 PDF/Office/Markdown/图片等文档格式（含 OCR 与视觉模型）

## 适用场景

- 通过 REST API 或 MCP 客户端对接文档索引与知识库问答
- 在 MinIO + PostgreSQL 栈上按项目/用户隔离构建多模态 RAG 服务
- 集中注册并发现多个 MCP server，供 composable-agents 等客户端调用

## 场景标签

`RAG` `文档问答` · 领域:知识与检索

## 证据(README 行号)

> L3: Multi-modal RAG service exposing a REST API and MCP server for document indexing and knowledge-base querying, powere
> L5: The service also hosts the **MCP server registry** — a CRUD API for registering external MCP servers and generating 

## 星数曲线

```mermaid
xychart-beta
    title "SoluDevTech/mcp-raganything 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `5cee6b7ea7c5` · [字段定义](../../DATASET.md)*
