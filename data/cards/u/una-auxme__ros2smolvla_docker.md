# una-auxme/ros2smolvla_docker

⭐ 23 · Apache-2.0 · 推送 2026-08-27 · [GitHub](https://github.com/una-auxme/ros2smolvla_docker) · [官网](https://una-auxme.github.io/en/projects/ros2smolvla/) · 组织维护

**在 UR 协作机器人上运行 LeRobot/SmoLVLA 的 Docker 容器套件**

由三个 Docker 容器组成的机器人学习运行环境：ROS2 驱动容器（默认 UR10e + Robotiq Hand-E 夹爪）、Gazebo 仿真容器、以及与 ROS2 互联的 LeRobot 框架容器。支持游戏手柄遥操作录制数据集、基于 lerobot/smolvla_base 微调策略、经 Hugging Face 加载模型并在真机或仿真中执行；通过 Cartesian 速度/位置转换层与相机桥接包连接 LeRobot 与 ROS2。要求 NVIDIA GPU（CUDA 12.6.3）、NVIDIA Container Toolkit，在 Ubuntu 24.04 + ROS2 Jazzy 上测试。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三容器架构：ROS2 驱动 + Gazebo 仿真 + LeRobot 框架
- 手柄 6DOF 遥操作录制数据集、lerobot-train 微调 SmolVLA 策略
- ROS2↔LeRobot 转换层（Twist 速度→笛卡尔位置）与相机桥接包
- docker compose 按 sim/real profile 构建运行，支持 GPU 集成

## 适用场景

- 在 UR10e 真机或 Gazebo 仿真中录制机器人操作数据集
- 微调 SmolVLA 视觉-语言-动作模型并部署到机械臂执行
- 搭建 VLA 模型研究到工业级轻量机器人部署的完整流程

## 场景标签

`微调` · 领域:训练与推理

## 证据(README 行号)

> L3: This repository contains the Docker container definitions for running the LeRobot
> L6: The project is divided into three Docker containers:
> L74: lerobot-train \

## 星数曲线

```mermaid
xychart-beta
    title "una-auxme/ros2smolvla_docker 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-30 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `d9d975c272e2` · [字段定义](../../DATASET.md)*
