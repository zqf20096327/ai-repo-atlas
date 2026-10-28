# palle-k/DL4S

⭐ 108 · Swift · MIT · 推送 2026-10-12 · [GitHub](https://github.com/palle-k/DL4S) · [官网](https://palle-k.github.io/DL4S/) · 个人维护

**Swift 深度学习库：自动微分与张量运算，跨苹果平台与 Linux**

纯 Swift 实现的深度学习库，内置反向模式自动微分，无需特殊 Swift 工具链即可构建和训练神经网络。提供张量运算（广播规则与 numpy 一致）、卷积/循环/Transformer 层、多种优化器与损失函数，以及 ResNet/VGG/AlexNet/Transformer 默认实现。运行于 Linux、macOS、iOS、tvOS、watchOS；Apple 设备默认用 Accelerate 框架加速，x86_64 Linux 可选启用 Intel MKL/IPP，否则回退到通用 CPU 实现；GPU 加速为实验分支、未并入主线。模型与优化器状态以 safetensors 格式存取（含分片）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 内置反向模式自动微分，支持二阶导数计算
- 支持 Linux/macOS/iOS/tvOS/watchOS，无需特殊 Swift 工具链
- 提供 ResNet/VGG/AlexNet/Transformer 等默认架构实现
- 模型与优化器状态用 safetensors 格式保存/加载（支持分片）

## 适用场景

- 在 Apple 平台应用中直接训练和运行神经网络
- 用 Swift 做 numpy 式向量化数学运算与求导
- 构建并持久化自定义神经网络模型

## 场景标签

 · 领域:机器学习库

## 证据(README 行号)

> L9: DL4S provides a high-level API for many accelerated operations common in neural networks and deep learning.
> L10: It furthermore has automatic differentiation builtin, which allows you to create and train neural networks without 
> L16: DL4S provides implementations for common network architectures, such as VGG, AlexNet, ResNet and Transformers.

## 星数曲线

```mermaid
xychart-beta
    title "palle-k/DL4S 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 107 --> 109
    line [108, 108]
```

2026-10-18 108 → 2026-10-28 108（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `7308e43fae71` · [字段定义](../../DATASET.md)*
