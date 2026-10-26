# PlateerLab/synaptic-memory

⭐ 33 · Python · NOASSERTION · 推送 2026-07-03 · [GitHub](https://github.com/PlateerLab/synaptic-memory) · [官网](https://pypi.org/project/synaptic-memory/) · 组织维护

**给 LLM agent 的知识图谱+MCP 工具服务器，零 LLM 索引**

面向 LLM agent 的知识图谱与 MCP 工具服务器：从 CSV/JSONL/Office 文件/SQL 数据库构建图（文档、分块、行、边），索引阶段默认零 LLM 调用，用 FK、NEXT_CHUNK、短语 DF 等结构信号建边。提供混合检索管线（BM25+HNSW+PPR+cross-encoder+MMR）、CDC 增量同步（SQLite/PostgreSQL/MySQL）、韩语 Kiwi 形态分析，以及约 20 个 agent 工具（搜索、结构化聚合、会话中摄取、多轮导航）。可作 MCP server 接入 Claude Desktop，或以 LangChain retriever 集成。后端可选 SQLite/pgvector/Kuzu/Qdrant+MinIO 组合。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 默认索引路径零 LLM 调用、零基础设施，确定性建图
- 混合检索管线：BM25 + HNSW + PPR + cross-encoder + MMR
- CDC 实时数据库同步，支持 SQLite/PostgreSQL/MySQL
- 约 20 个 MCP agent 工具：搜索、结构化聚合、会话中摄取、多轮会话状态

## 适用场景

- 为 Claude 等 agent 提供可多轮探索的知识图谱检索
- 在对话中摄取新文档并从生产数据库增量同步
- 以 LangChain retriever 形式接入现有 RAG 链
- 基于引用标识（法条号/条款码）构建多跳 REFERENCES 边

## 场景标签

`Agent 记忆` `知识图谱` `RAG` · 领域:Agent 开发

## 证据(README 行号)

> L4: A knowledge graph + MCP tool server for LLM agents, with hybrid retrieval,
> L35: |single-shot retrieval by default|MCP tools for multi-turn exploration|

## 星数曲线

```mermaid
xychart-beta
    title "PlateerLab/synaptic-memory 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 32 --> 34
    line [33, 33]
```

2026-10-18 33 → 2026-10-26 33（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `fbc8a047d88b` · [字段定义](../../DATASET.md)*
