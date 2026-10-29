# pedronahum/MetalHLO

⭐ 26 · MLIR · Apache-2.0 · 推送 2026-10-12 · [GitHub](https://github.com/pedronahum/MetalHLO) · 个人维护

**在 Apple Silicon GPU 上执行 StableHLO 的编译器与 JAX 后端**

面向 Apple Silicon（M1–M5）的 StableHLO MLIR 编译执行器：将 StableHLO 程序编译为 Metal 内核并执行，提供 Swift、C 和 PJRT API，可注册为标准 JAX 后端使 `import jax` 运行在 Apple GPU 上，也可作为独立库供任何产出 StableHLO 的程序使用。含三种执行后端（MPSGraph、自定义 Metal 内核、GPU+ANE+CPU 异构）与 XLA 风格 O0–O3 优化器，支持完整训练。限制：仅静态形状、单块 Apple GPU、macOS 专属；O3 与分布式为实验性。

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

- 通过 PJRT 插件作为标准 JAX 后端，兼容 jit/grad/vmap/scan 与 Flax/optax 训练
- 三种执行后端：MPSGraph、自定义 Metal 内核、GPU+ANE+CPU 异构并行
- XLA 风格优化器（O0–O3），含 attention/FFN/LayerNorm/GELU/softmax 模式融合
- 覆盖 fp32/fp16/bfloat16 前向与梯度训练，Linear algebra 经 LAPACK FFI 路由

## 适用场景

- 在 Mac 上让 JAX/Flax 程序直接跑 Apple GPU 训练与推理
- C/C++/Swift 工程嵌入 StableHLO 编译执行能力
- 利用统一内存在 GPU、神经引擎与 CPU 间做异构调度

## 场景标签

`推理引擎` `模型训练` · 领域:训练与推理

## 证据(README 行号)

> L5: MetalHLO compiles and executes StableHLO MLIR
> L7: PJRT APIs, so it works as a JAX
> L10: - **JAX backend** via the standard PJRT plugin — `import jax` runs on the Apple GPU.

## 星数曲线

```mermaid
xychart-beta
    title "pedronahum/MetalHLO 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-29"]
    y-axis "stars" 24 --> 27
    line [25, 26, 26]
```

2026-10-18 25 → 2026-10-29 26（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `9eed1e4d57d1` · [字段定义](../../DATASET.md)*
