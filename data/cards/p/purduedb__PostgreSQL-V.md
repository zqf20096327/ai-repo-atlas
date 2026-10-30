# purduedb/PostgreSQL-V

⭐ 26 · C · 推送 2026-10-17 · [GitHub](https://github.com/purduedb/PostgreSQL-V) · 组织维护

**Purdue 开发的 PostgreSQL 向量相似性搜索扩展，快速向量检索**

由 Purdue Database Group 开发的集成式向量数据库系统，在 PostgreSQL 内提供快速向量相似性搜索。架构上将向量索引与 PostgreSQL 核心引擎解耦，直接复用原生向量索引库，并以轻量一致性机制处理解耦引入的索引不一致问题。完整兼容 pgvector API，可作为其替换品直接使用；当前仓库为 CIDR 论文投稿所用原型版本。安装需先装 PostgreSQL，再编辑 install_pgvector.sh 指定 pg_config 路径后编译安装扩展。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 向量索引与 PostgreSQL 核心引擎解耦的架构设计
- 通过 IndexAmRoutine 实现与 pgvector 完全兼容，可作 drop-in 替换
- 轻量一致性机制处理索引不一致问题

## 适用场景

- 在 PostgreSQL 中做向量相似性搜索，支撑 RAG 检索
- 从 pgvector 迁移以获得不同的向量索引架构
- 研究解耦式向量数据库的设计与实验

## 场景标签

`向量数据库` · 领域:知识与检索

## 证据(README 行号)

> L6: **PostgreSQL-V** is a new integrated vector database system developed by **Purdue Database Group** that enables fast
> L8: Unlike prior systems (e.g., pgvector) that inherits legacy overhead by reusing PostgreSQL’s page-oriented structure,

## 星数曲线

```mermaid
xychart-beta
    title "purduedb/PostgreSQL-V 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-28", "2026-10-30"]
    y-axis "stars" 24 --> 27
    line [25, 26, 26]
```

2026-10-18 25 → 2026-10-30 26（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `e1af2ff749cc` · [字段定义](../../DATASET.md)*
