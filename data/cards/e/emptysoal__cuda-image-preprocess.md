# emptysoal/cuda-image-preprocess

⭐ 86 · Cuda · MIT · 推送 2025-11-05 · [GitHub](https://github.com/emptysoal/cuda-image-preprocess) · 个人维护 · 中文 README

**CUDA 加速图像预处理代码集，可配合 TensorRT 推理使用**

基于 CUDA 与 OpenCV 的 C++ 图像预处理项目：提供 BGR2RGB、双线性 Resize、HWC2CHW、Normalize 等单一操作的 CUDA kernel，以及串联全部操作的统一预处理模块，可单独用于加速图像操作，或与 TensorRT 推理流程结合使用。README 给出 Deeplabv3+ 与 YOLOv5-v5.0 在 FP32/FP16/INT8 下预处理前后的推理耗时对比数据。需自行编译（make），CUDA/OpenCV 安装路径与 Makefile 不一致时需手动修改。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 提供 BGR2RGB、bilinear、HWC2CHW、Normalize 等单一操作的 CUDA kernel
- 统一预处理模块一次完成 Resize/BGR2RGB/HWC2CHW/Normalize
- 可与 TensorRT 推理流程结合（提供 union_tensorrt 目录）
- README 给出 Deeplabv3+ 与 YOLOv5 在不同精度下的推理耗时对比数据

## 适用场景

- 在 TensorRT 推理前用 CUDA 加速图像预处理环节
- 单独使用某个图像操作（如 BGR 转 RGB）的 CUDA 加速版本
- 搭建 C++ 深度学习推理流水线时参考预处理 kernel 实现

## 场景标签

`图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L8:  - 单独使用，以加速图像处理操作；
> L9:  - **结合 TensorRT 使用，进一步加快推理速度**
> L57: - 在推理之前，图像通常需经过 Resize、BGR to RGB、HWC to CHW、Normalize

## 星数曲线

```mermaid
xychart-beta
    title "emptysoal/cuda-image-preprocess 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 85 --> 87
    line [86, 86]
```

2026-10-18 86 → 2026-10-31 86（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `2eb02450b229` · [字段定义](../../DATASET.md)*
