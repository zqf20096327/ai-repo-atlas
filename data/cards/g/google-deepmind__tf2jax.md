# google-deepmind/tf2jax

⭐ 125 · Python · Apache-2.0 · 推送 2026-10-14 · [GitHub](https://github.com/google-deepmind/tf2jax) · 组织维护

**将 TensorFlow 函数/图转换为 JAX 函数的实验性转换库**

Google DeepMind 维护的转换库：通过追踪 tf.function 生成 GraphDef，转换为等价的 JAX 函数，转换后可继续应用 jit/grad/vmap 等 JAX 变换。支持从 SavedModel、TF-Hub（TF1 格式）加载并转换，也可将 jax2tf 序列化的函数转回 JAX。面向需要在 JAX 代码库中复用或微调既有 TF 模型的开发者。限制：仅支持部分 TF 算子，TF1 控制流不支持，API 不稳定。

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

- tf.function → JAX 函数转换，可继续应用 JAX 变换（jit/grad/vmap 等）
- 支持 SavedModel 与 TF-Hub（TF1 格式）加载转换
- jax2tf 输出可经 convert_functional 转回 JAX 代码
- 支持 XlaCallModule（StableHLO 原生序列化）与 bfloat16 常量精度配置

## 适用场景

- 在 JAX 代码库中复用或微调已有的 TensorFlow SavedModel
- 将 jax2tf 序列化的函数重新接回 JAX 工作流
- 对转换后的模型做形状/精度（bfloat16）控制与调试

## 场景标签

 · 领域:机器学习框架工具

## 证据(README 行号)

> L6: TF2JAX is an experimental library for converting [TensorFlow] functions/graphs
> L46: TF2JAX enables existing TensorFlow functions and models (including
> L337: This repository is part of the [DeepMind JAX Ecosystem], to cite TF2JAX please

## 星数曲线

```mermaid
xychart-beta
    title "google-deepmind/tf2jax 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 124 --> 126
    line [125, 125]
```

2026-10-18 125 → 2026-10-26 125（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `736db5f43761` · [字段定义](../../DATASET.md)*
