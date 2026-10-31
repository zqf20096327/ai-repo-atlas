# DarkHater01/slopbench

⭐ 15 · JavaScript · MIT · 推送 2026-10-30 · [GitHub](https://github.com/DarkHater01/slopbench) · [官网](https://darkhater01.github.io/slopbench/) · 个人维护

**度量 LLM 编码 agent 代码冗余的基准：pass@1 与 inflation 双指标**

面向模型选型与 agent 工具评估的代码基准：对每个模型报告 pass@1（能否解题）与 inflation（生成 LOC ÷ 参考解 LOC），并以 ponytail Δ 度量 minimalism 提示词能削减多少行。当前跑 OpenCode Zen 免费层的 8 个模型，每个任务跑 3 次重复，两种 harness（单次补全与真实 OpenCode CLI agent）。生成代码在无网络的 Docker 沙箱中评分，参考解在仓库内手写、可通过 PR 争议修改。每日由 GitHub Actions 重新生成快照并提交到 data/。限制：5 个 Python 任务，LOC 可被博弈，非代码质量指标。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- inflation = 生成 LOC ÷ 参考解 LOC，仅在 pass@1 ≥ 0.6 时计入
- 双 harness：chat 单补全与真实 OpenCode CLI agent 沙箱运行
- 沙箱隔离：无网络、只读根文件系统、非 root、512MB 内存、50 秒超时
- 参考解在仓库内公开且可通过 PR 争议修改

## 适用场景

- 比较代码模型解题时的代码冗余程度
- 评估 minimalism 系统提示词能否减少生成行数
- 引用可复现的公开快照数据讨论模型行为

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L7: **Code benchmarks measure whether a model solves the task. None measure how much code it wastes.**
> L21: `inflation = LOC generated ÷ LOC of the reference solution`
> L114: runner/run.js        model × task × variant × rep → provider → Docker sandbox → data/raw.json

## 星数曲线

```mermaid
xychart-beta
    title "DarkHater01/slopbench 星数(近 2 点)"
    x-axis ["2026-10-22", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-22 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `a395aa56ff83` · [字段定义](../../DATASET.md)*
