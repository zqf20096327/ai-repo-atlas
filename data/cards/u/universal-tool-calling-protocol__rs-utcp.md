# universal-tool-calling-protocol/rs-utcp

⭐ 59 · Rust · MPL-2.0 · 推送 2026-05-12 · [GitHub](https://github.com/universal-tool-calling-protocol/rs-utcp) · [官网](https://universal-tool-calling-protocol.github.io/rust/) · 组织维护

**UTCP 协议的 Rust 客户端：统一接口调用 12 种协议的工具**

Universal Tool Calling Protocol 的官方 Rust 实现，为开发者提供单一 UtcpClient 接口，跨 HTTP、MCP、WebSocket、gRPC、CLI、GraphQL、TCP、UDP、SSE、WebRTC、HTTP Streams 与 Text 共 12 种通信协议调用工具。基于 Tokio 异步运行时，支持从 JSON 配置与 OpenAPI 3.0 规范自动生成和注册工具、按标签的语义工具检索、多认证方式与流式响应。内置 Codemode 插件：LLM 编写 Rhai 脚本在受限沙箱中编排工具调用，含代码校验、超时与资源限制。以 Cargo crate 形式分发。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MPL-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 12 种通信协议统一为一个工具调用接口（含 MCP stdio/SSE）
- 从 OpenAPI 3.0 规范自动生成 UTCP 工具
- Codemode 编排器：LLM 生成 Rhai 脚本在沙箱中执行工具工作流
- JSON 配置驱动的 provider 加载与协议白名单限制

## 适用场景

- 为 LLM agent 提供跨协议的统一工具执行层
- 把 REST/gRPC 等异构服务聚合成单一工具调用入口
- 通过配置文件构建可扩展的应用插件系统
- 在测试中替换工具实现（如 HTTP 换 CLI）

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L5:  Universal Tool Calling Protocol Client for Rust
> L16: - **🔌 12 Communication Protocols (formerly transports)** - HTTP, MCP, WebSocket, gRPC, CLI, GraphQL, TCP, UDP, SSE,
> L20: - **🤖 LLM Integration** - Built-in Codemode orchestrator for AI-driven workflows

## 星数曲线

```mermaid
xychart-beta
    title "universal-tool-calling-protocol/rs-utcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 58 --> 60
    line [59, 59]
```

2026-10-18 59 → 2026-10-26 59（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `889167b41901` · [字段定义](../../DATASET.md)*
