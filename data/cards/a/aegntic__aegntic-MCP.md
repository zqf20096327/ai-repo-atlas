# aegntic/aegntic-MCP

⭐ 10 · TypeScript · NOASSERTION · 推送 2026-11-27 · [GitHub](https://github.com/aegntic/aegntic-MCP) · 个人维护

**将 Obsidian 笔记库构建为多层 RAG 与知识图谱的 MCP 服务器**

面向 Obsidian 用户的知识库检索增强系统：将 markdown 笔记摄入知识库，通过六层检索架构（语义向量、Graphiti 知识图谱、NetworkX 图遍历、时间相关性、领域特化、元知识）加权融合输出查询结果；支持 27+ 实体类型与 40+ 关系类型的自动抽取，采用 Neo4j 与 Qdrant 双数据库（由安装脚本经 Docker 部署）。提供 CLI 与 MCP 服务器两种使用方式，可接入 Claude Code，需 Python 3.9+ 与 OpenAI API key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 六层加权融合的 RAG 检索架构（语义/图谱/遍历/时间/领域/元知识）
- 自动实体与关系抽取，Neo4j + NetworkX 双图架构
- 提供 6 个 MCP 工具接入 Claude Code
- CLI 支持 setup/ingest/query/status/server 子命令

## 适用场景

- 将个人 Obsidian 笔记库变成可对话检索的知识库
- 在 Claude Code 中通过 MCP 工具查询与搜索知识图谱
- 对科研或项目笔记做实体关系抽取与组织

## 场景标签

`RAG` `知识图谱` · 领域:知识与检索

## 证据(README 行号)

> L9: An elite Retrieval-Augmented Generation (RAG) system that transforms Obsidian vaults into AI-paired cognitive workfl
> L29: - **Claude Code Compatible**: Full Model Context Protocol server implementation
> L114: 2. **`query_rag`** - Query the elite RAG system with multi-layer retrieval


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 mid · 依据 README sha `6839707ac5a5` · [字段定义](../../DATASET.md)*
