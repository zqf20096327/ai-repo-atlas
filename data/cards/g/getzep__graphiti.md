# getzep/graphiti

⭐ 31,970 · Python · Apache-2.0 · 推送 2026-10-17 · [GitHub](https://github.com/getzep/graphiti) · [官网](https://help.getzep.com/graphiti) · 组织维护

**为 AI Agent 构建可查询的时序知识图谱框架**

Graphiti 是构建和查询时序上下文图谱的开源框架，面向处理动态数据的 AI Agent。事实带时间有效期窗口、追溯至原始数据（episodes），支持 Pydantic 定义或从数据涌现的本体，新数据增量集成无需全图重算，检索采用语义嵌入+BM25 关键词+图遍历的混合方式。图数据库后端支持 Neo4j、FalkorDB、Amazon Neptune、Kuzu（已弃用），默认使用 OpenAI 做推理与嵌入，另附 MCP server 实现。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 动量与使用信号

- 维护:`active` — 距上次 push 0.6 天,年发版 38,64 位贡献者
- 涨星:近 1 天 **+80**(自 20261016 起算)
- 安装:pypi 包 `graphiti-core` 月下载 619,128
- 平台:WINDOWS · 协议:OPENAI-API / MCP / OLLAMA

## 能力要点

- 事实带时间有效期窗口，历史查询无需全图重算
- 混合检索：语义嵌入 + BM25 关键词 + 图遍历
- 增量图构建，支持规定式与习得式本体（Pydantic 模型）
- 提供 MCP server，供 AI 助手调用图谱能力

## 适用场景

- 为 AI Agent 构建随交互持续演化的知识图谱
- 对频繁变化的数据做时间点查询与事实失效追踪
- 替代静态文档切片的 RAG，做结构化上下文检索

## 场景标签

`知识图谱` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L27: Graphiti is a framework for building and querying temporal context graphs for AI agents. Unlike static knowledge gr
> L143: - Neo4j 5.26 / FalkorDB 1.1.2 / Amazon Neptune Database Cluster or Neptune Analytics Graph + Amazon OpenSearch
> L165: pip install graphiti-core

---
*卡片 v1 · prompt 1.4 · 生成 2026-10-18 · 置信度 high · 依据 README sha `81bafdcd5ef9` · [字段定义](../../DATASET.md)*
