# IvanMurzak/MCP-Plugin-dotnet

⭐ 20 · C# · Apache-2.0 · 推送 2026-10-30 · [GitHub](https://github.com/IvanMurzak/MCP-Plugin-dotnet) · 个人维护

**.NET 应用的 MCP 桥接插件：把方法/数据暴露为 MCP 工具**

面向 .NET 应用（Unity Editor、WPF、游戏服务器等生命周期独立的程序）的 Model Context Protocol 集成方案：应用内嵌 McpPlugin 库通过 SignalR 连接到 McpPlugin.Server 桥接网关，由 MCP 客户端（如 Claude）启动，从而与正在运行的实例交互。通过 [AiTool]/[AiPrompt]/[AiResource] 特性注册组件，基于 ReflectorNet 支持复杂类型、模糊方法匹配与 JSON schema 自动生成；传输支持 stdio 与 streamableHttp，提供 OAuth 2.1 授权、超时与会话管理配置及分析/鉴权 Webhook。以 NuGet 包与 ASP.NET Core 托管方式提供。

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

- 桥接架构：应用内插件经 SignalR（默认 8080 端口）连接到 MCP 客户端启动的网关
- 特性注册 + 程序集扫描，自动发现 Tools/Prompts/Resources
- ReflectorNet 提供复杂类型参数、模糊匹配与 JSON schema 生成
- stdio 与 streamableHttp 双传输，支持 OAuth 2.1 鉴权与分析 Webhook

## 适用场景

- 把 Unity Editor 中正在运行的场景操作暴露给 Claude 等 AI 助手
- 让 WPF 桌面应用或游戏服务器的功能作为 MCP 工具被调用
- 为 .NET 应用接入 MCP 生态且避免被 MCP 客户端反复拉起进程

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L14: **MCP Plugin for .NET** is a comprehensive solution for integrating .NET applications with the Model Context Protoc
> L28: 1. **McpPlugin (In-App)**: A lightweight library you add to your .NET application (e.g., Unity, WPF, Console). It c
> L56: - **Flexible Transport**: The bridge supports both `stdio` (for local AI agents like Claude Desktop) and `streamabl

## 星数曲线

```mermaid
xychart-beta
    title "IvanMurzak/MCP-Plugin-dotnet 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-31 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `39700b17d086` · [字段定义](../../DATASET.md)*
