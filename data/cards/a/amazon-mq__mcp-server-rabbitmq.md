# amazon-mq/mcp-server-rabbitmq

⭐ 42 · Python · Apache-2.0 · 推送 2026-10-27 · [GitHub](https://github.com/amazon-mq/mcp-server-rabbitmq) · 组织维护

**让 AI agent 用对话管理 RabbitMQ 的 MCP server**

基于 MCP Python SDK 实现的 RabbitMQ broker 管理 MCP 服务器，供 Claude Desktop 等 MCP 客户端中的 AI agent 通过对话执行队列/交换机管理、健康检查、集群观测与蓝绿迁移。提供 v3（61 个单操作工具）与 v4（31 个 enum 分发器，--v4 启用）两种工具布局，支持多 broker 连接、工具组按需加载、变更类工具默认关闭（--allow-mutative-tools 开启），并含 SSRF 防护、凭据剥离、JWKS 认证等安全机制。通过 PyPI 以 pip/uv 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- v3 提供 61 个工具、v4 提供 31 个 enum 分发器，工具名经 --v1-compat 兼容
- 多 broker 同时连接并可按别名切换
- 变更类工具默认关闭，需 --allow-mutative-tools 显式开启
- 支持 --tool-groups 按组加载工具与 JWKS bearer 认证的 HTTP 传输

## 适用场景

- 在 Claude Desktop 中用对话查看队列积压、创建死信交换机
- 运维通过 AI agent 执行 RabbitMQ 健康检查与集群观测
- 跨多个 broker 做定义比对与蓝绿迁移前检查

## 场景标签

 · 领域:消息中间件/LLM 工具接入

## 证据(README 行号)

> L3: A Model Context Protocol (MCP) server for RabbitMQ broker management and operations. It lets AI agents manage Rabbit
> L5: **Package:** `amq-mcp-server-rabbitmq` on PyPI · **Stack:** Python, MCP Python SDK (`mcp.server.fastmcp`), uv

## 星数曲线

```mermaid
xychart-beta
    title "amazon-mq/mcp-server-rabbitmq 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 41 --> 43
    line [42, 42]
```

2026-10-18 42 → 2026-10-29 42（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `147c26071f32` · [字段定义](../../DATASET.md)*
