# jonortega20/fantasybot

⭐ 31 · Python · 推送 2026-09-02 · [GitHub](https://github.com/jonortega20/fantasybot) · 个人维护

**LALIGA Fantasy 自动化代理：读行情、竞价、卖人、排阵**

Python 标准库实现的 LALIGA Fantasy 代理：通过游戏非官方 API 与 futbolfantasy.com 读取阵容、市场与价值走势，执行竞价、出售、违约金条款买断和排阵等操作。提供确定性决策代理（agent 命令出计划，--execute 才执行；买断不自动，留任务确认），并可选部署在 Hermes Agent 运行时上（LLM 为 Claude，配持久记忆、自注册 cron 与 SOUL/USER/MEMORY 文件）。带 SSE 实时监控的本地 Web UI（绑定 127.0.0.1），决策命令支持 --json 输出。注意：非官方 API，可能违反游戏条款。

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

- 确定性代理：审查-决策-执行（排阵、竞价、出售、条款买断）
- 可选 Hermes LLM 大脑：持久记忆（MEMORY.md）、自主定时任务与分级自治配置
- 实时监控 Web UI，通过 events.jsonl/SSE 渲染操作时间线
- 决策命令支持 --json 供程序化消费

## 适用场景

- 每天自动审查球队、排阵并在市场竞价
- 最后一刻竞价策略：bid-plan 由 cron 在截止时出价
- 在 VPS 上 7x24 自主运营 Fantasy 球队
- 通过 Web UI 实时监督代理的读取与操作

## 场景标签

 · 领域:游戏自动化

## 证据(README 行号)

> L3: An agent for **LALIGA Fantasy**: it connects to the game's (unofficial) API and to
> L69: own reminders— fantasybot is deployed on top of
> L109: > This applies to the **deterministic agent** (`fantasybot agent`). When it's

## 星数曲线

```mermaid
xychart-beta
    title "jonortega20/fantasybot 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-27"]
    y-axis "stars" 29 --> 32
    line [30, 31, 31]
```

2026-10-18 30 → 2026-10-27 31（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `9fbb5aaec2df` · [字段定义](../../DATASET.md)*
