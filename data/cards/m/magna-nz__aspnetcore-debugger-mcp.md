# magna-nz/aspnetcore-debugger-mcp

⭐ 15 · C# · MIT · 推送 2026-09-14 · [GitHub](https://github.com/magna-nz/aspnetcore-debugger-mcp) · 个人维护

**让 AI agent 通过 MCP 调试 .NET/ASP.NET Core 应用的服务器**

MIT 许可的跨平台 MCP server，把 netcoredbg（按平台预打包，无需单独安装）经 Debug Adapter Protocol 暴露给 Claude 等 MCP 客户端，使 agent 能启动/附加调试会话、下断点、读取与修改变量、分析死锁与异常链、做服务端请求链路追踪。面向 .NET 开发者，以 dotnet 全局工具分发，需 .NET 10 SDK，支持 Linux/macOS/Windows，共提供 27 个工具。README 列有 Known limits 文档说明适配与追踪限制。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 按平台预打包 netcoredbg，安装无需额外组件
- 27 个 DAP 工具：断点、变量读写、线程/栈检查
- agent 友好组合工具：exception_autopsy、hang_analyze、请求追踪
- 跨平台 .NET 10 全局工具，一条命令安装

## 适用场景

- 让 Claude 直接运行并调试我的 ASP.NET Core 应用
- 不重启进程就修改变量验证修复假设
- 定位生产式卡死：分析线程阻塞与连接池占用
- 追踪慢请求在各调用层的耗时分布

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L15: **An MIT-licensed MCP server that lets an AI agent (Claude, etc.) debug your .NET / ASP.NET Core app — netcoredbg b
> L156: Claude (MCP client)
> L162: A protocol bridge with agent-friendly composites on top — `exception_autopsy`, `stack_explore`,

## 星数曲线

```mermaid
xychart-beta
    title "magna-nz/aspnetcore-debugger-mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `47619e8c7676` · [字段定义](../../DATASET.md)*
