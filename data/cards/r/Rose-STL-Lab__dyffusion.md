# Rose-STL-Lab/dyffusion

⭐ 235 · Python · Apache-2.0 · 推送 2025-10-27 · [GitHub](https://github.com/Rose-STL-Lab/dyffusion) · [官网](https://salvarc.github.io/blog/2023/dyffusion) · 组织维护

**时空预测的动力学引导扩散模型官方实现（NeurIPS 2023）**

DYffusion 论文的官方 PyTorch 实现：给定初始条件 x0，用动力学信息引导的扩散模型生成未来 h 个时刻的状态序列，面向概率时空预测。基于 PyTorch Lightning 与 Hydra 配置，提供 Navier-Stokes、弹簧网格、海表温度（SST）三类数据集的下载脚本与实验配置。训练分两阶段（插值网络、预测网络），依赖 Weights & Biases 做日志与 checkpoint。以源码方式安装，面向科研复现与自定义数据训练。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 扩散模型结合动力学信息做时空序列预测，可采样多个未来轨迹
- 两阶段训练：先插值网络（以 CRPS 优化）再预测网络
- 提供 Navier-Stokes、spring mesh、SST 数据集的下载脚本与实验 yaml 配置
- 支持自定义数据集训练与 Dropout 等基线复现实验

## 适用场景

- 复现 NeurIPS 2023 论文中的时空预测实验
- 在我自己的物理系统或时空数据上训练概率预测模型
- 生成集合预测（如每个初始条件预测 50 个样本）

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L13: *DYffusion forecasts a sequence of* $h$ *snapshots* $\mathbf{x}_1, \mathbf{x}_2, \dots, \mathbf{x}_h$
> L14: *given the initial conditions* $\mathbf{x}_0$ *similarly to how standard diffusion models are used to sample from a

## 星数曲线

```mermaid
xychart-beta
    title "Rose-STL-Lab/dyffusion 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 234 --> 236
    line [235, 235]
```

2026-10-18 235 → 2026-10-22 235（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `f9d631a979ab` · [字段定义](../../DATASET.md)*
