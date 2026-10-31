# solnera/esp32-mcpserver

⭐ 13 · C++ · MIT · 推送 2026-08-16 · [GitHub](https://github.com/solnera/esp32-mcpserver) · 个人维护

**ESP32 微控制器上的 MCP 服务器框架：让硬件向 LLM 暴露工具**

面向 ESP32 开发板的轻量 Model Context Protocol (MCP) 服务器实现，用 C++ 编写，基于 PlatformIO 与 ESPAsyncWebServer，通过 Streamable HTTP 上的 JSON-RPC 2.0 向 LLM/agent 暴露自定义工具。仅实现 tools 原语（不含 resources/prompts），支持三个 MCP 协议版本的协商、mDNS 发现、Origin 校验等 DNS-rebinding 防护。工具调用在独立 worker 任务上执行以免阻塞异步 TCP 任务；服务器不校验参数 schema，由 handler 自行检查。不支持批处理请求与 SSE。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- MCP JSON-RPC 2.0 over Streamable HTTP，支持 2025-11-25/2025-06-18/2025-03-26 三版本协商
- tools/call 在独立 worker 任务执行，含 20ms 快速路径与降级内联执行
- mDNS 发现（_mcp._tcp）与 DNS-rebinding 防护（Origin/Host/IP 校验）
- 流式 C++ schema 构建器发布 input/outputSchema（服务器不强制校验）

## 适用场景

- 让 AI agent 直接调用 ESP32 传感器/执行器等硬件工具
- 为自制智能设备构建本地优先、无需厂商云的 MCP 接入层
- 在 MCP 客户端中通过 mDNS 自动发现局域网内的 ESP32 设备

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L9: A lightweight Model Context Protocol (MCP) server implementation for the ESP32 microcontroller. This framework allow
> L13: - **Protocol Support**: MCP JSON-RPC 2.0 over Streamable HTTP, with version negotiation across `2025-11-25` (defaul

## 星数曲线

```mermaid
xychart-beta
    title "solnera/esp32-mcpserver 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-31"]
    y-axis "stars" 11 --> 14
    line [12, 13, 13]
```

2026-10-18 12 → 2026-10-31 13（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `16a377ea89ca` · [字段定义](../../DATASET.md)*
