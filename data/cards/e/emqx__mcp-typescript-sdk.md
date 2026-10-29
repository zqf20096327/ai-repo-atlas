# emqx/mcp-typescript-sdk

⭐ 97 · TypeScript · Apache-2.0 · 推送 2026-02-25 · [GitHub](https://github.com/emqx/mcp-typescript-sdk) · 组织维护

**TypeScript SDK：通过 MQTT 实现 MCP 协议的服务端与客户端**

面向开发者的 TypeScript 库，将 Model Context Protocol（MCP）跑在 MQTT 传输层上，同时支持浏览器（WebSocket）与 Node.js（TCP）环境并自动检测。提供 McpMqttServer（注册 tool/resource、生命周期控制）与 McpMqttClient（发现服务器、调用工具、读取资源、流式资源）两类 API，遵循 MCP v2024-11-05 规范与官方 MQTT 主题结构，用 Zod 做类型校验，可访问底层 MQTT 客户端做自定义发布订阅。要求 Node.js >= 18，另有 Python/Erlang/C/ESP32 等其他语言 SDK。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- MCP over MQTT，浏览器与 Node.js 双环境自动检测
- MCP 规范 v2024-11-05，含基于 MQTT 主题的服务器自动发现
- McpMqttServer/McpMqttClient 类 API，支持 tool/resource 注册与流式资源
- Zod schema 校验，可访问底层 MQTT 客户端自定义 pub/sub

## 适用场景

- 构建跨浏览器与 Node.js 的 MCP 服务器与客户端
- 让 AI agent 通过 MQTT 调用远程工具与资源
- 在 MQTT 基础设施上实现 MCP 服务发现与 RPC 通信

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L3: A TypeScript SDK for implementing Model Context Protocol (MCP) over MQTT, supporting both browser and Node.js enviro
> L20: - 🌐 **MQTT Transport**: Uses MQTT as the transport layer for reliable MCP communication

## 星数曲线

```mermaid
xychart-beta
    title "emqx/mcp-typescript-sdk 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 96 --> 98
    line [97, 97]
```

2026-10-18 97 → 2026-10-29 97（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `8a5d3e6758ab` · [字段定义](../../DATASET.md)*
