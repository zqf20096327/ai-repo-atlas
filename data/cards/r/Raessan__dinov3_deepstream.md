# Raessan/dinov3_deepstream

⭐ 28 · C++ · Apache-2.0 · 推送 2026-02-05 · [GitHub](https://github.com/Raessan/dinov3_deepstream) · 个人维护

**DINOv3 多任务视觉推理的 DeepStream C++/CUDA 应用**

基于 Meta DINOv3 骨干网络与 NVIDIA DeepStream/TensorRT 的 C++/CUDA 实时视觉应用：骨干特征仅计算一次，由轻量任务头共享完成目标检测、语义分割、单目深度估计与光流估计四项任务，各任务以 GStreamer probe 实现后处理与可视化。支持 V4L2 相机、视频文件、RTSP 流等输入，可通过命令行开关启用/禁用各任务。需自行构建并获取骨干权重（导出 ONNX/TensorRT），任务头 ONNX 模型随仓库附带；依赖 CUDA、DeepStream SDK 与 GStreamer，提供 Docker Compose 部署方式。作者声明目标是即插即用工具包而非超越 SOTA。

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

- DINOv3 骨干特征一次计算、四任务头共享复用
- 同时运行检测/分割/深度/光流，可逐任务开关
- GStreamer/DeepStream 流水线，CUDA kernel 做后处理
- Docker Compose + NVIDIA Container Toolkit 部署

## 适用场景

- 在边缘设备或 GPU 视频流水线上做多任务实时视觉分析
- 接入 RTSP/摄像头/视频文件流式处理并可视化多任务结果
- 机器人或生产环境的低延迟视频分析部署

## 场景标签

`目标检测` `图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L3: This repository provides a high-performance C++/CUDA application for performing multiple vision tasks—such as object
> L13: - **Real-time multi-task inference**: Run detection, segmentation, depth, and optical flow simultaneously

## 星数曲线

```mermaid
xychart-beta
    title "Raessan/dinov3_deepstream 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 27 --> 29
    line [28, 28]
```

2026-10-18 28 → 2026-10-31 28（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `0834640740dd` · [字段定义](../../DATASET.md)*
