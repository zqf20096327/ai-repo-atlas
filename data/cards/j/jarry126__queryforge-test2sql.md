# jarry126/queryforge-test2sql

⭐ 19 · Python · Apache-2.0 · 推送 2026-09-03 · [GitHub](https://github.com/jarry126/queryforge-test2sql) · 个人维护 · 中文 README

**生产级 Text-to-SQL 服务：自然语言转安全可执行 SQL 并回答**

基于 FastAPI + LangGraph + RAG 的 Text-to-SQL 后端服务：将自然语言问题转换为仅允许单条 SELECT 的 SQL（sqlglot 解析、拦截 DDL/DML、自动 LIMIT），在只读连接上执行并返回自然语言回答。内置 schema/few-shot/docs 三类语料检索（pgvector + pg_jieba，可切 Elasticsearch）、双层缓存、限流熔断、Langfuse 追踪与 Prometheus/Grafana 监控，基于 CSpider 做 Execution Accuracy 评测；配套独立 React 前端，支持 Docker 与 Kubernetes 部署。面向做企业数据问答或 Text-to-SQL 工程化落地的开发者。

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

## 能力要点

- SQL Guard 仅允许单条 SELECT，禁 DDL/DML，自动注入 LIMIT，只读执行沙箱
- schema/few-shot/docs 三类 RAG 语料，支持向量+关键词检索、RRF 融合与 rerank
- 限流、并发闸门、熔断、重试、双层缓存等生产韧性机制
- 基于 CSpider 的 Execution Accuracy 评测与 RAG 消融实验，附实验记录

## 适用场景

- 企业内部数据问答 / BI 场景的自然语言查数
- 研究或二次开发生产级 Text-to-SQL 链路
- LangGraph + RAG 生产部署（限流、监控、追踪）的参考实现

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L3: 把自然语言问题转成**安全、可执行**的 SQL，并返回自然语言回答。链路可控、可追踪、可监控，
> L17: - **SQL 安全**：SQL Guard 只允许单条 SELECT，拦截 DDL/DML，自动 LIMIT，配合只读执行与超时控制。

## 星数曲线

```mermaid
xychart-beta
    title "jarry126/queryforge-test2sql 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-31 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `708614bac396` · [字段定义](../../DATASET.md)*
