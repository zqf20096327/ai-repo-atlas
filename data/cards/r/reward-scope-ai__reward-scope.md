# reward-scope-ai/reward-scope

⭐ 21 · Python · MIT · 推送 2025-12-29 · [GitHub](https://github.com/reward-scope-ai/reward-scope) · 个人维护

**RL 训练中的 reward hacking 实时检测与可视化工具**

面向强化学习研究者的 Python 库：在训练过程中追踪各奖励分量，用 5 种检测器（动作重复、状态循环、分量失衡、奖励尖峰、边界利用）识别 reward hacking 模式，每个警报含严重度分数、证据与修复建议；采用自适应基线学习每次运行的'正常'模式以减少误报。提供 FastAPI+Chart.js 实时仪表盘（WebSocket 10Hz 更新）、SQLite 持久化、CLI 与 JSON/CSV 导出。以 Gymnasium 包装器或 Stable-Baselines3 回调接入，可选 WandB 日志；Isaac Lab 集成标注为 coming soon。需 Python 3.8+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 5 种 reward hacking 检测器，每条警报附严重度/证据/修复建议
- 自适应基线学习正常模式以降低误报
- FastAPI+Chart.js 实时仪表盘，WebSocket 10Hz 更新
- 支持自定义检测器与奖励分量追踪（含 info 字典自动提取）

## 适用场景

- RL 训练中实时观察奖励分量与 hacking 分数
- 排查分数上升但行为异常的策略
- 训练后将警报与回合历史导出做分析，或用 WandB 汇总监控

## 场景标签

`强化学习` · 领域:训练与推理

## 证据(README 行号)

> L8: RewardScope detects reward hacking during RL training, saving you from wasting hours on a broken policy. It tracks r
> L40: - 🚨 **Hacking Detection** - 5 detectors for common exploitation patterns
> L43: - 🔌 **Easy Integration** - Works with Gymnasium, Stable-Baselines3, and Isaac Lab (coming soon)

## 星数曲线

```mermaid
xychart-beta
    title "reward-scope-ai/reward-scope 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-28 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `722f7de0e5f1` · [字段定义](../../DATASET.md)*
