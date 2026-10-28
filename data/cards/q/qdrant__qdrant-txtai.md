# qdrant/qdrant-txtai

⭐ 25 · Python · Apache-2.0 · 推送 2026-06-23 · [GitHub](https://github.com/qdrant/qdrant-txtai) · 组织维护

**将 Qdrant 向量数据库接入 txtai 的后端集成库**

为 txtai 语义搜索框架提供 Qdrant 向量数据库后端的 Python 库：安装后通过配置 backend 为 qdrant_txtai.ann.qdrant.Qdrant，即可用 Qdrant 存储与检索 txtai 生成的 embeddings。支持连接 Qdrant 服务器实例（Docker 启动），也支持 Qdrant Python client 1.1.1 起的本地内存/磁盘持久化模式用于测试与实验。可编程式或 YAML 配置使用，可配置连接细节与向量集合属性。面向构建语义搜索应用的开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 为 txtai 提供 Qdrant 向量存储后端
- 支持 Qdrant 服务器模式（Docker 部署）与本地内存/磁盘持久化模式
- 可通过 YAML 配置连接细节与集合内部属性

## 适用场景

- txtai 应用中用 Qdrant 作为向量存储后端
- CI/CD 自动化测试中使用本地内存存储
- 数据量超出单机时改用 Qdrant 集群存储 embeddings

## 场景标签

`向量数据库` · 领域:知识与检索

## 证据(README 行号)

> L28: Running the txtai application with Qdrant as vector storage requires launching
> L53:   backend: qdrant_txtai.ann.qdrant.Qdrant

## 星数曲线

```mermaid
xychart-beta
    title "qdrant/qdrant-txtai 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-28 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `09858dba5de5` · [字段定义](../../DATASET.md)*
