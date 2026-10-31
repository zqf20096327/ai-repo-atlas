# Astrix-Labs/papez

⭐ 31 · Python · AGPL-3.0 · 推送 2026-09-07 · [GitHub](https://github.com/Astrix-Labs/papez) · [官网](https://papez.ai) · 组织维护

**给 AI agent 的因果图记忆引擎，MCP 服务形式提供**

面向 AI agent 的记忆层开源库：将记忆条目按 relevance × connectivity × reactivation 乘积公式打分，连成因果图，并在低分、孤立且未固定等条件同时满足时执行主动遗忘（STORE→ACTIVE→DORMANT→FADING→PRUNED 生命周期）。核心为纯 Python 内存因果图引擎（可选 JSON 持久化，无数据库依赖），内置 stdio MCP server，暴露 memory_store/recall/search/traverse 等 14 个工具；可选 extras 接入 OpenAI/本地 embeddings 与 Anthropic 做因果推断。LoCoMo 冻结协议下报 85.55 分。Postgres 等后端与 REST API 属于另行托管的商业产品，不在本包内。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三力乘积评分（relevance×connectivity×reactivation）与主动遗忘生命周期
- stdio MCP server 提供 14 个记忆工具（store/amend/recall/traverse/explain 等）
- 无数据库依赖，可选 JSON 持久化与本地 embeddings（无需 API key）
- memory_amend 修正链 SUPERSEDES 旧记忆并保留审计

## 适用场景

- 给我的 Claude/LLM agent 加上带因果推理的长期记忆
- 让 agent 记忆随时间衰减与主动遗忘，避免上下文膨胀
- 通过 MCP 工具遍历与解释记忆间的因果关系

## 场景标签

`Agent 记忆` `知识图谱` · 领域:Agent 开发

## 证据(README 行号)

> L12: > Papez doesn't just remember what happened; it remembers why. A scoring engine + causal graph + lifecycle manager 
> L30: This package (`papez`) is the core library: an in-memory causal graph engine with optional JSON persistence, plus a

## 星数曲线

```mermaid
xychart-beta
    title "Astrix-Labs/papez 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 30 --> 32
    line [31, 31]
```

2026-10-18 31 → 2026-10-31 31（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `338a054fcb27` · [字段定义](../../DATASET.md)*
