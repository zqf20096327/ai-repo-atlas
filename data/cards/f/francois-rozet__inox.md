# francois-rozet/inox

⭐ 37 · Python · MIT · 推送 2026-06-13 · [GitHub](https://github.com/francois-rozet/inox) · [官网](https://inox.readthedocs.io) · 个人维护

**极简 JAX 神经网络库：PyTree 模块与提升变换**

Inox 是一个基于 JAX 的极简神经网络库，提供类 PyTorch 语法的模块定义。模块以 PyTree 表示，支持复杂架构与函数式变换。相较 Equinox 只保留核心特性（PyTree 与提升变换），组件与 Equinox 生态大部分可互换，并借鉴 NNX 与 Serket 的接口设计。提供提升变换，将非数组叶节点视为静态以保持与 JAX 变换兼容；另提供分区机制，将模块的静态定义与动态内容（参数等）分离，便于参数更新。以 pip 安装的 Python 库形式提供。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 类 PyTorch 语法的模块定义
- 提升变换将非数组叶节点视为静态
- 静态定义与动态参数的分区机制
- 组件与 Equinox 生态大部分可互换

## 适用场景

- 在 JAX 中以直观语法定义神经网络
- 在含字符串/布尔标志的模型上使用 jit 等变换
- 分离模型结构与参数以便更新参数

## 场景标签

 · 领域:深度学习/框架

## 证据(README 行号)

> L5: Inox is a minimal JAX library for neural networks with an intuitive PyTorch-like syntax. As with Equinox, modules ar
> L7: Inox aims to be a leaner version of Equinox by only retaining its core features: PyTrees and lifted transformations.

## 星数曲线

```mermaid
xychart-beta
    title "francois-rozet/inox 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 36 --> 38
    line [37, 37]
```

2026-10-18 37 → 2026-10-30 37（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `ba5144816420` · [字段定义](../../DATASET.md)*
