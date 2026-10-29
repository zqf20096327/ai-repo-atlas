# THA-Embedded-Systems-Lab/soar_ros

⭐ 21 · C++ · NOASSERTION · 推送 2026-09-18 · [GitHub](https://github.com/THA-Embedded-Systems-Lab/soar_ros) · [官网](https://tha-embedded-systems-lab.github.io/soar_ros/) · 组织维护

**将 Soar 认知架构接入 ROS 2 的接口包**

面向认知机器人开发者的 ROS 2 C++ 包：为 Soar 认知架构内核创建包装器，以非阻塞 continuous 模式运行 Soar，并提供扩展自 ROS 的 Publisher/Subscriber/Service/Client/Action Client 类，用户只需定义 ROS 数据类型与 Soar WME 数据的转换逻辑。内置 std_msgs/geometry_msgs 等常见消息转换器，支持一个内核内多个 Soar agent。依赖一个 cmake 构建的 Soar fork 版本；Action Server 尚未支持。以 colcon 构建安装，附带 Dev Container 开发环境。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 非阻塞 continuous 模式运行 Soar 内核
- Publisher/Subscriber/Service/Client/Action Client 包装类
- 内置 std_msgs、geometry_msgs 等常见 ROS 2 消息与 Soar WME 的转换器
- 单内核支持多个 Soar agent；提供 VS Code Dev Container

## 适用场景

- 在 ROS 2 机器人项目中用 Soar agent 处理话题与服务
- 让 Soar 认知架构直接消费 ROS 2 传感器/命令消息
- 构建无人机或机器人等认知机器人应用的 Soar-ROS 集成层

## 场景标签

`Agent 框架` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L10: This ROS2 package provides an interface for the Soar cognitive
> L35: - Non blocking Soar kernel

## 星数曲线

```mermaid
xychart-beta
    title "THA-Embedded-Systems-Lab/soar_ros 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-29"]
    y-axis "stars" 19 --> 22
    line [20, 21, 21]
```

2026-10-18 20 → 2026-10-29 21（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `87316a7b5084` · [字段定义](../../DATASET.md)*
