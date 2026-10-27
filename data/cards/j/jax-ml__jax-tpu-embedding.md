# jax-ml/jax-tpu-embedding

⭐ 38 · Python · Apache-2.0 · 推送 2026-10-24 · [GitHub](https://github.com/jax-ml/jax-tpu-embedding) · [官网](https://jax-tpu-embedding.readthedocs.io/) · 组织维护

**JAX 在 TPU SparseCore 上做大规模嵌入加速的库**

JAX SparseCore 提供 Python 库，用于利用 TPU v5 及后续世代中的 SparseCore 加速器，加速涉及不规则稀疏内存访问与计算的工作负载，典型场景为深度学习推荐模型的嵌入查找，也可加速高带宽内存（HBM）中大规模数据集上的其他动态稀疏工作负载。通过 PyPI 以 pip 安装；使用 TPU 加速需要可访问 TPU v5+ 硬件及对应 jax/jaxlib TPU 版本。README 声明为研究项目而非官方 Google 产品，可能存在不完善之处。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 利用 TPU v5+ SparseCore 加速嵌入查找等稀疏工作负载
- 支持 HBM 中大规模数据集上的动态稀疏负载
- 通过 pip 从 PyPI 安装，附文档、规范与 Flux/Primitives 教程（Flax）

## 适用场景

- 在 TPU 上加速深度学习推荐模型的嵌入层
- JAX 项目中处理大规模稀疏嵌入计算
- 需要高带宽内存访问的稀疏负载加速

## 场景标签

 · 领域:深度学习基础设施/稀疏计算

## 证据(README 行号)

> L13: JAX SparseCore provides support for leveraging the SparseCore accelerators
> L18: computation. While they excel at tasks like embedding lookups (common in deep

## 星数曲线

```mermaid
xychart-beta
    title "jax-ml/jax-tpu-embedding 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-27"]
    y-axis "stars" 36 --> 39
    line [37, 38, 38]
```

2026-10-18 37 → 2026-10-27 38（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `353b79c68e74` · [字段定义](../../DATASET.md)*
