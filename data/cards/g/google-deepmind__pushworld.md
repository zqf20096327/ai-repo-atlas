# google-deepmind/pushworld

⭐ 96 · Python · Apache-2.0 · 推送 2026-05-05 · [GitHub](https://github.com/google-deepmind/pushworld) · 组织维护

**操作规划基准：含工具与可动障碍的推动谜题集合与求解器对比**

DeepMind 维护的 PushWorld 操作规划基准：提供人可编辑格式存储的基准谜题与参考解，附一个 C++ 实现的 Recursive Graph Distance (RGD) 规划器（2023 年 1 月时在 1/5/30 分钟内解题数居前）；python3 目录提供基准测试、解法视频绘制、PDDL/SAS 转换脚本，并实现兼容 OpenAI Gym 与 DeepMind RL 环境的接口以支持强化学习研究。谜题构建与运行需分别参照 cpp/README.md 与 python3/README.md，README 本身未给出完整安装命令。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 人可编辑的基准谜题集合与参考解
- C++ 实现的 RGD 规划器
- PDDL 与 SAS 格式转换脚本
- 兼容 OpenAI Gym 与 DeepMind RL 环境接口

## 适用场景

- 对比不同规划求解器在推动谜题上的性能
- 为强化学习研究提供操作规划环境
- 将谜题转换为 PDDL/SAS 用于经典规划器实验

## 场景标签

`模型评测` `强化学习` · 领域:评测与运维

## 证据(README 行号)

> L3: This repository contains the PushWorld environment, a collection of benchmark
> L4: puzzles to compare the performance of different solvers, and a state-of-the-art
> L22: To support reinforcement learning research with PushWorld, it also implements
> L23: interfaces compatible with the OpenAI Gym environment API and

## 星数曲线

```mermaid
xychart-beta
    title "google-deepmind/pushworld 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 95 --> 97
    line [96, 96]
```

2026-10-18 96 → 2026-10-24 96（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `f837f4fb7172` · [字段定义](../../DATASET.md)*
