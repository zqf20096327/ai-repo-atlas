# sadofriod/graphrag-ts

⭐ 10 · TypeScript · MIT · 推送 2026-11-25 · [GitHub](https://github.com/sadofriod/graphrag-ts) · [官网](https://ashesborn.cloud) · 个人维护 · 中文 README

**TypeScript GraphRAG 引擎：在 Postgres/pgvector 上构建带出处的知识图谱问答**

以 TypeScript 实现的 GraphRAG 引擎与 MCP server：将实体/关系抽取结果与来源证据存入 PostgreSQL/pgvector，答案携带可回溯的 chunk 级引用，引用覆盖不足时返回显式弃答。支持增量构建（复用未变更的社区摘要）、局部混合检索（向量+关键词+图）与全局 Map-Reduce 查询。可通过托管 MCP 端点（匿名读取层、x402 付费判定工具）使用，或用 Docker Compose 自托管，也可作为 Bun 库引入；要求 Bun >= 1.1，不能被纯 Node 直接导入。

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

- 证据在写入时随节点/边存储，答案带 chunk 级引用
- 引用覆盖不足时返回显式弃答而非弱信号作答
- Postgres 原生存图与向量，增量构建复用社区摘要
- 提供 MCP server（隔离 workspace）与本地浏览器 showcase

## 适用场景

- 为 Markdown 文档库搭建可溯源的图谱化问答
- 通过 MCP 客户端接入托管端点查询论文撤稿状态与证据审计
- 在已有 PostgreSQL 基础设施上运行 GraphRAG 而不引入额外图数据库

## 场景标签

`RAG` `知识图谱` `文档问答` · 领域:知识与检索

## 证据(README 行号)

> L8: `graphrag-ts` is a GraphRAG engine in TypeScript. It builds the knowledge graph in PostgreSQL,
> L61: ## MCP tools
> L102: It expects PostgreSQL with pgvector and RAG_* model settings configured as in the self-hosted path below.


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `de0e059db684` · [字段定义](../../DATASET.md)*
