# ookkshirsagar/rh56dfx_description

⭐ 16 · Python · MIT · 推送 2026-02-25 · [GitHub](https://github.com/ookkshirsagar/rh56dfx_description) · 个人维护

**Inspire RH56DFX 六自由度灵巧手的 ROS 2 URDF 描述包**

为 Inspire Robotics RH56DFX 6 自由度灵巧手提供 ROS 2 URDF/xacro 模型与 ros2_control 配置，含左右手两种变体、完整 mesh 几何与关节限位。结构上含 4 指（各 2 连杆）、拇指（4 连杆）、腕部 2 关节，8 个独立控制关节加 11 个 mimic 关节实现单指令多连杆弯曲。支持 RViz 可视化（带关节滑块 GUI）、通过 xacro 宏嵌入更大机器人 URDF、JointTrajectoryController 控制。依赖 ROS 2 Jazzy（Ubuntu 24.04），经 git clone 到工作空间安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 左右手变体 xacro 宏，可嵌入任意机器人 URDF
- 8 个独立控制关节 + mimic 关节实现单驱动多连杆弯曲
- 附 RViz 可视化 launch 与预存配置，支持前缀与 world 链接选项
- 提供 ros2_control 控制器配置与 4 篇教程

## 适用场景

- 在 RViz 中检查灵巧手模型与关节运动范围
- 把 RH56DFX 手通过 xacro 宏接到自己的机械臂/人形机器人上
- 用 ros2_control 做仿真与控制集成

## 场景标签

 · 领域:机器人/硬件描述

## 证据(README 行号)

> L3: A ROS 2 URDF/xacro description package for the **Inspire Robotics RH56DFX** 6-DOF dexterous robotic hand. Supports b
> L20: - Control it with ros2_control JointTrajectoryController

## 星数曲线

```mermaid
xychart-beta
    title "ookkshirsagar/rh56dfx_description 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 17
    line [15, 16]
```

2026-10-18 15 → 2026-10-31 16（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 low · 依据 README sha `1a3fa3240b71` · [字段定义](../../DATASET.md)*
