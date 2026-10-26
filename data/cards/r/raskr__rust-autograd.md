# raskr/rust-autograd

⭐ 504 · Rust · MIT · 推送 2026-06-02 · [GitHub](https://github.com/raskr/rust-autograd) · 个人维护

**Rust 张量与反向自动微分库，用于训练神经网络**

基于 ndarray 的 Rust 张量与可微运算库，提供反向模式自动微分、计算图、Adam 等优化器，以及受 TensorFlow/Theano 启发的低层神经网络训练特性；计算图仅做最少堆分配。通过 Cargo.toml 依赖方式安装，可选启用 BLAS 特性（accelerate/intel-mkl/openblas）加速矩阵运算。附有 MNIST 多层感知机等示例代码。

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

- 反向模式自动微分
- 基于 ndarray 的张量运算与计算图
- 受 TensorFlow/Theano 启发的神经网络训练特性与优化器
- 可选 BLAS 后端（accelerate/intel-mkl/openblas）

## 适用场景

- 在 Rust 中定义并求导数学函数
- 用 Rust 训练多层感知机等神经网络
- 作为深度学习研究/实验的张量后端

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L7: Tensors and differentiable operations backed by ndarray.
> L22: ### Reverse-mode automatic differentiation
> L32:  This crate has various low-level features inspired by tensorflow/theano to train neural networks.

## 星数曲线

```mermaid
xychart-beta
    title "raskr/rust-autograd 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-26"]
    y-axis "stars" 502 --> 505
    line [503, 504, 504]
```

2026-10-18 503 → 2026-10-26 504（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `39938bc39733` · [字段定义](../../DATASET.md)*
