# joungminsung/OpenDocuments

⭐ 121 · TypeScript · MIT · 推送 2026-07-26 · [GitHub](https://github.com/joungminsung/OpenDocuments) · [官网](https://joungminsung.github.io/OpenDocuments/) · 个人维护 · 中文 README

**自托管 RAG 平台：对组织文档做带引用的 AI 搜索**

开源的 TypeScript 自托管 RAG 平台：通过连接器索引 GitHub、Notion、Google Drive、Confluence、S3、本地文件与网页等来源，解析分块后存入 SQLite（元数据）与 LanceDB（向量），以向量+FTS5 关键词混合检索、重排、HyDE、多查询检索生成带来源引用的自然语言回答。支持 Ollama 本地或 OpenAI/Anthropic/Google/xAI 云模型，提供 CLI、Web UI、HTTP API、SDK、插件系统与 MCP server，供 MCP 客户端（Claude Code、Cursor 等）检索内部知识库。团队模式含 API key、角色、审计日志与工作区隔离。通过 npm 全局安装或 Docker Compose 部署。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 混合检索：向量 + FTS5 关键词 + 重排 + HyDE + 多查询 + 父文档召回
- 答案带来源引用、置信度评分与幻觉防护
- 本地优先：配合 Ollama 运行时数据不出自有基础设施
- MCP server 让 Claude Code、Cursor、Windsurf 等检索内部知识库

## 适用场景

- 把散落在 GitHub/Notion/Confluence 的团队文档统一成可问答的知识库
- 通过 MCP 让 AI 编程助手在写代码时检索组织文档
- 敏感文档场景下用 Ollama 做全本地 RAG 搜索

## 场景标签

`RAG` `文档问答` · 领域:知识与检索

## 证据(README 行号)

> L18: **OpenDocuments is an open source, self-hosted RAG (Retrieval-Augmented Generation) platform that turns scattered c
> L51: OpenDocuments **connects to your document sources**, **parses and chunks each document**, **stores metadata in SQLi
> L64: |**Local or cloud models**|Use Ollama locally or cloud providers such as OpenAI, Anthropic, Google, and xAI|

## 星数曲线

```mermaid
xychart-beta
    title "joungminsung/OpenDocuments 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-22", "2026-10-26"]
    y-axis "stars" 115 --> 122
    line [116, 118, 121, 121]
```

2026-10-18 116 → 2026-10-26 121（+5）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `6e7e6d03274d` · [字段定义](../../DATASET.md)*
