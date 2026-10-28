# sryu1/jsbgym

⭐ 52 · Python · MIT · 推送 2026-06-25 · [GitHub](https://github.com/sryu1/jsbgym) · 个人维护

**基于 JSBSim 飞行动力学模型的固定翼飞机控制强化学习环境**

提供用于固定翼飞机控制的强化学习环境，基于 JSBSim 飞行动力学模型，实现 Gymnasium 接口，通过 gym.make 创建环境并交互。支持 14 种机型（如 Cessna 172P、F-16、A320 等）、两种控制任务（保持航向与转向目标航向）、三种奖励塑形类型；状态空间为 11 元组，动作空间为控制面指令的 3 元组。通过 pip 安装，2D/3D 可视化可选接入 FlightGear（需单独安装并配置 FG_ROOT 等环境变量），FG 渲染模式训练中途存在已知连接错误。

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

- 实现 Gymnasium 接口的 JSBSim 飞行控制强化学习环境
- 14 种机型、2 种控制任务、3 种塑形类型可组合配置
- 支持 2D 绘图、3D 图形与 FlightGear 多种渲染模式
- 连续状态空间（11 元组）与连续动作空间（3 控制面指令）

## 适用场景

- 训练固定翼飞机航向与高度控制的强化学习智能体
- 在 Gymnasium 生态中做飞行控制任务的算法实验
- 用 FlightGear 可视化观察智能体的飞行动作

## 场景标签

`强化学习` · 领域:训练与推理

## 证据(README 行号)

> L8: JSBGym provides reinforcement learning environments for the control of fixed-wing aircraft using the JSBSim flight d
> L109: * **HeadingControlTask** aircraft must fly in a straight line, maintaining its initial altitude and direction of t

## 星数曲线

```mermaid
xychart-beta
    title "sryu1/jsbgym 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 51 --> 53
    line [52, 52]
```

2026-10-18 52 → 2026-10-28 52（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `74afc3931bf9` · [字段定义](../../DATASET.md)*
