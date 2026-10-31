# lcmialichi/php-gpu-tensors

⭐ 19 · C · MIT · 推送 2026-10-21 · [GitHub](https://github.com/lcmialichi/php-gpu-tensors) · 个人维护

**PHP 原生张量与 CUDA 扩展：在 PHP 中做 CPU/GPU 数值计算**

原生 PHP 扩展（C/C++ 编译，扩展名 phptensors），提供 13 种 dtype 的 CPU 张量 HostArray 与 CUDA 后端 CudaArray，数据搬运显式（toGpu/toHost）。GPU 侧支持反向自动微分、SGD/AdamW 优化器、NVRTC 运行时编译自定义 CUDA C++ 内核、可选 kernel fusion 与 CUDA Graphs 回放、cuDNN CNN 推理；自述为低层张量库而非完整 ML 框架。面向想用 PHP 做数值计算/机器学习实验的开发者。限 Linux，PHP 8.1-8.5，Windows/macOS 原生构建不支持，处于 beta，每进程单 CUDA 设备，非所有操作可融合。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- CPU HostArray 与 CUDA CudaArray 双后端，13 种 dtype，数据搬运显式
- 反向自动微分 + SGD/AdamW，支持 MNIST MLP 训练示例
- NVRTC 运行时编译自定义 CUDA C++ 内核
- 可选 Fusion 捕获/回放与 CUDA Graphs，cuDNN CNN 推理

## 适用场景

- 在 PHP 项目中做张量运算与批矩阵乘法
- 不依赖 Python 运行时在 NVIDIA GPU 上训练小型模型（MLP/CNN 推理）
- 从 PHP 编写并运行时编译 CUDA 自定义内核

## 场景标签

 · 领域:数值计算/GPU 计算

## 证据(README 行号)

> L12: PHP Tensors is a **native PHP extension** for numerical computing, GPU tensor
> L33: - **Tools beyond array math:** reverse-mode autograd, functional SGD/AdamW,
> L34:  runtime-compiled CUDA C++ kernels and optional cuDNN CNN inference.

## 星数曲线

```mermaid
xychart-beta
    title "lcmialichi/php-gpu-tensors 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-31 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `09ca45c13875` · [字段定义](../../DATASET.md)*
