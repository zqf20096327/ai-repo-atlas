# NVIDIA-ISAAC-ROS/isaac_ros_object_detection

⭐ 205 · C++ · Apache-2.0 · 推送 2026-09-22 · [GitHub](https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_object_detection) · [官网](https://developer.nvidia.com/isaac-ros-gems) · 组织维护

**NVIDIA GPU 加速的 ROS 2 图像目标检测包集合**

Isaac ROS Object Detection 提供 ROS 2 节点包，在输入图像上用 GPU 加速模型做边界框目标检测，支持 RT-DETR、DetectNet、YOLOv8、Grounding DINO 四种架构，需自备对应架构的训练模型。输入图像经 isaac_ros_dnn_image_encoder 编码为张量，输出含类别的检测数组；利用 ROS 2 原生 rosidl::Buffer 与 CUDA 缓冲后端减少 CPU 与加速器内存间的拷贝。README 给出多款 Jetson、DGX Spark 与 x86_64 RTX GPU 上的性能表，详细安装使用指引在 Isaac ROS 文档站。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 四种检测架构：RT-DETR / DetectNet / YOLOv8 / Grounding DINO
- 基于 rosidl::Buffer CUDA 后端减少大负载拷贝
- 提供从 AGX Thor 到 RTX 5090 多平台的 fps/延迟性能表
- 附带 DNN 图像编码器将图像处理为张量输入

## 适用场景

- 机器人 ROS 2 感知管线中定位图像内物体及其位置
- 在 Jetson 边缘设备上运行 GPU 加速目标检测
- 对比不同检测模型在自有硬件上的推理性能

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L10: Isaac ROS Object Detection contains ROS 2 packages to perform object
> L12: `isaac_ros_rtdetr`, `isaac_ros_detectnet`, `isaac_ros_yolov8`, and `isaac_ros_grounding_dino` each provide a method
> L13: classification using bounding boxes with an input image. Classification

## 星数曲线

```mermaid
xychart-beta
    title "NVIDIA-ISAAC-ROS/isaac_ros_object_detection 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-28"]
    y-axis "stars" 203 --> 206
    line [204, 205, 205]
```

2026-10-18 204 → 2026-10-28 205（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `5eb5d53bbd51` · [字段定义](../../DATASET.md)*
