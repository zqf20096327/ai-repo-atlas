# 77axel/Digit-Recognizer

⭐ 14 · Jupyter Notebook · MIT · 推送 2026-01-13 · [GitHub](https://github.com/77axel/Digit-Recognizer) · 个人维护

**从零实现的手写数字识别 CNN 教学项目**

用 NumPy/SciPy 从零实现的卷积神经网络，完成 MNIST 风格手写数字识别，不依赖 PyTorch/TensorFlow 等框架。前向与反向传播手动实现，计算密集部分（Softmax、ReLU、损失、权重更新、向量运算）下放到 C 扩展与 Fortran f2py 模块，并集成 OpenBLAS 加速矩阵乘法，编译产物经 ctypes 加载。完整训练流程在 Jupyter notebook lab.ipynb 中提供，面向深度学习原理与底层优化的学习者和实验者，需 Python 3.8+ 环境，数据集需先解压 data.zip。

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

- NumPy/SciPy 从零实现 CNN 前向与反向传播，不依赖 PyTorch/TensorFlow
- C 扩展与 Fortran f2py 模块承担 Softmax/ReLU/损失/权重更新等核心计算
- OpenBLAS 加速矩阵乘法，编译模块经 ctypes 加载
- 完整训练与测试流程包含在 lab.ipynb

## 适用场景

- 学习 CNN 与反向传播的底层实现原理
- 实验 C/Fortran 扩展对 Python 数值计算的性能优化
- 手写数字分类的训练与测试

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L7: A handwritten digit recognition system built from scratch using Python. This project demonstrates high-performance o
> L69: This project explores low-level neural network optimization. Instead of relying on frameworks like PyTorch or Tenso

## 星数曲线

```mermaid
xychart-beta
    title "77axel/Digit-Recognizer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `32d7afbb2f08` · [字段定义](../../DATASET.md)*
