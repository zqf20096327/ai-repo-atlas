# TallyGov/Tally

⭐ 23 · TypeScript · 推送 2026-06-22 · [GitHub](https://github.com/TallyGov/Tally) · 组织维护

**面向代币持有者的 Solana/DeFi 治理提案信号看板**

Tally 监听 Snapshot 与 Realms 上的治理提案，将提案文本与元数据规范化后按重要性与紧迫度打分（1-10 分），并生成通俗语言摘要，按 watch/important/critical/routine 四种状态发布可排序看板。流程为 FETCH -> SCORE -> SUMMARIZE -> CLASSIFY -> DIGEST。它定位为优先级排序层而非投票应用或治理门户，面向持有人、运营者与治理观察者。基于 Claude Agent SDK 构建，用 Bun 运行，MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 从 Snapshot 和 Realms 拉取并规范化治理提案
- 按重要性与紧迫度对提案打分（1-10）并分四种状态
- 将治理文本转为通俗摘要看板

## 适用场景

- 追踪 Solana 与 DeFi 治理提案而不必逐篇阅读原文
- 快速识别影响国库、代币经济或治理权的紧急提案
- 用一份可扫读的看板替代提案信息流

## 场景标签

 · 领域:加密货币/DAO 治理

## 证据(README 行号)

> L3: **Governance signal board for Solana and DeFi proposals.**
> L8: Built with Claude Agent SDK
> L24: It is not a voting app and it is not trying to become a whole governance portal. It is a prioritization layer for p

## 星数曲线

```mermaid
xychart-beta
    title "TallyGov/Tally 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-31 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `447d915973c1` · [字段定义](../../DATASET.md)*
