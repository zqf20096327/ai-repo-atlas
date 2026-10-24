# kornia/kornia-rs

⭐ 740 · Rust · Apache-2.0 · 推送 2026-10-23 · [GitHub](https://github.com/kornia/kornia-rs) · [官网](https://docs.rs/kornia) · 组织维护 · 中文 README

**Rust 底层计算机视觉库：快速图像 I/O 与 CPU/GPU 图像处理**

用 Rust 编写的底层计算机视觉库 kornia，提供线程安全的图像读取（AVIF/JPEG/PNG/WebP 等 14 种格式）与图像处理操作（灰度、缩放、裁剪、旋转、归一化等），同一 API 按数据驻留位置在 CPU 或 NVIDIA GPU 上调度。通过 DLPack 与 CUDA Array Interface 和 PyTorch/TensorRT 零拷贝互操作，并提供融合的 NV12/YUYV→归一化 CHW 单 CUDA kernel 预处理器，面向实时相机流水线。经 PyO3/Maturin 提供 Python 绑定，发布 Linux/macOS/Windows wheel，同一 wheel 无 GPU 时运行 CPU 路径。面向计算机视觉与机器人开发者。

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

- 同一 Image API 按 CPU/GPU 数据驻留自动调度
- DLPack/CUDA Array Interface 与 PyTorch、TensorRT 零拷贝互操作
- 单 CUDA kernel 融合 resize+normalize+HWC→CHW 的 Preprocessor
- libjpeg-turbo 解码与 SIMD (NEON/AVX2) 加速，支持 Python 3.8–3.14 含自由线程构建

## 适用场景

- 实时相机流水线中做 GPU 常驻的图像预处理并直连推理引擎
- 在 Rust 或 Python 项目中做高性能图像读取与处理
- 将相机帧融合为归一化模型输入，无主机拷贝开销

## 场景标签

`图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L13: The `kornia` crate is a low-level computer vision library for Rust 🦀
> L15: Fast, thread-safe image I/O and processing with a single API that runs on the CPU or an NVIDIA GPU — the same `Imag
> L57: - Convert images to grayscale, resize, crop, rotate, flip, pad, normalize, denormalize, and other image processing 

## 星数曲线

```mermaid
xychart-beta
    title "kornia/kornia-rs 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-24"]
    y-axis "stars" 738 --> 741
    line [739, 740, 740]
```

2026-10-18 739 → 2026-10-24 740（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `4d1fce7f2cb2` · [字段定义](../../DATASET.md)*
