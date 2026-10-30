# mshadmanrahman/root-kg

⭐ 16 · Python · MIT · 推送 2026-10-12 · [GitHub](https://github.com/mshadmanrahman/root-kg) · [官网](https://github.com/mshadmanrahman/root-kg) · 个人维护

**把笔记/会议/邮件建为个人知识图谱并给带引用回答的工具**

ROOT 将 Obsidian 库、会议记录、邮件等来源索引为单一 SQLite 知识层：本地 MiniLM 模型在 CPU 上做语义嵌入（零 API 成本），LLM 从变更笔记中抽取实体与 10 类带置信度的关系形成图谱，root_ask 结合语义检索与图遍历生成带引用的回答。以 MCP server 形式对外暴露 18 个工具，主要供 Claude Code 调用；支持 Anthropic/OpenRouter/Ollama 三种后端，无 Docker/Postgres/Neo4j 依赖，增量索引基于内容哈希。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 本地 MiniLM 嵌入模型，索引零 API 成本
- LLM 实体抽取 + 10 类带置信度的关系构成知识图谱
- 18 个 MCP 工具：检索、多源情报、GraphRAG 问答、周报摘要等
- 多 root 索引与按 root 的安全防护（缺失盘跳过不误删）

## 适用场景

- 跨笔记、会议和邮件用自然语言提问并获得带引用的回答
- 查看某人/项目在我所有记录中的关联与活动脉络
- 追踪未闭环的承诺事项与决策演化过程

## 场景标签

`知识库管理` `知识图谱` `RAG` `文档问答` · 领域:知识与检索

## 证据(README 行号)

> L12:  Ask questions across all your knowledge. Get cited answers.
> L89: **Query.** `root_ask` runs semantic search for the most relevant chunks, pulls the graph neighborhood of the entiti

## 星数曲线

```mermaid
xychart-beta
    title "mshadmanrahman/root-kg 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-30"]
    y-axis "stars" 14 --> 17
    line [15, 16, 16]
```

2026-10-18 15 → 2026-10-30 16（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `0a4e48b1de15` · [字段定义](../../DATASET.md)*
