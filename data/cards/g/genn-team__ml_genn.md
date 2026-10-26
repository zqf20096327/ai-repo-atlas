# genn-team/ml_genn

⭐ 44 · Python · LGPL-2.1 · 推送 2026-10-23 · [GitHub](https://github.com/genn-team/ml_genn) · [官网](https://ml-genn.readthedocs.io) · 组织维护

**基于 GeNN 的脉冲神经网络深度学习库，支持 ANN 转换与训练**

构建在 GeNN（GPU 增强的神经元网络仿真环境）之上的 Python 深度学习库，面向使用脉冲神经网络的研究与开发场景。提供两条主要路径：将 Keras 定义的 ANN 以 few-spike 等方法转换为 SNN，以及使用 e-prop 学习规则直接训练 SNN。安装需先装 PyGeNN，再分别以 setuptools 在 ml_genn 与 ml_genn_tf 目录执行 pip install .。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | LGPL-2.1 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 将 Keras 定义的 ANN 模型转换为 SNN（few-spike 转换方法）
- 支持 e-prop 学习规则直接训练 SNN
- 基于 GeNN 的 GPU 增强神经元网络仿真环境

## 适用场景

- 把已有 Keras ANN 模型转换为脉冲神经网络运行
- 使用 e-prop 规则从头训练 SNN
- 在 GPU 仿真环境下做 SNN 深度学习实验

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L4: A library for deep learning with Spiking Neural Networks (SNN)powered by GeNN, a GPU enhanced Neuronal Network simul
> L14: The following example illustrates how to convert an ANN model, defined in Keras, to an SNN using the few-spike (Stö

## 星数曲线

```mermaid
xychart-beta
    title "genn-team/ml_genn 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 43 --> 45
    line [44, 44]
```

2026-10-18 44 → 2026-10-26 44（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `b998426f997d` · [字段定义](../../DATASET.md)*
