# YuriyGuts/cartpole-q-learning

⭐ 15 · Python · MIT · 推送 2026-07-22 · [GitHub](https://github.com/YuriyGuts/cartpole-q-learning) · [官网](https://gym.openai.com/evaluations/eval_K41KvF0Re6BJW593cq2Tg) · 个人维护

**用 Q-Learning 训练的倒立摆平衡 agent 示例项目**

基于 Python 3 与 Gymnasium（原 OpenAI Gym）实现的 CartPole 倒立摆平衡 agent，采用 Q-Learning 算法训练。提供 verbose 模式（渲染、绘图、详细日志）与 performance 模式两种运行方式，回合统计结果输出到 experiment-results/episode_history.csv。使用 uv 管理依赖，附 make 命令封装；Linux 下 GUI 窗口可能需安装 python3.10-tk。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Q-Learning 算法训练 CartPole 平衡 agent
- 基于 Gymnasium 环境，uv 管理依赖
- verbose/performance 两种运行模式，回合统计输出 CSV

## 适用场景

- 学习 Q-Learning 强化学习算法的入门实现
- 运行并观察 CartPole 训练过程与回合统计

## 场景标签

`强化学习` · 领域:训练与推理

## 证据(README 行号)

> L3: A cart pole balancing agent powered by Q-Learning. Uses Python 3 and Gymnasium (formerly OpenAI Gym).

## 星数曲线

```mermaid
xychart-beta
    title "YuriyGuts/cartpole-q-learning 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `eded3bb0e159` · [字段定义](../../DATASET.md)*
