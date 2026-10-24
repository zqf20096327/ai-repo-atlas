# xylcbd/EasyCNN

⭐ 167 · C++ · 推送 2025-12-25 · [GitHub](https://github.com/xylcbd/EasyCNN) · 个人维护 · 中文 README

**纯 C++ 实现的小型 CNN 框架，供学习与训练测试**

EasyCNN 是一个纯 C++ 实现、无第三方依赖的卷积神经网络框架，提供数据层、卷积层、池化层、全连接层、softmax 层及多种激活层，损失函数支持交叉熵与 MSE，优化方法含 SGD 与动量 SGD，并使用多线程并行。支持导入传统 CNN 结构的 TensorFlow 模型，附 mnist 训练测试示例。Todo 列表显示批归一化、dropout、跨平台移植（Linux/Mac/Android/iOS）与 cuBLAS/OpenBLAS 加速等尚未完成，当前平台范围有限。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 纯 C++ 实现，无第三方依赖
- 覆盖卷积/池化/全连接/softmax 及 sigmoid、tanh、RELU 激活层
- 支持交叉熵与 MSE 损失，SGD 与动量 SGD 优化，多线程并行
- 支持导入传统 CNN 结构的 TensorFlow 模型

## 适用场景

- 阅读源码学习卷积神经网络的内部实现
- 在无依赖环境用 C++ 训练和测试简单 CNN（如 MNIST）
- 将传统 TensorFlow CNN 模型移植到该框架运行

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L2: Easy convolution neural network framework.
> L13: * All in one: without any dependency, pure c++ implemented.
> L14: * Basic layer: data layer, convolution layer, pooling layer, full connect layer, softmax layer, activation layers(s

## 星数曲线

```mermaid
xychart-beta
    title "xylcbd/EasyCNN 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 166 --> 168
    line [167, 167]
```

2026-10-18 167 → 2026-10-24 167（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `d12f2d3d653b` · [字段定义](../../DATASET.md)*
