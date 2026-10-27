# Tencent-Hunyuan/Hy-Embodied-RoboFusion

⭐ 35 · C · 推送 2026-05-15 · [GitHub](https://github.com/Tencent-Hunyuan/Hy-Embodied-RoboFusion) · 组织维护 · 中文 README

**面向机器人控制系统的 UDP 通信协议规范文档**

腾讯 RoboticsX 相关仓库，内容为 Robo Fusion 协议 1.0 版的规范文档：基于 UDP 的应用层通信协议，面向机器人控制系统，定义 PDO/SDO 两种通信模式、7 种电机控制模式（MIT/PP/PV/PT/CSP/CSV/CST）、IMU/力传感器/编码器数据结构、端口分配、小端字节序与 1 字节对齐规则，目标编译环境为 STM32H755 上的 CubeIDE/CubeMX。README 未提供安装命令或可运行代码入口，仅含协议数据结构与规范说明及联系方式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- PDO 周期实时数据与 SDO 请求-响应配置两种通信模式
- 支持 7 种电机控制模式（MIT/PP/PV/PT/CSP/CSV/CST）
- 定义 IMU、力传感器、编码器数据结构与端口分配（9110/8880/8887/8884）
- 目标硬件为 STM32H755，建议通信频率 1kHz

## 适用场景

- 机器人电机控制与传感器数据采集的通信实现参考
- 嵌入式开发者在 STM32 平台上对接该协议的寄存器与数据格式查阅

## 场景标签

 · 领域:机器人/嵌入式通信协议

## 证据(README 行号)

> L10: Robo Fusion 协议是一个基于UDP的应用层通信协议，专为机器人控制系统设计，支持电机控制、传感器数据采集和设备状态监控。协议采用结构化的二进制数据格式，支持多种设备类型和数据交换模式。
> L376: - 芯片型号：STM32H755

## 星数曲线

```mermaid
xychart-beta
    title "Tencent-Hunyuan/Hy-Embodied-RoboFusion 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 34 --> 36
    line [35, 35]
```

2026-10-18 35 → 2026-10-27 35（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 low · 依据 README sha `536032d16934` · [字段定义](../../DATASET.md)*
