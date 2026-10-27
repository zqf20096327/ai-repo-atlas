# KarelPeeters/Kyanite

⭐ 74 · Rust · NOASSERTION · 推送 2026-03-15 · [GitHub](https://github.com/KarelPeeters/Kyanite) · 个人维护

**Rust 神经网络推理库：运行 ONNX 模型于 CPU 或 Nvidia GPU**

用 Rust 编写的神经网络推理库，可加载 ONNX 文件并在 CPU（BLAS）或 Nvidia GPU（CUDA/cuDNN/cuBLAS）上执行。核心是 SSA 风格的图 IR 与图优化器（常量折叠、算子融合等）；GPU 路径含 Cuda Planner 生成执行计划，并用基于 NVRTC 的 autokernel 框架在运行时编译自定义内核。已测试全连接网络、ResNet CNN、LLaMA 与 Stable Diffusion。由 kn-graph、kn-cuda-sys、kn-cuda-eval、kn-runtime 及实验性 Python 包装 kn-python 五个 crate 组成。GPU 使用需自行安装 CUDA（测试版本 12.2）与 cuDNN（8.9.5）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- ONNX 加载并转换为内部图 IR，支持多种网络类型
- GPU 路径含 Cuda Planner 与 NVRTC 运行时编译自定义内核
- 图优化器提供常量折叠与多种算子融合
- 多 crate 结构，可运行时选择 CPU/GPU 执行

## 适用场景

- 在 Rust 项目中本地运行 ONNX 训练好的模型
- 在 Nvidia GPU 上做带算子融合的推理
- 作为库嵌入需要 LLM/CNN/图像生成模型推理的应用

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L13: Kyanite is a neural network inference library, written in/for Rust. It can run ONNX files either on the CPU or on N
> L30: * `kn-runtime`: A wrapper around the other crates to allow selecting between CPU and GPU execution at runtime.

## 星数曲线

```mermaid
xychart-beta
    title "KarelPeeters/Kyanite 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 73 --> 75
    line [74, 74]
```

2026-10-18 74 → 2026-10-27 74（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `fef19ee051f5` · [字段定义](../../DATASET.md)*
