# Marbacj/SQL-Reconciliation-Agent

⭐ 24 · Python · NOASSERTION · 推送 2026-10-24 · [GitHub](https://github.com/Marbacj/SQL-Reconciliation-Agent) · 个人维护 · 中文 README

**自然语言 SQL 对账平台：非技术人员对话完成跨表差异核对**

基于 LangGraph 的多 Agent SQL 对账平台，面向不写 SQL 的业务人员：输入自然语言对账请求，经意图路由、任务分解、并行 SQL 执行、SQL 自动修复（最多 3 次重试）后输出差异报告与根因分析。机制包括 ReAct 推理循环、RAG Schema 检索、AST 级只读安全拦截、三层记忆与失败案例自进化。适配 SQLite/MySQL/ClickHouse/Hive，提供 CLI、FastAPI Web UI 与 Docker Compose 部署，需配置外部 LLM API Key（默认 DeepSeek）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- LangGraph 状态机：Route → Plan → Act → Observe → Reflect 闭环与 8 类意图识别
- SQL 执行失败自动反馈 LLM 重写，最多重试 3 次
- AST 级拦截 DDL/DML 只读执行，JWT 多租户认证
- RAG Schema 检索 + 实时 PRAGMA 查询定位相关表

## 适用场景

- 让业务人员用一句话核对直播 GMV 与订单金额的差异
- 跨表、跨库数据对账并自动生成差异报告
- 对查询结果做同环比、趋势与 TopN 分析

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L14: **用自然语言驱动 SQL 对账 — 不写一行 SQL，自动完成数据差异发现**
> L23: SQL Reconciliation Agent 是一个**企业级 Multi-Agent 对账平台**，基于 **ReAct 推理 + LangGraph 编排 + RAG Schema 检索**，让非技术人员也能通过自然语言完
> L26: 用户自然语言 → Intent路由 → Plan分解 → 并行SQL执行 → SQL自动修复 → 差异比对 → Markdown报告

## 星数曲线

```mermaid
xychart-beta
    title "Marbacj/SQL-Reconciliation-Agent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-29 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `8a88448108a9` · [字段定义](../../DATASET.md)*
