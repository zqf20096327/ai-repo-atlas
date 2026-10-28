# prismworks-ai/prism-mcp-rs

⭐ 46 · Rust · MIT · 推送 2026-10-27 · [GitHub](https://github.com/prismworks-ai/prism-mcp-rs) · [官网](https://prismworks.ai) · 组织维护

**构建 MCP 客户端/服务端的异步 Rust SDK**

面向开发者的 Model Context Protocol（MCP）Rust SDK，用于构建 MCP 客户端与服务端。原生实现 MCP 2026-07-28 无状态生命周期，并兼容 MCP 2025-11-25 有状态初始化；支持 STDIO、HTTP、WebSocket、SSE 通知、HTTP/2 等传输，提供 OAuth 客户端原语、细粒度 RBAC 与限流、TLS 1.3 mTLS、OpenTelemetry 追踪、端点故障转移与原生插件等可选特性。CI 对上游 MCP 一致性测试运行验收。安装方式为 crates.io 依赖引入，MSRV 1.89，MIT 许可。

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

- 原生 MCP 2026-07-28 无状态生命周期，兼容 2025-11-25
- STDIO/HTTP/WebSocket/SSE/HTTP2 多传输与 Tasks 扩展实现
- 可选 RBAC、令牌桶限流、TLS 1.3 mTLS、OTLP 追踪与端点故障转移
- CI 运行上游 MCP 一致性 referee 验收（30/30、29/29 通过）

## 适用场景

- 用 Rust 实现 MCP 服务端供 AI 助手调用工具
- 构建连接 MCP 服务器的客户端应用
- 为生产 MCP 服务加认证、限流与可观测性控制

## 场景标签

 · 领域:AI 基础设施/MCP 协议 SDK

## 证据(README 行号)

> L15: `prism-mcp-rs` is an async Rust SDK for building Model Context Protocol (MCP) clients and servers. Version 3 implem
> L5: The reusable Rust connectivity and generic request-control substrate for MCP clients and servers. See the current st

## 星数曲线

```mermaid
xychart-beta
    title "prismworks-ai/prism-mcp-rs 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 45 --> 47
    line [46, 46]
```

2026-10-18 46 → 2026-10-28 46（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `6faf10fec87f` · [字段定义](../../DATASET.md)*
