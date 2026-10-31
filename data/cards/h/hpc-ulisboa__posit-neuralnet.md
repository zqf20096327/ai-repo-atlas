# hpc-ulisboa/posit-neuralnet

⭐ 21 · C++ · MIT · 推送 2026-08-17 · [GitHub](https://github.com/hpc-ulisboa/posit-neuralnet) · [官网](https://arxiv.org/abs/2105.00053) · 组织维护

**C++ 深度学习框架：用 posit 数值格式做神经网络训练与推理**

C++ 实现的深度学习训练与测试框架，用 posit 数值格式替代浮点，posit 通过 stillwater-sc/universal 库模拟，深度学习部分基于 LibTorch。提供任意 posit 配置、ReLU/Sigmoid/Tanh 激活函数、卷积/线性/池化/批归一化等层、交叉熵与 MSE 损失、SGD 优化器，以及 std::thread 多线程并行。附 MNIST 全连接网络与 LeNet-5 示例。为航空航天工程硕士论文开发，需 cmake>=3、gcc>=5、glibc>=2.17，从源码克隆构建。

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

- 支持任意 posit 配置的神经网络训练与推理
- 层覆盖卷积/线性/池化/批归一化/Dropout，含 SGD 优化器与两种损失函数
- 基于 LibTorch，posit 由 stillwater-sc/universal 模拟
- std::thread 多线程并行

## 适用场景

- 用 posit 数值格式训练 MNIST/LeNet-5 等网络
- 研究低精度数值格式对神经网络训练的影响
- 作为 C++ posit 深度学习实验的基础库

## 场景标签

`模型训练` `模型量化` · 领域:训练与推理

## 证据(README 行号)

> L3: Framework in C++ for Deep Learning (training and testing) using Posits.
> L4: The posits are emulated with stillwater-sc/universal library and the deep learning is based in PyTorch.
> L6: This is being developed for a thesis to obtain a Master of Science Degree in Aerospace Engineering.

## 星数曲线

```mermaid
xychart-beta
    title "hpc-ulisboa/posit-neuralnet 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-31 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `9d2e889317bb` · [字段定义](../../DATASET.md)*
