# SamFold/Mcp.Net

⭐ 37 · C# · MIT · 推送 2026-03-18 · [GitHub](https://github.com/SamFold/Mcp.Net) · 个人维护

**给 .NET 开发者的 MCP 协议实现：构建 AI 工具服务端与客户端**

用 C#/.NET 实现 Anthropic 的 Model Context Protocol，拆分为 Core/Server/Client 三个 NuGet 包：服务端支持 SSE 与 stdio 两种传输、动态工具发现、JSON Schema 参数校验、资源与提示目录、elicitation 流程；客户端可连接 MCP 服务器并与 OpenAI/Anthropic 模型交互。内置 OAuth 2.1 参考流（动态注册+PKCE），支持接入 Auth0/Entra ID/Supabase/Clerk 等身份提供方，可嵌入 ASP.NET Core。当前版本 0.9.0，部分高级内容类型仍在开发中。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- SSE 与 stdio 双传输，支持浏览器与 CLI 场景
- OAuth 2.1 参考流（动态注册、PKCE、refresh token 轮换）与外部身份提供方接入
- 动态工具发现与 JSON Schema 参数校验
- elicitation（服务器+客户端）与控制台 UX 辅助

## 适用场景

- 为 .NET 应用构建提供工具给 AI 模型的 MCP 服务器
- 开发连接 MCP 服务器的客户端并与 LLM 集成
- 在 ASP.NET Core 应用中嵌入 MCP 服务并接入企业身份认证

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L2:  Connect your apps to AI models with a standardized protocol for tools, resources, and prompts
> L9: Mcp.Net is a .NET implementation of the Model Context Protocol (MCP) - a standardized way for apps to talk to AI mod
> L110: - **Mcp.Net.Core**: Models, interfaces, and base protocol components
> L112: - **Mcp.Net.Client**: Client libraries for connecting to MCP servers

## 星数曲线

```mermaid
xychart-beta
    title "SamFold/Mcp.Net 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 36 --> 38
    line [37, 37]
```

2026-10-18 37 → 2026-10-31 37（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `fa34b0b1c8f7` · [字段定义](../../DATASET.md)*
