# DHDev0/Stochastic-muzero

⭐ 83 · Python · GPL-3.0 · 推送 2025-12-31 · [GitHub](https://github.com/DHDev0/Stochastic-muzero) · 个人维护

**Stochastic MuZero 的 PyTorch 实现，面向 Gym 环境的强化学习训练**

基于 MuZero Unplugged 的 Stochastic MuZero PyTorch 实现，支持在线与离线强化学习，适用于任意 Gymnasium 环境（离散/连续动作与观测空间的任意组合）。核心机制包括 MCTS 与机会节点扩展、afterstate 预测/动态函数与编码器、reanalyze 缓冲与人类对局数据集加载。提供 CLI（训练/推理/基准测试）、Jupyter 教程、Dockerfile 及 CartPole 预训练权重。依赖 Python 3.8-3.10、torch 1.13、ray、gymnasium，支持 Windows/Linux/macOS 与单/多 GPU/CPU，GPL-3.0 许可，作者为个人（Daniel Derycke）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 支持任意 Gymnasium 环境，含离散/连续动作与观测空间组合
- MCTS 扩展机会节点（chance node）与 afterstate 相关函数
- MLP/LSTM/Transformer/ResNet 多种观测网络结构可选
- 提供 CLI 训练/推理/基准、Dockerfile 与 CartPole 预训练权重

## 适用场景

- 在自定义 Gym 环境上训练 Stochastic MuZero 智能体
- 使用人类对局数据集做离线强化学习
- 复现论文中的随机环境（机会节点）MuZero 实验

## 场景标签

`强化学习` · 领域:训练与推理

## 证据(README 行号)

> L3: Pytorch Implementation of Stochastic MuZero. Base on Muzero Unplugged.
> L134: * [x] Work for any Gymnasium environments/games. (any combination of continous or/and discrete action and observat

## 星数曲线

```mermaid
xychart-beta
    title "DHDev0/Stochastic-muzero 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-28"]
    y-axis "stars" 81 --> 84
    line [82, 83, 83]
```

2026-10-18 82 → 2026-10-28 83（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `09a68b502e10` · [字段定义](../../DATASET.md)*
