# google-deepmind/xarray_jax

⭐ 53 · Python · Apache-2.0 · 推送 2026-06-08 · [GitHub](https://github.com/google-deepmind/xarray_jax) · 组织维护

**让 xarray 数据结构可作为 JAX PyTree 参与变换的兼容库**

将 xarray 的 DataArray/Dataset 注册为 JAX 自定义 PyTree，使其能直接进入 jit、grad、vmap 等核心变换：JAX 展平时抽取原始数组做加速计算，重建时恢复维度名与坐标等元数据。提供 vmap/pmap 包装（面向遗留代码）、基于 jax.sharding 的 SPMD 分片集成、沿命名维度的 scan 包装、动态可追踪坐标的 jax_coords 实验参数，以及处理非数组叶节点的 NonArrayLeafWrapper。jax_coords 被 GenCast 等 DeepMind 研究模型使用，但被标注为实验性且可能更换方案。

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

- 注册 xarray 结构为 JAX PyTree，支持 jit/grad/vmap 等变换
- 与 jax.sharding（NamedSharding、device meshes）集成实现 SPMD 分片
- 提供命名维度感知的 vmap/pmap/scan 包装
- NonArrayLeafWrapper 处理 PyTree 中的非数组叶节点，兼容 Flax 等上层库

## 适用场景

- 在 JAX 中对带标签的多维数据做自动微分与 JIT 编译
- 将 xarray Dataset 沿 batch 维度做 SPMD 分片并行
- 在时间序列模拟或循环计算中沿命名维度使用 scan

## 场景标签

 · 领域:科学计算/机器学习基础设施

## 证据(README 行号)

> L4: This library supports using xarray
> L28: **This library solves that problem.** It registers `xarray` data structures as

## 星数曲线

```mermaid
xychart-beta
    title "google-deepmind/xarray_jax 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 52 --> 54
    line [53, 53]
```

2026-10-18 53 → 2026-10-27 53（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `33f5c6847018` · [字段定义](../../DATASET.md)*
