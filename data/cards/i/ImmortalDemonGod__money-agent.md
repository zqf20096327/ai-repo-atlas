# ImmortalDemonGod/money-agent

⭐ 36 · Python · MIT · 推送 2026-07-26 · [GitHub](https://github.com/ImmortalDemonGod/money-agent) · [官网](https://onehonestdollar.com/) · 个人维护

**自主赚钱 agent 的接地验证实验：独立校验器核验 agent 声明**

一项关于 agent 声明可验证性的研究项目：沙箱中的自主 agent 以 25 美元启动资金尝试赚钱，并将其声明写入 MONEY_LOG.md；一台 agent 无法访问的独立机器上的校验器从真实 Stripe API 与卡流水计算事实写入 ledger/truth.json，两者差异即研究主题。v1 已结束，结果为经核验的 0 美元；v2 完成沙箱搭建待启动。仓库包含测试模拟脚本、案例研究与完整运行档案，裸 clone 无独立校验器时以弱模式（tripwire）运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- agent 声明与校验器事实分离，账本由构造保证优先
- tests/sim.sh 提供离线两车道仿真矩阵，无需 Stripe 账号或密钥
- v1 结论 $0.00 已验证，完整运行档案存于 archive/run-001/
- 两项发现（reach 约束、验证剧场）驱动 v2 设计

## 适用场景

- 研究自主 agent 声明的带外验证方法
- 复现并审查 claim-vs-fact 漂移的实验证据
- 作为 agent 评估/安全课程或讨论的案例材料

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L36: **The agent produces CLAIMS. A verifier it cannot invoke produces FACTS. The gap between them is the whole subject.
> L38: The agent, sandboxed with no credentials, narrates CLAIMS into MONEY_LOG.md. A verifier on a separate machine the a

## 星数曲线

```mermaid
xychart-beta
    title "ImmortalDemonGod/money-agent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 35 --> 37
    line [36, 36]
```

2026-10-18 36 → 2026-10-29 36（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `65296f4ea164` · [字段定义](../../DATASET.md)*
