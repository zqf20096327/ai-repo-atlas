# muellerberndt/cadence

⭐ 643 · Python · GPL-3.0 · 推送 2026-11-26 · [GitHub](https://github.com/muellerberndt/cadence) · [官网](https://cadence.floatingpragma.ai/) · 组织维护

**类脑持续学习 Python 库：从实时经验中学习并行动**

Cadence 是一个 Python 库，实现持续运行的平衡网络大脑：神经元相互驱动直至活动收敛，从收敛状态读取动作，突触通过自由与推动两阶段之差进行局部更新，无反向传播、无训练/使用切换。System 1 提供感知、记忆、可塑性与动作；可选的 System 2 通过观察者区域做慢速修正。默认 NumPy/CPU，可选 Numba/SciPy、MLX（Apple）与 PyTorch/CUDA 后端。定位为 alpha 研究软件，面向机器学习研究者与具身/机器人学习实验者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 局部可塑性的持续在线学习，无反向传播与训练/推理切换
- 工作痕迹、历史、召回与联想四种记忆，支持 grow/graft 扩展
- 平衡传播式对比学习与奖励驱动的三因子更新规则
- 浏览器实时演示：机械臂、Atari、Connect Four 等

## 适用场景

- 研究无反向传播的在线局部学习机制
- 为机器人或游戏环境搭建持续学习控制器
- 在持续交互流中测试记忆的习得、保持与恢复

## 场景标签

`科研工具` `模型训练` · 领域:学习与行业

## 证据(README 行号)

> L12: Cadence is a Python library for brains that learn while they live. Animal and human brains learn
> L149: The library puts continuing state, reciprocal interpretation, local plasticity
> L161: ## For machine-learning readers

## 星数曲线

```mermaid
xychart-beta
    title "muellerberndt/cadence 星数(近 20 点)"
    x-axis ["2026-10-25", "2026-10-26", "2026-10-27", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-26", "2026-11-27"]
    y-axis "stars" 434 --> 663
    line [453, 454, 455, 457, 456, 457, 458, 453, 572, 617, 624, 625, 630, 636, 637, 642, 643, 644, 643, 643]
```

2026-10-25 453 → 2026-11-27 643（+190）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 high · 依据 README sha `0965e907b546` · [字段定义](../../DATASET.md)*
