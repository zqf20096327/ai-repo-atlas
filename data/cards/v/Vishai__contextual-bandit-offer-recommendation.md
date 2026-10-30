# Vishai/contextual-bandit-offer-recommendation

⭐ 16 · Python · MIT · 推送 2026-10-20 · [GitHub](https://github.com/Vishai/contextual-bandit-offer-recommendation) · 个人维护

**实时优惠推荐系统：贝叶斯 Thompson Sampling 在线选品并持续学习**

面向电商/营销场景的上下文多臂老虎机推荐系统：为每个访客实时选择转化率最高的优惠，基于用户历史、设备、地理与购买特征维护贝叶斯后验，反馈即刻更新后验。以 FastAPI 服务形式提供（Docker 与 AWS ECS Fargate 部署），附带 SQL 特征管道、夜间自动再训练（离线评估门控晋升）、离线策略评估与回测（对比 random/greedy/UCB），以及 regret、分配、延迟与漂移监控。约 200 个 pytest 测试。README 明示结果来自模拟数据，真实提升需在线 A/B 验证；SQLite 仅适合演示与中等流量。

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

- Thompson Sampling 按用户上下文维护后验，反馈即时更新
- FastAPI 服务，p99 约 6 ms，100 ms 目标内，Docker/AWS ECS 部署
- 离线策略评估与回测，对比 random/greedy/UCB，doubly robust 估计
- 夜间自动再训练，离线评估门控后才晋升模型

## 适用场景

- 在线营销场景为每位访客实时挑选最优优惠券
- 对比多种 bandit 策略的历史回测与离线评估
- 搭建带自动再训练与漂移监控的推荐决策服务

## 场景标签

`推荐系统` · 领域:学习与行业

## 证据(README 行号)

> L12: - **Bayesian Thompson Sampling.** Each offer keeps a posterior over its
> L19: - **Measured before it ships.** Offline policy evaluation and backtesting compare

## 星数曲线

```mermaid
xychart-beta
    title "Vishai/contextual-bandit-offer-recommendation 星数(近 2 点)"
    x-axis ["2026-10-22", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-22 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `1841455e93ad` · [字段定义](../../DATASET.md)*
