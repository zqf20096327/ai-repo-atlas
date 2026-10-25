# lucidrains/evolutionary-policy-optimization

⭐ 112 · Python · MIT · 推送 2026-10-21 · [GitHub](https://github.com/lucidrains/evolutionary-policy-optimization) · 个人维护

**Evolutionary Policy Optimization 的 PyTorch 实现，面向强化学习研究**

lucidrains 对 Wang 等（CMU 机器人研究所，2025）论文 Evolutionary Policy Optimization 的 PyTorch 复现，将进化方法与梯度训练结合用于强化学习策略优化，并额外加入权重空间 crossover 的尝试。提供 pip 安装的 Python 库、端到端学习用法，以及 LunarLander-v3 的示例训练脚本 train_gym.py，支持单进程与 torchrun 多进程分布式训练及 wandb 日志。面向强化学习研究者与开发者。

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

- 论文方法的 PyTorch 实现，含隐变量策略
- 额外加入权重空间 crossover 的作者尝试
- 提供 LunarLander-v3 示例训练脚本，支持 torchrun 分布式与 wandb 日志

## 适用场景

- 复现论文方法做强化学习策略优化实验
- 在 Gym 环境上训练并对比进化+梯度混合方法
- 作为 PyTorch 库嵌入自己的 RL 训练流程

## 场景标签

`强化学习` · 领域:训练与推理

## 证据(README 行号)

> L5: Pytorch implementation of Evolutionary Policy Optimization, from Wang et al. of the Robotics Institute at Carnegie M
> L37: An example training script for LunarLander-v3 is provided at `train_gym.py`

## 星数曲线

```mermaid
xychart-beta
    title "lucidrains/evolutionary-policy-optimization 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-25"]
    y-axis "stars" 110 --> 113
    line [111, 112, 112]
```

2026-10-18 111 → 2026-10-25 112（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `d4b490bb2472` · [字段定义](../../DATASET.md)*
