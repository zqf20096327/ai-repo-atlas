# qdrant/qdrant-haystack

⭐ 46 · Python · Apache-2.0 · 推送 2026-10-05 · [GitHub](https://github.com/qdrant/qdrant-haystack) · 组织维护

**将 Qdrant 向量数据库接入 Haystack 的文档存储集成库**

由 deepset 开发的 Python 集成库，将 Qdrant 向量数据库封装为 Haystack 的 QdrantDocumentStore，作为其他向量嵌入存储的就地替换。支持本地内存模式（:memory:，适合 CI/CD 测试）、磁盘持久化模式，以及 Qdrant Cloud 集群连接，本地与云端功能一致。注意：V2 实现已迁移至 deepset-ai/haystack-core-integrations 仓库，本仓库为 V1 版本。通过 pip 或 poetry 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- QdrantDocumentStore 作为其他向量存储的就地替换
- 支持本地内存/磁盘持久化模式（Qdrant client ≥1.1.1）
- 支持连接 Qdrant Cloud 集群，与本地实例功能一致

## 适用场景

- 在 Haystack RAG 管道中使用 Qdrant 作为文档存储
- 自动化测试中用内存模式快速运行
- 不想自管实例时连接 Qdrant Cloud

## 场景标签

`向量数据库` · 领域:知识与检索

## 证据(README 行号)

> L7: An integration of Qdrant vector database with Haystack
> L10: The library finally allows using Qdrant as a document store, and provides an in-place replacement

## 星数曲线

```mermaid
xychart-beta
    title "qdrant/qdrant-haystack 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 45 --> 47
    line [46, 46]
```

2026-10-18 46 → 2026-10-26 46（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `5db117e519e7` · [字段定义](../../DATASET.md)*
