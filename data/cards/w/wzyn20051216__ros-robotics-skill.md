# wzyn20051216/ros-robotics-skill

⭐ 62 · Python · MIT · 推送 2026-03-09 · [GitHub](https://github.com/wzyn20051216/ros-robotics-skill) · 个人维护 · 中文 README

**面向 ROS 1/ROS 2 开发的工程化 skill/prompt pack，适配三大编码 agent**

为 Codex、Claude Code、Gemini CLI 提供的机器人开发技能包：以 SKILL.md 原生 skill（Gemini CLI 为等价命令包）形式注入 ROS 工程规范，覆盖工作区识别、catkin/colcon 构建工作流、依赖与资源安装规则一致性检查、Nav2 导航调优、ros2_control 硬件接口、Gazebo 仿真、SLAM、MoveIt 2、ROS 1→ROS 2 迁移等主题。内置 Python 脚本做工作区检测与一致性校验，提供 18 个专题参考文档；安装途径包括 npx skills、curl 脚本与源码安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- ROS 1 / ROS 2 / mixed 工作区识别与 catkin/colcon 构建工作流
- package.xml、CMakeLists、资源安装规则一致性检查（含深度 CMake 分析）
- Nav2、ros2_control、Gazebo、SLAM、MoveIt 2 等 18 个专题参考文档
- 附带工作区检测与一致性校验 Python 脚本

## 适用场景

- 在 Codex/Claude Code/Gemini CLI 中获得 ROS 专项工程规范
- 让 AI 助手按正确顺序排查 TF、时间戳、frame 等联调问题
- 规划 ROS 1 到 ROS 2 的渐进迁移

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L7: 一个面向 **ROS 1 / ROS 2 机器人开发、迁移与联调** 的开源工程化 skill / prompt pack，适配 **Codex、Claude Code、Gemini CLI**。
> L135: ├── SKILL.md
> L156: - ROS 1：`references/ros1-catkin.md`

## 星数曲线

```mermaid
xychart-beta
    title "wzyn20051216/ros-robotics-skill 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 61 --> 63
    line [62, 62]
```

2026-10-18 62 → 2026-10-24 62（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `2126e6f72f42` · [字段定义](../../DATASET.md)*
