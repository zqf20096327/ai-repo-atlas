# zilliztech/milvus-skill

⭐ 45 · Apache-2.0 · 推送 2026-03-24 · [GitHub](https://github.com/zilliztech/milvus-skill) · 组织维护

**教 LLM 用 pymilvus 操作 Milvus 向量库的 agent 技能**

由 Zilliz 团队维护的 agent skill，内容为 SKILL.md 主定义加 references/ 目录下的分领域参考文档，教 LLM 通过 pymilvus 操作 Milvus 向量数据库：连接（Milvus Lite/Standalone/Cluster/Zilliz Cloud）、集合与 schema 管理、向量增删改查、混合检索、BM25 全文检索、索引管理、分区、数据库与 RBAC，以及 RAG 等常见模式。以 Claude Code skill 命令安装，要求 Python 3.8+ 与 pymilvus。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- SKILL.md + 8 个分领域参考文档（collection/vector/index/partition/database/user-role/patterns）
- 支持向量 CRUD、混合检索（RRF/加权）、BM25 全文检索
- 覆盖 Milvus Lite/Standalone/Cluster 与 Zilliz Cloud 的连接
- 含 RAG、语义检索等常见模式文档

## 适用场景

- 让 Claude Code 等 agent 代我执行 Milvus 数据库操作
- 为 RAG/语义检索场景搭建和查询 Milvus 集合
- 需要 agent 处理 Milvus 索引、分区与 RBAC 管理

## 场景标签

`向量数据库` · 领域:知识与检索

## 证据(README 行号)

> L3: An agent skill that teaches LLMs how to use pymilvus to operate Milvus vector database.
> L17: ## Install as Claude Code Skill

## 星数曲线

```mermaid
xychart-beta
    title "zilliztech/milvus-skill 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 44 --> 46
    line [45, 45]
```

2026-10-18 45 → 2026-10-27 45（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `12a883aea3a7` · [字段定义](../../DATASET.md)*
