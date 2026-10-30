# Corning-AI/embedded-linux

⭐ 16 · Python · MIT · 推送 2026-06-03 · [GitHub](https://github.com/Corning-AI/embedded-linux) · 个人维护

**i.MX 8M Plus 上的嵌入式 Linux 全栈项目：NPU 实时目标检测**

面向嵌入式开发者的 NXP i.MX 8M Plus EVK 全栈工程：从 Yocto BSP 构建、内核模块（hello/chardev/BME280 I2C 驱动）、设备树、WiFi/BT 配置，到基于 TFLite INT8 + VX Delegate 的 NPU 实时目标检测与姿态估计（MobileNet SSD v2 检测 11ms、MoveNet 姿态 13ms）。数据通路为 OV5640 MIPI 摄像头 → GStreamer → NPU 推理 → HDMI 叠加显示，另含 AS7263 NIR 组织血氧监测仪表盘。构建需 Ubuntu 22.04 主机约 2 小时，依赖特定硬件 EVK 板。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- NPU 上 MobileNet SSD v2 INT8 检测达 11ms/帧，9 FPS 端到端
- OV5640 MIPI-CSI2 → GStreamer 零拷贝 → NPU → HDMI 完整数据通路
- 三个递进式内核模块示例（hello/chardev/BME280 I2C 驱动）
- AS7263 NIR 传感器实时组织血氧指数监测与 GTK3 仪表盘

## 适用场景

- 在 i.MX 8M Plus 上部署实时目标检测与姿态估计
- 学习嵌入式 Linux bring-up：Yocto、设备树、内核驱动、V4L2
- 边缘设备上的 NIR 光谱生理监测

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L11: Real-time object detection on the 2.3 TOPS NPU: OV5640 camera → MobileNet SSD v2 (INT8) → bounding boxes on HDMI, 1
> L19: OV5640 (MIPI-CSI2) → ISI DMA → GStreamer appsink → TFLite INT8 + VX Delegate → overlay → HDMI
> L32: app/camera-detect/         Detection + pose estimation app (Python, GStreamer, TFLite)

## 星数曲线

```mermaid
xychart-beta
    title "Corning-AI/embedded-linux 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-30"]
    y-axis "stars" 14 --> 17
    line [15, 16, 16]
```

2026-10-18 15 → 2026-10-30 16（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `6aeda01cdb46` · [字段定义](../../DATASET.md)*
