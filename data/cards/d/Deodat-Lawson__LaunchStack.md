# Deodat-Lawson/LaunchStack

⭐ 894 · TypeScript · Apache-2.0 · 推送 2026-10-28 · [GitHub](https://github.com/Deodat-Lawson/LaunchStack) · 个人维护

**TypeScript AI 应用引擎：文档摄取、OCR、RAG 与知识图的积木式框架**

以端口化 bricks 组织的 TypeScript 引擎，覆盖摄取、OCR、转录、结构化输出、混合检索、重排序、Neo4j 知识图谱同步与后台任务，并通过 Next.js 参考应用（web + worker）演示组装方式。架构分三层：引擎、13 个产品 pipelines、宿主应用，依赖边界由 CI lint 强制。包尚未发布到 npm，当前只能克隆仓库运行；需要 Node ≥ 20、pnpm、带 pgvector 的 Postgres 及配置好的 chat/embedding API（Gemini 或 Azure OpenAI）。提供 Docker Compose 与自托管路径，首个注册用户即成为 workspace owner。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- bricks/pipelines/host 三层架构，lint 强制依赖边界
- 文档摄取走事务性 outbox，由独立 worker 消费
- 13 个产品 verticals（提案、法务模板、趋势搜索等）组合引擎 bricks
- Docker Compose 提供 lite（~400MB RAM）与含 Docling OCR（~1.2GB RAM）两种栈

## 适用场景

- 我需要一个可自托带的文档问答/知识库应用的完整参考实现
- 我在构建 AI-native TypeScript 应用，需要摄取、RAG、知识图谱等引擎积木
- 我想用 Docker 一键跑起含 OCR 与转录的私有文档处理栈

## 场景标签

`RAG` `知识图谱` `文档解析` `文档问答` · 领域:知识与检索

## 证据(README 行号)

> L3: **A TypeScript engine for AI-native applications.** Ingestion, OCR, RAG, knowledge graph, LLM abstractions, and back
> L121: |`packages/`|The bricks: persistence, model calls, orchestration, conversion, indexing, retrieval, shared tools an
> L131: |`@launchstack/engine`|unpublished|`createEngine(CoreConfig)`: database, storage and graph handles; registration o

## 星数曲线

```mermaid
xychart-beta
    title "Deodat-Lawson/LaunchStack 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 893 --> 895
    line [894, 894]
```

2026-10-18 894 → 2026-10-28 894（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 mid · 依据 README sha `5b77da0614da` · [字段定义](../../DATASET.md)*
