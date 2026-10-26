# MoonshotAI/CombiBench

⭐ 56 · Lean · MIT · 推送 2026-06-15 · [GitHub](https://github.com/MoonshotAI/CombiBench) · 组织维护

**组合数学自动定理证明基准：100 道 Lean 4 形式化题**

基于 Lean 4 形式化语言的组合数学评测基准，人工编制 100 道不同难度与知识层级的题目，来源覆盖 IMO（2000 年以来全部组合题，除一道依赖图形）、Brualdi 教材随机抽样 42 题、hackmath 网站初中级题 10 题及其他数学竞赛，用于评估自动定理证明系统的组合数学能力。托管 leaderboard，接收附带论文的评测结果。需 Python>=3.10 与 Lean>=4.15.0，评测流程依赖自行部署的 kimina-lean-server 与 LLM API（OpenAI/Anthropic/TogetherAI/Google），支持一阶段与两阶段评测。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 100 道人工编制的 Lean 4 组合数学题
- 题目来自 IMO、Brualdi 教材、APMO、USAMO 等多源
- 支持一阶段与两阶段评测，兼容定理证明与填空任务
- 托管 leaderboard 接收附论文的评测结果

## 适用场景

- 评测自动定理证明系统在组合数学上的能力
- 对比不同 LLM 在形式化数学证明中的表现
- 提交结果至公开榜单参与排名

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L3: CombiBench is the first benchmark focused on combinatorial problems, based on the formal language Lean 4. CombiBench
> L9: We collected all combinatorics problems from the official IMO problems since 2000, except for one problem that relie

## 星数曲线

```mermaid
xychart-beta
    title "MoonshotAI/CombiBench 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-25", "2026-10-26"]
    y-axis "stars" 54 --> 57
    line [55, 56, 56]
```

2026-10-18 55 → 2026-10-26 56（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `af1e3bf61880` · [字段定义](../../DATASET.md)*
