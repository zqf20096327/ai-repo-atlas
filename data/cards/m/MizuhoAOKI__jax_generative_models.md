# MizuhoAOKI/jax_generative_models

⭐ 68 · Python · MIT · 推送 2025-12-19 · [GitHub](https://github.com/MizuhoAOKI/jax_generative_models) · 个人维护

**JAX 下统一 Diffusion 与 Flow Matching 的极简生成模型实现**

以共享的 strategy 接口统一 DDPM 扩散与 Flow Matching 两类生成建模范式，提供 mlp/resnet/unet 三种模型结构与 cat/gaussian-mixture/moon/swiss-roll/mnist 五种数据集，通过 tyro 命令行完成训练、采样、传输过程动画与 Rerun 可视化。面向希望在同一代码基础下对比两类分布传输算法的研究者与学习者；使用 uv 管理环境，GPU 加速需 CUDA 12 与 NVIDIA GPU，也提供 CPU 路径。

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

- 统一 strategy 接口同时支持 ddpm 与 flow-matching
- mlp/resnet/unet 模型 × 5 种数据集的组合实验
- mnist 上支持按数字条件的图像生成
- Rerun 实时可视化与训练后传输过程动画

## 适用场景

- 在同一框架下对比 Diffusion 与 Flow Matching 训练效果
- 学习两类生成建模算法的结构异同
- 小规模图像数据上做条件生成实验

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L15: **Minimal JAX implementation that unifies Diffusion and Flow Matching under a shared interface.**
> L17: `jax_generative_models` provides a unified interface for Diffusion and Flow Matching algorithms in JAX.
> L74:     uv run scripts/main.py generate strategy:<STRATEGY_NAME> model:<MODEL_NAME> dataset:<DATASET_NAME>

## 星数曲线

```mermaid
xychart-beta
    title "MizuhoAOKI/jax_generative_models 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 67 --> 69
    line [68, 68]
```

2026-10-18 68 → 2026-10-31 68（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `11ae4730bf4d` · [字段定义](../../DATASET.md)*
