# Armandpl/furuta

⭐ 42 · Python · 推送 2026-02-02 · [GitHub](https://github.com/Armandpl/furuta) · 组织维护

**旋转倒立摆机器人的构建与强化学习训练项目**

提供旋转倒立摆（Furuta pendulum）机器人从硬件搭建到强化学习控制训练的完整资料：硬件组装说明、依赖安装（poetry）、设备自检脚本，使用 StableBaselines3 库训练机器人平衡控制，借助 Weights and Biases 记录实验并托管预训练模型与报告。复用 Quanser Qube 的部分代码（速度滤波、仿真、动作限制）及多项已有工作，目标是以可负担、可复现的方式复现该经典 RL 控制任务。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 覆盖硬件搭建到 RL 训练的完整流程
- 使用 StableBaselines3 训练倒立摆平衡控制
- W&B 托管实验记录、预训练模型与报告
- 复用 Quanser Qube 的仿真与控制代码

## 适用场景

- 我想低成本搭建一台旋转倒立摆机器人
- 我想在真实硬件上实践强化学习控制
- 我想参考已有实验记录复现训练结果

## 场景标签

`强化学习` · 领域:训练与推理

## 证据(README 行号)

> L3: In this repository you will find everything you need to build and train a rotary inverted pendulum (also known as a 
> L33: - We use the StableBaselines3 library to train the robot.
> L10: - We wanted to learn about RL. Balancing a pendulum is kind of the "hello world" of the field, it seemed like a goo

## 星数曲线

```mermaid
xychart-beta
    title "Armandpl/furuta 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-29"]
    y-axis "stars" 40 --> 43
    line [41, 42, 42]
```

2026-10-18 41 → 2026-10-29 42（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `cdf3c057d1e2` · [字段定义](../../DATASET.md)*
