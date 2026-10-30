# amazon-mq/mcp-amqp-transport

⭐ 21 · TypeScript · Apache-2.0 · 推送 2026-10-21 · [GitHub](https://github.com/amazon-mq/mcp-amqp-transport) · 组织维护

**让 MCP 客户端与服务端通过 AMQP 消息代理通信的 SDK**

面向开发者的 Model Context Protocol (MCP) AMQP 传输层实现，支持 AMQP 0.9.1 与 AMQP 1.0 两种协议，提供客户端/服务端传输类与 CLI 适配器，可将基于 stdio 的 MCP 实现桥接到 RabbitMQ 等消息代理上。代理负责消息持久化、自动重试、死信队列与多实例负载均衡；另提供拦截器基类用于监控、安全与缓存等消息处理。通过环境变量或直接选项配置，支持 AMQPS TLS 连接。标注为 beta。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 实现 AMQP 0.9.1 与 AMQP 1.0 双协议的 MCP 传输层
- CLI 适配器将 stdio MCP 服务/客户端桥接到 AMQP
- 消息持久化、自动重试与死信队列由 broker 处理，服务端多实例可负载均衡
- 拦截器基类支持监控、安全、缓存等自定义消息处理

## 适用场景

- 让 MCP 客户端与服务端经由 RabbitMQ 等企业消息总线通信
- 为 MCP 服务增加容错与多实例横向扩展能力
- 在消息流中插入拦截器做监控、审计或安全策略

## 场景标签

 · 领域:LLM 基础设施/MCP 工具链

## 证据(README 行号)

> L5: AMQP transport implementation for the Model Context Protocol (MCP), enabling MCP servers and clients to communicate 
> L18: - **AMQP Transport Layer**: Full implementation of MCP transport over AMQP 0.9.1 and AMQP 1.0 protocols

## 星数曲线

```mermaid
xychart-beta
    title "amazon-mq/mcp-amqp-transport 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-30 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `5c7a44fda126` · [字段定义](../../DATASET.md)*
