# NVIDIA/warp

⭐ 7,338 · Python · Apache-2.0 · 推送 2026-11-22 · [GitHub](https://github.com/NVIDIA/warp) · [官网](https://nvidia.github.io/warp/stable/) · 组织维护

**面向仿真、机器人与机器学习的 GPU 加速 Python 框架**

NVIDIA Warp 将常规 Python 函数 JIT 编译为可在 CPU 或 GPU 上运行的内核代码，内置物理仿真、机器人与几何处理等原语，内核可微并可接入 PyTorch、JAX、Paddle 等机器学习管线。支持 Windows/Linux/macOS 多平台安装，CUDA 加速要求 R580 系列以上驱动与 Turing（sm_75）以上 GPU；提供示例目录、教程 Notebook 与 Colab 入口，源码构建时会下载受 NVIDIA 协议约束的 libmathdx。

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

- Python 函数 JIT 编译为 CPU/GPU 内核
- 内核可微，可与 PyTorch/JAX/Paddle 组成机器学习管线
- PyPI 提供 warp-lang 预编译 wheel，另提供 nightly、conda 与源码构建
- 示例覆盖物理仿真、几何处理、优化与 tile 式 GPU 编程

## 适用场景

- 编写物理仿真程序并利用 GPU 加速运行
- 搭建可微分仿真并与机器学习框架联合训练
- 处理网格、等值面等几何计算任务
- 在 Colab 中运行 Warp 教程 Notebook 学习入门

## 场景标签

 · 领域:开发工具/GPU 计算与仿真

## 证据(README 行号)

> L12: Warp is a Python framework for GPU-accelerated simulation, robotics, and machine learning. Warp takes
> L16: and more. Warp kernels are differentiable and can be used as part of machine-learning pipelines
> L34: Warp requires Python 3.11 or newer. We publish `warp-lang` wheels on PyPI for Windows (x86-64 and experimental Arm6

## 星数曲线

```mermaid
xychart-beta
    title "NVIDIA/warp 星数(近 25 点)"
    x-axis ["2026-10-20", "2026-10-22", "2026-10-23", "2026-10-24", "2026-10-25", "2026-10-26", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23"]
    y-axis "stars" 7202 --> 7350
    line [7214, 7219, 7226, 7230, 7233, 7237, 7245, 7248, 7252, 7256, 7259, 7263, 7233, 7285, 7300, 7306, 7312, 7314, 7317, 7321, 7325, 7332, 7335, 7337, 7338]
```

2026-10-20 7,214 → 2026-11-23 7,338（+124）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 high · 依据 README sha `b2a2b7953dcf` · [字段定义](../../DATASET.md)*
