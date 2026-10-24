# navado/ESP32MCPServer

⭐ 64 · C++ · MIT · 推送 2026-03-08 · [GitHub](https://github.com/navado/ESP32MCPServer) · 个人维护

**跑在 ESP32 上的 MCP 服务器，向 AI agent 暴露传感器与总线数据**

在 ESP32（及 nRF52840 传感器-only 模式）上运行的 Model Context Protocol 服务器，通过 WebSocket 上的 JSON-RPC 2.0 向 AI 助手与自动化工具暴露硬件数据：自动扫描并读取 BME280/MPU6050 等 I2C 传感器，解析 NMEA 0183 GPS/海洋数据，解码 NMEA 2000 与 OBD-II CAN 帧，并提供环形缓冲的总线历史查询、订阅推送与网页仪表盘。面向需要用 AI agent 直接读取物理硬件的嵌入式开发者；需 PlatformIO 编译烧录，nRF52840 目标无 WiFi 与 MCP 服务。

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

- MCP 协议：WebSocket + JSON-RPC 2.0，支持资源发现与订阅推送
- 解码 NMEA 0183/2000 与 OBD-II（60+ PID），读取 6 种 I2C 传感器驱动
- CAN/NMEA/OBD-II 持久化环形缓冲历史，可通过 MCP 查询
- mDNS + UDP 能力广播自动发现，内置浏览器仪表盘

## 适用场景

- 让 AI agent 通过 MCP 读取船载 GPS/深度/风速等 NMEA 数据
- 用对话式工具查询 OBD-II 车辆诊断数据
- 远程监控 I2C 传感器的实时读数与历史指标

## 场景标签

 · 领域:嵌入式 IoT/AI 硬件接口

## 证据(README 行号)

> L5: A Model Context Protocol (MCP) server running on ESP32 (and Nordic nRF52840 in sensor-only mode), exposing real-worl
> L7: Connect an AI agent directly to your hardware: query I2C sensors, parse NMEA 0183 GPS/marine data, decode NMEA 2000 

## 星数曲线

```mermaid
xychart-beta
    title "navado/ESP32MCPServer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 63 --> 65
    line [64, 64]
```

2026-10-18 64 → 2026-10-24 64（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `82747dc5dad9` · [字段定义](../../DATASET.md)*
