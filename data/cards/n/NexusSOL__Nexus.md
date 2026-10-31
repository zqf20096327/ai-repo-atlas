# NexusSOL/Nexus

⭐ 22 · TypeScript · MIT · 推送 2026-06-22 · [GitHub](https://github.com/NexusSOL/Nexus) · 组织维护

**Solana 跨链桥资金流入监控台，用 Claude 判定可部署资金**

面向加密市场操盘者的 Solana 跨链桥资金监控控制台：读取 Solana 与 EVM 链之间的桥接资金流，计算净流入、稳定币占比、通道集中度与落地质量四类核心指标，过滤循环桥转、滞留库存与拥挤通道，输出 PROMOTE/WATCH/SUPPRESS/OUTFLOW 决策与告警。配置 ANTHROPIC_API_KEY 与 Wormhole API key 后运行，支持五种异常类型检测。以 TypeScript 实现，git clone 后 npm 安装并本地运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 核心指标：netUsd、stablecoinSharePct、routeConcentrationPct 与落地质量
- 五类异常检测：solana_ingress、deployable_stablecoin、route_concentration、roundtrip_churn、suspicious_timing
- 四项风险控制：稳定币质量门、通道集中度上限、往返churn过滤、落地质量过滤
- agent 输出 PROMOTE/WATCH/SUPPRESS/OUTFLOW 决策的实时控制台

## 适用场景

- 判断大额桥接转入是否为可快速部署的真实资金
- 跟踪哪些跨链通道正在承载进入 Solana 的可用资本
- 过滤循环桥转与滞留库存带来的监控噪音

## 场景标签

 · 领域:加密货币/链上数据分析

## 证据(README 行号)

> L30: Live operating view for Nexus: route leaderboard across cross-chain corridors, live bridge-flow feed, selected corr
> L153: ANTHROPIC_API_KEY=sk-ant-...

## 星数曲线

```mermaid
xychart-beta
    title "NexusSOL/Nexus 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-31 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `adf8189d9baa` · [字段定义](../../DATASET.md)*
