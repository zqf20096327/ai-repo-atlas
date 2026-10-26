# amirhossein-razlighi/mlx3D

⭐ 43 · Python · MIT · 推送 2026-10-25 · [GitHub](https://github.com/amirhossein-razlighi/mlx3D) · [官网](https://amirhossein-razlighi.github.io/mlx3D/) · 个人维护

**面向 Apple Silicon 的可微 3D 视觉库：网格、NeRF、3D 高斯泼溅**

基于 MLX 构建的 Python 3D 计算机视觉库，将 PyTorch3D 风格的工作流带到 Mac 上：批量网格/点云结构、相机模型、可微渲染、NeRF 与带自定义 Metal 内核的 3D Gaussian Splatting，原生运行于 Apple GPU。提供 mlx3d-capture 一条命令从照片或手机视频训练 splat（含 COLMAP-free SfM）、交互式浏览器查看器、快速前向光栅化路径及 OBJ/PLY 读写。通过 pip 安装，要求 Apple Silicon Mac 与 Python ≥ 3.10。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 3DGS CUDA 光栅器的 Metal 移植（tile-based 前向/反向内核）
- mlx3d-capture 从照片/视频到训练 splat 的一条命令流水线（内置 COLMAP-free SfM）
- 批量 Meshes/Pointclouds、相机变换、chamfer/SSIM 等可微算子与损失
- FastGaussianRenderer 前向快速光栅化路径与浏览器交互查看器

## 适用场景

- 在 Mac 上从照片或手机视频重建 3D 高斯 splat
- 训练 NeRF / 3DGS 并交互查看与渲染导出
- 做可微网格渲染、点云拟合等几何优化研究

## 场景标签

`图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L9: **Differentiable 3D computer vision on Apple Silicon, built on MLX.**
> L11: MLX3D brings the PyTorch3D workflow to Macs: batched 3D data structures, cameras, differentiable rendering, and mod
> L22: - **Gaussian Splatting** — a Metal translation of the reference CUDA rasterizer (tile-based forward & backward kern

## 星数曲线

```mermaid
xychart-beta
    title "amirhossein-razlighi/mlx3D 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-26"]
    y-axis "stars" 41 --> 44
    line [42, 43, 43]
```

2026-10-18 42 → 2026-10-26 43（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `24fba043a064` · [字段定义](../../DATASET.md)*
