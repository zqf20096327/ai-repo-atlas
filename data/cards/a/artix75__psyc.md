# artix75/psyc

⭐ 15 · C · BSD-3-Clause · 推送 2026-02-27 · [GitHub](https://github.com/artix75/psyc) · 个人维护

**C 语言神经网络库：构建与训练多种层类型的网络**

运行于 POSIX 系统（Linux/macOS）的开源 C 语言神经网络库，提供全连接、卷积/池化、归一化、Dropout、Embedding、RNN/LSTM/GRU、Attention 等层类型，可组建 encoder-decoder 模型和 transformer。以 make 源码编译安装，交付动态/静态库、命令行工具 psycl 与编译辅助工具 psyc-cc。可自动检测 Apple Accelerate、AVX、BLAS 加速（均为可选依赖，zlib 为必需系统依赖）；当前无 CUDA 支持。附 MNIST/CIFAR/GPT2 仿真等示例与 man 手册文档（文档仍在完善中）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | BSD-3-Clause |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | `idea` | |

## 能力要点

- 覆盖卷积、循环、Attention 等层类型，可构建 encoder-decoder 与 transformer
- 自动检测 Apple Accelerate/AVX/BLAS 加速，无加速库时可回退自带实现
- 提供动态/静态库、psycl 命令行工具与 psyc-cc 编译辅助工具
- 附 MNIST/CIFAR/循环网络/encoder-decoder/GPT2 仿真等示例

## 适用场景

- 在 C 项目中集成神经网络的构建与训练
- 通过命令行工具快速搭建并训练网络（如 MNIST）
- 在 POSIX 环境下实验 encoder-decoder 与 transformer 结构

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L5: PsyC is an open-source C library that allows building neural networks on POSIX systems such as Linux or macOS. It pr
> L18: Supported layer types:

## 星数曲线

```mermaid
xychart-beta
    title "artix75/psyc 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `9a5fb38e3142` · [字段定义](../../DATASET.md)*
