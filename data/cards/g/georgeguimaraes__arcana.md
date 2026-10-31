# georgeguimaraes/arcana

⭐ 342 · Elixir · Apache-2.0 · 推送 2026-10-29 · [GitHub](https://github.com/georgeguimaraes/arcana) · [官网](https://hexdocs.pm/arcana) · 个人维护

**可嵌入 Elixir/Phoenix 应用的 RAG 库，含 agentic 流水线与仪表盘**

面向已有 Ecto Repo 的 Phoenix 应用的嵌入式 RAG 库：文档、分块、向量与知识图谱均存于现有 Postgres（pgvector），无需独立向量数据库或编排服务。提供三种使用形态：单次调用的 search/ask（含查询重写、混合检索、重排序）、可组合步骤的 Pipeline、由 LLM 选工具的 Agentic Loop。默认嵌入与重排序通过 Bumblebee 本地运行（EXLA/EMLX/Torchx），LLM 可切换 OpenAI、Anthropic、Z.ai 等。附 LiveView 仪表盘与评测指标（MRR/Recall/Hit）。以 mix 依赖安装，Apache-2.0 许可。

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

- 数据全部存于现有 Postgres + pgvector，无新增基础设施
- 三种模式：ask/search、可组合 Pipeline、LLM 驱动 Loop
- 默认嵌入与 cross-encoder 重排序本地运行，LLM 提供商可插拔
- GraphRAG（实体抽取、Leiden 社区检测）与 LiveView 仪表盘

## 适用场景

- 在 Phoenix 应用中直接加入向量检索与问答，不另建服务
- 构建多跳/开放式问题的 agentic RAG 应用
- 通过可替换 behaviour 定制检索、重排序与回答步骤

## 场景标签

`RAG` · 领域:知识与检索

## 证据(README 行号)

> L5: An embeddable RAG library for Elixir and Phoenix. Arcana lets you add vector search, knowledge graphs, and LLM-drive
> L17: - **Local-first by default.** Embeddings run on Bumblebee with EXLA, EMLX (Apple Silicon), or Torchx. The cross-enc

## 星数曲线

```mermaid
xychart-beta
    title "georgeguimaraes/arcana 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-28", "2026-10-31"]
    y-axis "stars" 340 --> 343
    line [341, 342, 342]
```

2026-10-18 341 → 2026-10-31 342（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 mid · 依据 README sha `454f51144e19` · [字段定义](../../DATASET.md)*
