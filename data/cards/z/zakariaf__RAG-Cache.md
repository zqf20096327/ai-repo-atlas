# zakariaf/RAG-Cache

⭐ 13 · Python · 推送 2025-12-02 · [GitHub](https://github.com/zakariaf/RAG-Cache) · 个人维护

**LLM 查询缓存层：精确+语义匹配降低 API 成本与延迟**

位于应用与 LLM 提供商（OpenAI/Anthropic）之间的缓存服务：先查 Redis 精确匹配（约 1ms），再查 Qdrant 向量库语义匹配（约 450ms，相似度阈值可配），均未命中才调用 LLM API（约 8.5s）。以 FastAPI 服务形式提供 REST 查询端点，附带指标与 Prometheus 端点、Docker Compose 部署。需 Python 3.11、Docker 与 OpenAI API key，Anthropic key 可选。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Redis 精确匹配 + Qdrant 语义匹配两级缓存
- 语义相似度阈值与缓存 TTL 可配置
- REST API 与 Prometheus 格式指标端点
- Docker Compose 开发与生产部署配置

## 适用场景

- 高重复度问答场景下减少 LLM API 调用费用
- 降低重复查询的响应延迟
- 减少对外部 LLM API 的依赖以提升可靠性

## 场景标签

 · 领域:LLM 基础设施/缓存

## 证据(README 行号)

> L3: A high-performance caching layer for Large Language Model (LLM) queries with exact and semantic matching capabilitie
> L7: RAG Cache sits between your application and LLM providers (OpenAI, Anthropic) to:
> L16: User Query → Exact Match (Redis) → Semantic Match (Qdrant) → LLM (if needed)

## 星数曲线

```mermaid
xychart-beta
    title "zakariaf/RAG-Cache 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 12 --> 14
    line [13, 13]
```

2026-10-18 13 → 2026-10-31 13（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `0a36b8a6f3b0` · [字段定义](../../DATASET.md)*
