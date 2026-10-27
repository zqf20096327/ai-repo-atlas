# AI-Buddy-Catalyst-Labs/insta_rag

⭐ 28 · Python · MIT · 推送 2025-11-25 · [GitHub](https://github.com/AI-Buddy-Catalyst-Labs/insta_rag) · [官网](https://pypi.org/project/insta-rag) · 组织维护

**配置驱动的 Python RAG 管道库，简化向量与知识图谱检索构建**

模块化的配置驱动 Python 库，把文档处理、语义分块、嵌入、混合检索（向量+BM25）、HyDE 查询改写与可选重排（如 Cohere）封装在统一 Client 之后。向量侧用 Qdrant 存向量、MongoDB 存内容；另提供基于 Neo4j 与 Graphiti 的 Graph RAG 客户端，支持实体/关系抽取、多租户 group_id 与多级删除；还可配合 Celery/Redis 做异步文档处理，并提供 FastAPI 集成示例与可选 CLI。面向希望以配置方式快速搭建 RAG 管道的开发者。README 标注 Beta。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 语义分块、向量+BM25 混合检索、HyDE 与可选重排的统一客户端
- 基于 Neo4j/Graphiti 的 Graph RAG，支持实体关系抽取、多租户命名空间与多级删除
- Celery/Redis 异步文档处理与 worker 水平扩展
- Qdrant 存向量 + MongoDB 存内容的混合存储

## 适用场景

- 用配置而非手写管线搭建生产 RAG 检索服务
- 构建基于知识图谱的实体关系查询与发现
- 用 Celery 异步处理大文档抽取并监控任务进度

## 场景标签

`RAG` `知识图谱` · 领域:知识与检索

## 证据(README 行号)

> L12: Insta RAG (a.k.a. **insta_rag**) is a **modular, configuration‑driven** Python library for building **advanced RAG 
> L26: Most RAG stacks feel like soldering a radio: a tangle of chunkers, embedders, retrievers, rerankers, and caches. **

## 星数曲线

```mermaid
xychart-beta
    title "AI-Buddy-Catalyst-Labs/insta_rag 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 27 --> 29
    line [28, 28]
```

2026-10-18 28 → 2026-10-27 28（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `5b4c0d919fe3` · [字段定义](../../DATASET.md)*
