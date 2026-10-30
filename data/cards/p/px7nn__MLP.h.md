# px7nn/MLP.h

⭐ 18 · C · MIT · 推送 2026-07-27 · [GitHub](https://github.com/px7nn/MLP.h) · 个人维护

**给 C 开发者的单头文件多层感知机库，零依赖**

以单个头文件 MLP.h 形式提供的 C 语言多层感知机实现：复制进项目、在一个 .c 文件中定义 MLP_IMPLEMENTATION 即可用，无构建系统、无链接、除标准库外无外部依赖。支持任意拓扑配置、多种激活函数（ReLU/Leaky ReLU/Sigmoid/Tanh/Softmax/Linear）、权重初始化器（He/Xavier/自动）与损失函数（MSE/BCE/CCE/自动推断）。内置模型保存加载、CSV 数据加载与全局错误报告系统。附带 XOR、MNIST、正弦拟合等训练示例与在线 MNIST 分类器演示。项目声明 pre-1.0，公开 API 可能在次版本间变动。

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

- 单头文件、C99/C11、零外部依赖，无需构建系统
- 任意拓扑、多种激活函数/初始化器/损失函数配置
- 模型二进制持久化与内置 CSV 加载
- 附 XOR/MNIST/正弦拟合等训练示例

## 适用场景

- 在 C 项目中嵌入小型神经网络训练与推理
- 学习前向传播、反向传播与训练循环的实现
- 不引入依赖快速搭建 MLP 原型做分类或拟合

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L3: **A tiny, single-header, dependency-free Multi-Layer Perceptron library for C.**
> L29: - **Flexible Network Configuration:** Configure arbitrary topologies, activation functions (`ReLU`, `Leaky ReLU`, `

## 星数曲线

```mermaid
xychart-beta
    title "px7nn/MLP.h 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-30 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `aed316ba8686` · [字段定义](../../DATASET.md)*
