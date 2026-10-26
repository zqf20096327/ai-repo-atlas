# Black-Bee-Drones/nectar-sdk

⭐ 34 · Python · Apache-2.0 · 推送 2026-10-22 · [GitHub](https://github.com/Black-Bee-Drones/nectar-sdk) · [官网](https://black-bee-drones.github.io/nectar-sdk/) · 组织维护

**面向无人机自主系统的 ROS2 SDK：统一飞控、视觉与 AI 接口**

ROS 2 软件开发套件，为自主飞行系统提供统一接口：ArduPilot 与 PX4 飞控（经 MAVROS、直连 MAVLink 或 uXRCE-DDS，另支持 Bebop 与 Crazyflie），视觉模块（相机、ArUco、颜色、光流、MediaPipe），AI 模块（YOLO/DETR/RF-DETR/ViT 的检测、分割、分类及训练评估），室内 VSLAM 定位、Qt6 操作员界面与 ArduPilot/PX4 SITL+Gazebo 仿真。面向参赛与研究场景（IMAV/CBR/SAE），由大学团队维护，Apache 2.0 许可，支持 Humble/Jazzy/Kilted 三个 ROS 2 发行版并提供 Docker。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 固件无关的飞行控制接口，支持 ArduPilot/PX4 经 MAVROS、直连 MAVLink 或 uXRCE-DDS
- AI 模块覆盖 YOLO/DETR/RF-DETR/ViT 的检测、分割、分类及训练评估
- 室内 VSLAM 定位与视觉位姿集成
- ArduPilot/PX4 SITL + Gazebo 仿真及 Docker 运行路径

## 适用场景

- 开发跨机型的无人机飞行控制与感知任务
- 室内外竞赛任务中复用同一套代码栈并做 sim-to-real
- 在无人机上运行目标检测/分割并接入导航与避障

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L3: ROS 2 software development kit for autonomous aerial systems. Unified interfaces for flight control, computer vision
> L30: - **AI** — detection, segmentation, and classification (YOLO, DETR, RF-DETR, ViT), training, evaluation

## 星数曲线

```mermaid
xychart-beta
    title "Black-Bee-Drones/nectar-sdk 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 33 --> 35
    line [34, 34]
```

2026-10-18 34 → 2026-10-26 34（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `b0f328a84d50` · [字段定义](../../DATASET.md)*
