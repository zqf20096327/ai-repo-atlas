# krukah/robopoker

⭐ 226 · Rust · MIT · 推送 2026-10-25 · [GitHub](https://github.com/krukah/robopoker) · [官网](https://robopoker.io) · 个人维护

**Rust 从零实现超人类级扑克 AI：CFR 求解、抽象与对战引擎**

以 12 个单一职责 crate 组成的 Rust 扑克 AI 实现，寻求与 Pluribus 功能对齐：纳秒级手牌评估、基于 EMD/Sinkhorn 最优传输的层级 k-means 抽象、游戏无关的 MCCFR 框架（可插拔 regret/policy/sampling）、深度受限与安全子博弈实时重解、AIVAT 方差缩减与 PostgreSQL 持久化。已在 crates.io 发布，含短牌/六人变体与 OpenTelemetry 遥测；训练需 16 vCPU/120 GB，对 Slumbot 实测 −13.1 bb/100。前端闭源。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 游戏无关 MCCFR 框架，在 Kuhn/Leduc/RPS 上以闭式均衡验证
- Sinkhorn/Greenkhorn 最优传输与层级 k-means 手牌抽象
- 深度受限 + 多世界安全子博弈实时重解
- 12 个 crate 全部发布至 crates.io，各层可独立复用

## 适用场景

- 研究和复现 Pluribus 式多人扑克 AI 流水线
- 复用其中的手牌评估、k-means、最优传输等独立算法 crate
- 搭建扑克求解与分析后端（含 PostgreSQL 持久化与遥测）

## 场景标签

 · 领域:博弈 AI/算法库

## 证据(README 行号)

> L8: A Rust implementation of superhuman-scale poker AI, seeking functional parity with Pluribus¹ — hand evaluation, opti
> L52: - `mccfr` — game-agnostic `CfrEncoder` → `Solver` → `Tree`, external sampling, dynamic tree construction
> L135: |`mccfr`|🟢|Game-agnostic MCCFR framework with pluggable regret/policy/sampling|

## 星数曲线

```mermaid
xychart-beta
    title "krukah/robopoker 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 225 --> 227
    line [226, 226]
```

2026-10-18 226 → 2026-10-26 226（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `42a5ead64605` · [字段定义](../../DATASET.md)*
