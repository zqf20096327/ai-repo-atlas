# JordyZomer/lemmalog

⭐ 340 · Rust · MIT · 推送 2026-10-01 · [GitHub](https://github.com/JordyZomer/lemmalog) · 个人维护

**面向 LLM agent 记忆的 Datalog 演绎数据库引擎，附 MCP 服务器**

Rust 实现的分层 Datalog 引擎，作为 LLM agent 的记忆层使用：LLM 在摄取边界抽取事实三元组，规则推导闭包、时间投影、矛盾候选与相关性扩散；每条事实携带指向来源 episode 的溯源，对话轮次间增量更新派生视图。提供 REPL、快照持久化、实体消解、混合检索（BM25+图/实体加权）与 what_if 假设推演。通过 MCP 服务器（12 个工具）接入 Claude Code / Kimi CLI，亦可经 headless CLI 操作同一快照；附通用 agent skill（SKILL.md）与 LongMemEval 基准示例。限制：MCP server 与 CLI 持有独立进程内副本，不可同时双写；部分引擎能力（leapfrog triejoin、DBSP）标注为未来阶段。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 分层 Datalog：negation-as-absence、seminaive 不动点、负增量重算
- 每条事实带溯源，`why()` 输出带环保护的证明树
- MCP server（12 个工具）供 Claude Code / Kimi CLI 作为共享记忆使用
- 实体消解（LLM 提议 alias + Datalog 闭包推导，冲突升级不合并身份）与 what_if 假设推演

## 适用场景

- 让长程调查、调试、审计类 agent 用演绎数据库做工作记忆
- agent 记忆需可验证溯源（每个结论可回查来源 episode）的场景
- 知识更新类问答：对既有记忆做时间投影与增量更新而非重新推理

## 场景标签

`Agent 记忆` `知识图谱` · 领域:Agent 开发

## 证据(README 行号)

> L3: A Datalog engine for LLM agent memory. This repo contains the engine
> L8: The thesis: **an agent's memory should be a deductive database** — the
> L46: |MCP server (`--features mcp`): the engine as tools for Claude Code / Kimi CLI|✅|

## 星数曲线

```mermaid
xychart-beta
    title "JordyZomer/lemmalog 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-21"]
    y-axis "stars" 339 --> 341
    line [340, 340]
```

2026-10-18 340 → 2026-10-21 340（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `6e4694d946d3` · [字段定义](../../DATASET.md)*
