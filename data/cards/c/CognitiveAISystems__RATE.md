# CognitiveAISystems/RATE

⭐ 26 · Python · MIT · 推送 2025-11-23 · [GitHub](https://github.com/CognitiveAISystems/RATE) · 组织维护

**带记忆机制的离线强化学习智能体官方实现（ICLR 2026）**

论文《Recurrent Action Transformer with Memory》的官方实现：结合 transformer 与记忆机制处理序列决策中长期依赖的离线 RL 智能体，训练框架另含 ELMUR 记忆增强 transformer。支持 T-Maze、ViZDoom、Minigrid、Memory-Maze、POPGym、Atari、MuJoCo 等环境，并实现 DT、RMT、TrXL、BC、CQL、IQL、DMamba 等 12 类基线算法。通过 pip -e 安装，各环境用配置脚本运行；ViZDoom/Minigrid 实验需先运行脚本采集数据，Atari/MuJoCo 需单独 conda 环境与数据集下载。

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

- transformer+记忆机制处理长时依赖的离线 RL 智能体（RATE/ELMUR）
- 7 类记忆密集环境（含 48 任务 POPGym 套件）
- 实现 DT/RMT/TrXL/CQL/IQL/DMamba 等 12 类基线
- 提供各环境数据采集脚本与训练配置

## 适用场景

- 复现论文中记忆密集任务上的实验结果
- 将 RATE/ELMUR 与其他序列决策基线在同一环境对比
- 基于该框架研究带记忆的离线 RL 方法

## 场景标签

`强化学习` · 领域:训练与推理

## 证据(README 行号)

> L19: RATE (Recurrent Action Transformer with Memory) is a novel offline RL agent designed specifically for solving memor
> L39: |✅|RATE|
> L40: |✅|ELMUR|

## 星数曲线

```mermaid
xychart-beta
    title "CognitiveAISystems/RATE 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 25 --> 27
    line [26, 26]
```

2026-10-18 26 → 2026-10-27 26（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `6d81af76756f` · [字段定义](../../DATASET.md)*
