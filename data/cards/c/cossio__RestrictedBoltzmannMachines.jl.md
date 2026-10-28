# cossio/RestrictedBoltzmannMachines.jl

⭐ 24 · Julia · MIT · 推送 2026-10-19 · [GitHub](https://github.com/cossio/RestrictedBoltzmannMachines.jl) · 个人维护

**Julia 语言受限玻尔兹曼机（RBM）训练与采样库**

Julia 包，用于训练与采样受限玻尔兹曼机（RBM）这类概率生成模型。支持 Binary/Spin/Potts/Gaussian/ReLU 系列等多种可见/隐藏层类型，可通过 CUDA 在 GPU 上运行。提供 PCD 与 Parallel Trajectory Tempering 训练、Gibbs 与 Metropolis 采样、自由能/伪似然/配分函数估计等功能，并实现 Centered 与 Standardized RBM 变体。包不导出任何符号，以 Julia Pkg 注册安装，被多篇生物物理与 RNA 建模论文使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 9 种可见/隐藏层类型任意组合构造 RBM
- PCD 与 Parallel Trajectory Tempering 训练，含正则化与回调
- Gibbs/Metropolis 采样与 AIS 配分函数估计
- CUDA GPU 加速，兼容 Adapt.jl 任意 GPU 数组后端

## 适用场景

- 在 Julia 中训练 RBM 生成模型并采样
- 用 GPU 加速的 RBM 做序列家族建模（如 RNA）
- 计算 RBM 的配分函数与似然评估

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L7: A Julia package for training and sampling Restricted Boltzmann Machines (RBMs) — a class of probabilistic generative
> L61: - **Training**: `pcd!` — Persistent Contrastive Divergence with customizable optimizer (via Optimisers.jl), regular
> L62: - **Sampling**: `sample_v_from_v`, `sample_h_from_v`, `sample_v_from_h` — Gibbs sampling; `metropolis` — Metropolis

## 星数曲线

```mermaid
xychart-beta
    title "cossio/RestrictedBoltzmannMachines.jl 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-28 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `94f1d2b8479b` · [字段定义](../../DATASET.md)*
