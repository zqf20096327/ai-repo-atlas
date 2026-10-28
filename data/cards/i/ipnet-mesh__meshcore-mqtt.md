# ipnet-mesh/meshcore-mqtt

⭐ 46 · Python · GPL-3.0 · 推送 2025-11-22 · [GitHub](https://github.com/ipnet-mesh/meshcore-mqtt) · [官网](https://ipnt.uk) · 组织维护

**将 MeshCore 设备接入 MQTT 的桥接服务，供 IoT 集成使用**

连接 MeshCore 网络设备与 MQTT broker 的桥接服务：通过 TCP、Serial、BLE 三种方式连接设备，将消息、电量、遥测等事件发布到 MQTT 主题，并支持经 MQTT 主题发送消息、查询设备、路由追踪等命令，实现双向通信。采用 Inbox/Outbox 双 worker 异步架构，提供 TLS、限流、健康检查与自动重连；配置支持 JSON/YAML/环境变量/命令行。README 中无 AI 相关功能描述（主题标签含 ai/claude-code 但正文未体现）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- TCP/Serial/BLE 三种方式连接 MeshCore 设备
- MeshCore 事件与 MQTT 主题的双向映射（发布+命令）
- Inbox/Outbox 异步架构与限流、健康检查、自动重连
- 多阶段 Alpine Docker 镜像（GHCR 预构建），非 root 运行

## 适用场景

- 把 MeshCore 网络的消息和遥测接入 Home Assistant 等 MQTT 平台
- 通过 MQTT 远程向 MeshCore 节点发消息或查询状态
- 对 mesh 网络做事件监控与路由诊断

## 场景标签

 · 领域:IoT/消息桥接

## 证据(README 行号)

> L10: A robust bridge service that connects MeshCore devices to MQTT brokers, enabling seamless integration with IoT plat
> L15: - **Multiple Connection Types**: Support for TCP, Serial, and BLE connections to MeshCore devices
> L213: The bridge provides full bidirectional communication between MQTT and MeshCore devices. Using the configured topic

## 星数曲线

```mermaid
xychart-beta
    title "ipnet-mesh/meshcore-mqtt 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 45 --> 47
    line [46, 46]
```

2026-10-18 46 → 2026-10-28 46（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 low · 依据 README sha `801343b215d8` · [字段定义](../../DATASET.md)*
