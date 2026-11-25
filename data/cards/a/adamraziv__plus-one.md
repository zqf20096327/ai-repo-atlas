# adamraziv/plus-one

⭐ 10 · TypeScript · MIT · 推送 2026-09-17 · [GitHub](https://github.com/adamraziv/plus-one) · [官网](https://open.substack.com/pub/adamraziv/p/inside-plus-one-building-a-verifiable?r=24re3c&utm_campaign=post&utm_medium=web&showWelcomeOnShare=true) · 个人维护

**自托管的家庭财务 agent：情侣通过 Telegram 记账与查询**

面向情侣的自托管家庭财务 agent，以 Telegram 为生产渠道，另提供 HTTP inbound 入口。由 orchestrator 协调 query/accounting/budgeting 等专职 agent，支持自然语言账户与交易查询、多轮收支录入、预算提案与导入对账。写操作经 maker-checker 校验、幂等与只追加约束，PostgreSQL 约束为最终执行层；运行需 Node.js、pnpm、本地 PostgreSQL（Docker）与 LLM_API_KEY，Telegram 为可选入口。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- orchestrator 协调 query/accounting/budgeting 多 agent 的架构
- 写操作经策略校验、幂等、回读与 PostgreSQL 约束的 checked mutations
- Telegram 网关支持配对、webhook/polling、重放去重与优雅停机
- NDJSON 轮转日志排除消息正文、金额与凭证等敏感内容

## 适用场景

- 情侣在 Telegram 中通过对话记录收支并创建账户/分类
- 用自然语言查询家庭余额、交易与报表
- 导入账单流水并做重复匹配与对账、期末关账
- 制定家庭预算并获得校验后的方案比较

## 场景标签

`多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L7: Plus One is an open-source, self-hosted household finance agent for couples. The v0.3.1 production channel is Telegr
> L46: - an `LLM_API_KEY` for non-test runs
> L23: - natural-language account, balance, transaction, and governed reporting queries, plus checked budgeting workflows

## 星数曲线

```mermaid
xychart-beta
    title "adamraziv/plus-one 星数(近 2 点)"
    x-axis ["2026-10-23", "2026-11-25"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-10-23 10 → 2026-11-25 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 mid · 依据 README sha `9722eec12a06` · [字段定义](../../DATASET.md)*
