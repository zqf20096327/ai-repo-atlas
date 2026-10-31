# DT42/BerryNet

⭐ 1,614 · Python · GPL-3.0 · 推送 2026-10-30 · [GitHub](https://github.com/DT42/BerryNet) · 组织维护

**树莓派等边缘设备上的深度学习智能网关**

在 Raspberry Pi 上本地运行深度学习推理的 AIoT 网关：通过 MQTT 连接摄像头客户端、AI 引擎（LiteRT 或 ONNX Runtime）与 Freeboard 仪表盘等独立组件，支持 MobileNet 分类与 SSD MobileNet/YOLOv4 目标检测模型，全程离线在设备端完成，多台边缘设备可组成分布式 AIoT 网络。结果以 MQTT 主题发布，可经数据采集器存储快照与推理结果。面向边缘计算与 IoT 开发者，支持树莓派摄像头/USB 摄像头/IP 摄像头输入，经 configure 脚本或 Docker 安装运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- MQTT 连接摄像头、AI 引擎与仪表盘的组件化架构
- LiteRT 与 ONNX Runtime 双推理引擎，MobileNet/SSD/YOLOv4 模型
- 支持树莓派摄像头、USB 摄像头与 IP 摄像头
- Freeboard Web 仪表盘展示检测图像与文本结果

## 适用场景

- 在树莓派上离线监控摄像头画面并实时检测物体
- 搭建分布式 AIoT 网络，多台边缘设备协同处理
- 存储快照与推理结果用于后续数据分析

## 场景标签

`目标检测` `推理引擎` · 领域:感知与多模态

## 证据(README 行号)

> L14: This project turns Raspberry Pi into an intelligent gateway with deep learning running on it. No internet connectio
> L22: Figure 1 shows the software architecture of the project, we use Python, MQTT and AI engines to analyze images or vi


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `7a8785083f76` · [字段定义](../../DATASET.md)*
