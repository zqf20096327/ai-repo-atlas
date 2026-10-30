# xin-pu/RLSharp

⭐ 16 · C# · MIT · 推送 2026-06-26 · [GitHub](https://github.com/xin-pu/RLSharp) · 个人维护

**.NET 强化学习库：自定义环境训练/部署策略**

面向 .NET 8 的强化学习库。核心为纯 .NET 抽象：用户自定义状态、动作、环境与奖励模型，通过 IAgent/IPolicy 接口进行训练、保存与推理部署；TorchSharp 仅作为 RLSharp.Torch 后端使用（CPU 运行时）。算法覆盖 Q-Learning、DQN、PPO、A2C/A3C 等离散方法，DDPG/TD3/SAC 仅为 Torch 层边界，需连续动作空间适配器才能完整训练。另提供 Web 可视化器（FrozenLake/CartPole/RiskyBandit）与 xUnit 测试套件。通过 dotnet 命令从源码构建，MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 纯 .NET 泛型接口：IAgent/IPolicy 分离训练与推理
- TorchSharp 仅限 RLSharp.Torch 后端，Core 不暴露张量
- 含 Q-Learning/DQN/PPO 等算法与 Web 训练可视化器
- 提供控制台示例与 xUnit 测试套件

## 适用场景

- 在 .NET 应用中自定义环境训练强化学习策略
- 将训练好的策略部署到真实系统做推理
- 通过 Web 界面观察 FrozenLake/CartPole 训练过程

## 场景标签

`强化学习` · 领域:训练与推理

## 证据(README 行号)

> L3: RLSharp is a reinforcement learning library for .NET. The public entry point is a pure .NET Core API: application co
> L9: - TorchSharp-backed generic agents for custom state/action types.

## 星数曲线

```mermaid
xychart-beta
    title "xin-pu/RLSharp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `7eff525f3d5f` · [字段定义](../../DATASET.md)*
