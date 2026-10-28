# microsoft/mcp-on-windows-samples

⭐ 30 · JavaScript · MIT · 推送 2026-06-19 · [GitHub](https://github.com/microsoft/mcp-on-windows-samples) · 组织维护

**Windows 上 MCP 服务器/客户端/主机的示例集合**

微软维护的 Model Context Protocol (MCP) Windows 平台示例项目，含 4 个样例：列出系统注册 MCP 服务器并支持手动调用工具的 JavaScript 客户端、演示 MCP host 集成并支持 MSIX 打包的 Electron 应用、可打包为 MSIX 或 MCPB (MCP Bundle) 格式的 C# 服务器，以及内嵌 MCP 服务器的 WinUI 3 应用（应用与服务器同包共享功能）。每个样例有独立的 README 说明配置与用法，需进入对应目录查看。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- JavaScript 客户端可列出 Windows 上注册的 MCP 服务器并手动调用工具
- Electron MCP host 示例支持 MSIX 打包
- C# MCP 服务器支持 MSIX 与 MCPB (MCP Bundle) 两种打包格式
- WinUI 3 应用内嵌 MCP 服务器，单包共享功能

## 适用场景

- 参考示例在 Windows 上开发自己的 MCP 服务器
- 学习 Electron/WinUI 3 应用如何集成 MCP host
- 了解 MCPB 打包格式的实现方式

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L3: This project contains sample implementations for the Model Context Protocol (MCP) on Windows.
> L7: - **mcp-client-js** - JavaScript MCP client that lists all registered MCP servers on Windows and allows manual tool 

## 星数曲线

```mermaid
xychart-beta
    title "microsoft/mcp-on-windows-samples 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 29 --> 31
    line [30, 30]
```

2026-10-18 30 → 2026-10-28 30（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `272a97b7a3a8` · [字段定义](../../DATASET.md)*
