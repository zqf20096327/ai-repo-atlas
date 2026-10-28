# tomtom215/a2a-rust

⭐ 20 · Rust · Apache-2.0 · 推送 2026-10-28 · [GitHub](https://github.com/tomtom215/a2a-rust) · [官网](https://a2a-rust.com/) · 个人维护

**Rust 版 A2A 协议 SDK：构建互操作 AI agent 的客户端与服务端**

独立实现的 Agent2Agent (A2A) v1.0.1 协议 Rust SDK，非 Google/Linux 基金会官方项目。提供 JSON-RPC 2.0、REST、WebSocket、gRPC 四种传输的客户端与服务端，覆盖 wire 类型、SSE 流式、推送通知、Agent Card 发现与 JWS 签名。服务端框架含可插拔存储（内存/SQLite/PostgreSQL）、多租户、拦截器与限流；可观测性支持 OpenTelemetry 与 Langfuse，附 Prometheus 规则和 Grafana 面板；安全上提供认证拦截器、SSRF 防护与请求加固。通过官方 TCK/ACTS 一致性套件度量并记录差距。

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

- 四种传输（JSON-RPC/REST/WebSocket/gRPC）的客户端与服务端实现
- 可插拔 TaskStore：内存/SQLite/PostgreSQL，多租户隔离
- OpenTelemetry traces/metrics/logs 导出与 Langfuse 集成，附 Grafana 面板
- Bearer/API-key/JWT 认证拦截器、SSRF 防护与限流

## 适用场景

- 在 Rust 服务中实现 A2A 协议的 agent 客户端或服务端
- 构建多租户、带认证与可观测性的 agent 服务
- 通过 SSE 流式与推送通知对接任务型 agent

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L21: A Rust implementation (no OpenSSL) of the **Agent2Agent (A2A) protocol**, written against the **v1.0.1** wire speci
> L23: Build, connect, and orchestrate AI agents with a type-safe, async-first SDK spanning four transports — JSON-RPC 2.0
> L29: **This is an independent project.** It is not affiliated with, endorsed by, or governed by the A2A project, the Lin

## 星数曲线

```mermaid
xychart-beta
    title "tomtom215/a2a-rust 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-28 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `cee8711e5419` · [字段定义](../../DATASET.md)*
