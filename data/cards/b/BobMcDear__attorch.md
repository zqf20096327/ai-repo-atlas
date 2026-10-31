# BobMcDear/attorch

⭐ 605 · Python · MIT · 推送 2026-08-14 · [GitHub](https://github.com/BobMcDear/attorch) · 个人维护

**用 Triton 实现的 PyTorch 神经网络层子集库，供开发者改写**

attorch 是用纯 Python 与 OpenAI Triton 编写的 PyTorch nn 模块子集，覆盖卷积、池化、注意力、40 余种激活/归一化层及损失函数，支持 AMP 混合精度、前向与反向传播，可用于训练与推理。面向想开发自定义深度学习算子但不具备编写 CUDA 内核能力或资源的开发者，定位为可 fork、自包含、易改写的起点。附带 attorch.nn 接口（缺失层回退到 PyTorch）、attorch.math 纯数学函数集、对照 PyTorch 的测试与示例。卷积与池化层性能慢于 PyTorch。

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

- 覆盖卷积/池化/注意力/激活/归一化/损失等层，支持 AMP 与前向反向传播
- attorch.nn 提供 PyTorch 回退接口，可部分替换 torch.nn
- attorch.math 提供纯数学函数，梯度可经 triton-autodiff 自动推导
- 提供与 PyTorch 对照的测试（pytest）与示例工作流

## 适用场景

- 在不写 CUDA 内核的前提下开发自定义深度学习算子
- fork 一个可读的 Triton 层实现作为研究或改造起点
- 在训练与推理中替换部分 torch.nn 层并利用算子融合

## 场景标签

 · 领域:深度学习/算子库

## 证据(README 行号)

> L14: attorch is a subset of PyTorch's ```nn``` module, written purely in Python using OpenAI's Triton. Its goal is to be
> L16: There already exist a number of wonderful PyTorch-like frameworks powered by Triton, including kernl, xFormers, Uns

## 星数曲线

```mermaid
xychart-beta
    title "BobMcDear/attorch 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 604 --> 606
    line [605, 605]
```

2026-10-18 605 → 2026-10-31 605（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `b9d158f91329` · [字段定义](../../DATASET.md)*
