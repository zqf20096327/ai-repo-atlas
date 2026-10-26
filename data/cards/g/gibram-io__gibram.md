# gibram-io/gibram

⭐ 106 · Go · MIT · 推送 2026-06-07 · [GitHub](https://github.com/gibram-io/gibram) · [官网](https://docs.gibram.io) · 组织维护

**内存态知识图谱服务器：为 RAG/GraphRAG 提供图+向量检索**

GibRAM 是一个在内存中运行的知识图谱服务器，面向 RAG/GraphRAG 工作流：在同一结构中存储命名实体、关系、文档块及其嵌入，支持关系遍历与语义搜索两种检索方式。数据存于 RAM 并可配置 TTL，定位为短生命周期的分析与探索，而非持久化存储。提供二进制脚本安装、Docker 运行与 Python SDK（GibRAMIndexer），SDK 中 chunker、extractor、embedder 组件可替换，示例含 OpenAIExtractor。默认监听 6161 端口。

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

- 实体、关系、文档块与嵌入存储于同一内存结构
- 图遍历检索与向量语义搜索并存
- 可配置 TTL 的内存态短时数据生命周期
- Python SDK 的 chunker/extractor/embedder 组件可替换

## 适用场景

- 为 RAG 应用检索与查询主题相关的上下文片段
- GraphRAG 风格的文档索引与关联查询
- 需要实体关系遍历补充向量检索遗漏场景的短期分析

## 场景标签

`知识图谱` `向量数据库` · 领域:知识与检索

## 证据(README 行号)

> L9: GibRAM is an in-memory knowledge graph server designed for retrieval augmented generation (RAG) workflows. It combin
> L15: - Python SDK: Provides a GraphRAG style workflow for indexing documents and running queries with minimal code. Comp

## 星数曲线

```mermaid
xychart-beta
    title "gibram-io/gibram 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 105 --> 107
    line [106, 106]
```

2026-10-18 106 → 2026-10-26 106（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `e0f36d3f1126` · [字段定义](../../DATASET.md)*
