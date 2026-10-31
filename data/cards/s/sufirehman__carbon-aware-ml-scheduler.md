# sufirehman/carbon-aware-ml-scheduler

⭐ 19 · Python · MIT · 推送 2026-06-24 · [GitHub](https://github.com/sufirehman/carbon-aware-ml-scheduler) · 个人维护

**面向研究者的碳感知 ML 训练调度器：按 UK 电网碳强度择时**

CAML-TC 是基于强化学习与启发式混合的碳感知调度系统：读取 UK National Grid 实时与 24 小时预测碳强度数据，为 ML 训练任务推荐低排放执行窗口。包含 Q-learning 智能体（8,000 回合真实电网数据训练）、多目标奖励设计、置信度衰减加权预测，以及 CodeCarbon 集成的排放测量与多页 Streamlit 仪表盘。以 pip 可装的 Python 库形式提供，面向研究员与工程师；当前仅覆盖 UK 电网，其他区域在路线图中。论文被 IEEE EEEIC 2026 接收。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Q-learning 与启发式混合调度引擎，按电网波动性自动选择策略
- 读取 UK National Grid 实时+24h 预测碳强度 API
- CodeCarbon 集成的逐策略排放测量
- pip 可安装的 Python 库，可直接嵌入自有 ML 流水线

## 适用场景

- 我想让 GPU 训练任务在电网低碳时段自动运行
- 对比 baseline/启发式/RL 三种调度策略的碳减排
- 研究碳感知调度算法在真实电网数据上的表现

## 场景标签

`MLOps` · 领域:训练与推理

## 证据(README 行号)

> L14: A **reinforcement learning–driven carbon-aware scheduling system** that dynamically optimises machine learning work
> L26: to shift compute workloads into low-emission periods, achieving **28–34% CO₂ reduction under realistic conditions**
> L63: scheduler = CarbonScheduler(duration_minutes=90, urgency="low")

## 星数曲线

```mermaid
xychart-beta
    title "sufirehman/carbon-aware-ml-scheduler 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-31 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `6e9fbcdf8a27` · [字段定义](../../DATASET.md)*
