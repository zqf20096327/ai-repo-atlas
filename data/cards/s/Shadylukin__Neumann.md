# Shadylukin/Neumann

⭐ 74 · Rust · Apache-2.0 · 推送 2026-06-13 · [GitHub](https://github.com/Shadylukin/Neumann) · [官网](https://scrunchee.ai) · 个人维护

**Rust 统一数据库：关系表、图与向量在同一存储层**

用 Rust 编写的统一数据库，将关系表、图关系与向量嵌入存储在同一基于张量的存储层中，查询语言支持在单条语句内组合关系过滤、向量相似度（HNSW）与图遍历。提供语义共识层：并发写不同字段自动合并，冲突按几何方式分类。面向 AI 应用场景（RAG、Agent 记忆、知识图谱、图权限），内置嵌入存储、LLM 语义缓存与加密密钥库。提供 Python/TypeScript SDK 与 Web 控制台。当前为 pre-1.0（v0.4.0），单节点已生产就绪，多节点共识仍需真实场景验证。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 单条语句组合关系过滤+向量相似度+图遍历
- 语义共识层：并发写不同字段自动合并（52M 冲突检查/秒）
- 内置嵌入存储、LLM 语义缓存与加密密钥库
- 提供 Python/TypeScript SDK 与 Web 控制台

## 适用场景

- RAG 应用中存储带嵌入与关系的文档并做语义搜索
- Agent 跨会话向量召回对话历史并缓存 LLM 调用
- 知识图谱中按语义相似度查找实体
- 基于图的访问控制，查询结果按请求者身份过滤

## 场景标签

`向量数据库` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L8: Neumann stores your tables, graphs, and vectors in one place.
> L44: **AI-native by design.** Built-in embedding storage, semantic caching for
> L50: **RAG** -- Store documents with embeddings and relationships. Semantic

## 星数曲线

```mermaid
xychart-beta
    title "Shadylukin/Neumann 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 73 --> 75
    line [74, 74]
```

2026-10-18 74 → 2026-10-27 74（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `8b59b62eafc5` · [字段定义](../../DATASET.md)*
