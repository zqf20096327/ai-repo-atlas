# asieradzk/RL_Matrix

⭐ 309 · C# · MIT · 推送 2026-04-23 · [GitHub](https://github.com/asieradzk/RL_Matrix) · 个人维护 · 中文 README

**C# 深度强化学习框架，含 PPO/DQN/GAIL 与分布式训练**

面向 C# 开发者的深度强化学习框架，基于 TorchSharp 后端纯 C# 实现。提供 PPO、DQN（含 C51、Rainbow 变体）、GAIL 等算法，支持连续/离散/混合动作空间的多头智能体、RNN 选项开关、多环境并行与可选网络化分布式训练，内置训练指标可视化仪表板。在 Unity 与 Godot 游戏引擎中经过测试，路线图显示非 Windows 非 CUDA 平台支持仍在测试优化阶段，仓库内示例正在更新中。通过 NuGet 分发。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 算法库含 PPO、DQN（至 C51/Rainbow）与 GAIL
- 单智能体同时处理连续、离散与混合动作空间
- 网络化分布式多环境训练与实时监控仪表板
- 在 Unity 与 Godot 引擎中经过测试

## 适用场景

- 用 C# 开发和训练深度强化学习智能体
- 在 Unity/Godot 游戏中集成强化学习训练
- 跨并行环境进行大规模 RL 训练并监控指标

## 场景标签

`强化学习` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L5: RLMatrix provides a comprehensive reinforcement learning framework for C# developers with performance exceeding Pyth
> L25: - **Comprehensive Algorithm Library**: Includes PPO, DQN with all popular modifications (up to C51 and DQN Rainbow)

## 星数曲线

```mermaid
xychart-beta
    title "asieradzk/RL_Matrix 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 308 --> 310
    line [309, 309]
```

2026-10-18 309 → 2026-10-25 309（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `77f32700841d` · [字段定义](../../DATASET.md)*
