# tteon/seocho

⭐ 59 · Python · MIT · 推送 2026-10-25 · [GitHub](https://github.com/tteon/seocho) · [官网](https://seocho.blog/) · 个人维护

**本体对齐的 agent 图记忆中间件：SDK+运行时+可复现实验**

面向开发者的 Python SDK 与可选 HTTP 运行时，用同一本体串联文档索引与基于图的回答：定义实体/关系/约束，摄取数据，检查 agent 回答背后的图证据。提供抽取校验、schema 感知查询、可复现 run/sweep 实验与保存运行对比、本地 dashboard。基线为 DozerDB/Neo4j 图数据库与 OpenAI Agents SDK，首跑需 Bolt 端点与模型 provider key；自述 alpha 阶段，运行完成仅为执行证据而非正确性证明。

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

- 同一本体驱动文档索引与图落地回答（GraphRAG）
- 可复现 run/sweep 实验与离线 saved-run 对比
- HTTP 运行时带策略检查，供 agent 调用
- 本地 dashboard 与可视化报告浏览运行证据

## 适用场景

- 为 agent 构建可审计的图记忆并追溯回答证据
- 对比索引或模型变更前后的问答效果
- 用自有语料运行可复现的 GraphRAG 实验

## 场景标签

`知识图谱` `Agent 记忆` `RAG` · 领域:Agent 开发

## 证据(README 行号)

> L5: **Ontology-aligned middleware for agentic graph memory.**
> L16: SEOCHO connects document indexing and graph-grounded answering through the same
> L20: It ships as a **Python SDK** and an optional **HTTP runtime**. You own the data,

## 星数曲线

```mermaid
xychart-beta
    title "tteon/seocho 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 58 --> 60
    line [59, 59]
```

2026-10-18 59 → 2026-10-27 59（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `53c2d32d1093` · [字段定义](../../DATASET.md)*
