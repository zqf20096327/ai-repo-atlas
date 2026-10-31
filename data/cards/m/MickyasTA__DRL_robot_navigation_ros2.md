# MickyasTA/DRL_robot_navigation_ros2

⭐ 16 · Python · NOASSERTION · 推送 2026-07-12 · [GitHub](https://github.com/MickyasTA/DRL_robot_navigation_ros2) · [官网](https://www.youtube.com/watch?v=IRASuKMiOvw&t=5s) · 组织维护

**ROS 2 机器人自主导航避障项目：TD3 强化学习驱动移动机器人**

将 Twin-Delayed DDPG（TD3）深度强化学习应用于 ROS 2 Foxy + Gazebo 仿真环境中的 Pioneer 3-DX 移动机器人：以 24 维状态（20 个 LiDAR 扇区 + 目标几何 + 上一步动作）为输入，输出连续线速度/角速度命令，在未知房间内到达随机目标并避障，同时用 slam_toolbox 实时建图。附带预训练模型可一键运行，也可从头训练。面向机器人学与强化学习研究者/开发者；限制：仅仿真、训练不稳定、路径硬编码，预训练模型来自上游 ROS 1 项目。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- TD3 actor-critic 智能体从原始 LiDAR 学习连续速度控制，无手工运动规划器
- slam_toolbox 在探索同时实时构建占据栅格地图
- 附带预训练模型，一条命令运行；支持从头训练
- TensorBoard 记录损失与 Q 值曲线

## 适用场景

- 在 Gazebo 仿真中演示 DRL 机器人避障与建图
- 参考或复现 TD3 连续控制导航训练流程
- 作为 ROS 2 机器人强化学习课程/毕设项目基础

## 场景标签

`强化学习` `教程课程` · 领域:学习与行业

## 证据(README 行号)

> L3: ### Goal-driven autonomous exploration & collision avoidance for a mobile robot, powered by Deep Reinforcement Learn
> L29: A neural-network policy is trained end-to-end with the **Twin-Delayed Deep Deterministic Policy Gradient (TD3)** al
> L39: - 🤖 **Learns straight from LiDAR** — a 24-dimensional state (20 LiDAR sectors + goal geometry + last action) maps t

## 星数曲线

```mermaid
xychart-beta
    title "MickyasTA/DRL_robot_navigation_ros2 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `8bbc3d37a051` · [字段定义](../../DATASET.md)*
