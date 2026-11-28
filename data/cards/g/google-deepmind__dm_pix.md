# google-deepmind/dm_pix

⭐ 453 · Python · Apache-2.0 · 推送 2026-11-05 · [GitHub](https://github.com/google-deepmind/dm_pix) · [官网](https://dm-pix.readthedocs.io) · 组织维护

**面向 JAX 用户的图像处理函数库，可被 JIT 编译与并行化**

PIX 是 DeepMind 维护的基于 JAX 的图像处理库，提供可在 JAX 中优化与并行化的图像处理函数和工具。所有函数支持 jax.jit、jax.vmap、jax.pmap，从而利用 JAX 的编译优化与加速器并行能力。库本身为纯 Python 实现，依赖 JAX（其安装因 CUDA 版本而异，故未列入强制依赖）。通过 PyPI 以 dm-pix 包名分发，附带 examples/ 示例目录、pytest 测试套件与隔离环境测试脚本，并作为 DeepMind JAX Ecosystem 的一部分提供引用条目。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 所有函数支持 jax.jit/jax.vmap/jax.pmap 编译与并行化
- 纯 Python 实现，pip 安装即用
- 提供 examples 示例与 pytest 测试套件
- 属于 DeepMind JAX Ecosystem 并提供官方引用条目

## 适用场景

- 为 JAX 机器学习流程添加图像预处理与增广操作
- 在 GPU/TPU 上以 jit/vmap/pmap 并行批量处理图像
- 作为 JAX 生态图像处理的起点示例学习

## 场景标签

`图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L3: PIX is an image processing library in [JAX], for [JAX].
> L15: PIX is a library built on top of JAX with the goal of providing image processing
> L16: functions and tools to JAX in a way that they can be optimised and parallelised

## 星数曲线

```mermaid
xychart-beta
    title "google-deepmind/dm_pix 星数(近 3 点)"
    x-axis ["2026-10-26", "2026-11-10", "2026-11-28"]
    y-axis "stars" 451 --> 454
    line [452, 453, 453]
```

2026-10-26 452 → 2026-11-28 453（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-25 · 置信度 high · 依据 README sha `d34ccd86495e` · [字段定义](../../DATASET.md)*
