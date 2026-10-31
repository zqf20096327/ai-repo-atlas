# irahardianto/qurio

⭐ 16 · Go · MIT · 推送 2026-02-15 · [GitHub](https://github.com/irahardianto/qurio) · 个人维护

**自托管 RAG 引擎：为 AI 编程助手提供有据可查的文档上下文**

面向 AI 编程助手（Gemini-CLI、Claude Code、Cursor 等）的本地文档摄取与检索引擎：抓取文档站点或上传 PDF/DOCX/MD，用保留代码块与语法的结构化分块器处理，经 Weaviate+PostgreSQL 存储后通过 MCP 协议向 agent 暴露 qurio_search 等四个检索工具。由 Go 后端、Vue 前端、Python 摄取 worker 等 Docker Compose 微服务组成，嵌入需 Gemini API Key，重排可选 Jina/Cohere。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 结构化分块器保留代码块、API 定义与配置文件的完整语法
- BM25+向量混合检索，检索参数（alpha/top_k）可配置
- 通过 MCP（JSON-RPC 2.0，Streamable HTTP）向 agent 暴露 4 个检索工具
- Docling OCR 管道处理扫描版 PDF 与图片，爬虫支持 llms.txt/sitemap/robots.txt

## 适用场景

- 给我的编程助手接入可信的本地技术文档，减少编造
- 把选定的文档站点与 PDF 建成团队共享知识库供 agent 检索
- 本地私有化地摄取与检索文档，数据不出机器

## 场景标签

`RAG` `文档解析` · 领域:知识与检索

## 证据(README 行号)

> L20: **Qurio** is a self-hosted, open-source ingestion and retrieval engine that functions as a local **Shared Library**
> L37: - **🔌 Native MCP Support:** Exposes a standard JSON-RPC 2.0 endpoint for seamless integration with AI coding assist
> L109: ### 2. Connect Your AI Agent (MCP)

## 星数曲线

```mermaid
xychart-beta
    title "irahardianto/qurio 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `80af1ac1af61` · [字段定义](../../DATASET.md)*
