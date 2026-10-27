# JdeRobot/BehaviorMetrics

⭐ 65 · Python · GPL-3.0 · 推送 2026-10-24 · [GitHub](https://github.com/JdeRobot/BehaviorMetrics) · [官网](https://jderobot.github.io/BehaviorMetrics/) · 组织维护

**自动驾驶方案的仿真评测工具：量化对比各控制器表现**

基于仿真对自动驾驶方案进行量化评测的开源工具：支持 CARLA（主要）与 Gazebo（部分）两种仿真器，提供 Follow-lane、交通驾驶、导航三类任务及各自定制的评测指标，用于横向比较不同自动驾驶方案。被评测的控制器（brain）可由 TensorFlow/PyTorch 端到端深度学习模型、强化学习策略或显式编程策略构成。提供 GUI（单个调试）与 headless（批量实验对比）两种流水线，通过 publish/subscribe 与仿真器通信。安装细节指向项目官网，仓库含 Docker 镜像发布记录。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 支持 CARLA（主要）与 Gazebo（部分）两种仿真器
- 三类任务（Follow-lane/交通驾驶/导航）各配自定义评测指标
- 控制器可为 TensorFlow/PyTorch 模型、强化学习策略或显式策略
- GUI 单体调试与 headless 批量实验两种评测模式

## 适用场景

- 在仿真中量化比较多个自动驾驶控制器的表现
- 批量运行不同模型在不同场景下的实验
- 调试单个 brain+模型控制器的驾驶行为

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L6: This software tool provides evaluation capabilities for autonomous driving solutions using simulation.
> L14: Each task comes with its custom evaluation metrics that can help compare autonomous driving solutions.
> L16: The inner part of the brain can be controlled by an end-to-end deep learning model, written in Tensorflow or PyTorc

## 星数曲线

```mermaid
xychart-beta
    title "JdeRobot/BehaviorMetrics 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 64 --> 66
    line [65, 65]
```

2026-10-18 65 → 2026-10-27 65（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `82e24b40ba6a` · [字段定义](../../DATASET.md)*
