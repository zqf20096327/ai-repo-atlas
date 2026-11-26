# Deodat-Lawson/LaunchStack

⭐ 898 · TypeScript · Apache-2.0 · 推送 2026-11-24 · [GitHub](https://github.com/Deodat-Lawson/LaunchStack) · 个人维护

**AI 应用引擎+自托管文档问答参考应用：摄取、RAG、知识图谱**

TypeScript 编写的 AI 原生应用引擎，以端口化砖块（persistence、llm、orchestration、conversion、indexing、retrieval 等）加 pipelines 组合层构成，并附带一个 Next.js 参考应用：上传文档、OCR、分块嵌入、混合检索与带权限引用的聊天，背景摄取由事务性 outbox + 独立 worker 处理。自托管只需 Docker 两条命令；本地开发需 Node ≥20、pnpm 与带 pgvector 的 Postgres。核心包尚未发布到 npm，需直接运行本仓库。

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

- 文档摄取、OCR、分块、嵌入、混合检索与重排序的完整管线
- 实体提取与 Neo4j 知识图谱同步
- 13 个产品 verticals 通过 @launchstack/pipelines 组合砖块
- Docker 两条命令自托管，自动 HTTPS 与 backup/restore 运维命令

## 适用场景

- 团队自托管一个可检索、可对话的文档知识库
- 基于引擎砖块搭建自己的 AI 原生应用
- 用 pipelines 里的提案、营销、趋势搜索等垂直流程

## 场景标签

`文档问答` `RAG` `知识图谱` `文档解析` · 领域:知识与检索

## 证据(README 行号)

> L3: **A TypeScript engine for AI-native applications.** Ingestion, OCR, RAG, knowledge graph, LLM abstractions, and back
> L13: The publishable bricks in `packages/` and the compositions package `@launchstack/pipelines` are **not yet on npm**.
> L156: |`@launchstack/llm`|unpublished|Structured output, guardrails, chat configuration, model providers and embeddings.

## 星数曲线

```mermaid
xychart-beta
    title "Deodat-Lawson/LaunchStack 星数(近 5 点)"
    x-axis ["2026-10-24", "2026-11-08", "2026-11-10", "2026-11-18", "2026-11-26"]
    y-axis "stars" 893 --> 899
    line [894, 896, 897, 898, 898]
```

2026-10-24 894 → 2026-11-26 898（+4）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-24 · 置信度 mid · 依据 README sha `0a1c791cf0f2` · [字段定义](../../DATASET.md)*
