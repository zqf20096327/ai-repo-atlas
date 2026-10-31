# Yehor-Mishchyriak/PureML

⭐ 13 · Python · Apache-2.0 · 推送 2026-03-21 · [GitHub](https://github.com/Yehor-Mishchyriak/PureML) · 个人维护

**纯 NumPy 实现的小型透明深度学习框架，面向教学与小型实验**

完全基于 NumPy 构建的深度学习框架：提供 Tensor 类与动态计算图自动微分引擎（显式 VJP 反向传播），内置 Affine/Conv1D/Conv2D/池化/Embedding 等层、常见损失函数、四种优化器（SGD/AdaGrad/RMSProp/AdamW）与三种学习率调度器，以及 zarr 压缩检查点持久化。自带 MNIST 数据集读取器与端到端示例模型。定位为教学、小中型项目与可复现实验，无 CUDA 支持，运行时依赖仅 numpy 与 zarr。通过 pip 安装，要求 Python 3.11+ 与 NumPy 2.x。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Tensor + 动态计算图自动微分，梯度以可读的显式 VJP 实现
- 内置 Conv/Pool/BatchNorm/Dropout/Embedding 等层与四种优化器
- zarr 支持的 zip 压缩检查点，保存/恢复超参数与优化器状态
- 自带 MNIST 读取器与端到端 'MNIST Beater' 示例模型

## 适用场景

- 学习深度学习内部机制（自动微分、反向传播的实现细节）
- 小型/中型项目上以少量依赖训练神经网络
- 做可复现实验与快速原型验证

## 场景标签

`教程课程` `模型训练` · 领域:学习与行业

## 证据(README 行号)

> L13: PureML is a learning-friendly deep-learning framework built entirely on top of **NumPy**. It aims to be **small, re
> L15: - **No hidden magic** — a Tensor class + autodiff engine with dynamic computation graph and efficient VJPs for back

## 星数曲线

```mermaid
xychart-beta
    title "Yehor-Mishchyriak/PureML 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-31"]
    y-axis "stars" 11 --> 14
    line [12, 13, 13]
```

2026-10-18 12 → 2026-10-31 13（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `762c651cd451` · [字段定义](../../DATASET.md)*
