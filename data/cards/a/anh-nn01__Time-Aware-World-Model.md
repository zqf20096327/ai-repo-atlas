# anh-nn01/Time-Aware-World-Model

⭐ 16 · Python · 推送 2025-11-24 · [GitHub](https://github.com/anh-nn01/Time-Aware-World-Model) · 组织维护

**世界模型的时间感知训练方法代码（ICML 2025 论文官方实现）**

ICML 2025 论文 Time-Aware World Model 的官方代码：一种模型无关的世界模型训练方法，通过在动力学模型中显式引入时间步长 Δt 并以变化频率采样观测进行训练，实验基于 TD-MPC2 架构，也说明如何将该方法并入其他世界模型（如 Dreamers）训练管线。提供 Conda 环境安装、训练与评估脚本，支持 meta-world、PDE 控制、F16 飞控（进行中）等任务，另含修改版 MTS3+MPC 的对比实验流程。面向强化学习与世界模型方向的研究者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 在动力学模型中条件化时间步长 Δt，架构无关，可并入任意世界模型训练管线
- 混合时间步长采样（Log-Uniform 或 Uniform）训练
- 基于 TD-MPC2 架构的实验，含 baseline 训练与多观测频率评估脚本
- 提供修改版 MTS3+MPC 用于控制任务对比实验

## 适用场景

- 复现论文中 TAWM 与固定 Δt baseline 的训练与评估
- 将时间感知训练方法并入自己的世界模型管线
- 在 meta-world、PDE 控制任务上研究不同观测频率下的世界模型性能

## 场景标签

`模型训练` `强化学习` · 领域:训练与推理

## 证据(README 行号)

> L16: This is the official code for **Time-Aware World Model (TAWM)**, a model-agnostic and more efficient training metho
> L24: Since TAWM's core contribution is the **time-aware concepts and training method**, which is ***architecture-agnosti

## 星数曲线

```mermaid
xychart-beta
    title "anh-nn01/Time-Aware-World-Model 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `43ca0b8f584b` · [字段定义](../../DATASET.md)*
