# enlite-ai/maze

⭐ 294 · Python · NOASSERTION · 推送 2026-06-01 · [GitHub](https://github.com/enlite-ai/maze) · [官网](https://maze-rl.readthedocs.io/) · 组织维护

**面向真实决策问题的应用型深度强化学习框架**

MazeRL 是基于 PyTorch 的应用导向深度强化学习框架，覆盖 RL 应用从仿真工程、agent 开发、训练到部署的开发周期。提供感知模块以组合策略/价值网络（dense、卷积、注意力等构建块），内置 A2C、PPO、Impala、SAC、进化策略等训练器，支持多步/多智能体场景与 Gym 兼容环境，配置采用 Hydra 系统。README 自述为非稳定预发布版，接口可能有破坏性变更；许可为研究与非商业免费，商业需另行授权。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 基于 PyTorch 的感知模块，支持 dense/卷积/图卷积/注意力/循环等构建块组合网络
- 内置 A2C、PPO、Impala、SAC、进化策略训练器，支持字典动作/观测空间
- 支持多步与多智能体环境结构，兼容 Gym 环境
- 支持模仿学习与策略微调的训练工作流

## 适用场景

- 我在工业决策问题上搭建并训练 RL agent
- 我想用组合式网络构建块快速为新环境配置策略网络
- 我需要从教师策略做模仿学习再微调

## 场景标签

`强化学习` · 领域:训练与推理

## 证据(README 行号)

> L11: MazeRL is an application oriented Deep Reinforcement Learning (RL) framework, addressing real-world decision proble
> L34:  - Use the provided Maze trainers (A2C, PPO, Impala, SAC, Evolution Strategies),

## 星数曲线

```mermaid
xychart-beta
    title "enlite-ai/maze 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 293 --> 295
    line [294, 294]
```

2026-10-18 294 → 2026-10-29 294（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `9978320d37ac` · [字段定义](../../DATASET.md)*
