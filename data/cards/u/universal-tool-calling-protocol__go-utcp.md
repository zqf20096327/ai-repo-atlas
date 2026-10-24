# universal-tool-calling-protocol/go-utcp

⭐ 125 · Go · MPL-2.0 · 推送 2026-08-27 · [GitHub](https://github.com/universal-tool-calling-protocol/go-utcp) · [官网](https://www.utcp.io/) · 组织维护

**UTCP 协议的 Go 实现：统一客户端抽象发现与调用异构工具**

Universal Tool Calling Protocol 的官方 Go 客户端库：在 HTTP、gRPC、GraphQL、WebSocket、SSE、TCP/UDP、WebRTC、CLI、MCP、本地文本模板等多种传输之上提供统一的工具发现、描述、搜索、调用与流式调用 API，以限定名 provider.tool 分发调用。面向需要把 agent、服务工作流引擎或自动化运行时接入多种工具而无需逐传输耦合的应用。含 CodeMode 插件用类 Go 程序组合多次工具调用，支持变量替换与 .env 加载。要求 Go 1.25 及以上。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MPL-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 统一工具发现/调用/流式调用 API 覆盖 12 种 provider 类型
- MCP 服务器作为可接入的 provider 传输之一
- CodeMode 插件支持循环、分支与多步工具编排
- 运行时动态注册/注销 provider 与变量/密钥替换

## 适用场景

- 为 AI agent 构建跨多种传输的统一工具调用层
- 通过单一 Go API 调用 HTTP、gRPC、MCP、CLI 等异构工具
- 用 CodeMode 编排多步工具调用逻辑

## 场景标签

 · 领域:AI agent 工具调用基础设施

## 证据(README 行号)

> L9: `go-utcp` is the Go implementation of the Universal Tool Calling Protocol (UTCP). It provides a single client-side a
> L29: This makes UTCP useful as infrastructure for AI agents, automation platforms, developer tools, integration services

## 星数曲线

```mermaid
xychart-beta
    title "universal-tool-calling-protocol/go-utcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 124 --> 126
    line [125, 125]
```

2026-10-18 125 → 2026-10-24 125（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `383af441e9fb` · [字段定义](../../DATASET.md)*
