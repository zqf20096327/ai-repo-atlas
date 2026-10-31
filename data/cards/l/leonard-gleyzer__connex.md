# leonard-gleyzer/connex

⭐ 23 · Python · Apache-2.0 · 推送 2026-06-29 · [GitHub](https://github.com/leonard-gleyzer/connex) · [官网](https://leonard-gleyzer.github.io/connex/) · 个人维护

**JAX 库：以 DAG 定义并动态编辑神经网络拓扑**

构建在 Equinox 之上的 JAX 神经网络库，将网络拓扑表示为有向无环图并编译为可训练的 Equinox 模块。支持在保留兼容参数的前提下增删连接或神经元、组合内置或自定义图操作、配置标量或逐节点 dropout、选用 padded/sparse/matmul/混合 affine 后端，并可导出训练参数为 NetworkX 加权有向图。训练遵循标准 Equinox 与 Optax 模式，编辑操作返回新模型、不改动原模型。通过 uv 安装。

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

- DAG 编译为可训练 Equinox 模块
- 训练后动态增删连接或神经元且保留兼容参数
- padded/sparse/matmul/混合 affine 后端，长链段自动用 jax.lax.scan
- 参数可导出为 NetworkX 加权有向图

## 适用场景

- 研究拓扑结构可变的神经网络
- 训练中动态修剪或扩展网络连接
- 将网络结构与权重导出做图分析

## 场景标签

 · 领域:深度学习/科研工具

## 证据(README 行号)

> L3: Connex is a JAX library built on
> L4: Equinox for trainable neural
> L5: networks whose topology is defined by a directed acyclic graph.

## 星数曲线

```mermaid
xychart-beta
    title "leonard-gleyzer/connex 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-31 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `376a2507e42f` · [字段定义](../../DATASET.md)*
