# kalashjain23/ControllerGPT

⭐ 46 · Python · Apache-2.0 · 推送 2026-05-14 · [GitHub](https://github.com/kalashjain23/ControllerGPT) · 个人维护

**用自然语言指令通过 ChatGPT 控制 ROS2 机器人的控制器**

面向 ROS2 机器人开发者的文本指令控制器：通过 rosbridge_suite 以 WebSocket 连接 ROS2，用 LangChain 接入 ChatGPT，用户指定话题与目标后由模型填充自定义消息/服务格式并发布执行。需自备 OpenAI API key，以源码方式克隆安装并在虚拟环境装依赖；支持按指定格式添加自定义 .msg/.srv 接口。示例以 Turtlesim 演示，项目受 ChatGPT_TurtleSim 启发。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自然语言目标转为 ROS2 话题发布与服务调用
- rosbridge_suite WebSocket 接口连接 ROS2
- LangChain + ChatGPT 生成消息/服务参数
- 支持按格式添加自定义 .msg/.srv 接口

## 适用场景

- 我在 ROS2 机器人上用一句话下达运动或服务调用指令
- 让 ChatGPT 填充消息格式并发布到指定话题
- 为自己的机器人消息和服务类型扩展控制接口

## 场景标签

 · 领域:机器人/具身智能

## 证据(README 行号)

> L2: **An AI controller that uses text prompts to control your robot.**
> L4: ROS2 is interfaced via WebSockets through rosbridge_suite.
> L5: ***LangChain*** is used to create an interface with ChatGPT.

## 星数曲线

```mermaid
xychart-beta
    title "kalashjain23/ControllerGPT 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 45 --> 47
    line [46, 46]
```

2026-10-18 46 → 2026-10-25 46（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `cbb65c79f64e` · [字段定义](../../DATASET.md)*
