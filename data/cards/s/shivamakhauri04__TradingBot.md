# shivamakhauri04/TradingBot

⭐ 51 · Jupyter Notebook · MIT · 推送 2026-01-29 · [GitHub](https://github.com/shivamakhauri04/TradingBot) · 个人维护

**用 DQN 强化学习做股票预测与自动交易的 Python 项目**

基于 Deep Q-Network 的股票交易项目：在自定义 gym 兼容环境中训练 agent 对历史股价做 buy/sell/hold 三种决策，采用经验回放、目标网络与 epsilon-greedy 探索。Q 网络为三层全连接（隐层 100），超参数由 YAML 配置。README 报告在 2014-2016 年 GOOG 数据上训练、2016-2017 测试期获利 3,841.44 美元。提供 git clone 源码、pip 依赖安装与 Jupyter 笔记本两种使用方式。

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

- gym 兼容的自定义交易环境（hold/buy/sell 三动作）
- DQN 训练：经验回放、目标网络、epsilon-greedy
- 超参数集中配置于 configs/default.yaml
- 提供模块化代码与原始 Jupyter 笔记本

## 适用场景

- 学习 DQN 在金融交易中的应用
- 在历史股价数据上训练自动买卖 agent
- 作为强化学习交易实验的代码起点

## 场景标签

`金融量化` `强化学习` · 领域:学习与行业

## 证据(README 行号)

> L7: Stock price prediction and automated trading using Deep Q-Network (DQN) reinforcement learning. Trains an agent to m
> L11: This project implements a **Deep Q-Network (DQN)** agent for automated stock trading. The key components are:

## 星数曲线

```mermaid
xychart-beta
    title "shivamakhauri04/TradingBot 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 50 --> 52
    line [51, 51]
```

2026-10-18 51 → 2026-10-28 51（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `660ad641b845` · [字段定义](../../DATASET.md)*
