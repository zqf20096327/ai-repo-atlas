# khlaifiabilel/autonomous-uav-visual-navigation

⭐ 23 · C++ · BSD-3-Clause · 推送 2026-08-01 · [GitHub](https://github.com/khlaifiabilel/autonomous-uav-visual-navigation) · 个人维护

**NVIDIA Redtail 历史快照：无人机/地面车的机载视觉自主导航**

NVIDIA Redtail 研究项目的历史快照与策展仓库：TrailNet Caffe S-ResNet-18 网络从单目前向相机估计车辆相对森林步道的朝向与横向偏移，px4_controller 将估计转换为 PX4 OFFBOARD 飞控指令，另含立体深度 DNN（TensorFlow/TensorRT、自定义 CUDA 插件）与 YOLO 检测触发的安全停止，全部机载运行于 Jetson 并经 TensorRT 加速。面向机器人/嵌入式研究开发者。README 明确声明为未维护的上游遗留软件（Ubuntu 16.04、ROS Kinetic、CUDA 9、Jetson TX1/TX2），不可用于生产飞行控制；仓库附 2026 现代化栈规划（ROS 2 Humble、CUDA 12.6、TensorRT 10）与 Docker 开发环境。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | BSD-3-Clause |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- TrailNet 单目视觉输出 3+3 类朝向/偏移估计并驱动 PX4 飞控
- caffe_ros 提供 TensorRT FP32/FP16/INT8 推理封装（引擎缓存、熵校准）
- 立体 DNN 含自定义 CUDA/TensorRT 插件（3D 卷积、cost volume、soft-argmax）
- 2026 现代化层提供 CUDA 12.6/TensorRT 10/ROS 2 Humble Docker 环境

## 适用场景

- 在 Jetson 平台上复现 Redtail 步道视觉导航研究
- 参考 TensorRT 机载推理与 DNN-PX4 控制集成方案
- 研究遗留机器人软件栈向 ROS 2/新 TensorRT 的迁移路径

## 场景标签

 · 领域:机器人/嵌入式视觉导航

## 证据(README 行号)

> L10: project for drones and ground vehicles: a TrailNet deep neural network estimates the vehicle's
> L11: orientation and lateral offset relative to a forest trail from a single forward camera, and a
> L111: - **TrailNet** — Caffe S-ResNet-18 model estimating trail-relative view orientation and lateral

## 星数曲线

```mermaid
xychart-beta
    title "khlaifiabilel/autonomous-uav-visual-navigation 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-27 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `e0b57d613167` · [字段定义](../../DATASET.md)*
