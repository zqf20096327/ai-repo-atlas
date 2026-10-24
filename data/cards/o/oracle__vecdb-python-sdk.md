# oracle/vecdb-python-sdk

⭐ 70 · Python · UPL-1.0 · 推送 2026-10-16 · [GitHub](https://github.com/oracle/vecdb-python-sdk) · [官网](https://docs.oracle.com/en/cloud/paas/autonomous-vector-database/vcapi/quickstart.html) · 组织维护

**在 Oracle AI Database 上构建向量搜索与 RAG 的 Python SDK**

Oracle 官方的 Python SDK，面向在 Oracle AI Database 上开发向量检索应用的开发者：提供语义/相似度搜索、向量与关系及空间过滤组合查询、RAG 与 AI agent 构建能力；支持集成 embeddings 或自带向量，默认自动创建向量索引，可调 HNSW 参数。向量与业务数据同库存储，避免引入独立向量数据库。要求 Python 3.10+、Oracle AI Database 23.26.3+ 与 ORDS 26.2.2+，通过 pip/uv 安装，配套示例应用与 Notebook。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | UPL-1.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 向量搜索与关系/空间/结构化过滤组合查询
- 集成 embeddings 生成，也支持自带向量
- 默认自动创建向量索引，可调 HNSW 参数
- 配套示例应用与可运行 Notebook（Oracle AI Developer Hub）

## 适用场景

- 在已有 Oracle 数据库上构建语义搜索而不引入独立向量库
- 构建 RAG 文档问答与 AI agent 应用
- 向量检索叠加地理空间与元数据过滤的应用

## 场景标签

`向量数据库` `RAG` `语义搜索` · 领域:知识与检索

## 证据(README 行号)

> L3: **Build vector search, RAG, and AI applications on Oracle AI Database - from Python.**
> L110: - 🔎 Run semantic and similarity search
> L112: - 🤖 Build RAG applications and AI agents

## 星数曲线

```mermaid
xychart-beta
    title "oracle/vecdb-python-sdk 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 69 --> 71
    line [70, 70]
```

2026-10-18 70 → 2026-10-24 70（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `abf17a85ffbf` · [字段定义](../../DATASET.md)*
