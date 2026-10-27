# ahmedfgad/NeuralGenetic

⭐ 254 · Python · 推送 2026-10-17 · [GitHub](https://github.com/ahmedfgad/NeuralGenetic) · [官网](https://pygad.readthedocs.io) · 个人维护

**用遗传算法训练神经网络的 Python 库（PyGAD 的 gann 模块源码仓库）**

NeuralGenetic 是 PyGAD 库的 pygad.gann 模块源码仓库，用于以遗传算法代替常规优化器训练神经网络，支持回归与分类任务（自 PyGAD 2.7.0 起）。训练过程通过 GA 生命周期回调（on_start/on_fitness/on_generation 等）控制，可设置代数或由回调返回 stop 终止。底层依赖 NumPy 实现的前馈网络（pygad.nn），另有 Keras/Torch 权重优化配套模块。安装通过 pip install pygad 完成，文档托管于 Read the Docs。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 用遗传算法训练回归/分类神经网络（PyGAD 2.7.0 起）
- 提供 GA 生命周期回调（on_start/on_fitness/on_generation）控制训练过程
- 配套模块覆盖 Keras 与 PyTorch 权重的遗传算法优化（kerasga/torchga）

## 适用场景

- 我需要用遗传算法而非梯度下降来训练神经网络
- 我想优化 Keras 或 PyTorch 模型的权重
- 我在学习遗传算法与神经网络的结合实现

## 场景标签

 · 领域:机器学习/优化

## 证据(README 行号)

> L3: NeuralGenetic is a Python project for training neural networks using the genetic algorithm.
> L5: NeuralGenetic is part of the PyGAD library which is an open-source Python 3 library for implementing the genetic alg

## 星数曲线

```mermaid
xychart-beta
    title "ahmedfgad/NeuralGenetic 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 253 --> 255
    line [254, 254]
```

2026-10-18 254 → 2026-10-27 254（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `a86026ab05a1` · [字段定义](../../DATASET.md)*
