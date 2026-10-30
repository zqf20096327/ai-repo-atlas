# RobotBase/robotclaw

⭐ 15 · Python · MIT · 推送 2026-03-14 · [GitHub](https://github.com/RobotBase/robotclaw) · [官网](https://pypi.org/project/robotclaw/) · 组织维护

**让 AI agent 操控 LOBOT LX 总线舵机机器人的 Python 库**

面向 OpenClaw AI agent 平台的 Python 机器人框架：将高层 AI 指令转换为真实舵机动作，兼容 LOBOT LX-16A/224/225 总线舵机，通过 USB 转 TTL 串口（115200/9600 波特率，6–8.4V ≥5A 供电）连接。提供关节级高层 API、动作示教录制与回放（存为 JSON、可调速）、CLI 诊断与示教工具，内置 OpenClaw 技能模块，纯 Python 无编译依赖。逆运动学、Dynamixel/Feetech 协议、ROS 2 桥接仍在路线图中未实现。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 关节级高层 API（如 left_hip_pitch）封装原始舵机 ID
- 动作示教：物理拖动机器人录制，存 JSON 后任意速度回放
- 内置 OpenClaw 技能，AI agent 可经自然语言控制机器人
- CLI 工具：robotclaw-scan 诊断与 robotclaw-teach 交互示教

## 适用场景

- 让 OpenClaw AI agent 通过对话控制双足机器人动作
- 教学场景中学生通过与 AI 对话学习机器人
- 快速原型验证机器人行为或迭代运动模式

## 场景标签

 · 领域:机器人/AI 具身控制

## 证据(README 行号)

> L13: **RobotClaw** is a Python robotics framework that bridges AI agents with physical robots. It turns high-level AI co
> L15: Built for the OpenClaw AI agent platform. Compatible with LOBOT LX series bus servos. Designed for makers, research

## 星数曲线

```mermaid
xychart-beta
    title "RobotBase/robotclaw 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `8489363bd9d2` · [字段定义](../../DATASET.md)*
