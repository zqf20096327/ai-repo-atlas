# NishanthSundaran/embodied_agent

⭐ 17 · Python · 推送 2026-04-20 · [GitHub](https://github.com/NishanthSundaran/embodied_agent) · 个人维护

**Claude 驱动的 UR3e 仿真机械臂自然语言抓放 agent**

ROS 2 Humble 包，将 UR3e + Robotiq 2F-140 + RealSense D435i 仿真环境接入 LLM 控制：用户输入英文指令，Claude Sonnet VLM 对 RGB 帧做物体定位（返回像素坐标经深度与相机内参反投影为 3D），Claude planner 通过 8 工具的 tool-use 循环分解为 pick/place/move-to 步骤，MoveIt 2 规划、Gazebo 执行，且经只读安全门查询论文的力/接近控制器状态以拒绝不安全动作。需要 Ubuntu 22.04、ROS 2 Humble、MoveIt 2、论文自有仿真包与 ANTHROPIC_API_KEY，以 colcon 工作区源码方式构建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Anthropic Messages API 上的 8 工具 agent 循环（describe_scene/pick/place/check_safety 等）
- VLM 视觉接地：像素坐标 + 深度 + 内参反投影 3D，TF2 变换到 base_link
- MoveIt 2 MoveGroup action 规划，Gazebo 中 UR3e 仿真执行
- 只读安全门：LLM 派发动作前查询力/接近控制器状态

## 适用场景

- 在仿真中用一句话指挥 UR3e 完成抓放任务
- 复用同一 ROS 2 节点接入其他 LLM 或工具调用框架
- 在带人安全约束的机械臂场景研究 LLM 具身规划

## 场景标签

 · 领域:机器人/具身智能

## 证据(README 行号)

> L7: in plain English; a Claude vision model grounds the objects it sees in the
> L8: RealSense view; a Claude planner breaks the instruction into pick / place /
> L27: - **Tool-use loop over Anthropic's Messages API** — 8 tools:


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `cec0350cc465` · [字段定义](../../DATASET.md)*
