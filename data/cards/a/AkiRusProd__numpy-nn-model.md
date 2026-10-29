# AkiRusProd/numpy-nn-model

⭐ 82 · Python · 推送 2026-02-28 · [GitHub](https://github.com/AkiRusProd/numpy-nn-model) · 个人维护

**基于 NumPy/CuPy 的 torch 风格神经网络框架，含磁带自动微分**

自研机器学习框架 neunet：以 NumPy 为 CPU 后端、CuPy 为可选 GPU 后端，实现基于 tape 的自动微分与 torch 风格 API。提供卷积/线性/循环层、激活函数、损失函数与 SGD/Adam 等优化器，另含实验性融合 CUDA 模块（CUDALinear、CUDAFusedAdamW 等）。附 14 个端到端 notebook 示例（GAN、VAE、DDPM、Seq2Seq Transformer、GPT2 推理等），并带 CPU/CUDA 测试套件。通过 git clone 源码安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- tape 自动微分 + torch 风格 API
- CPU(NumPy)/GPU(CuPy) 双后端张量
- 实验性融合 CUDA 模块（Linear/Softmax/RMSNorm/FusedAdamW 等）
- 14 个端到端示例 notebook（DDPM、GAN、VAE、Transformer、GPT2 推理等）

## 适用场景

- 学习自动微分与神经网络内部实现的原理
- 在纯 NumPy 环境下构建和训练 CNN/RNN/Transformer
- 用 CuPy 在 GPU 上加速训练并使用融合 CUDA 内核

## 场景标签

`教程课程` `模型训练` · 领域:学习与行业

## 证据(README 行号)

> L5: A custom CPU/GPU, torch-style machine learning framework with tape-based automatic differentiation. Built on NumPy f
> L8: - Tape-based autograd with a torch-like API
> L10: - Broad set of layers, activations, losses, and optimizers

## 星数曲线

```mermaid
xychart-beta
    title "AkiRusProd/numpy-nn-model 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 81 --> 83
    line [82, 82]
```

2026-10-18 82 → 2026-10-29 82（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `4af577444495` · [字段定义](../../DATASET.md)*
