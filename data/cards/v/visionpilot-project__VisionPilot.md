# visionpilot-project/VisionPilot

⭐ 41 · Python · MIT · 推送 2026-10-27 · [GitHub](https://github.com/visionpilot-project/VisionPilot) · [官网](https://visionpilot-project.github.io/visionpilot-page/) · 组织维护

**自动驾驶仿真研究平台：BeamNG.tech 中的感知、融合与控制**

基于 Python 的模块化自动驾驶研究与原型开发系统，集成 BeamNG.tech 仿真器与 Foxglove 可视化。感知层提供多车道检测（UFLD/传统CV）、交通标志与信号灯分类检测、多类目标检测（YOLO/CNN）；传感器融合覆盖相机、LiDAR、雷达、GPS、IMU；控制层含 PID 转向、巡航控制、AEB、盲区监测。需自行下载安装 BeamNG.tech 与预训练模型，通过 YAML 配置与启动脚本运行。项目处于活跃开发阶段，尚无稳定发布；CARLA 集成仅在规划中。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- UFLD 与传统 CV 融合的多车道检测（投票机制）
- YOLO 目标检测与 CNN 交通标志/信号灯分类
- 相机/LiDAR/雷达/GPS/IMU 多传感器融合
- PID 转向、巡航控制、AEB、盲区监测等安全功能

## 适用场景

- 在仿真环境中做自动驾驶感知与控制算法研究
- 测试车道保持与紧急制动等 ADAS 功能
- 实时查看 LiDAR 点云与车辆遥测的 Foxglove 可视化

## 场景标签

`目标检测` `图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L9: A modular Python project for autonomous driving research and prototyping, fully integrated with the BeamNG.tech simu
> L16: - **Real-Time Control**: PID steering, cruise control (CC), automatic emergency braking (AEB)

## 星数曲线

```mermaid
xychart-beta
    title "visionpilot-project/VisionPilot 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 40 --> 42
    line [41, 41]
```

2026-10-18 41 → 2026-10-31 41（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `21a3ee9de4c1` · [字段定义](../../DATASET.md)*
