# Raessan/depth_anything_v3_deepstream

⭐ 23 · C++ · Apache-2.0 · 推送 2026-04-06 · [GitHub](https://github.com/Raessan/depth_anything_v3_deepstream) · 个人维护

**Depth Anything V3 单目深度估计的 DeepStream/TensorRT 实时推理管线**

将 Depth Anything V3 模型接入 NVIDIA DeepStream 8.0 / TensorRT FP16 管线，实现实时单目深度估计。支持 USB 相机（V4L2）、视频文件、图片与 RTSP 流输入，可在桌面 GPU 与 Jetson 上运行；提供 CUDA 加速的百分位归一化 inferno 伪彩色可视化与原图并排显示。模型需先用脚本导出为 ONNX，首次运行时由 DeepStream 构建 TensorRT 引擎并缓存；DA3METRIC-LARGE 可将原始输出换算为米制深度。C++ 编译构建，另有 Docker 部署方式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- TensorRT FP16 全管线实时推理，支持 5 种 DA3 模型规格切换
- 多源输入：USB 相机/视频文件/图片/RTSP 流/通用 URI
- CUDA 核函数完成深度图伪彩色渲染，支持原图并排显示
- DA3METRIC-LARGE 可换算米制度量深度（需相机内参焦距）

## 适用场景

- 把单目深度估计接入 DeepStream 视频分析管线做实时推理
- 在 Jetson 等边缘设备上运行 DA3 深度估计
- 对比不同规格 DA3 模型的速度与显存占用

## 场景标签

`图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L3: Real-time monocular depth estimation using Depth Anything V3 as a production DeepStream 8.0 / TensorRT pipeline. Sup
> L9: - **Real-time inference**: Full TensorRT FP16 pipeline via DeepStream 8.0

## 星数曲线

```mermaid
xychart-beta
    title "Raessan/depth_anything_v3_deepstream 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-27"]
    y-axis "stars" 21 --> 24
    line [22, 23, 23]
```

2026-10-18 22 → 2026-10-27 23（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `785e0992d2ae` · [字段定义](../../DATASET.md)*
