# Yutarop/turtlebot3_agent

⭐ 20 · Python · MIT · 推送 2025-11-04 · [GitHub](https://github.com/Yutarop/turtlebot3_agent) · 个人维护

**用 LLM 自然语言控制 TurtleBot3 机器人的 ROS 2 agent**

面向 ROS 2 开发者的机器人控制 agent：接收自然语言指令，通过可调用的工具函数驱动 TurtleBot3 完成移动、转向、读取位置状态、操作摄像头与 LiDAR 扫描等任务。基于 ROS 2 Humble 构建（其他发行版兼容性未保证），需 Python 3.10+，通过配置环境变量设定机器人型号与 LLM 模型名，可选接入 LangSmith 追踪调试。工具目录开放自定义扩展。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自然语言指令映射为机器人运动/传感器工具调用
- 工具集覆盖运动控制、状态读取、摄像头与 LiDAR 操作
- 支持配置不同 LLM 模型（默认 gpt-4o-mini）
- 可选 LangSmith 追踪 agent 行为

## 适用场景

- 机器人开发者用自然语言指挥 TurtleBot3 执行移动与导航任务
- 在 ROS 2 Humble 环境中实验 LLM agent 控制实体机器人
- 自定义扩展工具目录，为 agent 增加新能力

## 场景标签

`AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L2: `TurtleBot3 Agent` enables intuitive control of a TurtleBot3 robot using natural language. It interprets user instru
> L72: `TurtleBot3 Agent` utilizes the tools implemented in the `tools/` directory as callable functions that it can invok

## 星数曲线

```mermaid
xychart-beta
    title "Yutarop/turtlebot3_agent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-28 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `465d0a27cc26` · [字段定义](../../DATASET.md)*
