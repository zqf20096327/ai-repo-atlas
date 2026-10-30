# 0xeb/claude-agent-sdk-dotnet

⭐ 34 · C# · MIT · 推送 2026-09-15 · [GitHub](https://github.com/0xeb/claude-agent-sdk-dotnet) · 个人维护

**面向 .NET 开发者的 Claude Agent SDK 移植库**

由个人维护的 Claude Agent SDK 非官方 .NET 移植（声明与 Anthropic 无关），追踪 Python claude-agent-sdk v0.2.82 的 API 与行为。通过调用本机 Claude Code CLI（>= 2.0.0）提供一次性 QueryAsync 请求与双向多轮客户端，支持控制协议（中断、模式切换、动态换模型）、Hook 系统、工具权限回调、进程内 MCP 服务器与沙箱配置。要求 .NET 8/9，NuGet 包标注即将发布，可从源码构建。当前版本 0.1.0，自述处于 Preview，control_cancel_request 未实现。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- QueryAsync 一次性请求与 ClaudeSDKClient 双向多轮客户端
- Hook 系统、工具权限回调与进程内 MCP 服务器支持
- 追踪 Python claude-agent-sdk v0.2.82 的 API 对齐
- 109 个测试（90 单元 + 19 集成，集成默认禁用）

## 适用场景

- 在 .NET 应用中接入 Claude Code 的 agent 能力
- 构建带工具权限控制与 Hook 的多轮对话客户端
- 以进程内 MCP 工具扩展 agent 的可调用能力

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L3: A modern .NET library for interacting with the Claude Code CLI, providing both a simple one-shot `QueryAsync()` API 
> L23: > **Parity:** This release tracks Python `claude-agent-sdk` v0.2.82. See CHANGELOG.md for details.
> L170: - **Parity:** Designed to match the Python Claude Agent SDK API, behavior, and ergonomics

## 星数曲线

```mermaid
xychart-beta
    title "0xeb/claude-agent-sdk-dotnet 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 33 --> 35
    line [34, 34]
```

2026-10-18 34 → 2026-10-30 34（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `06156d130ea2` · [字段定义](../../DATASET.md)*
