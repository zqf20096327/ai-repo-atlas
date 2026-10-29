# WalkCloud/Synthetix

⭐ 21 · TypeScript · Apache-2.0 · 推送 2026-07-23 · [GitHub](https://github.com/WalkCloud/Synthetix) · [官网](https://synthetix-doc.com) · 组织维护 · 中文 README

**自托管 AI 知识库与长文写作工作台**

面向需要将大批源文档转为结构化、可溯源长文输出的用户：上传 PDF/DOCX/HTML 等文档后构建三层知识库（原始分块、LightRAG 实体图、LLM 知识 Wiki），支持关键词/语义检索、知识图浏览、引导式大纲与逐节写作、双模型 A/B 生成、版本回滚、Markdown/PDF/DOCX 导出。写作产出带引用溯源与文档拓扑分析。提供配套 MCP server 供 AI 智能体（Claude Code 等）经 REST API 驱动。注意：知识图模式要求嵌入模型至少 1536 维，低维模型会静默降级为普通检索。提供 Windows Electron 安装包，数据库默认 SQLite，LightRAG 存储可选 PostgreSQL/pgvector、Neo4j、Milvus、Qdrant。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三层知识架构：原始分块 + LightRAG 实体图 + 可编辑知识 Wiki
- 逐节生成长文，带引用溯源、版本管理与文档拓扑覆盖分析
- 配套 MCP server，AI 智能体可用自然语言驱动摄入、写作与导出
- 支持 OpenAI 兼容端点、Anthropic、Ollama 等模型后端

## 适用场景

- 把成堆报告、规格书整理成可溯源的研究报告或技术方案
- 在私有文档库上做知识检索、图浏览与 Wiki 沉淀
- 多节长文写作时逐节生成、双模型对比并核验来源覆盖
- 通过 Claude Code 等 agent 以自然语言操作知识库与写作流程

## 场景标签

`知识库管理` `RAG` `知识图谱` `AI 写作` · 领域:内容生成

## 证据(README 行号)

> L25: Synthetix is a self-hosted AI workbench for people who need to turn large collections of source documents into stru
> L29: Instead of treating your files as one-off attachments, Synthetix converts them into a layered knowledge base, then 

## 星数曲线

```mermaid
xychart-beta
    title "WalkCloud/Synthetix 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-29 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `7b9f0abd35ad` · [字段定义](../../DATASET.md)*
