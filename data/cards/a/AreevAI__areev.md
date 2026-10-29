# AreevAI/areev

⭐ 27 · Rust · Apache-2.0 · 推送 2026-10-25 · [GitHub](https://github.com/AreevAI/areev) · [官网](https://areev.ai/store) · 组织维护

**构建微垂直 AI 产品的开源引擎：记忆、工作流、人工审批与受治理改进**

面向为特定行业/团队构建聚焦型 AI 产品（如发票处理、对账）的开发者引擎。提供持久化内容寻址记忆、带分支/重试/审批的工作流执行（Areev Run）、CAL 上下文组装语言、假名化/脱敏策略、基于证据的改进回路（提议→评估→审批→可回滚），以及训练语料导出与 adapter 治理。可通过 Python/TypeScript/Rust 嵌入或 MCP 接入。示例用合成数据与模拟集成，无需模型 key 或账户。改进回路默认确定性分析器，Areev 不运行守护进程。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 运行→记录→提议→评估→审批→应用的受治理改进回路，支持回滚
- CAL 在 token 预算下组装模型上下文，优先级/摘要/可复用查询
- 假名化与匿名化策略（ingress/egress、审计模式、密封 vault、本地再水化）
- 内容寻址记忆存储，支持结构化/关键词/向量检索与版本追溯

## 适用场景

- 为发票处理、对账等行业流程构建带记忆的 AI agent
- 在敏感数据场景下对模型可见上下文做假名化管控
- 从 agent 执行历史导出语料并治理模型调优的晋升与回滚

## 场景标签

`Agent 框架` `Agent 记忆` `工作流自动化` · 领域:Agent 开发

## 证据(README 行号)

> L5: Areev Core is the **open-source engine behind every product in the
> L10: You bring the domain rules, integrations, and customer experience. Areev supplies
> L136: Use individual components with an existing agent, or use **Areev Run** for

## 星数曲线

```mermaid
xychart-beta
    title "AreevAI/areev 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-29"]
    y-axis "stars" 25 --> 28
    line [26, 27, 27]
```

2026-10-18 26 → 2026-10-29 27（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `f65139c961f1` · [字段定义](../../DATASET.md)*
