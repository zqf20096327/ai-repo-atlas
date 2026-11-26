# Meckmin/mnist-numpy-from-scratch

⭐ 5 · Python · MIT · 推送 2026-11-23 · [GitHub](https://github.com/Meckmin/mnist-numpy-from-scratch) · 个人维护

**仅用 NumPy 从零实现 MNIST 手写数字识别神经网络**

用纯 NumPy 构建的模块化神经网络，不依赖 PyTorch/TensorFlow/scikit-learn。逐层手写 forward/backward，反向传播公式手工推导，并用中心差分梯度检验验证（相对误差低于 4×10⁻⁹）。含 softmax 数值稳定性处理、pytest 单元测试、固定种子与 JSON 结果保存、可复用的 408 KB 权重文件。面向学习神经网络原理的开发者，需自行下载 MNIST 原始 IDX 文件放入 data/ 目录；全连接结构无卷积，无法处理平移不变的输入。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 无 ML 库依赖，层、损失、优化器、训练循环均用 NumPy 实现
- 手工推导反向传播并用梯度检验逐项数值验证
- 附带学习率、隐藏层尺寸、训练时长等对照实验记录
- 训练权重保存为 float32 文件，可直接重载复现

## 适用场景

- 我想逐层理解反向传播的数学推导与实现
- 我想复现 MNIST 训练并查看超参数实验结果
- 我想参考梯度检验方法验证自己手写的梯度

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L3: A modular neural network built from scratch using only NumPy. No PyTorch, no TensorFlow, no scikit-learn or any othe
> L9: - **Numerically verified.** A gradient check compares every analytic gradient with a central-difference estimate; th


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `583758e2ec2d` · [字段定义](../../DATASET.md)*
