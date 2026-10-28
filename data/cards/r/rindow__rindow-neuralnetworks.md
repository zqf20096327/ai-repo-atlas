# rindow/rindow-neuralnetworks

⭐ 86 · PHP · BSD-3-Clause · 推送 2026-09-03 · [GitHub](https://github.com/rindow/rindow-neuralnetworks) · [官网](https://rindow.github.io/neuralnetworks) · 组织维护

**PHP 深度学习神经网络库，类 Keras 写法并支持 OpenCL GPU 加速**

面向 PHP 开发者的神经网络库：以类似 Keras 的方式在 PHP 中编写深度学习网络模型，支持 CNN 等模型构建与训练。计算上可接入 rindow-matlib 与 OpenBLAS 加速，宣称速度接近 TensorFlow 的 CPU 版本；支持 OpenCL GPU 加速（含非 NVIDIA 显卡与笔记本集成 GPU）。训练好的模型可部署在普通 PHP 虚拟主机上运行。需 PHP 8.1+，通过 Composer 安装，速度提升依赖额外安装预编译二进制。示例目录提供图像分类训练代码。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | BSD-3-Clause |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 类 Keras 语法在 PHP 中编写网络模型
- 支持 OpenCL GPU 加速，可用非 NVIDIA 显卡与集成 GPU
- 通过 rindow-matlib/OpenBLAS 加速 CPU 计算
- 训练好的模型可在普通 PHP web 主机上运行

## 适用场景

- 在纯 PHP 环境下开发和训练神经网络模型
- 把深度学习推理部署到不支持 Python 的 PHP 虚拟主机
- 用 OpenCL 在笔记本集成 GPU 上运行深度学习

## 场景标签

`模型训练` `推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L8: Rindow Neural Network Library is a high-level neural network library for deep learning.
> L12: Like Keras in Python, you can easily write network models in PHP.
> L25: It supports GPU acceleration using OpenCL.

## 星数曲线

```mermaid
xychart-beta
    title "rindow/rindow-neuralnetworks 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 85 --> 87
    line [86, 86]
```

2026-10-18 86 → 2026-10-28 86（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `dbc9c8e66b13` · [字段定义](../../DATASET.md)*
