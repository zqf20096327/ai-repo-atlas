# ebrahimpichka/DeepRL-trade

⭐ 21 · Jupyter Notebook · 推送 2026-02-13 · [GitHub](https://github.com/ebrahimpichka/DeepRL-trade) · 个人维护

**用 PPO/DQN 深度强化学习做 GOOG 股票算法交易的项目**

训练 PPO 与 DQN 两个强化学习智能体，在 GOOG 股票上自主生成长/持币/做空交易决策，并以 Buy & Hold 为基准做风险调整指标对比。环境为 Gymnasium 兼容的离散动作环境，奖励取总资产百分比变化；PPO 用自定义 actor-critic（LayerNorm+Dropout），DQN 用 stable-baselines3 的 MLP 策略。数据默认来自 yfinance（可选 Tiingo，需 API key），技术指标经 pandas-ta 计算并做滚动 z-score 归一化。评估跑 500 个随机起点 episode 输出置信区间与 pyfolio 统计，支持 Weights & Biases 实验跟踪，配置采用 YAML 分层覆盖。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- PPO 与 DQN 双智能体交易并与 Buy & Hold 基准对比
- Gymnasium 离散动作环境：Long/Cash/Short，奖励为资产百分比变化
- 500 随机起点 episode 评估，输出 95%/99% 置信区间与 pyfolio 统计
- yfinance/Tiingo 数据源、YAML 分层配置、W&B 实验跟踪

## 适用场景

- 学习强化学习在量化交易中的完整训练与评估流程
- 复现并对比 PPO 与 DQN 在股票交易上的表现
- 作为自定义交易环境与实验配置的起点做扩展研究

## 场景标签

`金融量化` `强化学习` · 领域:学习与行业

## 证据(README 行号)

> L9: This project trains two DRL agents — **Proximal Policy Optimization (PPO)** and **Deep Q-Learning (DQN)** — to auton
> L83: |**DQN Agent**|Standard MLP policy from stable-baselines3.|

## 星数曲线

```mermaid
xychart-beta
    title "ebrahimpichka/DeepRL-trade 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-30 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `e7e71452144a` · [字段定义](../../DATASET.md)*
