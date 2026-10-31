# swarnimarun/coreml-rs

⭐ 16 · Rust · MIT · 推送 2026-05-20 · [GitHub](https://github.com/swarnimarun/coreml-rs) · [官网](https://crates.io/crates/coreml-rs) · 个人维护

**Apple Core ML 的 Rust 绑定库：加载模型并在 CPU/GPU/ANE 上推理**

基于 swift-bridge 封装 Apple Core ML 框架的 Rust 库，面向在 macOS 上进行本地模型推理的 Rust 开发者。支持从文件路径、原始字节或预编译缓存加载 .mlmodel/.mlpackage 模型，可单条或批量推理，并可选择 CPU、CPU+GPU 或 CPU+Apple Neural Engine 计算平台。另提供内存管理（加载/卸载/重载、缓冲持久化）、可配置退避重试与模型结构内省（输入输出形状、描述）。要求 macOS、Xcode 及 Command Line Tools，运行时需可找到 libswift_Concurrency.dylib。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 加载 .mlmodel/.mlpackage，支持单条与批量推理
- 计算平台可选 CPU、CPU+GPU、CPU+Apple Neural Engine
- 内存管理与可配置退避重试
- 模型内省（输入/输出形状与描述），支持 f32/f16/i32 输入

## 适用场景

- 在 Rust 项目中加载并运行 Core ML 模型做推理
- 指定 Neural Engine 或 GPU 加速 macOS 本地推理
- 内省模型输入输出结构以集成到应用

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L3: Rust bindings for Apple's Core ML framework using swift-bridge.
> L4: Load `.mlmodel` / `.mlpackage` files and run inference on macOS — with CPU, GPU, or Apple Neural Engine.

## 星数曲线

```mermaid
xychart-beta
    title "swarnimarun/coreml-rs 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `c39aaa832cb0` · [字段定义](../../DATASET.md)*
