# masadcv/FastGeodis

⭐ 108 · C++ · BSD-3-Clause · 推送 2026-03-12 · [GitHub](https://github.com/masadcv/FastGeodis) · [官网](https://fastgeodis.readthedocs.io) · 个人维护

**面向开发者的通用测地距离变换 PyTorch 库（CPU/GPU）**

以 PyTorch 为接口提供 2D/3D 广义测地距离变换的 CPU（OpenMP）与 GPU（CUDA）实现，基于可并行化的 raster scan 思路，可计算测地距离、欧氏距离变换及二者混合，另含测地对称滤波（GSF）用于交互式分割。同时提供 Toivanen、Pixel Queue、Fast Marching 等 CPU 实现版本。面向在深度学习与图像处理管线中使用此类变换的开发者与科研人员；raster scan 实现以速度优先而非精确结果，CUDA 需配合已安装 PyTorch 的 conda 环境使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | BSD-3-Clause |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 2D/3D 广义测地距离变换的 CPU（OpenMP）与 GPU（CUDA）并行实现
- 测地/欧氏距离变换及二者混合的计算
- 测地对称滤波（GSF）用于交互式分割
- 提供 Toivanen、Pixel Queue、Fast Marching 多种 CPU 实现与单元测试

## 适用场景

- 在 PyTorch 深度学习管线中嵌入可微的测地距离变换
- 医学图像交互式分割中的测地对称滤波
- 需要 GPU 加速的 2D 图像/3D 体积距离变换计算

## 场景标签

`图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L8: This repository provides CPU (OpenMP) and GPU (CUDA) implementations of Generalised Geodesic Distance Transform in P
> L14: The above raster scan method can be parallelised for each row/plane on an available device (CPU or GPU). This leads

## 星数曲线

```mermaid
xychart-beta
    title "masadcv/FastGeodis 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 107 --> 109
    line [108, 108]
```

2026-10-18 108 → 2026-10-24 108（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `1f0e8ac6a906` · [字段定义](../../DATASET.md)*
