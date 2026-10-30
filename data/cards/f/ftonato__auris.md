# ftonato/auris

⭐ 21 · TypeScript · MIT · 推送 2026-04-13 · [GitHub](https://github.com/ftonato/auris) · [官网](https://deepwiki.com/ftonato/auris/) · 个人维护

**TypeScript 单仓 RAG 引擎：混合检索+可插拔适配器+追踪**

以 TypeScript monorepo 形式交付的领域无关 RAG 引擎，提供 Express REST API（/v1/query、/v1/index、/v1/health）。核心机制：稠密（ChromaDB）+稀疏（Elasticsearch/Typesense）混合检索经 RRF 融合，可选 Cohere 重排，LLM（默认 OpenAI GPT-4o）基于打包上下文生成带引用的回答；外部系统全部隔离在 hexagonal 端口之后，向量库/稀疏引擎/LLM 可替换而不改核心逻辑；每步管道输出 tracing spans，配置用 YAML+环境变量。限制：增量同步 worker 与 Weaviate/pgvector 为 Planned 状态，Embeddings 默认需 OpenAI key（否则为 stub）。

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

- 稠密+稀疏混合检索与加权 RRF 融合，可选 Cohere 交叉编码器重排
- hexagonal ports/adapters：向量库、稀疏引擎、LLM 均可替换
- 输入/输出 guardrails、HyDE 与多查询扩展、可插拔分块策略
- REST API、每步 tracing spans、Docker Compose 启动 Chroma 与 Elasticsearch

## 适用场景

- 团队搭建可替换后端、可观测的检索问答服务
- 在供应商变动时保持检索与 guardrails 逻辑稳定
- 通过 /v1/index 与文件摄取扩展构建本地知识问答

## 场景标签

`RAG` · 领域:知识与检索

## 证据(README 行号)

> L5: Domain-agnostic retrieval-augmented generation engine delivered as a TypeScript monorepo with an HTTP API.
> L7: Teams need retrieval, guardrails, and observability to stay coherent as vendors change; Auris isolates every externa

## 星数曲线

```mermaid
xychart-beta
    title "ftonato/auris 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-30 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `e5898db9b325` · [字段定义](../../DATASET.md)*
