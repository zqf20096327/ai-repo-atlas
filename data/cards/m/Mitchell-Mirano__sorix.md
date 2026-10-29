# Mitchell-Mirano/sorix

⭐ 18 · Python · MIT · 推送 2026-10-26 · [GitHub](https://github.com/Mitchell-Mirano/sorix) · 个人维护

**基于 NumPy/CuPy 的轻量深度学习库，PyTorch 风格 API**

构建于 NumPy/CuPy 之上的深度学习库，提供张量、自动微分引擎、Sequential API、基础层（Linear/ReLU/BatchNorm1D 等）、优化器（SGD/Adam/RMSprop）与数据加载器，支持 CPU 与经 CuPy 的 GPU 加速（需 CUDA）。API 设计参照 PyTorch，README 给出 MNIST 基准数据（体积与训练时间），并提供 pip/uv/Poetry 安装与 Colab 示例笔记本。卷积层（Conv2d/MaxPool2d）在路线图中尚未完成。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- NumPy（CPU）/CuPy（GPU）双后端
- 自动微分引擎与 PyTorch 风格 Sequential API
- 内置 SGD/Adam/RMSprop 优化器与数据加载器
- 模型 save/load 持久化与 Colab 示例笔记本

## 适用场景

- 研究和生产环境中训练轻量神经网络
- 资源受限或无服务器/边缘环境下运行模型
- 已有 PyTorch 经验的用户快速上手实验

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L18: **Sorix** is a high-performance, minimalist deep learning library built on top of NumPy/CuPy. Designed for research
> L24: * **⚡ High Performance**: Run optimized neural networks on NumPy (CPU) or CuPy (GPU).
> L90: - [x] **Core Autograd Engine** (NumPy/CuPy backends)

## 星数曲线

```mermaid
xychart-beta
    title "Mitchell-Mirano/sorix 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-29 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `a5e6cb4f070c` · [字段定义](../../DATASET.md)*
