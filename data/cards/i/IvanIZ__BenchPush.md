# IvanIZ/BenchPush

⭐ 22 · Python · MIT · 推送 2026-02-12 · [GitHub](https://github.com/IvanIZ/BenchPush) · 个人维护

**移动机器人推动类导航与操作任务的基准测试套件**

面向移动机器人推动类任务（pushing-based navigation and manipulation）的 Python 基准测试套件：提供 Maze、Ship-Ice、Box-Delivery、Area-Clearing 四类任务，每类均有 2D 与基于 MuJoCo 的 3D 版本，通过 gym.make 接口创建；配套评估指标（任务效率与交互努力）、策略模板与基线实现（SAC、PPO、RRT、SAM、GTSP 等）。以源码方式安装，PyPI 发布将在评审期后提供；Box-Delivery 与 Area-Clearing 需额外安装 spfa 包，GTSP 策略需 Julia 运行 GLNS 求解器。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 四类推动任务环境，均含 2D 与 MuJoCo 3D 版本，Gymnasium 接口创建
- 评估指标覆盖任务效率与交互努力
- 基线策略含 SAC/PPO（Stable Baselines3）、RRT、SAM、GTSP 等
- 提供策略模板与已训练模型权重下载

## 适用场景

- 在标准化环境中训练和评估推动类导航/操作算法
- 复现论文基线或用自定义策略跑基准对比
- 开发 2D/3D 仿真下的推动任务新方法

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L2: BenchPush is a comprehensive benchmarking suite designed for mobile robots performing pushing-based tasks. The goal 
> L139:  1 : Reinforcement Learning policies Integrated with Stable Baselines 3.

## 星数曲线

```mermaid
xychart-beta
    title "IvanIZ/BenchPush 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-29 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `9bacc562e2c0` · [字段定义](../../DATASET.md)*
