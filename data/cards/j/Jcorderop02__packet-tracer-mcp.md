# Jcorderop02/packet-tracer-mcp

⭐ 14 · TypeScript · MIT · 推送 2026-07-13 · [GitHub](https://github.com/Jcorderop02/packet-tracer-mcp) · 个人维护

**控制 Cisco Packet Tracer 9 的 MCP 服务器，供 Claude 等 AI 客户端搭建网络拓扑**

用 TypeScript/Bun 编写的 Model Context Protocol 服务器，通过自带的 .pts 扩展与本地 HTTP 桥接调用 Packet Tracer 9 的原生 IPC API，向 MCP 客户端暴露 57 个工具：设备增删、链路创建、CLI 执行、VLAN/BGP/OSPF/NAT/VoIP/IPv6/无线等配方编排、快照持久化与截图。采用 canvas-first 设计：无内存计划对象，配方执行前重读画布快照以保证幂等。需 Packet Tracer 9.0 与 Bun >=1.2，版本 0.1.0，作者自述为实验性项目、不建议生产使用；.pkz 格式在 PT 9.0.0.0810 下不工作，wifi_lan 配方存在功能限制。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 57 个 MCP 工具覆盖设备编辑、CLI、模拟操作、快照持久化等域
- canvas-first 设计：配方执行前重读画布快照，操作幂等
- 通过本地 HTTP 桥接与 .pts 扩展调用 PT 9 原生 IPC API，绕过 .pta 签名限制
- pt_generate_configs 可离线生成 IOS CLI 配置用于文档或真实硬件

## 适用场景

- 用 Claude Code 等 MCP 客户端自动搭建并验证 Cisco 网络实验拓扑
- CCNA/CCNP 学习与教学中自动生成路由、VLAN、NAT 等实验环境
- 对运行中的 Packet Tracer 画布做读取、巡检与快照比对

## 场景标签

 · 领域:网络仿真/AI 工具生态

## 证据(README 行号)

> L18: Servidor Model Context Protocol para controlar **Cisco Packet Tracer 9.0**
> L20: bridge HTTP local y desde ahí el servidor MCP llama a la API IPC nativa
> L21: de PT para crear topologías, configurar routers, lanzar simulaciones, etc.

## 星数曲线

```mermaid
xychart-beta
    title "Jcorderop02/packet-tracer-mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `4b1f3545d781` · [字段定义](../../DATASET.md)*
