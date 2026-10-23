# openmm/NNPOps

⭐ 102 · C++ · NOASSERTION · 推送 2026-06-09 · [GitHub](https://github.com/openmm/NNPOps) · 组织维护

**神经网络势能瓶颈算子的高性能实现库，面向分子模拟推理**

为神经网络势能（NNP）提供核心瓶颈算子的开源优化实现，包含 ANI 对称函数、CFConv 连续滤波卷积、邻居对枚举与 PME 等操作，可从 Python 调用。每个算子自包含、API 简单，便于嵌入其他代码。同时提供纯 C++ CPU 实现与 CUDA 实现，CUDA 版做了优化而 CPU 版未做调优。代码面向推理（运行模拟）而非训练，只计算对粒子位置的梯度而非模型参数梯度。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 提供 ANI 对称函数、CFConv、邻居对枚举、PME 四类算子的 Python 接口
- 全部算子均有纯 C++ CPU 与 CUDA 两种实现
- 算子自包含，可嵌入任意需要它的代码
- 面向推理：计算对粒子位置的梯度，不支持训练

## 适用场景

- 加速神经网络势能分子模拟的瓶颈计算
- 在自己的分子动力学代码中嵌入优化的 NNP 算子
- 在 GPU 上运行 NNP 模拟获得优化性能

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L7: The goal of this project is to promote the use of neural network potentials (NNPs)
> L23: 5. This code is designed for inference (running simulations), not training (creating

## 星数曲线

```mermaid
xychart-beta
    title "openmm/NNPOps 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 101 --> 103
    line [102, 102]
```

2026-10-18 102 → 2026-10-23 102（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `d12bb24b41b0` · [字段定义](../../DATASET.md)*
