# agent-accessibility/KMCP

⭐ 13 · Python · AGPL-3.0 · 推送 2026-10-19 · [GitHub](https://github.com/agent-accessibility/KMCP) · [官网](https://github.com/hashwnath/KMCP#quick-start) · 组织维护

**自托管 MCP 服务器：把文档源变成任意 agent 可检索的知识端点**

KnowledgeMCP 将网站、PDF、Confluence、Notion、S3、GitHub 等文档源摄取后，暴露为标准 MCP 端点，提供 docs_search、code_sample_search、docs_fetch 三个工具供 Claude、Cursor、Copilot 等 MCP 客户端调用。查询路径不含 LLM 调用：使用本地 fastembed 嵌入模型（默认 BAAI/bge-small-en-v1.5）加 OpenSearch 的 BM25/kNN 混合检索。本地通过 docker compose 启动，另附带 SAM 模板的 AWS 生产部署路径（Lambda+DynamoDB+SQS+S3+OpenSearch），支持多租户隔离与限额。后端为 AGPL-3.0 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 提供 docs_search / code_sample_search / docs_fetch 三个 MCP 工具
- 查询时零 LLM 调用：本地 fastembed 嵌入 + OpenSearch BM25/kNN 混合检索
- 支持 website_url、file_upload（PDF/DOCX/PPTX 等）、S3/Azure Blob/GCS、Confluence/Notion/SharePoint、GitHub/GitLab 六类源
- 本地 docker compose 一键启动，另提供 AWS SAM 模板的生产部署路径

## 适用场景

- 为团队文档搭建自托管的 MCP 检索端点
- 让 Claude/Cursor/Copilot 等 agent 直接查询内部文档与代码示例
- 在避免按查询付费 LLM 重排的前提下做 RAG 检索

## 场景标签

`语义搜索` · 领域:知识与检索

## 证据(README 行号)

> L11: KnowledgeMCP turns any documentation source (websites, PDFs, Confluence, Notion, S3, GitHub) into a **standards-com
> L13: - 🔌 **MCP-native** — three tools (`docs_search`, `code_sample_search`, `docs_fetch`) any agent can plug into

## 星数曲线

```mermaid
xychart-beta
    title "agent-accessibility/KMCP 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-28", "2026-10-31"]
    y-axis "stars" 11 --> 14
    line [12, 13, 13]
```

2026-10-18 12 → 2026-10-31 13（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `88c64a27f9ab` · [字段定义](../../DATASET.md)*
