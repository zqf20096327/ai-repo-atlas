# automatika-robotics/kompass

⭐ 38 · Python · MIT · 推送 2026-10-22 · [GitHub](https://github.com/automatika-robotics/kompass) · [官网](https://emos.automatikarobotics.com) · 组织维护

**机器人开发者的 GPU 加速事件驱动导航栈**

Kompass 是 EMOS（Embodied Operating System）的导航层，面向真实环境中的移动机器人。以 C++ 实现（kompass-core）、支持 CPU 或 GPU（GPGPU）执行，包含路径规划（OMPL）、多种控制算法（DWA/Stanley/Pure Pursuit/DVZ）、局部建图、安全限制与回归测试组件。用户以 Python 编写 Recipe，将事件与动作连线，运行时可切换控制器、调整安全限制而无需重启。ML 模型输出可触发事件并与 EmbodiedAgents 共用组件框架。限制：pip 安装为 CPU only，GPU 安装需脚本；ROS 2 apt 包要求 Humble 或更新。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 事件驱动 Recipe：一行事件-动作对，运行时重配置无需重启
- C++ 核心支持 CPU/任意 GPU（GPGPU，非单厂商工具链）
- 规划/控制/感知/安全/测试五类组件，支持差速、阿克曼、全向、足式底盘
- 每个 Recipe 自动生成 Web UI（FastHTML on Sugarcoat）

## 适用场景

- 移动机器人在有人走动的动态环境中做导航与避障
- 巡逻任务中根据传感器或检测模型输出实时切换行为
- 在 Jetson、AMD 板或纯 CPU 上部署同一份导航 Recipe

## 场景标签

 · 领域:机器人/导航软件栈

## 证据(README 行号)

> L15: **Kompass** is the navigation layer of EMOS, the Embodied Operating System. An event-driven navigation system, made
> L48: - **ML models as first-class citizens.** Any model output can drive an event — a detection, a tracked target, a dec
> L152: - **Kompass**: navigation. GPU-accelerated planning and control.

## 星数曲线

```mermaid
xychart-beta
    title "automatika-robotics/kompass 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 37 --> 39
    line [38, 38]
```

2026-10-18 38 → 2026-10-25 38（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `89bd4411a9d7` · [字段定义](../../DATASET.md)*
