# NVIDIA-ISAAC-ROS/isaac_ros_dnn_inference

⭐ 143 · C++ · Apache-2.0 · 推送 2026-09-24 · [GitHub](https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_dnn_inference) · [官网](https://developer.nvidia.com/isaac-ros-gems) · 组织维护

**NVIDIA 加速的 ROS 2 深度学习推理包，服务机器人感知**

NVIDIA Isaac ROS 生态下的 ROS 2 推理节点集合：提供 TensorRT 与 Triton 两种推理节点，将预训练 DNN 模型作用于输入 Tensor 并输出预测 Tensor，用于机器人 AI 感知；配套 DNN 编码/解码节点完成图像到 Tensor 的转换与结果还原，内置图像边界框检测与分割的编解码实现。TensorRT 针对目标硬件优化模型但不支持所有新模型，Triton 节点通过多后端（ONNX Runtime、TensorFlow、PyTorch 等）覆盖此类模型。运行于 Jetson 与 x86_64 CUDA GPU。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- TensorRT 与 Triton 双推理节点，Triton 支持 ONNX Runtime/TensorFlow/PyTorch 等多后端
- 提供图像边界框检测与分割的 DNN 编码/解码节点实现
- 基于 ROS 2 原生 rosidl::Buffer 的 CUDA 缓冲后端，减少 CPU 与加速器间数据拷贝
- 覆盖 Jetson（AGX Thor/Orin 等）与 x86_64 RTX GPU 的多平台性能数据

## 适用场景

- 在 ROS 2 机器人系统中接入预训练 DNN 做图像检测或分割
- 对比 TensorRT 与 Triton 节点在不同 NVIDIA 硬件上的推理性能
- 为自定义 DNN 模型选择可运行的推理通道

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L3: NVIDIA-accelerated DNN model inference ROS 2 packages using NVIDIA Triton/TensorRT for both Jetson and x86_64 with C
> L15: Isaac ROS DNN Inference contains ROS 2 packages for performing DNN

## 星数曲线

```mermaid
xychart-beta
    title "NVIDIA-ISAAC-ROS/isaac_ros_dnn_inference 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-28", "2026-10-29"]
    y-axis "stars" 141 --> 144
    line [142, 143, 143]
```

2026-10-18 142 → 2026-10-29 143（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `232aa418a57d` · [字段定义](../../DATASET.md)*
